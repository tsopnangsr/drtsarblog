from django.contrib import admin
from .models import Post

# Register your models here.
##admin.site.register(Post) # This is how to register a model on a classic way (undecorated way)
@admin.register(Post) # This is how to register The ModelAdmin class that is decorated (personalize)
class PostAdmin(admin.ModelAdmin):
    list_display =  ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    

