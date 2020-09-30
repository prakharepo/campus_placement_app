from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileViewForm
from .models import Profile
from django.http import JsonResponse

@login_required
def show_users(request):
    all_users = Profile.objects.all()
    offer = []
    for i in range(len(all_users)):
        if all_users[i].placed_in != 'NoOffer':
            offer.append(all_users[i])

    return render(request, "placement/show_offers.html", {'offers': offer})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        v_form = ProfileViewForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'v_form': v_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def delete_user(request, username):
    context = {}
    print(username)
    try:
        u = User.objects.get(id=username)
        u.delete()
        messages.success(request, f'Your account has been Deleted!!...Create New Account')
    except User.DoesNotExist:
        context['msg'] = 'User does not exist.'
    except Exception as e:
        context['msg'] = e.message

    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def validate_login(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        user_name = request.GET.get("username")
        # check for the user name in the database.
        if User.objects.filter(username=user_name).exists():
            return JsonResponse({"valid": True}, status=200)

        # if username not found, then user can't login.
        else:
            return JsonResponse({
                "valid": False,
                "msg": "This user do not exist. Please register."
            }, status=200)
    return JsonResponse({}, status=400)
