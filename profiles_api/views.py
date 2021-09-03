from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView Features"""
        an_apiview = [
            'a',
            'b',
            'c',
        ]

        return Response({"message": "Hello World", "an_apiview": an_apiview})
