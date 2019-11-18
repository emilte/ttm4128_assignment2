from django.shortcuts import render
from django.views import View
import pywbem
import json
from wbem import models as wbem_models
from wbem import forms as wbem_forms
import os
import easysnmp

# Create your views here.
class Dashboard(View):
    template = 'wbem/dashboard.html'

    def get(self, request):

        data = ["Linux"] * 4

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
            'urlpatterns': urls.urlpatterns,
            'urlnames': urlnames,
        })

class System(View):
    template = 'wbem/system.html'

    def get(self, request, system):
        result = {}

        # print(system)

        # -------------------- CIM --------------------
        server_url = 'http://ttm4128.item.ntnu.no:5988/cimom'

        conn = pywbem.WBEMConnection(server_url)

        result1 = conn.EnumerateInstances(ClassName='CIM_OperatingSystem')[0].properties['ElementName'].value
        result2 = conn.EnumerateInstances(ClassName='CIM_System')[0].properties['ElementName'].value
        result3 = conn.EnumerateInstances(ClassName='CIM_Processor')[0].properties['ElementName'].value

        #print(result3.properties['ElementName'].value)

        #element = result1.properties['ElementName'].value
        parsed = {i.split("=")[0]: i.split("=")[1].replace('"','') for i in result1.split('" ')}


        result['os_name'] = parsed['NAME']
        result['os_version'] = parsed['VERSION']
        result['system'] = result2
        result['processor'] = result3

        # -------------------- END: CIM --------------------

        # -------------------- SNMP --------------------
        session = easysnmp.Session(hostname='demo.snmplabs.com:161', community='public', version=2)

        l = session.get('sysLocation.0')
        result['snmp'] = l.value

        # -------------------- END: SNMP --------------------

        return render(request, self.template, {
            'iterable': True,
            'result': result,
        })




class Dynamic(View):
    template = 'wbem/dynamic.html'
    form = None
    iterable = False

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
                import inspect
                # This is because empty field is '' instead of None
                input = [field or None for field in data.values()]
                # Order of input is important
                result = getattr(conn, form.method)(*input)

                try: result, self.iterable = result.__dict__, True
                except: pass


                # print(inspect.isclass( type(result) ))
                # print(type(result))


                # def dictify(d):
                #     for k, v in d.items():
                #         if v:
                #             if type(v) not in [list, dict, str]:
                #                 v = v.__dict__
                #                 d[k] = dictify(v)
                #     return d
                #
                # result = dictify(result.__dict__)


                # if type(result) not in [list, dict, str]:
                #     self.iterable = True
                #     result = result.__dict__
                #     print(type(result))
                #     for k, v in result.items():
                #         print(k)
                #         if v:
                #             if type(v) not in [list, dict, str]:
                #                 result[k] = v.__dict__

                # try:
                #     self.iterable = True
                #     result = result.__dict__
                #     for k, v in result.items():
                #         print(k)
                #         try:
                #             result[k] = v.__dict__
                #             try:
                #                 for k2, v2 in result[k].items():
                #                     print(k2)
                #                     try: result[k][k2] = v2.__dict__
                #                     except: print("1")
                #             except: print("2")
                #         except: print("3")
                # except: print("4")




            except Exception as e:
                print(e)
                result = e

        return render(request, self.template, {
            'iterable': self.iterable,
            'form': form,
            'result': result,
        })

class Network(View):

    template = 'wbem/dynamic.html'
    form = None

    def get(self, request, system):
	    form=self.form()
	   # f = os.popen("/usr/bin/wbemcli ei 'http://ttm4128.item.ntnu.no:5988/root/cimv2:CIM_IPProtocolEndpoint' -nl | grep -oP '^-ElementName=\K.*'")
	    #interfaces = f.read()
	    return render(request, self.template, {'form':form})

    def post(self, request, system):


        interface_names = {'lo':'IPv4_lo', 'eth0':'IPv4_eth0'}
        result_string = ""

        form = self.form(request.POST)
        result = None

		#eth0 or lo
        interface=request.POST.get('interfaces_choice')
        interface_info = request.POST.getlist('interface_info_pre')

        if interface == 'lo':
            CIMinterface='IPv4_lo'
            iface_type = "Linux_LocalLoopbackPort"
        if interface == 'eth0':
            CIMinterface='IPv4_eth0'
            iface_type = "Linux_EthernetPort"

        if form.is_valid():
            data = form.cleaned_data
            try:
                import inspect
                for item in interface_info:
                    if 'mac_address' == item:
	                    print("MAC address:\n")
	                    f = os.popen("""/usr/bin/wbemcli ei 'http://ttm4128.item.ntnu.no:5988/root/cimv2:%s.SystemCreationClassName="Linux_ComputerSystem",SystemName="ttm4128.item.ntnu.no",CreationClassName=\'%s',DeviceID="lo"' -nl | grep -oP '^-PermanentAddress=\K.*'""" % (iface_type, iface_type))
	                    mac_address = f.read()
	                    print(mac_address)
	                    result_string += "\n" + "MAC address:\n" + mac_address + "\n"
                    if 'general' == item:
	                    print("General info:\n")
	                    f = os.popen("""/usr/bin/wbemcli gi 'http://ttm4128.item.ntnu.no:5988/root/cimv2:Linux_IPProtocolEndpoint.Name="%s",SystemCreationClassName="Linux_ComputerSystem",SystemName="ttm4128.item.ntnu.no",CreationClassName="Linux_IPProtocolEndpoint"' -nl""" % CIMinterface)
	                    info = f.read()
	                    result_string += "\n" + "General info:\n" + info + "\n"
	                    print(info)
                # Order of input is important

                try: result, self.iterable = result.__dict__, True
                except: pass
            except Exception as e:
                print(e)
                print("ERROR")
                result = e
        return render(request, self.template, {'form':form, 'result':result_string})
	   # return render(request, self.template)
