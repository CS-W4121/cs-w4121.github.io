---
layout: page
permalink: /writtensols
published: false
---

# Written HW Solutions

# Question 1

Suppose that you are hired to design a database system for a university. We have the following data schema:
```
Students(sid: integer, sname: string, age: real, year: real, gpa: real, majordept: string)
Classrooms(clid: integer, cbid: integer, csize: integer)
Courses(crid: integer, clid: integer, crsize: integer, crdept: string)
Buildings(bid: integer, bname: string, bnum_classrms: integer) 
```
Describe what the following SQL queries look to do in plain English:

------------

**Solutions**

1. Returns the name and age of the students who are above the second year of university. 
2. Returns the sizes of the courses whose course id is 3.
3. Returns the names of the students who have greater than 3 GPA and who major in Art History.
4. Returns the classroom id and the sizes of the classrooms where Art History courses are held.
5. Returns the students names that major in a subject which have courses of no more than 100 students.
6. Returns the course id for courses that are not held in Mudd.

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

------------

**Solutions**

i)

| PName        | Price          | DiscountPrice  | Category | Manufacturer |
| ------------- |:-------------:| -----:|:-----------:|:------------:|
| Gizmo | $19.99 | $16.99 | Gadgets | GWorks |
| PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks |

ii)

| ProdName        | Store          | 
| ------------- |:-------------:|
| Gizmo | Wiz |
| PowerGizmo | Ritz | 
| Camera | Wiz | 

iii)

| PName        | Price          | DiscountPrice  | Category | Manufacturer |
| ------------- |:-------------:| -----:|:-----------:|:------------:|
| Gizmo | $19.99 | $16.99 | Gadgets | GWorks |
| PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks |
| SingleTouch | $149.99 | $144.99 | Photography | Canon |
| MultiTouch | $203.99 | $199.99 | Household | Hitachi |

iv) 

|SUM(DiscountPrice - Price)|
|-------|
|-7|

<b> Note that any subset of the following tables, where duplicates are merged, count for full credit </b>

v)
| PName        | Price          | DiscountPrice  | Category | Manufacturer | ProdName | Store |
|:-------------:|:-------------:|:-----:|:-----------:|:------------:|:------------:|:------------:|
| Gizmo        | $19.99          | $16.99  | Gadgets | GWorks | Gizmo | Wiz |
| PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks | PowerGizmo | Ritz |

vi)
| ProdName | Store | PName        | Price          | DiscountPrice  | Category | Manufacturer |
|:------------:|:------------:|:----:|:-----------:|:------------:|:------------:|:------------:|
| Gizmo | Wiz | Gizmo        | $19.99          | $16.99  | Gadgets | GWorks |
| PowerGizmo | Ritz | PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks | 

vii)
| ProdName | Store | PName        | Price          | DiscountPrice  | Category | Manufacturer |
|:------------:|:------------:|:----:|:-----------:|:------------:|:------------:|:------------:|
| Gizmo | Wiz | Gizmo        | $19.99          | $16.99  | Gadgets | GWorks |
| PowerGizmo | Ritz | PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks | 
| Camera | Wiz | Camera | NULL | NULL | NULL | NULL |

# Question 3

Perform the following operations in set algebra:

Assume A and B are both sets, C and D are both multisets.

A = {2, 1, 3}, B = {3, 1, 4}, C = {2, 1, 3, 1}, D = {1, x, y}.

------------

**Solutions**

For all these solutions, any order is acceptable (i.e., {1, 2, 3, 4} or {2, 4, 1, 3}

1. {1, 2, 3, 4}
2. {1, 2, 3, 4}
3. {1, 1, 1, 2, 3, x, y}


# Question 4

Suppose we're given a table ***Product***:

|pid| PName        | Price          | DiscountPrice  | Category | Manufacturer |
|----| ------------- |:-------------:| -----:|:-----------:|:------------:|
| 18 | Gizmo | $19.99 | $16.99 | Gadgets | GWorks |
| 70 | PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks |
| 32 | SingleTouch | $149.99 | $144.99 | Photography | Canon |
| 67 | MultiTouch | $203.99 | $199.99 | Household | Hitachi |

Let S1 consist of the first two tuples of ***Product***, S2 be the last two tuples of ***Product***, and S is the whole instance. Show the results of the following operations.

------------

**Solutions**

1)
|pid| PName        | Price          | DiscountPrice  | Category | Manufacturer | pid| PName        | Price          | DiscountPrice  | Category | Manufacturer |
|----|:------------- |:-------------:|:----:|:-----------:|:------------:|----|:------------- |:-------------:|:----:|:-----------:|:------------:|
| 18 | Gizmo | $19.99 | $16.99 | Gadgets | GWorks | 18 | Gizmo | $19.99 | $16.99 | Gadgets | GWorks |
| 70 | PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks | 70 | PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks |
| 32 | SingleTouch | $149.99 | $144.99 | Photography | Canon | 32 | SingleTouch | $149.99 | $144.99 | Photography | Canon |
| 67 | MultiTouch | $203.99 | $199.99 | Household | Hitachi | 67 | MultiTouch | $203.99 | $199.99 | Household | Hitachi |

