from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() - datetime.timedelta(days=5)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_question_count(self):
        Question.objects.create(question_text="test",pub_date=timezone.now())
        self.assertEqual(Question.objects.count(),1)

    def test_question_instance(self):
        Question.objects.create(question_text="test",pub_date=timezone.now())
        self.assertIsInstance(Question.objects.first(),Question)

    def test_question_update(self):
        # Question을 만든다
        question = Question.objects.create(question_text="test",pub_date=timezone.now())

        # Question에 대한 update를 수행한다
        question.question_text = "update"
        question.save()

        # update가 잘 되었는지 확인한다.
        self.assertEqual(Question.objects.first().question_text,"update")

    def test_delete_question(self):
        question = Question.objects.create(question_text="test",pub_date=timezone.now())
        question.delete()
        self.assertEqual(Question.objects.count(),0)

    def test_num1(self):
        li = [x for x in range(1,101)]
        self.assertEqual(sum(li),5050)
        self.assertEqual(len(li),100)

    def test_num2(self):
        dic = {x:x**2 for x in range(1,11)}
        self.assertEqual(sum(dic.values()),385)

    def test_num3(self):
        dic = {"x":1,"y":2,"z":3}
        self.assertIsInstance(dic,dict)

    def test_num4(self):
        data = None
        self.assertIsNone(data)

    def test_num5(self):
        data = False
        self.assertFalse(data)



def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):


    def test_no_questions(self):
        res=self.client.get(reverse("polls:index"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "No polls are available")
        self.assertQuerySetEqual(res.context["latest_question_list"], [])

    def test_past_question(self):
        question = create_question(question_text="Past question", days=-30)
        res = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(res.context["latest_question_list"], [question])


