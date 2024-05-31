from django import forms
from .models import Upload  # If using model for uploads

class UploadForm(forms.Form):
    file = forms.FileField(required=True, allow_empty_File=False,
                            mimetypes=['application/vnd.ms-excel', 'data/csv'])
    # Add other validation rules as needed

    from django import forms

#class UploadFileForm(forms.Form):
# file = forms.FileField(label='Upload File')

