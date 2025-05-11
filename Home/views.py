from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import usersForm

# Create your views here.
def home(request):
    # context={
    #     'variable':"Hello developer , How are you?"
    # }
    # return render(request,'index.html',context)
    #return HttpResponse("This is home page")
     if request.method=='GET':
          output=request.GET.get('output')

     return render(request,'index.html',{'output':output})

def about(request):
     return render(request,'about.html')
    # return HttpResponse("This iS ABOUT page")

def food(request):
     return render(request,'food.html')

def orders(request):
     data={}
     try:
          if request.method=='POST':
               name=request.POST.get('name')
               phone=request.POST.get('phone')
               address=request.POST.get('address')
               food=request.POST.get('food')
               quantity=request.POST.get('quantity')
          
          data={
               'Name':name,
          'Phone':phone,
          "Address":address,
          'Food':food,
          'Quantity':quantity
          }
          url='/delivery/?output={}'.format(data)
          return HttpResponseRedirect(url)

     except:
          print('Invalid input')

     return render(request,'order.html')
    
def delivery(request):
     if request.method=='GET':
          output=request.GET.get('output')
     return render(request,'delivery.html',{'output':output})
    

def contact(request):
     detail={}
     try:
          if request.method=='POST':
               n1=request.POST.get('name')
               n2=request.POST.get('email')
               n3=request.POST.get('subject')
               n4=request.POST.get('message')

          detail={
          'Name':n1,
          'Email':n2,
          "Subject":n3,
          'Message':n4
     }
          # url='/?output={}'.format(detail)
          # return redirect(url)

     except:
          print('I got some error in your form filling')

     
     return render(request,'contact.html',{"output":detail})
    # return HttpResponse("This is a contact us page")

def submitform(request):
     fn=usersForm()
     data={'form':fn}
     return render(request,'userform.html',data) 

def calculator(request):
     
     return render(request,'calculator.html') 