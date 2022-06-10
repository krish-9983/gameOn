from django.shortcuts import render
"""
render html pages
"""



def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, 'about_us.html')