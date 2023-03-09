#!/bin/bash

rm -r dist/edarchimbaud
python loconotion edarchimbaud/edarchimbaud.toml
(cd dist/edarchimbaud; python ../../loconotion/modules/locorg.py)
(cd ../edarchimbaud.github.io; rm -r *)
cp -r dist/edarchimbaud/* ../edarchimbaud.github.io/.
echo "# edarchimbaud.github.io" > ../edarchimbaud.github.io/README.md
echo ".DS_Store" > ../edarchimbaud.github.io/.gitignore
(cd ../edarchimbaud.github.io; git add *; git commit -m "feat: new version"; git pull; git push)