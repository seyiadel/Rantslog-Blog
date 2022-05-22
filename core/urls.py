from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.about, name='about_page'),
    path('search/', views.search, name='search'),
    path('',views.homepage, name='homepage'),
    path('detail/<slug:slug>/',views.detail, name='post_detail'),
    path('category/<slug:slug>/',views.category, name='category_page'),
]