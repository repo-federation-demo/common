ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-alpine
COPY do_something_important.py do_something_important.py
ENTRYPOINT bash