from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.processing_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls', namespace='posts')),
    path('users/', include('users.urls', namespace='users')),
    path('comments/', include('comments.urls', namespace='comments')),
    path('auth/', include('django.contrib.auth.urls')),
    path('pages/', include('pages.urls', namespace='pages')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('posts:index'),
        ),
        name='registration',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
