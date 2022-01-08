from rest_framework.serializers import ModelSerializer
from content.models import Projects, Contributors, Issues, Comments

class ContributorsSerializer(ModelSerializer):
    class Meta:
        model = Contributors
        fields = ['user', 'project', 'permission', 'role']

class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'type', 'author']

class IssuesSerializer(ModelSerializer):
    class Meta:
        model = Issues
        fields = ['title', 'description', 'tag', 'priority', 'project',	'status', 'author', 'assignee', 'created_time']

class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment', 'description', 'author', 'issue', 'created_time']
