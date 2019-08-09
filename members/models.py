from django.db import models

# Create your models here.
class Members(models.Model):
    first_name = models.CharField(max_length=200)
    mid_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    date_created = models.DateTimeField('date published')
    date_updated = models.DateTimeField('date updated')

    def __str__(self):
        return self.first_name +' '+ self.last_name

class Loan(models.Model):
    mem_id = models.ForeignKey(Members, on_delete=models.CASCADE)
    loan_title = models.CharField(max_length=200)
    loan_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.loan_title