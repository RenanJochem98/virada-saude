# Parametro que deve ser informado no docker build (--build-arg URL_API=https://exemplo)
# ARGs duram apenas durante a compilacao de um estagio, deve ser renovado a cada "FROM"
# ARG URL_API

# develop stage
FROM node:17-alpine3.14 as develop-stage
# ARG URL_API
WORKDIR /app
COPY package*.json ./
RUN npm install -g @quasar/cli@1.2.2
COPY . .
# Para rodar em desenv, descomentar esse comando
#CMD ["URL_API_ENVIROMENT=http://localhost:8000", "quasar", "dev", "-m", "pwa"]

# Os estágios abaixo são desnecessários para desenv

# build stage
FROM develop-stage as build-stage
# ARG URL_API
RUN npm install
RUN quasar build -m pwa
#RUN quasar build

# production stage
FROM nginx:1.17.5-alpine as production-stage
COPY --from=build-stage /app/dist/pwa /usr/share/nginx/html
COPY nginx.conf /etc/nginx/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]