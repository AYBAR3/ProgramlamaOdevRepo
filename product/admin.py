from django.contrib import admin
from product.models import Category, Product, Imagess, Comment


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}



class productImageInline(admin.TabularInline):
    model = Imagess
    Extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','price', 'amount','status','image']
    list_filter = ['status','category']
    inlines=[productImageInline]
    prepopulated_fields={'slug':('title',)}








class ImageAdmin(admin.ModelAdmin):
    list_display=['title','images','product']
    list_editable = ['images']


class commentAdmin(admin.ModelAdmin):
    list_display=['subject','status']
    list_editable = ['status']






admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Imagess,ImageAdmin)
admin.site.register(Comment,commentAdmin)
