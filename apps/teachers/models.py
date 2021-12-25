from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=350, verbose_name="Teacher name")
    teacher_photo = models.ImageField(
        upload_to="uploads/teachers_photos", verbose_name="Teacher photo"
    )
    teacher_degree = models.CharField(max_length=350, verbose_name="Teacher degree")
    teacher_experience = models.CharField(
        max_length=350, verbose_name="Teacher experience"
    )
    teacher_hobbies = models.CharField(max_length=350, verbose_name="Teacher hobbies")
    teacher_bio = models.TextField(verbose_name="Teacher bio")

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.teacher_name
