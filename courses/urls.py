from django.urls import path
from django.contrib.auth.decorators import login_required

from courses.views import HomeView,AboutView,ContactView,CourseListView, CourseDetailView,LessonDetailView, SearchView, Creer_Classes, Creer_Sujets, Creer_Apprentissage

app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('courses/<int:category>', CourseListView, name='course_list'),
    path('courses/<slug>/', login_required(CourseDetailView.as_view()), name='course_detail'),
    path('courses/<course_slug>/<lesson_slug>/', login_required(LessonDetailView.as_view()), name='lesson_detail'),
    path('search/', SearchView, name='kerko_kurs'),
    path('creer/classes', Creer_Classes, name='creer_classes'),
    path('creer/sujets', Creer_Sujets, name='creer_sujets'),
    path('creer/apprentissage', Creer_Apprentissage, name='creer_apprentissage')
]
