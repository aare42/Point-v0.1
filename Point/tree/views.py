from django.shortcuts import get_object_or_404, render, redirect
from .graph import generate_graph
from .datahandling import courses_by_leaf, get_parent_leaves, get_children_leaves, get_student_leaf_status
from django.contrib.auth.models import User
# Create your views here.

from django.http import HttpResponse
from .models import Leaf
from django.template import loader


def index(request):
    latest_leaves_list = Leaf.objects.order_by('name')
    template = loader.get_template('tree/index.html')
    context = {
        'latest_leaves_list': latest_leaves_list,
    }
    return render(request, 'tree/index.html', context)


def leaf_detail(request, leaf_id):
    if request.user.is_authenticated:
        leaf = get_object_or_404(Leaf, pk=leaf_id)
        courses = courses_by_leaf(leaf)
        parent_leaves = get_parent_leaves(leaf)
        children_leaves = get_children_leaves(leaf)
        status = get_student_leaf_status(request.user, leaf)
        return render(request, 'tree/leaf_detail.html', {'leaf': leaf, 'courses': courses, 'parent_leaves': parent_leaves, 'children_leaves': children_leaves, 'status': status})
    else:
        leaf = get_object_or_404(Leaf, pk=leaf_id)
        courses = courses_by_leaf(leaf)
        parent_leaves = get_parent_leaves(leaf)
        children_leaves = get_children_leaves(leaf)
        return render(request, 'tree/leaf_detail.html', {'leaf': leaf, 'courses': courses, 'parent_leaves': parent_leaves, 'children_leaves': children_leaves})