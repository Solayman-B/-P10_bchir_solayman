from django.urls import path, include
from content.views import ProjectsViewset, ContributorsViewset, IssuesViewset, CommentsViewset
from rest_framework import routers

router = routers.SimpleRouter()

router.register('projects', ProjectsViewset, basename='projects')
router.register('contributors', ContributorsViewset, basename='contributors')
router.register('issues', IssuesViewset, basename='issues')
router.register('comments', CommentsViewset, basename='comments')

app_name='content'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]