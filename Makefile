.DEFAULT_GOAL := help

## GENERAL ##
OWNER 			= aptitus
SERVICE_NAME 	= evaluations
PATH_PREFIX 	= "/v1"

## VARIABLES FOR LOCAL BALANCER, 'SPRING CONFIG OR ENV VARS' ##
VIRTUAL_HOST		= $(PATH_PREFIX)/projects*
DB_HOST				= mysql57
DB_NAME				= db_project_microservice
DB_USER				= root
DB_PASS				= 1234
DB_PORT				= 3307

## DEV ##
TAG_DEV			= dev
TAG_CLI 		= cli

## DEPLOY ##
ENV 			?= dev
BUILD_NUMBER 	?= 000008
BUILD_TIMESTAMP ?= 20181004
export DEPLOY_REGION 	?= eu-west-1
ACCOUNT_ID		?= 929226109038
DESIRED_COUNT 	?= 1
MIN_SCALING		?= 1
MAX_SCALING		?= 2
HTTPS_PRIORITY 	?= 35
MEMORY_SIZE 	?= 128
CONTAINER_PORT 	?= 80
INFRA_BUCKET 	?= infraestructura.dev
SLACK_CHANNEL   ?= aptitus-dev-changelog

## RESULT_VARS ##
LOCAL_REGISTRY 	= local.$(OWNER).registry:5000
DOCKER_NETWORK 	= $(OWNER)_network
PROJECT_NAME	= $(OWNER)-$(ENV)-$(SERVICE_NAME)
export CONTAINER_NAME 	= $(PROJECT_NAME)_backend
export IMAGE_DEV		= $(PROJECT_NAME):$(TAG_DEV)
IMAGE_CLI		= $(PROJECT_NAME):$(TAG_CLI)
TAG_DEPLOY		= $(BUILD_TIMESTAMP).$(BUILD_NUMBER)
IMAGE_DEPLOY	= $(PROJECT_NAME):$(TAG_DEPLOY)
CLUSTER 		= $(OWNER)-dev
DEPLOY_REGISTRY = $(ACCOUNT_ID).dkr.ecr.$(DEPLOY_REGION).amazonaws.com
STACK_PATH		= $(INFRA_BUCKET)/build/cloudformation/$(OWNER)/$(ENV)/$(PROJECT_NAME)


## Target Commons ##

