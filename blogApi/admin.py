from django.contrib import admin
from .models import BlogPost
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class BlogPostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'category', 'date_created')
    list_display_links = ('id', 'title', )
    search_fields = ('title',)
    exclude = ('slug', )
    list_per_page = 25
    summernote_fields = ('content',)
    

admin.site.register(BlogPost, BlogPostAdmin)
