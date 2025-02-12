from django.shortcuts import render, redirect
from .forms import PersonForm

def person_form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with the actual view name or URL
    else:
        form = PersonForm()
    return render(request, 'person_form.html', {'form': form})
def success(request):
    return render(request, 'success.html')