build: ## build image to dev: make build
	cp app/requirements.txt docker/dev/resources/requirements.txt
	docker build -f docker/dev/Dockerfile -t $(IMAGE_DEV) docker/dev/
	rm -f docker/dev/resources/requirements.txt

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
	@docker run --rm -t -v $(PWD)/app:/app:rw --entrypoint /resources/test.sh $(IMAGE_DEV)
	@sudo chown -R $(USER):$(USER) $(PWD)/app/*

tests-e2e: ## Run the end to end Tests
	docker-compose -f docker-compose.test.yml run --rm test

## Migrate ##
migrate: ## Execute migrate
	@if [ ! -z "${local}" ]; then \
		if [ ${local} = "true" ]; then \
			echo "execute local migrations"; \
			docker run --rm -t -v $(PWD)/app:/app:rw --network $(DOCKER_NETWORK) \
			--entrypoint /resources/alembic.sh $(IMAGE_DEPLOY) upgrade head; \
		else \
			echo "Please set the 'local' variable. e.g local=true" && exit 1; \
		fi \
	else \
		docker run --rm -t -v $(PWD)/app:/app:rw \
		--entrypoint /resources/alembic.sh $(IMAGE_DEPLOY) upgrade head; \
	fi

revision: ## Create a new revision
	@docker run --rm -t -v $(PWD)/app:/app:rw -v $(PWD)/alembic:/alembic:rw --network $(DOCKER_NETWORK) --entrypoint /resources/alembic.sh $(IMAGE_DEPLOY) revision -m "$(DESC)"
	@sudo chown -R $(USER) $(PWD)/app/alembic/versions

downgrade: ## Execute migrate
	@docker run --rm -t -v $(PWD)/app:/app:rw --network $(DOCKER_NETWORK) \
			--entrypoint /resources/alembic.sh $(IMAGE_DEPLOY) downgrade base

migrate-id: ## Execute migrate
	@docker run --rm -t -v $(PWD)/alembic:/alembic:rw --network $(DOCKER_NETWORK) --entrypoint /resources/alembic.sh $(IMAGE_DEV) upgrade $(ID)

## Deploy ##

sync-cloudformation: ## Sync additional cloudformation resources in S3: make sync-cloudformation
	aws s3 sync ./cloudformation/stacks s3://$(STACK_PATH)

sync-config: ## Sync configs files from S3: make sync-config
	aws s3 sync s3://$(INFRA_BUCKET)/config/container/$(OWNER)/$(ENV)/$(SERVICE_NAME)/ app/config/

push-config: ## Sync configs files to push: make sync-config
	aws s3 sync app/config/ s3://$(INFRA_BUCKET)/config/container/$(OWNER)/$(ENV)/$(SERVICE_NAME)/

update-service: ## Deploy service with cloudformation: make update-service
	aws cloudformation deploy \
	--template-file ./cloudformation/master.yml \
	--stack-name $(PROJECT_NAME)-service \
	--parameter-overrides \
		S3Path=$(STACK_PATH) \
		HttpsListenerPriority=$(HTTPS_PRIORITY) \
		DesiredCount=$(DESIRED_COUNT) \
		MaxScaling=$(MAX_SCALING) \
		MinScaling=$(MIN_SCALING) \
		Image=$(DEPLOY_REGISTRY)/$(IMAGE_DEPLOY) \
		ServiceName=$(SERVICE_NAME) \
		Env=$(ENV) \
		Owner=$(OWNER) \
		PathPrefix=$(PATH_PREFIX) \
		ContainerPort=$(CONTAINER_PORT) \
		MemorySize=$(MEMORY_SIZE) \
		AwsXrayTracingName=$(AWS_XRAY_TRACING_NAME) \
		SegmentName=$(SEGMENT_NAME) \
		SubSegmentName=$(SUB_SEGMENT_NAME) \
	--region $(DEPLOY_REGION) \
	--capabilities CAPABILITY_NAMED_IAM

create-registry: ## Create registry in aws ECR service: make create-registry
	aws cloudformation deploy \
	--template-file ./cloudformation/registry.yml \
	--stack-name $(PROJECT_NAME)-registry \
	--parameter-overrides \
		ProjectName=$(PROJECT_NAME) \
	--region $(DEPLOY_REGION) \
	--capabilities CAPABILITY_IAM

install: ## Building images dev: make install
	@make build

deploy: ## Exec all step to deploy microservice in aws: make deploy
	@make install build-latest publish update-service

build-latest: ## Build image to push to aws ECR: make build-latest
	docker build -f docker/latest/Dockerfile --no-cache --build-arg IMAGE=$(IMAGE_DEV) -t $(IMAGE_DEPLOY) .

publish: ## Push image to aws ECR: make publish
	docker tag $(IMAGE_DEPLOY) $(DEPLOY_REGISTRY)/$(IMAGE_DEPLOY)
	aws --region $(DEPLOY_REGION) ecr get-login --no-include-email | sh
	docker push $(DEPLOY_REGISTRY)/$(IMAGE_DEPLOY)

chown: ## change the permission for app
	@sudo chown -R $(USER):$(USER) $(PWD)/app/*

slack-notify: ## Send slack notify
	curl -X POST \
	--data-urlencode 'payload={"channel":"$(SLACK_CHANNEL)","username":"Jenkins", "icon_url":"https://wiki.jenkins.io/download/attachments/2916393/logo.png", "attachments":[{"color":"good","title":"$(SLACK_TITLE)", "title_link":"$(SLACK_LINK)", "text":"$(SLACK_TEXT)"}]}' \
	https://hooks.slack.com/services/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

## Target Help ##

help:
	@printf "\033[31m%-16s %-59s %s\033[0m\n" "Target" "Help" "Usage"; \
	printf "\033[31m%-16s %-59s %s\033[0m\n" "------" "----" "-----"; \
	grep -hE '^\S+:.*## .*$$' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' | sort | awk 'BEGIN {FS = ":"}; {printf "\033[32m%-16s\033[0m %-58s \033[34m%s\033[0m\n", $$1, $$2, $$3}'
