from django.urls import path,include
from main import views

app_name='main'

urlpatterns = [
    path('', views.title_view, name='home'),
    path('add/', views.add_content, name='add'),
    path('<int:pk>', views.info_view, name='info'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/edit/', views.Edit_Info, name='edit_info'),
    path('<int:pk>/edit/xaraktiristika', views.Edit_Xaraktiristika.as_view(), name='edit_xaraktiristika'),
    path('<int:pk>/edit/sxoleio', views.Edit_Sxoleio.as_view(), name='edit_sxoleio'),
    path('<int:pk>/edit/ekpedeftikoi', views.Edit_Ekpedeftikoi.as_view(), name='edit_ekpedeftikoi'),
    path('<int:pk>/edit/goneis', views.Edit_Goneis.as_view(), name='edit_goneis'),
    path('<int:pk>/edit/sindesmoi', views.Edit_Sindesmoi.as_view(), name='edit_sindesmoi'),
    
]
