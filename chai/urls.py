
from django.urls import path
from . import views


urlpatterns = [
    path("",views.all_chai,name="chai"),
    path("<int:chai_id>",views.chai_detail,name="chai_detail"),

    
]