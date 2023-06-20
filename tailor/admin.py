from django.contrib import admin
from . import models 


# Register your models here.

# MALE ADMIN-----------------------------------------------------------------------------------

@admin.register(models.Male)
class MaleAdmin(admin.ModelAdmin):
    list_display = ["client_name", "client_phone_number", "head", "neck", "note"]
    list_filter = ["client_name", "client_phone_number", "head"]
    search_fields = ["client_name", "client_phone_number", "head"]

# FEMALE ADMIN-----------------------------------------------------------------------------------

@admin.register(models.Female)
class FemaleAdmin(admin.ModelAdmin):
    list_display = ["client_name", "client_phone_number", "bust", "waist", "hips"]
    list_filter = ["client_name", "client_phone_number" ]
    search_fields = ["client_name", "client_phone_number" ]

# CATALOG ADMIN----------------------------------------------------------------------------------

@admin.register(models.Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ["product_name", "price", "date_created", "date_updated"]
    list_filter = [ "product_name", "price", "date_created"]
    search_fields = ["product_name", "price", "date_created"]

# RECEIPTS ADMIN--------------------------------------------------------------------------------

@admin.register(models.Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ["unique_ID", "client_name", "invoice_date", "delivery_date", "total_price"]
    list_filter = [ "unique_ID", "client_name", "phone_number", "delivery_date"]
    search_fields = ["unique_ID", "client_name", "phone_number"]


# BLOG ADMIN --------------------------------------------------------------------------------------

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["blog_headline", "blog_category", "author", "date_published", "date_updated"]
    list_filter = ["blog_headline", "blog_category", "author", "date_published"]
    search_fields = ["blog_headline", "blog_category", "author"]

# COMMENT ADMIN----------------------------------------------------------------------------------

admin.site.register(models.Comment)
