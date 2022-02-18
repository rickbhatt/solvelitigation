from celery import shared_task

from django.core.mail import send_mail, EmailMessage

from django.conf import settings

from django.template.loader import render_to_string

from django.utils.dateparse import parse_datetime


@shared_task
def payment_success_mail(order_id, user_email):
    # to the customer
    template = render_to_string('regd_success_email.html', {'order_id': order_id})
    email = EmailMessage(
        'PAYMENT SUCCESSFUL',                                   #subject
        template,                                                      # body
        settings.EMAIL_HOST_USER,
        [user_email],                                       # sender email
    )
    email.fail_silently = False
    email.content_subtype = 'html'       # WITHOUT THIS THE HTML WILL GET RENDERED AS PLAIN TEXT
    email.send()

    return "executed"