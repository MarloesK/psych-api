ARG FUNCTION_DIR="/code"

FROM python:3.12 as build-image

ARG FUNCTION_DIR

RUN mkdir -p ${FUNCTION_DIR}

COPY requirements.txt ${FUNCTION_DIR}

RUN pip3 install --target ${FUNCTION_DIR} awslambdaric
RUN pip install -r ${FUNCTION_DIR}/requirements.txt --target ${FUNCTION_DIR}

COPY src ${FUNCTION_DIR}/src
COPY data ${FUNCTION_DIR}/data


FROM python:3.12-slim

ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}

COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "src.app.handler" ]