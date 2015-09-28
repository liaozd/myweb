from django.contrib import admin
from myblog.models import Entry, Tag
from django.db.models import TextField
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget


class EntryAdmin(MarkdownModelAdmin):
    # ref:https://github.com/arocks/qblog
    list_display = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}
    # http://arunrocks.com/recreating-the-building-a-blog-in-django-screencast/
    # python2.x should add this
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

# this is interesting, sync slug with title, when inputting in title
# by javascript
admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
