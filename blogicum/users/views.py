from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView, UpdateView
)

from posts.models import Post
from constants import PUBLICATION_COUNT
from .forms import ProfileUpdateForm


User = get_user_model()


class ProfileListView(ListView):
    template_name = 'blog/profile.html'
    context_object_name = 'profile'
    paginate_by = PUBLICATION_COUNT

    def get_queryset(self):
        profile = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(
            author=profile
        ).annotate(comment_count=Count('comments')).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(
            User,
            username=self.kwargs['username']
        )
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'blog/user.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('blog:profile', args=[self.kwargs['username']])
