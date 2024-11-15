
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path('ADMIN/', admin.site.urls),
    path('',include('tweet.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
      path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
