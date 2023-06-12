# # Create your models here.
# from django.db import models
# class Upload(models.Model):
#     upload_file = models.FileField()    
#     upload_date = models.DateTimeField(auto_now_add =True)

from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    feature_image = models.FileField(upload_to='tutorial/images/')
    attachment = models.FileField(upload_to='tutorial/attachments/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.feature_image.delete()
        self.attachment.delete()
        super().delete(*args, **kwargs)


    # class Meta:
    #     db_table = 'Tutorials'
    #     managed = False
