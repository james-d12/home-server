#!make

include .env

start:
	sudo docker-compose --env-file ./.env up -d
	sudo chown -R user: ${APP_DIR}
	sudo chmod -R u+x ${APP_DIR}
stop: 
	sudo docker-compose down

clean:
	rm -rf ${APP_DIR}