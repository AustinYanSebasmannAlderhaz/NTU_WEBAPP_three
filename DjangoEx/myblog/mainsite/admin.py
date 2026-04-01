from django.contrib import admin
from .models import Character, CharacterImage, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')


class CharacterImageInline(admin.TabularInline):
    model = CharacterImage
    extra = 1
    max_num = 3


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'gender',
        'affiliation',
        'homeland',
        'occupation',
        'element',
        'first_appearance',
    )
    search_fields = ('name', 'affiliation', 'homeland', 'occupation', 'element')
    inlines = [CharacterImageInline]


class CharacterImageAdmin(admin.ModelAdmin):
    list_display = ('character', 'id')


admin.site.register(Post, PostAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterImage, CharacterImageAdmin)
