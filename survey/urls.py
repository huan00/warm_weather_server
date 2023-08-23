from django.urls import path, include

from .views import SurveyView
from . import views

urlpatterns = [ 
    path('create', SurveyView.as_view(), name='create_survey'),
    path('get_question/<int:pk>', views.get_question, name='get_question'),
    path('get/<int:pk>', views.get_survey, name='get_survey' ),
    
    ]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]