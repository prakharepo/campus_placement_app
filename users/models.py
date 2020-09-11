from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id_no = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20)
    cgpa = models.CharField(max_length=20)
    degree = models.CharField(max_length=20)
    stream = models.CharField(max_length=20)
    placed_in = models.CharField(default='NoOffer', max_length=20)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
