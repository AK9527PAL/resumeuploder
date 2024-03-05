from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from .forms import ResumeForm
from .models import Resume
from .pdf import html2pdf
# Create your views here.
def index(request):
    form=ResumeForm()
    condidate=Resume.objects.all()
    if request.method=="POST":
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    return render(request,"index.html",{"form":form,"condidate":condidate})

def condidate(request,pk):
    condidate=Resume.objects.get(pk=pk)
    return render(request,"condidate.html",{"condidate":condidate})

def pdf(request):
    con="condidate.html"
    pdf=html2pdf(con)
    return HttpResponse(pdf,content_type="application/pdf")
