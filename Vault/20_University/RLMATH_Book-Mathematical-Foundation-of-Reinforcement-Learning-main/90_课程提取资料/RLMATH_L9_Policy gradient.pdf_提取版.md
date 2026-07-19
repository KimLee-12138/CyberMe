---
id: extract-rlmath-5e79cad6
type: extract
status: extracted
course: RLMATH
source:
  - "[[91_Raw-Archive/PDF/RLMATH_L9_Policy gradient.pdf_课件_未知日期_5e79cad6.pdf]]"
source_pages: all
source_hash: "5e79cad68fe297c0a81e1b33740f8915bfd062dfe2770417727f85e27eff5659"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# L9_Policy gradient.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

Lecture 9: Policy Gradient Methods
Shiyu Zhao

## 第2页

Introduction
Chapter 2:
Bellman 
EquationChapter 3:
Bellman Optimality  
EquationChapter 4:
Value Iteration & 
Policy IterationChapter 5: 
Monte Carlo 
Learning
Chapter 7:
Temporal ‐Difference  
Learning
Chapter 8:
Value Function 
Approximation
Chapter 9:
Policy Function 
Approximation
(or Policy Gradient)Chapter 10:
Actor‐Critic 
MethodsChapter 6:
Stochastic  
Approximation
tabular representation
to
function representation
Fundamental  toolsAlgorithm/Methods
Shiyu Zhao 1 / 43

## 第3页

Introduction
In this lecture, we will move
from value-based methods to policy-based methods
from value function approximation to policy function approximation
Shiyu Zhao 2 / 43

## 第4页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
3Gradients of the metrics
4Gradient-ascent algorithm (REINFORCE)
5Summary
Shiyu Zhao 3 / 43

## 第5页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
3Gradients of the metrics
4Gradient-ascent algorithm (REINFORCE)
5Summary
Shiyu Zhao 4 / 43

## 第6页

Basic idea of policy gradient
Previously, policies have been represented by tables:
The action probabilities of all states are stored in a table (ajs). Each
entry of the table is indexed by a state and an action.
a1a2a3a4a5
s1(a1js1)(a2js1)(a3js1)(a4js1)(a5js1)
..................
s9(a1js9)(a2js9)(a3js9)(a4js9)(a5js9)
We can directly access or change a value in the table.
Shiyu Zhao 5 / 43

## 第7页

Basic idea of policy gradient
Now, policies can be represented by parameterized functions:
(ajs;)
where2Rmis a parameter vector.
The function can be, for example, a neural network, whose input is s,
output is the probability to take each action, and parameter is .
Advantage: when the state space is large, the tabular representation
will be of low eciency in terms of storage and generalization.
The function representation is also sometimes written as (a;s; ),
(ajs), or(a;s).
Shiyu Zhao 6 / 43

## 第8页

Basic idea of policy gradient
Dierences between tabular and function representations:
First, how to dene optimal policies?
When represented as a table, a policy is optimal if it can maximize
every state value .
When represented by a function, a policy is optimal if it can
maximize certain scalar metrics .
Shiyu Zhao 7 / 43

## 第9页

Basic idea of policy gradient
Dierences between tabular and function representations:
Second, how to access the probability of an action?
In the tabular case, the probability of taking aatscan be directly
accessed by looking up the tabular policy.
In the case of function representation, we need to calculate the value
of(ajs;)given the function structure and the parameter.
Shiyu Zhao 8 / 43

## 第10页

Basic idea of policy gradient
Dierences between tabular and function representations:
Third, how to update policies?
When represented by a table, a policy can be updated by directly
changing the entries in the table.
When represented by a parameterized function, a policy cannot be
updated in this way anymore. Instead, it can only be updated by
changing the parameter .
Shiyu Zhao 9 / 43

## 第11页

Basic idea of policy gradient
The basic idea of the policy gradient is simple:
First, metrics (or objective functions) to dene optimal policies: J(),
which can dene optimal policies.
Second, gradient-based optimization algorithms to search for optimal
policies:
t+1=t+rJ(t)
Although the idea is simple, the complication emerges when we try to
answer the following questions.
What appropriate metrics should be used?
How to calculate the gradients of the metrics?
These questions will be answered in detail in this lecture.
Shiyu Zhao 10 / 43

## 第12页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
3Gradients of the metrics
4Gradient-ascent algorithm (REINFORCE)
5Summary
Shiyu Zhao 11 / 43

