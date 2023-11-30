"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from my_book.views import List_book,Delete_book,Detail_book,Create_book,Update_book
from my_book.views2 import list_book,create_book,detail_book,update_book,delete_book

urlpatterns = [
    path('admin/', admin.site.urls),

    path('books/',List_book.as_view()),
    path('create/',Create_book.as_view()),
    path('detatils/<int:pk>',Detail_book.as_view()),
    path('delete/<int:pk>',Delete_book.as_view()),
    path('update/<int:pk>',Update_book.as_view()),

    path('bookss/',list_book),
    path('createe/',create_book),
    path('detailss/<int:pk>',detail_book),
    path('updatee/<int:pk>',update_book),
    path('deletee/<int:pk>',delete_book),
    



]
