
FROM node:12-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

ENV PORT=3002
ENV PGUSER=postgres
ENV PGHOST=localhost
ENV PGPASSWORD=password123
ENV PGDATABASE=yelp
ENV PGPORT=5432


EXPOSE 3002


CMD ["node", "server.js"]
