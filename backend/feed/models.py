from django.db import models
import uuid
import os



def get_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('image', filename)



class Post(models.Model):
	title = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to=get_image_filename)
	content = models.TextField()

	class Meta:
		ordering = ['-created_at']


	def __str__(self):
		return f'Title : {self.title}'
