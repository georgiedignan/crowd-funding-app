from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserList(APIView):
    #retrieve all users
    def get(self, request):
        users = CustomUser.objects.all()
        serializers = CustomUserSerializer(users, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = CustomUserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

class CustomUserDetail(APIView):
    #helper method for getting auser and raising a 404 if that user does not exist
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    #get a single user's detail
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)