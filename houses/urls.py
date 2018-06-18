from django.conf.urls import url, include
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    url(r'^addlisting/$', views.addlisting, name='addlisting'),
    url(r'^listing/$', views.listbyuser, name='listbyuser'),
    url(r'^listing/details/(?P<id>\d+)/$', views.listbyuserdetails, name='detail'),
    url(r'^listing/details/(?P<id>\d+)/editlist$', views.editlist, name='editlist'),
    url(r'^listing/details/(?P<pk>\d+)/editlist2$', views.editlist2, name='editlist2'),
    url(r'^listing/details/(?P<pk>\d+)/deletelist$', views.deletelist, name='deletelist'),
    url(r'^userlist/', views.UserListView.as_view(), name='userlist'),
    url(r'^alllisting/', views.alllisting.as_view(), name='alllisting'),
    
]