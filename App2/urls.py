from django.urls import path
from App2 import views

urlpatterns = [
    # path('homeurl/',views.home,name="home"),
    # path('index/',views.index,name='index'),
    # path('student',views.student,name='student'),
    # path('valueurl/<int:val>',views.valuesend,name='valuesend'),
    # path('table/<int:v>',views.table,name='table'),
    # path('sample/',views.sample,name='sample'),
    path('register/',views.register, name='register'),
    path('display/',views.displey_details, name='details'),
    path('update/<int:id>',views.update_details, name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('signup/',views.signup,name="signup"),

]