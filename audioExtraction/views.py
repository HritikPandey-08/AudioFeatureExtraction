from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import AudioUploadForm
from .models import AudioFeatures
from django.http import StreamingHttpResponse
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from pydub import AudioSegment
from django.contrib import messages
import os
import math


def convert_file_size_bytes_to_readable(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_names = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    size = round(size_bytes / math.pow(1024, i), 2)
    return f"{size} {size_names[i]}"


def get_audio_duration(audio_file):
    try:
        audio_format = audio_file.name.split('.')[-1].lower()
        
        if audio_format == 'mp3':
            audio = MP3(audio_file)
            return audio.info.length  # Duration in seconds
        elif audio_format == 'flac':
            audio = FLAC(audio_file)
            return audio.info.length  # Duration in seconds
        else:
            # Use pydub for other formats (requires pydub and ffmpeg)
            audio = AudioSegment.from_file(audio_file)
            return len(audio) / 1000  # Duration in seconds
    except Exception as e:
        print(f"Error while getting audio duration: {e}")
        return None


def audio_extraction(request):
    """
    View function to handle audio extraction and display.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The response containing the rendered template.
    """
    # here i am using default user id (the user that i have created)
    # you can user your user id 
    audio_features = AudioFeatures.objects.filter(user_id=6)

    # Preprocess the data
    # using this to display data
    processed_audio_features = []
    total_duration = 0  # Initialize total duration
    for audio_feature in audio_features:
        audio_duration = get_audio_duration(audio_feature.audio)  # Calculate the duration
        if audio_duration is not None:  # Check for None to avoid errors
            processed_audio_feature = {
                'id' : audio_feature.pk,
                'title': audio_feature.title,
                'dateOfUpload': audio_feature.dateOfUpload,
                'size': convert_file_size_bytes_to_readable(audio_feature.size),
                'extension': audio_feature.extension,
                'duration': audio_duration, # Assign the duration
                'audio':audio_feature.audio
            }
            processed_audio_features.append(processed_audio_feature)

            # Accumulate total duration
            total_duration += audio_duration 
    
    # Calculate total duration in minutes
    total_duration_minutes = total_duration / 60
    if request.method == 'POST':
        form = AudioUploadForm(request.POST, request.FILES)
        if form.is_valid():

            # Get the user (Default user)
            user = get_user_model().objects.get(id=6)  

            
            # Extract audio features
            audio_file = request.FILES['audio']

             # Calculate total duration
            new_audio_duration = get_audio_duration(audio_file)
            if new_audio_duration is not None:
                total_duration += new_audio_duration  # Update total duration
                total_duration_minutes = total_duration / 60  # Convert to minutes

            # check duration
            if total_duration_minutes > 10:
                messages.warning(request, "Total duration of your files exceeds 10 minutes.")
    
            audio_feature = form.save(commit=False)

            # Assign the duration
            audio_feature.duration = new_audio_duration  
            
            # Get file size
            audio_feature.size = audio_file.size 
            
            # Get file extension
            audio_extension = os.path.splitext(audio_feature.audio.name)[1][1:]
            audio_feature.extension = audio_extension
            
            # Get the default user
            audio_feature.user = user 

            audio_feature.save()
            return redirect('audio_extraction')  # Redirect to a same page
    else:
        form = AudioUploadForm()
    
    return render(request, 'upload_audio_file.html', {'form': form,'audio_features': processed_audio_features,'total_duration_minutes': total_duration_minutes})

# using streaming for audio 
# because getting broken pipe error
def stream_audio(request, audio_id):
    """
    Stream the audio file to the client.

    Args:
        request (HttpRequest): The HTTP request object.
        audio_id (int): The ID of the audio feature to stream.

    Returns:
        StreamingHttpResponse: The response containing the audio stream.
    """
    audio_feature = AudioFeatures.objects.get(id=audio_id)
    audio_file = audio_feature.audio

    def audio_stream():
        with audio_file.open('rb') as file:
            while True:
                chunk = file.read(8192)  # Read 8KB chunk from the file
                if not chunk:
                    break
                yield chunk

    response = StreamingHttpResponse(audio_stream(), content_type=f'audio/{audio_feature.extension}')
    response['Content-Disposition'] = f'inline; filename="{audio_feature.audio.name}"'
    return response
