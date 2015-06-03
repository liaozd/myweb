from django import forms
from .models import YouTubeURL


class YouTubeURLForm(forms.ModelForm):
    request_url = forms.URLField(label='Paste the youtube URL:', max_length=200, help_text="Please enter the URL of the page.")

    class Meta:
        model = YouTubeURL