from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


from posts.models import Post
from comments.models import Comment
from .forms import CommentForm


User = get_user_model()


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('blog:post_detail', pk=pk)


@login_required
def edit_comment(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    form = CommentForm(request.POST or None, instance=comment)

    if request.user != comment.author:
        return redirect('blog:post_detail', pk=pk)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=pk)

    return render(request, 'blog/comment.html',
                  {'form': form, 'comment': comment, 'pk': pk})


@login_required
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post_id = comment.post.pk

    if request.user == comment.author:
        if request.method == 'POST':
            comment.delete()
            return redirect('blog:post_detail', pk=post_id)

    return render(request, 'blog/comment.html',
                  {'comment': comment, 'post_id': post_id})
