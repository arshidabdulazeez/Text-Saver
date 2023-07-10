from django.urls import path
from .views import *

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('snippets-overview/', SnippetOverview.as_view(), name='snippet_create'),
    path('snippets-details/<int:pk>/', SnippetDetails.as_view(), name='snippet_details'),
    path('snippets-create/', SnippetCreate.as_view(), name='snippet_create'),
    path('snippets-update/<int:pk>/', SnippetUpdate.as_view(), name='snippet_update'),
    path('snippets-delete/<int:pk>/', SnippetDelete.as_view(), name='snippet_delete'),
    
    path('tag-list/', TagList.as_view(), name='tag_list'),
    path('tag-details/<int:pk>/', TagDetails.as_view(), name='tag_details'),
]
