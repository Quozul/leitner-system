FROM node:20-alpine as build

WORKDIR /src/app

COPY package*.json ./
RUN npm ci

COPY . .

RUN npm run build

FROM nginx:alpine

COPY --from=build /src/app/dist /usr/share/nginx/html
