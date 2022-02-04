from django.db.models import Q
from content.models import Contributor, Issue, Comment, Project
from content.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from content.permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ContributorViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs['project_pk'])

class ProjectViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        # all the projects wich the author or the contributor is the connected user without duplicate
        return Project.objects.filter(Q(author=self.request.user) | Q(contributor__user=self.request.user)).distinct()

class IssueViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

class CommentViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])