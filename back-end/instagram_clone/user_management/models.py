from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    username = models.CharField()
    email = models.EmailField(unique=True)
    last_login= models.CharField()
    password = models.CharField()
    salt = models.CharField()
    bio = models.CharField()
    is_active = models.BooleanField()
    created_date = models.DateTimeField()


# class Comments(models.Model):
#     id = models.AutoField(primary_key=True, auto_created=True)
#     comment_body = models.CharField(max_length=255)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_date = models.DateTimeField()



