IMAGE_BASE_NAME=space_inc
IMAGE_DEPENDENCIES=poetry.lock Dockerfile
ENVIRONMENT_HASH=$$(shasum -a 256 ${IMAGE_DEPENDENCIES} | shasum -a 256 | cut -c1-8)
MNT_PATH ?= ${PWD}

dev-build:
	@docker build . --target dev-image -t ${IMAGE_BASE_NAME}_dev:${ENVIRONMENT_HASH}

prod-build:
	@docker build . --target production-image -t ${IMAGE_BASE_NAME}:${ENVIRONMENT_HASH}

server: prod-build
	@TAG=${ENVIRONMENT_HASH} \
	IMAGE_NAME=${IMAGE_BASE_NAME} \
	docker-compose up -d

down:
	@docker-compose down

test: dev-build
	@docker run -it -v ${MNT_PATH}/app:/code/app -v ${MNT_PATH}/tests:/code/tests ${IMAGE_BASE_NAME}_dev:${ENVIRONMENT_HASH} pytest
