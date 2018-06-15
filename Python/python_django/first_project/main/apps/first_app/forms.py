from django import form

class UploadFileForm(forms.Form):
    title = forms.Charfield(max_length=50)
    file = forms.FileField()