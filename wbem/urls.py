from django.urls import path, include
from wbem import views
from wbem import forms as wbem_forms

app_name = 'wbem'


urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),

    path('', views.API.as_view(), name="api"),

    path('ei/', views.Dynamic.as_view(form=wbem_forms.EcnForm), name="ei"),
    path('ein/', views.Dynamic.as_view(form=wbem_forms.EinForm), name="ein"),
    path('gi/', views.Dynamic.as_view(form=wbem_forms.GiForm), name="gi"),
    # path('mi/', views.Mi.as_view(), name="mi"),
    # path('ci/', views.Ci.as_view(), name="ci"),
    # path('di/', views.Di.as_view(), name="di"),
    # path('a/', views.A.as_view(), name="a"),
    # path('an/', views.An.as_view(), name="an"),
    # path('r/', views.R.as_view(), name="r"),
    # path('rn/', views.Rn.as_view(), name="rn"),
    # path('im/', views.Im.as_view(), name="im"),
    # path('eqy/', views.Eqy.as_view(), name="eqy"),
    #
    # path('ec/', views.Ec.as_view(), name="ec"),
    path('ecn/', views.Dynamic.as_view(form=wbem_forms.EcnForm), name="ecn"),
    path('gc/', views.Dynamic.as_view(form=wbem_forms.GcForm), name="gc"),
    # path('mc/', views.Mc.as_view(), name="mc"),
    # path('cc/', views.Cc.as_view(), name="cc"),
    # path('dc/', views.Dc.as_view(), name="dc"),
    #
    # path('ei/', views.Ei.as_view(), name="ei"),
    # path('ei/', views.Ei.as_view(), name="ei"),
    # path('ei/', views.Ei.as_view(), name="ei"),
    # path('ei/', views.Ei.as_view(), name="ei"),
    # path('ei/', views.Ei.as_view(), name="ei"),
    # path('ei/', views.Ei.as_view(), name="ei"),


]
