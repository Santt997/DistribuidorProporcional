# Commands

## Activate

`conda activate UMLgen-py310`

## Create

```bash
cd ~/Documents/GitHub/Nuevo/envs &&
conda env create --file UMLgen-py310.yml -y
```

## List

`conda list -n UMLgen-py310 "python|plantuml"`

## Export

`conda env export -n UMLgen-py310 > UMLgen0-py310.yml`

## Update

```bash
cd ~/Documents/GitHub/Nuevo/envs &&
conda env update --file UMLgen-py310.yml --prune && 
conda env export -n UMLgen-py310 > UMLgen0-py310.yml.tmp && 
if [[ ! -f UMLgen-py310.yml || $(md5sum UMLgen-py310.yml.tmp | cut -d' ' -f1) != $(md5sum UMLgen-py310.yml | cut -d' ' -f1) ]]; then
  mv UMLgen-py310.yml.tmp UMLgen-py310.yml && echo "✅ Actualizado" && stat UMLgen-py310.yml
else
  rm UMLgen-py310.yml.tmp && echo "Sin cambios"
fi
```

## Rename

`conda deactivate && conda rename -n UMLgen-py UMLgen-py310`

## Remove

`conda env remove --name UMLgen-py -y`
`conda env remove --name UMLgen-py310 -y`
