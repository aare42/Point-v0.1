from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from tree.models import Leaf

# Create your models here.
class StudentLeafStatus(models.Model):
    id = models.IntegerField(primary_key=TRUE)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    def create_student_leaves(self):
        leafs = Leaf.objects.all()
        for leaf in leafs:
            student_leaf = StudentLeaf(student=self, leaf=leaf, status_id=1)
            student_leaf.save()

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            self.create_student_leaves()
        else:
            super().save(*args, **kwargs)

class StudentLeaf(models.Model):
    leaf = models.ForeignKey(Leaf, on_delete=models.CASCADE)
    status = models.ForeignKey(StudentLeafStatus, on_delete=models.CASCADE, default=1)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student) + " : " + str(self.leaf)