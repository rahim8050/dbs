
from pyexpat.errors import messages
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
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

    d1 = Deposit(amount=1000, status=True, customer=c1)
    d1.save()
    deposit_count = Deposit.objects.count()

    # return HttpResponse(f"Ok, Done, we have {customer_count} customers and {deposit_count} deposits")

@login_required
def customers(request):
    data = Customer.objects.all()
    data = Customer.objects.all().order_by('id').values()  # ORM select * from customers
    paginator = Paginator(data, 15)
    page = request.GET.get('page', 1)
    try:
        paginated_data = paginator.page(page)
    except  EmptyPage:
        paginated_data = paginator.page(1)
    return render(request, "customers.html", {"data": paginated_data})


@login_required
@permission_required('dbs.delete_customer', raise_exception=True)
def delete_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id) # select * from customers where id=7
    customer.delete() # delete from customers where id =
    return redirect('customers')

@login_required
@permission_required('dbs.add_customer',raise_exception=True)
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
    if request.method == 'GET':
     form = LoginForm()
     return render(request, "log_in.html", {"form": form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('customers')





@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


def customer_details(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    deposits = Deposit.objects.filter(customer=customer_id)
    return render(request,"details.html",{"deposits":deposits,"customer":customer})
