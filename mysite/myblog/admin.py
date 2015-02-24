from django.contrib import admin
from . import models
from django.db.models import TextField
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget


class EntryAdmin(MarkdownModelAdmin):
    list_display = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}
    # http://arunrocks.com/recreating-the-building-a-blog-in-django-screencast/
    # python2.x should add this
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

# this is interesting, sync slug with title, when inputting in title
# by javascript
admin.site.register(models.Entry, EntryAdmin)
