# Written HW

This is the first and only written HW for CSEE 4121. Please either type or scan your solutions to these problems. Submit your clear written solutions in PDF format on Gradescope (more details at the bottom). 

Due Date: **March 4, 2020, 11:59 AM** (1 minute before noon!)

# Question 1

Suppose that you are hired to design a database system for a university. We have the following data schema:
```
Students(sid: integer, sname: string, age: real, year: real, gpa: real, majordept: string)
Classrooms(clid: integer, cbid: integer, csize: integer)
Courses(crid: integer, clid: integer, crsize: integer, crdept: string)
Buildings(bid: integer, bname: string, bnum_classrms: integer) 
```
Describe what the following SQL queries look to do in plain English:

i)
```
SELECT S.name, S.age 
FROM Students as S
WHERE S.year > 2
```

ii)
```
SELECT  Cr.crsize
FROM Courses as Cr
WHERE (Cr.crid = 3);
```

iii)
```
SELECT S.sname
FROM Students as S
WHERE (S.gpa > 3 AND S.majordept = “Art History”);
```

iv)
```
SELECT C.clid, C.csize
FROM Classrooms C
WHERE C.clid IN 	( SELECT Cr.clid 
			FROM Courses Cr
			WHERE Cr.crdept = “Art History”);
```

v)
```
SELECT S.sname
FROM Students S
WHERE EXISTS 	( SELECT *
			FROM Courses Cr
			WHERE S.majordept = Cr.crdept  AND Cr.crsize <= 100);
```

vi)
```
SELECT Cr.crid
FROM Courses Cr
WHERE Cr.clid NOT IN 	(SELECT C.clid
			      	FROM Classroom C
				WHERE C.cbid 		IN (SELECT B.bid
								FROM Buildings B
								WHERE B.bname = “Mudd”) );
```

# Question 2

Suppose we begin with two tables, ***Product*** and ***Purchase***.

***Product***:

| PName        | Price          | DiscountPrice  | Category | Manufacturer |
| ------------- |:-------------:| -----:|:-----------:|:------------:|
| Gizmo | $19.99 | $16.99 | Gadgets | GWorks |
| PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks |
| SingleTouch | $149.99 | $144.99 | Photography | Canon |
| MultiTouch | $203.99 | $199.99 | Household | Hitachi |

***Purchase***:

| ProdName        | Store          | 
| ------------- |:-------------:|
| Gizmo | Wiz |
| PowerGizmo | Ritz | 
| Camera | Wiz | 

For each of the following queries, draw the table that would be a result of the query.

i) 
```
SELECT *
FROM Product
WHERE DiscountPrice <= 100;
```

ii) 
```
SELECT *
FROM Purchase
LIMIT 3;
``` 

iii) 
```
SELECT * 
FROM Product
ORDER BY DiscountPrice
```

iv) 
```
SELECT SUM(DiscountPrice - Price)
FROM Product
WHERE Category = ‘Gadgets’
```

v) 
```
SELECT *
FROM Product
JOIN Purchase ON Product.PName = Purchase.ProdName
```

vi) 
```
SELECT *
FROM Purchase
JOIN Product ON Purchase.ProdName = Product.PName
```

vii)
```
SELECT *
FROM Purchase
LEFT OUTER JOIN Product ON Purchase.ProdName = Product.PName
```

# Question 3

Perform the following operations in set algebra:

Assume A and B are both sets, C and D are both multisets.

A = {2, 1, 3}, B = {3, 1, 4}, C = {2, 1, 3, 1}, D = {1, x, y}.

1. What is A U B, where U is union? <br/>
2. What is B U A? <br/>
3. What is D U C? <br/>
4. What is C * D, where * is cross-product? <br/>

# Question 4

Suppose we're given a table ***Product***:

|pid| PName        | Price          | DiscountPrice  | Category | Manufacturer |
|----| ------------- |:-------------:| -----:|:-----------:|:------------:|
| 18 | Gizmo | $19.99 | $16.99 | Gadgets | GWorks |
| 70 | PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks |
| 32 | SingleTouch | $149.99 | $144.99 | Photography | Canon |
| 67 | MultiTouch | $203.99 | $199.99 | Household | Hitachi |

Let S1 consist of the first two tuples of ***Product***, S2 be the last two tuples of ***Product***, and S is the whole instance. Show the results of the following operations.

1. Left outer join of S with itself, with the join condition being pid=pid.
2. Right outer join of S with itself, with the join condition being pid=pid.
3. Full outer join of S with itself, with the join condition being pid=pid.
4. Left outer join of S1 with S2, with the join condition being pid=pid.
5. Right outer join of S1 with S2, with the join condition being pid=pid.
6. Full outer join of S1 with S2, with the join condition being pid=pid.

# Question 5

Consider tables or relations R and S where R has n tuples and S has m tuples, with n >= m > 0. Give the minimum and maximum number of tuples that can be a result of the following expressions.

