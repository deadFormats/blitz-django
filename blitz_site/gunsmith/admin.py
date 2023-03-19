from django.contrib import admin
from .models import Platform, WeaponReceiver, WeaponSetup

# Register your models here.


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
    
    
@admin.register(WeaponReceiver)
class WeaponReceiverAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'platform', 'modified']
    list_filter = ['category', 'modified', 'platform']
    search_fields = ['name', 'category', 'platform']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['platform']
    date_hierarchy = 'modified'
    ordering = ['category', 'name']


@admin.register(WeaponSetup)
class WeaponSetupAdmin(admin.ModelAdmin):
    list_display = ['receiver', 'title', 'slug', 'author', 'share_setting', 'mode', 'created']
    list_filter = ['receiver', 'updated', 'author', 'share_setting', 'mode', 'created']
    search_fields = ['title', 'description', 'receiver', 'author']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author', 'receiver']
    date_hierarchy = 'updated'
    ordering = ['receiver', 'mode', 'created']
