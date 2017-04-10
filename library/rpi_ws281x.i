// SWIG interface file to define rpi_ws281x library python wrapper.
// Author: Tony DiCola (tony@tonydicola.com), Jeremy Garff (jer@jers.net)

// Define module name rpi_ws281x.  This will actually be imported under
// the name _rpi_ws281x following the SWIG & Python conventions.
%module rpi_ws281x

// Include standard SWIG types & array support for support of uint32_t
// parameters and arrays.
%include "stdint.i"
%include "carrays.i"

%typemap(out) uint8_t [256] {
  $result = PyList_New(256);
  int x;
  for(x = 0; x < 256; x++){
    PyList_SetItem($result, x, PyInt_FromLong($1[x]));
  }
}

%typemap(in) uint8_t [256] {
    uint8_t *temp = (uint8_t *)malloc(256 * sizeof(uint8_t));

    if (PyList_Check($input) && PyList_Size($input) == 256)
    {
        int x;
        for (x = 0; x < 256; x++) {
            PyObject *obj = PyList_GetItem($input, x);
            if (PyInt_Check(obj)) {
                temp[x] = (uint8_t)PyInt_AsLong(obj);
            }
            else
            {
                SWIG_exception_fail(SWIG_TypeError, "Expected list of 256 integer gamma values in $symname");
            }
        }
        $1 = &temp[0];
    }
    else
    {
        SWIG_exception_fail(SWIG_TypeError, "Expected list of 256 gamma integer values in $symname");
    }
};

// Declare functions which will be exported as anything in the ws2811.h header.
%{
#include "lib/ws2811.h"
%}

// Process ws2811.h header and export all included functions.
%include "lib/ws2811.h"

%inline %{
    uint32_t ws2811_led_get(ws2811_channel_t *channel, int lednum)
    {
        if (lednum >= channel->count)
        {
            return -1;
        }

        return channel->leds[lednum];
    }

    int ws2811_led_set(ws2811_channel_t *channel, int lednum, uint32_t color)
    {
        if (lednum >= channel->count)
        {
            return -1;
        }

        channel->leds[lednum] = color;

        return 0;
    }

    ws2811_channel_t *ws2811_channel_get(ws2811_t *ws, int channelnum)
    {
        return &ws->channel[channelnum];
    }
%}
