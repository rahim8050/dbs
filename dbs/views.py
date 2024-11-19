from lib2to3.fixes.fix_input import context
from pyexpat.errors import messages

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request

from dbs.app_forms import CustomerForm, LoginForm
from dbs.models import Customer, Deposit


# Create your views here.
def test(request):
    # save a customer
    # c1 = Customer(first_name='Saida', last_name='Ali', email='saida@x.com', dob='2000-11-28', gender='Female', weight=62)
    # c1.save()
    #
    # c2 = Customer(first_name='Jake', last_name='Juma', email='juma@x.com', dob='1999-11-28', gender='Male', weight=62)
    # c2.save()

    customer_count = Customer.objects.count()

    c1 = Customer.objects.get(id=1)
    print(c1)

    # d1 = Deposit(amount=1000, status=True, customer=c1)
    # d1.save()
    # deposit_count = Deposit.objects.count()

    # return HttpResponse(f"Ok, Done, we have {customer_count} customers and {deposit_count} deposits")


def customers(request):
    data = Customer.objects.all().order_by('-id').values()
    return render(request,'customers.html',{'customers':data})



def delete_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id) # select * from customers where id=7
    customer.delete() # delete from customers where id =
    return redirect('customers')


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {"form": form})

# pip install django-crispy-forms
# pip install crispy-bootstrap5
def login_user(request):
     form = LoginForm()
     return render(request, "log_in.html", {"form": form})





def logout_user(request):
    return None