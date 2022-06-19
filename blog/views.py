from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drf2.permissions import RegistedMoreThanAThreeDayUser as R
# Create your views here.
class MakeArticle(APIView):
    permission_classes = [R]
    def get(self, request):
        return render('main.html')
    
    def post(self, request):

        title = request.data.get('title', '')
        category = request.data.get('category', '')
        content = request.data.get('content', '')
        if len(title) <= 5:
            return Response({'error':'title must be longer than 5'})
        if category is None or "":
            return Response({'error':'you must select Category'})
        if len(content) <= 20:
            return Response({'error': 'content must be more than 20'})
        return Response({'message':'Article posted'})