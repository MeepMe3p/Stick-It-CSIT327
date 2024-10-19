from django.db import models

# Create your models here.
# SAUCE: https://docs.djangoproject.com/en/5.1/topics/db/models/


class Note(models.Model):
    content = models.TextField()
    border_color = models.CharField(max_length=10)  # Assuming you store the color as a hex code
    coordinates = models.JSONField()  # Storing x and y as a JSON object
    is_finished = models.BooleanField(default=False)
    checkbox_id = models.CharField(max_length=100)
    def __str__(self):
        return self.content

