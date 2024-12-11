from django import forms
from .models import Contact, Project

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'filePath', 'description']
