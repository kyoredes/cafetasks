from django.db import models
from django.contrib.auth import get_user_model


class Status(models.Model):
    name = models.CharField(
        max_length=20,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name
