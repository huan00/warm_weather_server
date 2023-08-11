from django.urls import path, include

from .views import SurveyView

urlpatterns = [ 
    path('survey', SurveyView.as_view(), name='create_survey')
    
    ]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]