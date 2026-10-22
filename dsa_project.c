#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Patient structure
struct Patient {
    char name[50];
    int age;
    int priority;  // Lower = more critical
    struct Patient* next;
};

struct Patient* front = NULL;

// Function to create new patient
struct Patient* newPatient(char* name, int age, int priority) {
    struct Patient* temp = (struct Patient*)malloc(sizeof(struct Patient));
    strcpy(temp->name, name);
    temp->age = age;
    temp->priority = priority;
    temp->next = NULL;
    return temp;
}

// Add patient in ascending priority order
void addPatient(char* name, int age, int priority) {
    struct Patient* temp = newPatient(name, age, priority);

    // if queue empty OR new patient has lower priority than front
    if (front == NULL || priority < front->priority) {
        temp->next = front;
        front = temp;
    } else {
        struct Patient* start = front;
        while (start->next != NULL && start->next->priority <= priority) {
            start = start->next;
        }
        temp->next = start->next;
        start->next = temp;
    }
    printf("✅ Patient %s (age %d) added with priority %d\n", name, age, priority);
}

// Treat (remove) lowest priority value patient (most critical)
void treatPatient() {
    if (front == NULL) {
        printf("⚠️ No patients waiting.\n");
        return;
    }
    struct Patient* temp = front;
    printf("🩺 Treating patient: %s (age %d, priority %d)\n", temp->name, temp->age, temp->priority);
    front = front->next;
    free(temp);
}

// Display patients in queue
void displayPatients() {
    if (front == NULL) {
        printf("⚠️ No patients waiting.\n");
        return;
    }
    printf("\n--- 🏥 Patient Queue (Lowest Priority First) ---\n");
    struct Patient* temp = front;
    while (temp != NULL) {
        printf("Name: %-10s | Age: %2d | Priority: %d\n", temp->name, temp->age, temp->priority);
        temp = temp->next;
    }
    printf("-----------------------------------------------\n");
}

// Menu-driven program
int main() {
    int choice, age, priority;
    char name[50];

    while (1) {
        printf("\n====== Hospital Patient Management System (Ascending PQ) ======\n");
        printf("1. Add Patient\n");
        printf("2. Treat Patient\n");
        printf("3. Display Patients\n");
        printf("4. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter Patient Name: ");
                scanf("%s", name);
                printf("Enter Age: ");
                scanf("%d", &age);
                printf("Enter Priority (1=Critical, 5=Normal): ");
                scanf("%d", &priority);
                addPatient(name, age, priority);
                break;
            case 2:
                treatPatient();
                break;
            case 3:
                displayPatients();
                break;
            case 4:
                printf("Exiting... Goodbye! 👋\n");
                exit(0);
            default:
                printf("⚠️ Invalid choice. Try again.\n");
        }
    }
    return 0;
}