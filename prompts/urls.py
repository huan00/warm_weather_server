from django.urls import path, include

from .views import PromptsView

urlpatterns = [ 
    path('prompts', PromptsView.as_view(), name='prompts')
    
    ]

# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls'))
# ]