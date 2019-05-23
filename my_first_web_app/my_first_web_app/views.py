from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request):
    return HttpResponseRedirect('home')

def home_page(request):
    context = {"name": "Betty Maker"}
    response = render(request, "index.html", context)
    return HttpResponse(response)


def portfolio_page(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0, 100)
        image_urls.append(
            "https://picsum.photos/400/600/?image={}".format(random_number)
        )
    context = {"gallery_images": image_urls}
    response = render(request, "portfolio.html", context)
    return HttpResponse(response)


def gallery_page(request):
    return HttpResponseRedirect('../portfolio')


def about_me_page(request):
    context = {
        "skills": ["html", "css", "python"],
        "interests": ["web development", "responsive design"],
    }
    response = render(request, "about_me.html", context)
    return HttpResponse(response)


def favourites_page(request):
    context = {"fave_links": ["https://gitignore.io/"]}
    response = render(request, "favourites.html", context)
    return HttpResponse(response)
