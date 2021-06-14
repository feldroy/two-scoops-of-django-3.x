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

class UserManager(BaseUserManager):
    """In users/managers.py"""
    def create_user(self, email=None, password=None, avatar_url=None):
        user = self.model(
            email=email,
            is_active=True,
            last_login=timezone.now(),
            registered_at=timezone.now(),
            avatar_url=avatar_url
        )
        resize_avatar(avatar_url)
        Ticket.objects.create_ticket(user)
        return user

class TicketManager(models.manager):
    """In tasks/managers.py"""
    def create_ticket(self, user: User):
        ticket = self.model(user=user)
        send_ticket_to_guest_checkin(ticket)
        return ticket
