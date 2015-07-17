from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post 
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/home.html', {'posts' : posts})
    
def solarsystem(request):
    return render(request, 'blog/solarsystem.html',{})

def post_detail(request,priKey):
    onePost = get_object_or_404(Post,pk=priKey)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    x = False
    x2 = "Alde"
    x3 = False
    return render(request, 'blog/home.html', {'onePost' : onePost,'x':x,'x2':x2,'x3':x3,'justonepost' : posts[0]})

def post_new(request):
	if(request.method == "POST"):
		form = PostForm(request.POST)
		if(form.is_valid()):
				post = form.save(commit=False)
				post.author = request.user
				post.published_date = timezone.now()
				post.save()
				return post_detail(request,post.pk)
	else:
		form = PostForm()
		return render(request,'blog/post_edit.html',{'form' : form})

def post_edit(request,priKey):
	post = get_object_or_404(Post, pk=priKey)
	if(request.method == "POST"):
		form = PostForm(request.POST, instance=post)
		if(form.is_valid()):
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return post_detail(request,post.pk)
	else:
		form = PostForm(instance=post)
		return render(request,'blog/post_edit.html',{'form' : form})