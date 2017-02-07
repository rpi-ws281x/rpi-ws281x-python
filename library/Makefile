.PHONY: clean lib

BUILD = lib
OBJECTS = $(BUILD)/ws2811.o $(BUILD)/rpihw.o $(BUILD)/pcm.o $(BUILD)/pwm.o $(BUILD)/dma.o $(BUILD)/mailbox.o
LIB = libws2811.a

all: $(BUILD)/version.h $(BUILD)/$(LIB)

$(BUILD)/version.h:
	cp version.h $(BUILD)/version.h

$(OBJECTS): $(BUILD)/%.o : $(BUILD)/%.c
	gcc $< -o $@ -c -g -O2 -Wall -Werror -fPIC

$(BUILD)/$(LIB): $(OBJECTS)
	ar rc $@ $^
	ranlib $@

clean:
	-rm -f $(OBJECTS) $(BUILD)/$(LIB) $(BUILD)/version.h
