/**
 *  @file files.h
 *  @author Ariel Leonardo Fideleff
 */

#ifndef __FILES_H__

#include <stddef.h>

/**
 *  Path of a folder where texts written by people are stored.
 *  Each person's texts should be @c .txt files contained in a folder named after the person,
 *  under this path.
 *  
 *  <b>This path must point to a folder in the same directory as the executable.</b>
 */
#define TEXTS_PATH "Textos"

/**
 *  Path of the folder where the sanitized sentences from a person will be stored.
 *  The resulting files would be named after the person and have a @c .txt extension.
 *
 *  <b>This path must point to a folder in the same directory as the executable.</b>
 */
#define INPUTS_PATH "Entradas"

/**
 *  Path to a file where a list of filenames inside a directory will be written.
 *  Specifically, this file will be used to list the texts written by a person.
 *
 *  <b>Must be the name of a file to be created <i>in the same directory</i> as the executable.</b>
 *
 *  @see TEXTS_PATH
 */
#define FILES_LIST_PATH "archivos.txt"  


/**
 *  Given the name of a person, returns the path to the folder that contains all of this person's
 *  texts.
 *
 *  @param personName The name of the person (without spaces).
 *  @return A path to the folder where the person's texts should be located in.
 *  @see TEXTS_PATH
 */
char* person_texts_path(char* personName);


/**
 *  Overwrites a file list stored at @p filesListPath with a blank file. 
 *  Creates a new file at this path if it doesn't exist.
 *
 *  @param filesListPath Path of a file that contains a filename list of a folder.
 */
void reset_files_list(char *filesListPath);

/**
 *  Writes a list of the filenames in @p textsPath, to the file located at @p filesListPath.
 *  For this purpose, it runs the commands @c cd and @c ls typically present in the host's command
 *  processor, under a Linux environment.
 *  As such, no file may be written to @p filesListPath in case of failure of the commands
 *  aforementioned (i.e. any of the paths isn't accessible or doesn't exist).
 *
 *  @param textsPath Path for a directory whose filenames within it will be listed.
 *  @param filesListPath Path of a file where the filnames of @p textsPath will be written.
 */
void list_texts(char *textsPath, char *filesListPath);

/**
 *  Given a path to a directory, prepends its path to each of the @p n filenames listed in 
 *  @p filenames.
 *
 *  @param directory Path of a directory which will be appended to the beginning of the filenames.
 *  @param filenames An array of pointers, each holding a reference to a string with a filename.
 *  @param n The amount of filenames provided.
 *  @return An array of pointers, each holding a reference to a new string containing the result
 *          of the concatenation of the directory path and each of the filenames given.
 */
char** prepend_directory_to_filenames(char *directory, char **filenames, int n);


/**
 *  Returns a list of paths with each of the texts written by @p personName.
 *  These texts should be @c .txt files contained in a folder named after the person,
 *  inside the directory located at #TEXTS_PATH.
 *
 *  @param personName The name of the person (without spaces).
 *  @param pathsCount A pointer to an integer where the amount of paths returned will be stored.
 *  @return An array of pointers, each holding a reference to the path of a text written by the
 *          person, represented as a string.
 *  @see TEXTS_PATH
 */
char** get_text_paths(char *personName, int *pathsCount);

/**
 *  Returns the path of the file where the sanitized sentences from a person will be written.
 *  This file will be a @c .txt file named after the person, which will be stored inside the
 *  directory located at #INPUTS_PATH.
 *
 *  @param personName The name of the person (without spaces).
 *  @see INPUTS_PATH
 */
char* sanitized_file_path(char *personName);

#endif /* __FILES_H__ */
