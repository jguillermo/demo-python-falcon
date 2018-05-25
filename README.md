MicroService Project
-----------------

Commands:

~~~~
$ make build
$ make up
~~~~

Run migrations:

execute all migrations

~~~~
$ make migrate local=true
~~~~

Create revisions:

~~~~
$ make revision DESC="add status column"
~~~~

Resource

~~~~
http://local.services.urbania.pe/v2/projects/
~~~~

UnitTest:

~~~~
$ make test_project
~~~~

for more command:

~~~~
$ make
~~~~
