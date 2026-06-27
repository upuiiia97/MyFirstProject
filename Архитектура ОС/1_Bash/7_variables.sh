#!/bin/bash

greetString="Hello"
nameString="stranger"

if [ "$#" -lt 1 ];
then
  echo "Недостаточно аргументов. Пож-та, передайте в качестве аргумента имя. Пример: $0 Vasya"
  exit 1
fi

if [ "$1" = "Vasya" ]; 
then
        greetString="Whatsupp"
        nameString="Vasiliy"
elif [ "$1" = "Masha" ];
then
        nameString="Masha"
elif [ "$1" = "Michael" ];
then
        greetString="Shalom"
        nameString="Michael"
fi

        echo "$greetString, $nameString!"
