from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.utils import timezone

from products.models import Prod


@login_required(login_url='login')
def addproduct(request):
    if request.method=='POST':
        if request.POST['product_name'] and request.POST['product_desc'] and request.FILES['product_image'] and request.POST['product_url']:
            myprod= Prod()
            myprod.product_name = request.POST['product_name']
            myprod.product_desc = request.POST['product_desc']

            if request.POST['product_url'].startswith('http://') or request.POST['product_url'].startswith('http://'):
                myprod.product_url = request.POST['product_url']
            else:
                myprod.product_url='https://'+request.POST['product_url']

            myprod.product_image = request.FILES['product_image']
            myprod.product_pubdate = timezone.datetime.now()
            myprod.product_by = request.user
            myprod.save()

            return redirect('/product/'+str(myprod.id))
        else:
            return render(request, 'addproduct.html', {'error': 'Please Enter all correct details'})
    else:
        return render(request, 'addproduct.html')


def pdetails(request, myprod_id):
    prod = get_object_or_404(Prod, pk=myprod_id)
    return render(request, 'pdetails.html', {'myproduct' : prod})


@login_required(login_url='signup')
def hitlike(request, myprod_id):
    if request.method == 'POST':
        prod = get_object_or_404(Prod, pk=myprod_id)
        prod.product_likes+= 1
        prod.save()

        return redirect('/product/'+str(prod.id))



@login_required(login_url='signup')
def hitdislike(request, myprod_id):
    if request.method == 'POST':
        prod = get_object_or_404(Prod, pk=myprod_id)
        prod.product_dislikes += 1
        prod.save()

        return redirect('/product/'+str(prod.id))

def prodDelete(request, myprod_id):
    if request.method == 'POST':
        prod = get_object_or_404(Prod, pk=myprod_id)
        prod.delete()

        return redirect('home')

def about(request):

    return render(request,'about.html',{'msg' : 'Your Request or Service hasbeen sent successfuuly'})