from django.db import models

class Purchase(models.Model):
    invoice = models.CharField(max_length=100, unique=True)
    supplier = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.invoice} - {self.supplier}"
