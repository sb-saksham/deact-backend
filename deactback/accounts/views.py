from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import UserModel
from .serializers import UserModelSerializer


class CreateUserView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = []
