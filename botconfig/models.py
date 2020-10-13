from django.db import models
from django.utils import timezone

class SiteConf(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name='Vaqt')
    aboutschool = models.TextField(verbose_name='Maktab haqida')
    email = models.EmailField(verbose_name='Email')
    tel = models.CharField(max_length=120, verbose_name='Telefon')
    starttext = models.TextField(max_length=512, verbose_name='Start bosilganda chiqadigan matn')
    qoida = models.TextField(max_length=4096, verbose_name='Qoidalar')
    address = models.TextField(max_length=1024, verbose_name='Manzil')

    def __str__(self):
        return f'{self.tel}, {self.email}, => ({self.id})'
    
    class Meta:
        verbose_name = ("Bot sozlamalari")
        verbose_name_plural = ("Bot sozlamalari")
        
