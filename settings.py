request_schema = {'from': {'type': 'string',
                           'minlength': 3,
                           'maxlength': 3},
                  'to': {'type': 'string',
                         'minlength': 3,
                         'maxlength': 3},
                  'day_time': {'type': 'datetime'},
                  'more_than_one_hour': {'type': 'float'},
                  'more_than_two_hours': {'type': 'float'}
               }


DOMAIN = {
    'weather': {},
    'delays': {},
    'request': {'resource_methods': ['GET', 'POST'], 'schema': request_schema}
}


RESOURCE_METHODS = ['GET', 'DELETE']
ITEM_METHODS = ['GET', 'PUT', 'DELETE']

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'nodelay'
