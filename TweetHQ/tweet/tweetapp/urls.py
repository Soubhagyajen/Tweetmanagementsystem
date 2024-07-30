from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('tweet/',views.home),
    # path('create/',views.create_tweet,name="create_tweet"),
    # path('<int:tweet_id>/edit/',views.edit_tweet,name="edit_tweet"),
    # path('<int:tweet_id>/delete/',views.delete_tweet,name="tweet_delete"),
    #  path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root URL for home view
    path('create/', views.create_tweet, name='create_tweet'),
    path('<int:tweet_id>/edit/', views.edit_tweet, name='edit_tweet'),
    path('<int:tweet_id>/delete/', views.delete_tweet, name='delete_tweet'),
    path('register/',views.Register,name='register'),
    #  path('like/<int:tweet_id>/', views.Like_tweets, name='like_tweet'),
    # path('unlike/<int:tweet_id>/', views.unlike_tweet, name='unlike_tweet'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)