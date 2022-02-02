from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from content.models import Project, Contributor, Issue, Comment

class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def validate_title(self, value):
        # Nous vérifions que la catégorie existe
        if Project.objects.filter(title=value).exists():
            # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError('Ce titre existe déjà')
        return value

class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
