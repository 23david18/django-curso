from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']   # filtros laterales
    search_fields = ['title', 'body']                          # barra de búsqueda
    prepopulated_fields = {'slug': ('title',)}                 # autocompleta slug
    raw_id_fields = ['author']                                 # selector de autor optimizado
    date_hierarchy = 'publish'                                 # navegación por fechas
    ordering = ['status', 'publish']                           # orden inicial


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'update']   
    search_fields = ['name', 'email', 'body']                          
   
