from myapp import views
from django.conf.urls import url

# Template urls
app_name = 'myapp'
urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^staas/$',views.form_name_view,name='staas'),
    url(r'^saas/$',views.SaasService,name='saas'),
    url(r'^iaas/$',views.IaasService,name='iaas'),
]
