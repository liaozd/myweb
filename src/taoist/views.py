from django.views.generic import CreateView

from .models import VideoUrl
from .forms import VideoUrlForm


class TaoistView(CreateView):
    model = VideoUrl
    form_class = VideoUrlForm
    template_name = 'taoist.html'
    success_url = '/taoist/'
