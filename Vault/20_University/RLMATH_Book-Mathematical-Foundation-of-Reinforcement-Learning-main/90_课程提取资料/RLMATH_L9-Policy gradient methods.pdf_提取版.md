---
id: extract-rlmath-f9656b6b
type: extract
status: extracted
course: RLMATH
source:
  - "[[91_Raw-Archive/PDF/RLMATH_L9-Policy gradient methods.pdf_课件_未知日期_f9656b6b.pdf]]"
source_pages: all
source_hash: "f9656b6bb6a617730495135c7f75cf526eb97dcaa35c0b116fc1af9e01d9dcab"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# L9-Policy gradient methods.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

Lecture 9: Policy Gradient Methods
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
Shiyu Zhao 1 / 42

## 第3页

Introduction
In this lecture, we will move
from value-based methods to policy-based methods
from value function methods to policy function methods (or called policy
gradient methods)
Shiyu Zhao 2 / 42

## 第4页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
Metric 1: Average value
Metric 2: Average reward
Summary of the two metrics
3Gradients of the metrics
4Gradient-ascent algorithm
5Summary
Shiyu Zhao 3 / 42

## 第5页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
Metric 1: Average value
Metric 2: Average reward
Summary of the two metrics
3Gradients of the metrics
4Gradient-ascent algorithm
5Summary
Shiyu Zhao 4 / 42

## 第6页

Basic idea of policy gradient
Previously, policies have been represented by tables:
The action probabilities of all states are stored in a table (ajs). Each entry
of the table is indexed by a state and an action.
a1a2a3a4a5
s1(a1js1)(a2js1)(a3js1)(a4js1)(a5js1)
..................
s9(a1js9)(a2js9)(a3js9)(a4js9)(a5js9)
Shiyu Zhao 5 / 42

## 第7页

Basic idea of policy gradient
Now, policies can be represented by parameterized functions:
(ajs;)
where2Rmis a parameter vector.
The function can be, for example, a neural network, whose input is s, output
is the probability to take each action, and parameter is .
Advantage: when the state space is large, the tabular representation will be
of low eciency in terms of storage and generalization.
The function representation is also sometimes written as (a;s; ),(ajs),
or(a;s).
Shiyu Zhao 6 / 42

## 第8页

Basic idea of policy gradient
Dierences between tabular and function representations:
First, how to dene optimal policies?
- In the tabular case, a policy is optimal if it can maximize every state
value .
- In the function case, a policy is optimal if it can maximize certain scalar
metrics .
Shiyu Zhao 7 / 42

## 第9页

Basic idea of policy gradient
Dierences between tabular and function representations:
Second, how to access the probability of an action?
- In the tabular case, the probability of taking aatscan be directly
accessed by looking up the tabular policy.
- In the function case, we need to calculate the value of (ajs;)given the
function structure and the parameter.
Shiyu Zhao 8 / 42

## 第10页

Basic idea of policy gradient
Dierences between tabular and function representations:
Third, how to update policies?
- In the tabular case, a policy can be updated by directly changing the
entries in the table.
- In the function case, a policy cannot be updated in this way anymore.
Instead, it can only be updated by changing the parameter .
Shiyu Zhao 9 / 42

## 第11页

Basic idea of policy gradient
The basic idea of the policy gradient is simple:
First, metrics (or objective functions) to dene optimal policies: J(), which
can dene optimal policies.
Second, gradient-based optimization algorithms to search for optimal policies:
t+1=t+rJ(t)
Although the idea is simple, the complication emerges when we try to answer
the following questions.
What appropriate metrics should be used?
How to calculate the gradients of the metrics?
These questions will be answered in detail in this lecture.
Shiyu Zhao 10 / 42

## 第12页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
Metric 1: Average value
Metric 2: Average reward
Summary of the two metrics
3Gradients of the metrics
4Gradient-ascent algorithm
5Summary
Shiyu Zhao 11 / 42

## 第13页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
Metric 1: Average value
Metric 2: Average reward
Summary of the two metrics
3Gradients of the metrics
4Gradient-ascent algorithm
5Summary
Shiyu Zhao 12 / 42

## 第14页

Metric 1: average value
The rst metric is the average state value or simply called average value:
v=X
s2Sd(s)v(s)
vis a weighted average of the state values.
d(s)0is the weight for state s.
SinceP
s2Sd(s) = 1 , we can interpret d(s)as a probability distribution. Then,
the metric can be written as
v=ESd[v(S)]
Shiyu Zhao 13 / 42

