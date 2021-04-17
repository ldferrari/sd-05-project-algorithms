FROM python:3
RUN mkdir algorithms
WORKDIR /algorithms
COPY . .
# Instalando as dependências
RUN apt-get update && apt-get install -y \
    python3-venv
RUN python3 -m venv .venv && \
    python3 -m pip install -r dev-requirements.txt

# Para rodar o container:
# docker build . -t trybe/algorithms
# docker run -it --name=project -v $PWD/challenges:/algorithms/challenges trybe/algorithms bash