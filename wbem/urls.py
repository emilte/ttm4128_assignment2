from django.urls import path, include
from wbem import views


app_name = 'wbem'


urlpatterns = [
    path('', views.Dashboard.as_view(), name="dashboard"),
]
