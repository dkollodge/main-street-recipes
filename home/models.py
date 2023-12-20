from django.db import models


# Create your models here.
class Recipe(models.Model):
    ID = models.IntegerField()
    Name = models.CharField()
    Image = models.ImageField()
    #Ingredients =
    #Instructions =
    DateCreated = models.DateTimeField(auto_now_add=True)
    Active = models.BooleanField(default=True)


# trying to figure out a way to handle ingredients per recipe.
# The easiest way logically would be to have a list of tuples (ingredientName, quantity), but the models
# doesn't seem to support it
# how can I structure the data within the models framework to reflect a 1 to many relationship?

# potential option - have a table of ingredient records containing a name, quantity, and recipe link.
# This will be subject to duplicates
