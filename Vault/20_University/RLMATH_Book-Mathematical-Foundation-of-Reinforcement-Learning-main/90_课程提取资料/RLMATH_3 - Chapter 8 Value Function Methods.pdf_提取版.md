---
id: extract-rlmath-f130ef44
type: extract
status: extracted
course: RLMATH
source:
  - "[[91_Raw-Archive/PDF/RLMATH_3 - Chapter 8 Value Function Methods.pdf_课件_未知日期_f130ef44.pdf]]"
source_pages: all
source_hash: "f130ef447c0eae07ed6ada6b4cb7cbaa219420562234232274808cb46794503c"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 3 - Chapter 8 Value Function Methods.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

Chapter 8
Value Function Methods
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
Figure 8.1: Where we are in this book.
In this chapter, we continue to study temporal-dierence learning algorithms. How-
ever, a dierent method is used to represent state/action values. So far in this book,
state/action values have been represented by tables . The tabular method is straightfor-
ward to understand, but it is inecient for handling large state or action spaces. To
solve this problem, this chapter introduces the value function method, which has become
a standard way to represent values. It is also where articial neural networks are incorpo-
rated into reinforcement learning as function approximators. The idea of value function
can also be extended to policy function , as introduced in Chapter 9.
151

## 第2页

8.1. Value representation: From table to function
1
sˆv(s)
s1s2s3s4 · · · snˆv(s) =as+b
Figure 8.2: An illustration of the function approximation method. The x-axis and y-axis correspond to
sand ^v(s), respectively.
8.1 Value representation: From table to function
We next use an example to demonstrate the dierence between the tabular and function
approximation methods.
Suppose that there are nstatesfsign
i=1, whose state values are fv(si)gn
i=1. Here,
is a given policy. Let f^v(si)gn
i=1denote the estimates of the true state values. If we use
the tabular method, the estimated values can be maintained in the following table. This
table can be stored in memory as an array or a vector. To retrieve or update any value,
we can directly read or rewrite the corresponding entry in the table.
State s1s2 sn
Estimated value ^v(s1) ^v(s2) ^v(sn)
We next show that the values in the above table can be approximated by a function.
In particular,f(si;^v(si))gn
i=1are shown as npoints in Figure 8.2. These points can be
tted or approximated by a curve. The simplest curve is a straight line, which can be
described as
^v(s;w) =as+b= [s;1]|{z}
T(s)"
a
b#
|{z}
w=T(s)w: (8.1)
Here, ^v(s;w) is a function for approximating v(s). It is determined jointly by the state s
and the parameter vector w2R2. ^v(s;w) is sometimes written as ^ vw(s). Here,(s)2R2
is called the feature vector ofs.
The rst notable dierence between the tabular and function approximation methods
concerns how they retrieve and update a value.
How to retrieve a value: When the values are represented by a table, if we want to
retrieve a value, we can directly read the corresponding entry in the table. However,
152

## 第3页

8.1. Value representation: From table to function
when the values are represented by a function, it becomes slightly more complicated
to retrieve a value. In particular, we need to input the state index sinto the function
and calculate the function value (Figure 8.3). For the example in (8.1), we rst need
to calculate the feature vector (s) and then calculate T(s)w. If the function is
an articial neural network, a forward propagation from the input to the output is
needed.
w
functions ˆv(s, w)
Figure 8.3: An illustration of the process for retrieving the value of swhen using the function approxi-
mation method.
The function approximation method is more ecient in terms of storage due to the
way in which the state values are retrieved. Specically, while the tabular method
needs to store nvalues, we now only need to store a lower dimensional parameter
vectorw. Thus, the storage eciency can be signicantly improved. Such a benet
is, however, notfree. It comes with a cost: the state values may not be accurately
represented by the function. For example, a straight line is not able to accurately t
the points in Figure 8.2. That is why this method is called approximation. From a
fundamental point of view, some information will certainly be lost when we use a low-
dimensional vector to represent a high-dimensional dataset. Therefore, the function
approximation method enhances storage eciency by sacricing accuracy.
How to update a value: When the values are represented by a table, if we want
to update one value, we can directly rewrite the corresponding entry in the table.
However, when the values are represented by a function, the way to update a value is
completely dierent. Specically, we must update wto change the values indirectly.
How to update wto nd optimal state values will be addressed in detail later.
Thanks to the way in which the state values are updated, the function approximation
method has another merit: its generalization ability is stronger than that of the tabular
method. The reason is as follows. When using the tabular method, we can update
a value if the corresponding state is visited in an episode. The values of the states
that have not been visited cannot be updated. However, when using the function
approximation method, we need to update wto update the value of a state. The
update ofwalso aects the values of some other states even though these states have
not been visited. Therefore, the experience sample for one state can generalize to help
estimate the values of some other states.
The above analysis is illustrated in Figure 8.4, where there are three states fs1;s2;s3g.
153

## 第4页

8.1. Value representation: From table to function
Suppose that we have an experience sample for s3and would like to update ^ v(s3).
When using the tabular method, we can only update ^ v(s3) without changing ^ v(s1) or
^v(s2), as shown in Figure 8.4(a). When using the function approximation method,
updatingwnot only can update ^ v(s3) but also would change ^ v(s1) and ^v(s2), as shown
in Figure 8.4(b). Therefore, the experience sample of s3can help update the values
of its neighboring states.
1
sˆv(s)
s1s2s3update ˆv(s3) update ˆv(s3)
sˆv(s)
s1s2s3
(a) Tabular method: when ^ v(s3) is updated, the other values remain the same.
1
sˆv(s)
s1s2s3update wfors3 update wfors3
sˆv(s)
s1s2s3
(b) Function approximation method: when we update ^ v(s3) by changing w, the values of the
neighboring states are also changed.
Figure 8.4: An illustration of how to update the value of a state.
We can use more complex functions that have stronger approximation abilities than
straight lines. For example, consider a second-order polynomial:
^v(s;w) =as2+bs+c= [s2;s;1]|{z}
T(s)2
64a
b
c3
75
|{z}
w=T(s)w: (8.2)
We can use even higher-order polynomial curves to t the points. As the order of the
curve increases, the approximation accuracy can be improved, but the dimension of the
parameter vector also increases, requiring more storage and computational resources.
Note that ^v(s;w) in either (8.1) or (8.2) is linear inw(though it may be nonlinear
ins). This type of method is called linear function approximation , which is the simplest
function approximation method. To realize linear function approximation, we need to
select an appropriate feature vector (s). That is, we must decide, for example, whether
we should use a rst-order straight line or a second-order curve to t the points. The
selection of appropriate feature vectors is nontrivial. It requires prior knowledge of the
given task: the better we understand the task, the better the feature vectors we can select.
For instance, if we know that the points in Figure 8.2 are approximately located on a
154

## 第5页

8.2. TD learning of state values based on function approximation
straight line, we can use a straight line to t the points. However, such prior knowledge
is usually unknown in practice. If we do not have any prior knowledge, a popular solution
is to use articial neural networks as nonlinear function approximations.
Another important problem is how to nd the optimal parameter vector. If we know
fv(si)gn
i=1, this is a least-squares problem. The optimal parameter can be obtained by
optimizing the following objective function:
J1=nX
i=1 
^v(si;w) v(si)2=nX
i=1 
T(si)w v(si)2
=






2
64T(s1)
...
T(sn)3
75w 2
64v(s1)
...
v(sn)3
75






2
:=kw vk2;
where
:=2
64T(s1)
...
T(sn)3
752Rn2; v:=2
64v(s1)
...
v(sn)3
752Rn:
It can be veried that the optimal solution to this least-squares problem is
w= (T) 1v:
More information about least-squares problems can be found in [47, Section 3.3] and
[48, Section 5.14].
The curve-tting example presented in this section illustrates the basic idea of value
function approximation. This idea will be formally introduced in the next section.
8.2 TD learning of state values based on function
approximation
In this section, we show how to integrate the function approximation method into TD
learning to estimate the state values of a given policy. This algorithm will be extended
to learn action values and optimal policies in Section 8.3.
This section contains quite a few subsections and many coherent contents. It is better
for us to review the contents rst before diving into the details.
The function approximation method is formulated as an optimization problem. The
objective function of this problem is introduced in Section 8.2.1. The TD learning
algorithm for optimizing this objective function is introduced in Section 8.2.2.
155

## 第6页

