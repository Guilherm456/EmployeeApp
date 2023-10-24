from django.db import models
from django.utils import timezone
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)

    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        if not self.id:
            self.created_at = timezone.now()
        super(Employee, self).save(*args, **kwargs)