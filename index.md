---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title: Home
menu: main
---

CSEE4121 - Computer Systems for Data Science 
{: style="color:black; font-size: 210%; font-weight:700; text-align: center;"}
Spring '20, Columbia University
{: style="color:black; font-size: 130%; text-align: center;"}
----

## Course Overview
Data scientists and engineers increasingly have access to a powerful and broad range of systems they use to conduct big data analysis and machine learning at scale: from databases, large-scale analytics to distributed machine learning frameworks.
The goal of this class is to provide data scientists and engineers that work with big data a better understanding of the foundations of how the systems they will be using are built. It will also give them a better understanding of the real-world performance, availability and scalability challenges when using and deploying these systems at scale. In the course we will cover foundational ideas in designing these systems, while focusing on specific popular systems that students are likely to encounter at work or when doing research. The class will include some written homework and programming assignments. Some of the assignments will be done in groups.
In this course we will answer the following questions:
<ul>
  <li>How are popular big data systems designed and architected? </li>
  <li>How to think about performance, scale and reliability of big data systems? </li>
  <li>How do they remain available and not lose data despite frequent server and hardware failures? </li>
</ul>
{: .text-justify}

## Instructor
Asaf Cidon \\
OH: Mondays 2:30-3:30 PM (By appointment only)

## Location and Time
501 Northwest Corner Building. \\
Mondays 4:10pm - 6:40pm

## TAs
(All Office Hours Held in the CS TA Room) \\
Hongyi Wang -- Mon 12pm - 2pm \\
Qianrui Zhang -- Tue 9am - 11am \\
Yujian Wu -- Wed 2pm - 4pm \\
Junlin Song -- Thu 12:00pm - 2:00pm\\
Ke Li -- Thu 3pm - 5pm \\
Mingen Pan -- Fri 4pm - 6pm 

## Piazza Link
[https://piazza.com/class/k5o2sby3t2e2pb](https://piazza.com/class/k5o2sby3t2e2pb)

## Prerequisites
Students are expected to have solid programming experience in Python or with an equivalent programming language. This class is intended to be accessible for data scientists who do not necessarily have a background in databases, operating systems or distributed systems.

## Schedule (this is a work in progress, and is likely to change)


<table>
<colgroup>
<col width="33%" />
<col width="45%" />
<col width="22%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Topic</th>
<th>Homework</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">Jan 27</td>
<td markdown="span">Introduction <a href="https://github.com/CS-W4121/cs-w4121.github.io/blob/master/slides/Topic%201%20-%20intro%20and%20rules%20of%20thumb%20part%20I.pptx">[pptx]<a href="https://github.com/CS-W4121/cs-w4121.github.io/blob/master/slides/Topic%201%20-%20intro%20and%20rules%20of%20thumb%20part%20I.pdf">[pdf]</a></td>

</tr>
<tr>
<td markdown="span">Feb 3</td>
<td markdown="span">Infrastructure for Big Data <a href="https://github.com/CS-W4121/cs-w4121.github.io/blob/master/slides/Topic%201%20-%20intro%20and%20rules%20of%20thumb%20part%20II.pptx"> [pptx]<a href="https://github.com/CS-W4121/cs-w4121.github.io/blob/master/slides/Topic%201%20-%20intro%20and%20rules%20of%20thumb%20part%20II.pdf"> [pdf]</a> Relational Model Part I <a href="https://github.com/CS-W4121/cs-w4121.github.io/blob/master/slides/Topic%202%20-%20relational%20model%20part%20I.pptx"> [pptx]<a href="https://github.com/CS-W4121/cs-w4121.github.io/blob/master/slides/Topic%202%20-%20relational%20model%20part%20I.pdf"> [pdf] </a></td>
<th rowspan="3" markdown="1">[Programming Homework 1]({{ site.baseurl }}{%link homeworks/hw1.md %})</th>
<!---
<th rowspan="3" markdown="1">[Programming Homework 1]</th>
-->
</tr>
<tr>
<td markdown="span">Rescheduled: Feb 14 (Friday), 1:30-3:40 PM, 501 SCH (Schermerhorn)</td>
<td markdown="span">SQL and Relational Model </td>
</tr>
<tr>
<td markdown="span">Feb 17</td>
<td markdown="span">SQL and Relational Model </td>
</tr>
<tr>
<td markdown="span">Feb 24</td>
<td markdown="span">NoSQL </td>
<th rowspan="3" markdown="1">[Written Homework]</th>
</tr>
<tr>
<td markdown="span">Mar 2</td>
<td markdown="span">Storage and Distributed File Systems </td>
</tr>
<tr>
<td markdown="span">Mar 9</td>
<td markdown="span">Midterm</td>
</tr>
<tr>
<td markdown="span">Mar 16</td>
<td markdown="span">Spring Break </td>
</tr>
<tr>
<td markdown="span">Mar 23</td>
<td markdown="span">Scaling</td>
<!---
<th rowspan="4" markdown="1">[Programming Homework 2]({{ site.baseurl }}{%link homeworks/hw2.md %})</th>
-->
<th rowspan="4" markdown="1">[Programming Homework 2]</th>
</tr>
<tr>
<td markdown="span">Mar 30</td>
<td markdown="span">MapReduce and Stragglers </td>
</tr>
<tr>
<td markdown="span">Apr 6</td>
<td markdown="span">Spark </td>
</tr>
<tr>
<td markdown="span">Apr 13</td>
<td markdown="span">Caching </td>
</tr>
<tr>
<td markdown="span">Apr 20</td>
<td markdown="span">Tensorflow </td>
<!---
<th rowspan="3" markdown="1">[Programming Homework 3]({{ site.baseurl }}{%link homeworks/hw3.md %})</th>
-->
<th rowspan="3" markdown="1">[Programming Homework 3]</th>
</tr>
<tr>
<td markdown="span">Apr 27</td>
<td markdown="span">Data Pipelines / Security and Privacy </td>
</tr>
<tr>
<td markdown="span">May 4</td>
<td markdown="span">Final Exam</td>
</tr>
</tbody>
</table>

## Grade Breakdown
20% Programming Homework 1 \\
10% Written Homework \\
20% Programming Homework 2 \\
10% Programming Homework 3 \\
15% Midterm \\
25% Final

## Collaboration/Copying Policy
Programming assignment 1 and the written assignment will be done alone. Programming assignments 2-3 will be done in pairs . You may not copy answers and code. We will enforce this policy when checking the assignments (we use a code similarity system).

## Course Materials
No textbook.
