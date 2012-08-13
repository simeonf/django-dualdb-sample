from chinook.models import *
from django.contrib import admin


class TrackInline(admin.TabularInline):
    model = PlaylistTrack

class PlaylistAdmin(admin.ModelAdmin):
    inlines = (TrackInline, )

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Genre)
admin.site.register(Invoice)
admin.site.register(Invoiceline)
admin.site.register(Mediatype)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Track)


