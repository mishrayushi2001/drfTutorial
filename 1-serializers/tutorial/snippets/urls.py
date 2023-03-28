from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include

urlpatterns = [
    # path('snippets/', views.snippet_list),
    path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]