8.2. TD learning of state values based on function approximation
To apply the TD learning algorithm, we need to select appropriate feature vectors.
Section 8.2.3 discusses this problem.
Examples are given in Section 8.2.4 to demonstrate the TD algorithm and the impacts
of dierent feature vectors.
A theoretical analysis of the TD algorithm is given in Section 8.2.5. This subsection
is mathematically intensive. Readers may read it selectively based on their interests.
8.2.1 Objective function
Letv(s) and ^v(s;w) be the true state value and approximated state value of s2S,
respectively. The problem to be solved is to nd an optimalwso that ^v(s;w) can best
approximate v(s) for every s. In particular, the objective function is
J(w) =E[(v(S) ^v(S;w))2]; (8.3)
where the expectation is calculated with respect to the random variable S2S. WhileS
is a random variable, what is its probability distribution? This question is important for
understanding this objective function. There are several ways to dene the probability
distribution of S.
The rst way is to use a uniform distribution . That is to treat all the states as equally
important by setting the probability of each state to 1 =n. In this case, the objective
function in (8.3) becomes
J(w) =1
nX
s2S(v(s) ^v(s;w))2; (8.4)
which is the average value of the approximation errors of all the states. However, this
way does not consider the real dynamics of the Markov process under the given policy.
Since some states may be rarely visited by a policy, it may be unreasonable to treat
all the states as equally important.
The second way, which is the focus of this chapter, is to use the stationary distribution .
The stationary distribution describes the long-term behavior of a Markov decision
process. More specically, after the agent executes a given policy for a suciently
long period, the probability of the agent being located at any state can be described
by this stationary distribution. Interested readers may see the details in Box 8.1.
Letfd(s)gs2Sdenote the stationary distribution of the Markov process under policy
. That is, the probability for the agent visiting safter a long period of time is d(s).
By denition,P
s2Sd(s) = 1. Then, the objective function in (8.3) can be rewritten
156

## 第7页

8.2. TD learning of state values based on function approximation
as
J(w) =X
s2Sd(s)(v(s) ^v(s;w))2; (8.5)
which is a weighted average of the approximation errors. The states that have higher
probabilities of being visited are given greater weights.
It is notable that the value of d(s) is nontrivial to obtain because it requires knowing
the state transition probability matrix P(see Box 8.1). Fortunately, we do not need to
calculate the specic value of d(s) to minimize this objective function as shown in the
next subsection. In addition, it was assumed that the number of states was nite when
we introduced (8.4) and (8.5). When the state space is continuous, we can replace the
summations with integrals.
Box 8.1: Stationary distribution of a Markov decision process
The key tool for analyzing stationary distribution is P2Rnn, which is the probabil-
ity transition matrix under the given policy . If the states are indexed as s1;:::;sn,
then [P]ijis dened as the probability for the agent moving from sitosj. The
denition of Pcan be found in Section 2.6.
Interpretation of Pk
(k= 1;2;3;:::).
First of all, it is necessary to examine the interpretation of the entries in Pk
. The
probability of the agent transitioning from sitosjusing exactly ksteps is denoted
as
p(k)
ij= Pr(Stk=jjSt0=i);
wheret0andtkare the initial and kth time steps, respectively. First, by the
denition of P, we have
[P]ij=p(1)
ij;
which means that [ P]ijis the probability of transitioning from sitosjusing a
single step . Second, consider P2
. It can be veried that
[P2
]ij= [PP]ij=nX
q=1[P]iq[P]qj:
Since [P]iq[P]qjis the joint probability of transitioning from sitosqand then
fromsqtosj, we know that [ P2
]ijis the probability of transitioning from sitosj
157

## 第8页

8.2. TD learning of state values based on function approximation
using exactly two steps . That is
[P2
]ij=p(2)
ij:
Similarly, we know that
[Pk
]ij=p(k)
ij;
which means that [ Pk
]ijis the probability of transitioning from sitosjusing
exactlyksteps .
Denition of stationary distributions.
Letd02Rnbe a vector representing the probability distribution of the states at
the initial time step. For example, if sis always selected as the starting state,
thend0(s) = 1 and the other entries of d0are 0. Let dk2Rnbe the vector
representing the probability distribution obtained after exactly ksteps starting
fromd0. Then, we have
dk(si) =nX
j=1d0(sj)[Pk
]ji; i= 1;2;:::: (8.6)
This equation indicates that the probability of the agent visiting siat stepk
equals the sum of the probabilities of the agent transitioning from fsjgn
j=1tosi
using exactly ksteps. The matrix-vector form of (8.6) is
dT
k=dT
0Pk
: (8.7)
When we consider the long-term behavior of the Markov process, it holds under
certain conditions that
lim
k!1Pk
=1ndT
; (8.8)
where 1n= [1;:::; 1]T2Rnand1ndT
is a constant matrix with all its rows
equal todT
. The conditions under which (8.8) is valid will be discussed later.
Substituting (8.8) into (8.7) yields
lim
k!1dT
k=dT
0lim
k!1Pk
=dT
01ndT
=dT
; (8.9)
where the last equality is valid because dT
01n= 1.
Equation (8.9) means that the state distribution dkconverges to a constant value
d, which is called the limiting distribution . The limiting distribution depends
158

## 第9页

8.2. TD learning of state values based on function approximation
on the system model and the policy . Interestingly, it is independent of the
initial distribution d0. That is, regardless of which state the agent starts from,
the probability distribution of the agent after a suciently long period can always
be described by the limiting distribution.
The value of dcan be calculated in the following way. Taking the limit of both
sides ofdT
k=dT
k 1Pgives lim k!1dT
k= limk!1dT
k 1Pand hence
dT
=dT
P: (8.10)
As a result, dis the left eigenvector of Passociated with the eigenvalue 1. The
solution of (8.10) is called the stationary distribution. It holds thatP
s2Sd(s) =
1 andd(s)>0 for alls2S. The reason why d(s)>0 (notd(s)0) will be
explained later.
Conditions for the uniqueness of stationary distributions.
The solution dof (8.10) is usually called a stationary distribution, whereas the
distribution din (8.9) is usually called the limiting distribution. Note that (8.9)
implies (8.10), but the converse may not be true. A general class of Markov
processes that have unique stationary (or limiting) distributions is irreducible (or
regular ) Markov processes. Some necessary denitions are given below. More
details can be found in [49, Chapter IV].
- Statesjis said to be accessible from state siif there exists a nite integer k
so that [P]k
ij>0, which means that the agent starting from sican possibly
reachsjafter a nite number of transitions.
- If two states siandsjare mutually accessible, then the two states are said to
communicate .
- A Markov process is called irreducible if all of its states communicate with each
other. In other words, the agent starting from an arbitrary state can possibly
reach any other state within a nite number of steps. Mathematically, it
indicates that, for any siandsj, there exists k1 such that [ Pk
]ij>0 (the
value ofkmay vary for dierent i;j).
- A Markov process is called regular if there exists k1 such that [ Pk
]ij>0
for alli;j. Equivalently, there exists k1 such that Pk
>0, where>is
elementwise. As a result, it is possible that every state is reachable from any
other state within at most ksteps. A regular Markov process is also irreducible,
but the converse is not true. However, if a Markov process is irreducible and
there exists isuch that [P]ii>0, then it is also regular. Moreover, if Pk
>0,
thenPk0
>0 for anyk0ksinceP0. It then follows from (8.9) that
d(s)>0 for every s.
159

## 第10页

8.2. TD learning of state values based on function approximation
Policies that may lead to unique stationary distributions.
Once the policy is given, a Markov decision process becomes a Markov process,
whose long-term behavior is jointly determined by the given policy and the system
model. Then, an important question is what kind of policies can lead to regular
Markov processes? In general, the answer is exploratory policies such as-greedy
policies. That is because an exploratory policy has a positive probability of taking
any action at any state. As a result, the states can communicate with each other
when the system model allows them to do so.
An example is given in Figure 8.5 to illustrate stationary distributions. The policy
in this example is -greedy with = 0:5. The states are indexed as s1;s2;s3;s4,
which correspond to the top-left, top-right, bottom-left, and bottom-right cells in
the grid, respectively.
We compare two methods to calculate the stationary distributions. The rst
method is to solve (8.10) to get the theoretical value of d. The second method is
to estimate dnumerically: we start from an arbitrary initial state and generate a
suciently long episode by following the given policy. Then, dcan be estimated
by the ratio between the number of times each state is visited in the episode and
the total length of the episode. The estimation result is more accurate when the
episode is longer. We next compare the theoretical and estimated results.
Figure 8.5: Long-term behavior of an -greedy policy with = 0:5. The asterisks in the right
gure represent the theoretical values of the elements of d.
- Theoretical value of d: It can be veried that the Markov process induced
by the policy is both irreducible and regular. That is due to the following
reasons. First, since all the states communicate, the resulting Markov process
is irreducible. Second, since every state can transition to itself, the resulting
160

## 第11页

