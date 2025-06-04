from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVarities(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('LN','LEMON'),
        ('OL','OOLONG'),    
        ('EL','ELAICHI'),
    ]
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default="")
    price = models.IntegerField()


    def __str__(self):
        return self.name

