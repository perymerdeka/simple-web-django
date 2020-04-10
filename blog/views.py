from django.views import generic
from .models import Post

# Create your views here.
class PostListView(generic.ListView):
    queryset        = Post.objects.filter(status=1).order_by('-created')
    template_name   = 'blog/index.html'
    paginate_by     = 3

class PostDetailView(generic.DetailView):
    model           = Post
    template_name   = 'blog/post_detail.html'
