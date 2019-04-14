from os.path import split
import logging
import urllib.request, urllib.response, urllib.error
import gzip


THIS_FILE_NAME = split(__file__)[-1]


logger = None

def init_logger (module_name:str=THIS_FILE_NAME, log_level:int=logging.INFO):
    global logger
    logging.basicConfig(level=log_level)
    logger = logging.getLogger(module_name)
    return logger

def contents_generator(
    mirror_url:str='http://ftp.uk.debian.org/debian/dists/stable/main/', file_name:str='Contents-amd64.gz'
):
    try:
        req = urllib.request.Request(mirror_url + file_name)
        res = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        error = "Unable to retrieve file_name: {} from {}.".format(file_name, mirror_url)
        logger.error(error)
        raise ValueError(error)

    # the use of 'rb' here is not a typo
    with gzip.open(res, 'rt') as f:
        for line in f:
            yield line

def main(architecture:str=None, mirror_url:str='http://ftp.uk.debian.org/debian/dists/stable/main/'):
    init_logger()
    logger.info("{} starts with architecture: {} and mirror: {}".format(
        THIS_FILE_NAME, architecture, mirror_url))
    i = 0
    for line in contents_generator(mirror_url=mirror_url, file_name="Contents-{}.gz".format(architecture)):
        logger.info (line.strip())
        i = i + 1
        if (i > 10):
            break

if __name__ == "__main__":
    main('amd64')
