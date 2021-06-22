from django.contrib import admin
from .models import User , submission , UserDetials ,Education ,Attachment

# Register your models here.

admin.site.register(User)
admin.site.register(submission)
admin.site.register(UserDetials)
admin.site.register(Education)
admin.site.register(Attachment)

