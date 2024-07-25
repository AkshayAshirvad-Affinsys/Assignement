
FROM node AS BASE
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

#ENV PORT=3002
#ENV PGUSER=postgres
#ENV PGHOST=localhost
#ENV PGPASSWORD=password123
#ENV PGDATABASE=yelp
#ENV PGPORT=5432

FROM node:slim
RUN groupadd -r myusergrp && useradd -r -g myusergrp myuser
WORKDIR /usr/src/app
COPY --from=BASE  /app /usr/src/app/
RUN chown -R myuser:myusergrp /usr/src/app


USER myuser
EXPOSE 3002


CMD ["node", "server.js"]
