from .import views
from django.conf.urls import url

urlpatterns = [ 
    url(r'^api/Home/Role$', views.role_list),
    url(r'^api/Home/Role/(?P<pk>[0-9]+)$', views.role_detail),
    url(r'^api/Home/Faculty$', views.faculty_list),
    url(r'^api/Home/Faculty/(?P<pk>[0-9]+)$', views.faculty_detail),
    url(r'^api/Home/Contribution$', views.contribution_list),
    url(r'^api/Home/Contribution/(?P<pk>[0-9]+)$', views.contribution_detail),
    url(r'^api/Home/FileType$', views.filetype_list),
    url(r'^api/Home/FileType/(?P<pk>[0-9]+)$', views.filetype_detail),
    url(r'^api/Home/User$', views.user_list),
    url(r'^api/Home/User/(?P<pk>[0-9]+)$', views.user_detail),
    url(r'^api/Home/Email$', views.send_email),
    url(r'^api/Home/UpVote/(?P<pk>[0-9]+)$', views.up_vote),
    url(r'^api/Home/DownVote/(?P<pk>[0-9]+)$', views.down_vote),
    url(r'^api/Home/Signin$', views.sign_in),
    url(r'^api/Home/Download$', views.download),
    
]
