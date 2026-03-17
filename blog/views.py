from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST



# def home(request):
#     Students = [{'name':"Pravat"}, {'Redg':"1234"},{'cgpa':"7.5"}]
    
#     return render(request, "blog/base.html", context = {'Students':Students})


"""def post_detail(request):
    fruits = ['Apple', 'Banana', 'Mango', 'Orange']
    userName = "Prince"
    city = "Bhubanwesar"
    context = {
        'fruits':fruits,
        'username': userName,
        'city': city,
        'page_title': 'Welcome Home'
    }
    
    return render(request, 'blog/base.html', context)"""
    
"""def home(request):
    context = {
        'firstname': 'Pravat'
    }
    
    return render(request, 'blog/second.html', context)"""

"""def home(request):
    context = {'Prince': 100}
    return render(request, 'blog/third.html', context)"""
    
"""def home(request):
    context = {'DS': 'A', 'DAA': 'B', 'Graph Theory': 'A', 'System Programming': 'B'}
    return render(request, 'blog/fourth.html', {'context': context})    """
    
"""def ClassRoom(request):
    template = loader.get_template('blog/fifth.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    
    return HttpResponse(template.render(context, request))"""

"""def student_results(request):
    results = [
        {'student': 'Prince', 'subject':'Data Structures', 'marks':85},           
        {'student': 'Akshay', 'subject':'DAA', 'marks':78},
        {'student': 'Priyanshu', 'subject':'Graph Theory', 'marks':92},
        {'student': 'Sourav', 'subject':'System Programming', 'marks':81},
        {'student': 'Sohom', 'subject':'Data Structures', 'marks':88},
        {'student': 'Shivam', 'subject':'DAA', 'marks':91},
        {'student': 'Sambit', 'subject':'Graph Theory', 'marks':69},
        {'student': 'Rahul', 'subject':'System Programming', 'marks':78},
        {'student': 'Roahn', 'subject':'DAA', 'marks':93},
        {'student': 'Sujal', 'subject':'Graph Theory', 'marks':75},
        {'student': 'Pritam', 'subject':'System Programming', 'marks':86},
        {'student': 'Ronny', 'subject':'Data Structures', 'marks':91}]
    
    context = {
        'page_title': 'student_results - Semester 1', 
        'results': results,
        }
    
    return render(request, 'blog/results.html', context)"""
    
    
    
"""def post_list(request):
    posts = Post.objects.all()
    
    post_list = Post.objects.filter()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    except PageNotAnInteger:
        posts = paginator.page(1)   
    
    
    return render (
        request,
        'blog/post/list.html',
        {'posts': posts}
    )"""
    
class PostListView(ListView):
    
    """Alternative post list view"""

    queryset = Post.objects.filter(status = 'PB')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    
    
    
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    # Form for users to comment
    form = CommentForm()

    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post,
            'comments': comments,
            'form': form 
        }
    )
    
def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            
            subject = (
                f"{cd['name']} ({cd['email']}) "
                f"recommends you read {post.title}"
            )
            
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}\'s comments: {cd['comments']}"
            )

            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd['to']]
            )
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request,
        'blog/post/share.html',
        {
            'post': post,
            'form': form,
            'sent': sent
        }
)

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(
    Post,
    id=post_id,
    status=Post.Status.PUBLISHED
    )
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object without saving it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    return render(
        request, 
        'blog/post/comment.html',
        {
            'post': post,
            'form': form,
            'comment': comment
        }
    )
