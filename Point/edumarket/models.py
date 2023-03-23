from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from tree.models import Leaf
from portfolio.models import StudentLeaf
# Create your models here.

class Educator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 127)

    def __str__(self):
        return self.name + " (" + self.user.username +")"

class Course(models.Model):
    name = models.CharField(max_length=63)
    author = models.ForeignKey(Educator, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=1000, null=True, blank=True)
    leaves = models.ManyToManyField(Leaf)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_educator(self):
        return self.author

class ContractStatus(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Contract(models.Model):
    from portfolio.models import Student
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def get_current_status(self):
        latest_status_change = self.contractstatuschange_set.order_by('-date').first()
        if latest_status_change:
            return latest_status_change.new_status
        else:
            return None

    def __str__(self):
        return str(self.student) + " - " + str(self.course.get_educator()) + " : " + str(self.course)

class ContractStatusChange(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    new_status = models.ForeignKey(ContractStatus, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    initiator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.contract.save()