## 第15页

Metric 1: average value
How to select the distribution d? There are two cases.
Case 1:disindependent of the policy .
This case is relatively simple because the gradient of the metric is easier to
calculate:rv=dTrv
In this case, we specically denote dasd0andvasv0
.
How to select d0?
One trivial way is to treat all the states equally important and hence select
d0(s) = 1=jSj.
Another important case is that we are only interested in a specic state s0.
For example, the episodes in some tasks always start from the same state s0.
Then, we only care about the long-term return starting from s0. In this case,
d0(s0) = 1; d 0(s6=s0) = 0
In this case, v=v(s0)
Shiyu Zhao 14 / 42

## 第16页

Metric 1: average value
How to select the distribution d? There are two cases.
Case 2:ddepends on the policy .
A common way is to select dasd(s), which is the stationary distribution
under. Details of stationary distribution can be found in the last lecture
and the book.
The interpretation of selecting dis as follows.
-dre
ects the long-run behavior of the Markov decision process under a
given policy .
- If one state is frequently visited in the long run, it is more important and
deserves more weight.
- If a state is hardly visited, then we give it less weight.
Shiyu Zhao 15 / 42

## 第17页

Metric 1: average value
An important equivalent expression:
You will see the following metric often in the literature:
J() = lim
n!1E"nX
t=0
tRt+1#
=E"1X
t=0
tRt+1#
:
Question: What is its relationship to the metric we introduced just now?
Answer: They are the same. That is because
J() =E"1X
t=0
tRt+1#
=X
s2Sd(s)E"1X
t=0
tRt+1jS0=s#
=X
s2Sd(s)v(s)
= v
Shiyu Zhao 16 / 42

## 第18页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
Metric 1: Average value
Metric 2: Average reward
Summary of the two metrics
3Gradients of the metrics
4Gradient-ascent algorithm
5Summary
Shiyu Zhao 17 / 42

## 第19页

Metric 2: average reward
The second metric is average one-step reward or simply average reward:
r:=X
s2Sd(s)r(s) =E[r(S)];
whereSd,
r(s) =X
a2A(ajs)r(s;a)
r(s;a) =E[Rjs;a] =X
rrp(rjs;a)
Remarks:
ris simply a weighted average of immediate rewards.
r(s)is the average immediate reward that can be obtained from s.
dis the stationary distribution.
Shiyu Zhao 18 / 42

## 第20页

Metric 2: average reward
An important equivalent expression:
Suppose an agent follows a given policy and generate a trajectory with the
rewards as (R1;R2;:::).
The average single-step reward along this trajectory is
lim
n!11
nEh
R1+R2++RnjS0=s0i
= lim
n!11
nE"n 1X
t=0Rt+1jS0=s0#
wheres0is the starting state of the trajectory.
Shiyu Zhao 19 / 42

## 第21页

Metrics to dene optimal policies - Remarks
An important fact is that
lim
n!11
nE"n 1X
t=0Rt+1jS0=s0#
= lim
n!11
nE"n 1X
t=0Rt+1#
=X
sd(s)r(s)
= r
Remarks:
Highlight: the starting state s0does not matter.
The derivation of the equation is nontrivial and can be found in my book.
Shiyu Zhao 20 / 42

## 第22页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
Metric 1: Average value
Metric 2: Average reward
Summary of the two metrics
3Gradients of the metrics
4Gradient-ascent algorithm
5Summary
Shiyu Zhao 21 / 42

## 第23页

Summary of the two metrics
Metric Expression 1 Expression 2 Expression 3
vP
s2Sd(s)v(s)ESd[v(S)] limn!1EPn
t=0
tRt+1
rP
s2Sd(s)r(s)ESd[r(S)] limn!11
nEPn 1
t=0Rt+1
Table: Summary of the dierent but equivalent expressions of vandr.
Shiyu Zhao 22 / 42

## 第24页

Summary of the two metrics
Remark 1 about the metrics:
All these metrics are functions of .
Sinceis parameterized by , these metrics are functions of .
In other words, dierent values of can generate dierent metric values.
Therefore, we can search for the optimal values of to maximize these metrics.
This is the basic idea of policy gradient methods.
Shiyu Zhao 23 / 42

## 第25页

