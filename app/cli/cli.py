import click
import os.path
import re


@click.group()
def cli():
    pass


@cli.command()
@click.option('--context', default='project')
@click.option('--resource', default='Project')
def create_resource(context, resource):
    if not resource:
        click.echo("The resource is required")
        exit()

    if not resource[0].isupper():
        click.echo("The first letter must be uppercase")
        exit()

    if not is_camel(resource):
        click.echo(resource)
        click.echo("Must be on 'PascalCase' format")
        exit()

    new_name_resource = create_new_name_resource(resource)

    build_layers_ddd(context, resource, new_name_resource)
    edit_route(context, resource, new_name_resource)
    edit_injector(context, resource, new_name_resource)
    edit_mapping(context, resource, new_name_resource)
    edit_base_test(resource, new_name_resource)
    click.echo('resource created')


@cli.command()
@click.option('--context', default='project')
@click.option('--resource', default='Project')
def delete_resource(context, resource):
    if not resource:
        click.echo("The resource is required")
        exit()

    if not resource[0].isupper():
        click.echo("The first letter must be uppercase")
        exit()

    if not is_camel(resource):
        click.echo(resource)
        click.echo("Must be on 'PascalCase' format")
        exit()

    new_name_resource = create_new_name_resource(resource)

    remove_layer_ddd(context, new_name_resource)
    back_router(context, resource, new_name_resource)
    back_injector(context, resource, new_name_resource)
    back_mapping(context, resource, new_name_resource)
    back_base_test(resource, new_name_resource)
    click.echo('resource removed')


def create_new_name_resource(resource):
    split = re.sub('(?!^)([A-Z][a-z]+)', r' \1', resource).split()
    return '_'.join(split).lower()


def remove_layer_ddd(context, new_name_resource):
    origin_path = '/app/' + context
    origin_paths = get_paths(origin_path)
    for pathKey, path_value in origin_paths.items():
        path_file = path_value + new_name_resource + '.py'
        delete_file(path_file)

        if pathKey == '8':
            path_file = '/app/tests/' + new_name_resource + '.py'
            delete_file(path_file)


def delete_file(path_file):
    if os.path.exists(path_file):
        os.remove(path_file)


def back_router(context, resource, new_name_resource):
    route_path = '/app/bootstrap/routes.yml'

    if not os.path.exists(route_path):
        click.echo(route_path)
        click.echo("route file not exist")
        exit()

    name_route_array = new_name_resource.split('_')
    name_route = '-'.join(name_route_array)

    content_route = read_file(route_path)

    with open(route_path, 'w') as f:
        add_new_route = '  - /'+name_route+': '+context+'.application.framework.handlers.'+new_name_resource+'.'+resource+'CollectionHandler'
        add_new_route_1 = '  - /' + name_route + '/{id}: ' + context + '.application.framework.handlers.' + new_name_resource + '.' + resource + 'Handler'
        file_content_replace_1 = content_route.replace(add_new_route, '')
        file_content_replace = file_content_replace_1.replace(add_new_route_1, '')
        f.write(file_content_replace)


def back_injector(context, resource, new_name_resource):
    injector_path = '/app/bootstrap/container.py'

    if not os.path.exists(injector_path):
        click.echo(injector_path)
        click.echo("route file not exist")
        exit()

    content_route = read_file(injector_path)

    with open(injector_path, 'w') as f:
        text = 'from ' + context + '.application.services.' + new_name_resource + ' import ' + resource + 'AppService\n'
        text += 'from ' + context + '.domain.services.' + new_name_resource + ' import ' + resource + 'DomainService\n'
        text += 'from ' + context + '.infrastructure.repository.sqlalchemy.' + new_name_resource + ' import ' + resource + 'SqlAlchemyRepository\n'
        text += 'from ' + context + '.infrastructure.repository.mockup.' + new_name_resource + ' import Mock' + resource + 'Repository\n'
        file_content_replace_1 = content_route.replace(text, '')

        text = '    ' + new_name_resource + ' = providers.Singleton(' + resource + 'SqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)\n'
        file_content_replace_2 = file_content_replace_1.replace(text, '')

        text = '    ' + new_name_resource + ' = providers.Singleton(' + resource + 'DomainService, repository=RepositoryInjector.' + new_name_resource + ')\n'
        file_content_replace_3 = file_content_replace_2.replace(text, '')

        text = '    ' + new_name_resource + ' = providers.Singleton(' + resource + 'AppService, domain_service=DomainServicesInjector.' + new_name_resource + ')\n'
        file_content_replace_4 = file_content_replace_3.replace(text, '')

        text = '    ' + new_name_resource + ' = providers.Factory(Mock' + resource + 'Repository)\n'
        file_content_replace_5 = file_content_replace_4.replace(text, '')

        text = '    ' + new_name_resource + ' = providers.Factory(' + resource + 'DomainService, repository=MockRepositoryInjector.' + new_name_resource + ')\n'
        file_content_replace_6 = file_content_replace_5.replace(text, '')

        text = '    ' + new_name_resource + ' = providers.Singleton(' + resource + 'AppService, domain_service=MockDomainServicesInjector.' + new_name_resource + ')\n'
        file_content_replace = file_content_replace_6.replace(text, '')

        f.write(file_content_replace)


