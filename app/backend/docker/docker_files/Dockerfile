FROM bobbystearman/hedera-py-java

### 3. Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
COPY . /code/
WORKDIR /code

RUN set -e; \
    /usr/local/bin/python -m pip install --upgrade pip ;\
    python -m pip install -r /code/requirements/dev.txt ;\
    chmod +x /code/docker/entrypoints/entrypoint.sh ;

EXPOSE 8000
ENTRYPOINT ["/code/docker/entrypoints/entrypoint.sh"]