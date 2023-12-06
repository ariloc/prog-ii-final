#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "parse.h"
#include "files.h"

void parse_file (FILE* input, FILE* output) {
    char c;
    char previous = 'z'; // Dummy character
    int firstInSentence = 1;
    while ((c = fgetc(input)) != EOF) {
        if (c == '.') {
            fputc('\n', output);
            firstInSentence = 1;
        }

        if (isalpha(c)) {
            if (!isalpha(previous) && !firstInSentence) fputc(' ',output);
            fputc(tolower(c), output);
            firstInSentence = 0;
        }

        previous = c;
    }

    if (!firstInSentence) 
        fputc('\n',output); // Make sure '\n' is inserted at the end
}

void sanitize_files(int n, char **inputPaths, char *outputPath) {
    FILE* output = fopen(outputPath, "w");

    for (int i = 0; i < n; i++) {
        FILE *input = fopen(inputPaths[i], "r");

        parse_file(input, output);

        fclose(input);
    }

    fclose(output);
}

void sanitize_texts(char *personName) {
    int pathCount;
    char** textPaths = get_text_paths(personName, &pathCount);

    char sanitizedFilePath[MAX_BUF];
    sprintf(sanitizedFilePath, "%s/%s.txt", INPUTS_PATH, personName);
    
    sanitize_files(pathCount, textPaths, sanitizedFilePath);

    // Free paths array
    for (int i = 0; i < pathCount; i++)
        free(textPaths[i]);
    free(textPaths);
}
