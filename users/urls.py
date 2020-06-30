from django.urls import path

from users.views import Profile, demande

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('demande/', demande, name='demande')

]
