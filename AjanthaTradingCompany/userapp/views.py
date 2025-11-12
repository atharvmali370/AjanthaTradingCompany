from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class UserRegisterView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'userapp/register.html', context)
    
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ajantha:home')
