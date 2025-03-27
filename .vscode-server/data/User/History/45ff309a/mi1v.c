#include "shell.h"

/**
 * split_string - Splits an input string into an array of arguments.
 * @input: The user input string to split.
 * @command: The command to split.
 * Return: An array of split arguments, or NULL on failure.
 */
char **split_string(char *input, char **command)
{
    char **args = NULL, *token;
    size_t i = 0, buffer = 2;

    token = strtok(input, " \n\t");
    if (!token) return NULL;

    *command = strdup(token);
    if (!(*command))
    { 
        perror("Failed to allocate command");
        return NULL;
    }

    args = malloc(buffer * sizeof(char *));
    if (!args)
    { 
        perror("Failed to allocate args");
        free(*command);
        return NULL;
    }

    while (token)
    {
        if (i >= buffer - 1)
        {
            buffer *= 2;
            args = realloc(args, buffer * sizeof(char *));
            if (!args)
            { 
                perror("Failed to reallocate args");
                free(*command);
                return NULL;
            }
        }
        token = strtok(NULL, " \n\t");
        args[i++] = token ? strdup(token) : NULL;
        if (token && !args[i - 1])
        {
            while (i--)
                free(args[i]);
            free(args);
            free(*command);
            return NULL;
        }
    }
    args[i] = NULL;
    return args;
}
