from Events import *


def test_get_event():
    ME = EventManager()

    ME.add_event('S1', "11/20/2022", 'n/a', True)
    ME.add_event('S2', "11/20/2022", 'n/a', True)
    ME.add_event('S3', "11/20/2022", 'n/a', True)
    a = 'S2'
    assert ME.get_event(a).name == a
