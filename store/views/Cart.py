from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.

# Index Class
class Cart(View):
     def get(self, request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_product_by_id(ids)
        return render(request,'cart.html',{'products':products})
    
     





        
 
    

            
            
    

            
      
          
        

