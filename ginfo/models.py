from django.db import models
# from urllib import request
# import os

# Create your models here.
class Scholar(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    name = models.CharField("scholar's name",max_length=100)
    designation = models.CharField("designation", max_length=400, blank=True)
    department = models.CharField("department", max_length=400, blank=True)
    labels = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    # profile_img = models.ImageField(null=True, blank=True, upload_to ='images/%Y/%m/%D/')

    # def get_remote_image(self):
    #     if self.image_url and not self.image_file:
    #         result = request.urlretrieve(self.image_url)
    #         self.image_file.save(
    #             os.path.basename(self.image_url),
    #             File(open(result[0], 'rb'))
    #             )
    #         self.save()
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Google Scholars'
    
    def __str__(self):
        return str(self.name)


class Citation(models.Model):
    scholar = models.ManyToManyField('Scholar', through='Authored' ,related_name="scholars")
    citation_title = models.TextField()
    citation_coauthor = models.TextField()
    citation_year = models.PositiveIntegerField()

    class Meta:
        ordering = ['-citation_year']

    def __str__(self):
        return f"{self.citation_year}: {self.citation_title}"


class Authored(models.Model):
    scholar = models.ForeignKey('Scholar', related_name='authored', on_delete=models.CASCADE)
    citation = models.ForeignKey('Citation', related_name='authored', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Scholar {self.scholar}  Citation {self.citation}"
    
    class Meta:
        verbose_name_plural = 'Authored'