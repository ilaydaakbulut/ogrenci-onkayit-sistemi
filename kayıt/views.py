from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import Kayit
from django.contrib import messages

def ogrenci_kayit(request): #veritabanına girilen verileri kaydetme

    form =Kayit(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"succesfully")
        return HttpResponseRedirect(instance.get_absolute_url())
    context ={
        "form": form,
    }
    return render(request,'kayitlar/ogrenci-kayit.html',context)



def ogrenci_viewt(request,id): #veritabanına girilen verileri kaydetme

    context ={
    }
    return render(request,'kayitlar/ogrenci-kayit.html',context)