2)
|pid| PName        | Price          | DiscountPrice  | Category | Manufacturer | pid| PName        | Price          | DiscountPrice  | Category | Manufacturer |
|----|:------------- |:-------------:|:----:|:-----------:|:------------:|----|:------------- |:-------------:|:----:|:-----------:|:------------:|
| 18 | Gizmo | $19.99 | $16.99 | Gadgets | GWorks | 18 | Gizmo | $19.99 | $16.99 | Gadgets | GWorks |
| 70 | PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks | 70 | PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks |
| 32 | SingleTouch | $149.99 | $144.99 | Photography | Canon | 32 | SingleTouch | $149.99 | $144.99 | Photography | Canon |
| 67 | MultiTouch | $203.99 | $199.99 | Household | Hitachi | 67 | MultiTouch | $203.99 | $199.99 | Household | Hitachi |

3) 
|pid| PName        | Price          | DiscountPrice  | Category | Manufacturer | pid| PName        | Price          | DiscountPrice  | Category | Manufacturer |
|----|:------------- |:-------------:|:----:|:-----------:|:------------:|----|:------------- |:-------------:|:----:|:-----------:|:------------:|
| 18 | Gizmo | $19.99 | $16.99 | Gadgets | GWorks | 18 | Gizmo | $19.99 | $16.99 | Gadgets | GWorks |
| 70 | PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks | 70 | PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks |
| 32 | SingleTouch | $149.99 | $144.99 | Photography | Canon | 32 | SingleTouch | $149.99 | $144.99 | Photography | Canon |
| 67 | MultiTouch | $203.99 | $199.99 | Household | Hitachi | 67 | MultiTouch | $203.99 | $199.99 | Household | Hitachi |

4) 
|pid| PName        | Price          | DiscountPrice  | Category | Manufacturer | pid| PName        | Price          | DiscountPrice  | Category | Manufacturer |
|----|:------------- |:-------------:|:----:|:-----------:|:------------:|----|:------------- |:-------------:|:----:|:-----------:|:------------:|
| 18 | Gizmo | $19.99 | $16.99 | Gadgets | GWorks | NULL | NULL | NULL | NULL | NULL | NULL |
| 70 | PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks | NULL | NULL | NULL | NULL | NULL | NULL |

5)
|pid| PName        | Price          | DiscountPrice  | Category | Manufacturer | pid| PName        | Price          | DiscountPrice  | Category | Manufacturer |
|----|:------------- |:-------------:|:----:|:-----------:|:------------:|----|:------------- |:-------------:|:----:|:-----------:|:------------:|
| NULL | NULL | NULL | NULL | NULL | NULL | 32 | SingleTouch | $149.99 | $144.99 | Photography | Canon |
| NULL | NULL | NULL | NULL | NULL | NULL | 67 | MultiTouch | $203.99 | $199.99 | Household | Hitachi |

6)
|pid| PName        | Price          | DiscountPrice  | Category | Manufacturer | pid| PName        | Price          | DiscountPrice  | Category | Manufacturer |
|----|:------------- |:-------------:|:----:|:-----------:|:------------:|----|:------------- |:-------------:|:----:|:-----------:|:------------:|
| 18 | Gizmo | $19.99 | $16.99 | Gadgets | GWorks | NULL | NULL | NULL | NULL | NULL | NULL |
| 70 | PowerGizmo | $29.99 | $25.99 | Gadgets | GWorks | NULL | NULL | NULL | NULL | NULL | NULL |
| NULL | NULL | NULL | NULL | NULL | NULL | 32 | SingleTouch | $149.99 | $144.99 | Photography | Canon |
| NULL | NULL | NULL | NULL | NULL | NULL | 67 | MultiTouch | $203.99 | $199.99 | Household | Hitachi |

# Question 5

Consider tables or relations R and S where R has n tuples and S has m tuples, with n >= m. Give the minimum and maximum number of tuples that can be a result of the following expressions.

------------

**Solutions**

1. max: n + m, min: n
2. max: m, min: 0
3. max: n * m, min: 0
4. max: m^2, min: m, we also accept min:0, max m
5. max: n, min: n-m
6. max: m, min: 0

