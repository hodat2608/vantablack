from django.db import models

from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    full_name = models.CharField(max_length=20, null=True, blank= True )
    avatar = models.ImageField(upload_to='images/', null=True,blank=True)
    bio = models.TextField(null=True, blank= True)
    date_birth = models.DateField(null=True,blank= True)
    email = models.EmailField(unique=True, null=True)
    address = models.TextField(null=True, blank= True, max_length=1000000)
    phone_number = models.TextField(null=True, blank= True, max_length=1000000)
    date_join = models.DateTimeField(auto_now_add=True)
    def __str__(self):

        return self.user.username


class PostViews(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    discription =  models.TextField(max_length=1000000, blank=True,null=True)
    post_image = models.ImageField(upload_to='images/', null=True,blank=True)
    post_likes = models.ManyToManyField(User, related_name='post_likes',blank=True)
    post_shares = models.ManyToManyField(User, related_name='post_shares',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created','-updated']

    def __str__(self):
        return self.discription
    
    def get_post_user_avatar(self):
        if self.post_user and hasattr(self.post_user, 'profileuser'):
            return self.post_user.profileuser.avatar
        return None

    def formatted_created_time(self):
        return self.created.strftime("%I:%M %p")
    
class share_post(models.Model):
    user_share_post = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    share_post_id = models.ForeignKey(PostViews, on_delete=models.CASCADE, null=True)
    discription_sh = models.TextField(null=True,max_length=1000000, blank= True)
    share_post_likes = models.ManyToManyField(User, related_name='share_post_like', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user_share_post} shared {self.share_post_id}'

    def formatted_created_time(self):
        return self.created.strftime("%I:%M %p")
    
    def get_user_share_post_avatar(self):
        if self.user_share_post and hasattr(self.user_share_post, 'profileuser'):
            return self.user_share_post.profileuser.avatar
        return None
    
#repply for post??
class CommentViews(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_comment = models.ForeignKey(PostViews, on_delete=models.CASCADE,null=True,blank=True)
    share_post_comment = models.ForeignKey(share_post, on_delete=models.CASCADE,null=True,blank=True)
    message = models.TextField(max_length=1000000,blank=True,null=True)
    massage_image = models.ImageField(upload_to='images/', null=True,blank=True)
    comment_likes = models.ManyToManyField(User, related_name='comment_likes',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f'{self.comment_user} comment at post: {self.post_comment}'
    
    def get_comment_user_avatar(self):
        if self.comment_user and hasattr(self.comment_user, 'profileuser'):
            return self.comment_user.profileuser.avatar
        return None
    
#repply for comment?
class Repply_commentviews(models.Model):
    user_rep = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rep_commentviews = models.ForeignKey(CommentViews, on_delete=models.CASCADE, null=True)
    rep_message = models.TextField(max_length=1000000,null=True,blank=True)
    rep_mess_image = models.ImageField(upload_to='images/', null=True,blank=True)
    rep_comment_likes = models.ManyToManyField(User, related_name='rep_comment_likes',blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user_rep} rep comment of {self.rep_commentviews}'
    
    def get_repply_comment_user_avatar(self):
        if self.user_rep and hasattr(self.user_rep, 'profileuser'):
            return self.user_rep.profileuser.avatar
        return None
    




#history_activity
class liked_post_activity(models.Model):
    user_liked_activity = models.ForeignKey(User, on_delete=models.CASCADE)
    post_liked_activity = models.ForeignKey(PostViews, on_delete=models.CASCADE, null=True,blank=True)
    activity_emotion = models.CharField(max_length=20,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.post_liked_activity
    

class commented_post_activity(models.Model):
    user_comment_activity = models.ForeignKey(User, on_delete=models.CASCADE)
    post_comment_activity = models.ForeignKey(PostViews, on_delete=models.CASCADE,null=True,blank=True)
    comment_content = models.ForeignKey(CommentViews,on_delete=models.CASCADE,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.post_comment_activity
    

class liked_comment_activity(models.Model):
    user_liked_comment = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    comment_liked_activity = models.ForeignKey(CommentViews,on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.comment_liked_activity
    
class repply_comment_activity(models.Model):
    user_rep_comment = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    comment_rep_activity = models.ForeignKey(CommentViews,on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.comment_rep_activity
    
class save_post(models.Model):
    user_save = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post_save = models.ForeignKey(PostViews, on_delete=models.CASCADE,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.post_save)


    


