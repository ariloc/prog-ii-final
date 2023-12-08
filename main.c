#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "c/src/files.h"
#include "c/src/parse.h"
#include "c/src/file_utils.h"
#include "c/src/call_python.h"

int main(int argc, char *argv[]) {
    if (argc != 2) {
        puts("usage: ./main [person_name]");
        return 0;
    }

    char *personName = argv[1];

    sanitize_texts(personName);

    call_python_script(personName);

    return 0;
}
