from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor
from blog.views.blog import PostsGridView
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)



def blog(request):
    # Instantiate PostsGridView and get the queryset
    view = PostsGridView()
    view.request = request  # Set the request
    queryset = view.get_queryset()

    # Set the context with the queryset and other necessary data
    context = {
        'posts': queryset,
        'page_obj': view.paginate_queryset(queryset, view.paginate_by)[2],  # Adding pagination context
    }

    return render(request, 'blog/posts_grid.html', context)

