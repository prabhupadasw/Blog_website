from django.db import models
from django.contrib.auth.models import AbstractUser, Group  # Import Group

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    class Meta:
        pass

# Set unique related_name for the conflicting fields in the custom User model
User._meta.get_field('groups').related_name = 'blog_user_groups'
User._meta.get_field('user_permissions').related_name = 'blog_user_permissions'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# Explicitly define the intermediary model for the ManyToMany relationship
class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)  # Reference Group model


