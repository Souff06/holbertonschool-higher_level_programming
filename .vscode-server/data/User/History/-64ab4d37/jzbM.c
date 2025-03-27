#include "shell.h"
/**
 *find_command -
*/
char *find_command(char *args)
{
 
    int i = 0;
    char path_search[4096];
        const char *path[] = {"/bin", "/usr/bin", NULL};
	  if (access(args, X_OK) == 0)
    {
        return strdup(args);
    }
        while(path[i] != NULL)
        {
        sprintf(path_search, "%s/%s", path[i], args);
	path_search[sizeof(path_search) - 1] = '\0';
                    if (access(path_search, X_OK) == 0)
                    {
                        return strdup(path_search);
                    }
                    i++;
        }
    return NULL;
}
/**
 * _execute_command - executes a command provided by the user
 *
 * @argv: main program arguments
 * @command: array of string as command and its arguments
 * @env: environment
 *
 * Return: 0 on success, otherwise 1
 */
void execute_command(char **argv, char *command, char **env)
{
    pid_t child;
    int status;
    char *cmd = find_command(command);
    if (cmd == NULL)
    {
        printf("Commande non trouvée\n");
        if (isatty(STDIN_FILENO))
            exit(EXIT_FAILURE);
        return; // Pas besoin de libérer cmd si c'est NULL
    }
    if (argv == NULL)
    {
        perror("argv est NULL");
        free(cmd);
        return;
    }
    child = fork();
    if (child < 0)
    {
        perror("Échec du fork");
        free(cmd);
        exit(EXIT_FAILURE);
    }
    else if (child == 0)
    {
        execve(cmd, argv, env);
        perror("Échec de execve");
        exit(EXIT_FAILURE);
    }
    else
    {
        waitpid(child, &status, 0);
        free(cmd);
    }
}
