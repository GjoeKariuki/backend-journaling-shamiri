from django.db import models

from django.conf import settings



User = settings.AUTH_USER_MODEL
class JournalEntry(models.Model):
    title = models.CharField(max_length=255, blank=False,Null=False)
    content = models.TextField(null=True)
    category = models.CharField(max_length=100)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date"]
    

    def __str__(self):
        return self.title