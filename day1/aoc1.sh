#!/usr/bin/env zsh

A=($(cat input1.txt));
for i in {1..${#A}}; do
  for x in {2..${#A}}; do
    for y in {3..${#A}};do
      if (( $A[$i] + $A[$x] + $A[$y] == 2020 )); then
        echo "$A[$i] * $A[$x] * $A[$y]" | bc -l;
        break 3;
      fi;
    done;
  done;
done
