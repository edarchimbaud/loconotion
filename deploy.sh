#!/bin/bash

rm -r dist/edarchimbaud
python loconotion edarchimbaud/edarchimbaud.toml
(cd ../edarchimbaud.github.io; rm *)
cp dist/edarchimbaud/* ../edarchimbaud.github.io/.
echo "# edarchimbaud.github.io" > ../edarchimbaud.github.io/README.md
echo ".DS_Store" > ../edarchimbaud.github.io/.gitignore
(cd ../edarchimbaud.github.io; git add *; git commit -m "feat: new version"; git pull; git push)