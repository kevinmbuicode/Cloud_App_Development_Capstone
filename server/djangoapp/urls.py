from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp/'
urlpatterns = [
    # route is a string contains a URL pattern

    # path for login

    # path for logout
    path('djangoapp/', views.home_page, name='djangoapp'),

    path('add_review/', views.add_review, name='add_review'),
    path('djangoapp/add_review', views.add_review, name='add_review'),

    path('dealer_details/', views.get_dealer_details, name='dealer_details'),
    path('djangoapp/dealer_details/',
         views.get_dealer_details, name='dealer_details'),

    path('registration/', views.registration_request, name='registration'),
    path('djangoapp/registration/',
         views.registration_request, name='registration'),

    path('about/', views.about, name='about'),
    path('djangoapp/about', views.about, name='about'),

    path('contact/', views.contact, name='contact'),
    path('djangoapp/contact/', views.contact, name='contact'),

    path('logout/', views.logout_request, name='logout'),
    path('logout/logout', views.logout_request, name='logout'),
    path('djangoapp/logout/', views.logout_request, name='logout'),

    path(route='', view=views.get_dealerships, name='index'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''paths appear twice I understand, but the first ones are the ones I configured in knowledge of the user may..
     input the website url and add a path directly rather than getting inside the website/homedirectory to..
     access an inner/already known path eg 'domain_name/contact.'''
