from rest_framework import serializers

from .models import Snippet,Tag
from django.urls import reverse


class TagField(serializers.CharField):
    def to_representation(self, value):
        print("eeeeeeeee",value)
        return value.title

class SnippetCreateSerializer(serializers.ModelSerializer):
    tag = TagField()

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'snippets', 'created_at', 'tag']

    
class SnippetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Snippet
        fields=['id','title', 'snippets' ,'created_at']


class SnippetDetailSerializer(serializers.ModelSerializer):
    tag = serializers.ReadOnlyField(source='tag.title')
    created_user = serializers.ReadOnlyField(source='created_user.username')
    class Meta:
        model = Snippet
        fields=['id','title', 'snippets' ,'created_at','created_user','tag']
        
class TagSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Tag
        fields = ['id','title']
        


class SnippetOverviewSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Snippet
        fields = ['id','snippets','detail_url']

    def get_detail_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('snippet_details', kwargs={'pk': obj.pk}))
        return ''