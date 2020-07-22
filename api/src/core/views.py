from django.shortcuts import render
from django.http import JsonResponse

#third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

class PostView

# Create your views here.

# class TestView(APIView):
   
#    permission_classes = (IsAuthenticated, )

#    def get(self, request, *args, **kwargs):
#       qs = Post.objects.all()
#       post = qs.first()
#       #serializer = PostSerializer(qs, many=True)
#       serializer  = PostSerializer(post)
#       return Response(serializer.data)

#    def post(self, request, *args, **kwargs):
#       serializer = PostSerializer(data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data)
#       else:
#          return Response(serializer.errors)

#To test download
#https://www.postman.com/downloads/