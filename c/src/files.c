#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "files.h"

char* person_texts_path(char* personName) {
    char* path = malloc(sizeof(char) * (strlen(personName) + strlen(TEXTS_PATH) + 1));
    sprintf(path, "%s/%s", TEXTS_PATH, personName);
    return path;
}

void list_texts(char *personName, char *filesListPath) {
    char command[MAX_BUF];
    sprintf(command, "cd %s/%s && ls > ../../%s", TEXTS_PATH, personName, filesListPath);
    system(command);
}

int count_lines(char *path) {
    FILE *fp = fopen(path,"r");

    char c, prev;
    int lines = 0;
    while ((c = fgetc(fp)) != EOF) {
        if (c == '\n') {
            ++lines;
        }
        prev = c;
    }
    if (prev != '\n') { // Count last line if it doesn't end with '\n'
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

    for (int i = 0; i < *lineCount; i++) {
        fgets(buf, MAX_BUF, fp);
        
        // Count characters before \n. Note that buf may not have \n if fgets encountered EOF.
        int lineLen = strcspn(buf, "\n");
        buf[lineLen] = '\0'; // Remove \n

        char *line = malloc(sizeof(char)*(lineLen+1));
        strcpy(line,buf);

        lines[i] = line;
    }

    fclose(fp);

    return lines;
}

char** append_directory_to_filenames(char *directory, char **filenames, int n) {
    char buf[MAX_BUF];
    char **paths = malloc(sizeof(char*) * n);

    for (int i = 0; i < n; i++) {
        sprintf(buf, "%s/%s", directory, filenames[i]);

        char *path = malloc(sizeof(char)*(strlen(buf)+1));
        strcpy(path,buf);

        paths[i] = path;
    }

    return paths;
}

char** get_text_paths(char* personName, int *pathsCount) {
    list_texts(personName, FILES_LIST_PATH);

    int fileCount;
    char **filenames = read_lines(FILES_LIST_PATH, &fileCount);

    char *textsPath = person_texts_path(personName);
    char **paths = append_directory_to_filenames(textsPath, filenames, fileCount);

    *pathsCount = fileCount;

    for (int i = 0; i < fileCount; i++)
        free(filenames[i]);
    free(filenames);
    free(textsPath);

    return paths;
}
