from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'Contact from {self.name}'


class Project(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    filePath = models.ImageField(upload_to='images/', null=False, blank=False)  # 'images/' is the folder where the images will be saved
    description = models.CharField(max_length=255, null=False, blank=False)
    websiteURL = models.URLField(max_length=200, null=False, blank=False)

    def __str__(self):
        return f"{self.title}"