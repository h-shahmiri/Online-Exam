from django.contrib import admin
from .models import Questions , Chosen , Users

# Register your models here.


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id','questpack','A','B','C','D','truequest')
    fieldsets    = (('Main' ,{'fields':[('questpack','truequest')]}),
                    ('off'  ,{'fields':[('A','B','C','D')]}),
                    )

    search_fields = ('questpack',)
    list_filter   = ('questpack','truequest')
admin.site.register(Questions , QuestionsAdmin)


class ChosenAdmin(admin.ModelAdmin):
    list_display = ('id','questpack','A','AB','B','BB','C','CB','D','DB', 'none','truequest')
    fieldsets    = (('Main' ,{'fields':[('questpack','truequest')]}),
                    ('off'  ,{'fields':[('A','AB'), ('B','BB'), ('C','CB'), ('D','DB')]}),
                    )
admin.site.register(Chosen , ChosenAdmin)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','username','password','email')
admin.site.register(Users , UsersAdmin)
