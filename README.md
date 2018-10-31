# Description

This is just another gnu wc sample implementation in Python 3, it supports words, bytes and lines count from standard and urls, like:

```sh
$ echo -e  "1\n2\n3 4" | ./wc.py
3       4       8
```
```sh
$ ./wc.py -e  https://raw.githubusercontent.com/requests/requests/master/README.md
400
```

# Testing

Python 3 is required to execute and test wc.py.
 
pip3 install -r requirements.txt

Run pytest for unitesting
