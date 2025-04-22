from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import requests





@api_view(['GET','POST'])

def blogview(request):

    if request.method =='GET':
        queryset = Blog.objects.all()
        serilize = BlogSerializer(queryset,many=True)
        return Response(serilize.data)
    
       
    
    elif request.method =='POST':
        queryset = BlogSerializer(data = request.data)
        if queryset.is_valid():
            queryset.save()
            return Response("Post Successfully")


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def BlogById(request, id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response({"error": "Blog not found."}, )

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated successfully."})
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        blog.delete()
        return Response({"message": "Post deleted successfully."})






API_BASE_URL = 'http://localhost:8000/api/blogs/'  

def bloghome(request):
    return render(request, 'home.html')

def blog_list_view(request):
    response = requests.get(API_BASE_URL)
    blogs = response.json() if response.status_code == 200 else []
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_detail_view(request, blog_id):
    response = requests.get(f"{API_BASE_URL}{blog_id}/")
    blog = response.json() if response.status_code == 200 else {}
    return render(request, 'blog_detail.html', {'blog': blog})
