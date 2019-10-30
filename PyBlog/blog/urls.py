from django.urls import path, include
import blog.views as views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("post/add/", views.PostCreateView.as_view(), name="post_new"),
    path("post/<pk>/", views.PostDetaiilView.as_view(), name="post_detail"),
    path("post/<pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("post/<pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("drafts/", views.DraftListView.as_view(), name="post_drafts"),
]

