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
