from django.db import models

class CulturalPost(models.Model):
    CATEGORY_CHOICES = [
        ('heritage', 'Heritage Site'),
        ('festival', 'Festival'),
        ('artform', 'Art Form'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.category})"
