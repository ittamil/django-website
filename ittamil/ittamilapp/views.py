from django.shortcuts import render, get_object_or_404, redirect
from ittamilapp.forms import CommentForm, UserDashBoardForm, RegistrationForm,EditProfileForm
#from ittamilapp.models import CommentModel, PostModel
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from ittamilapp.models import Comment, PostModel


def PostView(request):
    queryset = PostModel.objects.filter(status=1).order_by("-created_on")
    paginate_by = 5
    return render(request,'index.html',{'post':queryset})

#def PostDetailView(request, slug):
#    post = get_object_or_404(PostModel, slug=slug)
#    
#    comments = post.comments.filter(active=True).order_by("-created_on")
#  
#    new_comment = None
#    if request.method == "POST":
#        comment_form = CommentForm(data=request.POST)
#        if comment_form.is_valid():
#            new_comment = comment_form.save(commit=False)
#            new_comment.post = post
#            new_comment.save()
#    else:
#        comment_form = CommentForm()
#    return render(
#        request,
#        'post_detail.html',
#        {
#            "post": post,
#           
#            "comments": comments,
#            "new_comment": new_comment,
#            "comment_form": comment_form,
#        },
#    )
#

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegistrationForm()
    context = {
        'form':form
    }    
    return render(request,'registration/signup.html',context)

    

@login_required
def profile(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserDashBoardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserDashBoardForm()
    context = {
        'form':form
    }   
    return render(request,'user_dashboard.html',context)  

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm()
    context = {
        'form':form
    }   
    return render(request,'edit_profile.html',context)    

def LikeView(request, slug):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    if request.is_ajax():
        return HttpResponseRedirect(reverse('PostView', args=slug))
        html = render_to_string('index.html', context, request=request)
        return JsonResponse({'form': html})
   

def PostDetailView(request,  slug):
    post = get_object_or_404(PostModel,  slug=slug)
    comments = post.comments.order_by("-created_on")
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
            comment.save()
            # return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form= CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
#    if request.is_ajax():
#        html = render_to_string('comments.html', context, request=request)
#        return JsonResponse({'form': html})

    return render(request, 'post_detail.html', context)