8.2. TD learning of state values based on function approximation
Markov process is regular. It can be seen from Figure 8.5 that
PT
=2
66640:3 0:1 0:1 0
0:1 0:3 0 0:1
0:6 0 0:3 0:1
0 0:6 0:6 0:83
7775:
The eigenvalues of PT
can be calculated as f 0:0449;0:3;0:4449;1g. The
unit-length (right) eigenvector of PT
corresponding to the eigenvalue 1 is
[0:0463;0:1455;0:1785;0:9720]T. After scaling this vector so that the sum of
all its elements is equal to 1, we obtain the theoretical value of das follows:
d=2
66640:0345
0:1084
0:1330
0:72413
7775:
Theith element of dcorresponds to the probability of the agent visiting si
in the long run.
- Estimated value of d: We next verify the above theoretical value of dby
executing the policy for suciently many steps in the simulation. Specically,
we selects1as the starting state and run 1,000 steps by following the policy.
The proportion of the visits of each state during the process is shown in Fig-
ure 8.5. It can be seen that the proportions converge to the theoretical value
ofdafter hundreds of steps.
8.2.2 Optimization algorithms
To minimize the objective function J(w) in (8.3), we can use the gradient descent algo-
rithm:
wk+1=wk krwJ(wk);
where
rwJ(wk) =rwE[(v(S) ^v(S;wk))2]
=E[rw(v(S) ^v(S;wk))2]
= 2E[(v(S) ^v(S;wk))( rw^v(S;wk))]
= 2E[(v(S) ^v(S;wk))rw^v(S;wk)]:
161

## 第12页

8.2. TD learning of state values based on function approximation
Therefore, the gradient descent algorithm is
wk+1=wk+ 2kE[(v(S) ^v(S;wk))rw^v(S;wk)]; (8.11)
where the coecient 2 before kcan be merged into kwithout loss of generality. The
algorithm in (8.11) requires calculating the expectation. In the spirit of stochastic gra-
dient descent, we can replace the true gradient with a stochastic gradient. Then, (8.11)
becomes
wt+1=wt+t 
v(st) ^v(st;wt)
rw^v(st;wt); (8.12)
wherestis a sample of Sat timet.
Notably, (8.12) is notimplementable because it requires the true state value v, which
is unknown and must be estimated. We can replace v(st) with an approximation to make
the algorithm implementable. The following two methods can be used to do so.
Monte Carlo method: Suppose that we have an episode ( s0;r1;s1;r2;:::). Letgtbe
the discounted return starting from st. Then,gtcan be used as an approximation of
v(st). The algorithm in (8.12) becomes
wt+1=wt+t 
gt ^v(st;wt)
rw^v(st;wt):
This is the algorithm of Monte Carlo learning with function approximation.
Temporal-dierence method: In the spirit of TD learning, rt+1+
^v(st+1;wt) can be
used as an approximation of v(st). The algorithm in (8.12) becomes
wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt): (8.13)
This is the algorithm of TD learning with function approximation. This algorithm is
summarized in Algorithm 8.1.
Understanding the TD algorithm in (8.13) is important for studying the other algo-
rithms in this chapter. Notably, (8.13) can only learn the state values of a given policy.
It will be extended to algorithms that can learn action values in Sections 8.3.1 and 8.3.2.
8.2.3 Selection of function approximators
To apply the TD algorithm in (8.13), we need to select appropriate ^ v(s;w). There are two
ways to do that. The rst is to use an articial neural network as a nonlinear function
approximator. The input of the neural network is the state, the output is ^ v(s;w), and
the network parameter is w. The second is to simply use a linear function:
^v(s;w) =T(s)w;
162

## 第13页

8.2. TD learning of state values based on function approximation
Algorithm 8.1: TD learning of state values with function approximation
Initialization: A function ^v(s;w)that is dierentiable in w. Initial parameter w0.
Goal: Learn the true state values of a given policy .
For each episodef(st;rt+1;st+1)gtgenerated by , do
For each sample (st;rt+1;st+1), do
In the general case, wt+1=wt+t[rt+1+
^v(st+1;wt) ^v(st;wt)]rw^v(st;wt)
In the linear case, wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st)
where(s)2Rmis the feature vector of s. The lengths of (s) andware equal to m,
which is usually much smaller than the number of states. In the linear case, the gradient
is
rw^v(s;w) =(s);
Substituting which into (8.13) yields
wt+1=wt+t
rt+1+
T(st+1)wt T(st)wt
(st): (8.14)
This is the algorithm of TD learning with linear function approximation. We call it
TD-Linear for short.
The linear case is much better understood in theory than the nonlinear case. However,
its approximation ability is limited. It is also nontrivial to select appropriate feature
vectors for complex tasks. By contrast, articial neural networks can approximate values
as black-box universal nonlinear approximators, which are more friendly to use.
Nevertheless, it is still meaningful to study the linear case. A better understanding
of the linear case can help readers better grasp the idea of the function approximation
method. Moreover, the linear case is sucient for solving the simple grid world tasks
considered in this book. More importantly, the linear case is still powerful in the sense
that the tabular method can be viewed as a special linear case. More information can be
found in Box 8.2.
Box 8.2: Tabular TD learning is a special case of TD-Linear
We next show that the tabular TD algorithm in (7.1) in Chapter 7 is a special case
of the TD-Linear algorithm in (8.14).
Consider the following special feature vector for any s2S:
(s) =es2Rn;
whereesis the vector with the entry corresponding to sequal to 1 and the other
163

## 第14页

8.2. TD learning of state values based on function approximation
entries equal to 0. In this case,
^v(s;w) =eT
sw=w(s);
wherew(s) is the entry in wthat corresponds to s. Substituting the above equation
into (8.14) yields
wt+1=wt+t 
rt+1+
wt(st+1) wt(st)
est:
The above equation merely updates the entry wt(st) due to the denition of est.
Motivated by this, multiplying eT
ston both sides of the equation yields
wt+1(st) =wt(st) +t 
rt+1+
wt(st+1) wt(st)
;
which is exactly the tabular TD algorithm in (7.1).
In summary, by selecting the feature vector as (s) =es, the TD-Linear algorithm
becomes the tabular TD algorithm.
8.2.4 Illustrative examples
We next present some examples for demonstrating how to use the TD-Linear algorithm
in (8.14) to estimate the state values of a given policy. In the meantime, we demonstrate
how to select feature vectors.
1 2 3 4 5
1
2
3
4
5
(a)
1 2 3 4 5
1
2
3
4
5-3.8 -3.8 -3.6 -3.1 -3.2
-3.8 -3.8 -3.8 -3.1 -2.9
-3.6 -3.9 -3.4 -3.2 -2.9
-3.9 -3.6 -3.4 -2.9 -3.2
-4.5 -4.2 -3.4 -3.4 -3.5 (b)
 (c)
Figure 8.6: (a) The policy to be evaluated. (b) The true state values are represented as a table. (c) The
true state values are represented as a 3D surface.
The grid world example is shown in Figure 8.6. The given policy takes any action at a
state with a probability of 0.2. Our goal is to estimate the state values under this policy.
There are 25 state values in total. The true state values are shown in Figure 8.6(b). The
true state values are visualized as a three-dimensional surface in Figure 8.6(c).
164

## 第15页

8.2. TD learning of state values based on function approximation
We next show that we can use fewer than 25 parameters to approximate these state
values. The simulation setup is as follows. Five hundred episodes are generated by the
given policy. Each episode has 500 steps and starts from a randomly selected state-action
pair following a uniform distribution. In addition, in each simulation trial, the parameter
vectorwis randomly initialized such that each element is drawn from a standard normal
distribution with a zero mean and a standard deviation of 1. We set rforbidden =rboundary =
 1,rtarget = 1, and
= 0:9.
To implement the TD-Linear algorithm, we need to select the feature vector (s) rst.
There are dierent ways to do that as shown below.
The rst type of feature vector is based on polynomials. In the grid world example, a
statescorresponds to a 2D location. Let xandydenote the column and row indexes
ofs, respectively. To avoid numerical issues, we normalize xandyso that their values
are within the interval of [  1;+1]. With a slight abuse of notation, the normalized
values are also represented by xandy. Then, the simplest feature vector is
(s) ="
x
y#
2R2:
In this case, we have
^v(s;w) =T(s)w= [x;y]"
w1
w2#
=w1x+w2y:
Whenwis given, ^v(s;w) =w1x+w2yrepresents a 2D plane that passes through the
origin. Since the surface of the state values may not pass through the origin, we need
to introduce a bias to the 2D plane to better approximate the state values. To do
that, we consider the following 3D feature vector:
(s) =2
641
x
y3
752R3: (8.15)
In this case, the approximated state value is
^v(s;w) =T(s)w= [1;x;y]2
64w1
w2
w33
75=w1+w2x+w3y:
Whenwis given, ^v(s;w) corresponds to a plane that may not pass through the origin.
Notably,(s) can also be dened as (s) = [x;y;1]T, where the order of the elements
does not matter.
The estimation result when we use the feature vector in (8.15) is shown in Fig-
165

## 第16页

