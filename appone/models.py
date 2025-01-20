from django.db import models
class Song(models.Model):
    name = models.CharField(max_length=255, default='No Name')
    duration = models.IntegerField(default = 0, help_text="Duration in seconds")
    lyrics = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}{self.duration}'


class Device(models.Model):
    OS_ANDROID = 'android'
    OS_IOS = 'ios'

    OS_CHOICES = (
        (OS_ANDROID, 'Android'),
        (OS_IOS, 'iOs'),
    )
    FORM_FACTOR_PHONE = 'phone'
    FORM_FACTOR_TABLET = 'tablet'

    FORM_FACTOR_CHOICES = (
        (FORM_FACTOR_PHONE, 'Phone'),
        (FORM_FACTOR_TABLET, 'Tablet'),
    )

    os = models.CharField(max_length=20, choices=OS_CHOICES, default=OS_ANDROID)

    form_factor = models.CharField(max_length=20, choices=FORM_FACTOR_CHOICES, default=FORM_FACTOR_PHONE)

    model = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    enabled = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.pk}{self.get_os_display()}{self.get_form_factor_display()}{self.model}{self.created_at}{self.enabled}{self.description}"

    def get_os_display(self):
        return self.os

    def get_form_factor_display(self):
        return self.form_factor