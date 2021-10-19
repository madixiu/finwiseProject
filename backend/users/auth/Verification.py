from users.utils.util import get_number
from django.core.mail import send_mail
from django.conf import settings as django_settings

def SendVerificationNumber(email):
    number = get_number()
    sendMail("Finwise Account Activation",str(number),email)
    return number
 

def SendPasswordResetNumber (email):
    number = get_number()
    sendMail("Finwise Password Reset",str(number),email)
    return number

def sendMail(subject,message,email):
    print("MAKING SURE ITS IN")
    return send_mail(
    subject=subject,
    from_email=django_settings.EMAIL_HOST_USER,
    message=message,
    # html_message=html_message,
    recipient_list=(
        [email]
        # recipient_list or [getattr(self.user, UserModel.EMAIL_FIELD)]
    ),
    fail_silently=False,
)