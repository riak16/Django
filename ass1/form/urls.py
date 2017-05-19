from django.conf.urls import url
from .views import form_view

urlpatterns = [
	url(r'^$',form_view.as_view(),name='form_view'),
	#url(r'form/sub/$',views.response_sub,name='response-sub'),	
]