Summary of the two metrics
Remark 2 about the metrics:
One complication is that the metrics can be dened in either the discounted
case where
2(0;1)or the undiscounted case where 
= 1.
The undiscounted case is nontrivial.
We only consider the discounted case so far in this book. For details about
the undiscounted case, see the book.
Shiyu Zhao 24 / 42

## 第26页

Summary of the two metrics
Remark 3 about the metrics:
What is the relationship between randv?
The two metrics are equivalent (not equal) to each other. Specically, in the
discounted case where 
 <1, it holds that
r= (1 
)v:
Therefore, they can be maximized simultaneously. See the proof in the book.
Shiyu Zhao 25 / 42

## 第27页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
Metric 1: Average value
Metric 2: Average reward
Summary of the two metrics
3Gradients of the metrics
4Gradient-ascent algorithm
5Summary
Shiyu Zhao 26 / 42

## 第28页

Gradients of the metrics
Given a metric, we next
derive its gradient
and then, apply gradient-based methods to optimize the metric.
The gradient calculation is one of the most complicated parts of policy gradient
methods! That is because
rst, we need to distinguish dierent metrics v,r,v0

second, we need to distinguish discounted and undiscounted cases.
Shiyu Zhao 27 / 42

## 第29页

Gradients of the metrics
I simply give the expression of the gradient without proof:
rJ() =X
s2S(s)X
a2Ar(ajs;)q(s;a)
The above is a unied expression of many cases:
J()can be v,r, orv0
.
\=" may denote strict equality, approximation, or proportional to.
is a distribution or weight of the states.
The derivation of this expression is very complex .
Details are not given here. Interested readers can read my book.
For most readers, it is sucient to know this expression.
Shiyu Zhao 28 / 42

## 第30页

Gradients of the metrics
A compact and important expression of the gradient:
rJ() =X
s2S(s)X
a2Ar(ajs;)q(s;a)
=ES;A
rln(AjS;)q(S;A)
First, why is this expression useful?
Because we can use samples to approximate the gradient:
rJrln(ajs;)q(s;a)
wheres;aare samples. This is the idea of stochastic gradient descent.
Shiyu Zhao 29 / 42

## 第31页

Gradients of the metrics
A compact and important expression of the gradient:
rJ() =X
s2S(s)X
a2Ar(ajs;)q(s;a)
=ES;A
rln(AjS;)q(S;A)
Second, how to prove the above equation?
Proof: Consider the function lnwhere lnis the natural logarithm. It is easy
to see that
rln(ajs;) =r(ajs;)
(ajs;)
and hence
r(ajs;) =(ajs;)rln(ajs;):
Shiyu Zhao 30 / 42

## 第32页

Gradients of the metrics
A compact and important expression of the gradient:
rJ() =X
s2S(s)X
a2Ar(ajs;)q(s;a)
=ES;A
rln(AjS;)q(S;A)
Proof (continued): Then, we have
rJ=X
s(s)X
ar(ajs;)q(s;a)
=X
s(s)X
a(ajs;)rln(ajs;)q(s;a)
=ES"X
a(ajS;)rln(ajS;)q(S;a)#
=ES;A
rln(AjS;)q(S;A)
Shiyu Zhao 31 / 42

## 第33页

Gradients of the metrics
Remarks: It is required by ln(ajs;)that for any s;a;
(ajs;)>0
This can be achieved by using softmax functions that can normalize the
entries in a vector from ( 1;+1)to(0;1).
- For example, for any vector x= [x1;:::;xn]T,
zi=exi
Pn
j=1exj
wherezi2(0;1)andPn
i=1zi= 1.
Specically, the policy function has the form of
(ajs;) =eh(s;a; )
P
a02Aeh(s;a0;)
whereh(s;a; )is another function to be learned.
Shiyu Zhao 32 / 42

## 第34页

Gradients of the metrics
Remarks:
Such a form based on the softmax function can be realized by a neural
network whose input is sand parameter is . The network has jAjoutputs,
each of which corresponds to (ajs;)for an action a. The activation
function of the output layer should be softmax.
Since(ajs;)>0for alla, the parameterized policy is stochastic and hence
exploratory.
- There also exist deterministic policy gradient (DPG) methods. We will
study in the next lecture.
Shiyu Zhao 33 / 42

## 第35页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
Metric 1: Average value
Metric 2: Average reward
Summary of the two metrics
3Gradients of the metrics
4Gradient-ascent algorithm
5Summary
Shiyu Zhao 34 / 42

