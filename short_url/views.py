from django.shortcuts import render,redirect
from .models import short_urls
from .forms import UrlForm
from .short import shortener
from django.contrib.auth.decorators import login_required

# Create your views here.

def make(request,token):
    long_url = short_urls.objects.filter(short_url= token)[0]
    return redirect(long_url.long_url)


@login_required
def home(request):
    abc = short_urls.objects.filter(user = request.user)
    form = UrlForm(request.POST)
    a = ""
    myUrl = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortener().issue_token()
            NewUrl.short_url = a
            NewUrl.user = request.user
            NewUrl.save()
            myUrl = "http://127.0.0.1:8000/"+a

        else:
            form = UrlForm()
            a = "Invalid URL"
    return render(request,'index.html',{'form':form,'a':myUrl,'abc':abc,})
