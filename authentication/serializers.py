from rest_framework.serializers import ModelSerializer
from authentication.models import Users


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']