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
        "Allow any relation if a model in chinook is involved"
        return True
        if obj1._meta.app_label == 'chinook' or obj2._meta.app_label == 'chinook':
            return True
        return None
    
    def allow_syncdb(self, db, model):
        "This has nothing to do with the syncdb command!"""
        if db == 'chinookdb':
            # models in chinook save to chinookdb
            return model._meta.app_label == 'chinook' 
        elif model._meta.app_label == 'chinook':
            # models in chinook do not save to default
            return False
        else: # but all other models can save to default
            return True
