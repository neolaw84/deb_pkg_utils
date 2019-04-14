import gzip
import logging
import urllib.error
import urllib.request
import urllib.response
from os.path import split
from typing import List, Tuple, Optional

THIS_FILE_NAME = split(__file__)[-1]

logger = None


def init_logger(module_name: str = THIS_FILE_NAME, log_level: int = logging.INFO):
    global logger
    logging.basicConfig(level=log_level)
    logger = logging.getLogger(module_name)
    return logger


def contents_generator(
        mirror_url: str = 'http://ftp.uk.debian.org/debian/dists/stable/main/', file_name: str = 'Contents-amd64.gz'
) -> str:
    try:
        req = urllib.request.Request(mirror_url + file_name)
        res = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        error = "Unable to retrieve file_name: {} from {}.".format(file_name, mirror_url)
        logger.error(error)
        raise ValueError(error)

    # the use of 'rb' here is not a typo
    with gzip.open(res, 'rb') as f:
        for line in f:
            yield line.decode()


def get_repo(line: str = '') -> Optional[str]:
    line_segments = [x for x in line.strip().split() if x]
    if len(line_segments) != 2:
        return None
    repo = line_segments[1]
    return repo


class KeyCounter(object):
    def __init__(self):
        self.key_to_counter = {}

    def add_key(self, key: str) -> None:
        counter = self.key_to_counter.get(key, 0)
        counter = counter + 1
        self.key_to_counter[key] = counter
        logger.debug("current {key} -> counter {counter}".format(key=key, counter=counter))

    def sort_by_value(self, reverse: bool = False) -> List[Tuple]:
        return sorted(self.key_to_counter.items(), key=lambda kv: (kv[1], kv[0]), reverse=reverse)

    def sort_by_value_reverse(self) -> List[Tuple]:
        return self.sort_by_value(reverse=True)


def main(
        architecture: str = None, mirror_url: str = 'http://ftp.uk.debian.org/debian/dists/stable/main/', k: int = 10
)->None:
    init_logger()
    logger.info("{} starts with architecture: {} and mirror: {}".format(
        THIS_FILE_NAME, architecture, mirror_url))
    key_counter = KeyCounter()
    i = 0
    divider = 100
    for line in contents_generator(mirror_url=mirror_url, file_name="Contents-{}.gz".format(architecture)):
        repo = get_repo(line)
        key_counter.add_key(repo)
        if i % divider == 0:
            divider = divider * 10
            logger.info("processed ... {} lines in input.".format(i))
        i = i + 1
    top_list = key_counter.sort_by_value_reverse()
    top10_list = top_list[0:10]
    for i in range(0, k):
        print("{rank}. {package} {count}".format(
            rank=i + 1, package=top10_list[i][0], count=top10_list[i][1]
        ))


if __name__ == "__main__":
    main('ppc64el')
