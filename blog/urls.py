from django.urls import path

from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # Lista de posts (e lista filtrada por tag)
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),

    # Um post
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail',
    ),

    # Compartilhar por e-mail e comentar
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),

    # Feed RSS
    path('feed/', LatestPostsFeed(), name='post_feed'),

    # Busca de texto completo (SO com PostgreSQL). Ative junto com a
    # view post_search e a SearchForm, quando for usar o PostgreSQL:
    # path('search/', views.post_search, name='post_search'),
]
