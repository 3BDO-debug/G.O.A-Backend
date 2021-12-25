from django.db import models
from teachers.models import Teacher

# Create your models here.


class Class(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name="Class teacher"
    )
    class_name = models.CharField(max_length=350, verbose_name="Class name")
    class_category = models.CharField(max_length=350, verbose_name="Class category")
    class_cover = models.ImageField(
        upload_to="uploads/class_covers", verbose_name="Class cover"
    )
    class_lessons = models.IntegerField(verbose_name="Class lessons numbers")
    class_students = models.IntegerField(verbose_name="Class students")
    years_range = models.CharField(max_length=350, verbose_name="Years range")
    difficulty = models.CharField(max_length=350, verbose_name="IQ diffiulty")

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.class_name


class ClassDescription(models.Model):
    related_class = models.ForeignKey(
        Class, on_delete=models.CASCADE, verbose_name="Related class"
    )
    body = models.TextField(verbose_name="Description body")
    image = models.ImageField(
        upload_to="uploads/class_descriptions_images", verbose_name="Description image"
    )

    class Meta:
        verbose_name = "Class description"
        verbose_name_plural = "Class descriptions"

    def __str__(self):
        return f"Class description for {self.related_class.class_name}"
