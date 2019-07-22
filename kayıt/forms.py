from django import forms
from .models import kayıtislemi

class Kayit(forms.ModelForm):
    class Meta:
        model = kayıtislemi
        fields = ['isim', 'soyad','dogum_tarihi','veli1','veli2','telefon','adres',
                  'email','hobi','image','odeme']

    def __init__(self, *args, **kwargs):
        super(Kayit, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['adres'].widget = forms.Textarea(attrs={'class': 'form-control'})
        self.fields['hobi'].widget = forms.Textarea(attrs={'class': 'form-control'})


