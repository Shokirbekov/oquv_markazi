from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('lesson/<int:id>/', OneLessonView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('payments/', PaymentView.as_view()),
]
