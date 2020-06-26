from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """Time Stamped Model"""

    # 공통부분
    created = models.DateTimeField(auto_now_add=True)
    # auto now add는 생성시 자동으로
    updated = models.DateTimeField(auto_now=True)
    # auto now는 업데이트시 자동으로
    class Meta:
        abstract = True
        # 단순히 확장을 위해서 사용되며, 데이터베이스로 이동되지 않는다.
