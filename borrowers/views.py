import requests
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from allauth.socialaccount.models import SocialAccount, SocialToken


def list(request):
    fb_id = SocialAccount.objects.filter(
        user=request.user,
        provider='facebook'
    ).first()
    social_token = SocialToken.objects.filter(
        account__user=request.user,
        account__provider='facebook'
    ).first()
    uid = fb_id.uid
    token = social_token.token
    print uid, token
    base_url = 'https://graph.facebook.com/v2.5/'
    basic_info = '{base_url}{fb_uid}?fields=id,name,picture,education,work&format=json'.format(base_url=base_url)
    plus_token = '{basic_info}&access_token={token}'.format(basic_info=basic_info, token=token)
    r = requests.get(plus_token)
    print r.status_code
    print r.json()['name']
    print r.json()['picture']['url']


class LandingPageView(TemplateView):
    template_name = "index.html"


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutUsView(TemplateView):
    template_name = "about_us.html"