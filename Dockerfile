FROM node:8.12

WORKDIR /usr/src/app

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV

#COPY package.json /usr/src/app/
COPY package.docker.json /usr/src/app/package.json
COPY package-lock.docker.json /usr/src/app/package-lock.json

RUN npm install && npm cache clean --force
COPY . /usr/src/app

EXPOSE 8080

CMD [ "npm", "start" ]
