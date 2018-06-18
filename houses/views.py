from django.http import HttpResponse 
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login 
from .forms import MyHouseEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . models import Myhouses
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.template import RequestContext

@login_required
def addlisting(request):    
    if request.method == 'POST': 
        house_form = MyHouseEditForm(request.POST, files=request.FILES, )
        if house_form.is_valid():    
            Houses = house_form.save(commit=False)
            Houses.author=request.user
            Houses.save()
            messages.success(request, 'Listing Created Succesfully successfully')
            return redirect('addlisting')           
    else:        
        house_form = MyHouseEditForm()
    return render(request, 'houses/addlisting.html', {'house_form':house_form},  )

                  
def edit(request):    
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST) 
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():            
            user_form.save()            
            profile_form.save()
            messages.success(request, 'Profile updated successfully') 
        else:            
             messages.error(request, 'Error updating your profile') 
    
    else:        
        user_form = UserEditForm(instance=request.user)        
        profile_form = ProfileEditForm(instance=request.user.profile) 

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})






@login_required
def listbyuser (request):
    house_list = Myhouses.objects.filter(author=request.user)
    profile = Profile.objects.all()
    return render(request, 'houses/ListingByUser.html', {'house_list':house_list,'profile': profile})

class UserListView(LoginRequiredMixin,generic.ListView):
    model = Myhouses
    template_name ='houses/ListingByUser.html'
    paginate_by = 9
    
    
    def get_queryset(self):
        return Myhouses.objects.filter(author=self.request.user)

class alllisting(LoginRequiredMixin,generic.ListView):
    model = Myhouses
    template_name ='houses/alllisting.html'
    paginate_by = 2


@login_required
def listbyuserdetails(request, id):
    house_list1 = Myhouses.objects.get(id = id)

    context = {
        'house_list1':house_list1
    }

    return render(request, 'houses/ListingByUserDetails.html', context)


def editlist2(request, pk):
    house_edit = get_object_or_404(Myhouses, pk = pk)
    if request.method == 'POST': 
        house_form = MyHouseEditForm(request.POST, files=request.FILES, instance=house_edit)
        if house_form.is_valid():    
            Houses = house_form.save(commit=False)
            Houses.save()
            messages.success(request, 'Listing Updated Succesfully')
            return redirect('editlist', pk)           
    else:        
        house_form = MyHouseEditForm(instance=house_edit)
    return render(request, 'houses/addlisting.html', {'house_form':house_form, 'house_edit': house_edit},  )


def deletelist(request, pk):
    house_delete = get_object_or_404(Myhouses, pk = pk)
    if request.user == house_delete.author:
        house_delete.delete()
        messages.success(request, 'Listing Deleted Succesfully')
        return redirect('userlist')
    else:
        return HttpResponse('unauthorized ACTIVITY')


def editlist(request, id):
    house_edit = Myhouses.objects.get(id = id)
    if request.method == 'POST': 
        house_form = MyHouseEditForm(request.POST, files=request.FILES, instance=house_edit)
        if house_form.is_valid():    
            Houses = house_form.save(commit=False)
            Houses.save()
            messages.success(request, 'Listing Updated Succesfully')
            return redirect('editlist', id)           
    else:        
        house_form = MyHouseEditForm()
    return render(request, 'houses/editlist.html', {'house_form':house_form},  )