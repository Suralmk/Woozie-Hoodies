from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from io import BytesIO
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import weasyprint
import logging
@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    print(order_id)
    order = Order.objects.get(id=order_id)
    subject = f'Order number. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
                f'You have successfully placed an order.' \
                f'Your order ID is {order.id}.'
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[order.email]
    )
    order_html = render_to_string('orders/order_pdf.html', {"order" : order})
    out = BytesIO()
    style = [ weasyprint.CSS(settings.STATIC_ROOT / "css/pdf.css")]
    weasyprint.HTML(string=order_html).write_pdf(out, stylesheets=style)
    email.attach(f'order_{order.id}.pdf',out.getvalue(),'application/pdf')
    email.send()

# logger = logging.getLogger('weasyprint')
# logger.setLevel(logging.ERROR)

@shared_task
def download_order(order_id):
    order = get_object_or_404(Order, pk=order_id)
    pdf_buffer = BytesIO()
    order_html = render_to_string('orders/order_pdf.html', {"order" : order})
    style = [ weasyprint.CSS(settings.STATIC_ROOT / "css/pdf.css")]
    weasyprint.HTML(string=order_html).write_pdf(pdf_buffer, stylesheets=style)
    return  pdf_buffer.getvalue()
