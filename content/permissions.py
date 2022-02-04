from rest_framework import permissions
from .models import Contributor


class IsAuthorOrReadOnly(permissions.BasePermission):
	message = "Action impossible, seul l'auteur y est autorisé."

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True

		if obj.author == request.user:
			return True

# class IsContributor(permissions.BasePermission):
# 	message = "Accès refusé, vous n'êtes pas contributeur du projet."
#
# 	def has_permission(self, request, view):
# 		if request.user.is_authenticated:
# 			return True
#
# 	def has_object_permission(self, request, view, obj):
# 		contributor = Contributor.objects.filter(project=obj.id)
# 		# print(contributor.filter(user=request.user), 'REQUESTREQUESTREQUESTREQUESTREQUESTREQUESTREQUESTREQUESTREQUESTREQUESTREQUESTREQUESTREQUESTREQUESTREQUESTREQUEST')
# 		if request.method in permissions.SAFE_METHODS:
# 			return contributor.filter(user=request.user)