# FROM redis:latest
# RUN run -d --name my-redis -p 5005:5005 redis

FROM rasa/rasa:2.8.11-full

EXPOSE 5005
WORKDIR /app

COPY ./models /app/models

CMD [ "run", "--enable-api", "--endpoints", "/app/endpoints.yml"]



