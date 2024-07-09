from django.db import models

from django.conf import settings
import uuid



User = settings.AUTH_USER_MODEL
class JournalEntry(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255, blank=False,null=False)
    content = models.TextField(null=True)
    category = models.CharField(max_length=100)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date"]
    

    def __str__(self):
        return self.title