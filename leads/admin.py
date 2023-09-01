from django.contrib import admin
from .models import User, Lead, Agent

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Lead)