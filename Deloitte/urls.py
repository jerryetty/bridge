from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'deloitte'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^income', views.income, name='income'),
	url(r'^expenditure', views.expenditure, name='expenditure'),
	url(r'^liability', views.liability, name='liability'),
	url(r'^assets', views.assets, name='assets'),
	url(r'^equity', views.equity, name='equity'),
	url(r'^business_details', views.business_details, name='business_details'),
	]