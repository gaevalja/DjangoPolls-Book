from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):# admin.StackedInline
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [ #필드 분리
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # CHoiceInline 클래스 인클루드 하여 Question을 생성, 수정할 때 Choice도 같이 보여줌
    list_display = ('question_text','pub_date',)# 컬럼(제목) 추가
    list_filter = ['pub_date']# 필터 사이드 바
    search_fields = ['question_text'] # 검색 기능

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)