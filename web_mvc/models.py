from django.db import models

# Create your models here.
from django.utils import timezone

REPUTATION_SYSTEM = (
    (0, "Not Evaluated Yet"),
    (1, "One Star"),
    (2, "Two Star"),
    (3, "Three Star"),
    (4, "Four Star"),
    (5, "Five Star"),
)


class Author(models.Model):
    """ Author of Post as well as Contributor """
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True, null=False, blank=False)
    eth_address = models.CharField(max_length=256, unique=True, blank=False, null=False)
    joined_date = models.DateTimeField(default=timezone.now, auto_created=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """ Blog post contain details of Crowd Funding Project """
    title = models.CharField(max_length=500)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, auto_created=True)
    last_edited_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    # link this post to its author, protect it in case the author is deleted from system
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    front_image = models.ImageField(upload_to='storage/', null=True, blank=True)
    contributions = models.DecimalField(default=0.0, max_digits=30, decimal_places=27)
    contributors = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Delete image file also
        storage, path = self.front_image.storage, self.front_image.path
        super(Post, self).delete(*args, **kwargs)
        storage.delete(path)


class Contribution(models.Model):
    """ Contribution/Donation model """
    value = models.DecimalField(max_digits=30, decimal_places=27)
    contribute_date = models.DateTimeField(default=timezone.now, auto_created=True)
    # Link to the post and its contributor
    # Also delete this contribution if the underlining post is gone
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # Also delete this contribution if the underlining author is gone
    contributor = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "{} $Value$ to: '{}'".format(self.value, self.post.title)


class Reputation(models.Model):
    """ For user to evaluate POSTs/Authors creditability  """
    reputee_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    reputee_author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    valuate = models.CharField(max_length=1, choices=REPUTATION_SYSTEM, default=0)

    def __str__(self):
        return "{} on: {}".format(self.valuate, (
            self.reputee_post.title if self.reputee_post is not None else self.reputee_author.name))
