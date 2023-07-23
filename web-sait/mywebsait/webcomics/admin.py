from django.contrib import admin


from .models import *


class ComicsAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'slug', 'photo', 'file_pdf', 'content', 'time_create', 'time_update',  'is_published')
	list_display_link = ('id', 'title' )
	search_fields = ('title', 'content')
	ist_editable = ('is_published',)
	list_filter = ('is_published', 'time_create')
	prepopulated_fields = {"slug": ("title",)}




class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'slug')
	list_display_link = ('id', 'name' )
	search_fields = ('name',)
	prepopulated_fields = {"slug": ("name",)}








admin.site.register(Comics, ComicsAdmin)
admin.site.register(Category, CategoryAdmin)


