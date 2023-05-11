from django.db import models
from django.utils.translation import gettext_lazy as _


class Afinidad(models.TextChoices):
    A = "A", _("Aire")
    T = "F", _("Fuego")
    M = "M", _("Montaña")
    B = "B", _("Bosque")
    N = "N", _("Neutro")


class Jugador(models.Model):
    #ver en el admin los nombres
    def __str__(self):
        return self.nombre

    class Sexo(models.TextChoices):
        V = "V", _("Macho")
        M = "M", _("Hembra")
        N = "N", _("Neutro")

    nombre = models.CharField(max_length=100)
    desc = models.CharField(max_length=100, null=True, blank=True)
    sprite = models.CharField(max_length=250)
    sexo= models.CharField(max_length=1, choices=Sexo.choices)
    afinidad = models.CharField(max_length=1, choices=Afinidad.choices)



class Temporada(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.CharField(max_length=250)


class Club(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.CharField(max_length=250)


class Objeto(models.Model):
    def __str__(self):
        return self.nombre

    class Tipo(models.TextChoices):
        H = "H", _("Objetos historia")
        F = "F", _("Objetos para fichar")
        C = "C", _("Objetos curativos")
        S = "S", _("Supertecnicas")
        E = "E", _("Equipables")

    nombre = models.CharField(max_length=100)
    sprite = models.CharField(max_length=250)
    desc = models.CharField(max_length=100, null=True, blank=True)
    obtencion = models.CharField(max_length=250)
    tipo = models.CharField(max_length=1, choices=Tipo.choices)


class Stat(models.Model):
    class Nombre(models.TextChoices):
        PE = "PE", _("Puntos de Energia")
        PT = "PT", _("Puntos de tecnica")
        T = "T", _("Tiro")
        F = "F", _("Fisico")
        C = "C", _("Control")
        D = "D", _("Defensa")
        R = "R", _("Rapidez")
        A = "A", _("Aguante")
        V = "V", _("Valor")
        S = "S", _("Suerte")
        L = "L", _("Libertad")

    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=2, choices=Nombre.choices)
    valor = models.IntegerField()


class Supertecnica(models.Model):

    def __str__(self):
        return self.nombre, self.afinidad, self.tipo

    class Tipo(models.TextChoices):
        B = "B", _("Bloqueo")
        T = "T", _("Tiro")
        R = "R", _("Regate")
        A = "A", _("Atajo")

    nombre = models.CharField(max_length=50)
    afinidad = models.CharField(max_length=1, choices=Afinidad.choices)
    tipo = models.CharField(max_length=1, choices=Tipo.choices)


class JugadorClubTemporada(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)


class JugadorSupertecnica(models.Model):

    #def __str__(self):
     #   return self.jugador, self.supertecnica

    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    supertecnica = models.ForeignKey(Supertecnica, on_delete=models.CASCADE)

