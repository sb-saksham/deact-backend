from rest_framework.serializers import ModelSerializer


class UserModelSerializer(ModelSerializer):
    class Meta:
        fields = ['ethereum_address', 'name', 'account_type']
