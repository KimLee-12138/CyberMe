---
id: extract-rlmath-7f743592
type: extract
status: extracted
course: RLMATH
source:
  - "[[91_Raw-Archive/PDF/RLMATH_L8-Value function methods.pdf.pdf_课件_未知日期_7f743592.pdf]]"
source_pages: all
source_hash: "7f743592242cec6153a8792540a9a538f1fb5bfafa4093bd758d2049fffe5d33"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# L8-Value function methods.pdf.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

Lecture 8: Value Function Methods
Shiyu Zhao
Department of Articial Intelligence
Westlake University

## 第2页

Outline
Chapter 2:
Bellman EquationChapter 3:
Bellman Optimality 
EquationChapter 4:
Value Iteration & 
Policy IterationChapter 5: 
Monte Carlo 
Methods
Chapter 7:
Temporal- Difference 
Methods
Chapter 8:
Value Function 
Methods
Chapter 9:
Policy Gradient 
MethodsChapter 10:
Actor -Critic 
MethodsChapter 6:
Stochastic 
Approximationwith model
to
without model
tabular representation
to
function representation
Fundamental toolsAlgorithms/Methods
Chapter 1:
Basic Concepts
policy- based
plus
value -based
Shiyu Zhao 1 / 69

## 第3页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 2 / 69

## 第4页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 3 / 69

## 第5页

Motivating examples: from table to function
So far in this book, state and action values are represented by tables.
For example, state value:
State s1 s2 sn
Valuev(s1)v(s2)v(sn)
For example, action value:
a1 a2 a3 a4 a5
s1q(s1;a1)q(s1;a2)q(s1;a3)q(s1;a4)q(s1;a5)
..................
s9q(s9;a1)q(s9;a2)q(s9;a3)q(s9;a4)q(s9;a5)
Advantage: intuitive and easy to analyze
Disadvantage: dicult to handle large or continuous state or action spaces.
Two aspects: 1) storage; 2) generalization ability
Shiyu Zhao 4 / 69

## 第6页

Motivating examples: from table to function
So far in this book, state and action values are represented by tables.
For example, state value:
State s1 s2 sn
Valuev(s1)v(s2)v(sn)
For example, action value:
a1 a2 a3 a4 a5
s1q(s1;a1)q(s1;a2)q(s1;a3)q(s1;a4)q(s1;a5)
..................
s9q(s9;a1)q(s9;a2)q(s9;a3)q(s9;a4)q(s9;a5)
Advantage: intuitive and easy to analyze
Disadvantage: dicult to handle large or continuous state or action spaces.
Two aspects: 1) storage; 2) generalization ability
Shiyu Zhao 4 / 69

## 第7页

Motivating examples: from table to function
So far in this book, state and action values are represented by tables.
For example, state value:
State s1 s2 sn
Valuev(s1)v(s2)v(sn)
For example, action value:
a1 a2 a3 a4 a5
s1q(s1;a1)q(s1;a2)q(s1;a3)q(s1;a4)q(s1;a5)
..................
s9q(s9;a1)q(s9;a2)q(s9;a3)q(s9;a4)q(s9;a5)
Advantage: intuitive and easy to analyze
Disadvantage: dicult to handle large or continuous state or action spaces.
Two aspects: 1) storage; 2) generalization ability
Shiyu Zhao 4 / 69

## 第8页

Motivating examples: from table to function
So far in this book, state and action values are represented by tables.
For example, state value:
State s1 s2 sn
Valuev(s1)v(s2)v(sn)
For example, action value:
a1 a2 a3 a4 a5
s1q(s1;a1)q(s1;a2)q(s1;a3)q(s1;a4)q(s1;a5)
..................
s9q(s9;a1)q(s9;a2)q(s9;a3)q(s9;a4)q(s9;a5)
Advantage: intuitive and easy to analyze
Disadvantage: dicult to handle large or continuous state or action spaces.
Two aspects: 1) storage; 2) generalization ability
Shiyu Zhao 4 / 69

## 第9页

Motivating examples: from table to function
So far in this book, state and action values are represented by tables.
For example, state value:
State s1 s2 sn
Valuev(s1)v(s2)v(sn)
For example, action value:
a1 a2 a3 a4 a5
s1q(s1;a1)q(s1;a2)q(s1;a3)q(s1;a4)q(s1;a5)
..................
s9q(s9;a1)q(s9;a2)q(s9;a3)q(s9;a4)q(s9;a5)
Advantage: intuitive and easy to analyze
Disadvantage: dicult to handle large or continuous state or action spaces.
Two aspects: 1) storage; 2) generalization ability
Shiyu Zhao 4 / 69

## 第10页

Motivating examples: from table to function
Consider an example:
There arenstates:s1;:::;sn.
The state values are v(s1);:::;v(sn), whereis a given policy.
nis very large!
We hope to use a simple curve to approximate these values.
Shiyu Zhao 5 / 69

## 第11页

Motivating examples: from table to function
For example, we can use a simple straight line to t the dots.
1
sˆv(s)
s1s2s3s4 · · · snˆv(s) =as+b
Suppose the equation of the straight line is
^v(s;w) =as+b= [s;1]|{z}
T(s)"
a
b#
|{z}
w=T(s)w
wis the parameter vector; (s)the feature vector of s;^v(s;w)is linear inw.
Shiyu Zhao 6 / 69

## 第12页

Motivating examples: from table to function
For example, we can use a simple straight line to t the dots.
1
sˆv(s)
s1s2s3s4 · · · snˆv(s) =as+b
Suppose the equation of the straight line is
^v(s;w) =as+b= [s;1]|{z}
T(s)"
a
b#
|{z}
w=T(s)w
wis the parameter vector; (s)the feature vector of s;^v(s;w)is linear inw.
Shiyu Zhao 6 / 69

## 第13页

Motivating examples: from table to function
For example, we can use a simple straight line to t the dots.
1
sˆv(s)
s1s2s3s4 · · · snˆv(s) =as+b
Suppose the equation of the straight line is
^v(s;w) =as+b= [s;1]|{z}
T(s)"
a
b#
|{z}
w=T(s)w
wis the parameter vector; (s)the feature vector of s;^v(s;w)is linear inw.
Shiyu Zhao 6 / 69

## 第14页

Motivating examples: from table to function
For example, we can use a simple straight line to t the dots.
1
sˆv(s)
s1s2s3s4 · · · snˆv(s) =as+b
Suppose the equation of the straight line is
^v(s;w) =as+b= [s;1]|{z}
T(s)"
a
b#
|{z}
w=T(s)w
wis the parameter vector; (s)the feature vector of s;^v(s;w)is linear inw.
Shiyu Zhao 6 / 69

## 第15页

Motivating examples: from table to function
Dierence between the tabular and function methods:
Dierence 1: How to retrieve the value of a state
When the values are represented by a table, we can directly read the value in
the table.
When the values are represented by a function, we need to input the state
indexsinto the function and calculate the function value.
w
functions ˆv(s, w)
For example, s!(s)!T(s)w= ^v(s;w)
- Benet: storage. We do not need to store jSjstate values. We only need
to store a lower-dimensional w.
Shiyu Zhao 7 / 69

## 第16页

Motivating examples: from table to function
Dierence between the tabular and function methods:
Dierence 1: How to retrieve the value of a state
When the values are represented by a table, we can directly read the value in
the table.
When the values are represented by a function, we need to input the state
indexsinto the function and calculate the function value.
w
functions ˆv(s, w)
For example, s!(s)!T(s)w= ^v(s;w)
- Benet: storage. We do not need to store jSjstate values. We only need
to store a lower-dimensional w.
Shiyu Zhao 7 / 69

## 第17页

Motivating examples: from table to function
Dierence between the tabular and function methods:
Dierence 1: How to retrieve the value of a state
When the values are represented by a table, we can directly read the value in
the table.
When the values are represented by a function, we need to input the state
indexsinto the function and calculate the function value.
w
functions ˆv(s, w)
For example, s!(s)!T(s)w= ^v(s;w)
- Benet: storage. We do not need to store jSjstate values. We only need
to store a lower-dimensional w.
Shiyu Zhao 7 / 69

## 第18页

Motivating examples: from table to function
Dierence between the tabular and function methods:
Dierence 1: How to retrieve the value of a state
When the values are represented by a table, we can directly read the value in
the table.
When the values are represented by a function, we need to input the state
indexsinto the function and calculate the function value.
w
functions ˆv(s, w)
For example, s!(s)!T(s)w= ^v(s;w)
- Benet: storage. We do not need to store jSjstate values. We only need
to store a lower-dimensional w.
Shiyu Zhao 7 / 69

## 第19页

Motivating examples: from table to function
Dierence between the tabular and function methods:
Dierence 1: How to retrieve the value of a state
When the values are represented by a table, we can directly read the value in
the table.
When the values are represented by a function, we need to input the state
indexsinto the function and calculate the function value.
w
functions ˆv(s, w)
For example, s!(s)!T(s)w= ^v(s;w)
- Benet: storage. We do not need to store jSjstate values. We only need
to store a lower-dimensional w.
Shiyu Zhao 7 / 69

## 第20页

Motivating examples: from table to function
Dierence between the tabular and function methods:
Dierence 1: How to retrieve the value of a state
When the values are represented by a table, we can directly read the value in
the table.
When the values are represented by a function, we need to input the state
indexsinto the function and calculate the function value.
w
functions ˆv(s, w)
For example, s!(s)!T(s)w= ^v(s;w)
- Benet: storage. We do not need to store jSjstate values. We only need
to store a lower-dimensional w.
Shiyu Zhao 7 / 69

## 第21页

Motivating examples: from table to function
Dierence between the tabular and function methods:
Dierence 2: How to update the value of a state
When the values are represented by a table, we can directly rewrite the value
in the table.
When the values are represented by a function, we must update wto change
the values indirectly.
- How to update wwill be addressed in detail later.
Shiyu Zhao 8 / 69

## 第22页

Motivating examples: from table to function
Dierence between the tabular and function methods:
Dierence 2: How to update the value of a state
When the values are represented by a table, we can directly rewrite the value
in the table.
When the values are represented by a function, we must update wto change
the values indirectly.
- How to update wwill be addressed in detail later.
Shiyu Zhao 8 / 69

## 第23页

Motivating examples: from table to function
Dierence between the tabular and function methods:
Dierence 2: How to update the value of a state
When the values are represented by a table, we can directly rewrite the value
in the table.
When the values are represented by a function, we must update wto change
the values indirectly.
- How to update wwill be addressed in detail later.
Shiyu Zhao 8 / 69

## 第24页

Motivating examples: from table to function
Dierence between the tabular and function methods:
Dierence 2: How to update the value of a state
When the values are represented by a table, we can directly rewrite the value
in the table.
When the values are represented by a function, we must update wto change
the values indirectly.
- How to update wwill be addressed in detail later.
Shiyu Zhao 8 / 69

## 第25页

Motivating examples: from table to function
Dierence between the tabular and function methods:
Dierence 2: How to update the value of a state
1
sˆv(s)
s1s2s3update ˆv(s3) update ˆv(s3)
sˆv(s)
s1s2s3
(a) Tabular method
1
sˆv(s)
s1s2s3update wfors3 update wfors3
sˆv(s)
s1s2s3
(b) Function method
Benet: generalization ability. When we update ^v(s;w)by changing w, the
values of the neighboring states are also changed.
Shiyu Zhao 9 / 69

## 第26页

Motivating examples: from table to function
Dierence between the tabular and function methods:
Dierence 2: How to update the value of a state
1
sˆv(s)
s1s2s3update ˆv(s3) update ˆv(s3)
sˆv(s)
s1s2s3
(a) Tabular method
1
sˆv(s)
s1s2s3update wfors3 update wfors3
sˆv(s)
s1s2s3
(b) Function method
Benet: generalization ability. When we update ^v(s;w)by changing w, the
values of the neighboring states are also changed.
Shiyu Zhao 9 / 69

## 第27页

Motivating examples: from table to function
The benets are not free. It comes with a cost: the state values can not be
represented accurately. This is why this method is called approximation.
We can t the points more precisely using high-order curves:
^v(s;w) =as2+bs+c= [s2;s;1]|{z}
T(s)2
64a
b
c3
75
|{z}
w=T(s)w:
In this case,
The dimensions of wand(s)increase; the values may be tted more
accurately.
Although ^v(s;w)is nonlinear in s, it is linear in w. The nonlinearity is
contained in (s).
Shiyu Zhao 10 / 69

## 第28页

Motivating examples: from table to function
The benets are not free. It comes with a cost: the state values can not be
represented accurately. This is why this method is called approximation.
We can t the points more precisely using high-order curves:
^v(s;w) =as2+bs+c= [s2;s;1]|{z}
T(s)2
64a
b
c3
75
|{z}
w=T(s)w:
In this case,
The dimensions of wand(s)increase; the values may be tted more
accurately.
Although ^v(s;w)is nonlinear in s, it is linear in w. The nonlinearity is
contained in (s).
Shiyu Zhao 10 / 69

## 第29页

Motivating examples: from table to function
The benets are not free. It comes with a cost: the state values can not be
represented accurately. This is why this method is called approximation.
We can t the points more precisely using high-order curves:
^v(s;w) =as2+bs+c= [s2;s;1]|{z}
T(s)2
64a
b
c3
75
|{z}
w=T(s)w:
In this case,
The dimensions of wand(s)increase; the values may be tted more
accurately.
Although ^v(s;w)is nonlinear in s, it is linear in w. The nonlinearity is
contained in (s).
Shiyu Zhao 10 / 69

## 第30页

