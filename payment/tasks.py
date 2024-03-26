import weasyprint
from celery import shared_task
from io import BytesIO
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from order.models import Order

@shared_task
def payment_done(order_id):
    order = Order.objects.get(id=order_id)

    subject = f"Woozie - Payment Completed. Invoice No: {order.id}"
    message = ' Thank you! please find the attached invoice for your recent purchase.'
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[order.email]
    )
    # generating the pdf invoicepython
    order_html = render_to_string('orders/order_pdf.html', {"order" : order})
    out = BytesIO()
    style = [ weasyprint.CSS(settings.STATIC_ROOT / "css/pdf.css")]
    weasyprint.HTML(string=order_html).write_pdf(out, stylesheets=style)
    email.attach(f'order_{order.id}.pdf',out.getvalue(),'application/pdf')
    email.send()

