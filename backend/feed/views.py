from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import *






def home(request):
	posts = Post.objects.all()[:2]

	if request.method == "POST":
		title = request.POST['title']
		content = request.POST['content']
		image = request.FILES['image']
		post = Post(title=title, content=content, image=image)
		post.save()
		return redirect('home')

	return render(request, 'feed/home.html', {
		'posts':posts
		})

