from rest_framework.permissions import BasePermission
from django.utils import timezone
class RegistedMoreThanAThreeDayUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not request.user or not request.user.is_authenticated:
            return False
        return bool(user.join_date < (timezone.now() - timezone.timedelta(minutes=3)))