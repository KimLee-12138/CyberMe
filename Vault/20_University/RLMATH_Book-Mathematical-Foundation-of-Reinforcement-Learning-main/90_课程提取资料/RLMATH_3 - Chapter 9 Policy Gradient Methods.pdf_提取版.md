---
id: extract-rlmath-60e866fe
type: extract
status: extracted
course: RLMATH
source:
  - "[[91_Raw-Archive/PDF/RLMATH_3 - Chapter 9 Policy Gradient Methods.pdf_课件_未知日期_60e866fe.pdf]]"
source_pages: all
source_hash: "60e866fe227389d33464268be6231b944273b3096b04069b924c601fbf75ca1d"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 3 - Chapter 9 Policy Gradient Methods.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

Chapter 9
Policy Gradient Methods
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
Figure 9.1: Where we are in this book.
The idea of function approximation can be applied not only to represent state/action
values, as introduced in Chapter 8, but also to represent policies, as introduced in this
chapter. So far in this book, policies have been represented by tables: the action prob-
abilities of all states are stored in a table (e.g., Table 9.1). In this chapter, we show
that policies can be represented by parameterized functions denoted as (ajs;), where
2Rmis a parameter vector. It can also be written in other forms such as (ajs),
(a;s), or(a;s; ).
When policies are represented as functions, optimal policies can be obtained by op-
timizing certain scalar metrics. Such a method is called policy gradient . The policy
191

## 第2页

9.1. Policy representation: From table to function
a1a2a3a4a5
s1(a1js1)(a2js1)(a3js1)(a4js1)(a5js1)
..................
s9(a1js9)(a2js9)(a3js9)(a4js9)(a5js9)
Table 9.1: A tabular representation of a policy. There are nine states and ve actions for each state.
θ
functions
aπ(a|s,θ)
(a)
θ
functionsπ(a1|s,θ)
π(a5|s,θ)... (b)
Figure 9.2: Function representations of policies. The functions may have dierent structures.
gradient method is a big step forward in this book because it is policy-based . By contrast,
all the previous chapters in this book discuss value-based methods. The advantages of the
policy gradient method are numerous. For example, it is more ecient for handling large
state/action spaces. It has stronger generalization abilities and hence is more ecient in
terms of sample usage.
9.1 Policy representation: From table to function
When the representation of a policy is switched from a table to a function, it is necessary
to clarify the dierence between the two representation methods.
First, how to dene optimal policies? When represented as a table, a policy is dened
as optimal if it can maximize every state value . When represented by a function, a
policy is dened as optimal if it can maximize certain scalar metrics .
Second, how to update a policy? When represented by a table, a policy can be updated
by directly changing the entries in the table. When represented by a parameterized
function, a policy can no longer be updated in this way. Instead, it can only be
updated by changing the parameter .
Third, how to retrieve the probability of an action? In the tabular case, the probability
of an action can be directly obtained by looking up the corresponding entry in the
table. In the case of function representation, we need to input ( s;a) into the function
to calculate its probability (see Figure 9.2(a)). Depending on the structure of the
function, we can also input a state and then output the probabilities of all actions
(see Figure 9.2(b)).
192

## 第3页

9.2. Metrics for dening optimal policies
The basic idea of the policy gradient method is summarized below. Suppose that J()
is a scalar metric. Optimal policies can be obtained by optimizing this metric via the
gradient-based algorithm:
t+1=t+rJ(t);
whererJis the gradient of Jwith respect to ,tis the time step, and is the
optimization rate.
With this basic idea, we will answer the following three questions in the remainder of
this chapter.
What metrics should be used? (Section 9.2).
How to calculate the gradients of the metrics? (Section 9.3)
How to use experience samples to calculate the gradients? (Section 9.4)
9.2 Metrics for dening optimal policies
If a policy is represented by a function, there are two types of metrics for dening optimal
policies. One is based on state values and the other is based on immediate rewards.
Metric 1: Average state value
The rst metric is the average state value or simply called the average value . It is dened
as
v=X
s2Sd(s)v(s);
whered(s) is the weight of state s. It satises d(s)0 for anys2SandP
s2Sd(s) = 1.
Therefore, we can interpret d(s) as a probability distribution of s. Then, the metric can
be written as
v=ESd[v(S)]:
How to select the distribution d? This is an important question. There are two cases.
The rst and simplest case is that disindependent of the policy . In this case, we
specically denote dasd0and vas v0
to indicate that the distribution is independent
of the policy. One case is to treat all the states equally important and select d0(s) =
1=jSj. Another case is when we are only interested in a specic state s0(e.g., the
agent always starts from s0). In this case, we can design
d0(s0) = 1; d 0(s6=s0) = 0:
193

## 第4页

