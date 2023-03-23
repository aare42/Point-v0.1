from django.db import models
from django.contrib.auth.models import User

class LeafType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# Leaf - тема, листок на дереві знань. зберігає в собі інформацію про зв'язок з іншими темами
class Leaf(models.Model):
    name = models.CharField(max_length=63)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=1)
    description = models.CharField(max_length=1000, null=True, blank=True)
    type = models.ForeignKey(LeafType, on_delete=models.CASCADE, default=1)
    connections = models.ManyToManyField('self', through='Edge', symmetrical=False)

    def __str__(self):
        return str(self.name) + " (" + str(self.type) + ")"

    def create_student_leaves(self):
        from portfolio.models import Student, StudentLeaf
        students = Student.objects.all()
        for student in students:
            student_leaf = StudentLeaf(student=student, leaf=self, status_id=1)
            student_leaf.save()

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            self.create_student_leaves()
        else:
            super().save(*args, **kwargs)


class Edge(models.Model):
    parent_leaf = models.ForeignKey(Leaf, on_delete=models.CASCADE, related_name='parent_leaf')
    child_leaf = models.ForeignKey(Leaf, on_delete=models.CASCADE, related_name='child_leaf')

    def __str__(self):
        return str(self.parent_leaf) + " . . . needed for . . . " + str(self.child_leaf)


class Keypoint(models.Model):
    text = models.CharField(max_length=255)
    leaf = models.ForeignKey(Leaf, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text) + ":  (" + str(self.leaf) + ")"
