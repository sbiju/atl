from django.conf.urls import url

from .views import HomePageView, AboutUsView, LandingPageView


urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name='land'),
    url(r'^home/$', HomePageView.as_view(), name='home'),
    url(r'^about/$', AboutUsView.as_view(), name='about_us'),
]