1. R U S, where U is union.
2. R intersect S.
3. R inner join S.
4. S full outer join S.
5. R - S, where - is set difference, defined as the set of elements in R that do not belong to S.
6. S - R, where - is set difference, defined as the set of elements in S that do not belong to R.

# Question 6: ACID

From the following scenarios, consider whether the scenario is a failure of 1) atomicity, 2) consistency, 3) isolation or 4) durability (the letters in ACID). Choose one failure that bests fits the scenario. Provide a short (<= 1 sentence) explanation of why. 

i) 

The file system has declared that a file is written. But because of hardware failure in the disk controller, the writes disappeared and were never written to disk.

ii) 

We want to write a value to a 16-byte value to memory. However, because of a power outage right when we attempt to write the value, we only manage to write to the first 8-bytes.

iii) 

We are working on a database for a bank. We have an explicit constraint that, in the database, all clients must have an account balance of at minimum $100. However, because of a bug in the implementation of the database, the constraint is not enforced in a transaction and we have an account with a balance of $80. 

iv) 

Two users are accessing the same variable at around the same time. The starting value is 15. The first user, user A, wants to increment the value by 10. The other user, user B, wants to decrement the value by 5. User A reads the starting value, and before committing his change, user B comes in and reads the starting value and decrements the value and sets the value to 10. User A does not notice this and updates the value to 25 anyway.

v) 

There is an explicit constraint on a database that the total value of credits in the system must sum up to 1000. A user sends a transaction that is in explicit violation of the constraint and would lead to the total value of credits in the system increasing to 1100. Nonetheless, the database accepts the transaction.

vi) 

A user tries to rename a file in their shared folder (e.g., Dropbox or Google Drive). The file sharing program splits the file rename into two steps: it first copies a version of the file with a new name, and then deletes the old version. After the first step of the rename process, the file sharing program crashes. Now the user has two versions of the folder: one with the old name, and one with a new name. 

vii) 

We are working on a big matrix operation. We store the matrix in memory. This operation is mutable, which means that the matrix is being changed during the operation. After finishing the operation, we hope to write to the hard disk. However, because of a malfunction on the disk hand, it never gets written to the disk. Next time, we want to load the changed matrix, the file system cannot retrieve the matrix and it gives us an error. 

viii) 

Two users are trying to edit the same sentence on a Google Doc: "I love Rocknroll". The first user tries to edit the sentence to: "I love 80's Rocknroll". The second user is trying to write: "I love Guns N Roses". Since they are editing simultaneously, Google Doc produces the following sentence: "I love 80's Guns N Roses".

# Question 7

We have two systems in charge of running a batch of jobs. System A runs 40 jobs in 30 seconds, and System B runs the same 40 jobs in 35 seconds.
1. What is the throughput of the system on the running of the jobs in jobs/sec?
2. Which system performs better? By how much?
3. Suppose that we have discovered a performance issue on System B and fixed it. We now have the ability to run the same 40 jobs in 25 seconds. What is the speedup of the improved System B over the original?
4. What is the average latency of the jobs in System A (choose the right answer and explain why):

	A. 30 seconds

	B. 0.75 seconds

	C. 1.3 seconds

	D. The average latency is unknown

# Question 8 - Amdahl's Law

Your boss asks you to improve the performance of a system. Before you begin optimizing the system, we want to guess how much improvement we can get on performance time. For each of the following optimizations, figure out the speedup.

1. Improve the GPU compilation software used 50% of the time by 10%
2. Improve the memory pipeline used 5% of the time by 10x
3. Improve the speed of I/O from disk used 15% of the time by 10x
4. Which of these is therefore the optimization that you should spend your time on, which gives the most speedup improvement?

# Question 9

We first describe the memory hierarchy. Suppose that we have a latency to the CPU cache of 5ns, latency to memory of 25ns, and latency to flash of 1ms. For each of the following situations (where all we consider are random reads from a memory address), calculate the average latency.

1. Hit CPU cache 80% of reads and have to go to memory for the remaining 20% of reads.
2. Hit CPU cache 95% of reads but have to go to flash for the remaining 5% of reads.
3. Hit memory 85% of reads but have to go to flash for the remaining 15% of reads.

# Question 10

A computer systems is using a magnetic disk (hard disk) as storage. Suppose that the hard disk has a capacity of 300 GB, an RPM (rotations per minute) of 10000, an average seek of 4ms, and a max transfer rate of 100MB/s. 

1. First calculate T_{rot}, the time per rotation. 
2. Calculate T_{transfer}, the time taken to transfer a 4kB page.
3. Assuming that we are reading from random positions on disk, what is the T_{I/O} or time to perform one I/O operation of a 4kB read? What is thus the rate of I/O, under a random workload, in MB/sec?
4. Assume that we are reading 4kB pages sequentially on disk. What is different about the necessary I/Os to accomplish this task? What is thus the rate of I/O, under a sequential workload, file in MB/sec? What is the time taken to transfer a 125MB file. 

# Question 11

