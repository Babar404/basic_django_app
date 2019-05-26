from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField(max_length = 150)

    def __str__(self):
        return self.text[:50]    #Much better! It’s a best practice to add str() methods to all of your models to improve their readability.




