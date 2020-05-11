from django.contrib import admin

# Register your models here.
from .models import (User, Site, SiteActivity, SiteActivityType, Report, PipeLineDIA, MHDIA, UPVCDIA, ICChamber)
admin.site.register(User)
admin.site.register(Site)
admin.site.register(SiteActivity)
admin.site.register(SiteActivityType)
admin.site.register(Report)
admin.site.register(PipeLineDIA)
admin.site.register(MHDIA)
admin.site.register(UPVCDIA)
admin.site.register(ICChamber)
