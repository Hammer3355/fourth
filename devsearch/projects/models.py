from django.db import models


# ForeingKey - один ко многим
# ManyToManyField - многие ко многим
# OneToOneField - один к одному


class Project(models.Model):
    title = models.CharField(max_length=200)  # CharField - Короткое текстовое поле
    description = models.TextField(null=True,
                                   blank=True)  # TextField - Большое текстовое поле. Если поле  не заполнено, по умолчанию заполняется значением null.blank=True - Поле не ообязательное для заполнения.
    featured_image = models.ImageField(upload_to='projects/%Y/%m/%d/',
                                       default='default.jpg')  # upload_to='projects/%Y/%m/%d/' - Создается папка projects и в ней папки с датами в которых будут храниться ДИНАМИЧЕСКИЕ изображения.default='default.jpg' - изображения по умолчанию.
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)  # ManyToManyField - многие ко многим
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)  # IntegerField - Числовое поле
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)  # Заполняется автоматически в момент создания.

    def __str__(self):
        return self.name
