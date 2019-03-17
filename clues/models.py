from django.db import models
#import user

class clue(models.Model):
    #clue id, user
    title = models.CharField(max_length=50)
    clue_text = models.TextField()
    level=models.IntegerField
    points_to = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='clue_image')
    solution = models.TextField()