Motivating examples: from table to function
The benets are not free. It comes with a cost: the state values can not be
represented accurately. This is why this method is called approximation.
We can t the points more precisely using high-order curves:
^v(s;w) =as2+bs+c= [s2;s;1]|{z}
T(s)2
64a
b
c3
75
|{z}
w=T(s)w:
In this case,
The dimensions of wand(s)increase; the values may be tted more
accurately.
Although ^v(s;w)is nonlinear in s, it is linear in w. The nonlinearity is
contained in (s).
Shiyu Zhao 10 / 69

## 第31页

Motivating examples: from table to function
Quick summary:
Idea: Approximate the state and action values using parameterized
functions: ^v(s;w)v(s)wherew2Rmis the parameter vector.
Key dierence: How to retrieve and change the value of v(s)
Advantages:
1)Storage: The dimension of wmay be much smaller than jSj.
2)Generalization: When a state sis visited, the parameter wis updated
so that the values of some other unvisited states can also be updated.
Shiyu Zhao 11 / 69

## 第32页

Motivating examples: from table to function
Quick summary:
Idea: Approximate the state and action values using parameterized
functions: ^v(s;w)v(s)wherew2Rmis the parameter vector.
Key dierence: How to retrieve and change the value of v(s)
Advantages:
1)Storage: The dimension of wmay be much smaller than jSj.
2)Generalization: When a state sis visited, the parameter wis updated
so that the values of some other unvisited states can also be updated.
Shiyu Zhao 11 / 69

## 第33页

Motivating examples: from table to function
Quick summary:
Idea: Approximate the state and action values using parameterized
functions: ^v(s;w)v(s)wherew2Rmis the parameter vector.
Key dierence: How to retrieve and change the value of v(s)
Advantages:
1)Storage: The dimension of wmay be much smaller than jSj.
2)Generalization: When a state sis visited, the parameter wis updated
so that the values of some other unvisited states can also be updated.
Shiyu Zhao 11 / 69

## 第34页

Motivating examples: from table to function
Quick summary:
Idea: Approximate the state and action values using parameterized
functions: ^v(s;w)v(s)wherew2Rmis the parameter vector.
Key dierence: How to retrieve and change the value of v(s)
Advantages:
1)Storage: The dimension of wmay be much smaller than jSj.
2)Generalization: When a state sis visited, the parameter wis updated
so that the values of some other unvisited states can also be updated.
Shiyu Zhao 11 / 69

## 第35页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 12 / 69

## 第36页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 13 / 69

## 第37页

Objective function
Introduce in a more formal way:
Letv(s)and^v(s;w)be the true state value and the estimated state value,
respectively.
Our goal is to nd an optimal wso that ^v(s;w)can best approximate v(s)
for everys.
This is a policy evaluation problem. Later we will extend to policy
improvement.
To nd the optimal w, we need two steps.
The rst step is to dene an objective function.
The second step is to derive algorithms for optimizing the objective function.
Shiyu Zhao 14 / 69

## 第38页

Objective function
Introduce in a more formal way:
Letv(s)and^v(s;w)be the true state value and the estimated state value,
respectively.
Our goal is to nd an optimal wso that ^v(s;w)can best approximate v(s)
for everys.
This is a policy evaluation problem. Later we will extend to policy
improvement.
To nd the optimal w, we need two steps.
The rst step is to dene an objective function.
The second step is to derive algorithms for optimizing the objective function.
Shiyu Zhao 14 / 69

## 第39页

Objective function
Introduce in a more formal way:
Letv(s)and^v(s;w)be the true state value and the estimated state value,
respectively.
Our goal is to nd an optimal wso that ^v(s;w)can best approximate v(s)
for everys.
This is a policy evaluation problem. Later we will extend to policy
improvement.
To nd the optimal w, we need two steps.
The rst step is to dene an objective function.
The second step is to derive algorithms for optimizing the objective function.
Shiyu Zhao 14 / 69

## 第40页

Objective function
Introduce in a more formal way:
Letv(s)and^v(s;w)be the true state value and the estimated state value,
respectively.
Our goal is to nd an optimal wso that ^v(s;w)can best approximate v(s)
for everys.
This is a policy evaluation problem. Later we will extend to policy
improvement.
To nd the optimal w, we need two steps.
The rst step is to dene an objective function.
The second step is to derive algorithms for optimizing the objective function.
Shiyu Zhao 14 / 69

## 第41页

Objective function
Introduce in a more formal way:
Letv(s)and^v(s;w)be the true state value and the estimated state value,
respectively.
Our goal is to nd an optimal wso that ^v(s;w)can best approximate v(s)
for everys.
This is a policy evaluation problem. Later we will extend to policy
improvement.
To nd the optimal w, we need two steps.
The rst step is to dene an objective function.
The second step is to derive algorithms for optimizing the objective function.
Shiyu Zhao 14 / 69

## 第42页

Objective function
Introduce in a more formal way:
Letv(s)and^v(s;w)be the true state value and the estimated state value,
respectively.
Our goal is to nd an optimal wso that ^v(s;w)can best approximate v(s)
for everys.
This is a policy evaluation problem. Later we will extend to policy
improvement.
To nd the optimal w, we need two steps.
The rst step is to dene an objective function.
The second step is to derive algorithms for optimizing the objective function.
Shiyu Zhao 14 / 69

## 第43页

Objective function
Introduce in a more formal way:
Letv(s)and^v(s;w)be the true state value and the estimated state value,
respectively.
Our goal is to nd an optimal wso that ^v(s;w)can best approximate v(s)
for everys.
This is a policy evaluation problem. Later we will extend to policy
improvement.
To nd the optimal w, we need two steps.
The rst step is to dene an objective function.
The second step is to derive algorithms for optimizing the objective function.
Shiyu Zhao 14 / 69

## 第44页

Objective function
The objective function is
J(w) =E[(v(S) ^v(S;w))2]:
Our goal is to nd the best wthat can minimize J(w).
The expectation is with respect to the random variable S2S.
What is the probability distribution of S?
- This is new. We have not discussed the probability distribution of states
so far.
- There are several ways to dene the probability distribution of S.
Shiyu Zhao 15 / 69

## 第45页

Objective function
The objective function is
J(w) =E[(v(S) ^v(S;w))2]:
Our goal is to nd the best wthat can minimize J(w).
The expectation is with respect to the random variable S2S.
What is the probability distribution of S?
- This is new. We have not discussed the probability distribution of states
so far.
- There are several ways to dene the probability distribution of S.
Shiyu Zhao 15 / 69

## 第46页

Objective function
The objective function is
J(w) =E[(v(S) ^v(S;w))2]:
Our goal is to nd the best wthat can minimize J(w).
The expectation is with respect to the random variable S2S.
What is the probability distribution of S?
- This is new. We have not discussed the probability distribution of states
so far.
- There are several ways to dene the probability distribution of S.
Shiyu Zhao 15 / 69

## 第47页

Objective function
The objective function is
J(w) =E[(v(S) ^v(S;w))2]:
Our goal is to nd the best wthat can minimize J(w).
The expectation is with respect to the random variable S2S.
What is the probability distribution of S?
- This is new. We have not discussed the probability distribution of states
so far.
- There are several ways to dene the probability distribution of S.
Shiyu Zhao 15 / 69

## 第48页

Objective function
The objective function is
J(w) =E[(v(S) ^v(S;w))2]:
Our goal is to nd the best wthat can minimize J(w).
The expectation is with respect to the random variable S2S.
What is the probability distribution of S?
- This is new. We have not discussed the probability distribution of states
so far.
- There are several ways to dene the probability distribution of S.
Shiyu Zhao 15 / 69

## 第49页

Objective function
The rst way is to use a uniform distribution.
That is to treat all the states to be equally important by setting the
probability of each state as 1=jSj.
In this case, the objective function becomes
J(w) =E[(v(S) ^v(S;w))2] =1
jSjX
s2S(v(s) ^v(s;w))2:
Drawback:
- The states may not be equally important. For example, some states may
be rarely visited by a policy. Hence, this way does not consider the real
dynamics of the Markov process under the given policy.
Shiyu Zhao 16 / 69

## 第50页

Objective function
The rst way is to use a uniform distribution.
That is to treat all the states to be equally important by setting the
probability of each state as 1=jSj.
In this case, the objective function becomes
J(w) =E[(v(S) ^v(S;w))2] =1
jSjX
s2S(v(s) ^v(s;w))2:
Drawback:
- The states may not be equally important. For example, some states may
be rarely visited by a policy. Hence, this way does not consider the real
dynamics of the Markov process under the given policy.
Shiyu Zhao 16 / 69

## 第51页

Objective function
The rst way is to use a uniform distribution.
That is to treat all the states to be equally important by setting the
probability of each state as 1=jSj.
In this case, the objective function becomes
J(w) =E[(v(S) ^v(S;w))2] =1
jSjX
s2S(v(s) ^v(s;w))2:
Drawback:
- The states may not be equally important. For example, some states may
be rarely visited by a policy. Hence, this way does not consider the real
dynamics of the Markov process under the given policy.
Shiyu Zhao 16 / 69

## 第52页

Objective function
The rst way is to use a uniform distribution.
That is to treat all the states to be equally important by setting the
probability of each state as 1=jSj.
In this case, the objective function becomes
J(w) =E[(v(S) ^v(S;w))2] =1
jSjX
s2S(v(s) ^v(s;w))2:
Drawback:
- The states may not be equally important. For example, some states may
be rarely visited by a policy. Hence, this way does not consider the real
dynamics of the Markov process under the given policy.
Shiyu Zhao 16 / 69

## 第53页

Objective function
The second way is to use the stationary distribution.
Stationary distribution is an important concept that will be frequently used
in this course. It describes the long-run behavior of a Markov process.
Letfd(s)gs2Sdenote the stationary distribution of the Markov process
under policy . By denition, d(s)0andP
s2Sd(s) = 1 .
The objective function can be rewritten as
J(w) =E[(v(S) ^v(S;w))2] =X
s2Sd(s)(v(s) ^v(s;w))2:
This function is a weighted squared error.
Since more frequently visited states have higher values of d(s), their weights
in the objective function are also higher than those rarely visited states.
Shiyu Zhao 17 / 69

## 第54页

Objective function
The second way is to use the stationary distribution.
Stationary distribution is an important concept that will be frequently used
in this course. It describes the long-run behavior of a Markov process.
Letfd(s)gs2Sdenote the stationary distribution of the Markov process
under policy . By denition, d(s)0andP
s2Sd(s) = 1 .
The objective function can be rewritten as
J(w) =E[(v(S) ^v(S;w))2] =X
s2Sd(s)(v(s) ^v(s;w))2:
This function is a weighted squared error.
Since more frequently visited states have higher values of d(s), their weights
in the objective function are also higher than those rarely visited states.
Shiyu Zhao 17 / 69

## 第55页

Objective function
The second way is to use the stationary distribution.
Stationary distribution is an important concept that will be frequently used
in this course. It describes the long-run behavior of a Markov process.
Letfd(s)gs2Sdenote the stationary distribution of the Markov process
under policy . By denition, d(s)0andP
s2Sd(s) = 1 .
The objective function can be rewritten as
J(w) =E[(v(S) ^v(S;w))2] =X
s2Sd(s)(v(s) ^v(s;w))2:
This function is a weighted squared error.
Since more frequently visited states have higher values of d(s), their weights
in the objective function are also higher than those rarely visited states.
Shiyu Zhao 17 / 69

## 第56页

Objective function
The second way is to use the stationary distribution.
Stationary distribution is an important concept that will be frequently used
in this course. It describes the long-run behavior of a Markov process.
Letfd(s)gs2Sdenote the stationary distribution of the Markov process
under policy . By denition, d(s)0andP
s2Sd(s) = 1 .
The objective function can be rewritten as
J(w) =E[(v(S) ^v(S;w))2] =X
s2Sd(s)(v(s) ^v(s;w))2:
This function is a weighted squared error.
Since more frequently visited states have higher values of d(s), their weights
in the objective function are also higher than those rarely visited states.
Shiyu Zhao 17 / 69

## 第57页

Objective function
The second way is to use the stationary distribution.
Stationary distribution is an important concept that will be frequently used
in this course. It describes the long-run behavior of a Markov process.
Letfd(s)gs2Sdenote the stationary distribution of the Markov process
under policy . By denition, d(s)0andP
s2Sd(s) = 1 .
The objective function can be rewritten as
J(w) =E[(v(S) ^v(S;w))2] =X
s2Sd(s)(v(s) ^v(s;w))2:
This function is a weighted squared error.
Since more frequently visited states have higher values of d(s), their weights
in the objective function are also higher than those rarely visited states.
Shiyu Zhao 17 / 69

## 第58页

