#include <stdio.h>

#include "files_test.c"
#include "file_utils_test.c"
#include "parse_test.c"

int main() {
    run_files_tests();
    run_file_utils_tests();
    run_parse_tests();

    puts("ALL TESTS PASSED");
    
    return 0;
}
