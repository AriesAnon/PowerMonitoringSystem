from django.shortcuts import render
from power_monitoring_system_chart.models import AppliancesManagement
from django.db.models import Sum
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def power_monitor_chart(request):
    labels = []
    data = []

    queryset = AppliancesManagement.objects.order_by('-appliancerating')[:5]
    for appliance in queryset:
        labels.append(appliance.appliancename)
        data.append(appliance.appliancerating)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
