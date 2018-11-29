from django import forms

class ResumeForm(forms.Form):
    sec_cert = forms.BooleanField()
    sec_skill = forms.BooleanField()
    sec_exp = forms.BooleanField()
    sec_ed = forms.BooleanField()

    cert_1 = forms.BooleanField()
    cert_2 = forms.BooleanField()
    cert_3 = forms.BooleanField()
    cert_4 = forms.BooleanField()

    skill_prog_1 = forms.BooleanField()