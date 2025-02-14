#Views are the connector for the web in java springboot its like a controller 
from django.http import HttpResponse
from django.shortcuts import render
from .models import TodoItems
from .forms import UploadFileForm
from .utils import uploaded_file
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    return render(request, "home.html")

#This is for the todo
def todos(request):
    items = TodoItems.objects.all()
    return render(request, "todo.html", {"todos": items})

#This is for the uploading the file

def upload_csv_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['file']

            try:
                csv_content = uploaded_file(csv_file)
                return render(request , 'viewfile.html', {'csv_content' : csv_content})
            
            except ValidationError  as e:
                return render(request, 'fileupload.html', {'form': form, 'error': str(e) })
        else:
            return render(request, 'fileupload.html', {'form': form , 'error': "Invalid submission"})
    else:
        form = UploadFileForm()
    return render(request, 'fileupload.html', {'form':form})