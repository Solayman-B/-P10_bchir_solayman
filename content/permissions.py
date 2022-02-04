from rest_framework import permissions
from .models import Contributor


class IsAuthorOrReadOnly(permissions.BasePermission):
	message = "Action impossible, seul l'auteur y est autorisé."

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True

		if obj.author == request.user:
			return True