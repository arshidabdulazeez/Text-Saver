from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SnippetSerializer , TagSerializer ,SnippetOverviewSerializer,SnippetDetailSerializer,SnippetCreateSerializer

from django.http import Http404
from rest_framework.generics import ListAPIView

from . models import *

from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated


def get_snippet(self,pk):
    try:
        return Snippet.objects.get(pk=pk)
    except:
        raise Http404
        
class SnippetCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
                
        serializer = SnippetCreateSerializer(data=request.data)
                
        if serializer.is_valid():
            
            title = serializer.validated_data['title']
            snippets = serializer.validated_data['snippets']
            tag_title = serializer.validated_data['tag']
            
            if tag_title:
                tag = Tag.objects.filter(title=tag_title).first()
                if not tag:
                    tag = Tag.objects.create(title=tag_title)

            snippet = Snippet.objects.create(title=title, created_user=request.user, tag=tag , snippets=snippets)
            return Response({'id': snippet.id, 'message': 'Snippet created successfully.'})
        
        return Response(serializer.errors, status=400)
    
class SnippetOverview(APIView):

    """ if need Authentication for this view uncommend the below line """
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        snippet_count = Snippet.objects.count()
        
        snippets = Snippet.objects.all()
        serializer = SnippetOverviewSerializer(snippets, many=True, context={'request': request})
        
        data={}
        data['snippet_count'] = snippet_count,
        data['snippets'] = serializer.data
        return Response(data)
    
class SnippetDetails(APIView):

    """ if need Authentication for this view uncommend the below line """
    # permission_classes = [IsAuthenticated]
    
    
        
    def get(self, request, pk, format=None):
        
        snippet_data = get_snippet(self,pk)
        serializer = SnippetDetailSerializer(snippet_data)
        serialized_data = serializer.data

        return Response(serialized_data)
    
    
class SnippetUpdate(APIView):

    """ if need Authentication for this view uncommend the below line """
    # permission_classes = [IsAuthenticated]
        
    def get(self,request,pk,format=None):
        SnippetData=get_snippet(self,pk)
        serializer=SnippetSerializer(SnippetData)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        snippet = get_snippet(self,pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class SnippetDelete(APIView):

    """ if need Authentication for this view uncommend the below line """
    # permission_classes = [IsAuthenticated]
    
    def get(self,request,pk,format=None):
        SnippetData=get_snippet(self,pk)
        serializer=SnippetSerializer(SnippetData)
        return Response(serializer.data)
    
    def delete(self,request,pk,format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        
        snippet = get_snippet(self,pk)
        snippet.delete()
        return Response({'respone':serializer.data})
    
class TagList(APIView):

    """ if need Authentication for this view uncommend the below line """
    # permission_classes = [IsAuthenticated]
    
    def get(self,request,format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    
class TagDetails(ListAPIView):

    """ if need Authentication for this view uncommend the below line """
    # permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        try:
            tag = Tag.objects.filter(pk=pk).first()
            snippets = Snippet.objects.filter(tag=tag)
            serializer = SnippetSerializer(snippets, many=True)
            
            response_data={}
            response_data['tag'] = tag.title
            response_data['snipppets'] = serializer.data
            return Response(response_data)
        except:
            return Response({'error': 'Tag not found.'})
