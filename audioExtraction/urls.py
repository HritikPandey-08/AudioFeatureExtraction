from django.urls import path
from .views import audio_extraction,stream_audio

urlpatterns = [
    path('audioFeatures/', audio_extraction, name='audio_extraction'),
    path('stream_audio/<int:audio_id>/',stream_audio, name='stream_audio')
]
