from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

     def get(self, request,format=None):

         an_apiview = [
         'Uses HTTP methods as function (get, post, patch, put, delete)',
         'Is similar to a traditional Django View',
         'Gives you the most control over you application logic',
         'Is mapped manually to URLS',
         ]

         return Response({'message': 'hello!', 'an_apiview': an_apiview})
