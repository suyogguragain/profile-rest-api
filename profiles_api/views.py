from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializers


# Create your views here.


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView Features"""
        an_apiview = [
            'a',
            'b',
            'c',
        ]

        return Response({"message": "Hello World", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle apartial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello msg"""
        a_viewset = [
            'a',
            'b',
            'c',
        ]
        return Response({"message": "Hello!!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a new hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an objects by its ID"""
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
