from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from api.models import *
from .models import News
from django.core.paginator import Paginator
from django.core.mail import send_mail

# Create your views here.
def home(request):
    # context={
    #     'variable':"Hello developer , How are you?"
    # }
    # return render(request,'index.html',context)
    #return HttpResponse("This is home page")
     # if request.method=='GET':
     #      output=request.GET.get('output')
     newsData=News.objects.all()
     homeData=Homepage.objects.all()
     data={
          'homeData':homeData,
          'newsData':newsData,
     }

     return render(request,'index.html',data)

def about(request):
     ServiceData=Service.objects.all()
     memberData=TeamMember.objects.all()
     data={
          'ServiceData':ServiceData,
          'memberData':memberData
          }
     return render(request,'about.html',data)
    # return HttpResponse("This iS ABOUT page")

def food(request):
     foodData=FoodItem.objects.all().order_by('food_name')                 #[:3] this is limiting concept for showing number of content is 3.
     if request.method=='GET':
          st=request.GET.get('foodSearching')
          if st !=None:                 #__icontains it is using for single character and more character aur exact mactch 
               foodData=FoodItem.objects.filter(food_name__icontains=st)
     
     paginator=Paginator(foodData,4)
     page_number=request.GET.get('page')
     foodDataFinal=paginator.get_page(page_number)
     totalpage=foodDataFinal.paginator.num_pages
     data={
          'foodData':foodDataFinal,
          'totalpagelist':[i+1 for i in range(totalpage)]
     }
     return render(request,'food.html',data)


def orders(request, food_id):
    food = get_object_or_404(FoodItem, id=food_id)
    return render(request, 'order.html', {'food': food})

def orderSuccessful(request,food_id):
     food = get_object_or_404(FoodItem, id=food_id)
     if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))  # defaults to 1 if not sent
        payment_method = request.POST.get('payment_method')
        total_price = food.price * quantity

        # Save the order
        Order.objects.create(
            food=food,
            quantity=quantity,
            total_price=total_price,
            payment_method=payment_method,
        )
     return render(request, 'order_success.html', {'food': food,'total_price':total_price})

    
    
def delivery(request):
     if request.method=='GET':
          output=request.GET.get('output')
     return render(request,'delivery.html',{'output':output})
    

def contact(request):
     return render(request,'contact.html')
    # return HttpResponse("This is a contact us page")


def newsdetails(request,slug):
     newsDetail=News.objects.get(news_slug=slug)
     data={
          'newsDetail':newsDetail
     }

     return render(request,'newsdetails.html',data)

def contactformsave(request):
     detail={}
     try:
          if request.method=='POST':
               n1=request.POST.get('name')
               n2=request.POST.get('email')
               n3=request.POST.get('subject')
               n4=request.POST.get('message')
              
               if not ContactFormEnquiry.objects.filter(email=n2).exists():
                    data=ContactFormEnquiry(name=n1, email=n2, subject=n3,message=n4)
                    data.save()
                    detail={
                    "message":"Data is Submited",
                    "name":n1
                   }
               else:
                    detail={
                    "message":"You are already contact us Admin",
                    "name":n1
                   }
               send_mail (
                    subject = f'According to your {n3}',
                    message = f'Dear {n1},' + '''
We would like to inform you that your issue is currently being addressed and will be resolved shortly. 
We appreciate your patience and understanding.
Thank you for your patience.

Best regards,
My Restaurant''',
                    from_email = 'priyeshm845@gmail.com',
                    recipient_list = [n2],
                    fail_silently=True,
               )
          

     except:
          detail={
               "message":"You make Some Error Input field",
               'name':"Anonymous User"
          }

     return render(request,'contact.html',detail)