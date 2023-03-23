from django.shortcuts import render
from django.http import HttpResponse,request, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Product,Vehicle,Order,Order_detail,Customer
from django.urls import reverse
from datetime import datetime

# Create your views here.
def index(request):
    list = Vehicle.objects.all().values_list('company', flat=True).distinct()
    length= len(list)-1
    index_no=0
    vehicle_list=[]
    while length!=index_no:
        vehicle_list.append([list[index_no],list[index_no+1]])
        index_no+=2

    if length%2==0 :
        output= {'vehicle_list': vehicle_list}
    else:
        vehicle_list1 = list[:length - 1]
        output = {'vehicle_list': vehicle_list1,'last_vehicle': vehicle_list[length-1]}

    return render(request,'carparts/index.html',context=output)

def car_select(request,company):
    company_data= Vehicle.objects.all().filter(company=company)
    output = {'company_data': company_data,'company':company}
    return render(request, 'carparts/car_select.html',context=output)

def product(request,company):
    #name= request.POST.get('opt_carname')
    name= request.POST.get('carname')
    variant= request.POST.get('variant')
    model_no= request.POST.get('model_no')
    check= Vehicle.objects.filter(company=company,name= name,model_no=model_no, variant=variant).exists()

    if check:
        vehicle = Vehicle.objects.get(company=company, name=name, model_no=model_no, variant=variant)
        products= Product.objects.filter(vehicle_id=vehicle.pk)
        context={'products':products,'company':company,'url':"carparts:customer",
                 'car_name':name,'variant':variant,'model_no':model_no}
        return render(request, 'carparts/products.html', context=context)
    else:
        return render(request, 'carparts/car_select.html', {
            'error_message': "Product of select category is not available. ",
        })



def order(request,company):
    id_get= request.POST.get('prod_id')
    id= int(id_get)

    name= request.POST.get('car_name')
    variant= request.POST.get('variant')
    model_no= request.POST.get('model_no')
    #return HttpResponse(id)

    product= Product.objects.get(id=id)
    #return HttpResponse(product.unit_price)
    cust_name= request.POST.get('full_name')
    cust_address = request.POST.get('address')
    cust_phone = request.POST.get('phone')
    cust_email = request.POST.get('email')
    cust_city = request.POST.get('city')
    #return HttpResponse(cust_name)
    customer_obj= Customer(name=cust_name,phone_no=cust_phone,
                           city=cust_city,area_address=cust_address,email=cust_email)
    customer_obj.save()
    # order= Order(total_amount=product.unit_price,date_of_order=datetime.now(),customer_id=customer_obj.id)
    # order.save()
    # return render(request, 'carparts/order.html',context=None)
    order_ins=Order(total_amount=0, date_of_order=datetime.now(), customer_id=customer_obj.pk)
    order_ins.save()
    order_det= Order_detail(quantity=1,sub_total=product.unit_price,order_id=order_ins.pk,product_id=product.pk)
    order_det.save()
    customer_id= customer_obj.pk
    order_id= order_ins.pk
    vehicle = Vehicle.objects.get(company=company, name=name, model_no=model_no, variant=variant)
    products = Product.objects.filter(vehicle_id=vehicle.pk)
    context= {'company':company,'products':products,'cus_id':customer_id,'ord_id':order_id,'url':'carparts:add_item','add':'add',
              'car_name':name,'variant':variant,'model_no':model_no}
    return render(request,'carparts/products.html',context)



def add_item(request,company):
    cus_id = request.POST.get('cus_id')
    ord_id = request.POST.get('ord_id')
    prod_id = request.POST.get('prod_id')
    name= request.POST.get('car_name')
    variant= request.POST.get('variant')
    model_no= request.POST.get('model_no')
    product= Product.objects.get(id=prod_id)
    check= Order_detail.objects.filter(product_id=prod_id).exists()

    #return HttpResponse(cus_id)
    if check:
        ord_det_upd= Order_detail.objects.get(product_id=prod_id)
        ord_det_upd.quantity+=1
        ord_det_upd.sub_total+= product.unit_price
        ord_det_upd.save()
    else:
        order_det = Order_detail(quantity=1, sub_total=product.unit_price, order_id=ord_id, product_id=prod_id)
        order_det.save()
    vehicle = Vehicle.objects.get(company=company, name=name, model_no=model_no, variant=variant)
    products = Product.objects.filter(vehicle_id=vehicle.pk)
    context= {'company':company,'products':products,'cus_id':cus_id,'ord_id':ord_id,'url':'carparts:add_item',
              'car_name':name,'variant':variant,'model_no':model_no}
    return render(request,'carparts/products.html',context)



def customer(request,company):
    name= request.POST.get('car_name')
    variant= request.POST.get('variant')
    model_no= request.POST.get('model_no')
    id = request.POST.get('prod_id')
    #product= Product.objects.get(id=id)
    vehicle = Vehicle.objects.get(company=company, name=name, model_no=model_no, variant=variant)
    products = Product.objects.filter(vehicle_id=vehicle.pk)
    return render(request, 'carparts/customer.html', {'products':products,
        'prod_id': id,'company':company,'url':'carparts:order',
        'car_name': name, 'variant': variant, 'model_no': model_no
    })









