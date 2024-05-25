from django.contrib import admin

from .models import Sale
from listings.models import Listing


def approve(modeladmin, request, queryset):
  for sale in queryset:
    # Tạo một đối tượng Listing mới với các thông tin từ Sale
    listing = Listing(
      realtor=sale.realtor,
      title=sale.title,
      address=sale.address,
      city=sale.city,
      zipcode=sale.zipcode,
      description=sale.description,
      price=sale.price,
      bedrooms=sale.bedrooms,
      bathrooms=sale.bathrooms,
      garage=sale.garage,
      squaremeters=sale.squaremeters,
      lot_size=sale.lot_size,
      photo_main=sale.photo_main,
      photo_1=sale.photo_1,
      photo_2=sale.photo_2,
      photo_3=sale.photo_3,
      photo_4=sale.photo_4,
      photo_5=sale.photo_5,
      photo_6=sale.photo_6,
      is_published=True,  # Chuyển sang table listing, nên đánh dấu đã xuất bản
      list_date=sale.list_date,
    )
    listing.save()  # Lưu đối tượng Listing mới

    # Xóa đối tượng Sale hiện tại
    sale.delete()
  approve.short_description = "Approve selected sales"  # Mô tả hành động
class SaleAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price')
  list_per_page = 25
  actions = [approve]  # Đăng ký hành động approve vào trang admin






admin.site.register(Sale, SaleAdmin)