9.2. Metrics for dening optimal policies
The second case is that disdependent on the policy . In this case, it is common to
selectdasd, which is the stationary distribution under. One basic property of d
is that it satises
dT
P=dT
;
wherePis the state transition probability matrix. More information about the
stationary distribution can be found in Box 8.1.
The interpretation of selecting dis as follows. The stationary distribution re
ects the
long-term behavior of a Markov decision process under a given policy. If one state is
frequently visited in the long term, it is more important and deserves a higher weight;
if a state is rarely visited, then its importance is low and deserves a lower weight.
As its name suggests,  vis a weighted average of the state values. Dierent values
oflead to dierent values of  v. Our ultimate goal is to nd an optimal policy (or
equivalently an optimal ) to maximize  v.
We next introduce another two important equivalent expressions of  v.
Suppose that an agent collects rewards fRt+1g1
t=0by following a given policy ().
Readers may often see the following metric in the literature:
J() = lim
n!1E"nX
t=0
tRt+1#
=E"1X
t=0
tRt+1#
: (9.1)
This metric may be nontrivial to interpret at rst glance. In fact, it is equal to  v.
To see that, we have
E"1X
t=0
tRt+1#
=X
s2Sd(s)E"1X
t=0
tRt+1jS0=s#
=X
s2Sd(s)v(s)
= v:
The rst equality in the above equation is due to the law of total expectation. The
second equality is by the denition of state values.
The metric  vcan also be rewritten as the inner product of two vectors. In particular,
let
v= [:::;v(s);:::]T2RjSj;
d= [:::;d (s);:::]T2RjSj:
194

## 第5页

9.2. Metrics for dening optimal policies
Then, we have
v=dTv:
This expression will be useful when we analyze its gradient.
Metric 2: Average reward
The second metric is the average one-step reward or simply called the average reward
[2,64,65]. In particular, it is dened as
r:=X
s2Sd(s)r(s)
=ESd[r(S)]; (9.2)
wheredis the stationary distribution and
r(s):=X
a2A(ajs;)r(s;a) =EA(s;)[r(s;A)js] (9.3)
is the expectation of the immediate rewards. Here, r(s;a):=E[Rjs;a] =P
rrp(rjs;a).
We next present another two important equivalent expressions of  r.
Suppose that the agent collects rewards fRt+1g1
t=0by following a given policy ().
A common metric that readers may often see in the literature is
J() = lim
n!11
nE"n 1X
t=0Rt+1#
: (9.4)
It may seem nontrivial to interpret this metric at rst glance. In fact, it is equal to
r:
lim
n!11
nE"n 1X
t=0Rt+1#
=X
s2Sd(s)r(s) = r: (9.5)
The proof of (9.5) is given in Box 9.1.
The average reward  rin (9.2) can also be written as the inner product of two vectors.
In particular, let
r= [:::;r(s);:::]T2RjSj;
d= [:::;d(s);:::]T2RjSj;
195

## 第6页

9.2. Metrics for dening optimal policies
wherer(s) is dened in (9.3). Then, it is clear that
r=X
s2Sd(s)r(s) =dT
r:
This expression will be useful when we derive its gradient.
Box 9.1: Proof of (9.5)
Step 1: We rst prove that the following equation is valid for any starting state
s02S:
r= lim
n!11
nE"n 1X
t=0Rt+1jS0=s0#
: (9.6)
To do that, we notice
lim
n!11
nE"n 1X
t=0Rt+1jS0=s0#
= lim
n!11
nn 1X
t=0E[Rt+1jS0=s0]
= lim
t!1E[Rt+1jS0=s0]; (9.7)
where the last equality is due to the property of the Cesaro mean (also called the
Cesaro summation). In particular, if fakg1
k=1is a convergent sequence such that
limk!1akexists, thenf1=nPn
k=1akg1
n=1is also a convergent sequence such that
limn!11=nPn
k=1ak= limk!1ak.
We next examine E[Rt+1jS0=s0] in (9.7) more closely. By the law of total
expectation, we have
E[Rt+1jS0=s0] =X
s2SE[Rt+1jSt=s;S 0=s0]p(t)(sjs0)
=X
s2SE[Rt+1jSt=s]p(t)(sjs0)
=X
s2Sr(s)p(t)(sjs0);
wherep(t)(sjs0) denotes the probability of transitioning from s0tosusing exactly t
steps. The second equality in the above equation is due to the Markov memoryless
property: the reward obtained at the next time step depends only on the current
state rather than the previous ones.
Note that
lim
t!1p(t)(sjs0) =d(s)
196

## 第7页

