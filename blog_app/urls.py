from . import views
from django.urls import path


                             
urlpatterns = [
    path('', views.BlogList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

