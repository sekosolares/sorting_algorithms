#include <stdio.h>
#include <stdlib.h>

#define SIZE 5
int items[SIZE], front = -1, rear = -1;

void enQueue(int value) {
	if (rear == SIZE-1)
		printf("Queue is Full, bro! I'm sorry. :( \n");
	else {
		if (front == -1)
			front = 0;
		++rear;
		items[rear] = value;
		printf("Value %d inserted successfully!\n", value);
	}
}

void deQueue() {
	if (front == -1)
		printf("Queue is Empty, mate! Sorry baby. :( \n");
	else {
		printf("Deleting value %d ...\n", items[front]);
		++front;
		if (front > rear)
			front = rear = -1;
	}
}

int main(int argc, char const *argv[]) {
	enQueue(23);
	enQueue(33);
	enQueue(2);
	enQueue(48);
	enQueue(100);
	enQueue(64);

	deQueue();
	deQueue();
	deQueue();
	deQueue();
	deQueue();
	deQueue();

	return 0;
}
