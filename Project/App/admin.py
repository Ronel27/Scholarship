from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group

# Register your models here.

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'is_deleted', 'image' )  # Display the is_deleted status
    list_filter = ('is_deleted', 'due_date')  # Add a filter for is_deleted
    actions = ['delete_image']
    # actions = ['restore_announcements', 'soft_delete_announcements', 'hard_delete_announcements']
    def delete_image(self, request, queryset):
        """Custom admin action to delete images from selected announcements."""
        for announcement in queryset:
            if announcement.image:
                announcement.delete_image()  # Call the delete_image method from the model
        self.message_user(request, "Selected images have been deleted.")
    delete_image.short_description = "Delete images from selected announcements"


admin.site.register(Announcement, AnnouncementAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display = ("completename", "position", "description", "profile",)

admin.site.register(Staff,StaffAdmin,)

# class UploadedFileAdmin(admin.ModelAdmin):
#     list = ("file")

# admin.site.register(UploadedFile,UploadedFileAdmin)

class ScholarAdmin(admin.ModelAdmin):
    list_display = ("scholarname", "description", "logo", "file","category",)

admin.site.register(Scholar,ScholarAdmin,)

admin.site.unregister(User)
admin.site.unregister(Group)