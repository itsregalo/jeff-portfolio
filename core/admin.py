from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Portfolio)
admin.site.register(TechnicalSkill)
admin.site.register(ProffessionalSkill)
admin.site.register(AboutMe)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Education)