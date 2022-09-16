#!make

include .env

copy-config:
	cp -R ./config/* ${APP_DIR}/

start:
	sudo docker-compose --env-file ./.env up -d
	sudo chown -R user: ${APP_DIR}
	sudo chmod -R u+x ${APP_DIR}
stop: 
	sudo docker-compose down
restart:
	sudo docker-compose restart
log:
	sudo docker-compose logs $(app)
list:
	sudo docker container ls
clean:
	rm -rf ${APP_DIR}