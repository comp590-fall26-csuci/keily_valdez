FROM docker.io/library/debian:13-slim

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY lab3/Makefile .
COPY lab3/makefile-lab/ ./makefile-lab/

RUN make

CMD ["./makefile-lab/fibonacci"]