# Question 6: ACID
From the following scenarios, consider whether the scenario is a failure of 1) atomicity, 2) consistency, 3) isolation or 4) durability (the letters in ACID). Choose one failure that bests fits the scenario. Provide a short (<= 1 sentence) explanation of why. 

------------

**Solutions**

1. Durability
2. Atomicity
3. Consistency
4. Isolation
5. Consistency
6. Atomicity
7. Durability
8. Isolation

# Question 7

We have two systems in charge of running a batch of jobs. System A runs 40 jobs in 30 seconds, and System B runs the same 40 jobs in 35 seconds.

------------

**Solutions**

1. 40/30 = 1.33 jobs/s, 40/35 = 1.14 jobs/s
2. A. (7/6 - 1)% = 16.7%
3. 35 / 25 = 1.4
4. d. We do not know the latency, we are only given the system throughput. The idea is that throughput =/= latency. On one end of the spectrum, the jobs might have been executed serially, in that case the average latency would be 30 seconds / 40 = 0.75 seconds, but they might also have been executed in parallel and all started in the beginning and finished exactly after 30 seconds, in which case the latency would be 30 seconds. Or if not parallel, the machine could be idle for 19 seconds and then finish all the jobs in 1 second and then idle for the rest of the 10 seconds. 

# Question 8 - Amdahl's Law
Your boss asks you to improve the performance of a system. Before you begin optimizing the system, we want to guess how much improvement we can get on performance time. For each of the following optimizations, figure out the speedup.

------------

**Solutions**

1 / (1 - p + p/s)

1. 1 / (1 - 0.5 + (0.5/1.1)) =1.0476
2. 1 / (1 - 0.05 + (0.05/10)) = 1.0471
3. 1 / (1 - 0.15 + (0.15/10)) = 1.156
4. 3 or I/O

# Question 9
We first describe the memory hierarchy. Suppose that we have a latency to the CPU cache of 5ns, latency to memory of 25ns, and latency to flash of 1ms. For each of the following situations (where all we consider are random reads from a memory address), calculate the average latency.

------------

**Solutions**

1. 9 ns
2. 0.95 * 5 + 0.05 * 1000000 = 50004.75 ns
3. 0.85 * 25 + 0.15 * 1000 = 150021.25 ns

# Question 10
A computer systems is using a magnetic disk (hard disk) as storage. Suppose that the hard disk has a capacity of 300 GB, an RPM (rotations per minute) of 10000, an average seek of 4ms, and a max transfer rate of 100MB/s. 

------------

**Solutions**

1. 60/10000 s = 6 ms
2. 4kb/100MB/s = 4000/100*10^6 = 40 {mu}sec
3. Add them up. T_{i/o} = 6ms / 2 + 4 ms + 40mu = 7.040. (half rotation).  R_{i/o} = 4kb/(T_{i/o}) = 0.568 MB/s.
4. 100MB/s. 125/100 = 1.25 sec approximately. If include the one movement, 1.257 sec. 1.25/1.257 = 99.44 MB/s

# Question 11
Suppose that we have a rack that we are using to host our website. The rack consists of 42U. Assume that each network switch uses 10 watts and that each server uses 200 watts. Suppose that we have a Total Facility Power of 6000. What is the PUE of the following configurations?

------------

**Solutions**

1. 6000 / (10 * 10 + 16 * 200) = 1.81
2. 6000 / (4 * 10 + 19 * 200) = 1.56
3. 6000 /(21 * 200) = 1.43

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

For example, a record can be represented as (A, Professor, 94).

------------

**Solution**

1. (A, Professor, 99)

2. (A, Professor, 99), (E, Student, 35), (F, Student, 35)

3. (A, Professor, 99), (E, Student, 35), (F, Student, 35)

# Question 13

Consider a database with objects X and Y and assume that there are two transactions T1 and T2. T1 first reads X and Y and then writes object Y. T2 reads objects X and Y and then writes objects X and Y.

------------

**Solution**

1 

 - WR-conflict: c 
 - RW-conflict: a 
 - WW-conflict: d 
 - No-conflict: b

2

*There was a lot of confusion about disallows on this part. The idea is that strict 2PL prevents the sequence of steps in the interleaved schedule from looking exactly like it does. More clearly, by some locking mechanism or another, there is no way for transactions to proceed with the schedule since it is either waiting for or cannot get access to a lock.*

 - a) T2 tries to get a shared lock for W(A), but T1 already has it.
 - c) T2 tries to get the shared lock for R(A), but T1 already has an exclusive lock for W(A).
 - d) T1 gets an exclusive lock for W(A) and W(C), but T2 wants a exclusive lock for W(A).

