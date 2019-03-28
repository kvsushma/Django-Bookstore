from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'BookStore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),	
	url(r'^store/', include('store.urls'), name='store'),
	url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html', 'redirect_field_name': '/store/'}),

	url('', include('social.apps.django_app.urls', namespace='social')),

	#url(r'^$', 'store.views.index',name='index'), 
    url(r'^admin/', include(admin.site.urls)),
]
