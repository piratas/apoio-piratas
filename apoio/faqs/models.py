
from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone



class Question(models.Model):
    PENDING  = 'PE'
    APPROVED = 'AP'

    QUESTION_STATUS = ( (PENDING, 'Pending'), (APPROVED, 'Approved'), )

    question_text   = models.CharField(max_length=200)
    question_status = models.CharField(max_length=2, choices=QUESTION_STATUS, default=PENDING)
    pub_date        = models.DateTimeField('date published')

    def is_upperclass(self):
        return self.question_status in (self.PENDING, self.APPROVED)

    def was_published_recently(self):
        if self.question_status == self.APPROVED:
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Answer(models.Model):
    question     = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text  = models.TextField()
    answer_vote  = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100),])
    pub_date     = models.DateTimeField('date published')

    def was_answered_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

