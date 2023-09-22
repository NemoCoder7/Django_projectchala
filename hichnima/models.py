from django.db import models


class Comp(models.Model):
    class Os(models.TextChoices):
        WINDOWS = 1, "Windows"
        LINUX = 2, "Linux"
        MACOS = 3, "MacOs"
        MSDOC = 4, "MsDOC"
        __empty__ = "OSni tanlang"

    class Meta:
        verbose_name = "Kompyuter"
        verbose_name_plural = "Kompyuterlar"

    def __str__(self) -> str:
        return f"{self.model}, {self.processor} - {self.id}"

    model = models.CharField(max_length=20, verbose_name="Kompyuter modeli")
    processor = models.CharField(max_length=20, verbose_name="Kompyuter protsessori")
    graphic_card = models.CharField(
        max_length=30, verbose_name="Kompyuter videokartasi"
    )
    ram = models.SmallIntegerField(verbose_name="Operativ xotira")
    rom = models.SmallIntegerField(verbose_name="Doimiy xotira")
    display_diagnal = models.DecimalField(
        verbose_name="Ekran diagnali", max_digits=3, decimal_places=1
    )
    used = models.BooleanField(verbose_name="Yangi", default="True")
    os = models.SmallIntegerField(verbose_name="Operatsion tizim", choices=Os.choices)
