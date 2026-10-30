#!/bin/sh

rsync -avz --delete --progress ~/repos/Cooklang/recipes/ kitchen@pikitchen.local:/home/kitchen/Cooklang/recipes/
