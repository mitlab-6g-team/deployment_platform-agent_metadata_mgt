from django.db import models

class Topic(models.Model):
    consumer_process_pid=models.IntegerField(primary_key=True, blank=False)
    name=models.CharField(max_length=255, blank=False)
    type=models.CharField(max_length=255, blank=False)

    class Meta:
        db_table="topic"
