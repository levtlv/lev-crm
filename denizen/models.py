from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _

# Create your models here.
STATE_CHOICES = (
    (None, _('new')),
    ('S', _('supporter')),
    ('U', _('undecided')),
    ('H', _('huldai')),
    ('Z', _('zamir')),
    ('A', _('assaf Harel')),
     )

VOLUNTEER_CHOICES = (
    (None, _('no thanks')),
    ('W', _('willing')),
    ('F', _('fullfilled')),
)

HOOD_CHOICES = (
    (None, _('unknown')),
    ('ON', _('Old North')),
)

class Denizen(models.Model):
    name = models.CharField(_("name"), max_length=30)
    fathers_name = models.CharField(
        _("father's name"), max_length=20, null=True, blank=True)

    phone = models.CharField(_("phone"), max_length=30)
    email = models.EmailField(_("email"), null=True, blank=True)
    state = models.CharField(
        _("state"), blank=True, max_length=1, null=True, choices=STATE_CHOICES)
    hood = models.CharField(_("Neighborhood"),
        blank=True, max_length=2, choices = HOOD_CHOICES)
    election_day = models.CharField(_("willing to voounteer on election day"),
        blank=True, max_length=1, choices=VOLUNTEER_CHOICES)
    second_ring = models.CharField(_("willing to be in the second ring"),
                                   blank=True, max_length=1, choices=VOLUNTEER_CHOICES)
    home_meetup = models.CharField(_("willing to host a meetup"),
                                   blank=True, max_length=1, choices=VOLUNTEER_CHOICES)
    palrig = models.CharField(_("willing to hang a palrig"),
                              blank=True,max_length=1, choices=VOLUNTEER_CHOICES)
    digital = models.CharField(_("willing to  digital volounteer"),
                               blank=True,max_length=1, choices=VOLUNTEER_CHOICES)
    women_rights = models.BooleanField(
        _("Interested in women rights"), default=False)
    participation = models.BooleanField(
        _("Interested in civic participation"), default=False)
    commons = models.BooleanField(
        _("Interested in the commons"), default=False)
    education = models.BooleanField(
        _("Interested in education"), default=False)
    religion = models.BooleanField(_("Interested in religion"), default=False)
    address = models.TextField(_("Address"), blank=True, default='')
    notes = models.TextField(_("Notes"), blank=True, default='')
    zehut = models.CharField(_("zehut"), max_length=9, blank=True, null=True)
    birth_year = models.IntegerField(
        _("birth year"), blank=True, null=True, validators=[
            MinValueValidator(1910, _("they can't be more than 108 years old")),
            MaxValueValidator(2000, _("They can't be younger than 18"))])
    ballot = models.CharField(_("ballot name"), blank=True, max_length=30)

    def __str__(self):
        return self.name
