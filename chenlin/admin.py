from django.contrib import admin

# Register your models here.
from chenlin.models import WorkInfo, WorkPic


class WorkPicInline(admin.StackedInline):
    model = WorkPic
    extra = 1


class WorkInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Information', {'fields': ['serial_num', 'remark']}),
    ]
    inlines = [WorkPicInline]


admin.site.register(WorkInfo, WorkInfoAdmin)
admin.site.register(WorkPic)
