from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/', include('todoapp.urls')),
    path("", views.taskList,)
]