Objective function { Stationary distribution
More explanation about stationary distribution:
Distribution : Distribution of the state
Stationary : Long-run behavior
Summary : after the agent runs a long time following a policy, the probability
that the agent is at any state can be described by this distribution.
Remarks:
Stationary distribution is also called steady-state distribution, or limiting
distribution.
It is critical to understand the value function method.
It is also important for the policy gradient method in the next lecture.
Shiyu Zhao 18 / 69

## 第59页

Objective function { Stationary distribution
More explanation about stationary distribution:
Distribution : Distribution of the state
Stationary : Long-run behavior
Summary : after the agent runs a long time following a policy, the probability
that the agent is at any state can be described by this distribution.
Remarks:
Stationary distribution is also called steady-state distribution, or limiting
distribution.
It is critical to understand the value function method.
It is also important for the policy gradient method in the next lecture.
Shiyu Zhao 18 / 69

## 第60页

Objective function { Stationary distribution
More explanation about stationary distribution:
Distribution : Distribution of the state
Stationary : Long-run behavior
Summary : after the agent runs a long time following a policy, the probability
that the agent is at any state can be described by this distribution.
Remarks:
Stationary distribution is also called steady-state distribution, or limiting
distribution.
It is critical to understand the value function method.
It is also important for the policy gradient method in the next lecture.
Shiyu Zhao 18 / 69

## 第61页

Objective function { Stationary distribution
More explanation about stationary distribution:
Distribution : Distribution of the state
Stationary : Long-run behavior
Summary : after the agent runs a long time following a policy, the probability
that the agent is at any state can be described by this distribution.
Remarks:
Stationary distribution is also called steady-state distribution, or limiting
distribution.
It is critical to understand the value function method.
It is also important for the policy gradient method in the next lecture.
Shiyu Zhao 18 / 69

## 第62页

Objective function - Stationary distribution
Illustrative example:
Given a policy shown in the gure.
Letn(s)denote the number of times that shas been visited in a very long
episode generated by .
Then,d(s)can be approximated by
d(s)n(s)P
s02Sn(s0)
1 2
1
2
0200 400 600 8001000
Step index00.20.40.60.8Percentage of each state visiteds1
s2
s3
s4Figure: Long-run behavior of an -greedy policy with = 0:5.
Shiyu Zhao 19 / 69

## 第63页

Objective function - Stationary distribution
Illustrative example:
Given a policy shown in the gure.
Letn(s)denote the number of times that shas been visited in a very long
episode generated by .
Then,d(s)can be approximated by
d(s)n(s)P
s02Sn(s0)
1 2
1
2
0200 400 600 8001000
Step index00.20.40.60.8Percentage of each state visiteds1
s2
s3
s4Figure: Long-run behavior of an -greedy policy with = 0:5.
Shiyu Zhao 19 / 69

## 第64页

Objective function - Stationary distribution
Illustrative example:
Given a policy shown in the gure.
Letn(s)denote the number of times that shas been visited in a very long
episode generated by .
Then,d(s)can be approximated by
d(s)n(s)P
s02Sn(s0)
1 2
1
2
0200 400 600 8001000
Step index00.20.40.60.8Percentage of each state visiteds1
s2
s3
s4
Figure: Long-run behavior of an -greedy policy with = 0:5.
Shiyu Zhao 19 / 69

## 第65页

Objective function - Stationary distribution
The converged values can be predicted because they are the entries of d:
dT
=dT
P
For this example, we have Pas
P=2
66640:3 0:1 0:6 0
0:1 0:3 0 0:6
0:1 0 0:3 0:6
0 0:1 0:1 0:83
7775:
It can be calculated that the left eigenvector for the eigenvalue of one is
d=h
0:0345;0:1084;0:1330;0:7241iT
A comprehensive introduction can be found in my book.
Shiyu Zhao 20 / 69

## 第66页

Objective function - Stationary distribution
The converged values can be predicted because they are the entries of d:
dT
=dT
P
For this example, we have Pas
P=2
66640:3 0:1 0:6 0
0:1 0:3 0 0:6
0:1 0 0:3 0:6
0 0:1 0:1 0:83
7775:
It can be calculated that the left eigenvector for the eigenvalue of one is
d=h
0:0345;0:1084;0:1330;0:7241iT
A comprehensive introduction can be found in my book.
Shiyu Zhao 20 / 69

## 第67页

Objective function - Stationary distribution
The converged values can be predicted because they are the entries of d:
dT
=dT
P
For this example, we have Pas
P=2
66640:3 0:1 0:6 0
0:1 0:3 0 0:6
0:1 0 0:3 0:6
0 0:1 0:1 0:83
7775:
It can be calculated that the left eigenvector for the eigenvalue of one is
d=h
0:0345;0:1084;0:1330;0:7241iT
A comprehensive introduction can be found in my book.
Shiyu Zhao 20 / 69

## 第68页

Objective function - Stationary distribution
The converged values can be predicted because they are the entries of d:
dT
=dT
P
For this example, we have Pas
P=2
66640:3 0:1 0:6 0
0:1 0:3 0 0:6
0:1 0 0:3 0:6
0 0:1 0:1 0:83
7775:
It can be calculated that the left eigenvector for the eigenvalue of one is
d=h
0:0345;0:1084;0:1330;0:7241iT
A comprehensive introduction can be found in my book.
Shiyu Zhao 20 / 69

## 第69页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 21 / 69

## 第70页

Optimization algorithms
While we have the objective function, the next step is to optimize it.
To minimize the objective function J(w), we can use the gradient-descent
algorithm:
wk+1=wk krwJ(wk)
The true gradient is
rwJ(w) =rwE[(v(S) ^v(S;w))2]=E[rw(v(S) ^v(S;w))2]
= 2E[(v(S) ^v(S;w))( rw^v(S;w))]
= 2E[(v(S) ^v(S;w))rw^v(S;w)]
The true gradient above involves the calculation of an expectation.
Shiyu Zhao 22 / 69

## 第71页

Optimization algorithms
While we have the objective function, the next step is to optimize it.
To minimize the objective function J(w), we can use the gradient-descent
algorithm:
wk+1=wk krwJ(wk)
The true gradient is
rwJ(w) =rwE[(v(S) ^v(S;w))2]=E[rw(v(S) ^v(S;w))2]
= 2E[(v(S) ^v(S;w))( rw^v(S;w))]
= 2E[(v(S) ^v(S;w))rw^v(S;w)]
The true gradient above involves the calculation of an expectation.
Shiyu Zhao 22 / 69

## 第72页

Optimization algorithms
While we have the objective function, the next step is to optimize it.
To minimize the objective function J(w), we can use the gradient-descent
algorithm:
wk+1=wk krwJ(wk)
The true gradient is
rwJ(w) =rwE[(v(S) ^v(S;w))2]=E[rw(v(S) ^v(S;w))2]
= 2E[(v(S) ^v(S;w))( rw^v(S;w))]
= 2E[(v(S) ^v(S;w))rw^v(S;w)]
The true gradient above involves the calculation of an expectation.
Shiyu Zhao 22 / 69

## 第73页

Optimization algorithms
While we have the objective function, the next step is to optimize it.
To minimize the objective function J(w), we can use the gradient-descent
algorithm:
wk+1=wk krwJ(wk)
The true gradient is
rwJ(w) =rwE[(v(S) ^v(S;w))2]
=E[rw(v(S) ^v(S;w))2]= 2E[(v(S) ^v(S;w))( rw^v(S;w))]
= 2E[(v(S) ^v(S;w))rw^v(S;w)]
The true gradient above involves the calculation of an expectation.
Shiyu Zhao 22 / 69

## 第74页

Optimization algorithms
While we have the objective function, the next step is to optimize it.
To minimize the objective function J(w), we can use the gradient-descent
algorithm:
wk+1=wk krwJ(wk)
The true gradient is
rwJ(w) =rwE[(v(S) ^v(S;w))2]
=E[rw(v(S) ^v(S;w))2]
= 2E[(v(S) ^v(S;w))( rw^v(S;w))]= 2E[(v(S) ^v(S;w))rw^v(S;w)]
The true gradient above involves the calculation of an expectation.
Shiyu Zhao 22 / 69

## 第75页

Optimization algorithms
While we have the objective function, the next step is to optimize it.
To minimize the objective function J(w), we can use the gradient-descent
algorithm:
wk+1=wk krwJ(wk)
The true gradient is
rwJ(w) =rwE[(v(S) ^v(S;w))2]
=E[rw(v(S) ^v(S;w))2]
= 2E[(v(S) ^v(S;w))( rw^v(S;w))]
= 2E[(v(S) ^v(S;w))rw^v(S;w)]The true gradient above involves the calculation of an expectation.
Shiyu Zhao 22 / 69

## 第76页

Optimization algorithms
While we have the objective function, the next step is to optimize it.
To minimize the objective function J(w), we can use the gradient-descent
algorithm:
wk+1=wk krwJ(wk)
The true gradient is
rwJ(w) =rwE[(v(S) ^v(S;w))2]
=E[rw(v(S) ^v(S;w))2]
= 2E[(v(S) ^v(S;w))( rw^v(S;w))]
= 2E[(v(S) ^v(S;w))rw^v(S;w)]
The true gradient above involves the calculation of an expectation.
Shiyu Zhao 22 / 69

## 第77页

Optimization algorithms
We can use the stochastic gradient to replace the true gradient:
wk+1=wk+kE[(v(S) ^v(S;w))rw^v(S;w)]
+
wt+1=wt+t(v(st) ^v(st;wt))rw^v(st;wt)
wherestis a sample of S. Here, 2tis merged to t.
The samples are expected to satisfy the stationary distribution. In practice,
they may not satisfy.
This algorithm is not implementable because it requires the true state value
v, which is the unknown to be estimated.
We can replace v(st)with an approximation so that the algorithm is
implementable.
Shiyu Zhao 23 / 69

## 第78页

Optimization algorithms
We can use the stochastic gradient to replace the true gradient:
wk+1=wk+kE[(v(S) ^v(S;w))rw^v(S;w)]
+
wt+1=wt+t(v(st) ^v(st;wt))rw^v(st;wt)
wherestis a sample of S. Here, 2tis merged to t.
The samples are expected to satisfy the stationary distribution. In practice,
they may not satisfy.
This algorithm is not implementable because it requires the true state value
v, which is the unknown to be estimated.
We can replace v(st)with an approximation so that the algorithm is
implementable.
Shiyu Zhao 23 / 69

## 第79页

Optimization algorithms
We can use the stochastic gradient to replace the true gradient:
wk+1=wk+kE[(v(S) ^v(S;w))rw^v(S;w)]
+
wt+1=wt+t(v(st) ^v(st;wt))rw^v(st;wt)
wherestis a sample of S. Here, 2tis merged to t.
The samples are expected to satisfy the stationary distribution. In practice,
they may not satisfy.
This algorithm is not implementable because it requires the true state value
v, which is the unknown to be estimated.
We can replace v(st)with an approximation so that the algorithm is
implementable.
Shiyu Zhao 23 / 69

## 第80页

Optimization algorithms
We can use the stochastic gradient to replace the true gradient:
wk+1=wk+kE[(v(S) ^v(S;w))rw^v(S;w)]
+
wt+1=wt+t(v(st) ^v(st;wt))rw^v(st;wt)
wherestis a sample of S. Here, 2tis merged to t.
The samples are expected to satisfy the stationary distribution. In practice,
they may not satisfy.
This algorithm is not implementable because it requires the true state value
v, which is the unknown to be estimated.
We can replace v(st)with an approximation so that the algorithm is
implementable.
Shiyu Zhao 23 / 69

## 第81页

Optimization algorithms
In particular,
First, Monte Carlo learning with function approximation
Letgtbe the discounted return starting from stin the episode. Then, gtcan
be used to approximate v(st). The algorithm becomes
wt+1=wt+t(gt ^v(st;wt))rw^v(st;wt):
Second, TD learning with function approximation
By the spirit of TD learning, rt+1+
^v(st+1;wt)can be viewed as an
approximation of v(st). Then, the algorithm becomes
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt):
Shiyu Zhao 24 / 69

## 第82页

Optimization algorithms
In particular,
First, Monte Carlo learning with function approximation
Letgtbe the discounted return starting from stin the episode. Then, gtcan
be used to approximate v(st). The algorithm becomes
wt+1=wt+t(gt ^v(st;wt))rw^v(st;wt):
Second, TD learning with function approximation
By the spirit of TD learning, rt+1+
^v(st+1;wt)can be viewed as an
approximation of v(st). Then, the algorithm becomes
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt):
Shiyu Zhao 24 / 69

## 第83页

Optimization algorithms
In particular,
First, Monte Carlo learning with function approximation
Letgtbe the discounted return starting from stin the episode. Then, gtcan
be used to approximate v(st). The algorithm becomes
wt+1=wt+t(gt ^v(st;wt))rw^v(st;wt):
Second, TD learning with function approximation
By the spirit of TD learning, rt+1+
^v(st+1;wt)can be viewed as an
approximation of v(st). Then, the algorithm becomes
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt):
Shiyu Zhao 24 / 69

## 第84页

Optimization algorithms
In particular,
First, Monte Carlo learning with function approximation
Letgtbe the discounted return starting from stin the episode. Then, gtcan
be used to approximate v(st). The algorithm becomes
wt+1=wt+t(gt ^v(st;wt))rw^v(st;wt):
Second, TD learning with function approximation
By the spirit of TD learning, rt+1+
^v(st+1;wt)can be viewed as an
approximation of v(st). Then, the algorithm becomes
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt):
Shiyu Zhao 24 / 69

## 第85页

Optimization algorithms
In particular,
First, Monte Carlo learning with function approximation
Letgtbe the discounted return starting from stin the episode. Then, gtcan
be used to approximate v(st). The algorithm becomes
wt+1=wt+t(gt ^v(st;wt))rw^v(st;wt):
Second, TD learning with function approximation
By the spirit of TD learning, rt+1+
^v(st+1;wt)can be viewed as an
approximation of v(st). Then, the algorithm becomes
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt):
Shiyu Zhao 24 / 69

## 第86页

Optimization algorithms
Pseudocode: TD learning of state values with function approximation
Initialization: A function ^v(s;w)that is dierentiable in w. Initial parameter w0.
Goal: Learn the true state values of a given policy .
For each episodef(st;rt+1;st+1)gtgenerated by , do
For each sample (st;rt+1;st+1), do
In the general case,
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)In the linear case,
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st)
It can only estimate the state values of a given policy, but it is important to
understand other algorithms introduced later.
Shiyu Zhao 25 / 69

## 第87页

Optimization algorithms
Pseudocode: TD learning of state values with function approximation
Initialization: A function ^v(s;w)that is dierentiable in w. Initial parameter w0.
Goal: Learn the true state values of a given policy .
For each episodef(st;rt+1;st+1)gtgenerated by , do
For each sample (st;rt+1;st+1), do
In the general case,
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
In the linear case,
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st)
It can only estimate the state values of a given policy, but it is important to
understand other algorithms introduced later.
Shiyu Zhao 25 / 69

## 第88页

