from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    


class Flashcard(models.Model):

    
    name =models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description =models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='0')
    date= models.DateField()

    def __str__(self):
        return self.name


    def save_flashcard(self):
        self.save()

    def delete_flashcard(self):
        self.delete()    

