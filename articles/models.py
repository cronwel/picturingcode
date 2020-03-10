from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
  title = models.CharField(max_length=100)
  slug  = models.SlugField()
  body  = models.TextField()
  date  = models.DateField(auto_now_add=True)
  thumbnail = models.ImageField(default = 'default.png', blank=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


  def __str__(self):
    return self.title

  def snippet(self):
    return self.body[:50] + "..."

# snippet is something you creted from the body
# it is a function that can be accessed
# therefore you can call it form the html template
# it's the body but edited for the purpose of the view
