from django.contrib import admin
from django.urls import path,include
from .views import blogview,BlogById,blog_detail_view,blog_list_view,bloghome
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',bloghome,name='home'),
    path('api/', blogview,name='BlogsView'),
    path('api/<int:id>', BlogById,name='Blogbyid'),
    path('blogs/', blog_list_view, name='blog_list_view'),
    path('blogs/<int:blog_id>/',blog_detail_view, name='blog_detail_view')

   

]
urlpatterns += [
    path('api-token-auth/', obtain_auth_token)
]