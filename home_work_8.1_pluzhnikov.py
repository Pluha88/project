import re
def email_parse(email_address):
    re_email = re.compile(r"(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)", re.IGNORECASE)
    if not re_email.match(email_address):
        raise ValueError(f"wrong email: {email_address}")
    print(re_email.match(email_address).groupdict())
for i in ('someone@geekbrains.ru','som@eone@geekbra@insru',
          's@omeone@geek@brainsru','brulatiffene@mail.ru','crofrauzotreweu@mail.ru'):
    try:
        email_parse(i)
    except ValueError as err:
        print(err)