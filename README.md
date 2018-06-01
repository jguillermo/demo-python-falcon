MicroService Evaluations
-----------------

## Quick Configuration

#### Installing the AWS Command Line Interface

~~~~
pip install --upgrade pip
pip install awscli --upgrade --user
~~~~

#### Log in to Amazon ECR registry

~~~~
make login
~~~~

Enter your AWS account credentials

~~~~
AWS Access Key ID: EnterYourAccessKeyID
AWS Secret Access Key: EnterYoutSecretAccessKey
~~~~

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
https://services.aptitus.com/v1/evaluations/
~~~~

UnitTest:

~~~~
$ make test_project
~~~~

for more command:

~~~~
$ make
~~~~
