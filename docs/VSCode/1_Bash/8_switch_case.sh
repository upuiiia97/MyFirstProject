#!/bin/bash

name=$1

case "$name" in
  "Vasya") 
  greetString="Whatsupp"
  nameString="Vasiliy"
  ;;
  "Masha" )
  greetString="Hey"
  nameString="Masha"
  ;;
  * )
  greetString="Hello"
  nameString="Stranger"
  ;;
esac

echo "$greetString, $nameString!"