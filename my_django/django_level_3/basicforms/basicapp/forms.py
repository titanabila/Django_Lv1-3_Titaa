from django import forms
from django.core import validators

# Pengecekan, misalnya harus dimulai dengan huruf A
def check_for_a(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError("Name needs to start with A")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Input your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        # Mengambil data yang sudah dibersihkan dengan super().clean()
        all_clean_data = super(FormName, self).clean()
        
        # Mendapatkan email dan verify_email dengan .get() untuk menghindari KeyError
        email = all_clean_data.get('email')
        vemail = all_clean_data.get('verify_email')

        # Cek apakah kedua email diisi dan sama
        if email and vemail and email != vemail:
            raise forms.ValidationError("Make sure emails match!")
