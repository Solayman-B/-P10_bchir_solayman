from django.contrib import admin
from content.models import Contributor, Project, Issue, Comment

# Register your models here.

class ContributorAdmin(admin.ModelAdmin):
	pass

class ProjectAdmin(admin.ModelAdmin):
	pass

class IssueAdmin(admin.ModelAdmin):
	pass

class CommentAdmin(admin.ModelAdmin):
	pass


admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)