from django.http import HttpResponseRedirect
from django.shortcuts import render

from taoist.forms import YouTubeURLForm


def fgfw(request):
    if request.method == 'POST':
        form = YouTubeURLForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/thanks/')
        else:
            print form.errors
    else:
        form = YouTubeURLForm()

    return render(request, 'fgfw.html', {'form': form})