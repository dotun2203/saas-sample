from django.http import HttpResponse
from django.shortcuts import render
import pathlib

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)


def about_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    page_queryset = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_queryset.count() * 100.0) / queryset.count()
    except:
        percent = 0
    my_title = "My Page"
    html_template = "home.html"
   
    my_context ={
        "page_title":my_title,"total_visit_count":queryset.count(), "page_visit_count":page_queryset.count(), "percent": percent
    }
    return render(request, html_template, my_context)


def old_home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_= """
     <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Home</title>
    </head>
    <body>
        <h1>{page_title} anything?</h1>
    </body>
    </html>
""".format(**my_context)


    print(this_dir)
    # html_ = ''
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)

