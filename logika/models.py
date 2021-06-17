from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        if not self.parent:
            return f"{self.name}"
        else:
            return f"{self.parent} --> {self.name}"

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Article(models.Model):
    # John.posts.all()
    # Raychel.posts.all()
    # Peter.post_set.all()
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True)
    preview = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f"{self.owner}-->{self.title}"


class ArticleImages(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    @staticmethod
    def generate_name():
        import random
        return "image" + str(random.randint(111111, 999999))

    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(ArticleImages, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} -> {self.post.id}"


class Comment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner}->{self.post}->{self.created_at}-{self.body[0:10]}"