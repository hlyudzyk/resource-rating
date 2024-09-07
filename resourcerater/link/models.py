from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

    def get_rating(self):
        if self.reviews.count():
            total_rating = 0;
            for review in self.reviews.all():
                total_rating += review.rating
            return total_rating/self.reviews.count()
        return "No reviews"


class Review(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.link.name} - {self.rating} starts by {self.user.username}'
