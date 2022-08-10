from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Menus(models.Model):
    content = models.TextField()
    restaurant = models.ForeignKey(
        Restaurant,
        unique=True,
        on_delete=models.CASCADE
    )
    categories = models.ManyToManyField(Category, related_name="menus")

    def __str__(self):
        return f"Menu of {self.restaurant}"
