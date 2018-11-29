from django.contrib import admin
from .models import Cert, Skill, Exp, Edu, OnlineResource

admin.site.register(Cert)
admin.site.register(Exp)
admin.site.register(Edu)
admin.site.register(OnlineResource)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('category','description','priority')
    ordering = ('priority','description')