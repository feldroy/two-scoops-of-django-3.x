"""
Using This Code Example
=========================
The code examples provided are provided by Daniel and Audrey Feldroy of
Feldroy to help you reference Two Scoops of Django: Best Practices
for Django 3.x. Code samples follow PEP-0008, with exceptions made for the
purposes of improving book formatting. Example code is provided "as is", and
is not intended to be, and should not be considered or labeled as "tutorial
code".

Permissions
============
In general, you may use the code we've provided with this book in your
programs and documentation. You do not need to contact us for permission
unless you're reproducing a significant portion of the code or using it in
commercial distributions. Examples:
* Writing a program that uses several chunks of code from this course does
    not require permission.
* Selling or distributing a digital package from material taken from this
    book does require permission.
* Answering a question by citing this book and quoting example code does not
    require permission.
* Incorporating a significant amount of example code from this book into your
    product's documentation does require permission.
Attributions usually include the title, author, publisher and an ISBN. For
example, "Two Scoops of Django: Best Practices for Django 3.x, by Daniel and
Audrey Feldroy. Copyright 2020 Feldroy."

If you feel your use of code examples falls outside fair use of the permission
given here, please contact us at hi@feldroy.com.
"""

# sprinkles/views.py
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Sprinkle
from .utils import check_sprinkles

def sprinkle_list(request: HttpRequest) -> HttpResponse:
    """Standard list view"""

    request = check_sprinkles(request)

    return render(request,
        "sprinkles/sprinkle_list.html",
        {"sprinkles": Sprinkle.objects.all()})

def sprinkle_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """Standard detail view"""

    request = check_sprinkles(request)

    sprinkle = get_object_or_404(Sprinkle, pk=pk)

    return render(request, "sprinkles/sprinkle_detail.html",
        {"sprinkle": sprinkle})

def sprinkle_preview(request: HttpRequest) -> HttpResponse:
    """Preview of new sprinkle, but without the
            check_sprinkles function being used.
    """
    sprinkle = Sprinkle.objects.all()
    return render(request,
        "sprinkles/sprinkle_preview.html",
        {"sprinkle": sprinkle})
