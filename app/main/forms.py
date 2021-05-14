from django import forms
from django.forms.models import inlineformset_factory
# from django.forms.models
from . import models

class AstheniaForm(forms.ModelForm):
    class Meta:
        model = models.Asthenia
        fields = [
            'onoma',
            'orismos',
        ]

AstheniaXaraktitistikaFormset = inlineformset_factory(models.Asthenia ,models.Xaraktiristika, fields=('xaraktiristiko',))
AstheniaSxoleioFormset = inlineformset_factory(models.Asthenia ,models.Sxoleio, fields=('odigia',))
AstheniaEkpedeftikoiFormset = inlineformset_factory(models.Asthenia ,models.Ekpedeftikoi, fields=('odigia',))
AstheniaGoneisFormset = inlineformset_factory(models.Asthenia ,models.Goneis, fields=('odigia',))
AstheniaPerisoteraFormset = inlineformset_factory(models.Asthenia ,models.Perisotera, fields=('link',))

