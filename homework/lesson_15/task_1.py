"""Task 1

Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a
valid email string.

Email validations:

https://help.xmatters.com/ondemand/trial/valid_email_format.htm

https://en.wikipedia.org/wiki/Email_address """

class E_mail:
    def __init__(self, email_adr):
        self.email_adr = email_adr
        self.validate(email_adr)


    @classmethod
    def validate(cls, email_adr):
        if "@" and "." in email_adr:
            return True
        return False

if __name__ == '__main__':
    dante = E_mail("master.neo16@gmail.com")
    print(dante.validate("hren"))
    print(E_mail.validate("hren"))




