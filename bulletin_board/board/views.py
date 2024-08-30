from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, ResponseForm, ResponseAcceptForm
from .models import Post, Response
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = '-date_create'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class ResponseList(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Response
    ordering = '-date_create'
    template_name = 'responses.html'
    context_object_name = 'responses'
    paginate_by = 10


class ResponseToMyAdsList(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Response
    ordering = '-date_create'
    template_name = 'responses_to_my_ads.html'
    context_object_name = 'responses_to'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_update.html'


class ResponseCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ResponseForm
    model = Response
    template_name = 'response_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_details', kwargs={'pk': self.kwargs['pk']})


class ResponseDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Response
    template_name = 'response.html'
    context_object_name = 'response'


class ResponseAccept(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = ResponseAcceptForm
    model = Response
    template_name = 'response_accept.html'


class ResponseDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Response
    template_name = 'response_delete.html'
    success_url = reverse_lazy('responses_to_list')
