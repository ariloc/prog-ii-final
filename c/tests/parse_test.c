#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "../src/parse.h"

void compare_files(char *outputPath, char *expectedPath) {
    FILE *output = fopen(outputPath, "r");
    FILE *expected = fopen(expectedPath, "r");

    char a,b;
    do {
        a = fgetc(output);
        b = fgetc(expected);

        // If any reaches EOF, both should be EOF, otherwise one is shorter in length.
        assert(a == b);             
    } while (a != EOF && b != EOF);
    
    fclose(output);
    fclose(expected);
}

void test_parse_file_1() {
    char *inputPath = "inputs/parse_test/test_parse_file_1.txt";
    char *outputPath = "tmp/test_parse_file_1.out";
    char *expectedPath = "expected/parse_test/test_parse_file_1.txt";

    FILE *input = fopen(inputPath, "r");
    FILE *output = fopen(outputPath, "w");

    parse_file(input, output);
    fclose(input);
    fclose(output);

    compare_files(outputPath, expectedPath);
}

void run_parse_tests() {
    test_parse_file_1();

    puts("Parse tests passed");
}
