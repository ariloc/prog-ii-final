TARGET = main
SRCDIR = c/src
CC = gcc
CFLAGS = -Wall

VPATH = $(SRCDIR)

.PHONY: default clean

default: $(TARGET)

OBJECTS = main.o files.o parse.o
HEADERS = files.h parse.h

%.o: %.c $(HEADERS)
	$(CC) $(CFLAGS) -c $< -o $@

$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) $(OBJECTS) -o $@

clean:
	rm $(TARGET) $(OBJECTS)
