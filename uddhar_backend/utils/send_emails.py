import threading
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from uddhar_backend.settings import EMAIL_HOST_USER
from rescuer.models import RescuerUser
# from weasyprint import HTML
# import json
# import datetime


# from weasyprint import HTML


class EmailThread(threading.Thread):
    def __init__(
        self, subject, html_content, recipient_list, sender, images=None, pdfs=None
    ):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.sender = sender
        self.images = images
        self.pdfs = pdfs
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(self.subject, None, self.sender, self.recipient_list)

        # Attaching images
        if self.images is not None:
            for image in self.images:
                if isinstance(image, tuple):
                    attachment_name, attachment_content, attachment_mime_type = image
                    msg.attach(
                        attachment_name, attachment_content, attachment_mime_type
                    )

        # Attaching PDFs
        # if self.pdfs is not None:
        #     for pdf in self.pdfs:
        #         pdf_data = HTML(string=pdf["content"]).write_pdf()
        #         msg.attach(pdf["name"], pdf_data, "application/pdf")

        msg.content_subtype = "html"
        msg.body = self.html_content
        msg.send()


def send_html_mail(
    subject, html_content, recipient_list, sender, images=None, pdfs=None
):
    EmailThread(subject, html_content, recipient_list, sender, images, pdfs).start()


def notify(affected):
    variables = {"affected": affected}

    # Generating Ticket
    html_content = render_to_string(
        "notifications/notify.html",
        variables,
    )

    rescue_users_instance = RescuerUser.objects.all()
    email_list = set()

    for rescue_user in rescue_users_instance:
        email_list.add(rescue_user.user.email)

    # admin emails
    email_list.add("sktanim5800@gmail.com")
    email_list.add("nmuatasin2005@gmail.com")
    email_list.add("bayajidalam2001@gmail.com")
    email_list.add("twashinilahi231@gmail.com")
    email_list.add("tofaal91522@gmail.com")

    send_html_mail(
        subject="Uddhar Notification",
        html_content=html_content,
        recipient_list=list(email_list),
        sender=EMAIL_HOST_USER,
    )

    print("Email sent", list(email_list))
