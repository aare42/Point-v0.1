from edumarket.models import Course
from .models import Leaf, Edge
from portfolio.models import StudentLeaf, Student
from django.contrib.auth.models import User


def courses_by_leaf(leaf):
    courses_list = []
    for course in Course.objects.all():
        if leaf in course.leaves.all():
            courses_list.append(course)
    return courses_list

def get_parent_leaves(leaf):
    parent_leaves = []
    for edge in Edge.objects.all():
        if edge.child_leaf == leaf:
            parent_leaves.append(edge.parent_leaf)
    return parent_leaves

def get_children_leaves(leaf):
    children_leaves = []
    for edge in Edge.objects.all():
        if edge.parent_leaf == leaf:
            children_leaves.append(edge.child_leaf)
    return children_leaves

def get_student_leaf_status(user, leaf):
    for student in Student.objects.all():
        if student.user == user:
            our_student = student
    for sleaf in StudentLeaf.objects.all():
        if sleaf.student == our_student and sleaf.leaf == leaf:
            return sleaf.status