"""GradingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    # This will take the user to the home screen page, which will prompt the user to sign up/ sign in (below).
    path('', include('homePage.urls')),
    path('login/', include('homePage.urls')),
    path('admin/', admin.site.urls),
    path('signup/', include('signUpPage.urls'), name='signup'),
    path('grades/', include('grades.urls')),
    path('newcourse/', include('newcourse.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
