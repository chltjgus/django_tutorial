from django.urls import path

from . import views

# html파일에서 href로 끌어다 쓸 때 어디에 위치해 있는지 알려주기 위해 app_name을 지정
# html 파일에선 href="{% url 'polls:detail' question.id %}" 이런식으로 표기
app_name = "polls"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.IndexView.as_view(), name="index"),

    # path("<int:question_id>/", views.detail, name="detail"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # path("<int:question_id>/results/", views.results,name="results"),
    path("<int:pk>/results/", views.ResultView.as_view(), name="detail"),

    path("<int:question_id>/vote/", views.vote, name="vote"),
]