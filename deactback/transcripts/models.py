from django.db import models
from django.db.models.signals import post_save
from accounts.models import UserModel

REQUEST_TRANSCRIPT_CHOICES = [
    ('created', 'Request Created'),
    ('uploaded', 'Transcript Uploaded'),
]

TRANSCRIPT_ACCESS_CHOICES = [
    ('requested', 'Decision Pending'),
    ('approved', 'Request Approved'),
    ('declined', 'Request Declined')
]


class Transcript(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="transcripts")
    name = models.CharField(max_length=264)
    cid = models.CharField(primary_key=True, max_length=264)


# For User to request Education Institution
class RequestTranscript(models.Model):
    id = models.AutoField(primary_key=True)
    # Organisation Account
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="transcript_requests")

    # Transcript of below User
    address = models.CharField(max_length=264)
    name = models.CharField(max_length=264)
    status = models.CharField(choices=REQUEST_TRANSCRIPT_CHOICES, max_length=264, default="created")

    # After upload fields
    transcript = models.ForeignKey(Transcript, null=True, blank=True, on_delete=models.CASCADE)


# For Companies to request to User
class TranscriptRequestAccess(models.Model):
    id = models.AutoField(primary_key=True)
    # Company account
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="transcript_access_requests")

    # Document Details
    transcript_of = models.CharField(max_length=264)
    name = models.CharField(max_length=264)

    # After giving access fields
    status = models.CharField(max_length=264, default="requested", choices=TRANSCRIPT_ACCESS_CHOICES)
    transcript = models.ForeignKey(Transcript, null=True, blank=True, on_delete=models.CASCADE)
