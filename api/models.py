from django.db import models
from django.utils import timezone
class Department(models.Model):
    # Name of the department
    name = models.CharField(max_length=50)
    # Description of the department (optional)
    description = models.CharField(max_length=100, blank=True)
    
class Employee(models.Model):
    # Name of the employee
    name = models.CharField(max_length=50)
    # Email of the employee
    email = models.EmailField(max_length=254)
    # Department of the employee
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # Date of creation of the employee
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Lowercase the email
        self.email = self.email.lower()
        # Set the created_at date if the object is new
        if not self.id:
            self.created_at = timezone.now()
        super(Employee, self).save(*args, **kwargs)