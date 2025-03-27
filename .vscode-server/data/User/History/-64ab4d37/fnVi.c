#include "shell.h"
/**
 *find_command -
 150719*/
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
#include "shell.h"
/**
 *find_command -
 150719*/
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
void execute_command(char *command) {
    int status = -1;
    pid_t pid;
    char *cmd, *argv[3] = { NULL };
    cmd = find_command(command);
    if (cmd) {
        if (access(cmd, X_OK) == 0) {
            argv[0] = cmd;
            argv[1] = command;
            pid = fork();
            if (pid == -1) {
                perror("fork");
            } else if (pid == 0) {
                execve(cmd, argv, NULL);
                perror("execve");
                exit(EXIT_FAILURE);
            } else {
                waitpid(pid, &status, 0);
            }
        }
        free(cmd);
    } else {
        fprintf(stderr, "Command not found\n");
    }
}
