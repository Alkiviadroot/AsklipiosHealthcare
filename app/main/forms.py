from django import forms
from .models import Asthenia,Xaraktiristika

class AstheniaForm(forms.ModelForm):
    class Meta:
        model = Asthenia
        fields = [
            'onoma',
            'orismos',
        ]