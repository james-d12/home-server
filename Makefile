#!make

include .env

start:
	sudo docker compose --env-file ./.env up -d
	sudo chown -R user: ${APP_DIR}
	sudo chmod -R u+x ${APP_DIR}
	cp -R ./config/* ${APP_DIR}
stop: 
	sudo docker compose down
restart:
	sudo docker compose restart
log:
	sudo docker compose logs $(app)
list:
	sudo docker container ls
list-network:
	sudo docker network ls
clean:
	sudo docker compose down --remove-orphans
	sudo docker image prune --all
	rm -rf ${APP_DIR}
