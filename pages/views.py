from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price,state,bedrooms


def index(req):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[0:3]




    return render(req,'pages/index.html',{
        'listings':listings,
        'bedrooms':bedrooms,
        'price' : price,
        'state' : state
    })

def about(req):
    realtors = Realtor.objects.order_by('-id')

    mvp = Realtor.objects.all().filter(is_mvp=True)



    return render(req,'pages/about.html',{
        'realtors':realtors,
        'mvp':mvp,
    })