SERVER_NAME   	:= finez_server
DEV_COMPOSE   	:= deployment/docker-compose.dev.yml
PROD_COMPOSE   	:= deployment/docker-compose.prod.yml

dev.up:
	docker-compose -f ${DEV_COMPOSE} build && docker-compose -f ${DEV_COMPOSE} up -d;

dev.down:
	docker-compose -f ${DEV_COMPOSE} down;

prod.up:
	docker-compose -f ${PROD_COMPOSE} build && docker-compose -f ${PROD_COMPOSE} up -d;

prod.down:
	docker-compose -f ${PROD_COMPOSE} down;