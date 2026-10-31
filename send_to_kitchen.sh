#!/bin/sh

scp kitchen@pikitchen.local:~/Cooklang/recipes/config/aisle.conf ~/repos/Cooklang/recipes/config/aisle.conf
rsync -avz --delete --progress --exclude '/paprika-import/' ~/repos/Cooklang/recipes/ kitchen@pikitchen.local:/home/kitchen/Cooklang/recipes/
