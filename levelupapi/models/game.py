from django.db import models


class Game(models.Model):

    game_type            = models.ForeignKey("GameType",
                                            on_delete=models.CASCADE)
    maker               = models.CharField(max_length=255)
    title               = models.CharField(max_length=50)
    description         = models.CharField(max_length=255)
    number_of_players   = models.IntegerField()
    skill_level         = models.IntegerField()
    gamer               = models.ForeignKey("Gamer",
                                            on_delete=models.DO_NOTHING)