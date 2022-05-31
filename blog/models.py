from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=20, null=False)
    info = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"


class ArticleModel(models.Model):
    title = models.CharField(max_length=100, null=False)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000, null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "article"