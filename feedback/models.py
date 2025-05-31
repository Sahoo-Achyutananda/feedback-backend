from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length = 100)
    overall_rating = models.SmallIntegerField(null=False)
    code_rating = models.SmallIntegerField(null=True)
    ui_ux_rating = models.SmallIntegerField(null = True)
    comments = models.TextField(blank = True, null=True)
    project_name = models.CharField(max_length=20, null=True)
    project_version = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.TextField(null=True)

    def __str__(self):
        return f'{self.name} - {self.overall_rating}'
    
