
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    def clean_salary(self):
        sal = self.cleaned_data['salary']
        if sal < 50000:
            raise forms.ValidationError("Invalid Salary")
        return sal
    class Meta:
        model = Employee
        fields = "__all__"