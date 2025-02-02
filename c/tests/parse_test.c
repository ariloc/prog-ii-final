#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include <sys/stat.h>

#include "../src/parse.h"

// Helper functions
void compare_files(char *outputPath, char *expectedPath) {
    FILE *output = fopen(outputPath, "r");
    FILE *expected = fopen(expectedPath, "r");

    char a,b;
    do {
        a = (char)fgetc(output);
        b = (char)fgetc(expected);

        // If any reaches EOF, both should be EOF, otherwise one is shorter in length.
        assert(a == b);             
    } while (a != EOF && b != EOF);
    
    fclose(output);
    fclose(expected);
}

void create_tmp() {
    mkdir("./tmp", 0777);
}

void file_comparing_test (char* inputPath, char* outputPath, char *expectedPath) {
    create_tmp();

    FILE *input = fopen(inputPath, "r");
    FILE *output = fopen(outputPath, "w");

    sanitize_file(input, output);
    fclose(input);
    fclose(output);

    compare_files(outputPath, expectedPath);
}

// Tests
void test_parse_file_1() {
    char *inputPath = "inputs/parse_test/test_parse_file_1.txt";
    char *outputPath = "tmp/test_parse_file_1.out";
    char *expectedPath = "expected/parse_test/test_parse_file_1.txt";
    file_comparing_test(inputPath, outputPath, expectedPath);
}

void test_parse_file_2() {
    char *inputPath = "inputs/parse_test/test_parse_file_2.txt";
    char *outputPath = "tmp/test_parse_file_2.out";
    char *expectedPath = "expected/parse_test/test_parse_file_2.txt";
    file_comparing_test(inputPath, outputPath, expectedPath);
}

void test_parse_file_3() {
    char *inputPath = "inputs/parse_test/test_parse_file_3.txt";
    char *outputPath = "tmp/test_parse_file_3.out";
    char *expectedPath = "expected/parse_test/test_parse_file_3.txt";
    file_comparing_test(inputPath, outputPath, expectedPath);
}

void test_parse_file_4() {
    char *inputPath = "inputs/parse_test/test_parse_file_4.txt";
    char *outputPath = "tmp/test_parse_file_4.out";
    char *expectedPath = "expected/parse_test/test_parse_file_4.txt";
    file_comparing_test(inputPath, outputPath, expectedPath);
}

void test_parse_file_5() {
    char *inputPath = "inputs/parse_test/test_parse_file_5.txt";
    char *outputPath = "tmp/test_parse_file_5.out";
    char *expectedPath = "expected/parse_test/test_parse_file_5.txt";
    file_comparing_test(inputPath, outputPath, expectedPath);
}

void test_parse_file_6() {
    char *inputPath = "inputs/parse_test/test_parse_file_6.txt";
    char *outputPath = "tmp/test_parse_file_6.out";
    char *expectedPath = "expected/parse_test/test_parse_file_6.txt";
    file_comparing_test(inputPath, outputPath, expectedPath);
}

// Run all tests
void run_parse_tests() {
    test_parse_file_1();
    test_parse_file_2();
    test_parse_file_3();
    test_parse_file_4();
    test_parse_file_5();
    test_parse_file_6();

    puts("parse.c tests passed");
}
