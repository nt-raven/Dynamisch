from django.db import models

# Create your models here.

class new_model(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name= models.CharField(max_length = 100)
    email_id = models.CharField(max_length = 100)
    emp_password = models.CharField(max_length = 100)


    def __str__(self) -> str:
        return self.first_name