9.2. Metrics for dening optimal policies
by the denition of the stationary distribution. As a result, the starting state s0does
not matter. Then, we have
lim
t!1E[Rt+1jS0=s0] = lim
t!1X
s2Sr(s)p(t)(sjs0) =X
s2Sr(s)d(s) = r:
Substituting the above equation into (9.7) gives (9.6).
Step 2: Consider an arbitrary state distribution d. By the law of total expectation,
we have
lim
n!11
nE"n 1X
t=0Rt+1#
= lim
n!11
nX
s2Sd(s)E"n 1X
t=0Rt+1jS0=s#
=X
s2Sd(s) lim
n!11
nE"n 1X
t=0Rt+1jS0=s#
:
Since (9.6) is valid for any starting state, substituting (9.6) into the above equation
yields
lim
n!11
nE"n 1X
t=0Rt+1#
=X
s2Sd(s)r= r:
The proof is complete.
Some remarks
Metric Expression 1 Expression 2 Expression 3
vX
s2Sd(s)v(s)ESd[v(S)] lim
n!1EnX
t=0
tRt+1
rX
s2Sd(s)r(s)ESd[r(S)]lim
n!11
nEn 1X
t=0Rt+1
Table 9.2: Summary of the dierent but equivalent expressions of  vand r.
Up to now, we have introduced two types of metrics:  vand r. Each metric has
several dierent but equivalent expressions. They are summarized in Table 9.2. We
sometimes use  vto specically refer to the case where the state distribution is the
stationary distribution dand use v0
to refer to the case where d0is independent of .
Some remarks about the metrics are given below.
All these metrics are functions of . Sinceis parameterized by , these metrics
are functions of . In other words, dierent values of can generate dierent metric
197

## 第8页

9.3. Gradients of the metrics
values. Therefore, we can search for the optimal values of to maximize these metrics.
This is the basic idea of policy gradient methods.
The two metrics  vand rare equivalent in the discounted case where 
 < 1. In
particular, it can be shown that
r= (1 
)v:
The above equation indicates that these two metrics can be simultaneously maximized.
The proof of this equation is given later in Lemma 9.1.
9.3 Gradients of the metrics
Given the metrics introduced in the last section, we can use gradient-based methods to
maximize them. To do that, we need to rst calculate the gradients of these metrics.
The most important theoretical result in this chapter is the following theorem.
Theorem 9.1 (Policy gradient theorem) .The gradient of J()is
rJ() =X
s2S(s)X
a2Ar(ajs;)q(s;a); (9.8)
whereis a state distribution and ris the gradient of with respect to . Moreover,
(9.8) has a compact form expressed in terms of expectation:
rJ() =ES;A(S;)h
rln(AjS;)q(S;A)i
; (9.9)
where lnis the natural logarithm.
Some important remarks about Theorem 9.1 are given below.
It should be noted that Theorem 9.1 is a summary of the results in Theorem 9.2,
Theorem 9.3, and Theorem 9.5. These three theorems address dierent scenarios
involving dierent metrics and discounted/undiscounted cases. The gradients in these
scenarios all have similar expressions and hence are summarized in Theorem 9.1. The
specic expressions of J() andare not given in Theorem 9.1 and can be found in
Theorem 9.2, Theorem 9.3, and Theorem 9.5. In particular, J() could be  v0
, v,
or r. The equality in (9.8) may become a strict equality or an approximation. The
distribution also varies in dierent scenarios.
The derivation of the gradients is the most complicated part of the policy gradient
method. For many readers, it is sucient to be familiar with the result in Theorem 9.1
without knowing the proof. The derivation details presented in the rest of this section
are mathematically intensive. Readers are suggested to study selectively based on
their interests.
198

## 第9页

9.3. Gradients of the metrics
The expression in (9.9) is more favorable than (9.8) because it is expressed as an
expectation. We will show in Section 9.4 that this true gradient can be approximated
by a stochastic gradient.
Why can (9.8) be expressed as (9.9)? The proof is given below. By the denition of
expectation, (9.8) can be rewritten as
rJ() =X
s2S(s)X
a2Ar(ajs;)q(s;a)
=ES"X
a2Ar(ajS;)q(S;a)#
: (9.10)
Furthermore, the gradient of ln (ajs;) is
rln(ajs;) =r(ajs;)
(ajs;):
It follows that
r(ajs;) =(ajs;)rln(ajs;): (9.11)
Substituting (9.11) into (9.10) gives
rJ() =E"X
a2A(ajS;)rln(ajS;)q(S;a)#
=ES;A(S;)h
rln(AjS;)q(S;A)i
:
It is notable that (ajs;) must be positive for all (s;a) to ensure that ln (ajs;) is
valid. This can be achieved by using softmax functions :
(ajs;) =eh(s;a;)
P
a02Aeh(s;a0;); a2A; (9.12)
whereh(s;a; ) is a function indicating the preference for selecting aats. The policy
in (9.12) satises (ajs;)2(0;1) andP
a2A(ajs;) = 1 for any s2S. This policy
can be realized by a neural network. The input of the network is s. The output layer
is a softmax layer so that the network outputs (ajs;) for allaand the sum of the
outputs is equal to 1. See Figure 9.2(b) for an illustration.
Since(ajs;)>0 for alla, the policy is stochastic and hence exploratory . The policy
does not directly tell which action to take. Instead, the action should be generated
according to the probability distribution of the policy.
199

## 第10页

