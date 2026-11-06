#!/bin/sh

rsync \
-avzh \
--progress \
kitchen@pikitchen.local:/home/kitchen/Cooklang/recipes/config/ \
~/repos/Cooklang/recipes/config/

rsync \
-avzh \
--perms \
--delete \
--progress \
--exclude '/paprika-import/' \
--exclude '/.shopping-*' \
--exclude '/config/*' \
--exclude '.DS_Store' \
~/repos/Cooklang/recipes/ \
kitchen@pikitchen.local:/home/kitchen/Cooklang/recipes/
