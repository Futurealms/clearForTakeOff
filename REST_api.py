from eve import Eve
from machine import more_than


# def before_insert(resource_name, documents):
#     if resource_name == 'request':
#         for document in documents:
#             print(document)
#             document['more_than_one_hour'] = more_than(1)
#             document['more_than_two_hours'] = more_than(2)

def before_get(resource_name, response):
    print(response)
    if resource_name == 'request':
        response['_items']=[{'more_than_one_hour': more_than(1), 'more_than_two_hours': more_than(2)}]


app = Eve(settings='settings.py')
# app.on_insert += before_insert
app.on_fetched_resource += before_get
app.run(debug=True)
