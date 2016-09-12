from django.db import models


class PostQuerySet(models.QuerySet):

    def released(self):
        return self.filter(released=True)

    def not_released(self):
        return self.filter(released=False)
