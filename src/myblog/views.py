from django.views import generic
from myblog.models import Entry


class BlogIndex(generic.ListView):
    queryset = Entry.objects.published()
    template_name = 'home.html'
    paginate_by = 10


class BlogDetail(generic.DetailView):
    model = Entry
    template_name = 'post.html'
