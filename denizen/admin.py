from django.contrib import admin
from django.utils.translation import gettext as _

from denizen.models import Denizen


@admin.register(Denizen)
class DenizenAdmin(admin.ModelAdmin):
    list_filter = ('hood', 'state', 'women_rights', 'participation', 'commons',
                   'education', 'religion', 'election_day', 'second_ring',
                   'home_meetup', 'palrig', 'digital')
    list_display = ('name', 'state', 'hood')
    fieldsets = (
        (None, {
            'fields': ('name', 'phone', 'email', 'state', 'hood', 'address', 'zehut')
        }),
        (_('Intrests'), {
            'fields': ('women_rights', 'participation', 'commons', 'education', 'religion'),
        }),
        (_('Volunteering'), {
            'fields': ('election_day', 'second_ring', 'home_meetup', 'palrig', 'digital'),
        }),
    ) 
