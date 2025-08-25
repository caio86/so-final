#!/usr/bin/env bash

# Function to display a spinning progress indicator
show_spinner() {
  local pid=$1
  local delay=0.1
  local spinstr='|/-\'

  # Hide the cursor
  echo -ne "\033[?25l"

  while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
    local temp=${spinstr#?}
    printf " [%c] " "$spinstr"
    local spinstr=$temp${spinstr%"$temp"}
    sleep $delay
    printf "\b\b\b\b\b"
  done

  # Show cursor again
  echo -ne "\033[?25h"
  printf "    \b\b\b\b"
}

# Function to display a progress bar
show_progress_bar() {
  local pid=$1
  local delay=0.1
  local bar=""

  # Hide the cursor
  echo -ne "\033[?25l"

  while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
    bar="${bar}="
    printf " [%-20s] " "$bar"
    sleep $delay
    # Move cursor back to start of line
    printf "\r"
    if [ ${#bar} -eq 20 ]; then
      bar=""
    fi
  done

  # Show cursor again
  echo -ne "\033[?25h"
}

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

tmp=$(mktemp)
out="saida/$1-$(basename $2).csv"
mkdir saida 2>/dev/null
chmod 777 ./saida

echo "User time;System time;System input;System output;Swaps;Voluntary context switches;Involuntary context switches" >$out
chmod 666 $out

for x in $(seq $3); do
  /usr/bin/time -v tar $TAR_OPTS $OUTFILE $INFILE >/dev/null 2>$tmp &
  pid=$!

  echo "Executando repetição $x"

  show_spinner $pid

  ut=$(cat $tmp | awk -F ": " '/User/ {print $2}')
  st=$(cat $tmp | awk -F ": " '/System/ {print $2}')
  si=$(cat $tmp | awk -F ": " '/system input/ {print $2}')
  so=$(cat $tmp | awk -F ": " '/system output/ {print $2}')
  sw=$(cat $tmp | awk -F ": " '/Swaps/ {print $2}')
  vc=$(cat $tmp | awk -F ": " '/Voluntary/ {print $2}')
  ic=$(cat $tmp | awk -F ": " '/Involuntary/ {print $2}')

  echo "$ut;$st;$si;$so;$sw;$vc;$ic" >>$out
done

rm $tmp

echo "Processo TAR finalizado. Monitoramento encerrado."
