from django.db import models
from django.contrib.auth.models import User

# === OPPGAVER ===
class Task(models.Model):
    TASK_TYPE_CHOICES = [
        ('SMALL', 'Liten oppgave'),
        ('LARGE', 'Stor oppgave'),
        ('ADL', 'ADL-oppgave'),
    ]

    title = models.CharField(max_length=255)
    task_type = models.CharField(max_length=10, choices=TASK_TYPE_CHOICES)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.task_type})"


# === ROTEKASSE ===
class BrainDumpItem(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]


# === LISTER ===
class TaskList(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ListItem(models.Model):
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# === BRUKERINNSTILLINGER ===
class UserSettings(models.Model):
    THEME_CHOICES = [
        ('beige', 'Beige'),
        ('gronn', 'Grønn'),
        ('blaa', 'Blå'),
        ('rosa', 'Rosa'),
        ('mork', 'Mørk modus'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=20, choices=THEME_CHOICES, default='beige')
    icon_color = models.CharField(max_length=7, default='#1f1f1f')  # HEX-fargekode

    def __str__(self):
        return f"Innstillinger for {self.user.username}"


# === ABONNEMENT / BETALING ===
class Subscription(models.Model):
    PLAN_CHOICES = [
        ('free', 'Gratis'),
        ('pro', 'Pro'),
        ('premium', 'Premium'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default='free')
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    vipps_order_id = models.CharField(max_length=255, blank=True, null=True)
    valid_until = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Abonnement for {self.user.username} ({self.plan})"