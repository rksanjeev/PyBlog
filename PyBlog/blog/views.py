from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy
from blog import models, forms
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class AboutView(TemplateView):
    template_name = "about.html"


class PostListView(ListView):
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(
            published_date__lte=timezone.now()).order_by("-published_date")
        


class PostDetaiilView(DetailView):
    model = models.Post


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redeirect_field_name = "blog/post_detail.html"
    form_class = forms.PostForm
    model = models.Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    redeirect_field_name = "blog/post_detail.html"
    form_class = forms.PostForm
    model = models.Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Post
    success_url = reverse_lazy("post_list")


class DraftListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    redeirect_field_name = "blog/post_list.html"
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(published_date__isnull=True).order_by(
            "created_date"
        )
