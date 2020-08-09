from django.contrib import admin
#from ittamilapp.models import PostModel, CommentModel, AuthorProfileModel
from django_summernote.admin import SummernoteModelAdmin
from ittamilapp.models import PostModel, Comment, AuthorProfileModel
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

#@admin.register(CommentModel)
#class CommentAdmin(admin.ModelAdmin):
#    list_display = ('name', 'body',  'created_on', 'active')
#    list_filter = ('active', 'created_on')
#    search_fields = ('name', 'email', 'body')
#    actions = ['approve_comments']
#
#    def approve_comments(self, request, queryset):
#        queryset.update(active=True)

admin.site.register(PostModel, PostAdmin)
admin.site.register(AuthorProfileModel)
admin.site.register(Comment)