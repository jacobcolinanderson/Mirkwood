from django.contrib import admin

# Register your models here.
from .models import Item, Person

#admin.site.register(Item)
#admin.site.register(Person)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'race', 'personality')
    list_editable = ('name', 'race', 'personality')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'owner')
    list_editable = ('name', 'description', 'owner')