8.2. TD learning of state values based on function approximation
ure 8.7(a). It can be seen that the estimated state values form a 2D plane. Although
the estimation error converges as more episodes are used, the error cannot decrease
to zero due to the limited approximation ability of a 2D plane.
To enhance the approximation ability, we can increase the dimension of the feature
vector. To that end, consider
(s) = [1;x;y;x2;y2;xy]T2R6: (8.16)
In this case, ^ v(s;w) =T(s)w=w1+w2x+w3y+w4x2+w5y2+w6xy, which
corresponds to a quadratic 3D surface. We can further increase the dimension of the
feature vector:
(s) = [1;x;y;x2;y2;xy;x3;y3;x2y;xy2]T2R10: (8.17)
The estimation results when we use the feature vectors in (8.16) and (8.17) are shown
in Figures 8.7(b)-(c). As can be seen, the longer the feature vector is, the more
accurately the state values can be approximated. However, in all three cases, the
estimation error cannot converge to zero because these linear approximators still have
limited approximation abilities.
0100200300400500
Episode index012345State value error (RMSE)TD-Linear: =0.0005
(a)(s)2R3
0100200300400500
Episode index012345State value error (RMSE)TD-Linear: =0.0005(b)(s)2R6
0100200300400500
Episode index00.511.522.533.5State value error (RMSE)TD-Linear: =0.0005(c)(s)2R10
Figure 8.7: TD-Linear estimation results obtained with the polynomial features in (8.15), (8.16), and
(8.17).
In addition to polynomial feature vectors, many other types of features are available
such as Fourier basis and tile coding [3, Chapter 9]. First, the values of xandyof
166

## 第17页

8.2. TD learning of state values based on function approximation
0100200300400500
Episode index012345State value error (RMSE)TD-Linear: =0.0005
(a)q= 1 and(s)2R4
0100200300400500
Episode index012345State value error (RMSE)TD-Linear: =0.0005(b)q= 2 and(s)2R9
0100200300400500
Episode index0123456State value error (RMSE)TD-Linear: =0.0005(c)q= 3 and(s)2R16
Figure 8.8: TD-Linear estimation results obtained with the Fourier features in (8.18).
each state are normalized to the interval of [0 ;1]. The resulting feature vector is
(s) =2
664...
cos 
(c1x+c2y)
...3
7752R(q+1)2; (8.18)
wheredenotes the circumference ratio, which is 3 :1415:::, instead of a policy. Here,
c1orc2can be set as any integers in f0;1;:::;qg, whereqis a user-specied integer.
As a result, there are ( q+ 1)2possible values for the pair ( c1;c2) to take. Hence, the
dimension of (s) is (q+ 1)2. For example, in the case of q= 1, the feature vector is
(s) =2
6664cos 
(0x+ 0y)
cos 
(0x+ 1y)
cos 
(1x+ 0y)
cos 
(1x+ 1y)3
7775=2
66641
cos(y)
cos(x)
cos((x+y))3
77752R4:
The estimation results obtained when we use the Fourier features with q= 1;2;3 are
shown in Figure 8.8. The dimensions of the feature vectors in the three cases are
4;9;16, respectively. As can be seen, the higher the dimension of the feature vector
is, the more accurately the state values can be approximated.
8.2.5 Theoretical analysis
Thus far, we have nished describing the story of TD learning with function approxima-
tion. This story started from the objective function in (8.3). To optimize this objective
167

## 第18页

8.2. TD learning of state values based on function approximation
function, we introduced the stochastic algorithm in (8.12). Later, the true value function
in the algorithm, which was unknown, was replaced by an approximation, leading to the
TD algorithm in (8.13). Although this story is helpful for understanding the basic idea
of value function approximation, it is not mathematically rigorous. For example, the
algorithm in (8.13) actually does not minimize the objective function in (8.3).
We next present a theoretical analysis of the TD algorithm in (8.13) to reveal why
the algorithm works eectively and what mathematical problems it solves. Since gen-
eral nonlinear approximators are dicult to analyze, this part only considers the linear
case. Readers are advised to read selectively based on their interests since this part is
mathematically intensive.
Convergence analysis
To study the convergence property of (8.13), we rst consider the following deterministic
algorithm:
wt+1=wt+tEh 
rt+1+
T(st+1)wt T(st)wt
(st)i
; (8.19)
where the expectation is calculated with respect to the random variables st;st+1;rt+1.
The distribution of stis assumed to be the stationary distribution d. The algorithm
in (8.19) is deterministic because the random variables st;st+1;rt+1all disappear after
calculating the expectation.
Why would we consider this deterministic algorithm? First, the convergence of this
deterministic algorithm is easier (though nontrivial) to analyze. Second and more im-
portantly, the convergence of this deterministic algorithm implies the convergence of the
stochastic TD algorithm in (8.13). That is because (8.13) can be viewed as a stochastic
gradient descent (SGD) implementation of (8.19). Therefore, we only need to study the
convergence property of the deterministic algorithm.
Although the expression of (8.19) may look complex at rst glance, it can be greatly
simplied. To do that, dene
 =2
664...
T(s)
...3
7752Rnm; D =2
664...
d(s)
...3
7752Rnn; (8.20)
where  is the matrix containing all the feature vectors, and Dis a diagonal matrix with
the stationary distribution in its diagonal entries. The two matrices will be frequently
used.
Lemma 8.1. The expectation in (8.19) can be rewritten as
Eh 
rt+1+
T(st+1)wt T(st)wt
(st)i
=b Awt;
168

## 第19页

8.2. TD learning of state values based on function approximation
where
A:= TD(I 
P)2Rmm;
b:= TDr2Rm: (8.21)
Here,P;rare the two terms in the Bellman equation v=r+
Pv, andIis the
identity matrix with appropriate dimensions.
The proof is given in Box 8.3. With the expression in Lemma 8.1, the deterministic
algorithm in (8.19) can be rewritten as
wt+1=wt+t(b Awt); (8.22)
which is a simple deterministic process. Its convergence is analyzed below.
First, what is the converged value of wt? Hypothetically, if wtconverges to a constant
valuewast!1 , then (8.22) implies w=w+1(b Aw), which suggests that
b Aw= 0 and hence
w=A 1b:
Several remarks about this converged value are given below.
IsAinvertible? The answer is yes. In fact, Ais not only invertible but also positive
denite. That is, for any nonzero vector xwith appropriate dimensions, xTAx > 0.
The proof is given in Box 8.4.
What is the interpretation of w=A 1b? It is actually the optimal solution for min-
imizing the projected Bellman error . The details will be introduced in Section 8.2.5.
The tabular method is a special case. One interesting result is that, when the di-
mensionality of wequalsn=jSjand(s) = [0;:::; 1;:::; 0]T, where the entry corre-
sponding to sis 1, we have
w=A 1b=v: (8.23)
This equation indicates that the parameter vector to be learned is actually the true
state value. This conclusion is consistent with the fact that the tabular TD algorithm
is a special case of the TD-Linear algorithm, as introduced in Box 8.2. The proof
of (8.23) is given below. It can be veried that  = Iin this case and hence A=
TD(I 
P) =D(I 
P) andb= TDr=Dr. Thus,w=A 1b=
(I 
P) 1D 1Dr= (I 
P) 1r=v:
Second, we prove that wtin (8.22) converges to w=A 1bast!1 . Since (8.22) is
a simple deterministic process, it can be proven in many ways. We present two proofs as
follows.
169

## 第20页

8.2. TD learning of state values based on function approximation
Proof 1: Dene the convergence error as t:=wt w. We only need to show that t
converges to zero. To do that, substituting wt=t+winto (8.22) gives
t+1=t tAt= (I tA)t:
It then follows that
t+1= (I tA)(I 0A)0:
Consider the simple case where t=for allt. Then, we have
kt+1k2kI Akt+1
2k0k2:
When > 0 is suciently small, we have that kI Ak2<1 and hence t!0 as
t!1 . The reason why kI Ak2<1 holds is that Ais positive denite and hence
xT(I A)x<1 for anyx.
Proof 2: Consider g(w):=b Aw. Sincewis the root of g(w) = 0, the task is actually
a root-nding problem. The algorithm in (8.22) is actually a Robbins-Monro (RM)
algorithm. Although the original RM algorithm was designed for stochastic processes,
it can also be applied to deterministic cases. The convergence of RM algorithms can
shed light on the convergence of wt+1=wt+t(b Awt). That is, wtconverges to
wwhenP
tt=1andP
t2
t<1.
Box 8.3: Proof of Lemma 8.1
By using the law of total expectation, we have
Eh
rt+1(st) +(st) 

T(st+1) T(st)
wti
=X
s2Sd(s)Eh
rt+1(st) +(st) 

T(st+1) T(st)
wtst=si
=X
s2Sd(s)Eh
rt+1(st)st=si
+X
s2Sd(s)Eh
(st) 

