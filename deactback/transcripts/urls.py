from django.urls import path
from .views import CreateTranscript, CreateRequestTranscript,\
    CreateTranscriptRequestAccess, UpdateTranscriptRequestAccess, UpdateRequestTranscript

app_name = "transcript"

urlpatterns = [
    path('add/', CreateTranscript.as_view(), name="transcript"),
    path('request/', CreateRequestTranscript.as_view(), name="req_transcript"),
    path('access/', CreateTranscriptRequestAccess.as_view(), name="acc_transcript"),
    path('access/update/', UpdateRequestTranscript.as_view(), name="upd_req_transcript"),
    path('request/update/', UpdateTranscriptRequestAccess.as_view(), name="upd_acc_transcript")
]
