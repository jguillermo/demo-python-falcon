.DEFAULT_GOAL := help

## GENERAL ##
OWNER 			= aptitus
SERVICE_NAME 	= evaluations


## DEPLOY ##
ENV 			?= lab
BUILD_NUMBER 	?= 000006
BUILD_TIMESTAMP ?= 20181004
export DEPLOY_REGION 	?= ap-northeast-1
ACCOUNT_ID		?= 929226109038
DESIRED_COUNT 	?= 1
MIN_SCALING		?= 1
MAX_SCALING		?= 2
HTTPS_PRIORITY 	?= 41
MEMORY_SIZE 	?= 128
CONTAINER_PORT 	?= 80
INFRA_BUCKET 	?= infraestructura.dev
SLACK_CHANNEL   ?= $(OWNER)-dev-changelog

## RESULT_VARS ##
LOCAL_REGISTRY 	= local.$(OWNER).registry:5000
PROJECT_NAME	= $(OWNER)-$(ENV)-$(SERVICE_NAME)
export CONTAINER_NAME 	= $(PROJECT_NAME)_backend
export IMAGE_DEV = $(PROJECT_NAME):dev
IMAGE_CLI		= $(PROJECT_NAME):cli
TAG_DEPLOY		= $(BUILD_TIMESTAMP).$(BUILD_NUMBER)
IMAGE_DEPLOY	= $(PROJECT_NAME):$(TAG_DEPLOY)
CLUSTER 		= $(OWNER)-dev
DEPLOY_REGISTRY = $(ACCOUNT_ID).dkr.ecr.$(DEPLOY_REGION).amazonaws.com
STACK_PATH		= $(INFRA_BUCKET)/build/cloudformation/$(OWNER)/$(ENV)/$(PROJECT_NAME)

export IMAGE_TEST = $(ACCOUNT_ID).dkr.ecr.eu-west-1.amazonaws.com/aptitus-dev-testrestfull-test

## Target Commons ##

build: ## build image to dev: make build
	cp app/requirements.txt docker/dev/resources/requirements.txt
	docker build -f docker/dev/Dockerfile -t $(IMAGE_DEV) docker/dev/
	rm -f docker/dev/resources/requirements.txt

## Target Dev ##

pull: ## pull docker images from local registery: make pull
	docker pull $(LOCAL_REGISTRY)/$(IMAGE_DEV)
	docker tag $(LOCAL_REGISTRY)/$(IMAGE_DEV) $(IMAGE_DEV)
	docker rmi $(LOCAL_REGISTRY)/$(IMAGE_DEV)
	docker pull $(LOCAL_REGISTRY)/$(IMAGE_DEPLOY)
	docker tag $(LOCAL_REGISTRY)/$(IMAGE_DEPLOY) $(IMAGE_DEPLOY)
	docker rmi $(LOCAL_REGISTRY)/$(IMAGE_DEPLOY)

push: ## push docker images to local registry: make push
	docker tag $(IMAGE_DEV) $(LOCAL_REGISTRY)/$(IMAGE_DEV)
	docker push $(LOCAL_REGISTRY)/$(IMAGE_DEV)
	docker rmi $(LOCAL_REGISTRY)/$(IMAGE_DEV)
	docker tag $(IMAGE_DEPLOY) $(LOCAL_REGISTRY)/$(IMAGE_DEPLOY)
	docker push $(LOCAL_REGISTRY)/$(IMAGE_DEPLOY)
	docker rmi $(LOCAL_REGISTRY)/$(IMAGE_DEPLOY)
	docker images

up: ## up docker containers: make up
	docker-compose up -d
	@make status

down: ## Stops and removes the docker containers: make down
	docker-compose down

status: ## Show containers status: make status
	docker-compose ps

stop: ## Stops and removes the docker containers, use me with: make down
	docker-compose stop

restart: ## Restart all containers, use me with: make restart
	docker-compose restart
	@make status

ssh: ## Connect to container for ssh protocol
	docker exec -it $(CONTAINER_NAME) bash

log: ## Show container logs
	docker-compose logs -f

install-lib: ## Connect to container for ssh protocol install with pip: make install-lib
	docker exec -it $(CONTAINER_NAME) pip-3.5 install $(LIB)

tests: ## Run the unitTests
	docker run --rm -t -v $(PWD)/app:/app:rw --entrypoint /resources/test.sh $(IMAGE_DEV)
	sudo chown -R $(USER):$(USER) $(PWD)/app/*

tests-e2e: ## Run the end to end Tests
	docker-compose -f docker-compose.test.yml run --rm test

login-aws-test: ## Run the end to end Tests
	aws ecr get-login --no-include-email --region eu-west-1 | sh

## Migrate ##
migrate: ## Execute migrate
	@if [ ! -z "${local}" ]; then \
		if [ ${local} = "true" ]; then \
			echo "execute local migrations"; \
			docker run --rm -t -v $(PWD)/app:/app:rw \
			--entrypoint /resources/alembic.sh $(IMAGE_DEPLOY) upgrade head; \
		else \
			echo "Please set the 'local' variable. e.g local=true" && exit 1; \
		fi \
	else \
		docker run --rm -t -v $(PWD)/app:/app:rw \
		--entrypoint /resources/alembic.sh $(IMAGE_DEPLOY) upgrade head; \
	fi

revision: ## Create a new revision
	@docker run --rm -t -v $(PWD)/app:/app:rw -v $(PWD)/alembic:/alembic:rw --entrypoint /resources/alembic.sh $(IMAGE_DEPLOY) revision -m "$(DESC)"
	@sudo chown -R $(USER) $(PWD)/app/alembic/versions

downgrade: ## Execute migrate
	@docker run --rm -t -v $(PWD)/app:/app:rw \
			--entrypoint /resources/alembic.sh $(IMAGE_DEPLOY) downgrade base

migrate-id: ## Execute migrate
	@docker run --rm -t -v $(PWD)/alembic:/alembic:rw --entrypoint /resources/alembic.sh $(IMAGE_DEV) upgrade $(ID)


## Target Help ##

help:
	@printf "\033[31m%-16s %-59s %s\033[0m\n" "Target" "Help" "Usage"; \
	printf "\033[31m%-16s %-59s %s\033[0m\n" "------" "----" "-----"; \
	grep -hE '^\S+:.*## .*$$' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' | sort | awk 'BEGIN {FS = ":"}; {printf "\033[32m%-16s\033[0m %-58s \033[34m%s\033[0m\n", $$1, $$2, $$3}'
