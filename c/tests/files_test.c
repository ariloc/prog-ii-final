#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <stdlib.h>

#include "../src/files.h"

// Tests
void test_prepend_directory_to_filenames_1() {
    char *directoryPath = "this/is a/test/path";
    char *filenames[] = {
        "hola.txt",
        "hello_world.txt",
        "_normal_text_.txt",
        "a.txt",
        "file",
        "a",
        "a new name.txt",
        "another new name .txt",
        "the last of the names .txt.txt"
    };
    int n = 9;

    char *expectedPaths[] = {
        "this/is a/test/path/hola.txt",
        "this/is a/test/path/hello_world.txt",
        "this/is a/test/path/_normal_text_.txt",
        "this/is a/test/path/a.txt",
        "this/is a/test/path/file",
        "this/is a/test/path/a",
        "this/is a/test/path/a new name.txt",
        "this/is a/test/path/another new name .txt",
        "this/is a/test/path/the last of the names .txt.txt"
    };

    char **paths = prepend_directory_to_filenames(directoryPath, filenames, n);

    for (int i = 0; i < n; i++)
        assert(strcmp(paths[i], expectedPaths[i]) == 0);
    
    for (int i = 0; i < n; i++)
        free(paths[i]);
    free(paths);
}

void test_prepend_directory_to_filenames_2() {
    char *directoryPath = "./hola/mundo/";
    char *filenames[] = {
        "test1.txt",
        "test2_3.txt",
        "test test.txt",
        "a"
    };
    int n = 4;

    char *expectedPaths[] = {
        "./hola/mundo//test1.txt",      // Still valid paths, '//' intended behavior
        "./hola/mundo//test2_3.txt",
        "./hola/mundo//test test.txt",
        "./hola/mundo//a"
    };

    char **paths = prepend_directory_to_filenames(directoryPath, filenames, n);

    for (int i = 0; i < n; i++)
        assert(strcmp(paths[i], expectedPaths[i]) == 0);

    for (int i = 0; i < n; i++)
        free(paths[i]);
    free(paths);
}

// Run all tests
void run_files_tests() {
    test_prepend_directory_to_filenames_1();
    test_prepend_directory_to_filenames_2();

    puts("files.c tests passed");
}