## 第13页

Metrics to dene optimal policies - 1) The average value
There are two metrics.
The rst metric is the average state value or simply called average
value. In particular, the metric is dened as
v=X
s2Sd(s)v(s)
vis a weighted average of the state values.
d(s)0is the weight for state s.
SinceP
s2Sd(s) = 1 , we can interpret d(s)as a probability
distribution. Then, the metric can be written as
v=E[v(S)]
whereSd.
Shiyu Zhao 12 / 43

## 第14页

Metrics to dene optimal policies - 1) The average value
Vector-product form:
v=X
s2Sd(s)v(s) =dTv
where
v= [:::;v(s);:::]T2RjSj
d= [:::;d (s);:::]T2RjSj:
This expression is particularly useful when we analyze its gradient.
Shiyu Zhao 13 / 43

## 第15页

Metrics to dene optimal policies - 1) The average value
How to select the distribution d? There are two cases.
The rst case is that disindependent of the policy .
This case is relatively simple because the gradient of the metric is
easier to calculate.
In this case, we specically denote dasd0andvasv0
.
How to select d0?
One trivial way is to treat all the states equally important and hence
selectd0(s) = 1=jSj.
Another important case is that we are only interested in a specic
states0. For example, the episodes in some tasks always start from
the same state s0. Then, we only care about the long-term return
starting from s0.In this case,
d0(s0) = 1; d 0(s6=s0) = 0:
Shiyu Zhao 14 / 43

## 第16页

Metrics to dene optimal policies - 1) The average value
How to select the distribution d? There are two cases.
The second case is that ddepends on the policy .
A common way to select dasd(s), which is the stationary
distribution under .Details of stationary distribution can be found in
the last lecture and the book.
One basic property of dis that it satises
dT
P=dT
;
wherePis the state transition probability matrix.
The interpretation of selecting dis as follows.
If one state is frequently visited in the long run, it is more
important and deserves more weight.
If a state is hardly visited, then we give it less weight.
Shiyu Zhao 15 / 43

## 第17页

Metrics to dene optimal policies - 2) The average reward
The second metric is average one-step reward or simply average
reward. In particular, the metric is
r:=X
s2Sd(s)r(s) =E[r(S)];
whereSd.Here,
r(s):=X
a2A(ajs)r(s;a)
is the average of the one-step immediate reward that can be obtained
starting from state s,and
r(s;a) =E[Rjs;a] =X
rrp(rjs;a)
The weight dis the stationary distribution.
As its name suggests, ris simply a weighted average of the one-step
immediate rewards.
Shiyu Zhao 16 / 43

## 第18页

Metrics to dene optimal policies - 2) The average reward
An equivalent denition!
Suppose an agent follows a given policy and generate a trajectory with
the rewards as (Rt+1;Rt+2;:::).
The average single-step reward along this trajectory is
lim
n!11
nEh
Rt+1+Rt+2++Rt+njSt=s0i
= lim
n!11
nE"nX
k=1Rt+kjSt=s0#
wheres0is the starting state of the trajectory.
Shiyu Zhao 17 / 43

## 第19页

Metrics to dene optimal policies - Remarks
An important property is that
lim
n!11
nE"nX
k=1Rt+kjSt=s0#
= lim
n!11
nE"nX
k=1Rt+k#
=X
sd(s)r(s)
= r
Note that
The starting state s0does not matter.
The two denitions of rare equivalent.
See the proof in the book.
Shiyu Zhao 18 / 43

## 第20页

Metrics to dene optimal policies - Remarks
Remark 1 about the metrics:
All these metrics are functions of .
Sinceis parameterized by , these metrics are functions of .
In other words, dierent values of can generate dierent metric
values.
Therefore, we can search for the optimal values of to maximize these
metrics.
This is the basic idea of policy gradient methods.
Shiyu Zhao 19 / 43

## 第21页

Metrics to dene optimal policies - Remarks
Remark 2 about the metrics:
One complication is that the metrics can be dened in either the
discounted case where 
2(0;1)or the undiscounted case where

= 1.
We only consider the discounted case so far in this book. For details
about the undiscounted case, see the book.
Shiyu Zhao 20 / 43

## 第22页

Metrics to dene optimal policies - Remarks
Remark 3 about the metrics:
Intuitively, ris more short-sighted because it merely considers the
immediate rewards, whereas vconsiders the total reward overall steps.
However, the two metrics are equivalent to each other.
In the discounted case where 
 <1, it holds that
