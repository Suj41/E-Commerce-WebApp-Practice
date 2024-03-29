from django.db import models

class Customer(models.Model):
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=16)

    def register(self):
        self.save()

    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
