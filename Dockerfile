# imagem base
FROM debian:13

# atualozar o registry do apt
RUN apt update

# instalando ferramentas para o experimento
# xz e bzip2
RUN apt install xz-utils bzip2
