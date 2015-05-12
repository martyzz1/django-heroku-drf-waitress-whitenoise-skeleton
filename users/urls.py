from django.conf.urls import url, patterns, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'accounts', views.UserView)   # user-list

urlpatterns = patterns(
    '',
    url(r'^api/v1/auth/token/', 'rest_framework_jwt.views.obtain_jwt_token', name='api-auth-token'),
    url(r'^api/v1/auth/social/(?P<backend>[^/]+)/$', views.SocialTokentoJWT.as_view(), name='api-auth-social'),
    url(r'^api/v1/', include(router.urls)),

)
