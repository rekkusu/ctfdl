# ctfdl

```sh
% ctfdl -h
usage: ctfdl [-h] [-a dir] [-f FILE] [-y] [--no-extract] [--stdin] [URL [URL ...]]

CTF task downloader

positional arguments:
  URL                   URLs to download

optional arguments:
  -h, --help            show this help message and exit
  -a dir, --archive dir
                        directory to save downloaded files
  -f FILE, --file FILE
  -y, --extract         extract all files
  --no-extract          do not extract downloaded files
  --stdin               read urls from stdin

```

### Usage
```sh
% ctfdl http://localhost:1234/task-ecb13b07adbb0056ef3a8420679299faaf155894.tar.gz
./archives/task-ecb13b07adbb0056ef3a8420679299faaf155894.tar.gz: 100%|█████████████████████| 141/141 [00:00<00:00, 174kB/s]
task ./archives/task-ecb13b07adbb0056ef3a8420679299faaf155894.tar.gz
[+] file1 => task/file1
[+] file2 => task/file2
Proceed to extract?[Y/n]
Extracting...
Done.
% tree .
.
├── archives
│   └── task-ecb13b07adbb0056ef3a8420679299faaf155894.tar.gz
└── task
    ├── file1
    └── file2

2 directories, 3 files
```
