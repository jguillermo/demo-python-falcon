# -*- coding: utf-8 -*-


def split_query_string(items):
    params = {'filter': {}, 'fields': [], 'pagination': {}, 'sort': {}}
    for key, value in items:
        subkeys = key.split('.')
        if 'fields' in subkeys:
            params['fields'] = [value] if isinstance(value, str) else value
        elif subkeys[0] in params:
            params[subkeys[0]].update({subkeys[1]: value})

    params['sort'] = ', '.join("{0} {1}".format(key, val.upper()) for (key, val) in params['sort'].items())

    if params['pagination']:
        params['pagination']['page'] = int(params['pagination']['page']) if 'page' in params['pagination'] else 1
        params['pagination']['limit'] = int(params['pagination']['limit']) if 'limit' in params['pagination'] else 100
        params['pagination'].update({'offset': (params['pagination']['page'] * params['pagination']['limit']) - params['pagination']['limit']})

    return params


def join_query_string():
    pass
