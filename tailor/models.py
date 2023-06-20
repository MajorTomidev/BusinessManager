from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
import uuid

# Create your models here.

# MALE MEASUREMENTS --------------------------------------------------------------------------------

class Male(models.Model):
    client_name = models.CharField(max_length=100)
    client_address = models.TextField(blank=True, null=True)
    client_phone_number = models.CharField(max_length=11)
    client_email = models.EmailField(blank=True, null=True)
    head = models.PositiveIntegerField()
    neck = models.PositiveIntegerField()
    shoulder_length = models.PositiveIntegerField()
    chest = models.PositiveIntegerField()
    back = models.PositiveIntegerField()
    arm_length_short = models.PositiveIntegerField()
    arm_length_long = models.PositiveIntegerField()
    biceps = models.PositiveIntegerField()
    belly = models.PositiveIntegerField()
    wrist = models.PositiveIntegerField()
    top_length = models.PositiveIntegerField()
    trouser_length = models.PositiveIntegerField()
    waist = models.PositiveIntegerField()
    laps = models.PositiveIntegerField()
    calf = models.PositiveIntegerField()
    ankle = models.PositiveIntegerField()
    note = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add= True, verbose_name= ('Date Created'))
    date_updated = models.DateTimeField(auto_now= True, verbose_name= ('Last Updated'))
    

    def __str__(self):
        return self.client_name
    
    class Meta:
        verbose_name = ('Male')
        verbose_name_plural = ('Male Measurements')
        ordering = ['client_name']

# FEMALE MEASUREMENTS ------------------------------------------------------------------------------------------------------

class Female(models.Model):
    client_name = models.CharField(max_length=100)
    client_address = models.TextField(blank=True, null=True)
    client_phone_number = models.CharField(max_length=11)
    client_email = models.EmailField(blank=True, null=True)
    bust = models.PositiveIntegerField()
    waist = models.PositiveIntegerField()
    hips = models.PositiveIntegerField()
    bust_apex = models.PositiveIntegerField()
    shoulder = models.PositiveIntegerField()
    neck_to_waist = models.PositiveIntegerField()
    arm_length_long = models.PositiveIntegerField()
    arm_length_short = models.PositiveIntegerField()
    belly = models.PositiveIntegerField()
    wrist = models.PositiveIntegerField()
    note = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add= True, verbose_name= ('Date Created'))
    date_updated = models.DateTimeField(auto_now= True, verbose_name= ('Last Updated'))
    

    def __str__(self):
        return self.client_name
    
    class Meta:
        verbose_name = ('Female')
        verbose_name_plural = ('Female Measurements')
        ordering = ['client_name']

# CATALOG ------------------------------------------------------------------------------------------------------------------

class Catalog (models.Model):
    image = models. ImageField(default='catalog.jpg', upload_to='catalog_images')
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add= True, verbose_name= ('Date Created'))
    date_updated = models.DateTimeField(auto_now= True, verbose_name= ('Last Updated'))


    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = ('Catalog')
        verbose_name_plural = ('Catalogues')
        ordering = ['product_name']
    
# RECEIPTS --------------------------------------------------------------------------------------------------------------

class Receipt (models.Model):
   logo = models. ImageField(default='receipt.jpg', upload_to='receipt_images')
   unique_ID = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
   client_name = models.CharField(max_length=200)
   item = models.ManyToManyField(Catalog, blank=True)
   description = models.CharField(max_length=100)
   phone_number = models.CharField(max_length=11)
   invoice_date = models.DateTimeField(auto_now_add=True)
   delivery_date = models.DateTimeField(auto_now_add=True)
   quantity = models.PositiveIntegerField()
   discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
   unit_price = models.DecimalField(max_digits=10, decimal_places=2)
   total_price = models.DecimalField(max_digits=10, decimal_places=2)
   date_created = models.DateTimeField(auto_now_add= True, verbose_name= ('Date Created'))
   date_updated = models.DateTimeField(auto_now= True, verbose_name= ('Last Updated'))

   def __str__(self):
        return self.client_name
   
   class Meta:
        verbose_name = ('Receipt')
        verbose_name_plural = ('Receipts')
        ordering = ['unique_ID']


# BLOG ----------------------------------------------------------------------------------------------------------------

class BlogImage(models.Model):
    image = models.ImageField(default='blog.jpg', upload_to='album_pictures', null=True, blank=True)  

class Blog(models.Model):
    blog_image = models.ManyToManyField(BlogImage, blank=True)
    blog_headline = models.CharField(max_length=255)
    blog_category = models.CharField(max_length=100)
    blog_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published= models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_headline
    
    class Meta:
        verbose_name = ('Blog')
        verbose_name_plural = ('Blogs')
        ordering= (
            '-date_published',
        )

class Comment(models.Model):
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment= models.TextField()
    date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.blog.blog_headline}-comment'
    
    class Meta:
        verbose_name = ('Comment')
        verbose_name_plural = ('Comments')
        ordering = (
            '-date',
        )

    
    
