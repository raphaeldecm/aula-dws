from django.urls import path

from enquetes import views

urlpatterns = [
    # serão substituídas por urls para as baseviews
    path('', views.index, name='index'),
    path('<int:question_id>', views.details, name='detail'),
    path('create', views.create_question, name="create_pull"),
    path('create_choices/<int:id>', views.create_choices, name="create-choices"),
    path('create-user', views.create_user, name="create_user"),
    path('vote/<int:question_id>', views.vote, name="vote"),
    #path('', views.IndexView.as_view(), name="index"),
    # como está usando class views, o nome do atributo tem de ser pk
    #path('<int:pk>', views.DetailView.as_view(), name="detail")
]
