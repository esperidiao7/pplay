from django.conf.urls import include, url
from django.contrib import admin
from blog.views import home

urlpatterns = [
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'', include('blog.urls')),
]
