from django import forms
from taoist.models import VideoUrl


class VideoUrlForm(forms.ModelForm):
    request_url = forms.URLField(label='Paste the youtube URL:',
                                 max_length=200,
                                 help_text='Please enter the URL of the page.')

    class Meta:
        model = VideoUrl
