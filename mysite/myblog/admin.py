from django.contrib import admin
from . import models


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}

# this is interesting, sync slug with title, when inputting in title
# by javascript
admin.site.register(models.Entry, EntryAdmin)
