from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from listings.choices import price,state,bedrooms

def listings(req):
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listing,6)
    page = req.GET.get('page')
    pageobj = paginator.get_page(page)
    return render(req,'listings/listings.html',{'listings' : pageobj})

def listing(req,listing_id):
    listing = get_object_or_404(Listing,pk = listing_id)





    return render(req,'listings/listing.html',{
        'listing':listing
    })

def search(req):

    queryset = Listing.objects.order_by('-id')
    if 'keywords' in req.GET:
        keyword = req.GET['keywords']
        if keyword:
            queryset = queryset.filter(description__icontains=keyword)

    if 'city' in req.GET:
        city = req.GET['city']
        if city:
            queryset = queryset.filter(city__icontains=city)

    if 'state' in req.GET:
        statee = req.GET['state']
        if statee:
            queryset = queryset.filter(state__iexact=statee)

    if 'bedrooms' in req.GET:
        bedroomsq = req.GET['bedrooms']
        if bedroomsq:
            queryset = queryset.filter(bedrooms__lte=bedroomsq)

    if 'price' in req.GET:
        pricee = req.GET['price']
        if pricee:
            queryset = queryset.filter(price__lte=pricee)

    return render(req,'listings/search.html',{
        'bedrooms': bedrooms,
        'price': price,
        'state': state,
        'listings':queryset,
        'values':req.GET
    })