def back_mapping(context, resource, new_name_resource):
    mapping_path = '/app/' + context + '/infrastructure/repository/sqlalchemy/mapping.py'

    if not os.path.exists(mapping_path):
        click.echo(mapping_path)
        click.echo("route file not exist")
        exit()

    content_mapping = read_file(mapping_path)

    with open(mapping_path, 'w') as f:
        text = 'from ' + context + '.domain.entities.' + resource.lower() + ' import ' + resource + '\n'
        file_content_replace_1 = content_mapping.replace(text, '')

        text = new_name_resource + " = Table('" + resource.lower() + "', metadata,\n"
        text += "                Column('id', Integer, primary_key=True, nullable=False),\n"
        text += "                Column('name', String(255)),\n"
        text += "                )\n"
        file_content_replace_2 = file_content_replace_1.replace(text, '')

        text = '    mapper(' + resource + ', ' + new_name_resource + ')\n'
        file_content_replace = file_content_replace_2.replace(text, '')

        f.write(file_content_replace)


def back_base_test(resource, new_name_resource):
    base_test_path = '/app/tests/suite_test.py'

    if not os.path.exists(base_test_path):
        click.echo(base_test_path)
        click.echo("route file not exist")
        exit()

    content_route = read_file(base_test_path)

    with open(base_test_path, 'w') as f:
        text = 'from tests.' + new_name_resource + ' import ' + resource + 'TestCase\n'
        file_content_replace_1 = content_route.replace(text, '')

        text = '    suite.addTest(loader.loadTestsFromModule(' + resource + 'TestCase))\n'
        file_content_replace = file_content_replace_1.replace(text, '')

        f.write(file_content_replace)


def build_layers_ddd(context, resource, new_name_resource):
    origin_path = '/app/cli/template'

    origin_paths = get_paths(origin_path)
    destination_path = '/app/' + context
    destination_paths = get_paths(destination_path)

    for keyPath, valuePath in origin_paths.items():
        path_example = valuePath + 'example.py'
        if not os.path.exists(path_example):
            click.echo(path_example)
            click.echo("file not exist")
            exit()

        content = read_file(path_example)

        if keyPath == '9':
            destination_paths[keyPath] = '/app/tests/'

        path_destination = destination_paths[keyPath] + new_name_resource + '.py'
        path_destination_validate = destination_paths[keyPath]
        if not os.path.exists(path_destination_validate):
            click.echo(path_destination_validate)
            click.echo("the route destination not exist")
            exit()

        with open(path_destination, 'w+') as f:
            file_content = content.replace('Example', resource)
            file_content_replace = file_content.replace('context', context)
            final_file_content = file_content_replace.replace('example', new_name_resource)
            f.write(final_file_content)
        os.chmod(path_destination, 0o777)


def is_camel(s):
    return s != s.lower() and s != s.upper()


def edit_route(context, resource, new_name_resource):
    route_path = '/app/bootstrap/routes.yml'

    if not os.path.exists(route_path):
        click.echo(route_path)
        click.echo("route file not exist")
        exit()

    name_route_array = new_name_resource.split('_')
    name_route = '-'.join(name_route_array)

    content_route = read_file(route_path)

    with open(route_path, 'w') as f:
        add_new_route = '  - /'+name_route+': '+context+'.application.framework.handlers.'+new_name_resource+'.'+resource+'CollectionHandler'
        add_new_route_1 = '  - /' + name_route + '/{id}: ' + context + '.application.framework.handlers.' + new_name_resource + '.' + resource + 'Handler'
        final_content = content_route+'\n'+add_new_route+'\n'+add_new_route_1
        f.write(final_content)


