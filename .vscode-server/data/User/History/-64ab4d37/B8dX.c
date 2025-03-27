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
void execute_command(char *command_line) {
    int status = -1;
    pid_t pid;
    char *argv[100];
    int argc = 0;

    char *token = strtok(command_line, " ");
    while (token != NULL) {
        argv[argc++] = token;
        token = strtok(NULL, " ");
    }
    argv[argc] = NULL;

    pid = fork();
    if (pid == -1) {
        perror("fork");
    } else if (pid == 0) {
        execvp(argv[0], argv);
        perror("execvp");
        exit(EXIT_FAILURE);
    } else {
        waitpid(pid, &status, 0);
    }
}
