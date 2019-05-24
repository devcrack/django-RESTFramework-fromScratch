from django.urls import include, re_path
from django.urls import path
#from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail
from .apiviews import ChoiceList, CreateVote

urlpatterns = [
    path('choices/', ChoiceList.as_view(), name='choice_list'),
    path('vote/', CreateVote.as_view(), name='create_vote'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='poll_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
]
# urlpatterns = [
#     path('choices/', ChoiceList.as_view(), name='choice_list'),
#     path('vote/', CreateVote.as_view(), name='create_vote'),
#     path('polls/', PollList.as_view(), name='poll_list'),
#     path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
# ]


