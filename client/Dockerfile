#FROM node:10-alpine AS build
#WORKDIR /app
#COPY package.json ./
##RUN npm --verbose install
#COPY . .
#CMD ["npm", "run", "dev"]

#FROM node:10-alpine AS build
#WORKDIR /app
#COPY . .
#
#FROM nginx:1.19.6-alpine AS prod
#COPY --from=build /app/dist /usr/share/nginx/html
#EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]

FROM node:10-alpine
RUN npm install -g http-server
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 8080
CMD [ "http-server", "dist" ]
