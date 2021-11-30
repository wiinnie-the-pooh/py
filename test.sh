#!/usr/bin/env bash -e -x

verify(){
    test $(./getkey.sh "${1}") = "${2}" || echo "ERROR on: " "${1}" '=' "${2}"
}

verify "AD-3a" "ad-3"
verify "DAT-123" "dat-123"
verify "A-3" "jira"
verify "XYZ 123" "jira"
verify "XYZ 123" "jira"
verify "asdfasdfBD-333^asdf asdf -a sfasd fasdBD-123fasdf" "bd-333"
verify "feature/BF-18/abc-123-this is a great feature abc-123 X-88 ABCDEFG-999 abc XY-Z-333 abcDEF-33 ABC-1" "bf-18"
