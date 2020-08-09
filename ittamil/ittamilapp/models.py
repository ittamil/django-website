from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

STATUS = ((0, "Draft"), (1, "Publish"))

class PostModel(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    cover_image = models.ImageField(upload_to="images")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = RichTextField()
    likes = models.ManyToManyField(User, related_name="blog_post", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()


    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id, self.slug])


#class CommentModel(models.Model):
#    id = models.IntegerField(primary_key=True)
#    post = models.ForeignKey(PostModel, related_name='comments',on_delete=models.CASCADE)
#    name = models.CharField(max_length=80)
#    email = models.EmailField()
#    reply = models.ForeignKey('CommentModel', null=True, related_name="repiles" ,on_delete=models.CASCADE)
#    body = models.TextField()
#    created_on = models.DateTimeField(auto_now_add=True)
#    active = models.BooleanField(default=False)
#
#    class Meta:
#        ordering = ["created_on"]
#
#    def __str__(self):
#        return "Comment {} by {}".format(self.body, self.name)        

class UserModel(User):
    email = models.EmailField(primary_key=True,unique=True),        

class UserDashBoardModel(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("PostDetailView", kwargs={"slug": str(self.slug)})

class AuthorProfileModel(User):
    slug = models.SlugField(max_length=300, unique=True)
    About_Yourself = models.TextField(max_length=500,help_text="Yourself")
    FaceBook_Profile = models.URLField(max_length = 200,help_text="Paste Your facebook Profile Link") 
    Github_Profile = models.URLField(max_length = 200, help_text="Paste Your Github Profile Link") 
    Instagram_Profile = models.URLField(max_length = 200,help_text="Paste Your Instagram Profile Link") 
    LinkedIn_Profile = models.URLField(max_length = 200,help_text="Paste Your LinkedIn Profile Link")
    Telegram_Profile = models.URLField(max_length = 200,help_text="Paste Your Profile Profile Link") 
    UG_Degree_Name= models.CharField(max_length=300,help_text="Enter your UG Course name like 'Bachelor of Science'")
    Skill = models.TextField(max_length=500,help_text="Enter Your Skill Like One by One")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("AuthorDetailView", kwargs={"slug": str(self.slug)})



class Comment(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE , related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', null=True, related_name="replies",on_delete=models.CASCADE)
    content = models.TextField(max_length=160)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))