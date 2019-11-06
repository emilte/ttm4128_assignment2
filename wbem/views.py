from django.shortcuts import render
from django.views import View

# Create your views here.
class Dashboard(View):
    template = 'wbem/dashboard.html'

    def get(self, request):
        data = ["Linux", "v2", "76345"] * 3
        return render(request, self.template, {"data": data})
