from django.urls import path
from .views import hello, HelloView
from .views import year_post, MonthPost, post_detail
from .views import my_view
from .views import TemplIf
from .views import view_for
from .views import index, about
from .views import author_posts, post_full

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    path('', my_view, name='index'),
    path('if/', TemplIf.as_view(), name='templif'),
    path('for/', view_for, name='templ_for'),
    path('about/', about, name='about'),
    path('index/', index, name='index'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full'),
]
