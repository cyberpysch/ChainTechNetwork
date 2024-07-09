from django.shortcuts import render, HttpResponseRedirect
from .models import OfferLetter

# Create your views here.
def index(request):
    if request.method=="POST":
        role= request.POST.get('role')
        KRA= request.POST.get('KRA')
        phone= request.POST.get('phone')
        salary= request.POST.get('salary')
        saveOfferLetter = OfferLetter(role=role, KRA=KRA, phone=phone, salary=salary)
        saveOfferLetter.save()
    data=OfferLetter.objects.all()

    return render(request, "app/index.html",{"data":data})