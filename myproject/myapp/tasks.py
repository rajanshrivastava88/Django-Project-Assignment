from django.core.mail import send_mail

def send_email_summary(summary_data):
    subject = 'Data Upload Summary from MyDjangoApp'
    message = '\n'.join([f'{state} {dpd} {count}' for state, dpd, count in summary_data])
    recipient_list = ['tech@themedius.ai', 'hr@themedius.ai']
    send_mail(subject, message, '', recipient_list, fail_silently=False)  # Handle errors
