from Ask.managers import *
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone


class User(AbstractUser):
    avatar = models.ImageField(default="Ask/img/no_avatar.png", upload_to='uploads/%Y/%m/%d/')
    registerDate = models.DateTimeField(default=timezone.now, verbose_name="Profile created")

    objects = UserManager()

    def __str__(self):
        return self.username


class Tag(models.Model):
    title = models.CharField(verbose_name="Tag", max_length=25)
    objects = TagManager()

    def __str__(self):
        return self.title


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField(verbose_name="Голос", choices=VOTES)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()

    def __str__(self):
        return self.user.username + " liked"


class Question(models.Model):
    author = models.ForeignKey(User, null=False, verbose_name="Question Author", on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, verbose_name='Question date')
    title = models.CharField(max_length=70, verbose_name='Question Title')
    text = models.TextField(verbose_name='Question full text')
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True, verbose_name='Tags')
    votes = GenericRelation(LikeDislike, related_query_name='questions')
    rate = models.IntegerField(default=0, null=False, verbose_name='Rate')

    objects = QuestionManager()

    def __str__(self):
        return self.author.username


class Answer(models.Model):
    author = models.ForeignKey(User, null=False, verbose_name="Answer Author", on_delete=models.CASCADE)
    title = models.CharField(max_length=70, verbose_name='Answer Title')
    text = models.TextField(verbose_name='Answer full text')
    question = models.ForeignKey(Question, null=False, verbose_name="Question", on_delete=models.CASCADE)
    votes = GenericRelation(LikeDislike, related_query_name='answers')
    rate = models.IntegerField(default=0, null=False, verbose_name='Rate')

    objects = AnswerManager()

    def __str__(self):
        return self.author.username
