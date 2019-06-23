from django.shortcuts import render, redirect
from .models import Product
from .forms import CrudForm

# Create your views here.
def create(request):
    form=CrudForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crudapp:list')
    return render(request, 'crudapp/form.html',{'form':form})
def list(request):
    products=Product.objects.all()
    return render(request, 'crudapp/list.html',{'products':products})
def update(request,id):
    product=Product.objects.get(id=id)
    form=CrudForm(request.POST or None,instance=product)
    
    if form.is_valid():
        form.save()
        return redirect('crudapp:list')
    return render(request, 'crudapp/form.html',{'form':form,'product':product})

def delete(request,id):
    product=Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('crudapp:list')
    return render(request, 'crudapp/delete.html',{'product':product})
    

    
    
    