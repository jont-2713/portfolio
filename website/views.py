from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact form data to the database
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect after successful submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
