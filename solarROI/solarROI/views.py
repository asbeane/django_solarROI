from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.template.loader import get_template
from forms import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils import timezone
from models import *
import random, datetime, hashlib

# Create your views here.
### Base Home Page of Site/Application
def home(request):
    return render_to_response("home.html")


### Logging in and validating ###

# login function
def login(request):
    # c, for cotents.
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

# auth function with user and password POST requests
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    # if match return user object, else return none
    
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin/')
    else: return HttpResponseRedirect('/invalid/')
    

# It's peanut butter logged in time baby!
def loggedin(request):
     return render_to_response('loggedin.html',
                               {'full_name': request.user.username})
# you this login is invalid!
def invalid_login(request): 
    return render_to_response('invalid_login.html')

# byebye homies!
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

### Registration Section ###

# Register User baby, new user!
def register_user(request):
   args = {}
   args.update(csrf(request))
   if request.method == 'POST':
       form = CustomRegistrationForm(request.POST)
       args['form'] = form
       if form.is_valid(): 
           form.save()  # save user to database if form is valid
           username = form.cleaned_data['username']
           email = form.cleaned_data['email']
           salt = hashlib.sha1(str(random.random())).hexdigest()[:5]            
           activation_key = hashlib.sha1(salt+email).hexdigest()            
           key_expires = datetime.datetime.today() + datetime.timedelta(2)

           #Get user by username
           user = User.objects.get(username=username)

           # Create and save user profile                                                                                                                                  
           new_profile = UserProfile(user=user, activation_key=activation_key, 
                                     key_expires=key_expires)
           new_profile.save()

           # Send email with activation key
           email_subject = 'Account confirmation'
           email_body = "Salutations Solar Panel Enthusiast %s, thanks for signing up. To activate your account, click this link within 48hours http://0.0.0.0:8001/confirm/%s" % (username, activation_key)

           send_mail(email_subject, email_body, 'admin@solarROI.com',
                [email], fail_silently=False)

           #return HttpResponseRedirect('/register/register_success')
           return render_to_response('confirm.html')
   else:
       args['form'] = CustomRegistrationForm()

   return render_to_response('register.html', args, context_instance=RequestContext(request))




# registration sucess
def register_success(request, activation_key):
    #check if user is already logged in and if they are redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/home/')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.user
    user.is_active = True
    user.save()
    return render_to_response('register_success.html')


## Solar ROI Renderer ###
@login_required
def solarROI(request):
    return render_to_response('solarROI.html')
