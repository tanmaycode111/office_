from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from . models import Employee
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.
@login_required
def IndexView(request):
    return render(request,'office/index.html')

class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('office:list_employee')

class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employee_list'

class EmployeeDetailView(DetailView):
    model = Employee
    

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields  = '__all__'
    success_url = reverse_lazy('office:list_employee')

class EmployeeDeleteView(DeleteView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('office:list_employee')

class SignUpView(CreateView):
    form_class = UserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'office/signup.html'

def userview(request):
    userdetails = Employee.objects.all()
    context = {'userdeatil':userdetails}
    return render(request,'office/userdetail.html',context)