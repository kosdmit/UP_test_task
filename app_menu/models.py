from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')

    def save(self, *args, **kwargs):
        if self.parent:
            self.url = self.parent.url + '/' + self.slug
        else:
            self.url = '/' + self.slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
