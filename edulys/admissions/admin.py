from django.contrib import admin

# Register your models here.

from .models import School,Address,SchoolClass,AllImages


admin.site.register(Address)
admin.site.register(AllImages)

class SchoolClassInline(admin.TabularInline):
    extra = 1
    model = SchoolClass



class SchoolAdmin(admin.ModelAdmin):
    inlines = [
        SchoolClassInline,
    ]



admin.site.register(School,SchoolAdmin)
