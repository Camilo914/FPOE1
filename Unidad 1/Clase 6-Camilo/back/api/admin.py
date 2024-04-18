from django.contrib import admin
from .models.celular import Celular
from .models.post import Post
admin.site.register(Celular)
admin.site.register(Post)
