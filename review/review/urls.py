from django.conf.urls import include, url
from django.contrib import admin
from imdb.views import logout_page, register, register_success, home,\
    get_movieName, addMovieReview
#from imdb.views import signup

urlpatterns = [
    # Examples:
    # url(r'^$', 'review.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^signup/$', signup, name='signup'),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page, name='login'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^register/$', register, name='register'),
    url(r'^register/success/$', register_success, name='success'),
    url(r'^home/$', home, name='home'),
    url(r'^moviename/$', get_movieName, name='getmovie'),
    url(r'^addmovie/$', addMovieReview, name='movie'),
]
