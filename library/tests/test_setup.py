import pytest


def test_setup(_rpi_ws281x):
    from rpi_ws281x import PixelStrip
    strip = PixelStrip(10, 20)
    strip.begin()


def test_setup_init_fail(_rpi_ws281x):
    from rpi_ws281x import PixelStrip
    _rpi_ws281x.ws2811_init.return_value = 1
    strip = PixelStrip(10, 20)
    with pytest.raises(RuntimeError):
        strip.begin()


def test_num_pixels(_rpi_ws281x):
    from rpi_ws281x import PixelStrip
    strip = PixelStrip(10, 20)
    strip.begin()
    assert len(strip[:]) == 10
    assert len(strip) == 10
    assert strip.numPixels() == 10


def test_set_pixel(_rpi_ws281x):
    from rpi_ws281x import PixelStrip, RGBW
    strip = PixelStrip(10, 20)
    strip.begin()
    strip[0] = RGBW(255, 0, 0)
    assert strip[0] == strip.getPixelColor(0)
    assert strip[0] == RGBW(255, 0, 0)
    assert strip.getPixelColorRGB(0) == RGBW(255, 0, 0)
    assert strip.getPixelColorRGBW(0) == RGBW(255, 0, 0)
    assert strip.getPixelColorRGBW(0).r == 255


def test_set_multiple(_rpi_ws281x):
    from rpi_ws281x import PixelStrip, RGBW
    strip = PixelStrip(10, 20)
    strip.begin()
    strip[:] = RGBW(255, 0, 0)
    assert strip[:] == [RGBW(255, 0, 0)] * 10


def test_set_odd(_rpi_ws281x):
    from rpi_ws281x import PixelStrip, RGBW
    strip = PixelStrip(10, 20)
    strip.begin()
    strip[::2] = RGBW(255, 0, 0)
    assert strip[:] == [RGBW(255, 0, 0), RGBW(0, 0, 0)] * 5
