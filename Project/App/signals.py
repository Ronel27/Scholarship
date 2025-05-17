# # yourapp/signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.utils import timezone
# from App.models import Announcement

# @receiver(post_save, sender=Announcement)
# def delete_overdue_announcement(sender, instance, **kwargs):
#     """
#     Deletes a announcement if it's overdue and not completed.
#     This function is triggered every time a Announcement is saved.
#     """
#     if instance.due_date < timezone.now() and not instance.completed:
#         instance.delete()
#         print(f"Announcement '{instance.title}' was deleted as it was overdue.")
