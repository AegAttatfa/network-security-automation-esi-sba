from django.db import models

# Create your models here.


class Rule(models.Model):

    PROTOCOL=(
    ('TCP', 'TCP'),
    ('UDP', 'UDP'),
    ('ICMP', 'ICMP')
    )

    number = models.IntegerField(null=False)
    sourceIP = models.CharField(max_length=50)
    destinationIP = models.CharField(max_length=50)
    protocol = models.CharField(max_length=6, choices=PROTOCOL)

    def __str__(self):
        return str(self.number)
