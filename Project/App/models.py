import os
from traceback import format_tb
from django.db import models
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
# from django.core.exceptions import ValidationError
# from django.core.files.images import get_image_dimensions

# Create your models here.

CATEGORY_CHOICES =(
    ('Private','Private'),
    ('Government','Government')
)

class Announcement(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True,)
    description = models.TextField(null=True, blank=True,)
    due_date = models.DateField(null=True, blank=True,)
    is_deleted = models.BooleanField(default=False)  # Soft delete flag
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            if img.mode != 'RGB':
                img = img.convert('RGB')

            output = io.BytesIO()
            img = img.resize((572, 800))
            img.save(output, format='JPEG', quality=85)
            output.seek(0)

            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', len(output.getvalue()), None)

            super().save(*args, **kwargs)

    def delete_image(self):
        """Delete the image file associated with this announcement."""
        if self.image:
            if os.path.isfile(self.image.path):  # Check if the file exists
                os.remove(self.image.path)  # Delete the file
            self.image = None  # Set the image field to None
            self.save()  # Save the model to update the database
            def __str__(self):
                return f"{self.title} {self.description} {self.due_date} {self.image}"

class Staff(models.Model):
    completename = models.CharField(max_length=255)
    position  = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    profile = models.ImageField(null=True, blank=True, upload_to="images/")
    def save(self, *args, **kwargs):
        if self.profile:
            img = Image.open(self.profile)
            if img.mode != 'RGB':
                img = img.convert('RGB')

            output = io.BytesIO()
            img = img.resize((572, 549))
            img.save(output, format='JPEG', quality=85)
            output.seek(0)

            self.profile = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.profile.name.split('.')[0], 'image/jpeg', len(output.getvalue()), None)

            super().save(*args, **kwargs)
            def __str__(self):
                return f"{self.completename} {self.description} {self.position} {self.profile}"
    # def clean(self):
    #     if not self.photo:
    #         raise ValidationError("No image!")
    #     else:
    #         w, h = get_image_dimensions(self.photo)
    #         if w != 200:
    #             raise ValidationError("The image is %i pixel wide. It's supposed to be 200px" % w)
    #         if h != 200:
    #             raise ValidationError("The image is %i pixel high. It's supposed to be 200px" % h)

class Scholar(models.Model):
    scholarname = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=255, default='select')  
    file = models.FileField(upload_to='File/')
    logo = models.ImageField(null=True, blank=True, upload_to="images/")

    def save(self, *args, **kwargs):
        if self.logo:
            img = Image.open(self.logo)
            if img.mode != 'RGB':
                img = img.convert('RGB')

            output = io.BytesIO()
            img = img.resize((800, 533))
            img.save(output, format='JPEG', quality=85)
            output.seek(0)

            self.logo = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.logo.name.split('.')[0], 'image/jpeg', len(output.getvalue()), None)

            super().save(*args, **kwargs)
            def __str__(self):
                return f"{self.scholarname} {self.description} {self.category} {self.file} {self.logo}"

    