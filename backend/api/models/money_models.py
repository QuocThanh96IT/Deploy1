from django.db import models

class Money(models.Model):
  type = models.CharField(max_length=5)
  title = models.CharField(max_length=200, blank= False)
  amount = models.FloatField(null=False)
  date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return "{} - {}".format(self.type, self.title, self.amount, self.date)