for app in $(dirname $BASH_SOURCE)/../docs/_apps/*; do 
    if [ -d "$app" ] && [[ ! $(basename "$app") = _* ]]; then
        for v in "$app"/*; do
            if [ -d "$v" ]; then
                echo "Regenerating markdown for $(basename "$app"):$(basename "$v")"
                python $(dirname $BASH_SOURCE)/metadata_markdown.py "$v"
            fi
        done
    fi
done
