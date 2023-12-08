#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "file_utils.h"

void handle_file_open_error_rwa(char *path, char mode) {
    switch(mode) {
        case 'r':
            fprintf(stderr, "There was an error reading from %s.\nFile may not exist or you may not have permission to read it.\n", path);
            break;
        case 'w':
        case 'a':
            fprintf(stderr, "There was an error writing to %s.\nCheck path exists and you have permission to write in it.\n", path);
            break;
    }
    exit(1);
}

char* concatenate_paths(char *path1, char *path2) {
    char *path = malloc(sizeof(char) * (strlen(path1) + strlen(path2) + 2));
    sprintf(path, "%s/%s", path1, path2);
    return path;
}

int count_lines(char *path) {
    FILE *fp = fopen(path,"r");
    if (fp == NULL)
        handle_file_open_error_rwa(path, 'r');

    char c, prev = -1;
    int lines = 0;
    while ((c = (char)fgetc(fp)) != EOF) {
        if (c == '\n') {
            ++lines;
        }
        prev = c;
    }
    // Count last line if it doesn't end with '\n'
    // If prev == -1, the file is empty, therefore no lines should be counted.
    if (prev != '\n' && prev != -1) {
        ++lines;
    }

    fclose(fp);

    return lines;
}

char** read_lines(char *path, int *lineCount) {
    char buf[MAX_BUF];
    
    *lineCount = count_lines(path);
    char **lines = malloc(sizeof(char*) * (*lineCount));

    FILE *fp = fopen(path, "r");
    if (fp == NULL)
        handle_file_open_error_rwa(path, 'r');

    for (int i = 0; i < *lineCount; i++) {
        fgets(buf, MAX_BUF, fp);
        
        // Count characters before \n. Note that buf may not have \n if fgets encountered EOF.
        int lineLen = strcspn(buf, "\n");
        buf[lineLen] = '\0'; // Remove \n

        char *line = malloc(sizeof(char) * (lineLen+1));
        strcpy(line,buf);

        lines[i] = line;
    }

    fclose(fp);

    return lines;
}
