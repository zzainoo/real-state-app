from django.shortcuts import render , redirect
from .models import Contact
from django.contrib import messages
# from django.core.mail import send_mail

def contact(req):
    if req.method == 'POST':
        listing_id2 = req.POST['listing_id']

        listing = req.POST['listing']
        name = req.POST['name']
        email = req.POST['email']
        phone = req.POST['phone']
        message = req.POST['message']
        user_id = req.POST['user_id']
        # realtor_id = req.POST['realtor_id']
        if req.user.is_authenticated:
            user_id = req.user.id
            has_cont = Contact.objects.all().filter(listing_id=listing_id2,user_id=user_id)
            if has_cont:
                messages.add_message(req, messages.ERROR, "You are already added")
                return redirect('/listings/' + listing_id2)

        cont = Contact(listing=listing,listing_id=listing_id2,name=name,email=email,phone=phone,message=message,user_id=user_id)
        cont.save()



        # send_mail(
        #     'Subject here',
        #     'Here is the message.',
        #     'from@example.com',
        #     ['to@example.com'],
        #     fail_silently=False,
        # )
        messages.add_message(req,messages.ERROR,"You are added")

    return redirect('/listings/' + listing_id2)

