# Movie Theater Admission Control System

## 1. Identify the Components

### 1.1 Inputs

The system requires the following inputs:

- Customer Age
- Accompanied by Adult (Yes/No)
- Valid Ticket (Yes/No)

### 1.2 Process

The system checks whether:

1. The customer is 13 years old or older **OR** is accompanied by an adult.
2. The customer has a valid ticket.
3. If both conditions are satisfied, entry is approved; otherwise, entry is denied.

### 1.3 Output

The system produces one of the following outputs:

- **ENTRY APPROVED**
- **ENTRY DENIED**

---

## 2. Design the Algorithm

### 2.1 Algorithm Diagram (Flowchart Logic)

```text
START
   |
   V
Input Age
Input Adult Status
Input Ticket Status
   |
   V
(Age >= 13 OR Adult Present)?
   |
  YES
   |
Valid Ticket?
   |
YES ------> ENTRY APPROVED
   |
NO
   |
ENTRY DENIED

If first condition = NO
   |
ENTRY DENIED
   |
END
```

---

### 2.2 Truth Table

| Age ≥ 13 | Adult Present | Valid Ticket | Entry Allowed |
|-----------|---------------|-------------|--------------|
| No | No | No | No |
| No | No | Yes | No |
| No | Yes | No | No |
| No | Yes | Yes | Yes |
| Yes | No | No | No |
| Yes | No | Yes | Yes |
| Yes | Yes | No | No |
| Yes | Yes | Yes | Yes |

---

### 2.3 Step-by-Step Algorithm

1. Start the program.
2. Input the customer's age.
3. Input whether the customer is accompanied by an adult.
4. Input whether the customer has a valid ticket.
5. Check if the customer is at least 13 years old OR accompanied by an adult.
6. Check if the customer has a valid ticket.
7. If both requirements are met, display **ENTRY APPROVED**.
8. Otherwise, display **ENTRY DENIED**.
9. End the program.

---

### 2.4 Pseudocode

```text
START

INPUT age
INPUT accompaniedByAdult
INPUT validTicket

IF ((age >= 13 OR accompaniedByAdult = TRUE)
    AND validTicket = TRUE)
THEN
    DISPLAY "ENTRY APPROVED"
ELSE
    DISPLAY "ENTRY DENIED"
END IF

END
```

---

## 3. Evaluate Expression

### 3.1 Test with Input Samples

| Age | Adult Present | Valid Ticket | Result |
|------|--------------|-------------|---------|
| 15 | No | Yes | ENTRY APPROVED |
| 10 | Yes | Yes | ENTRY APPROVED |
| 10 | No | Yes | ENTRY DENIED |
| 16 | No | No | ENTRY DENIED |

---

## 4. Git Update

After completing the activity:

```bash
git add .
git commit -m "Completed movie theater admission algorithm activity"
git push origin main
```

---
### Logical Expression

```text
(Age >= 13 OR AccompaniedByAdult)
AND
ValidTicket
```