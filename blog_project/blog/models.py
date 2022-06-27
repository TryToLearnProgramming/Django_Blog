from turtle import title
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Post Table
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=256)
    text = models.TextField()
    cteate_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title

# Comments Table
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def aproved(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")
    
    def __str__(self):
        return super().text