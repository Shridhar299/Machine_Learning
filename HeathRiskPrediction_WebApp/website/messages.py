from flask import Blueprint, render_template, request, redirect
from flask_mail import Message as MailMessage
from . import mail
from flask import current_app as app

messages = Blueprint('messages', __name__)

@messages.route("/msg", methods=['GET', 'POST'])
def msg():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Send email to admin
        admin_email = app.config['MAIL_USERNAME']
        subject = "New Contact Form Submission"
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        email_msg = MailMessage(
            subject=subject,
            sender=admin_email,
            recipients=[admin_email],
            body=body
        )
        mail.send(email_msg)

        return redirect("/")
    else:
        return render_template('base.html')
