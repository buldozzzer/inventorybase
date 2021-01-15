FROM node:10-alpine AS build
WORKDIR /app
COPY package.json ./
#RUN npm --verbose install
COPY . .
CMD ["npm", "run", "dev"]