Optimization algorithms
Pseudocode: TD learning of state values with function approximation
Initialization: A function ^v(s;w)that is dierentiable in w. Initial parameter w0.
Goal: Learn the true state values of a given policy .
For each episodef(st;rt+1;st+1)gtgenerated by , do
For each sample (st;rt+1;st+1), do
In the general case,
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
In the linear case,
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st)
It can only estimate the state values of a given policy, but it is important to
understand other algorithms introduced later.
Shiyu Zhao 25 / 69

## 第89页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 26 / 69

## 第90页

Selection of function approximators
An important question that has not been answered: How to select the function
^v(s;w)?
The rst approach, which was widely used before , is to use a linear function
^v(s;w) =T(s)w
Here,(s)is the feature vector, which can be a polynomial basis, Fourier
basis, ... (see my book for details). We have seen in the motivating example
and will see again in the illustrative examples later.
The second approach, which is widely used nowadays , is to use a neural
network as a nonlinear function approximator.
- For example, the input is s, the output is ^v(s;w), and the parameter is w.
Shiyu Zhao 27 / 69

## 第91页

Selection of function approximators
An important question that has not been answered: How to select the function
^v(s;w)?
The rst approach, which was widely used before , is to use a linear function
^v(s;w) =T(s)w
Here,(s)is the feature vector, which can be a polynomial basis, Fourier
basis, ... (see my book for details). We have seen in the motivating example
and will see again in the illustrative examples later.
The second approach, which is widely used nowadays , is to use a neural
network as a nonlinear function approximator.
- For example, the input is s, the output is ^v(s;w), and the parameter is w.
Shiyu Zhao 27 / 69

## 第92页

Selection of function approximators
An important question that has not been answered: How to select the function
^v(s;w)?
The rst approach, which was widely used before , is to use a linear function
^v(s;w) =T(s)w
Here,(s)is the feature vector, which can be a polynomial basis, Fourier
basis, ... (see my book for details). We have seen in the motivating example
and will see again in the illustrative examples later.
The second approach, which is widely used nowadays , is to use a neural
network as a nonlinear function approximator.
- For example, the input is s, the output is ^v(s;w), and the parameter is w.
Shiyu Zhao 27 / 69

## 第93页

Selection of function approximators
An important question that has not been answered: How to select the function
^v(s;w)?
The rst approach, which was widely used before , is to use a linear function
^v(s;w) =T(s)w
Here,(s)is the feature vector, which can be a polynomial basis, Fourier
basis, ... (see my book for details). We have seen in the motivating example
and will see again in the illustrative examples later.
The second approach, which is widely used nowadays , is to use a neural
network as a nonlinear function approximator.
- For example, the input is s, the output is ^v(s;w), and the parameter is w.
Shiyu Zhao 27 / 69

## 第94页

Selection of function approximators
An important question that has not been answered: How to select the function
^v(s;w)?
The rst approach, which was widely used before , is to use a linear function
^v(s;w) =T(s)w
Here,(s)is the feature vector, which can be a polynomial basis, Fourier
basis, ... (see my book for details). We have seen in the motivating example
and will see again in the illustrative examples later.
The second approach, which is widely used nowadays , is to use a neural
network as a nonlinear function approximator.
- For example, the input is s, the output is ^v(s;w), and the parameter is w.
Shiyu Zhao 27 / 69

## 第95页

Selection of function approximators
An important question that has not been answered: How to select the function
^v(s;w)?
The rst approach, which was widely used before , is to use a linear function
^v(s;w) =T(s)w
Here,(s)is the feature vector, which can be a polynomial basis, Fourier
basis, ... (see my book for details). We have seen in the motivating example
and will see again in the illustrative examples later.
The second approach, which is widely used nowadays , is to use a neural
network as a nonlinear function approximator.
- For example, the input is s, the output is ^v(s;w), and the parameter is w.
Shiyu Zhao 27 / 69

## 第96页

Linear function approximation
In the linear case where ^v(s;w) =T(s)w, we have
rw^v(s;w) =(s):
Substituting the gradient into the TD algorithm
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
yields
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st);
which is the algorithm of TD learning with linear function approximation.
It is called TD-Linear in our course.
Shiyu Zhao 28 / 69

## 第97页

Linear function approximation
In the linear case where ^v(s;w) =T(s)w, we have
rw^v(s;w) =(s):
Substituting the gradient into the TD algorithm
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
yields
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st);
which is the algorithm of TD learning with linear function approximation.
It is called TD-Linear in our course.
Shiyu Zhao 28 / 69

## 第98页

Linear function approximation
In the linear case where ^v(s;w) =T(s)w, we have
rw^v(s;w) =(s):
Substituting the gradient into the TD algorithm
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
yields
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st);
which is the algorithm of TD learning with linear function approximation.
It is called TD-Linear in our course.
Shiyu Zhao 28 / 69

## 第99页

Linear function approximation
In the linear case where ^v(s;w) =T(s)w, we have
rw^v(s;w) =(s):
Substituting the gradient into the TD algorithm
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
yields
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st);
which is the algorithm of TD learning with linear function approximation.
It is called TD-Linear in our course.
Shiyu Zhao 28 / 69

## 第100页

Linear function approximation
In the linear case where ^v(s;w) =T(s)w, we have
rw^v(s;w) =(s):
Substituting the gradient into the TD algorithm
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
yields
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st);
which is the algorithm of TD learning with linear function approximation.
It is called TD-Linear in our course.
Shiyu Zhao 28 / 69

## 第101页

Linear function approximation
Disadvantages of linear function methods:
- Dicult to select appropriate feature vectors.
Advantages of linear function methods:
- The theoretical properties of the TD algorithm in the linear case can be
much better understood than in the nonlinear case.
- Linear function approximation is still powerful in the sense that the tabular
representation is a special case of linear function representation.
Shiyu Zhao 29 / 69

## 第102页

Linear function approximation
Disadvantages of linear function methods:
- Dicult to select appropriate feature vectors.
Advantages of linear function methods:
- The theoretical properties of the TD algorithm in the linear case can be
much better understood than in the nonlinear case.
- Linear function approximation is still powerful in the sense that the tabular
representation is a special case of linear function representation.
Shiyu Zhao 29 / 69

## 第103页

Linear function approximation
Disadvantages of linear function methods:
- Dicult to select appropriate feature vectors.
Advantages of linear function methods:
- The theoretical properties of the TD algorithm in the linear case can be
much better understood than in the nonlinear case.
- Linear function approximation is still powerful in the sense that the tabular
representation is a special case of linear function representation.
Shiyu Zhao 29 / 69

## 第104页

Linear function approximation
We next show that tabular representation is a special case of linear function
representation. Hence, the tabular and function representations are unied!
Consider a special feature vector for state s:
(s) =es2RjSj;
whereesis a vector with the sth entry as 1 and the others as 0.
In this case,
^v(s;w) =T(s)w=eT
sw=w(s);
wherew(s)is thesth entry ofw.
Shiyu Zhao 30 / 69

## 第105页

Linear function approximation
We next show that tabular representation is a special case of linear function
representation. Hence, the tabular and function representations are unied!
Consider a special feature vector for state s:
(s) =es2RjSj;
whereesis a vector with the sth entry as 1 and the others as 0.
In this case,
^v(s;w) =T(s)w=eT
sw=w(s);
wherew(s)is thesth entry ofw.
Shiyu Zhao 30 / 69

## 第106页

Linear function approximation
We next show that tabular representation is a special case of linear function
representation. Hence, the tabular and function representations are unied!
Consider a special feature vector for state s:
(s) =es2RjSj;
whereesis a vector with the sth entry as 1 and the others as 0.
In this case,
^v(s;w) =T(s)w=eT
sw=w(s);
wherew(s)is thesth entry ofw.
Shiyu Zhao 30 / 69

## 第107页

Linear function approximation
Recall that the TD-Linear algorithm is
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st);
When(st) =es, the above algorithm becomes
wt+1=wt+t(rt+1+
wt(st+1) wt(st))est:
This is a vector equation that merely updates the stth entry ofwt.
Multiplying eT
ston both sides of the equation gives
wt+1(st) =wt(st) +t(rt+1+
wt(st+1) wt(st));
which is exactly the tabular TD algorithm (which is called TD-Table here).
Summary: TD-Linear becomes TD-Table if we select a special feature vector.
Shiyu Zhao 31 / 69

## 第108页

Linear function approximation
Recall that the TD-Linear algorithm is
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st);
When(st) =es, the above algorithm becomes
wt+1=wt+t(rt+1+
wt(st+1) wt(st))est:
This is a vector equation that merely updates the stth entry ofwt.
Multiplying eT
ston both sides of the equation gives
wt+1(st) =wt(st) +t(rt+1+
wt(st+1) wt(st));
which is exactly the tabular TD algorithm (which is called TD-Table here).
Summary: TD-Linear becomes TD-Table if we select a special feature vector.
Shiyu Zhao 31 / 69

## 第109页

Linear function approximation
Recall that the TD-Linear algorithm is
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st);
When(st) =es, the above algorithm becomes
wt+1=wt+t(rt+1+
wt(st+1) wt(st))est:
This is a vector equation that merely updates the stth entry ofwt.
Multiplying eT
ston both sides of the equation gives
wt+1(st) =wt(st) +t(rt+1+
wt(st+1) wt(st));
which is exactly the tabular TD algorithm (which is called TD-Table here).
Summary: TD-Linear becomes TD-Table if we select a special feature vector.
Shiyu Zhao 31 / 69

## 第110页

Linear function approximation
Recall that the TD-Linear algorithm is
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st);
When(st) =es, the above algorithm becomes
wt+1=wt+t(rt+1+
wt(st+1) wt(st))est:
This is a vector equation that merely updates the stth entry ofwt.
Multiplying eT
ston both sides of the equation gives
wt+1(st) =wt(st) +t(rt+1+
wt(st+1) wt(st));
which is exactly the tabular TD algorithm (which is called TD-Table here).
Summary: TD-Linear becomes TD-Table if we select a special feature vector.
Shiyu Zhao 31 / 69

## 第111页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 32 / 69

## 第112页

Illustrative examples
Consider a 5x5 grid-world example:
1 2 3 4 5
1
2
3
4
5
Given a policy: (ajs) = 0:2for anys;a
Our aim is to estimate the state values of this policy (policy evaluation
problem).
There are 25 state values in total. We next show that we can use less than
25 parameters to approximate 25 state values.
Setrforbidden =rboundary = 1,rtarget = 1, and
= 0:9.
Shiyu Zhao 33 / 69

## 第113页

Illustrative examples
Consider a 5x5 grid-world example:
1 2 3 4 5
1
2
3
4
5
Given a policy: (ajs) = 0:2for anys;a
Our aim is to estimate the state values of this policy (policy evaluation
problem).
There are 25 state values in total. We next show that we can use less than
25 parameters to approximate 25 state values.
Setrforbidden =rboundary = 1,rtarget = 1, and
= 0:9.
Shiyu Zhao 33 / 69

## 第114页

Illustrative examples
Consider a 5x5 grid-world example:
1 2 3 4 5
1
2
3
4
5
Given a policy: (ajs) = 0:2for anys;a
Our aim is to estimate the state values of this policy (policy evaluation
problem).
There are 25 state values in total. We next show that we can use less than
25 parameters to approximate 25 state values.
Setrforbidden =rboundary = 1,rtarget = 1, and
= 0:9.
Shiyu Zhao 33 / 69

## 第115页

Illustrative examples
Consider a 5x5 grid-world example:
1 2 3 4 5
1
2
3
4
5
Given a policy: (ajs) = 0:2for anys;a
Our aim is to estimate the state values of this policy (policy evaluation
problem).
There are 25 state values in total. We next show that we can use less than
25 parameters to approximate 25 state values.
Setrforbidden =rboundary = 1,rtarget = 1, and
= 0:9.
Shiyu Zhao 33 / 69

## 第116页

Illustrative examples
Consider a 5x5 grid-world example:
1 2 3 4 5
1
2
3
4
5
Given a policy: (ajs) = 0:2for anys;a
Our aim is to estimate the state values of this policy (policy evaluation
problem).
There are 25 state values in total. We next show that we can use less than
25 parameters to approximate 25 state values.
Setrforbidden =rboundary = 1,rtarget = 1, and
= 0:9.
Shiyu Zhao 33 / 69

## 第117页

Illustrative examples
Ground truth:
The true state values and the 3D visualization
1 2 3 4 5
1
2
3
4
5
1 2 3 4 5
1
2
3
4
5-3.8-3.8-3.6-3.1-3.2
-3.8-3.8-3.8-3.1-2.9
-3.6-3.9-3.4-3.2-2.9
-3.9-3.6-3.4-2.9-3.2
-4.5-4.2-3.4-3.4-3.5
Experience samples:
500 episodes were generated following the given policy.
Each episode has 500 steps and starts from a randomly selected state-action
pair following a uniform distribution.
Shiyu Zhao 34 / 69

## 第118页

Illustrative examples
Ground truth:
The true state values and the 3D visualization
1 2 3 4 5
1
2
3
4
5
1 2 3 4 5
1
2
3
4
5-3.8-3.8-3.6-3.1-3.2
-3.8-3.8-3.8-3.1-2.9
-3.6-3.9-3.4-3.2-2.9
-3.9-3.6-3.4-2.9-3.2
-4.5-4.2-3.4-3.4-3.5
Experience samples:
500 episodes were generated following the given policy.
Each episode has 500 steps and starts from a randomly selected state-action
pair following a uniform distribution.
Shiyu Zhao 34 / 69

## 第119页

