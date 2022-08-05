from django.db import models

class Project(models.Model):
    
    name = models.CharField(max_length = 25)
    summary = models.CharField(max_length = 75)
    description = models.CharField(max_length = 300)

    def __str__(self):
        return self.name
