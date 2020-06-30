from django import forms
from django.contrib.auth.models import User
from .models import Classe, Sujets, Lesson



class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = '__all__'
        help_texts = {
            'Titre': 'Par exemple. Classe 11 ou classe d informatique',
            'description':'Mettez une brève description de la classe',
            'image':'Vous pouvez placer une photo de classe ou la laisser vierge'
        }

class SujetForm(forms.ModelForm):
    class Meta:
        model = Sujets
        fields = ['createur','slug', 'Titre', 'classe', 'description', 'image_sujet']
        help_texts = {
            'Titre': 'Par exemple. Mathématiques, géographie, etc.',
            'description':'Mettez une brève description du sujet',
            'classe':'Sélectionnez la classe pour laquelle vous allez créer le sujet',
            'image_sujet':'Vous pouvez publier une photo du sujet ou la laisser vierge'
        }
        labels = {
            'Titre':'Titre de cours'
        }
        widgets = {'createur': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class MesimiForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','Titre', 'cas', 'video_id', 'position', ]
        help_texts = {
            'Titre':'Définissez le titre de la leçon',
            'cas':'Choisissez le sujet auquel appartient cette leçon',
            'video_id':'Définissez l ID vidéo de Youtube que vous téléchargerez (<a href="/media/youtube_help.png">où puis-je trouver une pièce d identité</a>)',
            'position':'Définir le numéro de position ou la file d attente d apprentissage '
        }
        widgets = {
            'slug': forms.HiddenInput()
        }
