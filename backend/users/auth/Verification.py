from users.utils.util import get_number
from django.core.mail import send_mail
from django.conf import settings as django_settings

def SendVerificationNumber(email):
# print(get_number())
    # send_mail()
    number = get_number()
    sendMail("Finwise Activation",str(number),email)
    return number
    # return send_mail(
    # subject="testDjango",
    # from_email=django_settings.GRAPHQL_AUTH['EMAIL_FROM'],
    # message="hey fucker",
    # # html_message=html_message,
    # recipient_list=(
    #     ["mahdi.moradi72@gmail.com"]
    #     # recipient_list or [getattr(self.user, UserModel.EMAIL_FIELD)]
    # ),
    # fail_silently=False,
# )

# def 
def sendMail(subject,message,email):

    return send_mail(
    subject=subject,
    from_email=django_settings.GRAPHQL_AUTH['EMAIL_FROM'],
    message=message,
    # html_message=html_message,
    recipient_list=(
        [email]
        # recipient_list or [getattr(self.user, UserModel.EMAIL_FIELD)]
    ),
    fail_silently=False,
)