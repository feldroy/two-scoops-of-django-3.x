"""
Using This Code Example
=========================
The code examples provided are provided by Daniel and Audrey Roy Greenfeld of
feldroy.com to help you reference Two Scoops of Django: Best Practices
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
Audrey Roy Greenfeld. Copyright 2020 Feldroy.com."

If you feel your use of code examples falls outside fair use of the permission
given here, please contact us at hi@feldroy.com.
"""

# events/models.py
from textwrap import dedent

from django.conf import settings
from django.core.mail import mail_admins
from django.db import models

from model_utils.models import TimeStampedModel

from .managers import EventManager

class Event(TimeStampedModel):

    class Status(models.IntegerChoices):
        STATUS_UNREVIEWED = 0, "Unreviewed"
        STATUS_REVIEWED = 1, "Reviewed"


    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.IntegerField(choices=Status.choices,
                                    default=Status.STATUS_UNREVIEWED)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    objects = EventManager()

    def notify_admins(self):
        # create the subject and message
        subject = "{user} submitted a new event!".format(
                        user=self.creator.get_full_name())
        message = dedentf"""TITLE: {self.title}
                  START: {self.start}
                  END: {self.end}""")

        # Send to the admins!
        mail_admins(subject=subject,
            message=message,
            fail_silently=False)
