from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *




def home(request):
	posts = Post.objects.all()
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

	else:
		error_message = ''

	return render(request, 'feed/home.html', {
		'posts':posts,
		'error_message': error_message,
		'current_user_id': current_user_id
		})

