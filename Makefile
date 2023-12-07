SRCDIR = c/src
BUILDDIR = c/build
TESTDIR = c/tests

TARGET = main
TEST_TARGET = $(TESTDIR)/run_tests

CC = gcc
CFLAGS = -Wall -Wshadow -Wconversion -Wextra -g

VPATH = $(BUILDDIR) $(SRCDIR) $(TESTDIR) 

.PHONY: default clean test

default: $(TARGET)
test: $(TEST_TARGET)

SOURCES = $(wildcard $(SRCDIR)/*.c)
HEADERS = $(wildcard $(SRCDIR)/*.h)
OBJECTS = $(patsubst $(SRCDIR)/%.c,$(BUILDDIR)/%.o,$(SOURCES))

TESTS = $(wildcard $(TESTDIR)/*_test.c)

MAIN_OBJ = $(BUILDDIR)/main.o
RUN_TESTS_OBJ = $(BUILDDIR)/run_tests.o

$(MAIN_OBJ) $(OBJECTS): $(BUILDDIR)/%.o: %.c $(HEADERS) | $(BUILDDIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(TARGET): $(OBJECTS) $(MAIN_OBJ)
	$(CC) $(CFLAGS) $(OBJECTS) $(MAIN_OBJ) -o $@


$(RUN_TESTS_OBJ): $(BUILDDIR)/%.o: %.c $(OBJECTS) $(TESTS) | $(BUILDDIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(TEST_TARGET): $(RUN_TESTS_OBJ) $(OBJECTS)
	$(CC) $(CFLAGS) $(RUN_TESTS_OBJ) $(OBJECTS) -o $@


$(BUILDDIR):
	mkdir $(BUILDDIR)

clean:
	rm -f $(TARGET) $(TEST_TARGET) $(BUILDDIR)/*
