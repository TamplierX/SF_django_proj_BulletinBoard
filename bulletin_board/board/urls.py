from django.urls import path

from .views import (PostList, PostDetail, ResponseList, ResponseToMyAdsList, PostCreate, PostUpdate, ResponseCreate,
                    ResponseDetail, ResponseDelete, ResponseAccept)


urlpatterns = [
    path('', PostList.as_view(), name='posts_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_details'),
    path('my_responses', ResponseList.as_view(), name='responses_list'),
    path('responses_to_my_ads', ResponseToMyAdsList.as_view(), name='responses_to_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/response/', ResponseCreate.as_view(), name='response_create'),
    path('response/<int:pk>', ResponseDetail.as_view(), name='response_detail'),
    path('response/<int:pk>/delete', ResponseDelete.as_view(), name='response_delete'),
    path('response/<int:pk>/accept', ResponseAccept.as_view(), name='response_accept')
]
