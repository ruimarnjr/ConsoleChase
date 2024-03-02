from django.shortcuts import render

# Extracted from the Code Institute's Boutique Ado Walkthrough Project

def profile(request):
    """ Display the user's profile. """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)