#!/usr/bin/env bash

DEBUG=0

usage() {
  echo "Uso: $0 <xz|bz|gz> <arquivo> <qtdRepeticoes>"
  echo "  Typo de compresão: xz, bz, ou gz"
  echo "  Arquivo: caminho para um arquivo"
  echo "  Repetições: numero inteiro (1 ou maior)"
  exit 1
}

# Function to validate integer input
is_positive_int() {
  case $1 in
  '' | *[!0-9]*) return 1 ;; # Contains non-digit characters
  *) [ "$1" -ge 1 ] ;;       # Check if greater than or equal to 1
  esac
}

# Check if we have exactly 3 parameters
if [ $# -ne 3 ]; then
  echo "Error: Necessário 3 argumentos"
  usage
fi

# Validate filename
if [ ! -f "$2" ]; then
  echo "Error: Arquivo '$2' não existe ou não é um arquivo normal"
  exit 1
fi

if [ ! -r "$2" ]; then
  echo "Error: Arquivo '$2' não permite leitura"
  exit 1
fi
INFILE=$2

# Validate compression type
TAR_OPTS=""
case $1 in
xz)
  TAR_OPTS="-cJvf"
  OUTFILE="${INFILE}.tar.xz"
  ;;
bz)
  TAR_OPTS="-cjvf"
  OUTFILE="${INFILE}.tar.bz2"
  ;;
gz)
  TAR_OPTS="-czvf"
  OUTFILE="${INFILE}.tar.gz"
  ;; # Valid options
*)
  echo "Error: Primeiro parâmetro precisa ser um desses xz, bz, ou gz"
  usage
  ;;
esac

# Validate repetition count
if ! is_positive_int "$3"; then
  echo "Error: Terceiro parâmetro precisa ser um inteiro positivo"
  usage
fi

start_time=$(date +%s%3N)

/usr/bin/time -v tar $TAR_OPTS $OUTFILE $INFILE
# TAR_PID=$!

# Função para lidar com Ctrl+C
# cleanup() {
#   echo -e "\nInterrupção detectada. Finalizando processo TAR (PID: $TAR_PID)..."
#   kill -TERM $TAR_PID 2>/dev/null
#   wait $TAR_PID 2>/dev/null
#   echo "Processo finalizado. Saindo..."
#   exit 0
# }

# Configura o trap para capturar Ctrl+C
# trap cleanup SIGINT

# # Verifica se o processo existe antes de monitorar
# if kill -0 $TAR_PID 2>/dev/null; then
#   [[ $DEBUG == 1 ]] && echo "Monitorando context switches do processo TAR (PID: $TAR_PID)"
#   [[ $DEBUG == 1 ]] && echo "Data/Hora | Voluntary | Nonvoluntary"
#
#   # Monitora enquanto o processo existir
#   while kill -0 $TAR_PID 2>/dev/null; do
#     # Coleta apenas as informações de context switches com timestamp
#     if [ -f /proc/$TAR_PID/status ]; then
#       voluntary=$(grep -E "^voluntary_ctxt_switches" /proc/$TAR_PID/status 2>/dev/null | awk '{print $2}')
#       nonvoluntary=$(grep -E "^nonvoluntary_ctxt_switches" /proc/$TAR_PID/status 2>/dev/null | awk '{print $2}')
#       [[ $DEBUG == 1 ]] && echo "$(date '+%Y-%m-%d %H:%M:%S') | $voluntary | $nonvoluntary"
#     fi
#     # sleep 0.5 # Intervalo de verificação reduzido
#   done
# else
#   echo "Processo TAR não iniciou corretamente!"
#   exit 1
# fi

end_time=$(date +%s%3N)

exec_time=$((end_time - start_time))

echo "Processo TAR finalizado. Monitoramento encerrado."
