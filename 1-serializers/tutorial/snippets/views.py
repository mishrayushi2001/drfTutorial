from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.http import Http404
# @csrf_exempt
# @api_view(['GET','POST'])
class SnippetList(APIView):
# def snippet_list(request,format=None):
    def get(request,format=None):

        """
        List all code snippets, or create a new snippet.
        """
        # if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
        # elif request.method == 'POST':
    def post(self, request, format =None):
        # data = JSONParser().parse(request)
        # serializer = SnippetSerializer(data=data)
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return JsonResponse(serializer.errors, status=400)

    
# @csrf_exempt
# @api_view(['GET','PUT','DELETE'])
class SnippetDetail(APIView):
# def snippet_detail(request, pk, formt=None):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            # return HttpResponse(status=404)
            # return HttpResponse(status=status.HTTP_404_NOT_FOUND)
            return Http404
    def get(self,request,pk,format=None):
    # if request.method == 'GET':
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
        # return JsonResponse(serializer.data)
    # elif request.method == 'PUT':
    def put(self,request,pk,format=None):
        # data = JSONParser().parse(request)
        # serializer = SnippetSerializer(snippet, data=data)
        snippet=self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            # return JsonResponse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         # return JsonResponse(serializer.errors, status=400)
    # elif request.method == 'DELETE':
    def delete(self,request,pk,format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        # return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)