from django.contrib import admin
from .models import Leaf, LeafType, Keypoint, Edge

admin.site.register(LeafType)
admin.site.register(Keypoint)
admin.site.register(Edge)
admin.site.register(Leaf)