from django.db import models

class History(models.Model):
    total = models.BigIntegerField()
    string = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.total)