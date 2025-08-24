FROM debian:13 as base

RUN apt update

# instalando ferramentas para o experimento
# xz e bzip2
RUN apt install -y xz-utils bzip2 time

WORKDIR /exp

COPY arquivos_so.tar.xz /

RUN mkdir arquivos_testes

RUN tar -xJvf /arquivos_so.tar.xz -C ./arquivos_testes

# imagem base
FROM debian:13 as final

# atualozar o registry do apt
RUN apt update

# instalando ferramentas para o experimento
# xz e bzip2
RUN apt install -y xz-utils bzip2 time

WORKDIR /exp

COPY --from=base /exp /exp

COPY ronaldo.sh .
