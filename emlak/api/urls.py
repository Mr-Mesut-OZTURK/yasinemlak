from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, EmlakList, EmlakDetail, api_root

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)

# router.register('emlak', EmlakList)
# router.register('emlak/<int:id>', EmlakDetail)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('emlak/', EmlakList.as_view()),
    path('emlak/<int:pk>', EmlakDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

# # API endpoints
# urlpatterns = format_suffix_patterns([
#     path('', api_root),

#     path('emlak/', EmlakList.as_view(), name='snippet-list'),
#     path('emlak/<int:pk>/', EmlakDetail.as_view(), name='snippet-detail'),
#     # path('emlak/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    
#     path('users/', UserViewSet.as_view(), name='user-list'),
#     # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
# ])