from django.urls import path
# from office.views import IndexView,EmployeeCreateView,EmployeeListView,EmployeeDetailView,EmployeeUpdateView, EmployeeDeleteView
from . import views
app_name = 'office'

urlpatterns = [
    path('',views.IndexView,name='index_view'),
    path('create_employee/',views.EmployeeCreateView.as_view(),name='create_employee'),
    path('list_employee/',views.EmployeeListView.as_view(),name='list_employee'),
    path('detail_employee/<int:pk>/',views.EmployeeDetailView.as_view(),name='detail_employee'),
    path('update_employee/<int:pk>/',views.EmployeeUpdateView.as_view(),name='update_employee'),
    path('delete_employee/<int:pk>/',views.EmployeeDeleteView.as_view(),name='delete_employee'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('user/',views.userview,name='user'),
]
