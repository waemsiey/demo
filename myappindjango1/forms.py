#This one is like a specific class that handles the uploading of a form in java its just a class in a seperate file
from django import forms

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file = forms.FileField()