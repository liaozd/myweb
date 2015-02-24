from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin


# class EntryAdmin(admin.ModelAdmin):
class EntryAdmin(MarkdownModelAdmin):
    list_display = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}

# this is interesting, sync slug with title, when inputting in title
# by javascript
# http://arunrocks.com/recreating-the-building-a-blog-in-django-screencast/
admin.site.register(models.Entry, EntryAdmin)
