FROM nginx:1.15-alpine

RUN mkdir -p /home/nginx/vue

WORKDIR /home/nginx/vue

COPY ./conf.d/default.conf /etc/nginx/conf.d/
COPY ./html/dist /home/nginx/vue

EXPOSE 8082