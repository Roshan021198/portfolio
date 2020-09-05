from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('blogpost/<int:pk>',views.blogpost,name='blogpost'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('contact/',views.contact,name='contact'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