3

No data being modified. So completely safe no matter the number of transactions.

# Question 14
Consider two transactions T1 and T2 in a database with objects X and Y. T1 reads and writes X then reads and writes Y. T2 first reads X and Y and then writes X and Y.

------------

**Solution**

**1)**

R2[X]→R2[Y]→R1[X]→W1[X]→R1[Y]→W2[X]→W2[Y]→W1[Y]→C2→C1

A schedule is serializable if it contains the same transactions and operations as a serial schedule and the order of all conflicting operations (read/writes to the same objects by different transactions) is also the same. In the above schedule, T2 reads X before T1 writes X. However, T2 writes X after T1 reads and writes it. The schedule is thus clearly not serializable. Additionally, according to the above schedule, the final content of object X is written by T2 and the final content of object Y is written by T1. Such a result is not possible in any serial execution, where transactions execute one after the other in sequence.

**2)**

Strict 2PL has two two rules:

1. If a transaction wants to read (respectively, modify) an object, it first requests a shared (respectively, exclusive) lock on the object.
2. All locks held by a transaction are released when the transaction is completed.

With strict 2PL, the above schedule is not possible. Indeed, T2 first acquires shared locks on X and Y . When T1 runs, it also acquires a shared lock on X. When it tries to acquire an exclusive lock before writing X, however, it blocks, waiting for T2 to release its lock, which will happen only when T2 commits. The above schedule is thus impossible with strict 2PL. 

In fact, the schedule leads to a deadlock: when T2 tries to write X, it also blocks waiting for T1 to release its shared lock. Now, both transactions are waiting for each other. We have a deadlock.

**3)**

When the deadlock is detected, the DBMS will abort one of the transactions, allowing the other one to commit and release its locks.

# Question 15

As transaction conflicts are common in the case of concurrency updates, Jerry Mouse thinks about handling conflicts by splitting a transaction into several parts: the splitted parts altogether produce the same and consistent updates and outputs as the original intergrated transactions, but each requires less locks.

Tell Jerry whether the following splitting method works or not and explain him the reason.

 ”Suppose transaction T accesses object X and Y, and any other transaction S accesses at most one of X or Y and nothing else. Therefore, T can be splitted into two parts, one of which accesses X and the other accesses Y.” 

------------

**Solution**

The splitting method is correct. 

Consider T is splitted into T1 and T2. Assume T1 accesses only X and T2 accesses only Y . (The other cases can be proved using a similar argument). Further, if we assume that S accesses X only, then any schedule produced by T1, T2 and S is serializable (i.e. any schedule is equivalent to either S, T or T, S.

*Note: It is assumed that in T operations on X and Y are not entangled. One example on the contrary can be set value of Y to be that of X, where the splitting method doesn't work anymore. As long as assumption is clearly stated and reasonably explained suffice the requirement.*

*Note: The problem doesn't concern atomicity as it only cares if the **combined results** for spllited transactions altogether has the same and consistent result as the original one. Whether results of spllited transactions will be applied atomicitly can be taken care of by the DBMS. Credit will be given for the assumption that atomicity is not handled by DBMS.*

*Note: Jerry aims to improve the performance in case of conflicts by reducing waiting time incurred by conflicts (recall lock acquiring time in 2PL for a transaction). His method parallelizes transactions and reduces lock acquiring time as much as possible. Conflicts still exist due to the nature of operations of related transactions and total number of locks acquired won't change as well. Jerry didn't mean to eliminate conflicts and existing conflicts doesn't nesessarily lead to deadlock.*

# Question 16

A database is usually replicated on multiple sites for better performance. Suppose a transaction executing from a cellphone visits different replicas and reads and writes (parts of) the database.

Design a simple protocol whereby a transaction can read globally-consistent data from the database replica “nearest” to it. In particular, what should a reading transaction lock? what should a writing transaction lock?

Will your transaction lead to deadlocks? If so, how can you avoid it?

------------

**Solution**

A reading transaction should lock the required data item only on that database replica that is “nearest” to it.

A writing transaction should lock the required data item on all the database replica.

This can lead to deadlock. Deadlock can be avoided by ordering the locks acquired on the database replicas for the write. This can be done by imposing the constraint that any writing transaction should lock and update the database replica in a fixed order (which is the same for each transaction).

*Note: Other feasible solutions including but not limited to master-slave model, centralized lock service, peer propogation, update on read, etc. and conservative 2PL, wait-for graph for deadlocks detection & prevention. As long as type and effective range of locks are specified together with a valid deadlock prevention policy will suffice the requirement.*