Illustrative examples
Ground truth:
The true state values and the 3D visualization
1 2 3 4 5
1
2
3
4
5
1 2 3 4 5
1
2
3
4
5-3.8-3.8-3.6-3.1-3.2
-3.8-3.8-3.8-3.1-2.9
-3.6-3.9-3.4-3.2-2.9
-3.9-3.6-3.4-2.9-3.2
-4.5-4.2-3.4-3.4-3.5
Experience samples:
500 episodes were generated following the given policy.
Each episode has 500 steps and starts from a randomly selected state-action
pair following a uniform distribution.
Shiyu Zhao 34 / 69

## 第120页

Illustrative examples
TD-Table:
For comparison, the results by the tabular TD algorithm (called TD-Table
here):
0100200300400500
Episode index01234State value error (RMSE)TD-Table: =0.005
Shiyu Zhao 35 / 69

## 第121页

Illustrative examples
TD-Linear:
How to apply the TD-Linear algorithm?
- Feature vector selection:
(s) =2
641
x
y3
752R3:
- In this case, the approximated state value is
^v(s;w) =T(s)w= [1;x;y]2
64w1
w2
w33
75=w1+w2x+w3y:
Remark:(s)can also be dened as (s) = [x;y;1]T, where the order of
the elements does not matter.
Shiyu Zhao 36 / 69

## 第122页

Illustrative examples
TD-Linear:
How to apply the TD-Linear algorithm?
- Feature vector selection:
(s) =2
641
x
y3
752R3:
- In this case, the approximated state value is
^v(s;w) =T(s)w= [1;x;y]2
64w1
w2
w33
75=w1+w2x+w3y:
Remark:(s)can also be dened as (s) = [x;y;1]T, where the order of
the elements does not matter.
Shiyu Zhao 36 / 69

## 第123页

Illustrative examples
TD-Linear:
How to apply the TD-Linear algorithm?
- Feature vector selection:
(s) =2
641
x
y3
752R3:
- In this case, the approximated state value is
^v(s;w) =T(s)w= [1;x;y]2
64w1
w2
w33
75=w1+w2x+w3y:
Remark:(s)can also be dened as (s) = [x;y;1]T, where the order of
the elements does not matter.
Shiyu Zhao 36 / 69

## 第124页

Illustrative examples
TD-Linear:
How to apply the TD-Linear algorithm?
- Feature vector selection:
(s) =2
641
x
y3
752R3:
- In this case, the approximated state value is
^v(s;w) =T(s)w= [1;x;y]2
64w1
w2
w33
75=w1+w2x+w3y:
Remark:(s)can also be dened as (s) = [x;y;1]T, where the order of
the elements does not matter.
Shiyu Zhao 36 / 69

## 第125页

Illustrative examples
TD-Linear:
Results by the TD-Linear algorithm:
0100200300400500
Episode index012345State value error (RMSE)TD-Linear: =0.0005
The trend is right, but there are errors due to limited approximation ability!
We are trying to use a plane to approximate a non-plane surface!
Shiyu Zhao 37 / 69

## 第126页

Illustrative examples
TD-Linear:
Results by the TD-Linear algorithm:
0100200300400500
Episode index012345State value error (RMSE)TD-Linear: =0.0005
The trend is right, but there are errors due to limited approximation ability!
We are trying to use a plane to approximate a non-plane surface!
Shiyu Zhao 37 / 69

## 第127页

Illustrative examples
To enhance the approximation ability, we can use high-order feature vectors
and hence more parameters.
For example, we can consider
(s) = [1;x;y;x2;y2;xy]T2R6:
In this case,
^v(s;w) =T(s)w=w1+w2x+w3y+w4x2+w5y2+w6xy
which corresponds to a quadratic surface.
We can further increase the dimension of the feature vector:
(s) = [1;x;y;x2;y2;xy;x3;y3;x2y;xy2]T2R10:
Shiyu Zhao 38 / 69

## 第128页

Illustrative examples
To enhance the approximation ability, we can use high-order feature vectors
and hence more parameters.
For example, we can consider
(s) = [1;x;y;x2;y2;xy]T2R6:
In this case,
^v(s;w) =T(s)w=w1+w2x+w3y+w4x2+w5y2+w6xy
which corresponds to a quadratic surface.
We can further increase the dimension of the feature vector:
(s) = [1;x;y;x2;y2;xy;x3;y3;x2y;xy2]T2R10:
Shiyu Zhao 38 / 69

## 第129页

Illustrative examples
To enhance the approximation ability, we can use high-order feature vectors
and hence more parameters.
For example, we can consider
(s) = [1;x;y;x2;y2;xy]T2R6:
In this case,
^v(s;w) =T(s)w=w1+w2x+w3y+w4x2+w5y2+w6xy
which corresponds to a quadratic surface.
We can further increase the dimension of the feature vector:
(s) = [1;x;y;x2;y2;xy;x3;y3;x2y;xy2]T2R10:
Shiyu Zhao 38 / 69

## 第130页

Illustrative examples
To enhance the approximation ability, we can use high-order feature vectors
and hence more parameters.
For example, we can consider
(s) = [1;x;y;x2;y2;xy]T2R6:
In this case,
^v(s;w) =T(s)w=w1+w2x+w3y+w4x2+w5y2+w6xy
which corresponds to a quadratic surface.
We can further increase the dimension of the feature vector:
(s) = [1;x;y;x2;y2;xy;x3;y3;x2y;xy2]T2R10:
Shiyu Zhao 38 / 69

## 第131页

Illustrative examples
Results by the TD-Linear algorithm with higher-order feature vectors:
0100200300400500
Episode index012345State value error (RMSE)TD-Linear: =0.0005
The above gure: (s)2R6
0100200300400500
Episode index00.511.522.533.5State value error (RMSE)TD-Linear: =0.0005The above gure: (s)2R10
More examples and features are given in the book.
Shiyu Zhao 39 / 69

## 第132页

Illustrative examples
Results by the TD-Linear algorithm with higher-order feature vectors:
0100200300400500
Episode index012345State value error (RMSE)TD-Linear: =0.0005
The above gure: (s)2R6
0100200300400500
Episode index00.511.522.533.5State value error (RMSE)TD-Linear: =0.0005
The above gure: (s)2R10
More examples and features are given in the book.
Shiyu Zhao 39 / 69

## 第133页

Illustrative examples
Results by the TD-Linear algorithm with higher-order feature vectors:
0100200300400500
Episode index012345State value error (RMSE)TD-Linear: =0.0005
The above gure: (s)2R6
0100200300400500
Episode index00.511.522.533.5State value error (RMSE)TD-Linear: =0.0005
The above gure: (s)2R10
More examples and features are given in the book.
Shiyu Zhao 39 / 69

## 第134页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 40 / 69

## 第135页

Summary of the story
Up to now, we nished the story of TD learning with value function
approximation.
1) This story started from the objective function:
J(w) =E[(v(S) ^v(S;w))2]
The objective function suggests that it is a policy evaluation problem.
2) The gradient-descent algorithm is
wt+1=wt+t(v(st) ^v(st;wt))rw^v(st;wt)
3) The true value function, which is unknown, in the algorithm is replaced by
an approximation, leading to the algorithm:
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
Although this story is very helpful to understand the basic idea, it is not
mathematically rigorous.
Shiyu Zhao 41 / 69

## 第136页

Summary of the story
Up to now, we nished the story of TD learning with value function
approximation.
1) This story started from the objective function:
J(w) =E[(v(S) ^v(S;w))2]
The objective function suggests that it is a policy evaluation problem.
2) The gradient-descent algorithm is
wt+1=wt+t(v(st) ^v(st;wt))rw^v(st;wt)
3) The true value function, which is unknown, in the algorithm is replaced by
an approximation, leading to the algorithm:
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
Although this story is very helpful to understand the basic idea, it is not
mathematically rigorous.
Shiyu Zhao 41 / 69

## 第137页

Summary of the story
Up to now, we nished the story of TD learning with value function
approximation.
1) This story started from the objective function:
J(w) =E[(v(S) ^v(S;w))2]
The objective function suggests that it is a policy evaluation problem.
2) The gradient-descent algorithm is
wt+1=wt+t(v(st) ^v(st;wt))rw^v(st;wt)
3) The true value function, which is unknown, in the algorithm is replaced by
an approximation, leading to the algorithm:
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
Although this story is very helpful to understand the basic idea, it is not
mathematically rigorous.
Shiyu Zhao 41 / 69

## 第138页

Summary of the story
Up to now, we nished the story of TD learning with value function
approximation.
1) This story started from the objective function:
J(w) =E[(v(S) ^v(S;w))2]
The objective function suggests that it is a policy evaluation problem.
2) The gradient-descent algorithm is
wt+1=wt+t(v(st) ^v(st;wt))rw^v(st;wt)
3) The true value function, which is unknown, in the algorithm is replaced by
an approximation, leading to the algorithm:
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
Although this story is very helpful to understand the basic idea, it is not
mathematically rigorous.
Shiyu Zhao 41 / 69

## 第139页

Summary of the story
Up to now, we nished the story of TD learning with value function
approximation.
1) This story started from the objective function:
J(w) =E[(v(S) ^v(S;w))2]
The objective function suggests that it is a policy evaluation problem.
2) The gradient-descent algorithm is
wt+1=wt+t(v(st) ^v(st;wt))rw^v(st;wt)
3) The true value function, which is unknown, in the algorithm is replaced by
an approximation, leading to the algorithm:
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
Although this story is very helpful to understand the basic idea, it is not
mathematically rigorous.
Shiyu Zhao 41 / 69

## 第140页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 42 / 69

## 第141页

Theoretical analysis (optional)
The algorithm
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
does not minimize the following objective function:
J(w) =E[(v(S) ^v(S;w))2]
Shiyu Zhao 43 / 69

## 第142页

Theoretical analysis (optional)
Dierent objective functions:
Objective function 1: True value error
JE(w) =E[(v(S) ^v(S;w))2] =k^v(w) vk2
D
Objective function 2: Bellman error
JBE(w) =k^v(w) (r+
P^v(w))k2
D:=k^v(w) T(^v(w))k2
D;
whereT(x):=r+
Px
Objective function 3: Projected Bellman error
JPBE(w) =k^v(w) MT(^v(w))k2
D;
whereMis a projection matrix.
- The TD-Linear algorithm minimizes the projected Bellman error.
More details are omitted here. Interested readers can check my book.
Shiyu Zhao 44 / 69

## 第143页

Theoretical analysis (optional)
Dierent objective functions:
Objective function 1: True value error
JE(w) =E[(v(S) ^v(S;w))2] =k^v(w) vk2
D
Objective function 2: Bellman error
JBE(w) =k^v(w) (r+
P^v(w))k2
D:=k^v(w) T(^v(w))k2
D;
whereT(x):=r+
Px
Objective function 3: Projected Bellman error
JPBE(w) =k^v(w) MT(^v(w))k2
D;
whereMis a projection matrix.
- The TD-Linear algorithm minimizes the projected Bellman error.
More details are omitted here. Interested readers can check my book.
Shiyu Zhao 44 / 69

## 第144页

Theoretical analysis (optional)
Dierent objective functions:
Objective function 1: True value error
JE(w) =E[(v(S) ^v(S;w))2] =k^v(w) vk2
D
Objective function 2: Bellman error
JBE(w) =k^v(w) (r+
P^v(w))k2
D:=k^v(w) T(^v(w))k2
D;
whereT(x):=r+
Px
Objective function 3: Projected Bellman error
JPBE(w) =k^v(w) MT(^v(w))k2
D;
whereMis a projection matrix.
- The TD-Linear algorithm minimizes the projected Bellman error.
More details are omitted here. Interested readers can check my book.
Shiyu Zhao 44 / 69

## 第145页

Theoretical analysis (optional)
Dierent objective functions:
Objective function 1: True value error
JE(w) =E[(v(S) ^v(S;w))2] =k^v(w) vk2
D
Objective function 2: Bellman error
JBE(w) =k^v(w) (r+
P^v(w))k2
D:=k^v(w) T(^v(w))k2
D;
whereT(x):=r+
Px
Objective function 3: Projected Bellman error
JPBE(w) =k^v(w) MT(^v(w))k2
D;
whereMis a projection matrix.
- The TD-Linear algorithm minimizes the projected Bellman error.
More details are omitted here. Interested readers can check my book.
Shiyu Zhao 44 / 69

## 第146页

Theoretical analysis (optional)
Dierent objective functions:
Objective function 1: True value error
JE(w) =E[(v(S) ^v(S;w))2] =k^v(w) vk2
D
Objective function 2: Bellman error
JBE(w) =k^v(w) (r+
P^v(w))k2
D:=k^v(w) T(^v(w))k2
D;
whereT(x):=r+
Px
Objective function 3: Projected Bellman error
JPBE(w) =k^v(w) MT(^v(w))k2
D;
whereMis a projection matrix.
- The TD-Linear algorithm minimizes the projected Bellman error.
More details are omitted here. Interested readers can check my book.
Shiyu Zhao 44 / 69

## 第147页

Theoretical analysis (optional)
Dierent objective functions:
Objective function 1: True value error
JE(w) =E[(v(S) ^v(S;w))2] =k^v(w) vk2
D
Objective function 2: Bellman error
JBE(w) =k^v(w) (r+
P^v(w))k2
D:=k^v(w) T(^v(w))k2
D;
whereT(x):=r+
Px
Objective function 3: Projected Bellman error
JPBE(w) =k^v(w) MT(^v(w))k2
D;
whereMis a projection matrix.
- The TD-Linear algorithm minimizes the projected Bellman error.
More details are omitted here. Interested readers can check my book.
Shiyu Zhao 44 / 69

## 第148页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 45 / 69

## 第149页

Sarsa with function approximation
So far, we merely considered state value estimation. That is
^v(s)v(s); s2S
To search for optimal policies, we need to estimate action values.
The Sarsa algorithm with value function approximation is
wt+1=wt+th
rt+1+
^q(st+1;at+1;wt) ^q(st;at;wt)i
rw^q(st;at;wt):
This is the same as the algorithm we introduced previously in this lecture
except that ^vis replaced by ^q.
Shiyu Zhao 46 / 69

