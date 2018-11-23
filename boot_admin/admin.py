from django.contrib import admin
from boot_admin.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # 여러개의 항목을 보여주기 위해서
    list_display = ['pk', 'title', 'content', 'hashtag', 'user', 'deadline', ]
    list_display_links = ['title']
    search_fields = ['title', 'hashtag']
    list_filter = ['title']

    # 어떤 item(모델)이 있으면, 그 모델의 필드(text)를 2개까지 가져오겠다.
    def short_content(self, item):
        return item.content[:20]
