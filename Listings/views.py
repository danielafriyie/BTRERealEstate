from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from Listings import choices


def listings(request):
    bt_listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(bt_listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'listings': paged_listings}
    return render(request, 'listing/listings.html', context)


def listing(request, listing_id):
    d_listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': d_listing
    }
    return render(request, 'listing/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-id')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    # Pagination
    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    context = {
        'state_choices': choices.state_choices,
        'bedroom_choices': choices.bedroom_choices,
        'price_choices': choices.price_choices,
        'listings': paged_listing,
        'values': request.GET
    }
    return render(request, 'listing/search.html', context)
