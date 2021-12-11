#!/usr/local/bin/bash
# base64 encoded json strings:
export RAINBOW='eyJtZXNzYWdlIjoiU29tZXdoZXJlIG92ZXIgdGhlIHJhaW5ib3cuIiwibGVkZGF0YSI6W1sxNDgsMCwyMTFdLFs3NSwwMCwxMzBdLFswLDAsMjU1XSxbMCwxMjgsMjU1XSxbMCwyNTUsMF0sWzI1NSwyNTUsMF0sWzI1NSwxMjcsMF0sWzI1NSwwLDBdXX0K'
export RED='eyJtZXNzYWdlIjoiVGhlIHJlZCBtZW5hY2UuIiwibGVkZGF0YSI6W1syNTUsMCwwXSxbMjU1LDAsMF0sWzI1NSwwLDBdLFsyNTUsMCwwXSxbMjU1LDAsMF0sWzI1NSwwLDBdLFsyNTUsMCwwXSxbMjU1LDAsMF1dfQo='
export GREEN='eyJtZXNzYWdlIjoiSXRzIG5vdCBlYXN5IGJlaW5nIGdyZWVuLiIsImxlZGRhdGEiOltbMCwyNTUsMF0sWzAsMjU1LDBdLFswLDI1NSwwXSxbMCwyNTUsMF0sWzAsMjU1LDBdLFswLDI1NSwwXSxbMCwyNTUsMF0sWzAsMjU1LDBdXX0K'
export BLUE='eyJtZXNzYWdlIjoiSW0gYmx1ZSBkYWJvb2RlZWRhYm9vZGF5LiIsImxlZGRhdGEiOltbMCwwLDI1NV0sWzAsMCwyNTVdLFswLDAsMjU1XSxbMCwwLDI1NV0sWzAsMCwyNTVdLFswLDAsMjU1XSxbMCwwLDI1NV0sWzAsMCwyNTVdXX0K'
export DARK='eyJtZXNzYWdlIjoiSGVsbG8gZGFya25lc3MgbXkgb2xkIGZyaWVuZC4iLCJsZWRkYXRhIjpbWzAsMCwwXSxbMCwwLDBdLFswLDAsMF0sWzAsMCwwXSxbMCwwLDBdLFswLDAsMF0sWzAsMCwwXSxbMCwwLDBdXX0K'
while true; do
echo Hello darkness my old friend.
aws iot-data publish --topic 'ESP32/sub' --payload ${DARK}
sleep 3
echo The red menace!
aws iot-data publish --topic 'ESP32/sub' --payload ${RED}
sleep 3
echo Its not easy being green.
aws iot-data publish --topic 'ESP32/sub' --payload ${GREEN}
sleep 3
echo Im blue daboodeedabooday.
aws iot-data publish --topic 'ESP32/sub' --payload ${BLUE}
sleep 3
echo Somewhere over the rainbow.
aws iot-data publish --topic 'ESP32/sub' --payload ${RAINBOW}
sleep 3
done
