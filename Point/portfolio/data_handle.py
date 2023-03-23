from tree.models import Leaf
from .models import *

def update_student_leaves(student):
    for leaf in Leaf.objects.all():
        if not StudentLeaf.objects.filter(student=student, leaf=leaf).exists():
            new_student_leaf = StudentLeaf(student=student, leaf=leaf, status = StudentLeafStatus.objects.get(id=1))
            new_student_leaf.save()