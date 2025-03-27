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
void execute_command(char *command) {
    int status = -1;
    pid_t pid;
    char *cmd = find_command(command);

    if (cmd) {
        pid = fork();
        if (pid == -1) {
            perror("fork");
        } else if (pid == 0) {
            execl(cmd, command, NULL);
            perror("execl");
            free(cmd);
            exit(EXIT_FAILURE);
        } else {
            waitpid(pid, &status, 0);
        }
        free(cmd);
    } else {
        fprintf(stderr, "Command not found\n");
    }
}

void execute_command_line(char *command_line) {
    char *token = strtok(command_line, " ");
    while (token != NULL) {
        execute_single_command(token);
        token = strtok(NULL, " ");
    }
}
