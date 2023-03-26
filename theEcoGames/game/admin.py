from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Activity)
admin.site.register(ActivityLog)
admin.site.register(Tip)
admin.site.register(MeterReading)
admin.site.register(Award)
admin.site.register(Location)
admin.site.register(Faction)
admin.site.register(Challenger)
admin.site.register(Riddles)


# admin.site.register(ManyToManyTable_ActivityForm)
admin.site.register(UserTip)

# Register your models here.
