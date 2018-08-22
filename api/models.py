from django.db import models
import uuid

class OIDCClient(models.Model):
    #client_id = models.CharField(primary_key=True, max_length=200)
    #client_secret = models.CharField(max_length=200)
    client_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_secret = models.UUIDField(default=uuid.uuid4, editable=False)
    client_name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    redirect_url = models.URLField()

    def __str__(self):
        return self.client_id


class GearClient(models.Model):
    client_id = models.CharField(primary_key=True, max_length=200)
    client_secret = models.CharField(max_length=200)
    redirect_url = models.CharField(max_length=200)

    def __str__(self):
        return self.client_id
