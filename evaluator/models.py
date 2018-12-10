from django.db import models


class EvalData(models.Model):
    expression = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.expression

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %y')

