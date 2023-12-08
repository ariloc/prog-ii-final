#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include "../src/file_utils.h"

void test_count_lines_normal() {
    char *path = "inputs/file_utils_test/test_count_lines_normal.txt";
    assert(count_lines(path) == 8);
}

void test_count_lines_noendl() {
    char *path = "inputs/file_utils_test/test_count_lines_noendl.txt";
    assert(count_lines(path) == 4);
}

void text_count_lines_empty() {
    char *path = "inputs/file_utils_test/test_count_lines_empty.txt";
    assert(count_lines(path) == 0);
}

void test_read_lines_normal() {
    char *path = "inputs/file_utils_test/test_read_lines_normal.txt";

    int count;
    char **lines = read_lines(path, &count);
    int n = 13;

    char *expectedLines[] = {
        "cats",
        "dogs",
        "",
        "horses",
        "   other longer sentences",
        "     many sentences are right here now   ",
        "many many sentences",
        "and",
        "a ",
        "   short",
        "one",
        " ",
        ""
    };

    assert(count == n);
    for (int i = 0; i < n; i++)
        assert(strcmp(expectedLines[i],lines[i]) == 0);

    for (int i = 0; i < n; i++)
        free(lines[i]);
    free(lines);
}

void test_read_lines_noendl() {
    char *path = "inputs/file_utils_test/test_read_lines_noendl.txt";

    int count;
    char **lines = read_lines(path, &count);
    int n = 6;

    char *expectedLines[] = {
        "a  ",
        "  small\\0little",
        "",
        "   tiny   ",
        "test",
        ""
    };

    assert(count == n);
    for (int i = 0; i < n; i++)
        assert(strcmp(expectedLines[i],lines[i]) == 0);

    for (int i = 0; i < n; i++)
        free(lines[i]);
    free(lines);
}

void test_read_files_empty() {
    char *path = "inputs/file_utils_test/test_read_lines_empty.txt";

    int count;
    char **lines = read_lines(path, &count);
    int n = 0;

    assert(count == n);

    free(lines);
}

void run_file_utils_tests() {
    test_count_lines_normal();
    test_count_lines_noendl();
    test_read_lines_normal();
    test_read_lines_noendl();

    puts("file_utils.c tests passed");
}
