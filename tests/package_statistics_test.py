import random

from package_statistics import *


def test_download():
    init_logger()
    repos = []
    with open('data/contents_lines.txt', 'rt') as f:
        for line in f:
            line_segments = [x for x in line.strip().split() if x]
            if len(line_segments) != 2:
                continue
            file_name, repo = line_segments[0], line_segments[1]
            repos.append(repo)
    i = 0
    for line in contents_generator(mirror_url='http://ftp.uk.debian.org/debian/dists/stable/main/',
                                   file_name='Contents-amd64.gz'):
        line_segments = [x for x in line.strip().split() if x]
        if len(line_segments) != 2:
            continue
        assert (repos[i] == line_segments[1])
        i = i + 1
        if i > 10:
            break


def test_download_fail():
    init_logger()
    try:
        for _ in contents_generator(mirror_url='http://ftp.uk.debian.org/debian/dists/stable/main/',
                                    file_name='Contents-{}.gz'.format("non-existent-arch")):
            pass
    except ValueError:
        pass


def test_get_repo():
    init_logger()
    line1 = '  bin/ash                                                 shells/ash\n'
    line2 = 'bin/ash             shells/ash    \n '
    line3 = 'bin/ash                         \n'
    line4 = 'bin/ash                                                 shells/ash'
    repo1 = get_repo(line1)
    repo2 = get_repo(line2)
    repo3 = get_repo(line3)
    repo4 = get_repo(line4)
    assert (repo1 == 'shells/ash')
    assert (repo2 == 'shells/ash')
    assert (repo3 is None)
    assert (repo4 == 'shells/ash')


def construct_key_counter():
    my_keys = ['a'] * 5 + ['b'] * 10 + ['c'] * 3
    random.shuffle(my_keys)
    key_counter = KeyCounter()
    for key in my_keys:
        key_counter.add_key(key)
    return key_counter


def test_key_to_count():
    init_logger()
    key_counter = construct_key_counter()
    assert (key_counter.key_to_counter['a'] == 5)
    assert (key_counter.key_to_counter['b'] == 10)
    assert (key_counter.key_to_counter['c'] == 3)


def test_value_sorting():
    init_logger()
    key_counter = construct_key_counter()
    my_list = key_counter.sort_by_value_reverse()
    assert ([x[0] for x in my_list] == ['b', 'a', 'c'])
