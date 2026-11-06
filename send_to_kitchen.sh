#!/bin/sh

scp kitchen@pikitchen.local:~/Cooklang/recipes/config/aisle.conf ~/repos/Cooklang/recipes/config/aisle.conf

rsync \
-avzh \
--perms \
--delete \
--progress \
--exclude '/paprika-import/' \
--exclude '.DS_Store' \
~/repos/Cooklang/recipes/ \
kitchen@pikitchen.local:/home/kitchen/Cooklang/recipes/
