#!/usr/bin/env bash -e

extract(){
    exp="[^A-Z]*\([A-Z]\{2,\}-[0-9]\{1,\}\).*"
    found=$(echo "${1}" | grep ${exp})
    if [ -z "${found}" ]; then
        echo "jira"
        return
    fi
    echo $(echo "${1}" | sed -e "s|${exp}|\1|" | tr '[:upper:]' '[:lower:]')
}

out=$(extract ${1})
echo ${out}