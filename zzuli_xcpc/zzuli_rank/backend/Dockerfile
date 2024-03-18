FROM node:16

RUN mkdir -p /home/nodejs/backend

WORKDIR /home/nodejs/backend

COPY package.json .

COPY api.js .

RUN npm config set registry https://registry.npmmirror.com

RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "api.js"]