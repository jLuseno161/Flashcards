from django.db import models

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
    description =models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='0')
    date= models.DateField()