9.3. Gradients of the metrics
9.3.1 Derivation of the gradients in the discounted case
We next derive the gradients of the metrics in the discounted case where 
2(0;1). The
state value and action value in the discounted case are dened as
v(s) =E[Rt+1+
Rt+2+
2Rt+3+:::jSt=s];
q(s;a) =E[Rt+1+
Rt+2+
2Rt+3+:::jSt=s;At=a]:
It holds that v(s) =P
a2A(ajs;)q(s;a) and the state value satises the Bellman
equation.
First, we show that  v() and r() are equivalent metrics.
Lemma 9.1 (Equivalence between  v() and r()).In the discounted case where 
2
(0;1), it holds that
r= (1 
)v: (9.13)
Proof. Note that v() =dT
vand r() =dT
r, wherevandrsatisfy the Bellman
equationv=r+
Pv. Multiplying dT
on both sides of the Bellman equation yields
v= r+
dT
Pv= r+
dT
v= r+
v;
which implies (9.13).
Second, the following lemma gives the gradient of v(s) for anys.
Lemma 9.2 (Gradient of v(s)).In the discounted case, it holds for any s2S that
rv(s) =X
s02SPr(s0js)X
a2Ar(ajs0;)q(s0;a); (9.14)
where
Pr(s0js):=1X
k=0
k[Pk
]ss0=
(In 
P) 1
ss0
is the discounted total probability of transitioning from stos0under policy . Here,
[]ss0denotes the entry in the sth row and s0th column, and [Pk
]ss0is the probability of
transitioning from stos0using exactly ksteps under .
200

## 第11页

9.3. Gradients of the metrics
Box 9.2: Proof of Lemma 9.2
First, for any s2S, it holds that
rv(s) =r"X
a2A(ajs;)q(s;a)#
=X
a2A[r(ajs;)q(s;a) +(ajs;)rq(s;a)]; (9.15)
whereq(s;a) is the action value given by
q(s;a) =r(s;a) +
X
s02Sp(s0js;a)v(s0):
Sincer(s;a) =P
rrp(rjs;a) is independent of , we have
rq(s;a) = 0 +
X
s02Sp(s0js;a)rv(s0):
Substituting this result into (9.15) yields
rv(s) =X
a2A"
r(ajs;)q(s;a) +(ajs;)
X
s02Sp(s0js;a)rv(s0)#
=X
a2Ar(ajs;)q(s;a) +
X
a2A(ajs;)X
s02Sp(s0js;a)rv(s0):(9.16)
It is notable that rvappears on both sides of the above equation. One way to
calculate it is to use the unrolling technique [64]. Here, we use another way based on
thematrix-vector form , which we believe is more straightforward to understand. In
particular, let
u(s):=X
a2Ar(ajs;)q(s;a):
Since
X
a2A(ajs;)X
s02Sp(s0js;a)rv(s0) =X
s02Sp(s0js)rv(s0) =X
s02S[P]ss0rv(s0);
equation (9.16) can be written in matrix-vector form as
2
664...
rv(s)
...3
775
|{z}
rv2Rmn=2
664...
u(s)
...3
775
|{z}
u2Rmn+
(P
Im)2
664...
rv(s0)
...3
775
|{z}
rv2Rmn;
201

## 第12页

9.3. Gradients of the metrics
which can be written concisely as
rv=u+
(P
Im)rv:
Here,n=jSj, andmis the dimension of the parameter vector . The reason that
the Kronecker product 
emerges in the equation is that rv(s) is a vector. The
above equation is a linear equation of rv, which can be solved as
rv= (Inm 
P
Im) 1u
= (In
Im 
P
Im) 1u
=
(In 
P) 1
Im
u: (9.17)
For any state s, it follows from (9.17) that
rv(s) =X
s02S
(In 
P) 1
ss0u(s0)
=X
s02S
(In 
P) 1
ss0X
a2Ar(ajs0;)q(s0;a): (9.18)
The quantity [( In 
P) 1]ss0has a clear probabilistic interpretation. In particular,
since (In 
P) 1=I+
P+
2P2
+, we have

(In 
P) 1
ss0= [I]ss0+
[P]ss0+
2[P2
]ss0+=1X
k=0
k[Pk
]ss0:
Note that [ Pk
]ss0is the probability of transitioning from stos0using exactly k
steps (see Box 8.1). Therefore, [( In 
P) 1]ss0is the discounted total probability of
transitioning from stos0using any number of steps. By denoting [( In 
P) 1]ss0:=
Pr(s0js), equation (9.18) becomes (9.14).
With the results in Lemma 9.2, we are ready to derive the gradient of  v0
.
Theorem 9.2 (Gradient of  v0
in the discounted case) .In the discounted case where

2(0;1), the gradient of v0
=dT
0vis
rv0
=E
rln(AjS;)q(S;A)
;
whereSandA(S;). Here, the state distribution is
(s) =X
s02Sd0(s0)Pr(sjs0); s2S; (9.19)
where Pr(sjs0) =P1
k=0
k[Pk
]s0s= [(I 
P) 1]s0sis the discounted total probability of
202

## 第13页

