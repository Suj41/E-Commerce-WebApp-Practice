from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.

# Index Class
class Index(View):
     def get(self, request):
        cart=request.session.get('cart')
        if not cart:
             request.session['cart']={}
        product=None
        category=Category.get_all_category()
        category_id=request.GET.get('category')
        if category_id:
            product=Product.get_all_products_by_categoryid(category_id)
        else:
            product=Product.get_all_products()
        data={}
        data['category']=category
        data['product']=product
        print('you are:',request.session.get('email'))
        return render(request,'index.html', data)
    
     def post(self, request):
          product=request.POST.get('product')
          cart=request.session.get('cart')
          remove=request.POST.get('remove')
          if cart:
               quantity=cart.get(product)
               if quantity is not None:
                    if remove:
                        if quantity is not None:
                             cart.pop(product, None)
                        else:
                            cart[product]=quantity-1
                    else:
                        cart[product]=quantity+1
               else:
                    cart[product]=1
          else:
               cart={}
               cart[product]=1
          request.session['cart']=cart
          print(request.session['cart'])
          return redirect('homepage')






        
 
    

            
            
    

            
      
          
        

