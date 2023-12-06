#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "c/src/files.h"
#include "c/src/parse.h"

#define PYTHON_SCRIPT_NAME "main.py"

void call_python_script(char *personName) {
    char command[MAX_BUF];
    sprintf(command, "python3 %s %s", PYTHON_SCRIPT_NAME, personName);
    system(command);
}

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
