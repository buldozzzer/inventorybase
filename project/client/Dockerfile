FROM node:10-alpine AS build
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .

FROM nginx:1.19.0-alpine AS prod
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
