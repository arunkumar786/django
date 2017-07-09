'''
Created on 02-Jul-2017

@author: root
'''
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from imdb.models import Movie

movies = [tuple([x.movieName,x.movieName]) for x in Movie.objects.all()]

uniqueSetOfMovies = list(set(movies))

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,6)]
 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
    
class MovieNameForm(forms.Form):
    
    movieName = forms.CharField(label='MovieName', max_length=100,
                                )
    
class AddMovieReviewForm(forms.Form):
    
    movieName = forms.CharField(label='MovieName', max_length=100)
    movieReview = forms.CharField(label='MovieReview',
                                  required=True,
                                  widget=forms.Textarea)
    movieComments = forms.CharField(label='Comments',
                                    required=True,
                                    widget=forms.Textarea)
    movieRating = forms.IntegerField(label="MovieRating", 
                            widget=forms.Select(choices=INTEGER_CHOICES))