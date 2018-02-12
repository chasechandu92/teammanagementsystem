from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^members/$', views.members, name='members'),
		url(r'^addmember/$', views.add_member, name='add_member'),
		url(r'^editmember/$', views.edit_member, name='edit_member'),
		url(r'^deletemember/$', views.delete_member, name='delete_member'),
]