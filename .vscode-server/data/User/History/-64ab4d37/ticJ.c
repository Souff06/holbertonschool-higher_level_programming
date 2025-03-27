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

    // Création d'un tableau pour stocker les arguments de la ligne de commande
    char *argv[100]; // Supposons que nous ayons un maximum de 100 arguments
    int argc = 0;

    // Découpage de la ligne de commande en tokens
    char *token = strtok(command_line, " ");
    while (token != NULL) {
        // Stockage de chaque token dans le tableau d'arguments
        argv[argc++] = token;
        token = strtok(NULL, " ");
    }
    argv[argc] = NULL; // Assurez-vous que le dernier élément du tableau est NULL

    pid = fork();
    if (pid == -1) {
        perror("fork");
    } else if (pid == 0) {
        // Exécution de la ligne de commande avec tous ses arguments
        execvp(argv[0], argv);
        // Si execvp échoue, afficher une erreur et quitter le processus enfant
        perror("execvp");
        exit(EXIT_FAILURE);
    } else {
        // Attendre la fin de l'exécution du processus enfant dans le processus parent
        waitpid(pid, &status, 0);
    }
}
