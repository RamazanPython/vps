from django.db import models

from utils.consts import VpsStatusChoices
from utils.models import AbstractTimeTrackable, AbstractUuid


class Vps(AbstractTimeTrackable, AbstractUuid):
    cpu = models.PositiveIntegerField(
        verbose_name='Количество ядер'
    )
    ram = models.PositiveIntegerField(
        verbose_name='Объем RAM'
    )
    hdd = models.PositiveIntegerField(
        verbose_name='Объем HDD'
    )
    status = models.CharField(
        choices=VpsStatusChoices.choices(),
        max_length=17,
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Виртуальный выделенный сервер'
        verbose_name_plural = 'Виртуальные выделенные сервера'

    def __str__(self) -> str:
        return f'VPS {self.uid}'
