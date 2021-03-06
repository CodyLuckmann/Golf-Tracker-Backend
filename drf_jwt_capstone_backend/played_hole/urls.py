from django.urls import path
from played_hole import views

urlpatterns = [
    path('all/', views.get_all_played_holes),
    path('', views.create_played_hole),
    path('user/', views.get_played_hole_by_user),
    path('update/<int:played_hole_id>', views.update_played_hole),
    path('delete/<int:played_hole_id>', views.delete_played_hole),
    path('date/<int:course_id>/<str:dt>', views.get_hole_by_date),
    path('putts/<int:course_id>/<str:dt>', views.get_total_putts),
    path('alldates/<int:course_id>', views.get_all_dates),
]