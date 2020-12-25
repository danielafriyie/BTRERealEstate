from django.shortcuts import render
from Listings.models import Listing
from Realtors.models import Realtor
from Listings import choices


def index(request):
    listings = Listing.objects.order_by('-id').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': choices.state_choices,
        'bedroom_choices': choices.bedroom_choices,
        'price_choices': choices.price_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Ger all Realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # Get MVP realtors
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
