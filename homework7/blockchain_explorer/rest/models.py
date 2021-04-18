from django.db import models

# Create your models here.
class Tx(models.Model):
    id = models.BigIntegerField(primary_key=True)
    txid = models.CharField(max_length=128)
    from_addr = models.CharField(max_length=66)
    to_addr = models.CharField(max_length=66)
    value = models.CharField(max_length=128)
    timestamp = models.BigIntegerField()
    block_number = models.BigIntegerField()



class Block(models.Model):
    number = models.IntegerField(primary_key=True, auto_created=False)
    txs = models.ManyToManyField(Tx)
    timestamp = models.BigIntegerField()
