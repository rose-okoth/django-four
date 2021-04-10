from django.shortcuts import render, get_object_or_404, redirect
from .models import Neighborhood, Profile
from .forms import NeighborhoodForm, UserUpdateForm, ProfileUpdateForm
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

def create_post(request, hood_id):
    '''
    Function for user to create a neighborhood post
    '''
    hood = NeighbourHood.objects.get(id=hood_id)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            messages.success(request, "Post Successfully Created!")
            return redirect('single-hood', hood.id)

    context = {
        'form': PostForm()
        }

    return render(request, 'post.html', context)

def neighborhood_detail(request,slug=None):
    '''
    A function for showcasing the details of a neighborhood
    
    '''
    instance = get_object_or_404(Project, slug=slug)
    share_string = quote_plus(instance.description)
    reviews = Review.objects.filter()
    
    # average1 = reviews.aggregate(Avg("design_rating"))["design_rating__avg"]
    # average2 = reviews.aggregate(Avg("usability_rating"))["usability_rating__avg"]
    # average3 = reviews.aggregate(Avg("content_rating"))["content_rating__avg"]
    # average = (average1 + average2 + average3) / 3

    # if average == None:
    #     average = 0
    # average = round(average, 2)

    context = {
            "title":instance.name,
            "instance":instance,
            "share_string":share_string,
            # "instance": instance,
            # "reviews": reviews,
            # "average": average,
        }

    return render(request, "hood_detail.html", context)