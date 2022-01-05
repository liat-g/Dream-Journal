from django.contrib import admin
from .models import Journal, Comment, User
# Register your models here.


class JournalAdmin(admin.ModelAdmin):
    list = ('id', 'title', 'created_at',
            'content', 'is_draft', 'journal_rating')


class CommentAdmin(admin.ModelAdmin):
    list = ('id', 'created_at',
            'is_approved')


class UserAdmin(admin.ModelAdmin):
    list = ('id', 'password', 'username', 'is_dreamer')


admin.site.register(Journal, JournalAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User, UserAdmin)
