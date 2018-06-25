from django.db import models
from django.utils import timezone
# Create your models here.
class Institute(models.Model):
#	STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'),)
 
	name = models.CharField(max_length=250)
 
	phonenum = models.SlugField(max_length=20)
	
	phonenum2 = models.SlugField(max_length=20)
 
#	author = models.ForeignKey(User,on_delete=models.CASCADE)
 
	address = models.TextField(default = "address")
 
#	publish = models.DateTimeField(default=timezone.now)
	
#	created = models.DateTimeField(auto_now_add=True)
	
#	updated = models.DateTimeField(auto_now=True)
	
	
	objects = models.Manager() # The default manager.
	
#	def get_absolute_url(self):
#		return reverse('blog:post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])	
		
	class Meta:
		ordering = ('-name',)
		
	def __str__(self):
		return self.name
		
#	def save(self, *args, **kwargs):
#		self.slug = slugify(self.title)
#		super(Post, self).save(*args, **kwargs)