from django.shortcuts import render
from django.views import View
import pywbem
import json
from wbem import models as wbem_models
from wbem import forms as wbem_forms

# Create your views here.
class Dashboard(View):
    template = 'wbem/dashboard.html'

    def get(self, request):

        data = ["Linux", "v2", "76345"] * 3

        # server_url = 'http://ttm4128.item.ntnu.no:5988/root/cimv2'
        #server_url = Options.objects.first().server_url
        server_url = 'http://ttm4128.item.ntnu.no:5988/cimom'

        conn = pywbem.WBEMConnection(server_url)

        # server = pywbem.WBEMServer(conn)

        classnames = conn.EnumerateClassNames(DeepInheritance=False)
        print(classnames)

        instances = conn.EnumerateInstances('CIM_Processor')


        return render(request, self.template, {
            "data": data,
            "classnames": classnames,
        })


class Interactive(View):
    template = 'wbem/interactive.html'
    form = wbem_forms.ClassForm

    def get(self, request):

        form = self.form()

        return render(request, self.template, {
            'form': form,
        })

    def post(self, request):
        server_url = 'http://ttm4128.item.ntnu.no:5988/cimom'
        conn = pywbem.WBEMConnection(server_url)

        methods = {
            '1': conn.EnumerateClassNames,
        }

        form = self.form(request.POST)

        data = ["data"] * 3

        if form.is_valid():
            data = form.cleaned_data
            print(data)
            data = methods[form.cleaned_data['function']]()


        return render(request, self.template, {
            'form': form,
            'data': data,
        })

class EnumerateClassNames(View):
    template = 'wbem/enumerate_classnames.html'

    def get(self, request):
        server_url = 'http://ttm4128.item.ntnu.no:5988/cimom'
        conn = pywbem.WBEMConnection(server_url)
        data = conn.EnumerateClassNames()

        return render(request, self.template, {
            'data': data,
        })

class API(View):
    template = 'wbem/api.html'

    def get(self, request):
        from wbem import urls

        urlnames = [urls.app_name+':'+path.name for path in urls.urlpatterns]

        return render(request, self.template, {
            'urlnames': urlnames,
        })

# path('ei/', views.Ei.as_view(), name="ei"),
# path('ein/', views.Ein.as_view(), name="ein"),
# path('gi/', views.Gi.as_view(), name="gi"),
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
# path('ecn/', views.Ecn.as_view(), name="ecn"),
# path('gc/', views.Gc.as_view(), name="gc"),
# path('mc/', views.Mc.as_view(), name="mc"),
# path('cc/', views.Cc.as_view(), name="cc"),
# path('dc/', views.Dc.as_view(), name="dc"),

class Ei(View):
    """EnumerateInstances"""

    template = 'wbem/interactive.html'
    form = wbem_forms.EiForm

    def get(self, request):

        form = self.form()

        return render(request, self.template, {
            'form': form,
        })

    def post(self, request):
        server_url = 'http://ttm4128.item.ntnu.no:5988/cimom'
        conn = pywbem.WBEMConnection(server_url)

        form = self.form(request.POST)
        print(request.POST)

        result = None


        if form.is_valid():
            data = form.cleaned_data
            try:
                result = conn.EnumerateInstances(
                    ClassName=data['classname'],
                    namespace=data['namespace'] or None,
                    DeepInheritance=data['deep_inheritance'] or None,
                    IncludeQualifiers=data['include_qualifiers'] or None,
                    IncludeClassOrigin=data['include_class_origin'] or None,
                )
            except Exception as e:
                print(e),
                result = e

        return render(request, self.template, {
            'form': form,
            'result': result,
        })

class Ecn(View):
    """EnumerateClassNames"""

    template = 'wbem/interactive.html'
    form = wbem_forms.EcnForm

    def get(self, request):

        form = self.form()

        return render(request, self.template, {
            'form': form,
        })

    def post(self, request):
        server_url = 'http://ttm4128.item.ntnu.no:5988/cimom'
        conn = pywbem.WBEMConnection(server_url)

        form = self.form(request.POST)
        print(request.POST)

        result = None


        if form.is_valid():
            data = form.cleaned_data
            try:
                result = conn.EnumerateClassNames(
                    ClassName=data['classname'] or None,
                    namespace=data['namespace'] or None,
                    DeepInheritance=data['deep_inheritance'] or None,
                )
            except Exception as e:
                print(e),
                result = e

        return render(request, self.template, {
            'form': form,
            'result': result,
        })

class Dynamic(View):
    template = 'wbem/dynamic.html'
    form = None

    def get(self, request):

        form = self.form()

        return render(request, self.template, {
            'form': form,
        })

    def post(self, request):
        server_url = 'http://ttm4128.item.ntnu.no:5988/cimom'
        conn = pywbem.WBEMConnection(server_url)

        form = self.form(request.POST)

        result = None

        if form.is_valid():
            data = form.cleaned_data
            try:
                input = [field or None for field in data.values()]
                print(input)
                # Order of input is important
                print(getattr(conn, form.method))
                result = getattr(conn, form.method)(*input)

                import wbem.urls as urls
                print(urls.urlpatterns[-1])
                print(type(urls.urlpatterns[-1]))

            except Exception as e:
                print(e),
                result = e

        return render(request, self.template, {
            'form': form,
            'result': result,
        })
