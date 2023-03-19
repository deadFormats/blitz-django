from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Platform(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name
        
    
    
class WeaponReceiver(models.Model):
    class WeaponSlot(models.TextChoices):
        PRIMARY = "PRI", "Primary"
        SECONDARY = "SEC", "Secondary"
        
    class Category(models.TextChoices):
        ASSAULT_RIFLE = "AR", 'Assault Rifle'
        BATTLE_RIFLE = "BR", "Battle Rifle"
        SMG = "SMG", "Submachine Gun"
        LMG = "LMG", "Light Machine Gun"
        SHOTGUN = "SHT", "Shotgun"
        MARKSMAN_RIFLE = "MRK", "Marksman Rifle"
        SNIPER_RIFLE = "SNI", "Sniper Rifle"
        MELEE = "MEL", "Melee"
        HANDGUN = "HND", "Handgun"
        LAUNCHER = "LAU", "Launcher"
        
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.CharField(
        max_length=3,
        choices=Category.choices,
        default=Category.ASSAULT_RIFLE
    )
    platform = models.ForeignKey(
        Platform,
        related_name="receivers",
        on_delete=models.CASCADE
    )
    
    class Meta:
        ordering = ['category', 'name']
        indexes = [
            models.Index(fields=['category', 'platform']),
        ]

    def __str__(self):
        return self.name
    


class WeaponSetup(models.Model):
    class ShareSetting(models.TextChoices):
        PRIVATE = "PRI", 'Private'
        PUBLIC = "PUB", 'Public'
    
    class Mode(models.TextChoices):
        QUICKPLAY = "QP", "Quickplay"
        RANKED = 'RA', "Ranked"
        WARZONE = "WZ", "Warzone"

    receiver = models.ForeignKey(
        WeaponReceiver,
        related_name="setups",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        User,
        related_name="setups_created",
        on_delete=models.CASCADE
    )
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    share_setting = models.CharField(
        max_length=3,
        choices=ShareSetting.choices,
        default=ShareSetting.PUBLIC
    )
    mode = models.CharField(
        max_length=2, 
        choices=Mode.choices,
        default=Mode.QUICKPLAY
    )
    #  TODO add imagefield here 
    
    class Meta:
        ordering = ['-created', 'receiver']
        indexes = [
            models.Index(fields=['-created', 'author']),
            models.Index(fields=['author', 'receiver']),
        ]
    def __str__(self):
        return f'<{self.receiver.name} setup by {self.author.username}>'
        
        
