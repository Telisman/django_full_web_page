from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# AbstractUser model profile info:USER,ADMIN
class CustomKorisnici(AbstractUser):
    MAJSTOR = '1'
    KORISNIK = '2'
    USER_TYPE_CHOICE = (
        (MAJSTOR, 'majstor'),
        (KORISNIK, 'korisnik')
    )
    user_type = models.CharField(max_length=100,blank=True,choices=USER_TYPE_CHOICE)
    username = models.CharField(max_length=100,unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    profile_image = models.ImageField(null=True,blank=True, upload_to="images/", default='profile_image.png')
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(max_length=100,unique=True)
    bio = models.TextField(default=" ")


    def __str__(self):
        return self.username + ' | ' +self.last_name + ' | ' + self.first_name + ' | ' + str(self.phone_number) + ' | ' + self.user_type + ' | ' + self.email+ ' | ' + str(self.id)


# Custom category model option:
class TaskCategory(models.Model):
    category_title = models.CharField(max_length=50)
    def __str__(self):
        return self.category_title
    def get_absolute_url(self):
        return reverse('home')
# Custom POST model:POST info.
class Post(models.Model):
    postUser = models.ForeignKey(CustomKorisnici,null=True, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=250)
    # task_discription = models.CharField(max_length=250)
    task_discription = RichTextField(blank=True,null=True)
    task_category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    recommended_tools = models.CharField(max_length=250)
    budget = models.IntegerField(default=0)
    likes = models.ManyToManyField(CustomKorisnici, related_name='blog_like')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.postUser) + ' | ' +self.task_title + ' | ' + self.task_discription + ' | ' + str(self.task_category) + ' | ' + self.recommended_tools + ' | ' + str(self.budget) + ' | ' + str(self.id)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


# Custom comment model, for POST created by users:KORISNICI. Only users:MAJSTORI can comment on POST
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.TextField(blank=True,null=True)
    Mid = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return str(self.post) + str(self.body) + self.name + str(self.user)
        

# class CommentUserMajstor(models.Model):
#     user = models.ForeignKey(CustomKorisnici,related_name="commentsUser",on_delete=models.CASCADE)
#     body = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return str(self.user) + str(self.body)
