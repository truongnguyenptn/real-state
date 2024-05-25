from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from ..models import Post, Comment
from ..forms import CommentForm, DeleteCommentForm

class PostsGridView(views.ListView):
    paginate_by = 3
    model = Post
    template_name = 'blog/posts_grid.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')


class PostDetailView(views.DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']
        comments_count = len(post.comment_set.all())

        context['comment_form'] = CommentForm(
            initial={'post_slug': self.object.slug, }
        )
        context['comments'] = post.comment_set.all()
        context.update({
            'comments_count': comments_count,
        })

        return context


class PostCommentView(auth_mixins.LoginRequiredMixin, views.View):
    permission_required = 'blog.add_comment'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        post = Post.objects.get(slug=self.kwargs['slug'])
        comment = Comment(
            text=form.cleaned_data['text'],
            post=post,
            user=self.request.user,
        )
        comment.save()

        return redirect('post detail', post.slug)

    def form_invalid(self, form):
        pass


class PostCommentDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Comment
    form_class = DeleteCommentForm
    template_name = 'blog/delete_comment.html'

    def get_success_url(self):
        return reverse_lazy('post detail', kwargs={'slug': self.object.post.slug})
