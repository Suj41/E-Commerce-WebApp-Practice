from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.customer import Customer
from django.views import View



class Signup(View):
      def get(self, request):
            return render(request, 'signup.html')
      
    #Customr Registartion Code
      def post(self, request):
        postData= request.POST
        firstname=postData.get('firstname')
        lastname=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')

        # Form Validation

        value={
                'firstname':firstname,
                'lastname':lastname,
                'phone': phone,
                'email':email
            }

        customer=Customer(firstname=firstname, 
                                  lastname=lastname, 
                                  phone=phone, 
                                  email=email,
                                  password=password)
        
        error_msg=self.validateCustomer(customer)

        if not error_msg:
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data={
                'value':value,
                'error':error_msg
            }    
            return render(request,'signup.html',data)
        
        # Customer Validation Code
      def validateCustomer(self, customer):
            error_msg=None
            if len(customer.firstname)<4:
                error_msg='First Name should be 4 character long.'
            elif len(customer.lastname)<4:
                error_msg='Last Name should be 4 character long.'
            elif len(customer.phone)!=10:
                error_msg='Phone Number should be 10 character long.'
            elif len(customer.password)<6 or len(customer.password)>14 :
                error_msg='Password length should be between 6-14 character.'
            elif customer.isExist():
                error_msg='Email Address already exist.'
     

            
            