# The following is created by running:
# $ python manage.py inspectdb --database=chinookdb > chinook/models.py

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Album(models.Model):
    id = models.AutoField(primary_key=True, db_column=u'AlbumId') # Field name made lowercase.
    title = models.CharField(db_column=u'Title', max_length=160)
    artist = models.ForeignKey("Artist", db_column=u'ArtistId') # Field name made lowercase.

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = u'Album'



class Artist(models.Model):
    id = models.AutoField(primary_key=True, db_column=u'ArtistId') # Field name made lowercase.
    name = models.CharField(db_column=u'Name', blank=True, max_length=120)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'Artist'

class Customer(models.Model):
    id = models.AutoField(primary_key=True, db_column=u'CustomerId') # Field name made lowercase.
    firstname = models.CharField(max_length=40, db_column=u'FirstName')
    lastname = models.CharField(max_length=20, db_column=u'LastName')
    company = models.CharField(max_length=80, db_column=u'Company', blank=True)
    address = models.CharField(max_length=70, db_column=u'Address', blank=True)
    city = models.CharField(max_length=40, db_column=u'City', blank=True)
    state = models.CharField(max_length=40, db_column=u'State', blank=True)
    country = models.CharField(max_length=40, db_column=u'Country', blank=True)
    postalcode = models.CharField(max_length=10, db_column=u'PostalCode', blank=True)
    phone = models.CharField(max_length=24, db_column=u'Phone', blank=True)
    fax = models.CharField(max_length=24, db_column=u'Fax', blank=True)
    email = models.CharField(max_length=60, db_column=u'Email')
    support_rep = models.ForeignKey("Employee", null=True, db_column=u'SupportRepId', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Customer'

    def __unicode__(self):
        return u"%s, %s" % (self.lastname, self.firstname)


class Employee(models.Model):
    id = models.AutoField(primary_key=True, db_column=u'EmployeeId') # Field name made lowercase.
    lastname = models.CharField(max_length=20, db_column=u'LastName')
    firstname = models.CharField(max_length=20, db_column=u'FirstName')
    title = models.CharField(max_length=30, db_column=u'Title', blank=True)
    reports_to = models.ForeignKey("Employee", null=True, db_column=u'ReportsTo', blank=True)
    birthdate = models.DateTimeField(null=True, db_column=u'BirthDate', blank=True)
    hiredate = models.DateTimeField(null=True, db_column=u'HireDate', blank=True)
    address = models.CharField(max_length=70, db_column=u'Address', blank=True)
    city = models.CharField(max_length=40, db_column=u'City', blank=True)
    state = models.CharField(max_length=40, db_column=u'State', blank=True)
    country = models.CharField(max_length=40, db_column=u'Country', blank=True)
    postalcode = models.CharField(max_length=10, db_column=u'PostalCode', blank=True)
    phone = models.CharField(max_length=24, db_column=u'Phone', blank=True)
    fax = models.CharField(max_length=24, db_column=u'Fax', blank=True)
    email = models.CharField(max_length=60, db_column=u'Email', blank=True)
    class Meta:
        db_table = u'Employee'

    def __unicode__(self):
        return u"%s, %s" % (self.lastname, self.firstname)

class Genre(models.Model):
    id = models.AutoField(primary_key=True, db_column=u'GenreId')
    name = models.CharField(max_length=120, db_column=u'Name', blank=True)

    class Meta:
        db_table = u'Genre'

    def __unicode__(self):
        return u"%s" % self.name

class Invoice(models.Model):
    id = models.AutoField(primary_key=True, db_column=u'InvoiceId')
    customer = models.ForeignKey("Customer", db_column=u'CustomerId')
    invoicedate = models.DateTimeField(db_column=u'InvoiceDate')
    billingaddress = models.CharField(max_length=70, db_column=u'BillingAddress', blank=True)
    billingcity = models.CharField(max_length=40, db_column=u'BillingCity', blank=True)
    billingstate = models.CharField(max_length=40, db_column=u'BillingState', blank=True)
    billingcountry = models.CharField(max_length=40, db_column=u'BillingCountry', blank=True)
    billingpostalcode = models.CharField(max_length=10, db_column=u'BillingPostalCode', blank=True)
    total = models.TextField(db_column=u'Total')

    def __unicode__(self):
        return u"%s: %s" % (self.id, self.customer)

    class Meta:
        db_table = u'Invoice'

class Invoiceline(models.Model):
    id = models.AutoField(primary_key=True, db_column=u'InvoiceLineId')
    invoice = models.ForeignKey("Invoice", db_column=u'InvoiceId')
    track = models.ForeignKey("Track", db_column=u'TrackId')
    unit_price = models.DecimalField(max_digits=5, db_column=u'UnitPrice', decimal_places=2)
    quantity = models.IntegerField(db_column=u'Quantity')
    class Meta:
        db_table = u'InvoiceLine'

    def __unicode__(self):
        return u"%s/%s/%s" % (self.track, self.invoice, self.unit_price)

class Mediatype(models.Model):
    id = models.AutoField(primary_key=True, db_column=u'MediaTypeId')
    name = models.CharField(max_length=120, db_column=u'Name', blank=True)
    class Meta:
        db_table = u'MediaType'

    def __unicode__(self):
        return u"%s" % self.name

class Playlist(models.Model):
    id = models.AutoField(primary_key=True, db_column=u'PlaylistId')
    name = models.CharField(max_length=120, db_column=u'Name', blank=True)
    class Meta:
        db_table = u'Playlist'

    def __unicode__(self):
        return u"%s" % self.name


class PlaylistTrack(models.Model):
    playlist = models.ForeignKey("Playlist", db_column=u'PlaylistId')
    track = models.ForeignKey("Track", db_column=u'TrackId')
    class Meta:
        db_table = u'PlaylistTrack'
        unique_together = ('playlist', 'track')

    def __unicode__(self):
        return u"Playlist %s: %s" % (self.playlist, self.track)


class Track(models.Model):
    id = models.AutoField(primary_key=True, db_column=u'TrackId')
    playlist = models.ManyToManyField(Playlist, through=PlaylistTrack)
    name = models.CharField(max_length=200, db_column=u'Name')
    album = models.ForeignKey("Album", null=True, db_column=u'AlbumId', blank=True)
    mediatype = models.ForeignKey("MediaType", db_column=u'MediaTypeId')
    genre = models.ForeignKey("Genre", null=True, db_column=u'GenreId', blank=True)
    composer = models.CharField(max_length=220, db_column=u'Composer', blank=True)
    milliseconds = models.IntegerField(db_column=u'Milliseconds')
    bytes = models.IntegerField(null=True, db_column=u'Bytes', blank=True)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2, db_column=u'UnitPrice')

    class Meta:
        db_table = u'Track'

    def __unicode__(self):
        return u"%s" % self.name
