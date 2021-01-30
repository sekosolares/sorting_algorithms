#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct client {
	char Name[50];
	char Id[10];
	float Credit;
	char Address[100];
};

int main(int argc, char const *argv[]) {

	struct client Client1 = {0};

	strcpy(Client1.Name, "Alejandro Fernandez");
	strcpy(Client1.Id, "000000001");
	Client1.Credit = 1000000.00;
	strcpy(Client1.Address, "Calle de la amargura, Avenida 21, zona 3");

	printf("El cliente %s, con Id %s, con Direccion %s; tiene credito de %f\n", Client1.Name, Client1.Id, Client1.Address, Client1.Credit);

	return 0;
}
