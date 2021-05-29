from django import forms
from .models import Student
from .models import Employee


class stuForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


# using only form
class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name", max_length=50)
    lastname = forms.CharField(label="Enter last name", max_length=100)
    email = forms.EmailField(label="Enter Email")
    file = forms.FileField()  # for creating file input


# USING MODELFORM
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
