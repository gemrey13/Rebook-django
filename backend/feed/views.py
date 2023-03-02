from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


from .models import *




def home(request):
	posts = Post.objects.all()[:2]
	current_user_id = request.user.id

	if request.method == "POST" and 'login_btn' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			error_message = 'Invalid username or password'


	elif request.method == "POST" and "post_btn" in request.POST:
		title = request.POST['title']
		content = request.POST['content']
		image = request.FILES['image']
		post = Post(author=request.user, title=title, content=content, image=image)

		post.save()
		return redirect('home')

	elif request.method == "POST" and 'signup_btn' in request.POST:
		username = request.POST['username']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 != password2:
			error_message = 'Password does not match'
			

		elif User.objects.filter(username=username).exists(): 
			error_message = 'Username already exists!'


		elif User.objects.filter(email=email).exists():
			error_message = 'Email already exists!'
			

		elif password1 == password2:
			password = make_password(password1)
			user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
			user.save()
			error_message = 'You are now register!'
			
	else:
		error_message = ''

	return render(request, 'feed/home.html', {
		'posts':posts,
		'error_message': error_message,
		'current_user_id': current_user_id
		})

