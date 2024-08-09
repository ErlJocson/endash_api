from django.db import models

class Cards(models.Model):
    title = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logos')
    video = models.FileField(upload_to='videos')
    link = models.CharField(max_length=500)
    position = models.IntegerField()

# DynamoDB 
# {
# "ID": {
# "N": "0"
# },
# "title": {
# "S": ""
# },
# "logo" : {
# "S":""
# },
# "video" : {
# "S":""
# },
# "link" : {
# "S":""
# },
# "position" : {
# "N":"0"
# }
# }
