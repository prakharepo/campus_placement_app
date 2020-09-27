from django.shortcuts import render
from .models import company, Post, application
from django.contrib import messages
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
@login_required
def apply_job(request, company_id):
    current_user = request.user
    print(current_user)
    comp = company.objects.get(pk=company_id)

    try:
        entry = application(name=current_user, applied_in=comp)
        entry.save()
        messages.success(request, f'You have applied to ' + comp.company_name + ' job profile')
    except:
        messages.success(request, f'You have ALREADY applied to ' + comp.company_name + ' job profile')


    all_companies = company.objects.all()
    return render(request, "placement/show_company.html", {'companies': all_companies})

@login_required
def your_app(request):
    current_user = request.user
    app = application.objects.all()
    user_app = []
    for i in range(len(app)):
        if app[i].name == current_user:
            user_app.append(app[i])
    return render(request, "placement/your_app.html", {'apps':user_app})