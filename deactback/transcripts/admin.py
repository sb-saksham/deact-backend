from django.contrib import admin
from .models import Transcript, RequestTranscript, TranscriptRequestAccess

admin.site.register(Transcript)
admin.site.register(RequestTranscript)
admin.site.register(TranscriptRequestAccess)