r= (1 
)v:
See the proof in the book.
Shiyu Zhao 21 / 43

## 第23页

Metrics to dene optimal policies - Excise
Excise:
You will see the following metric often in the literature:
J() =E"1X
t=0
tRt+1#
What is its relationship to the metrics we introduced just now?
Shiyu Zhao 22 / 43

## 第24页

Metrics to dene optimal policies - Excise
J() =E"1X
t=0
tRt+1#
Answer: First, clarify and understand this metric.
It starts from S0dand thenA0;R1;S1;A1;R2;S2;:::
At(St)andRt+1;St+1p(Rt+1jSt;At);p(St+1jSt;At)
Then, we know this metric is the same as the average value because
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
Shiyu Zhao 23 / 43

## 第25页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
3Gradients of the metrics
4Gradient-ascent algorithm (REINFORCE)
5Summary
Shiyu Zhao 24 / 43

## 第26页

Gradients of the metrics
Given a metric, we next
derive its gradient
and then, apply gradient-based methods to optimize the metric.
The gradient calculation is one of the most complicated parts of policy
gradient methods! That is because
rst, we need to distinguish dierent metrics v,r,v0

second, we need to distinguish the discounted and undiscounted cases.
The calculation of the gradients:
We will not discuss the details in this lecture.
Interested readers may see my book for details.
Shiyu Zhao 25 / 43

## 第27页

Gradients of the metrics
Summary of the results about the gradients:
rJ() =X
s2S(s)X
a2Ar(ajs;)q(s;a)
where
J()can be v,r, orv0
.
\=" may denote strict equality, approximation, or proportional to.
is a distribution or weight of the states.
Shiyu Zhao 26 / 43

## 第28页

Gradients of the metrics
Some specic results:
rr'X
sd(s)X
ar(ajs;)q(s;a);
rv=1
1 
rr
rv0
=X
s2S(s)X
a2Ar(ajs;)q(s;a)
Details are not given here. Interested readers can read my book.
Shiyu Zhao 27 / 43

## 第29页

Gradients of the metrics
A compact and useful form of the gradient:
rJ() =X
s2S(s)X
a2Ar(ajs;)q(s;a)
=E
rln(AjS;)q(S;A)
whereSandA(AjS;).
Why is this expression useful?
Because we can use samples to approximate the gradient!
rJrln(ajs;)q(s;a)
Shiyu Zhao 28 / 43

## 第30页

Gradients of the metrics
rJ() =X
s2S(s)X
a2Ar(ajs;)q(s;a)
=E
rln(AjS;)q(S;A)
How to prove the above equation?
Consider the function lnwhere lnis the natural logarithm. It is easy to
see that
rln(ajs;) =r(ajs;)
(ajs;)
and hence
r(ajs;) =(ajs;)rln(ajs;):
Shiyu Zhao 29 / 43

## 第31页

Gradients of the metrics
Then, we have
rJ=X
sd(s)X
ar(ajs;)q(s;a)
=X
sd(s)X
a(ajs;)rln(ajs;)q(s;a)
=ESd"X
a(ajS;)rln(ajS;)q(S;a)#
=ESd;A
rln(AjS;)q(S;A)
:=E
rln(AjS;)q(S;A)
Shiyu Zhao 30 / 43

## 第32页

Gradients of the metrics
Some remarks: Because we need to calculate ln(ajs;), we must
ensure that for all s;a;
(ajs;)>0
This can be archived by using softmax functions that can normalize
the entries in a vector from ( 1;+1)to(0;1).
For example, for any vector x= [x1;:::;xn]T,
zi=exi
Pn
j=1exj
wherezi2(0;1)andPn
i=1zi= 1.
Then, the policy function has the form of
(ajs;) =eh(s;a; )
P
a02Aeh(s;a0;);
whereh(s;a; )is another function.
Shiyu Zhao 31 / 43

## 第33页

Gradients of the metrics
Some remarks:
Such a form based on the softmax function can be realized by a neural
network whose input is sand parameter is . The network has jAj
outputs, each of which corresponds to (ajs;)for an action a. The
activation function of the output layer should be softmax.
Since(ajs;)>0for alla, the parameterized policy is stochastic and
hence exploratory.
There also exist deterministic policy gradient (DPG) methods.
Shiyu Zhao 32 / 43

## 第34页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
3Gradients of the metrics
4Gradient-ascent algorithm (REINFORCE)
5Summary
Shiyu Zhao 33 / 43

