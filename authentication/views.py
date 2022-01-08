from rest_framework.viewsets import ModelViewSet
from authentication.models import Users
from authentication.serializers import UsersSerializer


class UsersViewset(ModelViewSet):
    serializer_class = UsersSerializer

    def get_queryset(self):
        return Users.objects.all()