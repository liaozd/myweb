from django import forms
from taoist.models import VideoUrl


class VideoUrlForm(forms.ModelForm):
    request_url = forms.URLField(label='Input YouTube Link',
                                 max_length=300,
                                 )

    class Meta:
        model = VideoUrl
        fields = ['request_url']
