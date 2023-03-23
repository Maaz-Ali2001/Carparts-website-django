from django.urls import path
from . import views

app_name = 'carparts'

# urlpatterns=[path("",views.index,name='index')
#     ,path("<int:question_id>/",views.details,name='details'),
#              path('<int:question_id>/vote/', views.vote, name='vote'),path('<int:question_id>/vote/results'
#                                 ,views.results,name='results')]

urlpatterns=[path("",views.index,name='index'),
             path('<str:company>/',views.car_select, name='car_select'),
             path('<str:company>/product/',views.product,name='product'),
             path('<str:company>/customer/',views.customer,name='customer'),
             path('<str:company>/order/',views.order,name='order'),
             path('<str:company>/add/',views.add_item,name='add_item')]