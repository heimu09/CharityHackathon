from django.db import models

class Donation(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=15)
    telegram = models.CharField("Телеграм", max_length=255, null=True, blank=True)
    amount = models.DecimalField("Сумма", max_digits=10, decimal_places=2)
    initiative = models.CharField("Инициатива", max_length=255, default="Благотворительность")
    donation_date = models.DateTimeField("Дата пожертвования", auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.initiative} - {self.amount}"

    class Meta:
        verbose_name = "Пожертвование"
        verbose_name_plural = "Пожертвования"


class BulletinBoard(models.Model):
    full_name = models.CharField('ФИО', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=15)
    required_amount = models.IntegerField('Необходимая сумма')
    telegram = models.CharField('Телеграм', max_length=255)
    message = models.TextField('Сообщения')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{}: {}".format(self.full_name, self.telegram)

    class Meta:
        verbose_name = "Доска объявления"
        verbose_name_plural = "Доски объявлений"
