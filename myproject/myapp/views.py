from django.shortcuts import render, redirect
from .forms import UploadForm
from .tasks import send_email_summary  # Import email sending task

def index(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            # Process uploaded file data here (e.g., using pandas)
            # ...
            summary_data = process_file(uploaded_file)  # Replace with your processing logic
            send_email_summary.delay(summary_data)  # Schedule email sending
            return redirect('success')  # Redirect to success page (optional)
    else:
        form = UploadForm()
    return render(request, 'myapp/index.html', {'form': form})

def success(request):
    # Optional success page view
    return render(request, 'myapp/success.html')

