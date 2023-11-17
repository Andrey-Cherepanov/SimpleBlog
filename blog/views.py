from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'post':posts})

def post_detail(request, id):
    post = get_object_or_404(Post,
                             id=id,
                             ststus=Post.Status.Published)

    return render(request,
                  'blog/post/detail.html',
                  {'post':post})
