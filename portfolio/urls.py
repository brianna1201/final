from django.urls import path
from django.contrib import admin
import portfolio.views

urlpatterns = [
    path('', portfolio.views.portfolio, name='portfolio'),
    path('admin/', admin.site.urls),
]