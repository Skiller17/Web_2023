"""
URL configuration for ask_zhokhov2 project.

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
from ask import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('ask/', views.ask, name = 'ask'),
    path('tags/<int:i>', views.tags, name='tags'),
    path('question/<int:i>', views.question, name = "question"),
    path('authefication/', views.authefication, name = 'auth'),
    path('registration/', views.registration, name = 'reg'),
    path('hot/', views.hot, name = 'hot'),
    path('tag/<str:tag_title>', views.questions_with_tags, name='question_tag'),
    path('settings/', views.settings, name='setting')
]