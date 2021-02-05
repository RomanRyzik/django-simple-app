from django.db import models

class Table_1(models.Model):
    table_1_id = models.IntegerField(primary_key=True)
    field_1 = models.TextField(max_length=999)
    table_2 = models.ForeignKey(
        'Table_2',
        related_name='table_2',
        on_delete=models.CASCADE
    )

class Table_2(models.Model):
    table_2_id = models.IntegerField(primary_key=True)
    field_2 = models.TextField(max_length=999)