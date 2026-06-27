#!/bin/bash

for i in {1..20}; do
    echo "Скачиание изображения $1..."
    curl "https://picsum.photos/800/400" -L > "attachments/image_$1.jpg"
done

echo "Готово! Скачано 20 изображений в папку attachments"
