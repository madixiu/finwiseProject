# build stage

FROM node:lts as build-stage
WORKDIR /frontend/
COPY frontend/package.json /frontend/
RUN npm cache verify
RUN npm install
COPY frontend /frontend/
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY nginx/prod/prod.conf /etc/nginx/nginx.conf
# COPY nginx/prod/finwise.pem /etc/ssl/finwise.pem
COPY nginx/prod/letsencrypt /etc/letsencrypt/
COPY backend/static /usr/src/app/static/
COPY --from=build-stage /frontend/dist /dist/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