Suppose that we have a rack that we are using to host our website. The rack consists of 42U. Assume that each network switch uses 10 watts and that each server uses 200 watts. Suppose that we have a Total Facility Power of 6000. What is the PUE of the following configurations?

1. 10 1U network switches with 16 2U servers.
2. 4 1U network switches with 19 2U servers.
3. 21 2U servers. 

# Question 12

Suppose we have an excerpt of a write-ahead log of table ***Payroll*** as:

| LSN | Prev LSN | Tx ID | Type | Loc | Old Val | New Val | 
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| 400 | 399 | 60 | UPDATE | A.Salary | 94 | 99 |
| 401 | 0 | 68 | BEGIN | null | null | null |
| 402 | 400 | 60 | COMMIT | null | null | null |
| 403 | 401 | 68 | UPDATE | E.Salary | 17.5 | 35 | 
| 404 | 0 | 69 | BEGIN | null | null | null |
| 405 | 403 | 68 | UPDATE | F.Salary | 17.5 | 35 |
| 406 | 405 | 68 | COMMIT | null | null | null |
| 407 | 404 | 69 | UPDATE | F.Salary | 35 | 40 | 
| 408 | 392 | 62 | UPDATE | B.Salary | 103 | 109 | 

where each transaction has a unique transaction id (Tx ID) and each log entry has a log sequence number (LSN). 

Assume all transactions with Tx ID below 60 has been committed and the table ***Payroll*** at the time right before log 400 is: 

| Name | Title | Salary |
| :---: | :---: | :---: |
| A | Professor | 94 |
| B | Professor | 103 |
| C | Staff | 62 |
| D | Staff | 58 |
| E | Student | 17.5 | 
| F | Student | 17.5

Show all records that has been updated in the database at the following time:

1. All logs before and including 404 are applied.
2. All logs before and including 406 are applied.
3. All logs before and including 408 are applied.

For example, a record can be represented as (A, Professor, 94).

# Question 13

Consider a database with objects X and Y and assume that there are two transactions T1 and T2. T1 first reads X and Y and then writes object Y. T2 reads objects X and Y and then writes objects X and Y.

a.
| T1 | T2 |
| :---: | :---: |
| R(A) |     |
|      | R(A)  |
|      | W(A)  |
|  	| Commit |
| R(A) |       |

b. 
| T1 | T2 |
| :---: | :---: |
| R(A)  |   |
|       |  R(A) |
| W(A)  |  |
| R(A)  |   |
| W(A)  |  |
| R(A)  |   |
| Commit |  |
|	| R(A) |


c.
| T1 | T2 |
| :---: | :---: |
| R(A)  |   |
| W(A)  | |
|   | R(A) |
|   | W(A)  |
|   | Commit |
| R(B) |  |
| W(B)  |    |
| Commit |  |

d.
| T1 | T2 |
| :---: | :---: |
| W(A)  |   |
|  W(C) | |
|    | W(A) |
|   | W(B)  |
|   | Commit |
| W(B) |  |
| Commit | |

1. For each of the above schedules, which one is
a. a read-write conflict
b. a write-read conflict
c. a write-write conflict
d. a schedule without a conflict
2. For each of the above schedules, show that Strict 2PL disallows these schedules.
3. Why is there no such thing as a read-read conflict?

# Question 14

Consider two transactions T1 and T2 in a database with objects X and Y. T1 reads and writes X then reads and writes Y. T2 first reads X and Y and then writes X and Y.

1. Give an example schedule that is not serializable. Explain why your schedule is not serializable.
2. Show that strict 2PL disallows this schedule. Analyze whether deadlock is possible. 
3. Explain how deadlock is handled.

# Question 15

As transaction conflicts are common in the case of concurrency updates, Jerry Mouse thinks about handling conflicts by splitting a transaction into several parts: the splitted parts altogether produce the same and consistent updates and outputs as the original intergrated transactions, but each requires less locks.

Tell Jerry whether the following splitting method works or not and explain him the reason.

 ”Suppose transaction T accesses object X and Y, and any other transaction S accesses at most one of X or Y and nothing else. Therefore, T can be splitted into two parts, one of which accesses X and the other accesses Y.” 

# Question 16

A database is usually replicated on multiple sites for better performance. Suppose a transaction executing from a cellphone visits different replicas and reads and writes (parts of) the database.

Design a simple protocol whereby a transaction can read globally-consistent data from the database replica “nearest” to it. In particular, what should a reading transaction lock? what should a writing transaction lock?

Will your transaction lead to deadlocks? If so, how can you avoid it?

## How to Submit

Submit your solutions as PDF on **Gradescope** to **Written HW1**.

Once you click submit, please enter the file in the submission box like below:
![alt text](pics/upload1.png)

Note that after submitting, you have to select the pages that correspond to the solutions. So if your solution to Q3 is on page 1, select the page and assign it to Q3. See the image below on how to upload. 

![alt text](pics/HowToUpload.png)
