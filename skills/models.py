from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SwapRequest(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected"),
    ]

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_requests",
    )

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_requests",
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending",
    )

    def __str__(self):
        return (
            f"{self.sender.username} → "
            f"{self.receiver.username} "
            f"({self.skill.name})"
        )
