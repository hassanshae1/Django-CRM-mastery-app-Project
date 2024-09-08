from django.shortcuts import render, HttpResponseRedirect

from enroll.models import User
from .forms import StudentRegistration
# Create your views here.
# THis Function to add students new
def add_show(request):
    if request.method == 'POST':
        # Create a form instance with the POST data
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # Extract cleaned data from the form
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            # Save the data to the database
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            # Reinitialize the form after saving the data
            fm = StudentRegistration()
    else:
        # Initialize a blank form if the method is not POST
        fm = StudentRegistration()
    
    # Retrieve all student registrations from the database
    stud = User.objects.all()
    
    # Render the template with the form and student data
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

#this function will delete data
def delete_data(request,id):
    if request.method == 'POST':
       pi = User.objects.get(pk=id) 
       pi.delete()
       return HttpResponseRedirect('/')
       
    