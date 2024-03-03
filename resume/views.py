from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
# Create your views here.
def index(request):
    form=ResumeForm()
    condidate=Resume.objects.all()
    if request.method=="POST":
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    return render(request,"index.html",{"form":form,"condidate":condidate})
