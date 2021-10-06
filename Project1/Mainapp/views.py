from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from .forms import *
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# def home(request):
#     form = UserForm
#     mydict={
#         'form':form
#     }
#     return render(request,'index.html',context=mydict)
def register(request):
    if request.method=='POST':
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            phone=form.cleaned_data.get('phone_number')
            user.Meta.phone_number=phone
            user.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('blog-home')
        else:
            form = UserRegistrationForm()
        return render(request,'users/register.html',{'form':form})


# class UserViewSet(viewsets.ModelViewSet):
#     authentication_classes = (BasicAuthentication)
#     permission_classes = (IsAuthenticated,)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer