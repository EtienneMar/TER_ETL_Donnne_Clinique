FROM node:20.0.0-alpine
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package*.json ./
RUN npm install --silent
RUN npm install serve
RUN npm install axios
COPY . ./
RUN npm run build
EXPOSE 3000
