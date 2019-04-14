from package_statistics import *

def test_download ():
    logger = init_logger('package_statistics_test')
    repos = []
    with open ('data/contents_lines.txt', 'rt') as f:
        for line in f:
            line_segments = [x for x in line.strip().split() if x]
            if len(line_segments) != 2:
                continue
            file_name, repo = line_segments[0], line_segments[1]
            repos.append(repo)
    i = 0
    for line in contents_generator(mirror_url='http://ftp.uk.debian.org/debian/dists/stable/main/', file_name='Contents-amd64.gz'):
        line_segments = [x for x in line.strip().split() if x]
        if len(line_segments) != 2:
            continue
        assert (repos[i] == line_segments[1])
        i = i + 1
        if (i > 10):
            break

def test_download_fail ():
    logger = init_logger('package_statistics_test')
    try:
        for line in contents_generator(mirror_url='http://ftp.uk.debian.org/debian/dists/stable/main/',
                                   file_name='Contents-{}.gz'.format("non-existent-arch")):
            pass
    except ValueError:
        pass
    except:
        assert(False)