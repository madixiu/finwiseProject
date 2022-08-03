FROM node:lts


#RUN mkdir /finwise
#RUN cd /finwise
#RUN mkdir /frontend
# set working directory
RUN mkdir /frontend
WORKDIR /frontend

# add `/app/node_modules/.bin` to $PATH
#ENV PATH /app/node_modules/.bin:$PATH

# copy both 'package.json' and 'package-lock.json' (if available)
#COPY package.json ./

# https://docs.npmjs.com/cli/cache
#RUN npm cache verify

# install and cache app dependencies
#RUN npm install
#RUN npm install @vue/cli@4.3.1 -g

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . /frontend/

# expose port 8080 to the host
#EXPOSE 8080

# start app
CMD ["npm", "run", "serve"]
# CMD ["sh", "start_dev.sh"]