## 第36页

Gradient-ascent algorithm
Now, we present the rst policy gradient algorithm to nd optimal policies!
1) The gradient-ascent algorithm maximizing J()is
t+1=t+rJ(t)
=t+Eh
rln(AjS;t)q(S;A)i
2) Since the true gradient is unknown, we can replace it by a stochastic one:
t+1=t+rln(atjst;t)q(st;at)
3) Furthermore, since qis unknown, it can be replaced by an estimate:
t+1=t+rln(atjst;t)qt(st;at)
Shiyu Zhao 35 / 42

## 第37页

Gradient-ascent algorithm
Ifq(st;at)is estimated by Monte Carlo estimation, the algorithm has a
specics name, REINFORCE.
REINFORCE is one of earliest and simplest policy gradient algorithms.
Many other policy gradient algorithms such as the actor-critic methods can
be obtained by extending REINFORCE (next lecture).
Pseudocode: Policy Gradient by Monte Carlo (REINFORCE)
Initialization: Initial parameter ;
2(0;1);>0.
Goal: Learn an optimal policy to maximize J().
For each episode, do
Generate an episode fs0;a0;r1;:::;sT 1;aT 1;rTgfollowing().
Fort= 0;1;:::;T 1:
Value update: qt(st;at) =PT
k=t+1
k t 1rk
Policy update:  +rln(atjst;)qt(st;at)
Shiyu Zhao 36 / 42

## 第38页

Gradient-ascent algorithm
Remark 1: How to do sampling?
ES;Ah
rln(AjS;t)q(S;A)i
 !rln(ajs;t)q(s;a)
How to sample S?
-S, where the distribution is a long-run behavior under .
- In practice, people usually do not care about it.
How to sample A?
-A(AjS;). Hence,atshould be sampled following (t)atst.
- Therefore, policy gradient methods are on-policy.
Shiyu Zhao 37 / 42

## 第39页

Gradient-ascent algorithm
Remark 2: How to interpret this algorithm?
Since
rln(atjst;t) =r(atjst;t)
(atjst;t)
the algorithm can be rewritten as
t+1=t+rln(atjst;t)qt(st;at)
=t+qt(st;at)
(atjst;t)
|{z}
tr(atjst;t):
Therefore, we have the important expression of the algorithm:
t+1=t+tr(atjst;t)
Shiyu Zhao 38 / 42

## 第40页

Gradient-ascent algorithm
The interpretation of
t+1=t+tr(atjst;t)
is as follows. Suppose that is suciently small.
Interpretation:
Ift>0, the probability of choosing (st;at)is increased:
(atjst;t+1)>(atjst;t)
Ift<0, the probability of choosing (st;at)is lower:
(atjst;t+1)<(atjst;t)
Math: Whent+1 tis suciently small, the denition of dierential implies
(atjst;t+1)(atjst;t) + (r(atjst;t))T(t+1 t)
=(atjst;t) +t(r(atjst;t))T(r(atjst;t))
=(atjst;t) +tkr(atjst;t)k2
Shiyu Zhao 39 / 42

## 第41页

Gradient-ascent algorithm
t+1=t+qt(st;at)
(atjst;t)
|{z}
tr(atjst;t)
Interpretation (continued) :tcan balance exploration and exploitation.
The reason is as follows.
First,tis proportional to qt(st;at).
greaterqt(st;at) =)greatert=)greater(atjst;t+1)
Therefore, the algorithm intends to exploit actions with greater values.
Second,tis inversely proportional to (atjst;t)(whenqt(st;at)>0).
smaller(atjst;t) =)greatert=)greater(atjst;t+1)
Therefore, the algorithm intends to explore actions that have low
probabilities.
Shiyu Zhao 40 / 42

## 第42页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
Metric 1: Average value
Metric 2: Average reward
Summary of the two metrics
3Gradients of the metrics
4Gradient-ascent algorithm
5Summary
Shiyu Zhao 41 / 42

## 第43页

Summary
Contents of this lecture:
Metrics for optimality
Gradients of the metrics
Gradient-ascent algorithm
A special case: REINFORCE
Next lecture: Actor-critic
Shiyu Zhao 42 / 42

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_Book-Mathematical-Foundation-of-Reinforcement-Learning-main_课程MOC|Book-Mathematical-Foundation-of-Reinforcement-Learning-main MOC]]
