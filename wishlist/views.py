from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from .models import Wishlist
from profiles.models import UserProfile


@login_required
def wishlist(request):
    """
    A view to render the user's wishlist
    """
    wishlist = None
    try:
        profile_user = UserProfile.objects.get(user=request.user)
        wishlist = Wishlist.objects.filter(profile_user=profile_user)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context=context)


@login_required
def add_to_wishlist(request, product_id):

    """
    Add a product in your wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    Wishlist.objects.create(
        profile_user=user,
        product=product
    )
    messages.info(
        request, f'{product.name} has been added to your Wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))
