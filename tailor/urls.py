from django.urls import path
from .views import MaleView, MaleViewTest, FemaleView, FemaleViewTest, CatalogView, ReceiptView, BlogSingleView, BlogView, CommentViewTest

urlpatterns =[
    path('male/', MaleView, name= 'malepage'),
    path('test/', MaleViewTest, name= 'test_male'),
    path('female/', FemaleView, name= 'femalepage'),
    path('test/', FemaleViewTest, name= 'test_fml'),
    path('catalog/', CatalogView, name= 'catalogpage'),
    path('receipt/', ReceiptView, name= 'receiptpage'),
    path('blog/<int:pk>/', BlogSingleView, name= 'blogsinglepage'),
    path('blog/', BlogView, name= 'blogpage'),
    path('test/', CommentViewTest, name= 'test_cmt'),
]