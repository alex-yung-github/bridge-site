from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from csv import writer

# Create your views here.

def home(request):
    return HttpResponse("This is the home page")

@csrf_exempt
def log_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        computing_ID = data.get('computingID')
        todayDate = date.today()

        logInformation = [todayDate, first_name, last_name, computing_ID]
        with open('AttendenceLog.csv','a', newline='') as log:
            writerObject = writer(log)
            writerObject.writerow(logInformation)
            log.close()

        print(logInformation)

        response = {"received": True}

        return JsonResponse(response, safe=False)
    return JsonResponse({"error": "Invalid request method"}, status=400)