9.3. Gradients of the metrics
transitioning from s0tosunder policy .
Box 9.3: Proof of Theorem 9.2
Sinced0(s) is independent of , we have
rv0
=rX
s2Sd0(s)v(s) =X
s2Sd0(s)rv(s):
Substituting the expression of rv(s) given in Lemma 9.2 into the above equation
yields
rv0
=X
s2Sd0(s)rv(s) =X
s2Sd0(s)X
s02SPr(s0js)X
a2Ar(ajs0;)q(s0;a)
=X
s02S X
s2Sd0(s)Pr(s0js)!X
a2Ar(ajs0;)q(s0;a)
:=X
s02S(s0)X
a2Ar(ajs0;)q(s0;a)
=X
s2S(s)X
a2Ar(ajs;)q(s;a) (change s0tos)
=X
s2S(s)X
a2A(ajs;)rln(ajs;)q(s;a)
=E[rln(AjS;)q(S;A)];
whereSandA(S;). The proof is complete.
With Lemma 9.1 and Lemma 9.2, we can derive the gradients of  rand v.
Theorem 9.3 (Gradients of  rand vin the discounted case) .In the discounted case
where
2(0;1), the gradients of randvare
rr= (1 
)rvX
s2Sd(s)X
a2Ar(ajs;)q(s;a)
=E
rln(AjS;)q(S;A)
;
whereSdandA(S;). Here, the approximation is more accurate when 
is
closer to 1.
203

## 第14页

9.3. Gradients of the metrics
Box 9.4: Proof of Theorem 9.3
It follows from the denition of  vthat
rv=rX
s2Sd(s)v(s)
=X
s2Srd(s)v(s) +X
s2Sd(s)rv(s): (9.20)
This equation contains two terms. On the one hand, substituting the expression of
rvgiven in (9.17) into the second term gives
X
s2Sd(s)rv(s) = (dT

Im)rv
= (dT

Im)
(In 
P) 1
Im
u
=
dT
(In 
P) 1

Imu: (9.21)
It is noted that
dT
(In 
P) 1=1
1 
dT
;
which can be easily veried by multiplying ( In 
P) on both sides of the equation.
Therefore, (9.21) becomes
X
s2Sd(s)rv(s) =1
1 
dT

Imu
=1
1 
X
s2Sd(s)X
a2Ar(ajs;)q(s;a):
On the other hand, the rst term of (9.20) involves rd. However, since the second
term contains1
1 
, the second term becomes dominant, and the rst term becomes
negligible when 
!1. Therefore,
rv1
1 
X
s2Sd(s)X
a2Ar(ajs;)q(s;a):
Furthermore, it follows from  r= (1 
)vthat
rr= (1 
)rvX
s2Sd(s)X
a2Ar(ajs;)q(s;a)
=X
s2Sd(s)X
a2A(ajs;)rln(ajs;)q(s;a)
=E[rln(AjS;)q(S;A)]:
204

## 第15页

9.3. Gradients of the metrics
The approximation in the above equation requires that the rst term does not go to
innity when 
!1. More information can be found in [66, Section 4].
9.3.2 Derivation of the gradients in the undiscounted case
We next show how to calculate the gradients of the metrics in the undiscounted case
where
= 1. Readers may wonder why we suddenly start considering the undiscounted
case while we have only considered the discounted case so far in this book. In fact, the
denition of the average reward  ris valid for both discounted and undiscounted cases.
While the gradient of  rin the discounted case is an approximation, we will see that its
gradient in the undiscounted case is more elegant.
State values and the Poisson equation
In the undiscounted case, it is necessary to redene state and action values. Since the
undiscounted sum of the rewards, E[Rt+1+Rt+2+Rt+3+:::jSt=s], may diverge, the
state and action values are dened in a special way [64]:
v(s):=E[(Rt+1 r) + (Rt+2 r) + (Rt+3 r) +:::jSt=s];
q(s;a):=E[(Rt+1 r) + (Rt+2 r) + (Rt+3 r) +:::jSt=s;At=a];
where ris the average reward, which is determined when is given. There are dierent
names for v(s) in the literature such as the dierential reward [65] or bias [2, Sec-
tion 8.2.1]. It can be veried that the state value dened above satises the following
Bellman-like equation:
v(s) =X
a(ajs;)"X
rp(rjs;a)(r r) +X
s0p(s0js;a)v(s0)#
: (9.22)
Sincev(s) =P
a2A(ajs;)q(s;a), it holds that q(s;a) =P
rp(rjs;a)(r r) +P
s0p(s0js;a)v(s0). The matrix-vector form of (9.22) is
v=r r1n+Pv; (9.23)
where 1n= [1;:::; 1]T2Rn. Equation (9.23) is similar to the Bellman equation and it
has a specic name called the Poisson equation [65,67].
How to solve vfrom the Poisson equation? The answer is given in the following
theorem.
205

## 第16页

