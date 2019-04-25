from django import forms
from .models import ComplainBox


class ComplainForm(forms.ModelForm):
    class Meta:
        model = ComplainBox
        fields = ('fullname', 'postal', 'phone', 'msg')
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'postal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'type': 'tel'}),
            'msg': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type Your Problem'})
    }
