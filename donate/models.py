#models.py
from django.db import models

class Donation(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=15)
    telegram = models.CharField("Телеграм", max_length=255, null=True, blank=True)
    amount = models.DecimalField("Сумма", max_digits=10, decimal_places=2)
    initiative = models.CharField("Инициатива", max_length=255, default="Благотворительность")
    donation_date = models.DateTimeField("Дата пожертвования", auto_now_add=True)

    currency = models.CharField(max_length=3)
    description = models.CharField(max_length=255)
    stripe_token = models.CharField(max_length=255)

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


class Expense(models.Model):
    amount = models.DecimalField('Сумма', max_digits=10, decimal_places=2)
    description = models.CharField('Описание', max_length=255)
    comment = models.TextField('Комментарий', blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Расход на {self.description}: {self.amount}"

    def save(self, *args, **kwargs):
        if self.amount > 0:
            self.amount = -self.amount
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"


class CrowdFunding(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    telegram = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    goal = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.full_name}: {self.title}"


class CryptoDonation(models.Model):
    account_number = models.CharField("Ваш номер счета", max_length=50)
    address = models.CharField("Наш адрес", max_length=50, default="DS717DA7128D94")
    amount = models.DecimalField("Сумма ввода", max_digits=10, decimal_places=2)
    cryptocurrency = models.CharField("Криптовалюта", max_length=50, default="USDT")
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.amount} {self.cryptocurrency}"

    class Meta:
        verbose_name = "Криптопожертвование"
        verbose_name_plural = "Криптопожертвования"
