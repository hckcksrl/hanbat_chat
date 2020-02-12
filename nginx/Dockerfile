FROM nginx:latest
MAINTAINER hckcksrl <hckcksrl@gmail.com>

COPY . ./home
WORKDIR home
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80