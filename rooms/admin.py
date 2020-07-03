from django.contrib import admin
from . import models
from django.utils.html import mark_safe  # html return을 위해

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):  # 내장
    model = models.Photo  # Rooom에서 Photo 만들기


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    inlines = (PhotoInline,)  # Rooom에서 Photo 만들기

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")},),
        ("Spaces", {"fields": ("amenities", "facilities", "house_rules")},),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("guests", "beds", "bedrooms", "baths",),
            },
        ),
        ("Last Details", {"fields": ("host",)},),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    # ordering = (
    #     "name",
    #     "price",
    #     "bedrooms",
    # )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    raw_id_fields = ("host",)

    search_fields = ("=city", "^host__username")
    # =정확히 같다 , ^이것으로 시작
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def save_model(self,request, obj,form, change):
        obj.user =request.user
        super().save_model(request, obj,form, change)

    def count_amenities(self, obj):  # 자동이다. self는 class, obj는 내가 설정해놓은 admin의 row
        return obj.amenities.count()

    # count_amenities.short_description = "hello"
    # list_display의 count_amentities와 같은 이름의 함수

    def count_photos(self, obj):
        return obj.photos.count()
        # realated로 photos라고 설정했기 떄문에 photos란 이름으로 사용 가능


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"

