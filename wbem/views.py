from django.shortcuts import render
from django.views import View
import pywbem
import json
from wbem.models import *

# Create your views here.
class Dashboard(View):
    template = 'wbem/dashboard.html'

    def get(self, request):

        data = ["Linux", "v2", "76345"] * 3

        # server_url = 'http://ttm4128.item.ntnu.no:5988/root/cimv2'
        #server_url = Options.objects.first().server_url
        server_url = 'http://ttm4128.item.ntnu.no:5988/cimom'

        conn = pywbem.WBEMConnection(server_uri)

        # server = pywbem.WBEMServer(conn)

        classnames = conn.EnumerateClassNames(DeepInheritance=False)
        print(classnames)

        instances = conn.EnumerateInstances('CIM_Processor')


        return render(request, self.template, {
            "data": data,
            "classnames": classnames,
        })
