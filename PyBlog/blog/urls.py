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
    path("post/<pk>/comment", views.add_comment_to_post, name="add_comment_to_post"),
    path("comments/<pk>/approve", views.comment_approve, name="comment_approve"),
    path("comments/<pk>/remove", views.comment_remove, name="comment_remove"),
    path("post/<pk>/publish", views.post_publish, name="post_publish"),
]

