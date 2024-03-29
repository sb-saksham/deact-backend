from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import RetrieveModelMixin

from .models import Transcript, RequestTranscript, TranscriptRequestAccess
from .serializers import TranscriptSerializer, RequestTranscriptSerializer,\
    TranscriptRequestAccessSerializer, TranscriptRequestAccessUpdateSerializer, RequestTranscriptUpdateSerializer


class CreateTranscript(CreateAPIView, RetrieveModelMixin):
    queryset = Transcript.objects.all()
    serializer_class = TranscriptSerializer
    permission_classes = [IsAuthenticated]


class CreateRequestTranscript(CreateAPIView, RetrieveModelMixin):
    queryset = RequestTranscript.objects.all()
    serializer_class = RequestTranscriptSerializer
    permission_classes = [IsAuthenticated]


class CreateTranscriptRequestAccess(CreateAPIView, RetrieveModelMixin):
    queryset = TranscriptRequestAccess.objects.all()
    serializer_class = TranscriptRequestAccessSerializer
    permission_classes = [IsAuthenticated]


class UpdateTranscriptRequestAccess(UpdateAPIView):
    queryset = TranscriptRequestAccess.objects.all()
    serializer_class = TranscriptRequestAccessUpdateSerializer
    permission_classes = [IsAuthenticated]


class UpdateRequestTranscript(UpdateAPIView):
    queryset = RequestTranscript.objects.all()
    serializer_class = RequestTranscriptUpdateSerializer
    permission_classes = [IsAuthenticated]
