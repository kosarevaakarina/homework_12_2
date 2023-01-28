from dict.dict import get_val


def test_get_val_first():
    assert get_val({"vcs": "mercurial"}, "vcs") == 'mercurial'

def test_get_val_second():
    assert get_val({"vcs": "mercurial"}, "vcs", "git") == 'mercurial'


def test_get_val_third():
    assert get_val({}, "vcs", "git") == 'git'
    assert get_val({}, "vcs", "bazaar") == 'bazaar'
