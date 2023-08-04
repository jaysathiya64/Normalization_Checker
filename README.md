# Normalization_Checker
Normalization is the process of removing redundant data from tables to improve data integrity, scalability and storage efficiency.Data integrity (completeness, accuracy and consistency of data),scalability (ability of a system to continue to function well in a growing amount of work),storage efficiency (ability to store and manage data that consumes the least amount of space)

Normalization generally involves splitting an existing table into multiple (more than one) tables, which can be re-joined or linked each time a query is issued (executed).

In this project we will cover Till BCNF (Which include 1NF, 2NF, 3NF and BCNF) .
In input user give Relational set, FD’s and Candidate key for the given relation and output show whether the relation is normal form or not.

### 1 Normal Form
A relation R is in first normal form (1NF) if and only if it does not contain any composite attribute or multi-valued attributes or their combinations.

### 2 Normal Form
A relation R is in second normal form (2NF)
  * If and only if it is in 1NF and	
  * Every non-primary key attribute is fully dependent on the primary ke

    ### Non – Primary Key Attribute
  * Primary key is an attribute or set of attributes that are chosen to uniquely identify any records in a table. The values of a primary     key cannot be duplicated. On the other hand, non-prime (non-key) attributes are the attributes other than the primary key attributes.     They can store a value any many times.

### 3 Normal Form
A relation R is in third normal form (3NF)
  * If and only if it is in 2NF and
  * Every non-key attribute is non-transitively dependent on the primary key
  * It is in 2NF and there is no transitive dependency (Transitive dependency???) A → B & B → C then A → C

### BCNF (Boyce-Codd Normal Form)
A relation R is in Boyce-Codd normal form (BCNF)
  * If and only if it is in 3NF and
  * For every functional dependency X → Y, X should be the primary key of the table.

## Steps
Download the main.py file and input.txt file in the same directory.<br>
Input must be in a form of Relational Set, Functional Dependency and Candidate Key.<br>
Run main.py file.

# Output:
## 2 Normal Form
### Input
  R(A,B,C,D)
    CK:-AB
    AB -> D 
    B -> C

### Output
![image](https://github.com/jaysathiya64/Normalization_Checker/assets/126950992/2cc03fb8-98e5-489f-9b01-900bdbb0fd60)



## 3 Normal Form
### Input
  R1(A,B,C,D,E)
    CK:-CE
    CE -> D
    D -> B
    C -> A

### Output
![image](https://github.com/jaysathiya64/Normalization_Checker/assets/126950992/de1c5092-4d72-407b-b776-1daaab9fca31)


## BCNF (Boyce-Codd Normal Form)
### Input
  R1(A,B,C,D,E,F)
    CK:-A
    A -> B
    A -> C
    C -> A
    C -> D

### Output
![image](https://github.com/jaysathiya64/Normalization_Checker/assets/126950992/5517e00c-f5f7-42f7-984d-1a303b085378)