## 第150页

Sarsa with function approximation
So far, we merely considered state value estimation. That is
^v(s)v(s); s2S
To search for optimal policies, we need to estimate action values.
The Sarsa algorithm with value function approximation is
wt+1=wt+th
rt+1+
^q(st+1;at+1;wt) ^q(st;at;wt)i
rw^q(st;at;wt):
This is the same as the algorithm we introduced previously in this lecture
except that ^vis replaced by ^q.
Shiyu Zhao 46 / 69

## 第151页

Sarsa with function approximation
So far, we merely considered state value estimation. That is
^v(s)v(s); s2S
To search for optimal policies, we need to estimate action values.
The Sarsa algorithm with value function approximation is
wt+1=wt+th
rt+1+
^q(st+1;at+1;wt) ^q(st;at;wt)i
rw^q(st;at;wt):
This is the same as the algorithm we introduced previously in this lecture
except that ^vis replaced by ^q.
Shiyu Zhao 46 / 69

## 第152页

Sarsa with function approximation
So far, we merely considered state value estimation. That is
^v(s)v(s); s2S
To search for optimal policies, we need to estimate action values.
The Sarsa algorithm with value function approximation is
wt+1=wt+th
rt+1+
^q(st+1;at+1;wt) ^q(st;at;wt)i
rw^q(st;at;wt):
This is the same as the algorithm we introduced previously in this lecture
except that ^vis replaced by ^q.
Shiyu Zhao 46 / 69

## 第153页

Sarsa with function approximation
To search for optimal policies, we can combine policy evaluation and policy
improvement.
Pseudocode: Sarsa with function approximation
Initialization: Initial parameter w0. Initial policy 0.t=>0for allt.2(0;1).
Goal: Learn an optimal policy to lead the agent to the target state from an initial state s0.
For each episode, do
Generatea0ats0following0(s0)
Ifst(t= 0;1;2;::: ) is not the target state, do
Collect the experience sample (rt+1;st+1;at+1)given (st;at): generate
rt+1;st+1by interacting with the environment; generate at+1followingt(st+1).
Update q-value (update parameter):
wt+1=wt+th
rt+1+
^q(st+1;at+1;wt) ^q(st;at;wt)i
rw^q(st;at;wt)
Update policy:
t+1(ajst) = 1 "
jA(st)j(jA(st)j 1)ifa= arg max a2A(st)^q(st;a;wt+1)
t+1(ajst) =
jA(st)jotherwise
st st+1,at at+1
Shiyu Zhao 47 / 69

## 第154页

Sarsa with function approximation
To search for optimal policies, we can combine policy evaluation and policy
improvement.
Pseudocode: Sarsa with function approximation
Initialization: Initial parameter w0. Initial policy 0.t=>0for allt.2(0;1).
Goal: Learn an optimal policy to lead the agent to the target state from an initial state s0.
For each episode, do
Generatea0ats0following0(s0)
Ifst(t= 0;1;2;::: ) is not the target state, do
Collect the experience sample (rt+1;st+1;at+1)given (st;at): generate
rt+1;st+1by interacting with the environment; generate at+1followingt(st+1).
Update q-value (update parameter):
wt+1=wt+th
rt+1+
^q(st+1;at+1;wt) ^q(st;at;wt)i
rw^q(st;at;wt)
Update policy:
t+1(ajst) = 1 "
jA(st)j(jA(st)j 1)ifa= arg max a2A(st)^q(st;a;wt+1)
t+1(ajst) =
jA(st)jotherwise
st st+1,at at+1
Shiyu Zhao 47 / 69

## 第155页

Sarsa with function approximation
Illustrative example:
Sarsa with linear function approximation: ^q(s;a;w ) =T(s;a)w

= 0:9,= 0:1,rboundary =rforbidden = 10,rtarget = 1,= 0:001.
0100 200 300 400 500-1000-5000Total reward
0100 200 300 400 500
Episode index0500Episode length
1 2 3 4 5
1
2
3
4
5
For details, please see the book.
Shiyu Zhao 48 / 69

## 第156页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 49 / 69

## 第157页

Q-learning with function approximation
Similar to Sarsa, tabular Q-learning can also be extended to the case of value
function approximation.
The q-value update rule is
wt+1=wt+th
rt+1+
max
a2A(st+1)^q(st+1;a;wt) ^q(st;at;wt)i
rw^q(st;at;wt);
which is the same as Sarsa except that ^q(st+1;at+1;wt)is replaced by
maxa2A(st+1)^q(st+1;a;wt).
Shiyu Zhao 50 / 69

## 第158页

Q-learning with function approximation
Similar to Sarsa, tabular Q-learning can also be extended to the case of value
function approximation.
The q-value update rule is
wt+1=wt+th
rt+1+
max
a2A(st+1)^q(st+1;a;wt) ^q(st;at;wt)i
rw^q(st;at;wt);
which is the same as Sarsa except that ^q(st+1;at+1;wt)is replaced by
maxa2A(st+1)^q(st+1;a;wt).
Shiyu Zhao 50 / 69

## 第159页

Q-learning with function approximation
Pseudocode: Q-learning with function approximation (on-policy version)
Initialization: Initial parameter w0. Initial policy 0.t=>0for allt.2(0;1).
Goal: Learn an optimal path to lead the agent to the target state from an initial state s0.
For each episode, do
Ifst(t= 0;1;2;::: ) is not the target state, do
Collect the experience sample (at;rt+1;st+1)givenst: generateatfollowing
t(st); generatert+1;st+1by interacting with the environment.
Update value (update parameter):
wt+1 =wt+th
rt+1 +
maxa2A(st+1)^q(st+1;a;wt) 
^q(st;at;wt)i
rw^q(st;at;wt)
Update policy:
t+1(ajst) = 1 "
jA(st)j(jA(st)j 1)ifa= arg max a2A(st)^q(st;a;wt+1)
t+1(ajst) ="
jA(st)jotherwise
Shiyu Zhao 51 / 69

## 第160页

Q-learning with function approximation
Illustrative example:
Q-learning with linear function approximation: ^q(s;a;w ) =T(s;a)w

= 0:9,= 0:1,rboundary =rforbidden = 10,rtarget = 1,= 0:001.
0100 200 300 400 500-4000-20000Total reward
0100 200 300 400 500
Episode index01000Episode length
1 2 3 4 5
1
2
3
4
5
Shiyu Zhao 52 / 69

## 第161页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 53 / 69

## 第162页

Deep Q-learning
Deep Q-learning or deep Q-network (DQN):
One of the earliest and most successful algorithms that introduce deep neural
networks into RL.
The role of neural networks is to be a nonlinear function approximator.
Dierent from the following algorithm:
wt+1=wt+th
rt+1+
max
a2A(st+1)^q(st+1;a;wt) ^q(st;at;wt)i
rw^q(st;at;wt)
because of the way of training a network.
Shiyu Zhao 54 / 69

## 第163页

Deep Q-learning
Deep Q-learning or deep Q-network (DQN):
One of the earliest and most successful algorithms that introduce deep neural
networks into RL.
The role of neural networks is to be a nonlinear function approximator.
Dierent from the following algorithm:
wt+1=wt+th
rt+1+
max
a2A(st+1)^q(st+1;a;wt) ^q(st;at;wt)i
rw^q(st;at;wt)
because of the way of training a network.
Shiyu Zhao 54 / 69

## 第164页

Deep Q-learning
Deep Q-learning or deep Q-network (DQN):
One of the earliest and most successful algorithms that introduce deep neural
networks into RL.
The role of neural networks is to be a nonlinear function approximator.
Dierent from the following algorithm:
wt+1=wt+th
rt+1+
max
a2A(st+1)^q(st+1;a;wt) ^q(st;at;wt)i
rw^q(st;at;wt)
because of the way of training a network.
Shiyu Zhao 54 / 69

## 第165页

Deep Q-learning
Deep Q-learning or deep Q-network (DQN):
One of the earliest and most successful algorithms that introduce deep neural
networks into RL.
The role of neural networks is to be a nonlinear function approximator.
Dierent from the following algorithm:
wt+1=wt+th
rt+1+
max
a2A(st+1)^q(st+1;a;wt) ^q(st;at;wt)i
rw^q(st;at;wt)
because of the way of training a network.
Shiyu Zhao 54 / 69

## 第166页

Deep Q-learning
Deep Q-learning aims to minimize the objective function/loss function:
wt+1=wt+th
rt+1+
max
a2A(st+1)^q(st+1;a;wt) ^q(st;at;wt)i
rw^q(st;at;wt)
+
J(w) =E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
where (S;A;R;S0)are random variables.
Shiyu Zhao 55 / 69

## 第167页

Deep Q-learning
How to minimize the objective function? Gradient-descent!
How to calculate the gradient of the objective function? Tricky!
That is because, in this objective function
J(w) =E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
;
the parameter wnot only appears in ^q(S;A;w )but also in
y:=R+
max
a2A(S0)^q(S0;a;w )
Since the optimal adepends on w,
rwy6=
max
a2A(S0)rw^q(S0;a;w )
To solve this problem, we can assume that winyis xed (at least for a
while) when we calculate the gradient.
Shiyu Zhao 56 / 69

## 第168页

Deep Q-learning
How to minimize the objective function? Gradient-descent!
How to calculate the gradient of the objective function? Tricky!
That is because, in this objective function
J(w) =E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
;
the parameter wnot only appears in ^q(S;A;w )but also in
y:=R+
max
a2A(S0)^q(S0;a;w )
Since the optimal adepends on w,
rwy6=
max
a2A(S0)rw^q(S0;a;w )
To solve this problem, we can assume that winyis xed (at least for a
while) when we calculate the gradient.
Shiyu Zhao 56 / 69

## 第169页

Deep Q-learning
How to minimize the objective function? Gradient-descent!
How to calculate the gradient of the objective function? Tricky!
That is because, in this objective function
J(w) =E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
;
the parameter wnot only appears in ^q(S;A;w )but also in
y:=R+
max
a2A(S0)^q(S0;a;w )
Since the optimal adepends on w,
rwy6=
max
a2A(S0)rw^q(S0;a;w )
To solve this problem, we can assume that winyis xed (at least for a
while) when we calculate the gradient.
Shiyu Zhao 56 / 69

## 第170页

Deep Q-learning
How to minimize the objective function? Gradient-descent!
How to calculate the gradient of the objective function? Tricky!
That is because, in this objective function
J(w) =E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
;
the parameter wnot only appears in ^q(S;A;w )but also in
y:=R+
max
a2A(S0)^q(S0;a;w )
Since the optimal adepends on w,
rwy6=
max
a2A(S0)rw^q(S0;a;w )
To solve this problem, we can assume that winyis xed (at least for a
while) when we calculate the gradient.
Shiyu Zhao 56 / 69

## 第171页

Deep Q-learning
How to minimize the objective function? Gradient-descent!
How to calculate the gradient of the objective function? Tricky!
That is because, in this objective function
J(w) =E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
;
the parameter wnot only appears in ^q(S;A;w )but also in
y:=R+
max
a2A(S0)^q(S0;a;w )
Since the optimal adepends on w,
rwy6=
max
a2A(S0)rw^q(S0;a;w )
To solve this problem, we can assume that winyis xed (at least for a
while) when we calculate the gradient.
Shiyu Zhao 56 / 69

## 第172页

Deep Q-learning
To do that, we can introduce two networks.
One is a main network representing ^q(s;a;w )
The other is a target network ^q(s;a;wT).
The objective function in this case degenerates to
J=E"
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )2#
;
wherewTis the target network parameter.
WhenwTis xed, the gradient of Jcan be easily obtained as
rwJ=E
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )
rw^q(S;A;w )
:
The basic idea of deep Q-learning is to use the gradient-descent algorithm to
minimize the objective function.
However, such an optimization process evolves some important techniques
that deserve special attention.
Shiyu Zhao 57 / 69

## 第173页

Deep Q-learning
To do that, we can introduce two networks.
One is a main network representing ^q(s;a;w )
The other is a target network ^q(s;a;wT).
The objective function in this case degenerates to
J=E"
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )2#
;
wherewTis the target network parameter.
WhenwTis xed, the gradient of Jcan be easily obtained as
rwJ=E
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )
rw^q(S;A;w )
:
The basic idea of deep Q-learning is to use the gradient-descent algorithm to
minimize the objective function.
However, such an optimization process evolves some important techniques
that deserve special attention.
Shiyu Zhao 57 / 69

## 第174页

Deep Q-learning
To do that, we can introduce two networks.
One is a main network representing ^q(s;a;w )
The other is a target network ^q(s;a;wT).
The objective function in this case degenerates to
J=E"
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )2#
;
wherewTis the target network parameter.
WhenwTis xed, the gradient of Jcan be easily obtained as
rwJ=E
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )
rw^q(S;A;w )
:
The basic idea of deep Q-learning is to use the gradient-descent algorithm to
minimize the objective function.
However, such an optimization process evolves some important techniques
that deserve special attention.
Shiyu Zhao 57 / 69

## 第175页

Deep Q-learning
To do that, we can introduce two networks.
One is a main network representing ^q(s;a;w )
The other is a target network ^q(s;a;wT).
The objective function in this case degenerates to
J=E"
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )2#
;
wherewTis the target network parameter.
WhenwTis xed, the gradient of Jcan be easily obtained as
rwJ=E
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )
rw^q(S;A;w )
:
The basic idea of deep Q-learning is to use the gradient-descent algorithm to
minimize the objective function.
However, such an optimization process evolves some important techniques
that deserve special attention.
Shiyu Zhao 57 / 69

## 第176页

