from django.urls import path, include
from wbem import views


app_name = 'wbem'


urlpatterns = [
    path('', views.Dashboard.as_view(), name="dashboard"),
    path('interactive', views.Interactive.as_view(), name="interactive"),
    path('enumerate_classnames', views.EnumerateClassNames.as_view(), name="enumerate_classnames"),

]
