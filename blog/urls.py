from django.urls import path
from . import views
# nama Aplikasi
app_name = 'blog'


urlpatterns = [
    path('', views.PostListView.as_view(), name='post'),
    path('<slug:slug>/',views.PostDetailView.as_view(), name='detail'),
]