Deep Q-learning
To do that, we can introduce two networks.
One is a main network representing ^q(s;a;w )
The other is a target network ^q(s;a;wT).
The objective function in this case degenerates to
J=E"
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )2#
;
wherewTis the target network parameter.
WhenwTis xed, the gradient of Jcan be easily obtained as
rwJ=E
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )
rw^q(S;A;w )
:
The basic idea of deep Q-learning is to use the gradient-descent algorithm to
minimize the objective function.
However, such an optimization process evolves some important techniques
that deserve special attention.
Shiyu Zhao 57 / 69

## 第177页

Deep Q-learning
To do that, we can introduce two networks.
One is a main network representing ^q(s;a;w )
The other is a target network ^q(s;a;wT).
The objective function in this case degenerates to
J=E"
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )2#
;
wherewTis the target network parameter.
WhenwTis xed, the gradient of Jcan be easily obtained as
rwJ=E
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )
rw^q(S;A;w )
:
The basic idea of deep Q-learning is to use the gradient-descent algorithm to
minimize the objective function.
However, such an optimization process evolves some important techniques
that deserve special attention.
Shiyu Zhao 57 / 69

## 第178页

Deep Q-learning - Two networks
Technique 1: Two networks, a main network and a target network.
Why is it used?
The mathematical reason has been explained when we calculate the gradient.
Implementation details:
LetwandwTdenote the parameters of the main and target networks,
respectively. They are set to be the same initially.
In every iteration, we draw a mini-batch of samples f(s;a;r;s0)gfrom the
replay buer (will be explained later).
For every (s;a;r;s0), we can calculate the desired output as
yT:=r+
max
a2A(s0)^q(s0;a;wT)
Therefore, we obtain a mini-batch of data:
f(s;a;yT)g
Usef(s;a;yT)gto train the network so as to minimize (yT ^q(s;a;w ))2.
Shiyu Zhao 58 / 69

## 第179页

Deep Q-learning - Two networks
Technique 1: Two networks, a main network and a target network.
Why is it used?
The mathematical reason has been explained when we calculate the gradient.
Implementation details:
LetwandwTdenote the parameters of the main and target networks,
respectively. They are set to be the same initially.
In every iteration, we draw a mini-batch of samples f(s;a;r;s0)gfrom the
replay buer (will be explained later).
For every (s;a;r;s0), we can calculate the desired output as
yT:=r+
max
a2A(s0)^q(s0;a;wT)
Therefore, we obtain a mini-batch of data:
f(s;a;yT)g
Usef(s;a;yT)gto train the network so as to minimize (yT ^q(s;a;w ))2.
Shiyu Zhao 58 / 69

## 第180页

Deep Q-learning - Two networks
Technique 1: Two networks, a main network and a target network.
Why is it used?
The mathematical reason has been explained when we calculate the gradient.
Implementation details:
LetwandwTdenote the parameters of the main and target networks,
respectively. They are set to be the same initially.
In every iteration, we draw a mini-batch of samples f(s;a;r;s0)gfrom the
replay buer (will be explained later).
For every (s;a;r;s0), we can calculate the desired output as
yT:=r+
max
a2A(s0)^q(s0;a;wT)
Therefore, we obtain a mini-batch of data:
f(s;a;yT)g
Usef(s;a;yT)gto train the network so as to minimize (yT ^q(s;a;w ))2.
Shiyu Zhao 58 / 69

## 第181页

Deep Q-learning - Two networks
Technique 1: Two networks, a main network and a target network.
Why is it used?
The mathematical reason has been explained when we calculate the gradient.
Implementation details:
LetwandwTdenote the parameters of the main and target networks,
respectively. They are set to be the same initially.
In every iteration, we draw a mini-batch of samples f(s;a;r;s0)gfrom the
replay buer (will be explained later).
For every (s;a;r;s0), we can calculate the desired output as
yT:=r+
max
a2A(s0)^q(s0;a;wT)
Therefore, we obtain a mini-batch of data:
f(s;a;yT)g
Usef(s;a;yT)gto train the network so as to minimize (yT ^q(s;a;w ))2.
Shiyu Zhao 58 / 69

## 第182页

Deep Q-learning - Two networks
Technique 1: Two networks, a main network and a target network.
Why is it used?
The mathematical reason has been explained when we calculate the gradient.
Implementation details:
LetwandwTdenote the parameters of the main and target networks,
respectively. They are set to be the same initially.
In every iteration, we draw a mini-batch of samples f(s;a;r;s0)gfrom the
replay buer (will be explained later).
For every (s;a;r;s0), we can calculate the desired output as
yT:=r+
max
a2A(s0)^q(s0;a;wT)
Therefore, we obtain a mini-batch of data:
f(s;a;yT)g
Usef(s;a;yT)gto train the network so as to minimize (yT ^q(s;a;w ))2.
Shiyu Zhao 58 / 69

## 第183页

Deep Q-learning - Two networks
Technique 1: Two networks, a main network and a target network.
Why is it used?
The mathematical reason has been explained when we calculate the gradient.
Implementation details:
LetwandwTdenote the parameters of the main and target networks,
respectively. They are set to be the same initially.
In every iteration, we draw a mini-batch of samples f(s;a;r;s0)gfrom the
replay buer (will be explained later).
For every (s;a;r;s0), we can calculate the desired output as
yT:=r+
max
a2A(s0)^q(s0;a;wT)
Therefore, we obtain a mini-batch of data:
f(s;a;yT)g
Usef(s;a;yT)gto train the network so as to minimize (yT ^q(s;a;w ))2.
Shiyu Zhao 58 / 69

## 第184页

Deep Q-learning - Experience replay
Technique 2: Experience replay
Question: What is experience replay?
Answer:
After we have collected some experience samples, we do NOT use these
samples in the order they were collected.
Instead, we store them in a set, called replay buer B:=f(s;a;r;s0)g
Every time we train the neural network, we can draw a mini-batch of random
samples from the replay buer.
The draw of samples, or called experience replay, should follow a uniform
distribution.
Shiyu Zhao 59 / 69

## 第185页

Deep Q-learning - Experience replay
Technique 2: Experience replay
Question: What is experience replay?
Answer:
After we have collected some experience samples, we do NOT use these
samples in the order they were collected.
Instead, we store them in a set, called replay buer B:=f(s;a;r;s0)g
Every time we train the neural network, we can draw a mini-batch of random
samples from the replay buer.
The draw of samples, or called experience replay, should follow a uniform
distribution.
Shiyu Zhao 59 / 69

## 第186页

Deep Q-learning - Experience replay
Technique 2: Experience replay
Question: What is experience replay?
Answer:
After we have collected some experience samples, we do NOT use these
samples in the order they were collected.
Instead, we store them in a set, called replay buer B:=f(s;a;r;s0)g
Every time we train the neural network, we can draw a mini-batch of random
samples from the replay buer.
The draw of samples, or called experience replay, should follow a uniform
distribution.
Shiyu Zhao 59 / 69

## 第187页

Deep Q-learning - Experience replay
Technique 2: Experience replay
Question: What is experience replay?
Answer:
After we have collected some experience samples, we do NOT use these
samples in the order they were collected.
Instead, we store them in a set, called replay buer B:=f(s;a;r;s0)g
Every time we train the neural network, we can draw a mini-batch of random
samples from the replay buer.
The draw of samples, or called experience replay, should follow a uniform
distribution.
Shiyu Zhao 59 / 69

## 第188页

Deep Q-learning - Experience replay
Technique 2: Experience replay
Question: What is experience replay?
Answer:
After we have collected some experience samples, we do NOT use these
samples in the order they were collected.
Instead, we store them in a set, called replay buer B:=f(s;a;r;s0)g
Every time we train the neural network, we can draw a mini-batch of random
samples from the replay buer.
The draw of samples, or called experience replay, should follow a uniform
distribution.
Shiyu Zhao 59 / 69

## 第189页

Deep Q-learning - Experience replay
Technique 2: Experience replay
Question: What is experience replay?
Answer:
After we have collected some experience samples, we do NOT use these
samples in the order they were collected.
Instead, we store them in a set, called replay buer B:=f(s;a;r;s0)g
Every time we train the neural network, we can draw a mini-batch of random
samples from the replay buer.
The draw of samples, or called experience replay, should follow a uniform
distribution.
Shiyu Zhao 59 / 69

## 第190页

Deep Q-learning - Experience replay
Question: Why is experience replay necessary in deep Q-learning? Why does
the replay must follow a uniform distribution?
Answer: The answers lie in the objective function.
J=E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
Rp(RjS;A);S0p(S0jS;A):RandSare determined by the system
model.
(S;A)d:(S;A)is an index and treated as a single random variable
The distribution of the state-action pair (S;A)is assumed to be uniform.
- Why uniform distribution? Because no prior knowledge.
- Can we use stationary distribution like before? No, since no policy is given.
Shiyu Zhao 60 / 69

## 第191页

Deep Q-learning - Experience replay
Question: Why is experience replay necessary in deep Q-learning? Why does
the replay must follow a uniform distribution?
Answer: The answers lie in the objective function.
J=E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
Rp(RjS;A);S0p(S0jS;A):RandSare determined by the system
model.
(S;A)d:(S;A)is an index and treated as a single random variable
The distribution of the state-action pair (S;A)is assumed to be uniform.
- Why uniform distribution? Because no prior knowledge.
- Can we use stationary distribution like before? No, since no policy is given.
Shiyu Zhao 60 / 69

## 第192页

Deep Q-learning - Experience replay
Question: Why is experience replay necessary in deep Q-learning? Why does
the replay must follow a uniform distribution?
Answer: The answers lie in the objective function.
J=E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
Rp(RjS;A);S0p(S0jS;A):RandSare determined by the system
model.
(S;A)d:(S;A)is an index and treated as a single random variable
The distribution of the state-action pair (S;A)is assumed to be uniform.
- Why uniform distribution? Because no prior knowledge.
- Can we use stationary distribution like before? No, since no policy is given.
Shiyu Zhao 60 / 69

## 第193页

Deep Q-learning - Experience replay
Question: Why is experience replay necessary in deep Q-learning? Why does
the replay must follow a uniform distribution?
Answer: The answers lie in the objective function.
J=E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
Rp(RjS;A);S0p(S0jS;A):RandSare determined by the system
model.
(S;A)d:(S;A)is an index and treated as a single random variable
The distribution of the state-action pair (S;A)is assumed to be uniform.
- Why uniform distribution? Because no prior knowledge.
- Can we use stationary distribution like before? No, since no policy is given.
Shiyu Zhao 60 / 69

## 第194页

Deep Q-learning - Experience replay
Question: Why is experience replay necessary in deep Q-learning? Why does
the replay must follow a uniform distribution?
Answer: The answers lie in the objective function.
J=E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
Rp(RjS;A);S0p(S0jS;A):RandSare determined by the system
model.
(S;A)d:(S;A)is an index and treated as a single random variable
The distribution of the state-action pair (S;A)is assumed to be uniform.
- Why uniform distribution? Because no prior knowledge.
- Can we use stationary distribution like before? No, since no policy is given.
Shiyu Zhao 60 / 69

## 第195页

Deep Q-learning - Experience replay
Question: Why is experience replay necessary in deep Q-learning? Why does
the replay must follow a uniform distribution?
Answer: The answers lie in the objective function.
J=E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
Rp(RjS;A);S0p(S0jS;A):RandSare determined by the system
model.
(S;A)d:(S;A)is an index and treated as a single random variable
The distribution of the state-action pair (S;A)is assumed to be uniform.
- Why uniform distribution? Because no prior knowledge.
- Can we use stationary distribution like before? No, since no policy is given.
Shiyu Zhao 60 / 69

## 第196页

Deep Q-learning - Experience replay
Answer (continued):
However, the samples are not uniformly collected because they are generated
consequently by certain policies.
To break the correlation between consequent samples, we can use the
experience replay technique by uniformly drawing samples from the replay
buer.
This is the mathematical reason why experience replay is necessary and why
the experience replay must be uniform.
Shiyu Zhao 61 / 69

## 第197页

Deep Q-learning - Experience replay
Answer (continued):
However, the samples are not uniformly collected because they are generated
consequently by certain policies.
To break the correlation between consequent samples, we can use the
experience replay technique by uniformly drawing samples from the replay
buer.
This is the mathematical reason why experience replay is necessary and why
the experience replay must be uniform.
Shiyu Zhao 61 / 69

## 第198页

Deep Q-learning - Experience replay
Answer (continued):
However, the samples are not uniformly collected because they are generated
consequently by certain policies.
To break the correlation between consequent samples, we can use the
experience replay technique by uniformly drawing samples from the replay
buer.
This is the mathematical reason why experience replay is necessary and why
the experience replay must be uniform.
Shiyu Zhao 61 / 69

## 第199页

Deep Q-learning - Experience replay
Revisit the tabular case:
Question: Why does not tabular Q-learning require experience replay?
- Answer: Because it does not require any distribution of SorA.
Question: Why does Deep Q-learning involve distributions?
- Answer: Because we need to dene a scalar objective function
J(w) =E[], where Eis for all (S;A).
- The tabular case aims to solve a set of equations for all (s;a)(Bellman
optimality equation), whereas the deep case aims to optimize a scalar
objective function.
Question: Can we use experience replay in tabular Q-learning?
- Answer: Yes, we can. And more sample ecient (why?)
Shiyu Zhao 62 / 69

## 第200页

Deep Q-learning - Experience replay
Revisit the tabular case:
Question: Why does not tabular Q-learning require experience replay?
- Answer: Because it does not require any distribution of SorA.
Question: Why does Deep Q-learning involve distributions?
- Answer: Because we need to dene a scalar objective function
J(w) =E[], where Eis for all (S;A).
- The tabular case aims to solve a set of equations for all (s;a)(Bellman
optimality equation), whereas the deep case aims to optimize a scalar
objective function.
Question: Can we use experience replay in tabular Q-learning?
- Answer: Yes, we can. And more sample ecient (why?)
Shiyu Zhao 62 / 69

