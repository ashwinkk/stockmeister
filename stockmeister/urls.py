from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'stockmeister.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^test/', 'trial.views.test', name='trial'),
    url(r'^newuser/','newprofuser.views.newuser',name='newuser'),
    url(r'^login/','login.views.Login',name='login'),
    url(r'^update/','update.views.update',name='update'),
    url(r'^getdata/','datamine.views.getdata',name='getdata'),
    url(r'^admin/', include(admin.site.urls)),
]
