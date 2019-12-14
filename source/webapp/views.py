from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
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


class AddPhoto(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'create.html'
    fields = ['photo', 'note', 'like']

    def form_valid(self, form):
        self.object = self.model.objects.create(author=self.request.user, ** form.cleaned_data)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class EditPhoto(UserPassesTestMixin, UpdateView):
    model = Photo
    template_name = 'edit.html'
    context_object_name = 'photo'
    fields = ['photo', 'note', 'like']


    def test_func(self, **kwargs):
        photo = Photo.objects.get(pk=self.kwargs.get('pk'))
        if self.request.user == photo.author or self.request.user.has_change_permission('webapp.change_photo'):
            return True
        else:
            return False

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class DeletePhoto(UserPassesTestMixin, DeleteView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_photo'

    def test_func(self, **kwargs):
        photo = Photo.objects.get(pk=self.kwargs.get('pk'))
        if self.request.user == photo.author or self.request.user.has_perm('webapp.change_photo'):
            return True
        else:
            return False
