from django.urls import path

from study import views

app_name = 'study'

urlpatterns = [
    path('home/', views.HomeStudyView.as_view(), name='home'),
    path('create-word/html/', views.CreateWordView.as_view(), name='create_word_html'),
    path('create-word/crispy/', views.CrispyCreateWordView.as_view(), name='create_word_crispy'),
]
