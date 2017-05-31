from basic_app import views
from django.conf.urls import url

# Template urls
app_name = 'basic_app'
urlpatterns = [
    url(r'^register/$',views.register,name='register'),
]
