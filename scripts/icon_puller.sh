#!/bin/sh
set -ex
icons="rss-square"

dest=fontawesome
url=https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/svgs/solid

mkdir -p "${dest}"
for icon in $icons; do
  icon="${icon}.svg"
  wget -O "${dest}/${icon}" "${url}/${icon}"
done