T(st+1) T(st)
wtst=si
:
(8.24)
Here,stis assumed to obey the stationary distribution d.
First, consider the rst term in (8.24). Note that
Eh
rt+1(st)st=si
=(s)Eh
rt+1st=si
=(s)r(s);
wherer(s) =P
a(ajs)P
rrp(rjs;a). Then, the rst term in (8.24) can be rewritten
170

## 第21页

8.2. TD learning of state values based on function approximation
as
X
s2Sd(s)Eh
rt+1(st)st=si
=X
s2Sd(s)(s)r(s) = TDr; (8.25)
wherer= [;r(s);]T2Rn.
Second, consider the second term in (8.24). Since
Eh
(st) 

T(st+1) T(st)
wtst=si
= Eh
(st)T(st)wtst=si
+Eh

(st)T(st+1)wtst=si
= (s)T(s)wt+
(s)Eh
T(st+1)st=si
wt
= (s)T(s)wt+
(s)X
s02Sp(s0js)T(s0)wt;
the second term in (8.24) becomes
X
s2Sd(s)Eh
(st) 

T(st+1) T(st)
wtst=si
=X
s2Sd(s)h
 (s)T(s)wt+
(s)X
s02Sp(s0js)T(s0)wti
=X
s2Sd(s)(s)h
 (s) +
X
s02Sp(s0js)(s0)iT
wt
= TD(  +
P)wt
= TD(I 
P)wt: (8.26)
Combining (8.25) and (8.26) gives
Eh 
rt+1+
T(st+1)wt T(st)wt
(st)i
= TDr TD(I 
P)wt
:=b Awt; (8.27)
whereb:= TDrandA:= TD(I 
P).
Box 8.4: Proving that A= TD(I 
P)is invertible and positive denite.
The matrix Ais positive denite if xTAx > 0 for any nonzero vector xwith ap-
propriate dimensions. If Ais positive (or negative) denite, it is denoted as A0
(orA0). Here,andshould be dierentiated from >and<, which indicate
elementwise comparisons. Note that Amay not be symmetric. Although positive
171

## 第22页

8.2. TD learning of state values based on function approximation
denite matrices often refer to symmetric matrices, nonsymmetric ones can also be
positive denite.
We next prove that A0 and hence Ais invertible. The idea for proving A0
is to show that
D(I 
P):=M0: (8.28)
It is clear that M0 impliesA= TM0 since  is a tall matrix with full column
rank (suppose that the feature vectors are selected to be linearly independent). Note
that
M=M+MT
2+M MT
2:
SinceM MTis skew-symmetric and hence xT(M MT)x= 0 for any x, we know
thatM0 if and only if M+MT0. To show M+MT0, we apply the fact
that strictly diagonal dominant matrices are positive denite [4].
First, it holds that
(M+MT)1n>0; (8.29)
where 1n= [1;:::; 1]T2Rn. The proof of (8.29) is given below. Since P1n=1n,
we haveM1n=D(I 
P)1n=D(1n 
1n) = (1 
)d. Moreover, MT1n=
(I 
PT
)D1n= (I 
PT
)d= (1 
)d, where the last equality is valid because
PT
d=d. In summary, we have
(M+MT)1n= 2(1 
)d:
Since all the entries of dare positive (see Box 8.1), we have ( M+MT)1n>0.
Second, the elementwise form of (8.29) is
nX
j=1[M+MT]ij>0; i = 1;:::;n;
which can be further written as
[M+MT]ii+X
j6=i[M+MT]ij>0:
It can be veried according to the expression of Min (8.28) that the diagonal entries
ofMare positive and the o-diagonal entries of Mare nonpositive. Therefore, the
172

## 第23页

