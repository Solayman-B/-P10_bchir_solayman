from django.urls import path, include
from content.views import ProjectViewset, ContributorViewset, IssueViewset, CommentViewset
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('projects', ProjectViewset, basename='projects')

project_router = routers.NestedSimpleRouter(router, 'projects', lookup='project')
project_router.register('users', ContributorViewset, basename='users')
project_router.register('issues', IssueViewset, basename='issues')

issue_router = routers.NestedSimpleRouter(project_router, 'issues', lookup='issue')
issue_router.register('comments', CommentViewset, basename='comments')

app_name='content'

urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issue_router.urls) ),
]
