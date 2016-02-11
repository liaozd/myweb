from django import forms
from taoist.models import VideoUrl


class VideoUrlForm(forms.ModelForm):
    request_url = forms.URLField(label='',
                                 widget=forms.TextInput(attrs={'placeholder': 'YouTube URL Link Here'}),
                                 max_length=300,
                                 )

    class Meta:
        model = VideoUrl
        fields = ['request_url']
