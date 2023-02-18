import requests
import urllib.parse
import argparse
import os
import os.path
import sys
import re
from typing import Optional, Tuple
from tqdm import tqdm
from .extractors import Extractor, TarExtractor, ZipExtractor


archive_exts = {
        '.tar.gz': TarExtractor,
        '.tgz': TarExtractor,
        '.tar.xz': TarExtractor,
        '.txz': TarExtractor,
        '.tar.bz2': TarExtractor,
        '.zip': ZipExtractor,
}


def execute(url: str, args: argparse.Namespace):
    path = download(url, args.archive)
    if path and not args.no_extract:
        extract(path, args.extract)


def download(url: str, dir: str = './') -> Optional[str]:
    try:
        head = requests.head(url, allow_redirects=True)
    except requests.exceptions.MissingSchema:
        sys.stderr.write('Invalid URL\n')
        return None
    except requests.exceptions.InvalidURL:
        sys.stderr.write('Invalid URL\n')
        return None

    content_length = int(head.headers['content-length'])
    if 'content-disposition' in head.headers.keys():
        disposition = head.headers['content-disposition']
        quoted_filename = re.findall("filename=\"(.+)\"", disposition)
        if len(quoted_filename) > 0:
            filename = quoted_filename[0]
        else:
            filename = re.findall("filename=(.+)", disposition)[0]
    else:
        parse_url = urllib.parse.urlparse(url)
        filename = os.path.join(dir, os.path.basename(parse_url.path))

    r = requests.get(url, allow_redirects=True, stream=True)
    progress = tqdm(desc=filename, total=content_length, unit='B', unit_scale=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)
            progress.update(len(chunk))

    return filename


def extract(path: str, extract=False):
    dest = get_taskname(path)
    os.makedirs(dest, exist_ok=True)

    extractor: Optional[Extractor] = None
    for ext in archive_exts:
        if path.endswith(ext):
            extractor = archive_exts[ext](path)

    if extractor is None:
        return

    for file in extractor.list():
        print(f'[+] {file} => {os.path.join(dest,file)}')

    if not extract:
        check = input('Proceed to extract?[Y/n]')
        if check.capitalize() == 'N':
            print('Cancelled')
            return

    print('Extracting...')
    extractor.extract(dest)
    print('Done.')


def remove_ext(name: str) -> str:
    if '.tar' in name:
        return name.split('.tar')[0]
    else:
        return os.path.splitext(name)[0]


def get_taskname(s: str) -> str:
    s = os.path.basename(s)

    m = re.match(r"(.*?)[._-]?([0-9a-fA-F]{32,})[_-]?(.*?)$", s)
    if m is None:
        # no hash in filename
        return remove_ext(s)

    return remove_ext(m.group(1) + m.group(3))


def main():
    parser = argparse.ArgumentParser(description='CTF task downloader')
    parser.add_argument('urls', metavar='URL', nargs='*', help='URLs to download')
    parser.add_argument('-a', '--archive', metavar='dir', default='./archives', help='directory to save downloaded files')
    parser.add_argument('-f', '--file')
    parser.add_argument('-y', '--extract', action='store_true', help='extract all files')
    parser.add_argument('--no-extract', action='store_true', help='do not extract downloaded files')
    parser.add_argument('--stdin', action='store_true', help='read urls from stdin')
    args = parser.parse_args()

    os.makedirs(args.archive, exist_ok=True)
    if args.stdin:
        while True:
            try:
                url = input()
                if not url:
                    break
                execute(url, args)
            except KeyboardInterrupt:
                break
            except EOFError:
                break
    elif args.file:
        with open(args.file, 'r') as f:
            for url in f.readlines():
                execute(url.strip(), args)
    else:
        for url in args.urls:
            execute(url, args)

if __name__ == '__main__':
    main()
