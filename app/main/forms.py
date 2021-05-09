from django import forms
from . import models

class AstheniaForm(forms.ModelForm):
    class Meta:
        model = models.Asthenia
        fields = [
            'onoma',
            'orismos',
        ]