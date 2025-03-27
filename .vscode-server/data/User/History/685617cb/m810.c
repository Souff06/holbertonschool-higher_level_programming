#include "main.h"
/**
 * read_textfile - Function that reads a text file
 * and prints it to the POSIX standard output.
 * @filename: the name of file to read
 * @letters: the number of letters to read
 *
 * Return: number of byte to read and print
 */
ssize_t read_textfile(const char *filename, size_t letters)
{
int fd;
ssize_t letters_readed;
char *text = malloc(sizeof(char *) * letters);
if ((filename == NULL) || (letters == 0))
{
return (0);
}
fd = open(filename, O_RDONLY);
if (fd == -1)
return (0);
letters_readed = read(fd, text, letters);
write(STDOUT_FILENO, text, letters_readed);
close(fd);
return (letters_readed);
}
