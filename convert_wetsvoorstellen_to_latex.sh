#!/bin/bash

# First convert all .md to .tex (without --standalone, since the master handles the preamble)
find . -wholename "./.temp/wetsvoorstellen/*.md" | while read file; do
    output="./.output/${file%.md}.tex"
    mkdir -p "$(dirname "$output")"
    pandoc "$file" -o "$output"  # no --standalone
done

# Then generate the master file
{
    cat <<'EOF'
\documentclass{article}
\usepackage{hyperref}
\title{Wetsvoorstellen}

\begin{document}
\maketitle
\tableofcontents
EOF

    prev_dir=""
    find . -wholename "*wetsvoorstellen*.tex" ! -name "main.tex" | sort | while read file; do
    dir=$(dirname "$file")
    if [ "$dir" != "$prev_dir" ]; then
        chapter=$(basename "$dir" | sed 's/^[0-9]*-//' | sed 's/-/ /g')
        echo "\\chapter{$chapter}"
        prev_dir="$dir"
    fi
    echo "\\input{${file%.tex}}"
    done

  echo '\end{document}'
} > ./.output/.temp/main.tex