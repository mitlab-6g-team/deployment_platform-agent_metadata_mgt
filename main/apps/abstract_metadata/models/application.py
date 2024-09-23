from django.db import models
from uuid import uuid4
import hashlib

def create_token():
    # 生成一個唯一的亂數字串
    random_string = str(uuid4())

    # 使用SHA-256進行哈希處理
    hash_object = hashlib.sha256(random_string.encode())
    hashed_str = hash_object.hexdigest()

    return hashed_str

class Application(models.Model):
    uid=models.UUIDField(primary_key=True, blank=False)
    created_time=models.DateTimeField(blank=False)
    name=models.CharField(max_length=255, blank=False)
    description=models.TextField(blank=True)
    status=models.CharField(max_length=255, default='disabled', blank=False)
    token=models.CharField(max_length=255, blank=True, default=create_token)

    class Meta:
        db_table="application"

