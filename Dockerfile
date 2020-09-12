FROM python:3.8.0-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . .

RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install cython \
    && apk del .build-deps

#RUN python setup.py install
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN mkdir -p /root/.streamlit

RUN /bin/sh -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN /bin/sh -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

EXPOSE 8501

ENTRYPOINT [ 'python' ]
CMD [ 'setup.py install' ]
CMD [ 'streamlit', 'run', 'src/reflect/app/streamlit_app.py' ]

EXPOSE 8501 
