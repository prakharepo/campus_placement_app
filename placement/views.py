from django.shortcuts import render
from .models import company, Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, "placement/index.html")

def show_campus(request):
    return render(request, "placement/show_campus.html")

def show_company(request):
    all_companies = company.objects.all()
    return render(request, "placement/show_company.html", {'companies': all_companies})
@login_required
def show_description(request, company_id):
    # print(company_id)
    all_companies = company.objects.get(pk=company_id)
    return render(request, "placement/show_description.html", {'companies': all_companies})

def announcement(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'placement/announcement.html', context)