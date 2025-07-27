from django.shortcuts import render
from django.http import HttpResponse

def profile(request):


   profile = request.user.profile
   context = {
      'profile' : profile
   }
   return render(request, 'accounts/profile.html', context)