from django.views.generic import ListView, DetailView

from webapp.models import Photo


class IndexView(ListView):
    template_name = 'index.html'
    model = Photo
    context_object_name = 'photos'

    def session(self, request):
        print(request.session.items())

class PhotoView(DetailView):
    model = Photo
    template_name = 'detail.html'
    context_object_name = 'photo'

