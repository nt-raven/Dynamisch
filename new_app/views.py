from django.shortcuts import render, redirect
from .models import *

# Create your views here.
# def index_view(request):
#     return render(request, "new_app/index.html")

# def index_form(request):
#     return render(request, "new_app/index.html")

def insert_page(request):
    return render(request, "new_app/index.html")

def insert_data(request):
    #comes data from form
    f_name = request.POST["f_name"]
    l_name = request.POST["l_name"]
    email = request.POST["email"]
    psd = request.POST["psd"]

    #creating object into model class
    # insert data into table                
    new_user = new_model.objects.create(first_name=f_name, last_name=l_name, email_id=email, emp_password=psd)

    # after insert render into show.html
    # return render(request, "new_app/show.html")
    # after render insert show_page view
    return redirect('show_page')
#show page view
def show_page(request):
    # select* from table
    all_data = new_model.objects.all()
    a=10
    print(a)
    return render(request, "new_app/show.html", {'key1': all_data, "key2": a})

def update_page(request, pk):
    #fetching data of perticuler id
    get_data = new_model.objects.get(id=pk)
    b = "ALL IS WELL"
    return render(request, "new_app/update.html", {'key3': get_data, 'key4': b})


#updating data entry from table in update_page     


def update_data(request, pk):
    update_data = new_model.objects.get(id=pk)
    update_data.first_name = request.POST['f_name']
    update_data.last_name = request.POST['l_name']
    update_data.email_id = request.POST['email']
    update_data.emp_password = request.POST['psd']
    #query to save data
    update_data.save()
    # render to show page
    return redirect('show_page')

#create function to delete data
def delete_data(request, pk):
    del_data =new_model.objects.get(id=pk)
    # query to delete data
    del_data.delete()
    return redirect('show_page')