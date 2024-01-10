# urls.py

from django.urls import path
from .views import essay_list, add_comment , add_essay ,comment_approval_page,update_essay,delete_essay

urlpatterns = [
    path('', essay_list, name='essay_list'),
    path('essays/add/', add_essay, name='add_essay'),
    path('comment-approval/', comment_approval_page, name='comment_approval_page'),
    path('update_essay/<int:pk>',update_essay,name='update_essay'),
    path('delete_essay/<int:pk>',delete_essay,name='delete_essay'),

    path('essays/<int:essay_id>/add_comment/', add_comment, name='add_comment'),
]
