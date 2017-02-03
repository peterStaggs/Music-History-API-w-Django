from django.conf.urls import url, include
from rest_framework import routers
from music import views

# register each view to the router
router = routers.DefaultRouter()
router.register(r'Artist', views.ArtistViewSet)
router.register(r'Album', views.AlbumViewSet)
router.register(r'Genre', views.GenreViewSet)
router.register(r'Song', views.SongViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]