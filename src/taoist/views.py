from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView


class TaoistView(TemplateView):
    template_name = "taoist.html"
