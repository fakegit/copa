from django.contrib import admin

from mirror.models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'hash', 'savepoint', 'conflict', 'content_length', 'created_at', 'download']
