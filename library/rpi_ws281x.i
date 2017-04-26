// SWIG interface file to define rpi_ws281x library python wrapper.
// Author: Tony DiCola (tony@tonydicola.com), Jeremy Garff (jer@jers.net)

// Define module name rpi_ws281x.  This will actually be imported under
// the name _rpi_ws281x following the SWIG & Python conventions.
%module rpi_ws281x

// Include standard SWIG types & array support for support of uint32_t
// parameters and arrays.
%include "stdint.i"
%include "carrays.i"

%typemap(out) uint8_t * {
  $result = PyList_New(256);
  int x;
  for(x = 0; x < 256; x++){
    PyList_SetItem($result, x, PyInt_FromLong($1[x]));
  }
}

%{
static int convert_iarray(PyObject *input, uint8_t *ptr, int size) {
  int i;
  if (!PySequence_Check(input)) {
      PyErr_SetString(PyExc_TypeError,"Expecting a sequence");
      return 0;
  }
  if (PyObject_Length(input) != size) {
      PyErr_SetString(PyExc_ValueError,"Sequence size mismatch");
      return 0;
  }
  for (i =0; i < size; i++) {
      PyObject *o = PySequence_GetItem(input,i);
      if (!PyInt_Check(o)) {
         Py_XDECREF(o);
         PyErr_SetString(PyExc_ValueError,"Expecting a sequence of floats");
         return 0;
      }
      ptr[i] = PyInt_AsLong(o);
      Py_DECREF(o);
  }
  return 1;
}
%}

%typemap(in) uint8_t * {
   /* As a consequence of this malloc, I believe there's a potential memory leak
   /  which would occur if gamma is set more than once.
   /  The gamma value is only freed once at cleanup.
   /  Using a typemap is also risky here, since it would apply to all *uint8_t,
   /  this type is presently only used for the gamma table.
   */
   $1 = malloc(sizeof(uint8_t) * 256);
   if (!convert_iarray($input,$1,256)) {
      return NULL;
   }
}

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
