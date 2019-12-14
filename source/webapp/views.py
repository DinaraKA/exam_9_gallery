from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Photo


class IndexView(ListView):
    template_name = 'index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ['-created_at']

    def session(self, request):
        print(request.session.items())

class PhotoView(DetailView):
    model = Photo
    template_name = 'detail.html'
    context_object_name = 'photo'


class AddPhoto(CreateView):
    model = Photo
    template_name = 'create.html'
    fields = ['photo', 'note', 'like', 'author']

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class EditPhoto(UpdateView):
    model = Photo
    template_name = 'edit.html'
    context_object_name = 'photo'
    fields = ['photo', 'note', 'like', 'author']


    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class DeletePhoto(DeleteView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:index')