from django.conf.urls import include,url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.post_list,name="post_list"),
    url(r'^solarsystem', views.solarsystem),
    url(r'^post/(?P<priKey>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^postedit/(?P<priKey>[0-9]+)/$', views.post_edit, name='post_edit'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]