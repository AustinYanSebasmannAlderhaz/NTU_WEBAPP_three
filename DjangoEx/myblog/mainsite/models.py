from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title


class Character(models.Model):
    class Gender(models.TextChoices):
        MALE = 'male', '男生'
        FEMALE = 'female', '女生'

    name = models.CharField(max_length=120)
    gender = models.CharField(max_length=6, choices=Gender.choices)
    affiliation = models.CharField(max_length=120, blank=True)
    homeland = models.CharField(max_length=120, blank=True)
    occupation = models.CharField(max_length=120, blank=True)
    element = models.CharField(max_length=80, blank=True)
    first_appearance = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class CharacterImage(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='characters/')

    class Meta:
        ordering = ('id',)

    def clean(self):
        super().clean()
        if not self.character_id:
            return

        existing_images = CharacterImage.objects.filter(character_id=self.character_id)
        if self.pk:
            existing_images = existing_images.exclude(pk=self.pk)

        if existing_images.count() >= 3:
            raise ValidationError('A character can have at most 3 images.')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.character.name} image #{self.pk or "new"}'
