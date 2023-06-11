from django.shortcuts import render,redirect,get_object_or_404
from . models import Crud

# Create your views here.
def add(request):
    task=Crud.objects.all()
    if request.method == 'POST':
        slno=request.POST.get('slno','')
        itemname=request.POST.get('itemname','')
        desc=request.POST.get('desc','')
        crud=Crud(slno=slno,itemname=itemname,desc=desc)
        crud.save()
    return render(request,'index.html',{'crud':task})

def delete(request,task_id):
    task1=Crud.objects.get(id=task_id)
    if request.method == 'POST':
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')


def Update(request,task_id1):
    task=get_object_or_404(Crud,id=task_id1)
    if request.method=='POST':
        task.slno=request.POST.get('slno')
        task.item_name=request.POST.get('item_name')
        task.desc=request.POST.get('desc')
        task.save()
        return redirect('/')
        # task=task.objects.all()
    return render(request,'update.html',{'task':task})