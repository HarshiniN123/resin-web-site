from django.db import models

#Create your models here.

class Orders(models.Model):
    name=models.CharField(max_length=200)
    phonenumber=models.BigIntegerField()
    address=models.CharField(max_length=200)
    email=models.EmailField(null=True, blank=True)
    Resin = {
        "A":"Four Inch Agate Frame",
        "B":"Four Inch Round Frame",
        "C":"Four Inch Heart Frame",
        "D":"Six Inch Agate Frame",
        "E":"Six Inch Round Frame",
        "F":"Twelve Inch Agate Frame",
        "G":"12x9 Inch Agate Frame",
        "H":"8 Inch Agate Frame",
        "V":"None"
    }
    resin = models.CharField(max_length=100, choices=Resin)
    Wooden = {
        "I":"Eight Inch Frames",
        "J":"Ten Inch Frames",
        "K":"Twelve Inch Frames",
        "L":"None"
    }
    wooden = models.CharField(max_length=100, choices=Wooden)
    Keychain ={
        "M":"Photo Placed Agate Keychain",
        "N":"Photo Placed Round Keychain",
        "O":"Photo Placed Heart Keychain",
        "P":"Photo Placed Rectangle Keychain",
        "U":"Photo Placed Square Keychain",
        "Q":"Baby Feet Keychain",
        "R":"Alphabet Keychain",
        "S":"Spotify Keychain",
        "T":"None"
    }
    keychain = models.CharField(max_length=100, choices=Keychain)

    productdesc =models.CharField(max_length=300)
    color =models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name} =>{self.phonenumber} =>{self.address} =>{self.email} =>{self.resin}=>{self.wooden} =>{self.keychain} =>{self.productdesc} => {self.color}"

class Meta:
    db_table ="Orders"


    
