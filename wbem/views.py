from django.shortcuts import render
from django.views import View
import pywbem
import json
from wbem.models import *
from wbem.forms import *

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
    form = ClassForm

    def get(self, request):

        self.form()

        return render(request, self.template, {
            'form': self.form,
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