9.3. Gradients of the metrics
Theorem 9.4 (Solution of the Poisson equation) .Let
v
= (In P+1ndT
) 1r: (9.24)
Then,v
is a solution of the Poisson equation in (9.23) . Moreover, any solution of the
Poisson equation has the following form:
v=v
+c1n;
wherec2R.
This theorem indicates that the solution of the Poisson equation may not be unique.
Box 9.5: Proof of Theorem 9.4
We prove using three steps.
Step 1: Show that v
in (9.24) is a solution of the Poisson equation.
For the sake of simplicity, let
A:=In P+1ndT
:
Then,v
=A 1r. The fact that Ais invertible will be proven in Step 3. Substi-
tutingv
=A 1rinto (9.23) gives
A 1r=r 1ndT
r+PA 1r:
This equation is valid as proven below. Recognizing this equation gives (  A 1+
In 1ndT
+PA 1)r= 0, and consequently,
( In+A 1ndT
A+P)A 1r= 0:
The term in the brackets in the above equation is zero because  In+A 1ndT
A+
P= In+ (In P+1ndT
) 1ndT
(In P+1ndT
) +P= 0. Therefore, v
in
(9.24) is a solution.
Step 2: General expression of the solutions.
Substituting  r=dT
rinto (9.23) gives
v=r 1ndT
r+Pv (9.25)
and consequently
(In P)v= (In 1ndT
)r: (9.26)
206

## 第17页

9.3. Gradients of the metrics
It is noted that In Pis singular because ( In P)1n= 0 for any . Therefore,
the solution of (9.26) is not unique: if v
is a solution, then v
+xis also a solution
for anyx2Null(In P). WhenPis irreducible, Null( In P) = spanf1ng.
Then, any solution of the Poisson equation has the expression v
+c1nwhere
c2R.
Step 3: Show that A=In P+1ndT
is invertible.
Sincev
involvesA 1, it is necessary to show that Ais invertible. The analysis is
summarized in the following lemma.
Lemma 9.3. The matrix In P+1ndT
is invertible and its inverse is

In (P 1ndT
) 1=1X
k=1(Pk
 1ndT
) +In:
Proof. First of all, we state some preliminary facts without proof. Let (M)
be the spectral radius of a matrix M. Then,I Mis invertible if (M)<1.
Moreover,(M)<1 if and only if lim k!1Mk= 0.
Based on the above facts, we next show that lim k!1(P 1ndT
)k!0, and then
the invertibility of In (P 1ndT
) immediately follows. To do that, we notice
that
(P 1ndT
)k=Pk
 1ndT
; k1; (9.27)
which can be proven by induction. For instance, when k= 1, the equation is
valid. When k= 2, we have
(P 1ndT
)2= (P 1ndT
)(P 1ndT
)
=P2
 P1ndT
 1ndT
P+1ndT
1ndT

=P2
 1ndT
;
where the last equality is due to P1n=1n,dT
P=dT
, anddT
1n= 1. The case
ofk3 can be proven similarly.
Sincedis the stationary distribution of the state, it holds that lim k!1Pk
=1ndT

(see Box 8.1). Therefore, (9.27) implies that
lim
k!1(P 1ndT
)k= lim
k!1Pk
 1ndT
= 0:
As a result, (P 1ndT
)<1 and hence In (P 1ndT
) is invertible. Furthermore,
207

## 第18页

9.3. Gradients of the metrics
the inverse of this matrix is given by
(In (P 1ndT
)) 1=1X
k=0(P 1ndT
)k
=In+1X
k=1(P 1ndT
)k
=In+1X
k=1(Pk
 1ndT
)
=1X
k=0(Pk
 1ndT
) +1ndT
:
The proof is complete.
The proof of Lemma 9.3 is inspired by [66]. However, the result ( In P+
1ndT
) 1=P1
k=0(Pk
 1ndT
) given in [66] (the statement above equation (16)
in [66]) is inaccurate becauseP1
k=0(Pk
 1ndT
) is singular sinceP1
k=0(Pk
 
1ndT
)1n= 0. Lemma 9.3 corrects this inaccuracy.
Derivation of gradients
Although the value of vis not unique in the undiscounted case, as shown in Theorem 9.4,
the value of  ris unique. In particular, it follows from the Poisson equation that
r1n=r+ (P In)v
=r+ (P In)(v
+c1n)
=r+ (P In)v
:
Notably, the undetermined value cis canceled and hence  ris unique. Therefore, we
can calculate the gradient of  rin the undiscounted case. In addition, since vis not
unique, vis not unique either. We do not study the gradient of  vin the undiscounted
case. For interested readers, it is worth mentioning that we can add more constraints to
uniquely solve vfrom the Poisson equation. For example, by assuming that a recurrent
state exists, the state value of this recurrent state can be determined [65, Section II], and
henceccan be determined. There are also other ways to uniquely determine v. See, for
example, equations (8.6.5)-(8.6.7) in [2].
The gradient of  rin the undiscounted case is given below.
Theorem 9.5 (Gradient of  rin the undiscounted case) .In the undiscounted case, the
208

## 第19页

