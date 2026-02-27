from django.db import models

# Create your models here.
# reflection model
class Reflection(models.Model):
    trope_name = models.CharField(max_length=100)
    reflection_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    time_spent = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.trope_name
    
# poll model 
class Poll(models.Model):
    selected_trope = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.selected_trope