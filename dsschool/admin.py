from django.contrib import admin
from dsschool.models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    # 여러개의 항목을 보여주기 위해서
    list_display = ['pk', 'name', 'short_summary', 'discount', ]
    list_display_links = ['name']
    search_fields = ['name', 'summary']
    list_filter = ['name']

    # 어떤 item(모델)이 있으면, 그 모델의 필드(text)를 2개까지 가져오겠다.
    def short_summary(self, item):
        return item.summary[:20]
