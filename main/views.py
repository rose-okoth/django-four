from django.shortcuts import render, get_object_or_404, redirect
from .models import Neighborhood, Profile, Business, Post
from .forms import NeighborhoodForm, UserUpdateForm, ProfileUpdateForm, PostForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from urllib.parse import quote_plus

def home(request):
    return render(request, 'index.html')

def hood(request):
    '''
    A function for showcasing the list of neighborhoods
    
    '''
    queryset = Neighborhood.objects.all()   

    context = {
            "title":"Hoods",
            "object_list":queryset
        }

    return render(request,"hood.html", context)

def new_hood(request):
    '''
    A function for creating new neighborhoods
    
    '''
    form = NeighborhoodForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user.profile
        instance.save()
        messages.success(request, "Hood Successfully Created!")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form":form,
    }

    return render(request,"new_hood.html",context)

def user_profile(request):
    '''
    A function for creating the user profile and updating
    
    '''
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Successfully Updated!')
            return redirect('main:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    profile = request.user.profile.neighborhood.all

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': profile
    }

    return render(request, 'profile.html', context)

def create_post(request, slug=None):
    '''
    A function for adding posts
    
    '''
    hood = Neighborhood.objects.get(slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.hood = hood
            post.save()
            messages.success(request, "Post Successfully Created!")
            return redirect('main:detail', slug)
    else:
        form = PostForm

    return render(request,'post.html', {'form': form, 'hood': hood})

def neighborhood_detail(request,slug=None):
    '''
    A function for showcasing the details of a neighborhood
    
    '''
    instance = get_object_or_404(Neighborhood, slug=slug)
    

    context = {
            "title":instance.name,
            "instance":instance,
        }

    return render(request, "hood_detail.html", context)