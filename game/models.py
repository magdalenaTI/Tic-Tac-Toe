from django.db import models

class Room(models.Model):
    
    def __str__(self) -> str:
        return f"{self.id}"
