#!/bin/sh

scp kitchen@pikitchen.local:~/Cooklang/recipes/config/aisle.conf ~/repos/Cooklang/recipes/config/aisle.conf
rsync -avz --delete --progress ~/repos/Cooklang/recipes/ kitchen@pikitchen.local:/home/kitchen/Cooklang/recipes/
