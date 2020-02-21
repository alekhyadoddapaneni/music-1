from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from .models import Employee
from django.core.serializers import serialize
import json
from .forms import EmployeeForm

# Example to read 1 Employee record
class ReadOneEmployee(View):
    def get(self,request,emp_id):
        try:
            res = Employee.objects.get(idno=emp_id)
        except Employee.DoesNotExist:
            return HttpResponse(content_type="application/json",status=400)
        else:
            json_date = serialize("json",[res])
            return HttpResponse(json_date,content_type="application/json",status=200)

# Example to read all Employee record's
class ReadAllEmployees(View):
    def get(self,request):
        qs = Employee.objects.all()
        json_data = serialize("json",qs)
        return HttpResponse(json_data,content_type="application/json")


@method_decorator(csrf_exempt,name="dispatch")
class WriteOneEmployee(View):
    def post(self,request,*args,**kwargs):
        json_data = json.loads(request.body)
        emp = EmployeeForm(json_data)
        emp.save()
        json_data = json.dumps({"msg":"Details are saved"})
        return HttpResponse(json_data,content_type="application/json")

        # if emp.is_valid():
        #     emp.save()
        #     json_data = json.dumps({"message":"Details are saved"})
        #     return HttpResponse(json_data,content_type="application/json")
        # if emp.errors:
        #     json_data = json.dumps(emp.errors)
        #     return HttpResponse(json_data, content_type="application/json")
        #
        #
        #
        #





