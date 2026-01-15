#!/usr/bin/env bash
POSITION=50
count=0

input=$(cat 1.txt)
check_position () {
  if [[ ${POSITION} -eq 100 ]]; then 
    POSITION=0
  elif [[ ${POSITION} -eq -1 ]]; then 
    POSITION=99
  fi
  if [[ ${POSITION} -eq 0 ]]; then
    echo 'HIT!'
    ((count++))
  fi
  if [[ ${POSITION} -gt 100 ]]; then 
    echo "error! $POSITION out of bounds"
    exit 1
  elif [[ ${POSITION} -eq -1 ]]; then 
    echo "error! $POSITION out of bounds"
    exit 1
  fi
}

for i in ${input}; do
  first_letter=${i:0:1}
  movement="${i:1}"
  #echo $i
  echo -n "${POSITION} "
  if [[ ${first_letter} == 'L' ]]; then
    echo -n "-"
    echo -n " ${movement}"
    #(( POSITION = POSITION - movement ))
    while [[ ${movement} -gt 0 ]]; do
      ((POSITION--))
      ((movement--))
      check_position
    done
  elif [[ ${first_letter} == 'R' ]]; then
    echo -n "+"
    echo -n " ${movement}"
    #(( POSITION = POSITION + movement ))
    while [[ ${movement} -gt 0 ]]; do
      ((POSITION++))
      ((movement--))
      check_position
    done
  else
    echo "error: $i"
    exit 1
  fi
  #check_position
  echo " = ${POSITION} "
  #sleep 0.05
done
echo $count
