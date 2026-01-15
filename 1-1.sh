#!/usr/bin/env bash
POSITION=50
count=0

input=$(cat 1.txt)

for i in ${input}; do
  first_letter=${i:0:1}
  movement="${i:1}"
  #echo $i
  echo -n "${POSITION} "
  if [[ ${first_letter} == 'L' ]]; then
    echo -n "-"
    echo -n " ${movement}"
    (( POSITION = POSITION - movement ))
  elif [[ ${first_letter} == 'R' ]]; then
    echo -n "+"
    echo -n " ${movement}"
    (( POSITION = POSITION + movement ))
  else
    echo "error: $i"
    exit 1
  fi
  while [[ ${POSITION} -ge 100 ]]; do
    (( POSITION = POSITION - 100 ))
  done
  while [[ ${POSITION} -lt 0 ]]; do
    ABS_POSITION=$(( POSITION >= 0 ? POSITION : -POSITION ))
    (( POSITION = 100 - ABS_POSITION ))
  done
  echo " = ${POSITION} "
  if [[ ${POSITION} -eq 0 ]]; then
    echo 'HIT!'
    ((count++))
  fi
  #sleep 0.05
done
echo $count
