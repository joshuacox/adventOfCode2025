#!/usr/bin/env bash
total=0

input=$(cat 2.txt.sample|tr ',' '\n')

test_string () {
  #echo $1
  string=$1
  REPEATERS=$(echo "$string" | grep -oE '(.)\1+' | awk '{ print $0, length }')
  REPEATERS_COUNT=$(echo ${REPEATERS} | wc -l)
  if [[ ${REPEATERS_COUNT} -gt 0 ]]; then
    REJECT=1
    #echo ${REPEATERS}
    (( total = total + $1 ))
    echo ${1}
    ((count++))
  else
    REJECT=0
  fi
}

for i in ${input}; do
  START=$(echo $i |cut -f1 -d'-')
  END=$(echo $i |cut -f2 -d'-')
  count=${START}

  while [[ ${count} -le ${END} ]]; do
    #test_string "${count}"
    ./2-1.py ${count}
  done
done
echo $count
echo $total
