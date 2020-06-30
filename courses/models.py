from django.db import models
from memberships.models import Membership
from django.contrib.auth.models import User
from django.urls import reverse

class Classe(models.Model):
    Titre = models.CharField(max_length=150)
    description = models.TextField(max_length= 200, null=True)
    image = models.ImageField(upload_to='cat_images', default='cat_images/default.jpg')

    def __str__(self):
        return '{}'.format(self.Titre)

class Sujets(models.Model):
    createur = models.ForeignKey(User,on_delete = models.CASCADE)
    slug = models.SlugField()
    Titre = models.CharField(max_length=30)
    classe = models.ForeignKey(Classe,on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    etabli = models.DateTimeField(auto_now=True)
    image_sujet = models.ImageField(upload_to='kurs_images', default='default.jpg')

    def __str__(self):
        return self.Titre

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_memberships(self):
        return self.courses.all()

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')




class Lesson(models.Model):
    slug = models.SlugField()
    Titre = models.CharField(max_length=30)
    cas = models.ForeignKey(Sujets,on_delete=models.CASCADE)
    video_id = models.CharField(max_length=11)
    position = models.IntegerField()

    def __str__(self):
        return self.Titre

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.cas.slug,'lesson_slug':self.slug})