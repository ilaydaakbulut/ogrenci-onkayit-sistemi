from django.db import models
import os
from django.urls import reverse


def _handle_file_upload(instance, filename):
    name, extension = os.path.splitext(filename)
    return "file_storge/{}{}".format(instance.isim, extension)

class kayitislemi(models.Model):
    pesin = 'pesin odeme'
    taksit = 'taksitli ödeme'

    odemesecimi = [
        (1, '---'),
        (2, 'Peşin = 54.000 TL'),
        (3, '3 Taksit = 56.000 TL'),
        (4, '6 Taksit = 60.000 TL'),
        (5, '9 Taksit = 65.000 TL'),
    ]
    isim = models.CharField(max_length=100, blank=False, null=True,
                             verbose_name='Ad :', help_text='Adınızı giriniz.')
    soyad = models.CharField(max_length=100, blank=False, null=True,
                            verbose_name='Soyad :', help_text='Soyadınızı giriniz.')
    adres = models.TextField(max_length=1000, blank=False, verbose_name='Adres :',
                               null=True,help_text="Adresinizi giriniz.")
    dogum_tarihi = models.CharField(max_length=100, blank=False, null=True,
                             verbose_name='Dogum tarihi :', help_text='Doğum tarihinizi giriniz.')

    veli1 = models.CharField(max_length=100, blank=False, null=True,
                            verbose_name='1. Veli :', help_text='1. velinizi giriniz.')
    veli2 = models.CharField(max_length=100, blank=False, null=True,
                            verbose_name='2. Veli :', help_text='2. velinizi giriniz.')
    email = models.EmailField(max_length=50, null=True, verbose_name='E-posta :',
                              help_text="E-postanızı giriniz.")
    hobi = models.TextField(max_length=1000, blank=False, verbose_name='Hobi :',
                             null=True,help_text="Hobilerinizi giriniz.")
    telefon = models.CharField(max_length=100, blank=False, null=True,
                             verbose_name='Telefon :', help_text='Telefonunuzu giriniz.')
    image = models.ImageField(max_length=150,null=True,blank=True, verbose_name="Fotograf :",upload_to=_handle_file_upload)
    odeme = models.IntegerField( choices=odemesecimi, default=1, blank=False, null=True,
                                verbose_name='ödeme İşlemi :')

    class Meta: # kayit yapılacak yerin ismi ve neye göre sıralanacağı
        verbose_name_plural="Öğrenci Kayıtları"
        ordering = ['id']

    def __str__(self):   #veritabanında nasıl görüneceğini belirtir.
        return "%s %s" %(self.isim, self.soyad)
    def get_absolute_url(self):
        return reverse("ogrenci:ogrenci_kayit_id", kwargs={"id": self.id})


