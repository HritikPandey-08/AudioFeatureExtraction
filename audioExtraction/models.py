from django.db import models
from django.contrib.auth import get_user_model

class AudioFeatures(models.Model):
    """
    Model to store information about uploaded audio files.
    
    This model defines the structure of the AudioFeatures table in the database,
    where each entry corresponds to an uploaded audio file and its associated information.
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    """
    ForeignKey to associate the audio with a user.
    
    This field establishes a many-to-one relationship with the user model.
    The 'on_delete=models.CASCADE' parameter ensures that when a user is deleted,
    their uploaded audio entries are also deleted (cascading behavior).
    """
    
    title = models.CharField(max_length=200)
    """
    CharField to store the title of the audio file.
    
    This field stores the title of the audio file provided by the user.
    'max_length=200' specifies the maximum length of the title.
    """
    
    audio = models.FileField(upload_to='audio_files/')
    """
    FileField to store the uploaded audio file.
    
    This field stores the actual audio file uploaded by the user.
    'upload_to' parameter specifies the directory where the file will be stored.
    """
    
    dateOfUpload = models.DateTimeField(auto_now_add=True)
    """
    DateTimeField to store the upload date and time.
    
    This field automatically records the date and time when the audio file is uploaded.
    'auto_now_add=True' ensures that the timestamp is set when the entry is created.
    """
    
    size = models.FloatField(max_length=200)
    """
    FloatField to store the size of the audio file in bytes.
    
    This field stores the size of the audio file in bytes.
    'max_length=200' specifies the maximum length of the field.
    """
    
    duration = models.FloatField(max_length=200)
    """
    FloatField to store the duration of the audio file in seconds.
    
    This field stores the duration of the audio file in seconds.
    'max_length=200' specifies the maximum length of the field.
    """
    
    extension = models.CharField(max_length=200)
    """
    CharField to store the extension of the audio file.
    
    This field stores the file extension (format) of the uploaded audio file.
    'max_length=200' specifies the maximum length of the extension.
    """
