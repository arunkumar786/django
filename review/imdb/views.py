# Create your views here.
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from imdb.models import Movie
from django.http.response import HttpResponse

 
from imdb.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.db.models.aggregates import Count
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
            )
#             user.backend = 'django.contrib.auth.backends.ModelBackend'
#             user.is_staff = True
#             user.is_superuser = True
#             user.is_active = True
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )
        
@csrf_protect
def get_movieName(request):
    sum = 0; comments = " " 
    if request.method == 'POST':
        movie_form = MovieNameForm(request.POST)
        if movie_form.is_valid():
            movieName = movie_form.cleaned_data['movieName']
            try:
                obj = Movie.objects.all()
                obj1 = obj.filter(movieName=movieName)
            
                totalReviews = len(obj1)
                totalComments = len(obj1)
                # calculating avg rating for each movie;
                for indrating in obj1:
                    sum = sum + indrating.movieRating
                    comments = comments + indrating.comments  
                avgrating = sum / totalReviews    
            
#                 return HttpResponse("movieName is:"+movieName+"<br />" 
#                                 "avgRating is:"+str(avgrating)+"<br />"
#                                 "totalreviews:"+str(totalReviews)+"<br />"
#                                 "totalcomments:"+str(totalComments)+"<br />"
#                                 "listofComments:<br />"+comments+ "<br />"
#                                 )
                return render(request, "movielist.html", {'movieName':movieName,
                                                          'avgrating':avgrating,
                                                'totalReviews':totalReviews,
                                                'totalComments':totalComments,
                                                'obj':obj1})
            except Exception as arg:
                return HttpResponse("movie Doesn't exist")
            
    else:
        movie_form = MovieNameForm()
        
    return render(request, 'moviename.html' , {'movie_form':movie_form})

@csrf_protect
def addMovieReview(request):
    if request.method == "POST":
        addMovieForm = AddMovieReviewForm(data=request.POST)
        if addMovieForm.is_valid():
            try:
                movieName = addMovieForm.cleaned_data['movieName']
                movieReview = addMovieForm.cleaned_data['movieReview']
                movieRating = addMovieForm.cleaned_data['movieRating']
                movieComments = addMovieForm.cleaned_data['movieComments']
                newMovie = Movie.objects.create(movieName=movieName,
                                                movieRating=movieRating,
                                                movieReview=movieReview,
                                                comments=movieComments)
                newMovie.save()
                obj = Movie.objects.all()
                return render_to_response('successfullymovieadded.html')
                 
            except Exception as arg:
                return HttpResponse(arg)
        print(addMovieForm.errors)
    else:
        addMovieForm = AddMovieReviewForm()
    return render(request, "addmovie.html", {'addMovieForm':addMovieForm})