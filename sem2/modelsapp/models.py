from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biografy = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return f'{self.last_name}, {self.first_name}'