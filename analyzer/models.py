from django.db import models

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField(blank=True, null=True)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Resume({self.id})"
    