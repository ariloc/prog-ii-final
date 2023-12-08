#include <stdio.h>
#include <stdlib.h>

#include "file_utils.h"
#include "call_python.h"

void call_python_script(char *personName) {
    char command[MAX_BUF];
    sprintf(command, "python3 %s %s", PYTHON_SCRIPT_NAME, personName);
    system(command);
}
