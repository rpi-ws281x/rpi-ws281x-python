import pytest
import mock
import sys

_mock_rpi_ws281x = mock.MagicMock()
channels = {}


def ws2811_channel_get(new_ws2811_t, ch):
    if ch not in channels:
        channels[ch] = {'new_ws2811_t': new_ws2811_t}
    return channels[ch]


def ws2811_channel_t_count_set(ch, count):
    ch['count'] = count
    ch['leds'] = [0 for _ in range(count)]


def ws2811_channel_t_count_get(ch):
    return ch['count']


def ws2811_led_set(ch, n, rgbw):
    ch['leds'][n] = rgbw


def ws2811_led_get(ch, n):
    return ch['leds'][n]


_mock_rpi_ws281x.ws2811_channel_t_count_set = ws2811_channel_t_count_set
_mock_rpi_ws281x.ws2811_channel_t_count_get = ws2811_channel_t_count_get
_mock_rpi_ws281x.ws2811_channel_get = ws2811_channel_get
_mock_rpi_ws281x.ws2811_led_set = ws2811_led_set
_mock_rpi_ws281x.ws2811_led_get = ws2811_led_get


@pytest.fixture(scope='function', autouse=False)
def _rpi_ws281x():
    _mock_rpi_ws281x.ws2811_init.return_value = 0
    sys.modules['_rpi_ws281x'] = _mock_rpi_ws281x

    yield _mock_rpi_ws281x
    del sys.modules['_rpi_ws281x']
    _mock_rpi_ws281x.reset_mock()
    channels.clear()


@pytest.fixture(scope='function', autouse=True)
def rpi_ws281x(_rpi_ws281x):
    if "." not in sys.path:
        sys.path.append(".")
    yield None
    del sys.modules['rpi_ws281x']
