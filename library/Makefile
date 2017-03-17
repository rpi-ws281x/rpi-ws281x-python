.PHONY: clean lib

SRC = lib
BUILD = lib-built
OBJECTS = $(BUILD)/ws2811.o $(BUILD)/rpihw.o $(BUILD)/pcm.o $(BUILD)/pwm.o $(BUILD)/dma.o $(BUILD)/mailbox.o
LIB = libws2811.a

all: $(BUILD) $(BUILD)/version.h $(BUILD)/$(LIB)

$(BUILD):
	mkdir -p $(BUILD)

$(BUILD)/version.h:
	cp version.h $(BUILD)/version.h

$(OBJECTS): $(BUILD)/%.o : $(SRC)/%.c
	gcc $< -o $@ -c -g -O2 -Wall -Werror -fPIC

$(BUILD)/$(LIB): $(OBJECTS)
	ar rc $@ $^
	ranlib $@

clean:
	-rm -f $(OBJECTS) $(BUILD)/$(LIB) $(BUILD)/version.h
