from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.filter(status=Post.Status.PUBLISHED).count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-publish')[:count]
    return {'latest_posts': latest_posts}