from django.db import models


# Доска объявлений
class BulletinBoard(models.Model):
    name = models.CharField('Имя', max_length=70)
    phone_number = models.CharField('Номер телефона', max_length=15)
    required_amount = models.IntegerField('Необходимая сумма')
    telegram = models.CharField('Телеграм', max_length=255)
    position = models.CharField('Должность', max_length=70, null=True, blank=True)
    message = models.TextField('Сообщения')

    create_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return "{}: {}".format(self.name, self.telegram)
    
    class Meta:
        verbose_name = "Доска объявления"
        verbose_name_plural = "Доски объявлений"
    

# class DistributionNeeds(models.Model):
#     name = models.CharField('Нужда', max_length=255)
#     percent = models.FloatField('Процент')


