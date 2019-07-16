from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


class Rule(models.Model):

    PROTOCOL=(
    ('TCP', 'TCP'),
    ('UDP', 'UDP'),
    ('ICMP', 'ICMP')
    )

    number = models.IntegerField(null=False, unique=True,
                                validators=[MinValueValidator(100), MaxValueValidator(199)])

    sourceIP =  models.GenericIPAddressField(protocol='IPv4')
    destinationIP =  models.GenericIPAddressField(protocol='IPv4')

    protocol = models.CharField(max_length=6, choices=PROTOCOL)


    
    def __str__(self):
        return str(self.number)