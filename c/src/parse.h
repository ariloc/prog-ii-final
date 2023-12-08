/**
 *  @file parse.h
 *  @author Ariel Leonardo Fideleff
 */

#ifndef __PARSE_H__

#include <stddef.h>
#include <stdio.h>

/**
 *  Given an @p input file stream and an @p output file stream, processes the contents of the first
 *  stream and <i>appends</i> them into the second one, in order to separate it into sentences under
 *  the following criteria:
 *  - Output text will only consist of lowercase letters, spaces and newlines.
 *  - Each line of the output text will correspond to a single sentence of the input file,
 *    considering sentences are separated by periods (@p '.'). Therefore, any newline 
 *    character (@p '\n') that doesn't separate two sentences will be discarded as well.
 *  - Any symbols or numbers found within the text will be discarded, including any kind of 
 *    punctuation marks.
 *  - Words of the sentence have to be separated by a single space, additional spaces will be
 *    discarded. Two words are considered distinct if there is a non-alphabetical character
 *    between them.
 *  - Each of the output lines has to end in a newline character (@p '\n').
 *
 *  @param input An input file stream to read from.
 *  @param output An output file stream where the sanitized contents of the input file will be 
 *                written.
 */
void sanitize_file(FILE* input, FILE* output);

/**
 *  Sanitizes the contents of a list of files whose paths are given, and they are combined in order
 *  into a single file at @p outputPath.
 *  
 *  @param n The amount of files to be sanitized and combined.
 *  @param inputPaths An array of pointers, each holding a reference to a string representing the
 *                    path of a file to be sanitized and combined into @p outputPath.
 *  @param outputPath Path of the file to write with the sanitized contents of the given input files.
 *  @see sanitize_file()
 */
void sanitize_files(int n, char **inputPaths, char *outputPath);

/**
 *  Sanitizes the texts written by a person by the name @p personName, and combines them into a
 *  single file at #INPUTS_PATH.
 *
 *  The texts processed by the program will be found inside a folder named after the person,
 *  under a directory located at #TEXTS_PATH.
 *
 *  @param personName The name of the person after whom a folder with texts to be sanitized has
 *                    its name (without spaces).
 *  @see get_text_paths()
 *  @see sanitized_file_path()
 */
void sanitize_texts(char *personName);

#endif
