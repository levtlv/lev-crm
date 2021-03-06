from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _

# Create your models here.
STATE_CHOICES = (
    ('N', _('new')),
    ('!', _('for zippi')),
    ('P', _('in progress')),
    ('W', _('walk in')),
    ('S', _('supporter')),
    ('U', _('undecided')),
    ('H', _('huldai')),
    ('Z', _('zamir')),
    ('A', _('assaf Harel')),
    ('O', _('other')),
     )

VOLUNTEER_CHOICES = (
    (None, _('unknown')),
    ('N', _('no thanks')),
    ('W', _('willing')),
    ('F', _('fullfilled')),
)

HOOD_CHOICES = (
    ('בבלי צמרות איילון והצפון החדש', 'בבלי צמרות איילון והצפון החדש'),
    ('הכרם ונווה צדק', 'הכרם ונווה צדק'),
    ('הצפון הישן (צפוני ודרומי)', 'הצפון הישן (צפוני ודרומי)'),
    ('התקווה ודרום מזרח העיר', 'התקווה ודרום מזרח העיר'),
    ('יד אליהו','יד אליהו'),
    ('יפו','יפו'),
    ('לב העיר', 'לב העיר'),
    ('מעוז אביב והדר יוסף','מעוז אביב והדר יוסף'),
    ("נאות אפקה א' ו-ב'", "נאות אפקה א' ו-ב'"),
    ('נווה אביבים וסביבתה ורמת אביב','נווה אביבים וסביבתה ורמת אביב'),
    ('נחלת יצחק בצרון ורמת ישראל','נחלת יצחק בצרון ורמת ישראל'),
    ("עג'מי וגבעת עלייה","עג'מי וגבעת עלייה"),
    ('פלורנטין ונווה שאנן','פלורנטין ונווה שאנן'),
    ('צהלה והמשתלה', 'צהלה והמשתלה'),
    ('צפון חדש - כיכר המדינה והדרומי', 'צפון חדש - כיכר המדינה והדרומי'),
    ('צפון יפו', 'צפון יפו'),
    ('צפון מערביות', 'צפון מערביות'),
    ('רביבים שיכון דן ונווה דן', 'רביבים שיכון דן ונווה דן'),
    ("רמת אביב ג' ואפקה", "רמת אביב ג' ואפקה"),
    ('רמת החייל ונווה שרת', 'רמת החייל ונווה שרת'),
    ('שפירא קרית שלום וסביבתה', 'שפירא קרית שלום וסביבתה'),
    ('תל ברוך ותל ברוך צפון', 'תל ברוך ותל ברוך צפון'),
)

class Denizen(models.Model):
    name = models.CharField(_("name"), max_length=30)
    fathers_name = models.CharField(
        _("father's name"), max_length=20, null=True, blank=True)

    phone = models.CharField(_("phone"), max_length=30)
    edu_foundations = models.CharField(
        _("Education Foundations"), max_length=60, default='', blank=True)
    email = models.EmailField(_("email"), null=True, blank=True)
    state = models.CharField(
        _("state"), blank=True, max_length=1, null=True, choices=STATE_CHOICES,
        default='N')
    hood = models.CharField(_("Neighborhood"),
        blank=True, max_length=32, choices=HOOD_CHOICES)
    election_day = models.CharField(_("willing to voounteer on election day"),
        blank=True, max_length=1, choices=VOLUNTEER_CHOICES)
    second_ring = models.CharField(_("willing to be in the second ring"),
                                   blank=True, max_length=1, choices=VOLUNTEER_CHOICES)
    home_meetup = models.CharField(_("willing to host a meetup"),
                                   blank=True, max_length=1, choices=VOLUNTEER_CHOICES)
    palrig = models.CharField(_("willing to hang a palrig"),
                              blank=True, max_length=1, choices=VOLUNTEER_CHOICES)
    call_center = models.CharField(_("willing to be a call center volounteer"),
                               blank=True, max_length=1, choices=VOLUNTEER_CHOICES)
    field = models.CharField(_("willing to be a volounteer in the field"),
                               blank=True, max_length=1, choices=VOLUNTEER_CHOICES)
    digital = models.CharField(_("willing to  digital volounteer"),
                               blank=True, max_length=1, choices=VOLUNTEER_CHOICES)
    meetup_guest = models.CharField(_("want to be a guest in a meetup"),
                               blank=True, max_length=1, choices=VOLUNTEER_CHOICES)
    women_rights = models.BooleanField(
        _("Interested in women rights"), default=False)
    participation = models.BooleanField(
        _("Interested in civic participation"), default=False)
    commons = models.BooleanField(
        _("Interested in the commons"), default=False)
    education = models.BooleanField(
        _("Interested in education"), default=False)
    religion = models.BooleanField(_("Interested in religion"), default=False)
    address = models.CharField(_("Address"), max_length=40, blank=True, default='')
    notes = models.TextField(_("Notes"), blank=True, default='')
    zehut = models.CharField(_("zehut"), max_length=9, blank=True, null=True)
    birth_year = models.IntegerField(
        _("birth year"), blank=True, null=True, validators=[
            MinValueValidator(1910, _("they can't be more than 108 years old")),
            MaxValueValidator(2000, _("They can't be younger than 18"))])
    ballot = models.CharField(_("ballot name"), blank=True, max_length=30)
    source = models.CharField(_("Source"), max_length=20)
    whatever = models.CharField(_("Whatever"), max_length=60, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Denizen")
        verbose_name_plural = _("Denizens")

    def save(self):
        #TODO: DRY !!!
        if self.election_day.lower() == 'x':
            self.election_day = 'W'
        if self.second_ring.lower() == 'x':
            self.second_ring = 'W'
        if self.home_meetup.lower() == 'x':
            self.home_meetup = 'W'
        if self.palrig.lower() == 'x':
            self.palrig = 'W'
        if self.digital.lower() == 'x':
            self.digital = 'W'
        if self.election_day.lower() == 'x':
            self.election_day = 'W'
        if self.election_day.lower() == 'x':
            self.election_day = 'W'
        if self.field.lower() == 'x':
            self.field = 'W'
        if self.meetup_guest.lower() == 'x':
            self.meetup_guest = 'W'
        super().save()

    def __str__(self):
        return self.name
