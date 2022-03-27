from .main import get_taskname
import pytest


@pytest.mark.parametrize(('filename', 'expected'), [
    ('taskname_6adfb183a4a2c94a2f92dab5ade762a47889a5a1.tar.gz', 'taskname'),
    ('taskname-6adfb183a4a2c94a2f92dab5ade762a47889a5a1.tar.gz', 'taskname'),
    ('taskname.tar.gz-6adfb183a4a2c94a2f92dab5ade762a47889a5a1', 'taskname'),
    ('taskname.tar.gz.6adfb183a4a2c94a2f92dab5ade762a47889a5a1', 'taskname'),
    ('task-name_6adfb183a4a2c94a2f92dab5ade762a47889a5a1.tar.gz', 'task-name'),
    ('6adfb183a4a2c94a2f92dab5ade762a47889a5a1-taskname.tar.gz', 'taskname'),
    ('6adfb183a4a2c94a2f92dab5ade762a47889a5a1_taskname.tar.gz', 'taskname'),
    ('task-name.tar.gz', 'task-name'),

    ('taskname-6adfb183a4a2c94a2f92dab5ade762a47889a5a1.zip', 'taskname'),
    ('taskname.zip-6adfb183a4a2c94a2f92dab5ade762a47889a5a1', 'taskname'),
    ('6adfb183a4a2c94a2f92dab5ade762a47889a5a1-taskname.zip', 'taskname'),
    ('task-name.zip', 'task-name'),

    # short name
    ('sn_6adfb183a4a2c94a2f92dab5ade762a47889a5a1.tar.gz', 'sn'),
    ('sn.tar.gz-6adfb183a4a2c94a2f92dab5ade762a47889a5a1', 'sn'),
    ('s-n_6adfb183a4a2c94a2f92dab5ade762a47889a5a1.tar.gz', 's-n'),
    ('6adfb183a4a2c94a2f92dab5ade762a47889a5a1_sn.tar.gz', 'sn'),
    ('sn.tar.gz', 'sn'),
])
def test_get_taskname(filename, expected):
    assert get_taskname(filename) == expected