def edit_injector(context, resource, new_name_resource):
    injector_path = '/app/bootstrap/container.py'

    if not os.path.exists(injector_path):
        click.echo(injector_path)
        click.echo("route file not exist")
        exit()

    with open(injector_path, 'r') as f:
        content_injector = f.readlines()

    content_route_list = list(content_injector)

    for key, lines in enumerate(content_injector, start=0):

        if 'class ConfigInjector' in lines:
            text = 'from ' + context + '.application.services.' + new_name_resource + ' import ' + resource + 'AppService\n'
            text += 'from ' + context + '.domain.services.' + new_name_resource + ' import ' + resource + 'DomainService\n'
            text += 'from ' + context + '.infrastructure.repository.sqlalchemy.' + new_name_resource + ' import ' + resource + 'SqlAlchemyRepository\n'
            text += 'from ' + context + '.infrastructure.repository.mockup.' + new_name_resource + ' import Mock' + resource + 'Repository\n'
            content_route_list.insert(key - 1, text)

        if 'class RepositoryInjector' in lines:
            text = '    ' + new_name_resource + ' = providers.Singleton(' + resource + 'SqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)\n'
            content_route_list.insert(key + 2, text)

        if 'class DomainServicesInjector' in lines:
            text = '    ' + new_name_resource + ' = providers.Singleton(' + resource + 'DomainService, repository=RepositoryInjector.' + new_name_resource + ')\n'
            content_route_list.insert(key + 3, text)

        if 'class AppServicesInjector' in lines:
            text = '    ' + new_name_resource + ' = providers.Singleton(' + resource + 'AppService, domain_service=DomainServicesInjector.' + new_name_resource + ')\n'
            content_route_list.insert(key + 4, text)

        if 'class MockRepositoryInjector' in lines:
            text = '    ' + new_name_resource + ' = providers.Factory(Mock' + resource + 'Repository)\n'
            content_route_list.insert(key + 5, text)

        if 'class MockDomainServicesInjector' in lines:
            text = '    ' + new_name_resource + ' = providers.Factory(' + resource + 'DomainService, repository=MockRepositoryInjector.' + new_name_resource + ')\n'
            content_route_list.insert(key + 6, text)

        if 'class MockAppServicesInjector' in lines:
            text = '    ' + new_name_resource + ' = providers.Singleton(' + resource + 'AppService, domain_service=MockDomainServicesInjector.' + new_name_resource + ')\n'
            content_route_list.insert(key + 7, text)

    content_final = ''

    for key, lines in enumerate(content_route_list, start=0):
        content_final += lines

    with open(injector_path, 'w') as f:
        f.write(content_final)


def edit_mapping(context, resource, new_name_resource):
    mapping_path = '/app/' + context + '/infrastructure/repository/sqlalchemy/mapping.py'

    if not os.path.exists(mapping_path):
        click.echo(mapping_path)
        click.echo("route file not exist")
        exit()

    with open(mapping_path, 'r') as f:
        content_mapping = f.readlines()

    content_mapping_list = list(content_mapping)

    for key, lines in enumerate(content_mapping, start=0):

        if 'metadata = MetaData' in lines:
            text = 'from '+context+'.domain.entities.'+resource.lower()+' import '+resource+'\n'
            content_mapping_list.insert(key - 1, text)

        if 'def load_mapper' in lines:
            text = new_name_resource + " = Table('"+resource.lower()+"', metadata,\n"
            text += "                Column('id', Integer, primary_key=True, nullable=False),\n"
            text += "                Column('name', String(255)),\n"
            text += "                )\n"
            content_mapping_list.insert(key, text)

        if 'clear_mappers()' in lines:
            text = '    mapper('+resource+', '+new_name_resource+')\n'
            content_mapping_list.insert(key + 3, text)

    content_final = ''

    for key, lines in enumerate(content_mapping_list, start=0):
        content_final += lines

    with open(mapping_path, 'w') as f:
        f.write(content_final)


def edit_base_test(resource, new_name_resource):
    base_test_path = '/app/tests/suite_test.py'

    if not os.path.exists(base_test_path):
        click.echo(base_test_path)
        click.echo("route file not exist")
        exit()

    with open(base_test_path, 'r') as f:
        content_base_test = f.readlines()

    content_base_test_list = list(content_base_test)

    for key, lines in enumerate(content_base_test, start=0):

        if 'def suite' in lines:
            text = 'from tests.'+new_name_resource+' import '+resource+'TestCase\n'
            content_base_test_list.insert(key - 1, text)

        if 'return suite' in lines:
            text = '    suite.addTest(loader.loadTestsFromModule('+resource+'TestCase))\n'
            content_base_test_list.insert(key - 1, text)

    content_final = ''

    for key, lines in enumerate(content_base_test_list, start=0):
        content_final += lines

    with open(base_test_path, 'w') as f:
        f.write(content_final)


def get_paths(base_path):
    path_collection = {
        '0': base_path + '/application/framework/handlers/',
        '1': base_path + '/application/services/',
        '2': base_path + '/domain/services/',
        '3': base_path + '/domain/repository/',
        '4': base_path + '/domain/entities/',
        '5': base_path + '/domain/factories/entities/',
        '6': base_path + '/domain/valueObjects/',
        '7': base_path + '/infrastructure/repository/sqlalchemy/',
        '8': base_path + '/infrastructure/repository/mockup/',
        '9': base_path + '/tests/'
    }
    return path_collection


def read_file(path):
    with open(path, 'r') as f:
        content = f.read()
    return content


if __name__ == '__main__':
    cli()
