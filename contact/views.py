from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.


def contact_us(request):
    # code taken from ceciliabinck django tast-world-snacks
    """ View for rendering contact us page"""

    if request.method == "POST":
        if request.POST.get("txtName") and request.POST.get("txtEmail"):
            post = Contact()
            post.full_name = request.POST.get("txtName")
            post.email = request.POST.get("txtEmail")
            post.phone_number = request.POST.get("txtPhone")
            post.message = request.POST.get("txtMsg")
            post.save()

            subject = "STEPZ Contact Form"
            message = post.message = request.POST.get(
                "txtMsg") + " From: " + post.full_name + " Sender's Email Address " + post.email
            from_email = "stepz@example.com"
            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, ['tabita.mukoko@gmail.com'])
                except BadHeaderError:
                    return HttpResponse("Invalid Header Found")
                return render(request, "contact/contact_success.html")
            return HttpResponse("Make sure all fields are entered and valid.")
        return render(request, "contact/contact_success.html")
    return render(request, "contact/contact_us.html")


