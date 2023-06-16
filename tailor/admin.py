from django.contrib import admin
from . import models 


# Register your models here.
# MALE ADMIN--------------------------------------------------------------------------------
@admin.register(models.Male)
class MaleAdmin(admin.ModelAdmin):
    list_display = ["client_name", "client_phone_number", "head", "neck", "note"]
    list_filter = ["client_name", "client_phone_number", "head"]
    search_fields = ["client_name", "client_phone_number", "head"]

# FEMALE ADMIN--------------------------------------------------------------------------------
@admin.register(models.Female)
class FemaleAdmin(admin.ModelAdmin):
    list_display = ["client_name", "client_phone_number", "bust", "waist", "hips"]
    list_filter = ["client_name", "client_phone_number" ]
    search_fields = ["client_name", "client_phone_number" ]

# RECEIPTS ADMIN--------------------------------------------------------------------------------
@admin.register(models.Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ["unique_ID", "full_name", "invoice_date", "delivery_date", "total_price"]
    list_filter = [ "unique_ID", "full_name", "phone_number", "delivery_date"]
    search_fields = ["unique_ID", "full_name", "phone_number"]

# CATALOG ADMIN----------------------------------------------------------------------------------
@admin.register(models.Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ["product_name", "price", "date_created", "date_updated"]
    list_filter = [ "product_name", "price", "date_created"]
    search_fields = ["product_name", "price", "date_created"]

# READERS ADMIN -----------------------------------------------------------------------------------

@admin.register(models.Reader)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    list_filter = ["name", "email"]
    search_fields = ["name", "email"]

# AUTHOR ADMIN --------------------------------------------------------------------------------------------

@admin.register(models.Author)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]

# POST ADMIN ----------------------------------------------------------------------------------------------

@admin.register(models.Post)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ["title", "date_posted", "author"]
    list_filter = ["title", "date_posted", "author"]
    search_fields = ["title", "date_posted", "author"]

# COMMENT ADMIN--------------------------------------------------------------------------------------------

admin.site.register(models.Comment)
