from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from .models import TotalAcutalamount,ActualAmount
from django.db.models import Sum

# Create your views here.
def taxcal(request):
    
    finalvalue=0
    if request.method=='POST':
        amount=float(request.POST.get('amount'))
        tax=1.106470588
        actualAmount =float(amount)/tax
        finalvalue=round(actualAmount,2)
        actualAmount=ActualAmount.objects.create(totalamount=amount,tax=tax,actualamount=finalvalue)
        actualAmount.save()
        
        totalsum = ActualAmount.objects.aggregate(Sum('actualamount'))['actualamount__sum'] or 0
        
        total_sum=TotalAcutalamount.objects.update_or_create(id=1,defaults={'totalacutalamount':totalsum})
        return redirect(f"{reverse('taxcal')}?finalvalue={finalvalue}")
    finalvalue=request.GET.get('finalvalue')
    total_sum = TotalAcutalamount.objects.first()
    total_sum_value = total_sum.totalacutalamount if total_sum else 0
    
    items=ActualAmount.objects.all()
    return render(request,'main.html',{'finalvalue':finalvalue,'total_sum_value':total_sum_value,'items':items})

def removedata(request):
    data=ActualAmount.objects.all()
    data.delete()
    totalsum = ActualAmount.objects.aggregate(Sum('actualamount'))['actualamount__sum'] or 0
        
    TotalAcutalamount.objects.update_or_create(id=1,defaults={'totalacutalamount':totalsum})
    return redirect('taxcal')

def removeitem(request,id):
    data=ActualAmount.objects.get(id=id)
    data.delete()
    totalsum = ActualAmount.objects.aggregate(Sum('actualamount'))['actualamount__sum'] or 0
        
    TotalAcutalamount.objects.update_or_create(id=1,defaults={'totalacutalamount':totalsum})
    return redirect('taxcal')

