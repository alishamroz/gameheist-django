from django.db import models

# Create your models here.
class Games(models.Model):
    gameDate= models.DateField()
    gameSlot=models.CharField(max_length=20)
    teamname= models.CharField(max_length=120)
    player1= models.CharField(max_length=120)
    player2= models.CharField(max_length=120)
    player3= models.CharField(max_length=120)
    player4= models.CharField(max_length=120)
    phoneno=models.BigIntegerField()
    date=models.DateField()

    def __str__(self):
        return self.teamname

class Contact(models.Model):
    fname= models.CharField(max_length=120)
    lname= models.CharField(max_length=120)
    email=models.EmailField()
    comment=models.TextField(max_length=256)
    def __str__(self):
        return self.fname+" "+self.lname