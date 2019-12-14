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


class EditPhoto(PermissionRequiredMixin, UpdateView):
    model = Photo
    template_name = 'edit.html'
    context_object_name = 'photo'
    fields = ['photo', 'note', 'like']
    permission_required = 'webapp.change_photo'

    # def test_func(self, **kwargs):
    #     if self.request.user.pk == self.model.author:
    #         print(self.model)
    #         return True
    #     else:
    #         return False

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class DeletePhoto(PermissionRequiredMixin, DeleteView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_photo'