from django.db import models
from wedd.models import MatrimonialProfile
from acc.models import CustomUser

# Create your models here.
class Interest(models.Model):
    sender = models.ForeignKey(MatrimonialProfile, related_name='sent_interests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(MatrimonialProfile, related_name='received_interests', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(null=True, blank=True)  # Add this line

# Chatting

class Message(models.Model):
    sender = models.ForeignKey(MatrimonialProfile, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(MatrimonialProfile, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Shortlist

class Shortlist(models.Model):
    user = models.ForeignKey(MatrimonialProfile, related_name='shortlists', on_delete=models.CASCADE)
    profile = models.ForeignKey(MatrimonialProfile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(MatrimonialProfile, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class ConnectionRequest(models.Model):
    sender = models.ForeignKey(MatrimonialProfile, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(MatrimonialProfile, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.status}"