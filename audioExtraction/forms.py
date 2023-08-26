from django import forms
from .models import AudioFeatures

class AudioUploadForm(forms.ModelForm):
    """
    A form for uploading audio files along with their title.
    
    This form is used to handle the uploading of audio files and capturing their associated titles.
    It utilizes the AudioFeatures model to store the uploaded audio information.
    """
    class Meta:
        model = AudioFeatures
        fields = ('title','audio')
        """
         The 'title' and 'audio' fields are included in the form for user input.
        """