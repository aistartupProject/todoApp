from django.urls import path

from .views import posts, new_post, read_post, edit_post, delete_post, join, board_login, board_logout, review_list, search_view, review_detail

urlpatterns = [
    path('posts/', posts, name='posts'),
    path('new', new_post, name='new_post'),
    path('<int:id>', read_post, name='read_post'),
    path('<int:id>/edit', edit_post, name='edit_post'),
    path('<int:id>/delete', delete_post, name='delete_post'),
    path('join/', join, name='join'),
    path('login/', board_login, name='login'),
    path('logout/', board_logout, name='logout'),
    
    path('', review_list, name='review_list'),
    path('search/', search_view, name='search_view'),
    path('review/<str:name>/', review_detail, name='review_detail')
]