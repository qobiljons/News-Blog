from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.shortcuts import redirect

# Create your views here.

#
# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(request, username=data["username"], password=data["password"])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse("Good login")
#                 else:
#                     return HttpResponse("Your profile is not active!")
#             else:
#                 return HttpResponse("Password or username is incorrect!")
#         return HttpResponse("Please fill the form correctly otherwise i may think you an an asshole")
#
#     else:
#         form = LoginForm()
#         context = {
#             "form": form
#         }
#     return render(request, "registration/login.html", context=context)


def logout_view(request):
    logout(request)
    return redirect("login")
