/**
 *  @file call_python.h
 *  @author Ariel Leonardo Fideleff
 */

#ifndef __CALL_PYTHON_H__

#include <stddef.h>

/**
 *  Name of the python script that completes sentences with missing words based on the input generated
 *  by this program.
 */
#define PYTHON_SCRIPT_NAME "main.py"

/**
 *  Call the python script named as #PYTHON_SCRIPT_NAME with @p personName as an argument, in order
 *  to complete a list of sentences with a missing word written by a person.
 *
 *  The script will use the sanitized output file generated by this program to complete the sentences.
 *
 *  @param personName The name of the person whose sentences with missing words will be completed by
 *                    the python script.
 *  @see PYTHON_SCRIPT_NAME
 */
void call_python_script(char *personName);

#endif /* __CALL_PYTHON_H__ */