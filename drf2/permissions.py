from rest_framework.permissions import BasePermission
from django.utils import timezone
from rest_framework.exceptions import APIException
from rest_framework import status
class RegistedMoreThanAThreeDayUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not request.user or not request.user.is_authenticated:
            return False
        return bool(user.join_date < (timezone.now() - timezone.timedelta(minutes=3)))
    
class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

    
class IsAdminOrIsAuthenticatedReadOnly(BasePermission):
    SAFE_METHODS = ('POST', 'GET',)
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user
        
        if request.method == 'GET':
            if not user.is_authenticated:
                response ={
                        "detail": "서비스를 이용하기 위해 로그인 해주세요.",
                    }
                raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)
            if user.is_authenticated:
                return True
        
        if request.method == 'POST':
            if not user.is_authenticated:
                response ={
                        "detail": "서비스를 이용하기 위해 로그인 해주세요.",
                    }
                raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)
            if user.is_authenticated and user.is_admin:
                return True
                
            if user.is_authenticated and (user.join_date < (timezone.now() - timezone.timedelta(days=7))):
                return True
        
        return False        