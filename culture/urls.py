from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from culture import views


urlpatterns = [
    path('', views.home, name='home'),
    path('heritage-sites/', views.heritage_sites, name='heritage_sites'),
    path('festivals/', views.festivals, name='festivals'),
    path('artforms/', views.artforms, name='artforms'),
    path('add-post/', views.add_post, name='add_post'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='culture/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete-post/<int:id>/', views.delete_post, name='delete_post'),
]
