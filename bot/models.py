from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nomi')
    
    def __str__(self):
       return self.name

    class Meta:
        verbose_name = ("Kurslar")
        verbose_name_plural = ("Kurslar")

class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ismi:')
    img = models.ImageField(upload_to='images', verbose_name='O\'qituvchi rasmi:')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kurs')
    about = models.TextField(verbose_name='O\'qituvchi haqida:')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("O'qituvchilar")
        verbose_name_plural = ("O'qituvchlar")


class About(models.Model):
    name = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, verbose_name='Bo\'lim')
    text = models.TextField(max_length=4096, verbose_name='Kurs haqida')
    img = models.ImageField(upload_to='images', verbose_name='Kurs uchun rasm')

    def __str__(self):
        return f'Kurslar haqida ({self.name})'
    
    class Meta:
        verbose_name = ("Kurslar haqida")
        verbose_name_plural = ("Kurslar haqida")
