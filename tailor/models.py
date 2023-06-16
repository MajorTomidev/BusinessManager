from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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
        ordering = ['id']

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
        ordering = ['id']

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
        ordering = ['id']
    
# RECEIPTS --------------------------------------------------------------------------------------------------------------

class Receipt (models.Model):
   logo = models. ImageField(default='receipt.jpg', upload_to='receipt_images')
   unique_ID = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
   client_name = models.CharField(max_length=200)
   item = models.CharField(max_length=100)
   description = models.CharField(max_length=100)
   phone_number = models.CharField(max_length=11)
   invoice_date = models.DateTimeField(auto_now_add=True)
   delivery_date = models.DateTimeField(auto_now_add=True)
   quantity = models.PositiveIntegerField()
   discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
   unit_price = models.DecimalField(max_digits=10, decimal_places=2)
   total_price = models.DecimalField(max_digits=10, decimal_places=2)

   def __str__(self):
        return self.client_name
   
   class Meta:
        verbose_name = ('Receipt')
        verbose_name_plural = ('Receipts')
        ordering = ['id']


# BLOG ----------------------------------------------------------------------------------------------------------------

class Reader(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Reader')
        verbose_name_plural = ('Readers')
        ordering = ['id']


class Author(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Author')
        verbose_name_plural = ('Authors')
        ordering = ['id']


class Post(models.Model):
    title = models.CharField(max_length=100)
    content= models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')
        ordering= (
            '-date_posted',
        )


class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    comment_text= models.TextField()
    date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.title}-comment'
    
    class Meta:
        verbose_name = ('Comment')
        verbose_name_plural = ('Comments')
        ordering = ['id']

      
    
    
