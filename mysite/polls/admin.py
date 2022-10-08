from django.contrib import admin

# Register your models here.

from .models import Question, Choice

# admin.site.register(Question)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "status",
                    "order"]
    list_display_links = ['pub_date',]
    list_editable = ['status',]

admin.site.register(Choice)