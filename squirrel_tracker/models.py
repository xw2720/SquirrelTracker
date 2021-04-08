from django.db import models
from django.utils.translation import gettext as _



class Meta:
    managed = True

# create squirrel
class Squirrel(models.Model):
    Latitude  = models.FloatField(
        help_text = _('E.g. 40.782091'),
    )

    Longitude = models.FloatField(
        help_text = _('E.g. -73.964285'),
    )

    Unique_squirrel_id = models.CharField(
        max_length = 20,
        primary_key = True,
        default = None,
        help_text = _('E.g. 37F-PM-1014-03')
    )

    PM = 'PM'
    AM = 'AM'
    SHIFT_CHOICES = [
        (PM, _('PM')),
        (AM, _('AM')),
    ]
    Shift = models.CharField(
        max_length = 10,
        choices = SHIFT_CHOICES,
        blank = True,# or default=AM
    )

    Date = models.DateField(
        help_text =_('Date'),
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'


    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
    ]
    Age = models.CharField(
        max_length = 15,
        choices = AGE_CHOICES,
        blank = True,
    )

    GRAY = 'Gray'
    CINNAMON  = 'Cinnamon'
    BLACK = 'Black'
    FURColor_CHOICES = [
        (GRAY, _('Gray')),
        (CINNAMON, _('Cinnamon')),
        (BLACK, _('Black')),
        ]
    Primary_fur_color = models.CharField(
        max_length = 15,
        help_text = _('Select from the list'),
        choices = FURColor_CHOICES,
        blank = True,
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    LOCATION_CHOICES = [
        (GROUND_PLANE, _('Ground Plane')),
        (ABOVE_GROUND, _('Above Ground')),
    ]
    Location = models.CharField(
        max_length = 20,
        choices = LOCATION_CHOICES,
        blank = True,
    )

    Specific_location = models.TextField(
        blank = True,
        help_text=('specific location'),
        max_length=100
    )

    Running = models.BooleanField(
        help_text = _('Is the squirrel running?'),
        #default = False
    )

    Chasing = models.BooleanField(
        help_text = _('Is the squirrel chasing?'),
    )

    Climbing = models.BooleanField(
        help_text = _('Is the squirrel  climbing?'),
    )

    Eating = models.BooleanField(
        help_text = _('Is the squirrel eating?'),
    )

    Foraging = models.BooleanField(
        help_text = _('Is the squirrel foraging?'),
    )

    Other_activities = models.TextField(
        help_text=_('Other Activities'),
        blank = True,
    )

    Kuks = models.BooleanField(
        help_text = _('Kuks'),
    )

    Quaas = models.BooleanField(
        help_text = _('Quaas'),
    )

    Moans = models.BooleanField(
        help_text = _('Moan'),
    )

    Tail_flags = models.BooleanField(
        help_text = _('Tail Flags'),
    )

    Tail_twitches = models.BooleanField(
        help_text = _('Tail Twitches'),
    )

    Approaches = models.BooleanField(
        help_text = _('Approaches'),
    )

    Indifferent = models.BooleanField(
        help_text = _('Indifferent'),
    )

    Runs_from = models.BooleanField(
        help_text = _('Runs From'),
    )

    def __str__(self):
        return self.Unique_squirrel_id