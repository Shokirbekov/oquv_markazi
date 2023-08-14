from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import *

class HomeView(View):
    def get(self, request):
        data = {
            "data": Profile.objects.get(user=request.user),
            "lesson": LessonProfile.objects.filter(profil__user=request.user),
            "grade": Grade.objects.all()
        }
        return render(request, "home.html", data)

class OneLessonView(View):
    def get(self, request, id):
        lesson = get_object_or_404(Lesson, id=id)
        grades = Grade.objects.filter(lesson=lesson).order_by('-day')
        payment = Tolov.objects.filter(profil__user=request.user)  # Include Tolov data here
        data = {
            "lesson": lesson,
            "grade": grades,
            "name": Profile.objects.get(user=request.user),
            "payment": payment
        }
        return render(request, "lesson.html", data)

class ProfileView(View):
    def get(self, request):
        data = {
            "profile": Profile.objects.get(user=request.user),
            "lesson": LessonProfile.objects.filter(profil__user=request.user)
        }
        return render(request, "profile.html", data)

class PaymentView(View):
    def get(self, request):
        data = {
            "tolov": Tolov.objects.filter(profil__user=request.user),
            "name": Profile.objects.get(user=request.user)
        }
        return render(request, "payment.html", data)