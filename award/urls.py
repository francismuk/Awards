from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^search/', views.search_projects, name='search'),url(r'^image/(\d+)',views.image,name ='image'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)