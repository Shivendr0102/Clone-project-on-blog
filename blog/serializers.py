from rest_framework import serializers
from .models import Comment , Post
from django.shortcuts import render , get_object_or_404, redirect
# from noconflict import classmaker
from six import with_metaclass


class CommentSerializer(serializers.Serializer):
    # post = PostSerializer()
    comment_author = serializers.CharField(source = 'author')
    comment_text = serializers.CharField(source = 'text')




class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField()
    date = serializers.DateTimeField(source = 'created_date')
    author = serializers.CharField()
    # if title==Comment.post:
    #     print("hello")
    comment = CommentSerializer()

    # def match(self):
    #     # post = get_object_or_404(Post,pk=pk)
    #     # comment = Comment()
    #     comment = CommentSerializer()
    #     # # print (comment.post)
    #     # if comment.post == post:
    #     #     print("hello")
    #     return comment()
    #


# class CommentSerializer(serializers.Serializer):
#     post = PostSerializer()
#     comment_author = serializers.CharField(source = 'author')
#     comment_text = serializers.CharField(source = 'text')