8.2. TD learning of state values based on function approximation
above inequality can be rewritten as
[M+MT]ii>X
j6=i[M+MT]ij:
The above inequality indicates that the absolute value of the ith diagonal entry in
M+MTis greater than the sum of the absolute values of the o-diagonal entries
in the same row. Thus, M+MTis strictly diagonal dominant and the proof is
complete.
TD learning minimizes the projected Bellman error
While we have shown that the TD-Linear algorithm converges to w=A 1b, we next
show thatwis the optimal solution that minimizes the projected Bellman error . To do
that, we review three objective functions.
The rst objective function is
JE(w) =E[(v(S) ^v(S;w))2];
which has been introduced in (8.3). By the denition of expectation, JE(w) can be
reexpressed in a matrix-vector form as
JE(w) =k^v(w) vk2
D;
wherevis the true state value vector and ^ v(w) is the approximated one. Here, kk2
D
is a weighted norm: kxk2
D=xTDx=kD1=2xk2
2, whereDis given in (8.20).
This is the simplest objective function that we can imagine when talking about func-
tion approximation. However, it relies on the true state, which is unknown. To obtain
an implementable algorithm, we must consider other objective functions such as the
Bellman error and projected Bellman error [50{54].
The second objective function is the Bellman error. In particular, since vsatises
the Bellman equation v=r+
Pv, it is expected that the estimated value ^ v(w)
should also satisfy this equation to the greatest extent possible. Thus, the Bellman
error is
JBE(w) =k^v(w) (r+
P^v(w))k2
D:=k^v(w) T(^v(w))k2
D: (8.30)
Here,T() is the Bellman operator. In particular, for any vector x2Rn, the Bellman
operator is dened as
T(x):=r+
Px:
173

## 第24页

8.2. TD learning of state values based on function approximation
Minimizing the Bellman error is a standard least-squares problem. The details of the
solution are omitted here.
Third, it is notable that JBE(w) in (8.30) may not be minimized to zero due to the
limited approximation ability of the approximator. By contrast, an objective function
that can be minimized to zero is the projected Bellman error :
JPBE(w) =k^v(w) MT(^v(w))k2
D;
whereM2Rnnis the orthogonal projection matrix that geometrically projects any
vector onto the space of all approximations.
In fact, the TD learning algorithm in (8.13) aims to minimize the projected Bellman
errorJPBE rather than JEorJBE. The reason is as follows. For the sake of simplicity,
consider the linear case where ^ v(w) = w. Here,  is dened in (8.20). The range space
of  is the set of all possible linear approximations. Then,
M= (TD) 1TD2Rnn
is the projection matrix that geometrically projects any vector onto the range space .
Since ^v(w) is in the range space of , we can always nd a value of wthat can minimize
JPBE(w) to zero. It can be proven that the solution minimizing JPBE(w) isw=A 1b.
That is
w=A 1b= arg min
wJPBE(w);
The proof is given in Box 8.5.
Box 8.5: Showing that w=A 1bminimizes JPBE(w)
We next show that w=A 1bis the optimal solution that minimizes JPBE(w). Since
JPBE(w) = 0,^v(w) MT(^v(w)) = 0, we only need to study the root of
^v(w) =MT(^v(w)):
In the linear case, substituting ^ v(w) = wand the expression of Minto the above
equation gives
w= (TD) 1TD(r+
Pw): (8.31)
174

## 第25页

8.2. TD learning of state values based on function approximation
Since  has full column rank, we have  x= y,x=yfor anyx;y. Therefore,
(8.31) implies
w= (TD) 1TD(r+
Pw)
() TD(r+
Pw) = (TD)w
() TDr+
TDPw= (TD)w
() TDr= TD(I 
P)w
()w= (TD(I 
P)) 1TDr=A 1b;
whereA;bare given in (8.21). Therefore, w=A 1bis the optimal solution that
minimizesJPBE(w).
Since the TD algorithm aims to minimize JPBE rather than JE, it is natural to ask
how close the estimated value ^ v(w) is to the true state value v. In the linear case, the
estimated value that minimizes the projected Bellman error is ^ v(w) = w. Its deviation
from the true state value vsatises
k^v(w) vkD=kw vkD1
1 
min
wk^v(w) vkD=1
1 
min
wp
JE(w):
(8.32)
The proof of this inequality is given in Box 8.6. Inequality (8.32) indicates that the
discrepancy between  wandvis bounded from above by the minimum value of JE(w).
However, this bound is loose, especially when 
is close to one. It is thus mainly of
theoretical value.
Box 8.6: Proof of the error bound in (8.32)
Note that
kw vkD=kw Mv+Mv vkD
kw MvkD+kMv vkD
=kMT(w) MT(v)kD+kMv vkD; (8.33)
where the last equality is due to  w=MT(w) andv=T(v). Substituting
MT(w) MT(v) =M(r+
Pw) M(r+
Pv) =
MP(w v)
175

## 第26页

8.2. TD learning of state values based on function approximation
into (8.33) yields
kw vkDk
MP(w v)kD+kMv vkD

kMkDkP(w v)kD+kMv vkD
=
kP(w v)kD+kMv vkD (becausekMkD= 1)

kw vkD+kMv vkD: (becausekPxkDkxkDfor allx)
The proof ofkMkD= 1 andkPxkDkxkDare postponed to the end of the box.
Recognizing the above inequality gives
kw vkD1
1 
kMv vkD
=1
1 
min
wk^v(w) vkD;
where the last equality is because kMv vkDis the error between vand its
orthogonal projection into the space of all possible approximations. Therefore, it is
the minimum value of the error between vand any ^v(w).
We next prove some useful facts, which have already been used in the above proof.
Properties of matrix weighted norms. By denition, kxkD=p
xTDx=kD1=2xk2.
The induced matrix norm is kAkD= maxx6=0kAxkD=kxkD=kD1=2AD 1=2k2. For
matricesA;B with appropriate dimensions, we have kABxkDkAkDkBkDkxkD.
To see that,kABxkD=kD1=2ABxk2=kD1=2AD 1=2D1=2BD 1=2D1=2xk2
kD1=2AD 1=2k2kD1=2BD 1=2k2kD1=2xk2=kAkDkBkDkxkD.
Proof ofkMkD= 1. This is valid because kMkD=k(TD) 1TDkD=
kD1=2(TD) 1TDD 1=2k2= 1, where the last equality is valid due to the
fact that the matrix in the L2-norm is an orthogonal projection matrix and the
L2-norm of any orthogonal projection matrix is equal to one.
Proof ofkPxkDkxkDfor anyx2Rn. First,
kPxk2
D=xTPT
DPx=X
i;jxi[PT
DP]ijxj=X
i;jxi X
k[PT
]ik[D]kk[P]kj!
xj:
176

## 第27页

8.2. TD learning of state values based on function approximation
Reorganizing the above equation gives
kPxk2
D=X
k[D]kkX
i[P]kixi2
X
k[D]kkX
i[P]kix2
i
(due to Jensen's inequality [55,56])
=X
iX
k[D]kk[P]ki
x2
i
=X
i[D]iix2
i (due todT
P=dT
)
=kxk2
D:
Least-squares TD
We next introduce an algorithm called least-squares TD (LSTD) [57]. Like the TD-Linear
algorithm, LSTD aims to minimize the projected Bellman error. However, it has some
advantages over the TD-Linear algorithm.
Recall that the optimal parameter for minimizing the projected Bellman error is
w=A 1b, whereA= TD(I 
P) andb= TDr. In fact, it follows from (8.27)
thatAandbcan also be written as
A=Eh
(st) 
(st) 
(st+1)Ti
;
b=Eh
rt+1(st)i
:
The above two equations show that Aandbare expectations of st;st+1;rt+1. The idea of
LSTD is simple: if we can use random samples to directly obtain the estimates of Aand
b, which are denoted as ^Aand^b, then the optimal parameter can be directly estimated
asw^A 1^b.
In particular, suppose that ( s0;r1;s1;:::;st;rt+1;st+1;:::) is a trajectory obtained
by following a given policy . Let ^Atand^btbe the estimates of Aandbat timet,
respectively. They are calculated as the averages of the samples:
^At=t 1X
k=0(sk) 
(sk) 
(sk+1)T;
^bt=t 1X
k=0rk+1(sk): (8.34)
Then, the estimated parameter is
wt=^A 1
t^bt:
177

## 第28页

8.2. TD learning of state values based on function approximation
The reader may wonder if a coecient of 1 =tis missing on the right-hand side of (8.34).
In fact, it is omitted for the sake of simplicity since the value of wtremains the same
when it is omitted. Since ^Atmay not be invertible especially when tis small, ^Atis usually
biased by a small constant matrix I, whereIis the identity matrix and is a small
positive number.
The advantage of LSTD is that it uses experience samples more eciently and con-
verges faster than the TD method. That is because this algorithm is specically designed
based on the knowledge of the optimal solution's expression. The better we understand
a problem, the better algorithms we can design.
The disadvantages of LSTD are as follows. First, it can only estimate state values.
By contrast, the TD algorithm can be extended to estimate action values as shown in the
next section. Moreover, while the TD algorithm allows nonlinear approximators, LSTD
does not. That is because this algorithm is specically designed based on the expression
ofw. Second, the computational cost of LSTD is higher than that of TD since LSTD
updates an mmmatrix in each update step, whereas TD updates an m-dimensional
vector. More importantly, in every step, LSTD needs to compute the inverse of ^At, whose
computational complexity is O(m3). The common method for resolving this problem is
to directly update the inverse of ^Atrather than updating ^At. In particular, ^At+1can be
calculated recursively as follows:
^At+1=tX
k=0(sk) 
(sk) 
(sk+1)T
=t 1X
k=0(sk) 
(sk) 
(sk+1)T+(st) 
(st) 
(st+1)T
=^At+(st) 
(st) 
(st+1)T:
The above expression decomposes ^At+1into the sum of two matrices. Its inverse can be
calculated as [58]
^A 1
t+1=
^At+(st) 
(st) 
(st+1)T 1
=^A 1
t+^A 1
t(st) 
(st) 
(st+1)T^A 1
t
1 + 
(st) 
(st+1)T^A 1
t(st):
Therefore, we can directly store and update ^A 1
tto avoid the need to calculate the matrix
inverse. This recursive algorithm does not require a step size. However, it requires setting
the initial value of ^A 1
0. The initial value of such a recursive algorithm can be selected as
^A 1
0=I, whereis a positive number. A good tutorial on the recursive least-squares
approach can be found in [59].
178

## 第29页

8.3. TD learning of action values based on function approximation
8.3 TD learning of action values based on function
approximation
While Section 8.2 introduced the problem of state value estimation, the present section
introduces how to estimate action values . The tabular Sarsa and tabular Q-learning
algorithms are extended to the case of value function approximation. Readers will see
that the extension is straightforward.
8.3.1 Sarsa with function approximation
The Sarsa algorithm with function approximation can be readily obtained from (8.13)
by replacing the state values with action values. In particular, suppose that q(s;a) is
approximated by ^ q(s;a;w ). Replacing ^ v(s;w) in (8.13) by ^ q(s;a;w ) gives
wt+1=wt+th
rt+1+
^q(st+1;at+1;wt) ^q(st;at;wt)i
rw^q(st;at;wt): (8.35)
The analysis of (8.35) is similar to that of (8.13) and is omitted here. When linear
functions are used, we have
^q(s;a;w ) =T(s;a)w;
where(s;a) is a feature vector. In this case, rw^q(s;a;w ) =(s;a).
The value estimation step in (8.35) can be combined with a policy improvement step
to learn optimal policies. The procedure is summarized in Algorithm 8.2. It should be
noted that accurately estimating the action values of a given policy requires (8.35) to be
run suciently many times. However, (8.35) is executed only once before switching to the
policy improvement step. This is similar to the tabular Sarsa algorithm. Moreover, the
implementation in Algorithm 8.2 aims to solve the task of nding a good path to the target
state from a prespecied starting state. As a result, it cannot nd the optimal policy
for every state. However, if sucient experience data are available, the implementation
process can be easily adapted to nd optimal policies for every state.
An illustrative example is shown in Figure 8.9. In this example, the task is to nd a
good policy that can lead the agent to the target when starting from the top-left state.
Both the total reward and the length of each episode gradually converge to steady values.
In this example, the linear feature vector is selected as the Fourier function of order 5.
The expression of a Fourier feature vector is given in (8.18).
179

## 第30页

8.3. TD learning of action values based on function approximation
0 100 200 300 400 500-1000-5000Total reward
0 100 200 300 400 500
Episode index0500Episode length
1 2 3 4 5
1
2
3
4
5
Figure 8.9: Sarsa with linear function approximation. Here, 
= 0:9,= 0:1,rboundary =rforbidden =
 10,rtarget = 1, and= 0:001.
Algorithm 8.2: Sarsa with function approximation
Initialization: Initial parameter w0. Initial policy 0.t=>0for allt.2(0;1).
Goal: Learn an optimal policy that can lead the agent to the target state from an initial
states0.
For each episode, do
Generatea0ats0following0(s0)
Ifst(t= 0;1;2;::: ) is not the target state, do
Collect the experience sample (rt+1;st+1;at+1)given (st;at): generatert+1;st+1
by interacting with the environment; generate at+1followingt(st+1).
Update q-value:
wt+1=wt+th
rt+1+
^q(st+1;at+1;wt) ^q(st;at;wt)i
rw^q(st;at;wt)
Update policy:
t+1(ajst) = 1 
jA(st)j(jA(st)j 1)ifa= arg max a2A(st)^q(st;a;wt+1)
t+1(ajst) =
jA(st)jotherwise
st st+1,at at+1
8.3.2 Q-learning with function approximation
Tabular Q-learning can also be extended to the case of function approximation. The
update rule is
wt+1=wt+th
rt+1+
max
a2A(st+1)^q(st+1;a;wt) ^q(st;at;wt)i
rw^q(st;at;wt):(8.36)
The above update rule is similar to (8.35) except that ^ q(st+1;at+1;wt) in (8.35) is replaced
with max a2A(st+1)^q(st+1;a;wt).
Similar to the tabular case, (8.36) can be implemented in either an on-policy or
o-policy fashion. An on-policy version is given in Algorithm 8.3. An example for
demonstrating the on-policy version is shown in Figure 8.10. In this example, the task is
to nd a good policy that can lead the agent to the target state from the top-left state.
180

## 第31页

8.4. Deep Q-learning
Algorithm 8.3: Q-learning with function approximation (on-policy ver-
sion)
Initialization: Initial parameter w0. Initial policy 0.t=>0for allt.2(0;1).
Goal: Learn an optimal path that can lead the agent to the target state from an initial
states0.
For each episode, do
Ifst(t= 0;1;2;::: ) is not the target state, do
Collect the experience sample (at;rt+1;st+1)givenst: generate atfollowing
t(st); generatert+1;st+1by interacting with the environment.
Update q-value:
wt+1=wt+th
rt+1+
max
a2A(st+1)^q(st+1;a;wt) ^q(st;at;wt)i
rw^q(st;at;wt)
Update policy:
t+1(ajst) = 1 
jA(st)j(jA(st)j 1)ifa= arg max a2A(st)^q(st;a;wt+1)
t+1(ajst) =
jA(st)jotherwise
As can be seen, Q-learning with linear function approximation can successfully learn an
optimal policy. Here, linear Fourier basis functions of order ve are used. The o-policy
version will be demonstrated when we introduce deep Q-learning in Section 8.4.
0 100 200 300 400 500-4000-20000Total reward
0 100 200 300 400 500
Episode index01000Episode length
1 2 3 4 5
1
2
3
4
5
Figure 8.10: Q-learning with linear function approximation. Here, 
= 0:9,= 0:1,rboundary =
rforbidden = 10,rtarget = 1, and= 0:001.
One may notice in Algorithm 8.2 and Algorithm 8.3 that, although the values are
represented as functions, the policy (ajs) is still represented as a table. Thus, it still
assumes nite numbers of states and actions. In Chapter 9, we will see that the policies
can be represented as functions so that continuous state and action spaces can be handled.
8.4 Deep Q-learning
We can integrate deep neural networks into Q-learning to obtain an approach called
deep Q-learning ordeep Q-network (DQN) [22, 60, 61]. Deep Q-learning is one of the
181

## 第32页

8.4. Deep Q-learning
earliest and most successful deep reinforcement learning algorithms. Notably, the neural
networks do not have to be deep. For simple tasks such as our grid world examples,
shallow networks with one or two hidden layers may be sucient.
Deep Q-learning can be viewed as an extension of the algorithm in (8.36). However,
its mathematical formulation and implementation techniques are substantially dierent
and deserve special attention.
8.4.1 Algorithm description
Mathematically, deep Q-learning aims to minimize the following objective function:
J=E"
R+
max
a2A(S0)^q(S0;a;w ) ^q(S;A;w )2#
; (8.37)
where (S;A;R;S0) are random variables that denote a state, an action, the immediate
reward, and the next state, respectively. This objective function can be viewed as the
squared Bellman optimality error. That is because
q(s;a) =E
Rt+1+
max
a2A(St+1)q(St+1;a)St=s;At=a
;for alls;a
is the Bellman optimality equation (the proof is given in Box 7.5). Therefore, R+

maxa2A(S0)^q(S0;a;w ) ^q(S;A;w ) should equal zero in the expectation sense when
^q(S;A;w ) can accurately approximate the optimal action values.
To minimize the objective function in (8.37), we can use the gradient descent algorith-
m. To that end, we need to calculate the gradient of Jwith respect to w. It is noted that
the parameter wappears not only in ^ q(S;A;w ) but also in y:=R+
maxa2A(S0)^q(S0;a;w ).
As a result, it is nontrivial to calculate the gradient. For the sake of simplicity, it is as-
sumed that the value of winyis xed (for a short period of time) so that the calculation
of the gradient becomes much easier. In particular, we introduce two networks: one is a
main network representing ^ q(s;a;w ) and the other is a target network ^q(s;a;wT). The
objective function in this case becomes
J=E"
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )2#
;
wherewTis the target network's parameter. When wTis xed, the gradient of Jis
rwJ= E
R+
max
a2A(S0)^q(S0;a;wT) ^q(S;A;w )
rw^q(S;A;w )
; (8.38)
where some constant coecients are omitted without loss of generality.
To use the gradient in (8.38) to minimize the objective function, we need to pay
182

## 第33页

8.4. Deep Q-learning
attention to the following techniques.
The rst technique is to use two networks, a main network and a target network,
as mentioned when we calculate the gradient in (8.38). The implementation details
are explained below. Let wandwTdenote the parameters of the main and target
networks, respectively. They are initially set to the same value.
In every iteration, we draw a mini-batch of samples f(s;a;r;s0)gfrom the replay buer
(the replay buer will be explained soon). The inputs of the main network are sand
a. The output y= ^q(s;a;w ) is the estimated q-value. The target value of the output
isyT:=r+
maxa2A(s0)^q(s0;a;wT). The main network is updated to minimize the
TD error (also called the loss function)P(y yT)2over the samplesf(s;a;yT)g.
Updatingwin the main network does not explicitly use the gradient in (8.38). Instead,
it relies on the existing software tools for training neural networks. As a result, we
need a mini-batch of samples to train a network instead of using a single sample to
update the main network based on (8.38). This is one notable dierence between deep
and nondeep reinforcement learning algorithms.
The main network is updated in every iteration. By contrast, the target network is
set to be the same as the main network every certain number of iterations to satisfy
the assumption that wTis xed when calculating the gradient in (8.38).
The second technique is experience replay [22,60,62]. That is, after we have collected
some experience samples, we do not use these samples in the order they were collected.
Instead, we store them in a dataset called the replay buer . In particular, let ( s;a;r;s0)
be an experience sample and B:=f(s;a;r;s0)gbe the replay buer. Every time we
update the main network, we can draw a mini-batch of experience samples from the
replay buer. The draw of samples, or called experience replay , should follow a uniform
distribution .
Why is experience replay necessary in deep Q-learning, and why must the replay
follow a uniform distribution? The answer lies in the objective function in (8.37).
In particular, to well dene the objective function, we must specify the probability
distributions for S;A;R;S0. The distributions of RandS0are determined by the
system model once ( S;A) is given. The simplest way to describe the distribution of
the state-action pair ( S;A) is to assume it to be uniformly distributed.
However, the state-action samples may notbe uniformly distributed in practice s-
ince they are generated as a sample sequence according to the behavior policy. It is
necessary to break the correlation between the samples in the sequence to satisfy the
assumption of uniform distribution. To do this, we can use the experience replay tech-
nique by uniformly drawing samples from the replay buer. This is the mathematical
reason why experience replay is necessary and why experience replay must follow a
uniform distribution. A benet of random sampling is that each experience sample
183

## 第34页

8.4. Deep Q-learning
Algorithm 8.3: Deep Q-learning (o-policy version)
Initialization: A main network and a target network with the same initial parameter.
Goal: Learn an optimal target network to approximate the optimal action values from
the experience samples generated by a given behavior policy b.
Store the experience samples generated by bin a replay buerB=f(s;a;r;s0)g
For each iteration, do
Uniformly draw a mini-batch of samples from B
For each sample (s;a;r;s0), calculate the target value as yT=r+

maxa2A(s0)^q(s0;a;wT), wherewTis the parameter of the target network
Update the main network to minimize (yT ^q(s;a;w ))2using the mini-batch
of samples
SetwT=weveryCiterations
may be used multiple times, which can increase the data eciency. This is especially
important when we have a limited amount of data.
The implementation procedure of deep Q-learning is summarized in Algorithm 8.3.
This implementation is o-policy. It can also be adapted to become on-policy if needed.
8.4.2 Illustrative examples
An example is given in Figure 8.11 to demonstrate Algorithm 8.3. This example aims
to learn the optimal action values for every state-action pair. Once the optimal action
values are obtained, the optimal greedy policy can be obtained immediately.
A single episode is generated by the behavior policy shown in Figure 8.11(a). This
behavior policy is exploratory in the sense that it has the same probability of taking
any action at any state. The episode has only 1,000 steps as shown in Figure 8.11(b).
Although there are only 1,000 steps, almost all the state action pairs are visited in this
episode due to the strong exploration ability of the behavior policy. The replay buer is
a set of 1,000 experience samples. The mini-batch size is 100, meaning that we uniformly
draw 100 samples from the replay buer every time we acquire samples.
The main and target networks have the same structure: a neural network with one
hidden layer of 100 neurons (the numbers of layers and neurons can be tuned). The
neural network has three inputs and one output. The rst two inputs are the normalized
row and column indexes of a state. The third input is the normalized action index. Here,
\normalization" means converting a value to the interval of [0,1]. The output of the
network is the estimated value. The reason why we design the inputs as the row and
column of a state rather than a state index is that we know that a state corresponds to
a two-dimensional location in the grid. The more information about the state we use
when designing the network, the better the network can perform. Moreover, the neural
184

## 第35页

8.4. Deep Q-learning
1 2 3 4 5
1
2
3
4
5
(a) The behavior policy.
1 2 3 4 5
1
2
3
4
5
 (b) An episode with 1,000 steps.
1 2 3 4 5
1
2
3
4
5 (c) The nal learned policy.
02004006008001000
Iteration index012345TD error / loss function
(d) The loss function converges to zero.
02004006008001000
Iteration index0246810State value error (RMSE) (e) The value error converges to zero.
Figure 8.11: Optimal policy learning via deep Q-learning. Here, 
= 0:9,rboundary =rforbidden = 10,
andrtarget = 1. The batch size is 100.
network can also be designed in other ways. For example, it can have two inputs and
ve outputs, where the two inputs are the normalized row and column of a state and the
outputs are the ve estimated action values for the input state [22].
As shown in Figure 8.11(d), the loss function, dened as the average squared TD
error of each mini-batch, converges to zero, meaning that the network can t the training
samples well. As shown in Figure 8.11(e), the state value estimation error also converges
to zero, indicating that the estimates of the optimal action values become suciently
accurate. Then, the corresponding greedy policy is optimal.
This example demonstrates the high eciency of deep Q-learning. In particular, a
short episode of 1,000 steps is sucient for obtaining an optimal policy here. By contrast,
an episode with 100,000 steps is required by tabular Q-learning, as shown in Figure 7.4.
One reason for the high eciency is that the function approximation method has a strong
generalization ability. Another reason is that the experience samples can be repeatedly
used.
We next deliberately challenge the deep Q-learning algorithm by considering a scenario
with fewer experience samples. Figure 8.12 shows an example of an episode with merely
100 steps. In this example, although the network can still be well-trained in the sense
185

## 第36页

8.5. Summary
1 2 3 4 5
1
2
3
4
5
(a) The behavior policy.
1 2 3 4 5
1
2
3
4
5 (b) An episode with 100 steps.
1 2 3 4 5
1
2
3
4
5 (c) The nal learned policy.
02004006008001000
Iteration index01234567TD error / loss function
(d) The loss function converges to zero.
02004006008001000
Iteration index45678State value error (RMSE) (e) The value error does not converge to zero.
Figure 8.12: Optimal policy learning via deep Q-learning. Here, 
= 0:9,rboundary =rforbidden = 10,
andrtarget = 1. The batch size is 50.
that the loss function converges to zero, the state estimation error cannot converge to
zero. That means the network can properly t the given experience samples, but the
experience samples are too few to accurately estimate the optimal action values.
8.5 Summary
This chapter continued introducing TD learning algorithms. However, it switches from
the tabular method to the function approximation method. The key to understanding
the function approximation method is to know that it is an optimization problem. The
simplest objective function is the squared error between the true state values and the
estimated values. There are also other objective functions such as the Bellman error
and the projected Bellman error. We have shown that the TD-Linear algorithm actually
minimizes the projected Bellman error. Several optimization algorithms such as Sarsa
and Q-learning with value approximation have been introduced.
One reason why the value function approximation method is important is that it allows
articial neural networks to be integrated with reinforcement learning. For example,
deep Q-learning is one of the most successful deep reinforcement learning algorithms.
186

## 第37页

8.6. Q&A
Although neural networks have been widely used as nonlinear function approximators,
this chapter provides a comprehensive introduction to the linear function case. Fully
understanding the linear case is important for better understanding the nonlinear case.
Interested readers may refer to [63] for a thorough analysis of TD learning algorithms
with function approximation. A more theoretical discussion on deep Q-learning can be
found in [61].
An important concept named stationary distribution is introduced in this chapter.
The stationary distribution plays an important role in dening an appropriate objective
function in the value function approximation method. It also plays a key role in Chapter 9
when we use functions to approximate policies. An excellent introduction to this topic
can be found in [49, Chapter IV]. The contents of this chapter heavily rely on matrix
analysis. Some results are used without explanation. Excellent references regarding
matrix analysis and linear algebra can be found in [4,48].
8.6 Q&A
Q: What is the dierence between the tabular and function approximation methods?
A: One important dierence is how a value is updated and retrieved.
How to retrieve a value: When the values are represented by a table, if we would like
to retrieve a value, we can directly read the corresponding entry in the table. However,
when the values are represented by a function, we need to input the state index sinto
the function and calculate the function value. If the function is an articial neural
network, a forward prorogation process from the input to the output is needed.
How to update a value: When the values are represented by a table, if we would like
to update one value, we can directly rewrite the corresponding entry in the table.
However, when the values are represented by a function, we must update the function
parameter to change the values indirectly.
Q: What are the advantages of the function approximation method over the tabular
method?
A: Due to the way state values are retrieved, the function approximation method is
more ecient in storage. In particular, while the tabular method needs to store jSj
values, the function approximation method only needs to store a parameter vector
whose dimension is usually much less than jSj.
Due to the way in which state values are updated, the function approximation method
has another merit: its generalization ability is stronger than that of the tabular
method. The reason is as follows. With the tabular method, updating one state
value would not change the other state values. However, with the function approx-
imation method, updating the function parameter aects the values of many states.
187

## 第38页

8.6. Q&A
Therefore, the experience sample for one state can generalize to help estimate the
values of other states.
Q: Can we unify the tabular and the function approximation methods?
A: Yes. The tabular method can be viewed as a special case of the function approxi-
mation method. The related details can be found in Box 8.2.
Q: What is the stationary distribution and why is it important?
A: The stationary distribution describes the long-term behavior of a Markov decision
process. More specically, after the agent executes a given policy for a suciently long
period, the probability of the agent visiting a state can be described by this stationary
distribution. More information can be found in Box 8.1.
The reason why this concept emerges in this chapter is that it is necessary for dening
a valid objective function. In particular, the objective function involves the probability
distribution of the states, which is usually selected as the stationary distribution. The
stationary distribution is important not only for the value approximation method but
also for the policy gradient method, which will be introduced in Chapter 9.
Q: What are the advantages and disadvantages of the linear function approximation
method?
A: Linear function approximation is the simplest case whose theoretical properties
can be thoroughly analyzed. However, the approximation ability of this method is
limited. It is also nontrivial to select appropriate feature vectors for complex tasks.
By contrast, articial neural networks can be used to approximate values as black-box
universal nonlinear approximators, which are more friendly to use. Nevertheless, it
is still meaningful to study the linear case to better grasp the idea of the function
approximation method. Moreover, the linear case is powerful in the sense that the
tabular method can be viewed as a special linear case (Box 8.2).
Q: Why does deep Q-learning require experience replay?
A: The reason lies in the objective function in (8.37). In particular, to well dene
the objective function, we must specify the probability distributions of S;A;R;S0.
The distributions of RandS0are determined by the system model once ( S;A) is
given. The simplest way to describe the distribution of the state-action pair ( S;A)
is to assume it to be uniformly distributed. However, the state-action samples may
notbe uniformly distributed in practice since they are generated as a sequence by the
behavior policy. It is necessary to break the correlation between the samples in the
sequence to satisfy the assumption of uniform distribution. To do this, we can use
the experience replay technique by uniformly drawing samples from the replay buer.
A benet of experience replay is that each experience sample may be used multiple
times, which can increase the data eciency.
188

## 第39页

8.6. Q&A
Q: Can tabular Q-learning use experience replay?
A: Although tabular Q-learning does not require experience replay, it can also use
experience relay without encountering problems. That is because Q-learning has no
requirements about how the samples are obtained due to its o-policy attribute. One
benet of using experience replay is that the samples can be used repeatedly and
hence more eciently.
Q: Why does deep Q-learning require two networks?
A: The fundamental reason is to simplify the calculation of the gradient of (8.37).
Sincewappears not only in ^ q(S;A;w ) but also in R+
maxa2A(S0)^q(S0;a;w ), it is
nontrivial to calculate the gradient with respect to w. On the one hand, if we x
winR+
maxa2A(S0)^q(S0;a;w ), the gradient can be easily calculated as shown in
(8.38). This gradient suggests that two networks should be maintained. The main
network's parameter is updated in every iteration. The target network's parameter
is xed within a certain period. On the other hand, the target network's parameter
cannot be xed forever. It should be updated every certain number of iterations.
Q: When an articial neural network is used as a nonlinear function approximator,
how should we update its parameter?
A: It must be noted that we should not directly update the parameter vector by
using, for example, (8.36). Instead, we should follow the network training procedure
to update the parameter. This procedure can be realized based on neural network
training toolkits, which are currently mature and widely available.
189

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_Book-Mathematical-Foundation-of-Reinforcement-Learning-main_课程MOC|Book-Mathematical-Foundation-of-Reinforcement-Learning-main MOC]]
