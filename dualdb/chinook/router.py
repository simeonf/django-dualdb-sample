"""See https://docs.djangoproject.com/en/dev/topics/db/multi-db/#using-routers 
for details on db routers."""

class ChinookRouter(object): 
    """
    chinook/models.py => chinookdb, others => default
    """
    def db_for_read(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'chinook':
            return 'chinookdb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'chinook':
            return 'chinookdb'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in chinook app"
        if obj1._meta.app_label == 'chinook' and obj2._meta.app_label == 'chinook':
            return True
        # Allow if neither is chinook app
        elif 'chinook' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'chinookdb' or model._meta.app_label == "chinook":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True
