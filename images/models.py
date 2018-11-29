from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE) #cascade is set so when user is deleted it deletes all their images
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True) #helps create SEO friendly URLS
    url = models.URLField() #the original URL for this image
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,
                               db_index=True)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name = 'images_liked', #names relationship from related object back to this one.
                                        blank=True)
    
    def __str__(self):
        return self.title

    #overriding the default save() method
    # more here:
    # https://docs.djangoproject.com/en/2.1/topics/db/models/#overriding-predefined-model-methods
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
