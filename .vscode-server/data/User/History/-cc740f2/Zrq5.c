#include "main.h"

int _strlen(char *s);
/**
 * append_text_to_file - Function that creates
 * appends text at the end of a file.
 * @filename: the name of file to append
 * @text_content: the content of the file
 *
 * Return: 1 on success else -1
 */
int append_text_to_file(const char *filename, char *text_content)
{
int fd;
ssize_t readed;
if (filename == NULL)
{
return (-1);
}
fd = open(filename, O_WRONLY | O_APPEND);
if (fd == -1)
return (-1);
if (text_content != NULL)
{
readed = write(fd, text_content, _strlen(text_content));
if (readed == -1)
{
close(fd);
return (-1);
}
}
close(fd);
return (1);
}
/**
 * _strlen - Function that return the lenght of string
 *
 * @s: string to count
 *
 * Return: the lenght of string
 */
int _strlen(char *s)
{
int i = 0;
while (s[i] != '\0')
i++;
return (i);
}