## 第35页

Gradient-ascent algorithm
Now, we are ready to present the rst policy gradient algorithm to nd
optimal policies!
The gradient-ascent algorithm maximizing J()is
t+1=t+rJ()
=t+Eh
rln(AjS;t)q(S;A)i
The true gradient can be replaced by a stochastic one:
t+1=t+rln(atjst;t)q(st;at)
Shiyu Zhao 34 / 43

## 第36页

Gradient-ascent algorithm
Furthermore, since qis unknown, it can be approximated:
t+1=t+rln(atjst;t)qt(st;at)
There are dierent methods to approximate q(st;at)
In this lecture, Monte-Carlo based method, REINFORCE
In the next lecture, TD method and more
Shiyu Zhao 35 / 43

## 第37页

Gradient-ascent algorithm
Remark 1: How to do sampling?
ESd;Ah
rln(AjS;t)q(S;A)i
 !rln(ajs;t)q(s;a)
How to sample S?
Sd, where the distribution dis a long-run behavior under .
How to sample A?
A(AjS;). Hence,atshould be sampled following (t)atst.
Therefore, the policy gradient method is on-policy.
Shiyu Zhao 36 / 43

## 第38页

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
Shiyu Zhao 37 / 43

## 第39页

Gradient-ascent algorithm
It is a gradient-ascent algorithm for maximizing (atjst;):
t+1=t+tr(atjst;t)
Intuition: Whentis suciently small
Ift>0, the probability of choosing (st;at)is enhanced:
(atjst;t+1)>(atjst;t)
The greater tis, the stronger the enhancement is.
Ift<0, then(atjst;t+1)<(atjst;t).
Math: Whent+1 tis suciently small, we have
(atjst;t+1)(atjst;t) + (r(atjst;t))T(t+1 t)
=(atjst;t) +t(r(atjst;t))T(r(atjst;t))
=(atjst;t) +tkr(atjst;t)k2
Shiyu Zhao 38 / 43

## 第40页

Gradient-ascent algorithm
t+1=t+qt(st;at)
(atjst;t)
|{z}
tr(atjst;t)
The coecient tcan well balance exploration and exploitation.
First,tis proportional to qt(st;at).
Ifqt(st;at)is great, then tis great.
Therefore, the algorithm intends to enhance actions with greater
values.
Second,tis inversely proportional to (atjst;t).
If(atjst;t)is small, then tis large.
Therefore, the algorithm intends to explore actions that have low
probabilities.
Shiyu Zhao 39 / 43

## 第41页

REINFORCE algorithm
Recall that
t+1=t+rln(atjst;t)q(st;at)
is replaced by
t+1=t+rln(atjst;t)qt(st;at)
whereqt(st;at)is an approximation of q(st;at).
Ifq(st;at)is approximated by Monte Carlo estimation, the algorithm
has a specics name, REINFORCE.
REINFORCE is one of earliest and simplest policy gradient algorithms.
Many other policy gradient algorithms such as the actor-critic methods
can be obtained by extending REINFORCE (next lecture).
Shiyu Zhao 40 / 43

## 第42页

REINFORCE algorithm
Pseudocode: Policy Gradient by Monte Carlo (REINFORCE)
Initialization: A parameterized function (ajs;),
2(0;1), and>0.
Aim: Search for an optimal policy maximizing J().
For thekth iteration, do
Selects0and generate an episode following (k). Suppose the
episode isfs0;a0;r1;:::;sT 1;aT 1;rTg.
Fort= 0;1;:::;T 1, do
Value update: qt(st;at) =PT
k=t+1
k t 1rk
Policy update: t+1=t+rln(atjst;t)qt(st;at)
k=T
Shiyu Zhao 41 / 43

## 第43页

Outline
1Basic idea of policy gradient
2Metrics to dene optimal policies
3Gradients of the metrics
4Gradient-ascent algorithm (REINFORCE)
5Summary
Shiyu Zhao 42 / 43

## 第44页

Summary
Contents of this lecture:
Metrics for optimality
Gradients of the metrics
Gradient-ascent algorithm
A special case: REINFORCE
Next lecture: Actor-critic
Shiyu Zhao 43 / 43

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_Book-Mathematical-Foundation-of-Reinforcement-Learning-main_课程MOC|Book-Mathematical-Foundation-of-Reinforcement-Learning-main MOC]]
