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


class API(View):
    template = 'wbem/api.html'

    def get(self, request):
        from wbem import urls

        urlnames = [urls.app_name+':'+path.name for path in urls.urlpatterns]

        return render(request, self.template, {
            'urlnames': urlnames,
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
                # Order of input is important
                result = getattr(conn, form.method)(*input)

            except Exception as e:
                result = e

        return render(request, self.template, {
            'form': form,
            'result': result,
        })
