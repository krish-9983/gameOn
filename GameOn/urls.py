"""GameOn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from .views import home_view, about_view
from Tournaments.views import tournaments_view, tournament_detail_view, search_view, tournament_create_view, tournament_delete_view
from registerations.views import register_checkout_view, tournament_registerations_view
from profiles.views import profile_view, profile_edit_view, profile_tournament_history_view

urlpatterns = [
    path('about', about_view),
    path('tournament/<int:pk>/registerations', tournament_registerations_view),
    path('tournament/create/', tournament_create_view),
    path('tournament/create', tournament_create_view),
    path('tournaments/create', tournament_create_view),
    path('tournaments/create/', tournament_create_view),
    path('profile/tournaments/history', profile_tournament_history_view),
    path('search/',search_view),
    path('accounts/profile/', profile_view ),
    path('accounts/profile/edit/', profile_edit_view),
    path('tournament/<int:pk>/', tournament_detail_view),
    path('tournament/<int:pk>/delete', tournament_delete_view),
    path('register/tournament/<int:pk>', register_checkout_view),
    path('accounts/', include('allauth.urls')),
    path('tournaments', tournaments_view),
    path('tournaments/', tournaments_view),
    path('tournament/', tournaments_view),
    path('', home_view),
    path('home', home_view),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
