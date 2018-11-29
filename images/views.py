from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.http import limited_parse_qsl

from common.decorators import ajax_required
from .forms import ImageCreateForm
from .models import Image

@login_required
def image_create(request):
    if request.method == 'POST':
        #form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # create new Image instance but prevent it from being saved
            # to the DB by setting commit=False
            new_item = form.save(commit=False)

            #assign user to this item
            new_item.user = request.user
            # finally save the image object to the DB
            new_item.save()

            # display success message
            messages.success(request, 'Image added successfully')

            #redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # built form with data provided by the bookmarklet via GET
        
        form = ImageCreateForm(data=request.GET)
        
    return render(request,
                  'images/image/create.html', #template
                  {'section': 'images',     #context
                   'form':form})

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)

    total_likes = image.users_like.count()

    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image,
                   'total_likes': total_likes})
@ajax_required
@login_required
@require_POST #only allows the POST http verb
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})

@login_required
def image_list(request):
    images = Image.objects.all() #create QuerySet to return all images
    paginator = Paginator(images, 8) #retrieve 8 images per page.
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver first page
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            #If the request is AJAX and the page is out of range
            #return an empty page
            return HttpResponse('')
        #if page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'images/image/list_ajax.html',
                      {'section':'images','images':images})
    return render(request,
                  'images/image/list.html',
                  {'section':'images','images':images})
    
