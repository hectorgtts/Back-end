
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leaderboardv1/', include('leaderboardv1.urls')),  # Make sure 'leaderboardv1.urls' is correctly pointing to your app's urls.py
    # other paths...
]