9.3. Gradients of the metrics
gradient of the average reward ris
rr=X
s2Sd(s)X
a2Ar(ajs;)q(s;a)
=E
rln(AjS;)q(S;A)
; (9.28)
whereSdandA(S;).
Compared to the discounted case shown in Theorem 9.3, the gradient of  rin the
undiscounted case is more elegant in the sense that (9.28) is strictly valid and Sobeys
the stationary distribution.
Box 9.6: Proof of Theorem 9.5
First of all, it follows from v(s) =P
a2A(ajs;)q(s;a) that
rv(s) =r"X
a2A(ajs;)q(s;a)#
=X
a2A[r(ajs;)q(s;a) +(ajs;)rq(s;a)]; (9.29)
whereq(s;a) is the action value satisfying
q(s;a) =X
rp(rjs;a)(r r) +X
s0p(s0js;a)v(s0)
=r(s;a) r+X
s0p(s0js;a)v(s0):
Sincer(s;a) =P
rrp(rjs;a) is independent of , we have
rq(s;a) = 0 rr+X
s02Sp(s0js;a)rv(s0):
Substituting this result into (9.29) yields
rv(s) =X
a2A"
r(ajs;)q(s;a) +(ajs;) 
 rr+X
s02Sp(s0js;a)rv(s0)!#
=X
a2Ar(ajs;)q(s;a) rr+X
a2A(ajs;)X
s02Sp(s0js;a)rv(s0):
(9.30)
Let
u(s):=X
a2Ar(ajs;)q(s;a):
209

## 第20页

9.4. Monte Carlo policy gradient (REINFORCE)
SinceP
a2A(ajs;)P
s02Sp(s0js;a)rv(s0) =P
s02Sp(s0js)rv(s0), equation
(9.30) can be written in matrix-vector form as
2
664...
rv(s)
...3
775
|{z}
rv2Rmn=2
664...
u(s)
...3
775
|{z}
u2Rmn 1n
rr+ (P
Im)2
664...
rv(s0)
...3
775
|{z}
rv2Rmn;
wheren=jSj,mis the dimension of , and
is the Kronecker product. The above
equation can be written concisely as
rv=u 1n
rr+ (P
Im)rv;
and hence
1n
rr=u+ (P
Im)rv rv:
Multiplying dT

Imon both sides of the above equation gives
(dT
1n)
rr=dT

Imu+ (dT
P)
Imrv dT

Imrv
=dT

Imu;
which implies
rr=dT

Imu
=X
s2Sd(s)u(s)
=X
s2Sd(s)X
a2Ar(ajs;)q(s;a):
9.4 Monte Carlo policy gradient (REINFORCE)
With the gradient presented in Theorem 9.1, we next show how to use the gradient-based
method to optimize the metrics to obtain optimal policies.
The gradient-ascent algorithm for maximizing J() is
t+1=t+rJ(t)
=t+Eh
rln(AjS;t)q(S;A)i
; (9.31)
where>0 is a constant learning rate. Since the true gradient in (9.31) is unknown, we
210

## 第21页

9.4. Monte Carlo policy gradient (REINFORCE)
can replace the true gradient with a stochastic gradient to obtain the following algorithm:
t+1=t+rln(atjst;t)qt(st;at); (9.32)
whereqt(st;at) is an approximation of q(st;at). Ifqt(st;at) is obtained by Monte Carlo
estimation, the algorithm is called REINFORCE [68] or Monte Carlo policy gradient ,
which is one of earliest and simplest policy gradient algorithms.
The algorithm in (9.32) is important since many other policy gradient algorithms can
be obtained by extending it. We next examine the interpretation of (9.32) more closely.
Sincerln(atjst;t) =r(atjst;t)
(atjst;t);we can rewrite (9.32) as
t+1=t+qt(st;at)
(atjst;t)
|{z}
tr(atjst;t);
which can be further written concisely as
t+1=t+tr(atjst;t): (9.33)
Two important interpretations can be seen from this equation.
First, since (9.33) is a simple gradient-ascent algorithm, the following observations
can be obtained.
- Ift0, the probability of choosing ( st;at) is enhanced. That is
(atjst;t+1)(atjst;t):
The greater tis, the stronger the enhancement is.
- Ift<0, the probability of choosing ( st;at) decreases. That is
(atjst;t+1)<(atjst;t):
The above observations can be proven as follows. When t+1 tis suciently small,
it follows from the Taylor expansion that
(atjst;t+1)(atjst;t) + (r(atjst;t))T(t+1 t)
=(atjst;t) +t(r(atjst;t))T(r(atjst;t)) (substituting (9.33))
=(atjst;t) +tkr(atjst;t)k2
2:
It is clear that (atjst;t+1)(atjst;t) whent0 and(atjst;t+1)<(atjst;t)
whent<0.
Second, the algorithm can strike a balance between exploration and exploitation to a
211

## 第22页

