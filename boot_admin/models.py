from django.db import models
from django.conf import settings
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    hashtag = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="event_post_set")
    deadline = models.DateTimeField()
    update_date = models.DateTimeField(auto_now_add=True)

#    is_publish = models.BooleanField(default = False)
# 정렬조건 지정 위 class 하위로 지정해야 함. 같은 레벨 아님 !!

    class Meta:
        ordering = ['-update_date', '-id']  # ==> desc로 정렬

    def generate(self):
        self.title = ""
        self.hashtag = "#이벤트"
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.title}, {self.user}'
