from django.db import models

# Create your models here.


# class ToDoList(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name


# class Item(models.Model):
#     todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
#     text = models.CharField(max_length=300)
#     complete = models.BooleanField()


# def __str__(self):
#     return self.text


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.TextField()

    def __str__(self):
        return self.name + " - "+self.email