9.4. Monte Carlo policy gradient (REINFORCE)
Algorithm 9.1: Policy Gradient by Monte Carlo (REINFORCE)
Initialization: Initial parameter ;
2(0;1);>0.
Goal: Learn an optimal policy for maximizing J().
For each episode, do
Generate an episode fs0;a0;r1;:::;sT 1;aT 1;rTgfollowing().
Fort= 0;1;:::;T 1:
Value update: qt(st;at) =PT
k=t+1
k t 1rk
Policy update:  +rln(atjst;)qt(st;at)
certain extent due to the expression of
t=qt(st;at)
(atjst;t):
On the one hand, tisproportional toqt(st;at). As a result, if the action value of
(st;at) is large, then (atjst;t) is enhanced so that the probability of selecting at
increases. Therefore, the algorithm attempts to exploit actions with greater values.
One the other hand, tisinversely proportional to(atjst;t) whenqt(st;at)>0. As
a result, if the probability of selecting atis small, then (atjst;t) is enhanced so that
the probability of selecting atincreases. Therefore, the algorithm attempts to explore
actions with low probabilities.
Moreover, since (9.32) uses samples to approximate the true gradient in (9.31), it is
important to understand how the samples should be obtained.
How to sample S?Sin the true gradient E[rln(AjS;t)q(S;A)] should obey the
distribution which is either the stationary distribution dor the discounted total
probability distribution in (9.19). Either dorrepresents the long-term behavior
exhibited under .
How to sample A?AinE[rln(AjS;t)q(S;A)] should obey the distribution of
(AjS;). The ideal way to sample Ais to select atfollowing(ajst;t). Therefore,
the policy gradient algorithm is on-policy.
Unfortunately, the ideal ways for sampling SandAare not strictly followed in practice
due to their low eciency of sample usage. A more sample-ecient implementation of
(9.32) is given in Algorithm 9.1. In this implementation, an episode is rst generated by
following(). Then,is updated multiple times using every experience sample in the
episode.
212

## 第23页

9.5. Summary
9.5 Summary
This chapter introduced the policy gradient method, which is the foundation of many
modern reinforcement learning algorithms. Policy gradient methods are policy-based . It
is a big step forward in this book because all the methods in the previous chapters are
value-based . The basic idea of the policy gradient method is simple. That is to select an
appropriate scalar metric and then optimize it via a gradient-ascent algorithm.
The most complicated part of the policy gradient method is the derivation of the
gradients of the metrics. That is because we have to distinguish various scenarios with
dierent metrics and discounted/undiscounted cases. Fortunately, the expressions of the
gradients in dierent scenarios are similar. Hence, we summarized the expressions in
Theorem 9.1, which is the most important theoretical result in this chapter. For many
readers, it is sucient to be aware of this theorem. Its proof is nontrivial, and it is not
required for all readers to study.
The policy gradient algorithm in (9.32) must be properly understood since it is the
foundation of many advanced policy gradient algorithms. In the next chapter, this algo-
rithm will be extended to another important policy gradient method called actor-critic.
9.6 Q&A
Q: What is the basic idea of the policy gradient method?
A: The basic idea is simple. That is to dene an appropriate scalar metric, derive
its gradient, and then use gradient-ascent methods to optimize the metric. The most
important theoretical result regarding this method is the policy gradient given in
Theorem 9.1.
Q: What is the most complicated part of the policy gradient method?
A: The basic idea of the policy gradient method is simple. However, the derivation
procedure of the gradients is quite complicated. That is because we have to distin-
guish numerous dierent scenarios. The mathematical derivation procedure in each
scenario is nontrivial. It is sucient for many readers to be familiar with the result
in Theorem 9.1 without knowing the proof.
Q: What metrics should be used in the policy gradient method?
A: We introduced three common metrics in this chapter:  v, v0
, and r. Since they
all lead to similar policy gradients, they all can be adopted in the policy gradient
method. More importantly, the expressions in (9.1) and (9.4) are often encountered
in the literature.
Q: Why is a natural logarithm function contained in the policy gradient?
213

## 第24页

9.6. Q&A
A: A natural logarithm function is introduced to express the gradient as an expected
value. In this way, we can approximate the true gradient with a stochastic one.
Q: Why do we need to study undiscounted cases when deriving the policy gradient?
A: The denition of the average reward  ris valid for both discounted and undis-
counted cases. While the gradient of  rin the discounted case is an approximation,
its gradient in the undiscounted case is more elegant.
Q: What does the policy gradient algorithm in (9.32) do mathematically?
A: To better understand this algorithm, readers are recommended to examine its
concise expression in (9.33), which clearly shows that it is a gradient-ascent algorithm
for updating the value of (atjst;t). That is, when a sample ( st;at) is available, the
policy can be updated so that (atjst;t+1)(atjst;t) or(atjst;t+1)<(atjst;t)
depending on the coecients.
214

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_Book-Mathematical-Foundation-of-Reinforcement-Learning-main_课程MOC|Book-Mathematical-Foundation-of-Reinforcement-Learning-main MOC]]