## 第201页

Deep Q-learning - Experience replay
Revisit the tabular case:
Question: Why does not tabular Q-learning require experience replay?
- Answer: Because it does not require any distribution of SorA.
Question: Why does Deep Q-learning involve distributions?
- Answer: Because we need to dene a scalar objective function
J(w) =E[], where Eis for all (S;A).
- The tabular case aims to solve a set of equations for all (s;a)(Bellman
optimality equation), whereas the deep case aims to optimize a scalar
objective function.
Question: Can we use experience replay in tabular Q-learning?
- Answer: Yes, we can. And more sample ecient (why?)
Shiyu Zhao 62 / 69

## 第202页

Deep Q-learning - Experience replay
Revisit the tabular case:
Question: Why does not tabular Q-learning require experience replay?
- Answer: Because it does not require any distribution of SorA.
Question: Why does Deep Q-learning involve distributions?
- Answer: Because we need to dene a scalar objective function
J(w) =E[], where Eis for all (S;A).
- The tabular case aims to solve a set of equations for all (s;a)(Bellman
optimality equation), whereas the deep case aims to optimize a scalar
objective function.
Question: Can we use experience replay in tabular Q-learning?
- Answer: Yes, we can. And more sample ecient (why?)
Shiyu Zhao 62 / 69

## 第203页

Deep Q-learning - Experience replay
Revisit the tabular case:
Question: Why does not tabular Q-learning require experience replay?
- Answer: Because it does not require any distribution of SorA.
Question: Why does Deep Q-learning involve distributions?
- Answer: Because we need to dene a scalar objective function
J(w) =E[], where Eis for all (S;A).
- The tabular case aims to solve a set of equations for all (s;a)(Bellman
optimality equation), whereas the deep case aims to optimize a scalar
objective function.
Question: Can we use experience replay in tabular Q-learning?
- Answer: Yes, we can. And more sample ecient (why?)
Shiyu Zhao 62 / 69

## 第204页

Deep Q-learning - Experience replay
Revisit the tabular case:
Question: Why does not tabular Q-learning require experience replay?
- Answer: Because it does not require any distribution of SorA.
Question: Why does Deep Q-learning involve distributions?
- Answer: Because we need to dene a scalar objective function
J(w) =E[], where Eis for all (S;A).
- The tabular case aims to solve a set of equations for all (s;a)(Bellman
optimality equation), whereas the deep case aims to optimize a scalar
objective function.
Question: Can we use experience replay in tabular Q-learning?
- Answer: Yes, we can. And more sample ecient (why?)
Shiyu Zhao 62 / 69

## 第205页

Deep Q-learning - Experience replay
Revisit the tabular case:
Question: Why does not tabular Q-learning require experience replay?
- Answer: Because it does not require any distribution of SorA.
Question: Why does Deep Q-learning involve distributions?
- Answer: Because we need to dene a scalar objective function
J(w) =E[], where Eis for all (S;A).
- The tabular case aims to solve a set of equations for all (s;a)(Bellman
optimality equation), whereas the deep case aims to optimize a scalar
objective function.
Question: Can we use experience replay in tabular Q-learning?
- Answer: Yes, we can. And more sample ecient (why?)
Shiyu Zhao 62 / 69

## 第206页

Deep Q-learning
Pseudocode: Deep Q-learning (o-policy version)
Initialization: A main network and a target network with the same initial parameter.
Goal: Learn an optimal target network to approximate the optimal action values from the
experience samples generated by a given behavior policy b.
Store the experience samples generated by bin a replay buerB=f(s;a;r;s0)g
For each iteration, do
Uniformly draw a mini-batch of samples from B
For each sample (s;a;r;s0), calculate the target value as yT=r+

maxa2A(s0)^q(s0;a;wT), wherewTis the parameter of the target network
Update the main network to minimize (yT ^q(s;a;w ))2using the mini-batch of
samples
SetwT=weveryCiterations
Remarks:
Why no policy update?
The network input and output are dierent from the DQN paper.
Shiyu Zhao 63 / 69

## 第207页

Deep Q-learning
Pseudocode: Deep Q-learning (o-policy version)
Initialization: A main network and a target network with the same initial parameter.
Goal: Learn an optimal target network to approximate the optimal action values from the
experience samples generated by a given behavior policy b.
Store the experience samples generated by bin a replay buerB=f(s;a;r;s0)g
For each iteration, do
Uniformly draw a mini-batch of samples from B
For each sample (s;a;r;s0), calculate the target value as yT=r+

maxa2A(s0)^q(s0;a;wT), wherewTis the parameter of the target network
Update the main network to minimize (yT ^q(s;a;w ))2using the mini-batch of
samples
SetwT=weveryCiterations
Remarks:
Why no policy update?
The network input and output are dierent from the DQN paper.
Shiyu Zhao 63 / 69

## 第208页

Deep Q-learning
Pseudocode: Deep Q-learning (o-policy version)
Initialization: A main network and a target network with the same initial parameter.
Goal: Learn an optimal target network to approximate the optimal action values from the
experience samples generated by a given behavior policy b.
Store the experience samples generated by bin a replay buerB=f(s;a;r;s0)g
For each iteration, do
Uniformly draw a mini-batch of samples from B
For each sample (s;a;r;s0), calculate the target value as yT=r+

maxa2A(s0)^q(s0;a;wT), wherewTis the parameter of the target network
Update the main network to minimize (yT ^q(s;a;w ))2using the mini-batch of
samples
SetwT=weveryCiterations
Remarks:
Why no policy update?
The network input and output are dierent from the DQN paper.
Shiyu Zhao 63 / 69

## 第209页

Deep Q-learning
Illustrative example:
We need to learn optimal action values for every state-action pair.
Once the optimal action values are obtained, the optimal greedy policy can
be obtained immediately.
Shiyu Zhao 64 / 69

## 第210页

Deep Q-learning
Setup:
One single episode is used to train the network.
This episode is generated by an exploratory behavior policy shown in Fig. (a).
The episode only has 1,000 steps! The tabular Q-learning requires 100,000
steps.
A shallow neural network with one single hidden layer is used as a nonlinear
approximator of ^q(s;a;w ). The hidden layer has 100 neurons.
See details in the book.
Shiyu Zhao 65 / 69

## 第211页

Deep Q-learning
Setup:
One single episode is used to train the network.
This episode is generated by an exploratory behavior policy shown in Fig. (a).
The episode only has 1,000 steps! The tabular Q-learning requires 100,000
steps.
A shallow neural network with one single hidden layer is used as a nonlinear
approximator of ^q(s;a;w ). The hidden layer has 100 neurons.
See details in the book.
Shiyu Zhao 65 / 69

## 第212页

Deep Q-learning
Setup:
One single episode is used to train the network.
This episode is generated by an exploratory behavior policy shown in Fig. (a).
The episode only has 1,000 steps! The tabular Q-learning requires 100,000
steps.
A shallow neural network with one single hidden layer is used as a nonlinear
approximator of ^q(s;a;w ). The hidden layer has 100 neurons.
See details in the book.
Shiyu Zhao 65 / 69

## 第213页

Deep Q-learning
Setup:
One single episode is used to train the network.
This episode is generated by an exploratory behavior policy shown in Fig. (a).
The episode only has 1,000 steps! The tabular Q-learning requires 100,000
steps.
A shallow neural network with one single hidden layer is used as a nonlinear
approximator of ^q(s;a;w ). The hidden layer has 100 neurons.
See details in the book.
Shiyu Zhao 65 / 69

## 第214页

Deep Q-learning
Setup:
One single episode is used to train the network.
This episode is generated by an exploratory behavior policy shown in Fig. (a).
The episode only has 1,000 steps! The tabular Q-learning requires 100,000
steps.
A shallow neural network with one single hidden layer is used as a nonlinear
approximator of ^q(s;a;w ). The hidden layer has 100 neurons.
See details in the book.
Shiyu Zhao 65 / 69

## 第215页

Deep Q-learning
Setup:
One single episode is used to train the network.
This episode is generated by an exploratory behavior policy shown in Fig. (a).
The episode only has 1,000 steps! The tabular Q-learning requires 100,000
steps.
A shallow neural network with one single hidden layer is used as a nonlinear
approximator of ^q(s;a;w ). The hidden layer has 100 neurons.
See details in the book.
Shiyu Zhao 65 / 69

## 第216页

Deep Q-learning
1 2 3 4 5
1
2
3
4
5
The behavior policy.
 An episode of 1,000 steps.
1 2 3 4 5
1
2
3
4
5 The obtained policy.
02004006008001000
Iteration index012345TD error / loss function
The TD error converges to zero.
02004006008001000
Iteration index0246810State value error (RMSE) The state estimation error converges to zero.
Shiyu Zhao 66 / 69

## 第217页

Deep Q-learning
1 2 3 4 5
1
2
3
4
5
The behavior policy.
 An episode of 1,000 steps.
1 2 3 4 5
1
2
3
4
5 The obtained policy.
02004006008001000
Iteration index012345TD error / loss function
The TD error converges to zero.
02004006008001000
Iteration index0246810State value error (RMSE) The state estimation error converges to zero.
Shiyu Zhao 66 / 69

## 第218页

Deep Q-learning
1 2 3 4 5
1
2
3
4
5
The behavior policy.
 An episode of 1,000 steps.
1 2 3 4 5
1
2
3
4
5 The obtained policy.
02004006008001000
Iteration index012345TD error / loss function
The TD error converges to zero.
02004006008001000
Iteration index0246810State value error (RMSE) The state estimation error converges to zero.
Shiyu Zhao 66 / 69

## 第219页

Deep Q-learning
1 2 3 4 5
1
2
3
4
5
The behavior policy.
 An episode of 1,000 steps.
1 2 3 4 5
1
2
3
4
5 The obtained policy.
02004006008001000
Iteration index012345TD error / loss function
The TD error converges to zero.
02004006008001000
Iteration index0246810State value error (RMSE) The state estimation error converges to zero.
Shiyu Zhao 66 / 69

## 第220页

Deep Q-learning
1 2 3 4 5
1
2
3
4
5
The behavior policy.
 An episode of 1,000 steps.
1 2 3 4 5
1
2
3
4
5 The obtained policy.
02004006008001000
Iteration index012345TD error / loss function
The TD error converges to zero.
02004006008001000
Iteration index0246810State value error (RMSE) The state estimation error converges to zero.
Shiyu Zhao 66 / 69

## 第221页

Deep Q-learning
What if we only use a single episode of 100 steps ? Insucient data
1 2 3 4 5
1
2
3
4
5
The behavior policy.
1 2 3 4 5
1
2
3
4
5 An episode of 100 steps.
1 2 3 4 5
1
2
3
4
5 The nal policy.
02004006008001000
Iteration index01234567TD error / loss function
The TD error converges to zero.
02004006008001000
Iteration index45678State value error (RMSE) The state error does not converge to zero.
Shiyu Zhao 67 / 69

## 第222页

Deep Q-learning
What if we only use a single episode of 100 steps ? Insucient data
1 2 3 4 5
1
2
3
4
5
The behavior policy.
1 2 3 4 5
1
2
3
4
5 An episode of 100 steps.
1 2 3 4 5
1
2
3
4
5 The nal policy.
02004006008001000
Iteration index01234567TD error / loss function
The TD error converges to zero.
02004006008001000
Iteration index45678State value error (RMSE) The state error does not converge to zero.
Shiyu Zhao 67 / 69

## 第223页

Deep Q-learning
What if we only use a single episode of 100 steps ? Insucient data
1 2 3 4 5
1
2
3
4
5
The behavior policy.
1 2 3 4 5
1
2
3
4
5 An episode of 100 steps.
1 2 3 4 5
1
2
3
4
5 The nal policy.
02004006008001000
Iteration index01234567TD error / loss function
The TD error converges to zero.
02004006008001000
Iteration index45678State value error (RMSE) The state error does not converge to zero.
Shiyu Zhao 67 / 69

## 第224页

Deep Q-learning
What if we only use a single episode of 100 steps ? Insucient data
1 2 3 4 5
1
2
3
4
5
The behavior policy.
1 2 3 4 5
1
2
3
4
5 An episode of 100 steps.
1 2 3 4 5
1
2
3
4
5 The nal policy.
02004006008001000
Iteration index01234567TD error / loss function
The TD error converges to zero.
02004006008001000
Iteration index45678State value error (RMSE) The state error does not converge to zero.
Shiyu Zhao 67 / 69

## 第225页

Deep Q-learning
What if we only use a single episode of 100 steps ? Insucient data
1 2 3 4 5
1
2
3
4
5
The behavior policy.
1 2 3 4 5
1
2
3
4
5 An episode of 100 steps.
1 2 3 4 5
1
2
3
4
5 The nal policy.
02004006008001000
Iteration index01234567TD error / loss function
The TD error converges to zero.
02004006008001000
Iteration index45678State value error (RMSE) The state error does not converge to zero.
Shiyu Zhao 67 / 69

## 第226页

Outline
1Motivating examples: from table to function
2Algorithm for state value estimation
Objective function
Optimization algorithms
Selection of function approximators
Illustrative examples
Summary of the story
Theoretical analysis (optional)
3Sarsa with function approximation
4Q-learning with function approximation
5Deep Q-learning
6Summary
Shiyu Zhao 68 / 69

## 第227页

Summary
This lecture introduces the method of value function approximation.
First, understand the basic idea.
Second, understand the basic algorithms.
Shiyu Zhao 69 / 69

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_Book-Mathematical-Foundation-of-Reinforcement-Learning-main_课程MOC|Book-Mathematical-Foundation-of-Reinforcement-Learning-main MOC]]
