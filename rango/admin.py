from django.contrib import admin
from rango.models import Category, Page  # 不要改，改了运行admin报错


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')


# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)  # 这里逻辑没懂...
