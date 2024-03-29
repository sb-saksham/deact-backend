from rest_framework.serializers import ModelSerializer


class TranscriptSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'


class TranscriptRequestAccessSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'


class RequestTranscriptSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'


class TranscriptRequestAccessUpdateSerializer(ModelSerializer):
    class Meta:
        fields = ['id', 'status', 'transcript']


class RequestTranscriptUpdateSerializer(ModelSerializer):
    class Meta:
        fields = ['id', 'status', 'transcript']
