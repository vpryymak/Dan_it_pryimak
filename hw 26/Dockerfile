FROM node:18

WORKDIR /app

COPY package.json .

RUN npm i

COPY . .

EXPOSE 10000

CMD ["npm", "run", "start"]
