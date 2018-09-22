from django.contrib import admin
from django.utils.translation import gettext as _

from denizen.models import Denizen


@admin.register(Denizen)
class DenizenAdmin(admin.ModelAdmin):
    search_fields = ('name', 'source')
    list_filter = ('state', 'election_day', 'second_ring',
                   'home_meetup', 'meetup_guest', 'palrig', 'digital',
                   'call_center', 'field', 'hood')
    list_display = ('name', 'phone', 'state', 'hood')
    fieldsets = (
        (None, {
            'fields': ('name', 'phone', 'email', 'state', 'hood', 'address',
                       'notes', 'edu_foundations')
        }),
        (_('Intrests'), {
            'fields': ('women_rights', 'participation', 'commons', 'education', 'religion'),
        }),
        (_('Volunteering'), {
            'fields': ('election_day', 'second_ring', 'home_meetup',
                       'meetup_guest', 'palrig', 'digital', 'field',
                       'call_center'),
        }),
    )
