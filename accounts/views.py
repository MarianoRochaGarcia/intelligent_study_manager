from django.shortcuts import render
from .forms import UserForm, ProfileImageForm
from django.shortcuts import redirect

def profile(request):
   
   profile = request.user.profile
   
   if request.method == "POST":
      form = ProfileImageForm(request.POST, request.FILES, instance=profile)
      if form.is_valid():
         form.save()
         return redirect('profile')
   else: 
      form = ProfileImageForm(instance=profile)
      
   context = {
      'profile' : profile,
      'form': form
   }
   return render(request, 'accounts/profile.html', context)

def profile_edit(request):
   profile = request.user.profile
   user = profile.user
   if request.method == 'GET':
      form = UserForm(instance=user)
      context = {
         'form': form,
         'user': user
      }
      return render(request,'accounts/profile_edit.html', context)
   if request.method == 'POST':
      form = UserForm(request.POST, instance=user)
      if form.is_valid():
         form = form.save()
         return redirect('profile')

def profile_delete(request):
   user = request.user
   user.delete()
   return redirect('login_view')