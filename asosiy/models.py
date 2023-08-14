from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    J = [
        ("Monday, Wednesday, Friday", "Monday, Wednesday, Friday"),
        ("Tuesday, Wednesday, Friday", "Tuesday, Wednesday, Friday"),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    days = models.CharField(max_length=100, choices=J)

    def __str__(self):
        return self.name

class Profile(models.Model):
    J = [
        ("Male", "Male"),
        ("Female", "Female")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_info")
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=100, choices=J)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    J = [
        ("Male", "Male"),
        ("Female", "Female")
    ]

    profil = models.ForeignKey(Profile, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices=J)
    city = models.CharField(max_length=100)


class Grade(models.Model):
    J = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5")
    ]

    Y = [
        ("Lesson", "Lesson"),
        ("Homework", "Homework")
    ]

    profil = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_info")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson_items")
    grade = models.CharField(max_length=100, choices=J)
    type = models.CharField(max_length=200, choices=Y, null=True)
    day = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.profil.name}, {self.lesson.name}({self.grade})"

class Class(models.Model):
    name = models.CharField(max_length=100)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson_item")

    def __str__(self):
        return self.name

class Tolov(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson_tolov")
    profil = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.profil.name}, {self.lesson.name} to'lov"


class LessonProfile(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson_info")
    profil = models.ForeignKey(Profile, on_delete=models.CASCADE)
    klass = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="class_info", null=True)
    tolov = models.ForeignKey(Tolov, on_delete=models.CASCADE, related_name="tolov_info", null=True)