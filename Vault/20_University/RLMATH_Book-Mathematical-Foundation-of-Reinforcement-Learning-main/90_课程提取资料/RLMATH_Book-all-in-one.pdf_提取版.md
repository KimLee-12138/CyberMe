---
id: extract-rlmath-20ff2d84
type: extract
status: extracted
course: RLMATH
source:
  - "[[91_Raw-Archive/PDF/RLMATH_Book-all-in-one.pdf_课件_未知日期_20ff2d84.pdf]]"
source_pages: all
source_hash: "20ff2d84d41c14c1bc8cd0eae96100968b9cc0fc7a046c9aee337dc73b2d28f0"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# Book-all-in-one.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

Mathematical Foundations
of
Reinforcement Learning
Shiyu Zhao

## 第2页

Contents
Contents v
Preface vii
Overview of this Book ix
1 Basic Concepts 1
1.1 A grid world example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 State and action . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 State transition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.5 Reward . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.6 Trajectories, returns, and episodes . . . . . . . . . . . . . . . . . . . . . . 8
1.7 Markov decision processes . . . . . . . . . . . . . . . . . . . . . . . . . . 11
1.8 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.9 Q&A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2 State Values and Bellman Equation 15
2.1 Motivating example 1: Why are returns important? . . . . . . . . . . . . 16
2.2 Motivating example 2: How to calculate returns? . . . . . . . . . . . . . 17
2.3 State values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.4 Bellman equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.5 Examples for illustrating the Bellman equation . . . . . . . . . . . . . . . 22
2.6 Matrix-vector form of the Bellman equation . . . . . . . . . . . . . . . . 25
2.7 Solving state values from the Bellman equation . . . . . . . . . . . . . . 27
2.7.1 Closed-form solution . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.7.2 Iterative solution . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.7.3 Illustrative examples . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.8 From state value to action value . . . . . . . . . . . . . . . . . . . . . . . 30
2.8.1 Illustrative examples . . . . . . . . . . . . . . . . . . . . . . . . . 31
2.8.2 The Bellman equation in terms of action values . . . . . . . . . . 32
2.9 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
i

## 第3页

2.10 Q&A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3 Optimal State Values and Bellman Optimality Equation 35
3.1 Motivating example: How to improve policies? . . . . . . . . . . . . . . . 36
3.2 Optimal state values and optimal policies . . . . . . . . . . . . . . . . . . 37
3.3 Bellman optimality equation . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.3.1 Maximization of the right-hand side of the BOE . . . . . . . . . . 39
3.3.2 Matrix-vector form of the BOE . . . . . . . . . . . . . . . . . . . 40
3.3.3 Contraction mapping theorem . . . . . . . . . . . . . . . . . . . . 40
3.3.4 Contraction property of the right-hand side of the BOE . . . . . . 44
3.4 Solving an optimal policy from the BOE . . . . . . . . . . . . . . . . . . 46
3.5 Factors that in
uence optimal policies . . . . . . . . . . . . . . . . . . . 49
3.6 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
3.7 Q&A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
4 Value Iteration and Policy Iteration 57
4.1 Value iteration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.1.1 Elementwise form and implementation . . . . . . . . . . . . . . . 58
4.1.2 Illustrative examples . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.2 Policy iteration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
4.2.1 Algorithm analysis . . . . . . . . . . . . . . . . . . . . . . . . . . 62
4.2.2 Elementwise form and implementation . . . . . . . . . . . . . . . 65
4.2.3 Illustrative examples . . . . . . . . . . . . . . . . . . . . . . . . . 67
4.3 Truncated policy iteration . . . . . . . . . . . . . . . . . . . . . . . . . . 70
4.3.1 Comparing value iteration and policy iteration . . . . . . . . . . . 70
4.3.2 Truncated policy iteration algorithm . . . . . . . . . . . . . . . . 72
4.4 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
4.5 Q&A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
5 Monte Carlo Methods 77
5.1 Motivating example: Mean estimation . . . . . . . . . . . . . . . . . . . 78
5.2 MC Basic: The simplest MC-based algorithm . . . . . . . . . . . . . . . 80
5.2.1 Converting policy iteration to be model-free . . . . . . . . . . . . 80
5.2.2 The MC Basic algorithm . . . . . . . . . . . . . . . . . . . . . . . 81
5.2.3 Illustrative examples . . . . . . . . . . . . . . . . . . . . . . . . . 83
5.3 MC Exploring Starts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
5.3.1 Utilizing samples more eciently . . . . . . . . . . . . . . . . . . 86
5.3.2 Updating policies more eciently . . . . . . . . . . . . . . . . . . 87
5.3.3 Algorithm description . . . . . . . . . . . . . . . . . . . . . . . . 88
5.4 MC-Greedy: Learning without exploring starts . . . . . . . . . . . . . . 89
5.4.1-greedy policies . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
ii

## 第4页

5.4.2 Algorithm description . . . . . . . . . . . . . . . . . . . . . . . . 90
5.4.3 Illustrative examples . . . . . . . . . . . . . . . . . . . . . . . . . 91
5.5 Exploration and exploitation of -greedy policies . . . . . . . . . . . . . . 92
5.6 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
5.7 Q&A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
6 Stochastic Approximation 101
6.1 Motivating example: Mean estimation . . . . . . . . . . . . . . . . . . . 102
6.2 Robbins-Monro algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . 103
6.2.1 Convergence properties . . . . . . . . . . . . . . . . . . . . . . . . 105
6.2.2 Application to mean estimation . . . . . . . . . . . . . . . . . . . 108
6.3 Dvoretzky's convergence theorem . . . . . . . . . . . . . . . . . . . . . . 109
6.3.1 Proof of Dvoretzky's theorem . . . . . . . . . . . . . . . . . . . . 110
6.3.2 Application to mean estimation . . . . . . . . . . . . . . . . . . . 112
6.3.3 Application to the Robbins-Monro theorem . . . . . . . . . . . . 112
6.3.4 An extension of Dvoretzky's theorem . . . . . . . . . . . . . . . . 113
6.4 Stochastic gradient descent . . . . . . . . . . . . . . . . . . . . . . . . . . 114
6.4.1 Application to mean estimation . . . . . . . . . . . . . . . . . . . 116
6.4.2 Convergence pattern of SGD . . . . . . . . . . . . . . . . . . . . . 116
6.4.3 A deterministic formulation of SGD . . . . . . . . . . . . . . . . . 118
6.4.4 BGD, SGD, and mini-batch GD . . . . . . . . . . . . . . . . . . . 119
6.4.5 Convergence of SGD . . . . . . . . . . . . . . . . . . . . . . . . . 121
6.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
6.6 Q&A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
7 Temporal-Dierence Methods 125
7.1 TD learning of state values . . . . . . . . . . . . . . . . . . . . . . . . . . 126
7.1.1 Algorithm description . . . . . . . . . . . . . . . . . . . . . . . . 126
7.1.2 Property analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
7.1.3 Convergence analysis . . . . . . . . . . . . . . . . . . . . . . . . . 130
7.2 TD learning of action values: Sarsa . . . . . . . . . . . . . . . . . . . . . 133
7.2.1 Algorithm description . . . . . . . . . . . . . . . . . . . . . . . . 133
7.2.2 Optimal policy learning via Sarsa . . . . . . . . . . . . . . . . . . 134
7.3 TD learning of action values: n-step Sarsa . . . . . . . . . . . . . . . . . 138
7.4 TD learning of optimal action values: Q-learning . . . . . . . . . . . . . 140
7.4.1 Algorithm description . . . . . . . . . . . . . . . . . . . . . . . . 140
7.4.2 O-policy vs on-policy . . . . . . . . . . . . . . . . . . . . . . . . 141
7.4.3 Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
7.4.4 Illustrative examples . . . . . . . . . . . . . . . . . . . . . . . . . 144
7.5 A unied viewpoint . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
7.6 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
iii

## 第5页

7.7 Q&A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
8 Value Function Methods 151
8.1 Value representation: From table to function . . . . . . . . . . . . . . . . 152
8.2 TD learning of state values based on function approximation . . . . . . . 155
8.2.1 Objective function . . . . . . . . . . . . . . . . . . . . . . . . . . 156
8.2.2 Optimization algorithms . . . . . . . . . . . . . . . . . . . . . . . 161
8.2.3 Selection of function approximators . . . . . . . . . . . . . . . . . 162
8.2.4 Illustrative examples . . . . . . . . . . . . . . . . . . . . . . . . . 164
8.2.5 Theoretical analysis . . . . . . . . . . . . . . . . . . . . . . . . . . 167
8.3 TD learning of action values based on function approximation . . . . . . 179
8.3.1 Sarsa with function approximation . . . . . . . . . . . . . . . . . 179
8.3.2 Q-learning with function approximation . . . . . . . . . . . . . . 180
8.4 Deep Q-learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
8.4.1 Algorithm description . . . . . . . . . . . . . . . . . . . . . . . . 182
8.4.2 Illustrative examples . . . . . . . . . . . . . . . . . . . . . . . . . 184
8.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
8.6 Q&A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
9 Policy Gradient Methods 191
9.1 Policy representation: From table to function . . . . . . . . . . . . . . . 192
9.2 Metrics for dening optimal policies . . . . . . . . . . . . . . . . . . . . . 193
9.3 Gradients of the metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
9.3.1 Derivation of the gradients in the discounted case . . . . . . . . . 200
9.3.2 Derivation of the gradients in the undiscounted case . . . . . . . . 205
9.4 Monte Carlo policy gradient (REINFORCE) . . . . . . . . . . . . . . . . 210
9.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
9.6 Q&A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
10 Actor-Critic Methods 215
10.1 The simplest actor-critic algorithm (QAC) . . . . . . . . . . . . . . . . . 216
10.2 Advantage actor-critic (A2C) . . . . . . . . . . . . . . . . . . . . . . . . 217
10.2.1 Baseline invariance . . . . . . . . . . . . . . . . . . . . . . . . . . 217
10.2.2 Algorithm description . . . . . . . . . . . . . . . . . . . . . . . . 220
10.3 O-policy actor-critic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
10.3.1 Importance sampling . . . . . . . . . . . . . . . . . . . . . . . . . 221
10.3.2 The o-policy policy gradient theorem . . . . . . . . . . . . . . . 224
10.3.3 Algorithm description . . . . . . . . . . . . . . . . . . . . . . . . 226
10.4 Deterministic actor-critic . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
10.4.1 The deterministic policy gradient theorem . . . . . . . . . . . . . 227
10.4.2 Algorithm description . . . . . . . . . . . . . . . . . . . . . . . . 234
iv

## 第6页

10.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
10.6 Q&A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
A Preliminaries for Probability Theory 237
B Measure-Theoretic Probability Theory 243
C Convergence of Sequences 251
C.1 Convergence of deterministic sequences . . . . . . . . . . . . . . . . . . . 251
C.2 Convergence of stochastic sequences . . . . . . . . . . . . . . . . . . . . . 254
D Preliminaries for Gradient Descent 259
Bibliography 270
Symbols 271
Index 273
v

## 第7页

vi

## 第8页

Preface
This book aims to provide a mathematical butfriendly introduction to the fundamental
concepts, basic problems, and classic algorithms in reinforcement learning. Some essential
features of this book are highlighted as follows.
The book introduces reinforcement learning from a mathematical point of view. Hope-
fully, readers will not only know the procedure of an algorithm but also understand
why the algorithm was designed in the rst place and why it works eectively.
The depth of the mathematics is carefully controlled to an adequate level. The math-
ematics is also presented in a carefully designed manner to ensure that the book is
friendly to read. Readers can read the materials presented in gray boxes selectively
according to their interests.
Many illustrative examples are given to help readers better understand the topics. All
the examples in this book are based on a grid world task, which is easy to understand
and helpful for illustrating concepts and algorithms.
When introducing an algorithm, the book aims to separate its core idea from compli-
cations that may be distracting. In this way, readers can better grasp the core idea
of an algorithm.
The contents of the book are coherently organized. Each chapter is built based on the
preceding chapter and lays a necessary foundation for the subsequent one.
This book is designed for senior undergraduate students, graduate students, researcher-
s, and practitioners who are interested in reinforcement learning. It does not require
readers to have any background in reinforcement learning because it starts by introduc-
ing the most basic concepts. If the reader already has some background in reinforcement
learning, I believe the book can help them understand some topics more deeply or provide
dierent perspectives. This book, however, requires the reader to have some knowledge
of probability theory and linear algebra. Some basics of the required mathematics are
also included in the appendix of this book.
I have been teaching a graduate-level course on reinforcement learning since 2019. I
want to thank the students in my class for their feedback on my teaching. I put the draft
of this book online in August 2022. Up to now, I have received valuable feedback from
many readers. I want to express my gratitude to these readers. Moreover, I would like
vii

## 第9页

to thank my research assistant, Jialing Lv, for her excellent support in editing the book
and my lecture videos; my teaching assistants, Jianan Li and Yize Mi, for their help in
my teaching; my Ph.D. student Canlun Zheng for his help in the design of a picture in
the book; and my family for their wonderful support. Finally, I would like to thank the
editors of this book, Dr. Lanlan Chang and Mr. Sai Guo from Springer Nature Press
and Tsinghua University Press, for their great support.
Please note that I have created an open course based on this textbook. Both the slides
of the open course and the PDF of this textbook are available online for free download. For
more information, you can visit the homepage of the textbook: https://github.com/
MathFoundationRL/Book-Mathematical-Foundation-of-Reinforcement-Learning
I sincerely hope this book can help readers smoothly enter the exciting eld of rein-
forcement learning.
Shiyu Zhao
viii

## 第10页

Overview of this Book
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
Figure 1: The map of this book.
Before we start the journey, it is important to look at the \map" of the book shown
in Figure 1. This book contains ten chapters, which can be classied into two parts: the
rst part is about basic tools, and the second part is about algorithms. The ten chapters
are highly correlated. In general, it is necessary to study the earlier chapters rst before
the later ones.
Next, please follow me on a quick tour through the ten chapters. Two aspects of each
chapter will be covered. The rst aspect is the contents introduced in each chapter, and
the second aspect is its relationships with the previous and subsequent chapters. A heads
up for you to read this overview is as follows. The purpose of this overview is to give you
an impression of the contents and structure of this book. It is all right if you encounter
many concepts you do not understand. Hopefully, you can make a proper study plan
ix

## 第11页

that is suitable for you after reading this overview.
Chapter 1 introduces the basic concepts such as states, actions, rewards, returns, and
policies, which are widely used in the subsequent chapters. These concepts are rst
introduced based on a grid world example, where a robot aims to reach a prespecied
target. Then, the concepts are introduced in a more formal manner based on the
framework of Markov decision processes.
Chapter 2 introduces two key elements. The rst is a key concept, and the second is
a key tool. The key concept is the state value , which is dened as the expected return
that an agent can obtain when starting from a state if it follows a given policy. The
greater the state value is, the better the corresponding policy is. Thus, state values
can be used to evaluate whether a policy is good or not.
The key tool is the Bellman equation , which can be used to analyze state values. In
a nutshell, the Bellman equation describes the relationship between the values of all
states. By solving the Bellman equation, we can obtain the state values. Such a
process is called policy evaluation , which is a fundamental concept in reinforcement
learning. Finally, this chapter introduces the concept of action values.
Chapter 3 also introduces two key elements. The rst is a key concept, and the
second is a key tool. The key concept is the optimal policy . An optimal policy has the
greatest state values compared to other policies. The key tool is the Bellman optimality
equation . As its name suggests, the Bellman optimality equation is a special Bellman
equation.
Here is a fundamental question: what is the ultimate goal of reinforcement learn-
ing? The answer is to obtain optimal policies. The Bellman optimality equation is
important because it can be used to obtain optimal policies. We will see that the
Bellman optimality equation is elegant and can help us thoroughly understand many
fundamental problems.
The rst three chapters constitute the rst part of this book. This part lays the
necessary foundations for the subsequent chapters. Starting in Chapter 4, the book
introduces algorithms for learning optimal policies.
Chapter 4 introduces three algorithms: value iteration, policy iteration, and truncated
policy iteration. The three algorithms have close relationships with each other. First,
the value iteration algorithm is exactly the algorithm introduced in Chapter 3 for
solving the Bellman optimality equation. Second, the policy iteration algorithm is
an extension of the value iteration algorithm. It is also the foundation for Monte
Carlo (MC) algorithms introduced in Chapter 5. Third, the truncated policy iteration
algorithm is a unied version that includes the value iteration and policy iteration
algorithms as special cases.
x

## 第12页

The three algorithms share the same structure. That is, every iteration has two steps.
One step is to update the value, and the other step is to update the policy. The idea
of the interaction between value and policy updates widely exists in reinforcement
learning algorithms. This idea is also known as generalized policy iteration . In ad-
dition, the algorithms introduced in this chapter are actually dynamic programming
algorithms, which require system models. By contrast, all the algorithms introduced
in the subsequent chapters do not require models. It is important to well understand
the contents of this chapter before proceeding to the subsequent ones.
Starting in Chapter 5, we introduce model-free reinforcement learning algorithms that
do not require system models. While this is the rst time we introduce model-free
algorithms in this book, we must ll a knowledge gap: how to nd optimal policies
without models? The philosophy is simple. If we do not have a model, we must have
some data. If we do not have data, we must have a model. If we have neither, then we
can do nothing. The \data" in reinforcement learning refer to the experience samples
generated when the agent interacts with the environment.
This chapter introduces three algorithms based on MC estimation that can learn
optimal policies from experience samples. The rst and simplest algorithm is MC
Basic, which can be readily obtained by extending the policy iteration algorithm
introduced in Chapter 4. Understanding the MC Basic algorithm is important for
grasping the fundamental idea of MC-based reinforcement learning. By extending
this algorithm, we further introduce two more complicated but more ecient MC-
based algorithms. The fundamental trade-o between exploration and exploitation is
also elaborated in this chapter.
Up to this point, the reader may have noticed that the contents of these chapters are
highly correlated. For example, if we want to study the MC algorithms (Chapter 5), we
must rst understand the policy iteration algorithm (Chapter 4). To study the policy
iteration algorithm, we must rst know the value iteration algorithm (Chapter 4). To
comprehend the value iteration algorithm, we rst need to understand the Bellman opti-
mality equation (Chapter 3). To understand the Bellman optimality equation, we need
to study the Bellman equation (Chapter 2) rst. Therefore, it is highly recommended to
study the chapters one by one. Otherwise, it may be dicult to understand the contents
in the later chapters.
There is a knowledge gap when we move from Chapter 5 to Chapter 7: the algorithms
in Chapter 7 are incremental , but the algorithms in Chapter 5 are non-incremental .
Chapter 6 is designed to ll this knowledge gap by introducing the stochastic ap-
proximation theory. Stochastic approximation refers to a broad class of stochastic
iterative algorithms for solving root-nding or optimization problems. The classic
Robbins-Monro and stochastic gradient descent algorithms are special stochastic ap-
proximation algorithms. Although this chapter does not introduce any reinforcement
xi

## 第13页

learning algorithms, it is important because it lays the necessary foundations for s-
tudying Chapter 7.
Chapter 7 introduces the classic temporal-dierence (TD) algorithms. With the prepa-
ration in Chapter 6, I believe the reader will not be surprised when seeing the TD
algorithms. From a mathematical point of view, TD algorithms can be viewed as
stochastic approximation algorithms for solving the Bellman or Bellman optimality
equations. Like Monte Carlo learning, TD learning is also model-free, but it has some
advantages due to its incremental form. For example, it can learn in an online manner:
it can update the value estimate every time an experience sample is received. This
chapter introduces quite a few TD algorithms such as Sarsa and Q-learning. The
important concepts of on-policy and o-policy are also introduced.
Chapter 8 introduces the value function approximation method. In fact, this chap-
ter continues to introduce TD algorithms, but it uses a dierent way to represent
state/action values. In the preceding chapters, state/action values are represented by
tables . The tabular method is straightforward to understand, but it is inecient for
handling large state or action spaces. To solve this problem, we can employ the value
function approximation method. The key to understanding this method is to under-
stand the three steps in its optimization formulation. The rst step is to select an
objective function for dening optimal policies. The second step is to derive the gradi-
ent of the objective function. The third step is to apply a gradient-based algorithm to
solve the optimization problem. This method is important because it has become the
standard technique to represent values. It is also the location in which articial neu-
ral networks are incorporated into reinforcement learning as function approximators.
The famous deep Q-learning algorithm is also introduced in this chapter.
Chapter 9 introduces the policy gradient method, which is the foundation of many
modern reinforcement learning algorithms. The policy gradient method is policy-based .
It is a large step forward in this book because all the methods in the previous chapters
arevalue-based . The basic idea of the policy gradient method is simple: it selects
an appropriate scalar metric and then optimizes it via a gradient-ascent algorithm.
Chapter 9 has an intimate relationship with Chapter 8 because they both rely on the
idea of function approximation. The advantages of the policy gradient method are
numerous. For example, it is more ecient for handling large state/action spaces. It
has stronger generalization abilities and is more ecient in sample usage.
Chapter 10 introduces actor-critic methods. From one point of view, actor-critic refers
to a structure that incorporates both policy-based and value-based methods. From
another point of view, actor-critic methods are not new since they still fall into the
scope of the policy gradient method. Specically, they can be obtained by extending
the policy gradient algorithm introduced in Chapter 9. It is necessary for the reader
to properly understand the contents in Chapters 8 and 9 before studying Chapter 10.
xii

## 第14页

Chapter 1
Basic Concepts
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
Figure 1.1: Where we are in this book.
This chapter introduces the basic concepts of reinforcement learning. These concepts
are important because they will be widely used in this book. We rst introduce these
concepts using examples and then formalize them in the framework of Markov decision
processes.
1.1 A grid world example
Consider an example as shown in Figure 1.2, where a robot moves in a grid world. The
robot, called agent , can move across adjacent cells in the grid. At each time step, it can
1

## 第15页

1.2. State and action
only occupy a single cell. The white cells are accessible for entry, and the orange cells
areforbidden . There is a target cell that the robot would like to reach. We will use such
grid world examples throughout this book since they are intuitive for illustrating new
concepts and algorithms.
Start
ForbiddenForbidden
Target
Figure 1.2: The grid world example is used throughout the book.
The ultimate goal of the agent is to nd a \good" policy that enables it to reach
the target cell when starting from any initial cell. How can the \goodness" of a policy
be dened? The idea is that the agent should reach the target without entering any
forbidden cells, taking unnecessary detours, or colliding with the boundary of the grid.
It would be trivial to plan a path to reach the target cell if the agent knew the map of
the grid world. The task becomes nontrivial if the agent does not know any information
about the environment in advance. Then, the agent must interact with the environment
to nd a good policy by trial and error. To do that, the concepts presented in the rest of
the chapter are necessary.
1.2 State and action
The rst concept to be introduced is the state, which describes the agent's status with
respect to the environment. In the grid world example, the state corresponds to the
agent's location. Since there are nine cells, there are nine states as well. They are
indexed as s1;s2;:::;s 9, as shown in Figure 1.3(a). The set of all the states is called the
state space , denoted asS=fs1;:::;s 9g.
For each state, the agent can take ve possible actions : moving upward, moving
rightward, moving downward, moving leftward, and staying still. These ve actions are
denoted as a1;a2;:::;a 5, respectively (see Figure 1.3(b)). The set of all actions is called
theaction space , denoted asA=fa1;:::;a 5g. Dierent states can have dierent action
spaces. For instance, considering that taking a1ora4in states1would lead to a collision
with the boundary, we can set the action space for state s1asA(s1) =fa2;a3;a5g. In
this book, we consider the most general case: A(si) =A=fa1;:::;a 5gfor alli.
2

## 第16页

1.3. State transition
s1 s2 s3
s4 s5 s6
s7 s8 s9
(a) States
a1
a2 a4
a3a5 (b) Actions
Figure 1.3: Illustrations of the state and action concepts. (a) There are nine states fs1;:::;s 9g. (b)
Each state has ve possible actions fa1;a2;a3;a4;a5g.
1.3 State transition
When taking an action, the agent may move from one state to another. Such a process is
called state transition . For example, if the agent is in state s1and selects action a2(that
is, moving rightward), then the agent moves to state s2. Such a process can be expressed
as
s1a2  !s2:
We next examine two important examples.
What is the next state when the agent attempts to go beyond the boundary, for
example, taking action a1in states1? The answer is that the agent will be bounced
back because it is impossible for the agent to exit the state space. Hence, we have
s1a1  !s1.
What is the next state when the agent attempts to enter a forbidden cell, for example,
taking action a2in states5? Two dierent scenarios may be encountered. In the rst
scenario, although s6is forbidden, it is still accessible . In this case, the next state
iss6; hence, the state transition process is s5a2  !s6. In the second scenario, s6is
not accessible because, for example, it is surrounded by walls. In this case, the agent
is bounced back to s5if it attempts to move rightward; hence, the state transition
process iss5a2  !s5.
Which scenario should we consider? The answer depends on the physical environmen-
t. In this book, we consider the rst scenario where the forbidden cells are accessible,
although stepping into them may get punished. This scenario is more general and in-
teresting. Moreover, since we are considering a simulation task, we can dene the state
transition process however we prefer. In real-world applications, the state transition
process is determined by real-world dynamics.
The state transition process is dened for each state and its associated actions. This
process can be described by a table as shown in Table 1.1. In this table, each row
3

## 第17页

1.4. Policy
corresponds to a state, and each column corresponds to an action. Each cell indicates
the next state to transition to after the agent takes an action at the corresponding state.
a1(upward) a2(rightward) a3(downward) a4(leftward) a5(still)
s1s1 s2 s4 s1 s1
s2s2 s3 s5 s1 s2
s3s3 s3 s6 s2 s3
s4s1 s5 s7 s4 s4
s5s2 s6 s8 s4 s5
s6s3 s6 s9 s5 s6
s7s4 s8 s7 s7 s7
s8s5 s9 s8 s7 s8
s9s6 s9 s9 s8 s9
Table 1.1: A tabular representation of the state transition process. Each cell indicates the next state to
transition to after the agent takes an action at a state.
Mathematically, the state transition process can be described by conditional proba-
bilities. For example, for s1anda2, the conditional probability distribution is
p(s1js1;a2) = 0;
p(s2js1;a2) = 1;
p(s3js1;a2) = 0;
p(s4js1;a2) = 0;
p(s5js1;a2) = 0;
which indicates that, when taking a2ats1, the probability of the agent moving to s2
is one, and the probabilities of the agent moving to other states are zero. As a result,
taking action a2ats1will certainly cause the agent to transition to s2. The preliminaries
of conditional probability are given in Appendix A. Readers are strongly advised to be
familiar with probability theory since it is necessary for studying reinforcement learning.
Although it is intuitive, the tabular representation is only able to describe determinis-
ticstate transitions. In general, state transitions can be stochastic and must be described
by conditional probability distributions. For instance, when random wind gusts are ap-
plied across the grid, if taking action a2ats1, the agent may be blown to s5instead of
s2. We havep(s5js1;a2)>0 in this case. Nevertheless, we merely consider deterministic
state transitions in the grid world examples for simplicity in this book.
1.4 Policy
Apolicy tells the agent which actions to take at every state. Intuitively, policies can
be depicted as arrows (see Figure 1.4(a)). Following a policy, the agent can generate a
trajectory starting from an initial state (see Figure 1.4(b)).
4

## 第18页

1.4. Policy
(a) A deterministic policy
(b) Trajectories obtained from the policy
Figure 1.4: A policy represented by arrows and some trajectories obtained by starting from dierent
initial states.
Mathematically, policies can be described by conditional probabilities. Denote the
policy in Figure 1.4 as (ajs), which is a conditional probability distribution function
dened for every state. For example, the policy for s1is
(a1js1) = 0;
(a2js1) = 1;
(a3js1) = 0;
(a4js1) = 0;
(a5js1) = 0;
which indicates that the probability of taking action a2in states1is one, and the prob-
abilities of taking other actions are zero.
The above policy is deterministic . Policies may be stochastic in general. For example,
the policy shown in Figure 1.5 is stochastic: in state s1, the agent may take actions to
go either rightward or downward. The probabilities of taking these two actions are the
5

## 第19页

1.5. Reward
same (both are 0 :5). In this case, the policy for s1is
(a1js1) = 0;
(a2js1) = 0:5;
(a3js1) = 0:5;
(a4js1) = 0;
(a5js1) = 0:
p= 0.5
p= 0.5
Figure 1.5: A stochastic policy. In state s1, the agent may move rightward or downward with equal
probabilities of 0 :5.
Policies represented by conditional probabilities can be stored as tables. For example,
Table 1.2 represents the stochastic policy depicted in Figure 1.5. The entry in the ith
row andjth column is the probability of taking the jth action at the ith state. Such
a representation is called a tabular representation . We will introduce another way to
represent policies as parameterized functions in Chapter 8.
a1(upward) a2(rightward) a3(downward) a4(leftward ) a5(still)
s1 0 0.5 0.5 0 0
s2 0 0 1 0 0
s3 0 0 0 1 0
s4 0 1 0 0 0
s5 0 0 1 0 0
s6 0 0 1 0 0
s7 0 1 0 0 0
s8 0 1 0 0 0
s9 0 0 0 0 1
Table 1.2: A tabular representation of a policy. Each entry indicates the probability of taking an action
at a state.
1.5 Reward
Reward is one of the most unique concepts in reinforcement learning.
6

## 第20页

1.5. Reward
After executing an action at a state, the agent obtains a reward, denoted as r, as
feedback from the environment. The reward is a function of the state sand action a.
Hence, it is also denoted as r(s;a). Its value can be a positive or negative real number
or zero. Dierent rewards have dierent impacts on the policy that the agent would
eventually learn. Generally speaking, with a positive reward, we encourage the agent to
take the corresponding action. With a negative reward, we discourage the agent from
taking that action.
In the grid world example, the rewards are designed as follows:
If the agent attempts to exit the boundary, let rboundary = 1.
If the agent attempts to enter a forbidden cell, let rforbidden = 1.
If the agent reaches the target state, let rtarget = +1.
Otherwise, the agent obtains a reward of rother= 0.
Special attention should be given to the target state s9. The reward process does not
have to terminate after the agent reaches s9. If the agent takes action a5ats9, the next
state is again s9, and the reward is rtarget = +1. If the agent takes action a2, the next
state is also s9, but the reward is rboundary = 1.
A reward can be interpreted as a human-machine interface, with which we can guide
the agent to behave as we expect. For example, with the rewards designed above, we can
expect that the agent tends to avoid exiting the boundary or stepping into the forbidden
cells. Designing appropriate rewards is an important step in reinforcement learning. This
step is, however, nontrivial for complex tasks since it may require the user to understand
the given problem well. Nevertheless, it may still be much easier than solving the problem
with other approaches that require a professional background or a deep understanding of
the given problem.
The process of getting a reward after executing an action can be intuitively represented
as a table, as shown in Table 1.3. Each row of the table corresponds to a state, and each
column corresponds to an action. The value in each cell of the table indicates the reward
that can be obtained by taking an action at a state.
One question that beginners may ask is as follows: if given the table of rewards, can
we nd good policies by simply selecting the actions with the greatest rewards? The
answer is no. That is because these rewards are immediate rewards that can be obtained
after taking an action. To determine a good policy, we must consider the total reward
obtained in the long run (see Section 1.6 for more information). An action with the
greatest immediate reward may not lead to the greatest total reward.
Although intuitive, the tabular representation is only able to describe deterministic
reward processes. A more general approach is to use conditional probabilities p(rjs;a) to
describe reward processes. For example, for state s1, we have
p(r= 1js1;a1) = 1; p(r6= 1js1;a1) = 0:
7

## 第21页

1.6. Trajectories, returns, and episodes
a1(upward) a2(rightward) a3(downward) a4(leftward) a5(still)
s1rboundary 0 0 rboundary 0
s2rboundary 0 0 0 0
s3rboundary rboundary rforbidden 0 0
s4 0 0 rforbidden rboundary 0
s5 0 rforbidden 0 0 0
s6 0 rboundary rtarget 0rforbidden
s7 0 0 rboundary rboundary rforbidden
s8 0 rtarget rboundary rforbidden 0
s9rforbidden rboundary rboundary 0rtarget
Table 1.3: A tabular representation of the process of obtaining rewards. Here, the process is deterministic.
Each cell indicates how much reward can be obtained after the agent takes an action at a given state.
This indicates that, when taking a1ats1, the agent obtains r= 1 with certainty. In
this example, the reward process is deterministic. In general, it can be stochastic. For
example, if a student studies hard, he or she would receive a positive reward (e.g., higher
grades on exams), but the specic value of the reward may be uncertain.
1.6 Trajectories, returns, and episodes
r= 0
r= 0
r= 0
r= +1r= +1s1 s2 s3
s4 s5 s6
s7 s8 s9
(a) Policy 1 and the trajectory
r= 0
r=−1
r= 0 r= +1r= +1s1 s2 s3
s4 s5 s6
s7 s8 s9 (b) Policy 2 and the trajectory
Figure 1.6: Trajectories obtained by following two policies. The trajectories are indicated by red dashed
lines.
Atrajectory is a state-action-reward chain. For example, given the policy shown in
Figure 1.6(a), the agent can move along a trajectory as follows:
s1a2  !
r=0s2a3  !
r=0s5a3  !
r=0s8a2  !
r=1s9:
The return of this trajectory is dened as the sum of all the rewards collected along the
trajectory:
return = 0 + 0 + 0 + 1 = 1 : (1.1)
8

## 第22页

1.6. Trajectories, returns, and episodes
Returns are also called total rewards orcumulative rewards .
Returns can be used to evaluate policies. For example, we can evaluate the two
policies in Figure 1.6 by comparing their returns. In particular, starting from s1, the
return obtained by the left policy is 1 as calculated above. For the right policy, starting
froms1, the following trajectory is generated:
s1a3  !
r=0s4a3   !
r= 1s7a2  !
r=0s8a2   !
r=+1s9:
The corresponding return is
return = 0 1 + 0 + 1 = 0 : (1.2)
The returns in (1.1) and (1.2) indicate that the left policy is better than the right one
since its return is greater. This mathematical conclusion is consistent with the intuition
that the right policy is worse since it passes through a forbidden cell.
A return consists of an immediate reward and future rewards . Here, the immediate
reward is the reward obtained after taking an action at the initial state; the future
rewards refer to the rewards obtained after leaving the initial state. It is possible that the
immediate reward is negative while the future reward is positive. Thus, which actions to
take should be determined by the return (i.e., the total reward) rather than the immediate
reward to avoid short-sighted decisions.
The return in (1.1) is dened for a nite-length trajectory. Return can also be dened
for innitely long trajectories. For example, the trajectory in Figure 1.6 stops after
reachings9. Since the policy is well dened for s9, the process does not have to stop after
the agent reaches s9. We can design a policy so that the agent stays still after reaching
s9. Then, the policy would generate the following innitely long trajectory:
s1a2  !
r=0s2a3  !
r=0s5a3  !
r=0s8a2  !
r=1s9a5  !
r=1s9a5  !
r=1s9:::
The direct sum of the rewards along this trajectory is
return = 0 + 0 + 0 + 1 + 1 + 1 + =1;
which unfortunately diverges. Therefore, we must introduce the discounted return con-
cept for innitely long trajectories. In particular, the discounted return is the sum of the
discounted rewards:
discounted return = 0 + 
0 +
20 +
31+
41 +
51 +:::; (1.3)
where
2(0;1) is called the discount rate . When
2(0;1), the value of (1.3) can be
9

## 第23页

1.6. Trajectories, returns, and episodes
calculated as
discounted return = 
3(1 +
+
2+:::) =
31
1 
:
The introduction of the discount rate is useful for the following reasons. First, it
removes the stop criterion and allows for innitely long trajectories. Second, the dis-
count rate can be used to adjust the emphasis placed on near- or far-future rewards. In
particular, if 
is close to 0, then the agent places more emphasis on rewards obtained in
the near future. The resulting policy would be short-sighted. If 
is close to 1, then the
agent places more emphasis on the far future rewards. The resulting policy is far-sighted
and dares to take risks of obtaining negative rewards in the near future. These points
will be demonstrated in Section 3.5.
One important notion that was not explicitly mentioned in the above discussion is the
episode . When interacting with the environment by following a policy, the agent may stop
at some terminal states . The resulting trajectory is called an episode (or a trial). If the
environment or policy is stochastic, we obtain dierent episodes when starting from the
same state. However, if everything is deterministic, we always obtain the same episode
when starting from the same state.
An episode is usually assumed to be a nite trajectory. Tasks with episodes are called
episodic tasks . However, some tasks may have no terminal states, meaning that the pro-
cess of interacting with the environment will never end. Such tasks are called continuing
tasks . In fact, we can treat episodic and continuing tasks in a unied mathematical
manner by converting episodic tasks to continuing ones. To do that, we need well dene
the process after the agent reaches the terminal state. Specically, after reaching the
terminal state in an episodic task, the agent can continue taking actions in the following
two ways.
First, if we treat the terminal state as a special state, we can specically design its
action space or state transition so that the agent stays in this state forever. Such
states are called absorbing states , meaning that the agent never leaves a state once
reached. For example, for the target state s9, we can specifyA(s9) =fa5gor set
A(s9) =fa1;:::;a 5gwithp(s9js9;ai) = 1 for all i= 1;:::; 5.
Second, if we treat the terminal state as a normal state, we can simply set its action
space to the same as the other states, and the agent may leave the state and come
back again. Since a positive reward of r= 1 can be obtained every time s9is reached,
the agent will eventually learn to stay at s9forever to collect more rewards. Notably,
when an episode is innitely long and the reward received for staying at s9is positive,
a discount rate must be used to calculate the discounted return to avoid divergence.
In this book, we consider the second scenario where the target state is treated as a normal
state whose action space is A(s9) =fa1;:::;a 5g.
10

## 第24页

1.7. Markov decision processes
1.7 Markov decision processes
The previous sections of this chapter illustrated some fundamental concepts in reinforce-
ment learning through examples. This section presents these concepts in a more formal
way under the framework of Markov decision processes (MDPs).
An MDP is a general framework for describing stochastic dynamical systems. The
key ingredients of an MDP are listed below.
Sets:
- State space: the set of all states, denoted as S.
- Action space: a set of actions, denoted as A(s), associated with each state s2S.
- Reward set: a set of rewards, denoted as R(s;a), associated with each state-action
pair (s;a).
Model:
- State transition probability: In state s, when taking action a, the probability of
transitioning to state s0isp(s0js;a). It holds thatP
s02Sp(s0js;a) = 1 for any ( s;a).
- Reward probability: In state s, when taking action a, the probability of obtaining
rewardrisp(rjs;a). It holds thatP
r2R(s;a)p(rjs;a) = 1 for any ( s;a).
Policy: In state s, the probability of choosing action ais(ajs). It holds thatP
a2A(s)(ajs) = 1 for any s2S.
Markov property: The Markov property refers to the memoryless property of a s-
tochastic process. Mathematically, it means that
p(st+1jst;at;st 1;at 1;:::;s 0;a0) =p(st+1jst;at);
p(rt+1jst;at;st 1;at 1;:::;s 0;a0) =p(rt+1jst;at); (1.4)
wheretrepresents the current time step and t+ 1 represents the next time step.
Equation (1.4) indicates that the next state or reward depends merely on the current
state and action and is independent of the previous ones. The Markov property is
important for deriving the fundamental Bellman equation of MDPs, as shown in the
next chapter.
Here,p(s0js;a) andp(rjs;a) for all (s;a) are called the model ordynamics . The
model can be either stationary ornonstationary (or in other words, time-invariant or
time-variant). A stationary model does not change over time; a nonstationary model
may vary over time. For instance, in the grid world example, if a forbidden area may pop
up or disappear sometimes, the model is nonstationary. In this book, we only consider
stationary models.
11

## 第25页

1.8. Summary
One may have heard about the Markov processes (MPs). What is the dierence
between an MDP and an MP? The answer is that, once the policy in an MDP is xed,
the MDP degenerates into an MP. For example, the grid world example in Figure 1.7 can
be abstracted as a Markov process. In the literature on stochastic processes, a Markov
process is also called a Markov chain if it is a discrete-time process and the number of
states is nite or countable [1]. In this book, the terms \Markov process" and \Markov
chain" are used interchangeably when the context is clear. Moreover, this book mainly
considers nite MDPs where the numbers of states and actions are nite. This is the
simplest case that should be fully understood.
p= 0.5
p= 0.5
s1 s2 s3
s4 s5 s6
s7 s8 s9Prob=0.5
Prob=0.5Prob=1 Prob=1Prob=1Prob=1
Prob=1 Prob=1Prob=1
Figure 1.7: Abstraction of the grid world example as a Markov process. Here, the circles represent states
and the links with arrows represent state transitions.
Finally, reinforcement learning can be described as an agent-environment interaction
process. The agent is a decision-maker that can sense its state, maintain policies, and
execute actions. Everything outside of the agent is regarded as the environment . In the
grid world examples, the agent and environment correspond to the robot and grid world,
respectively. After the agent decides to take an action, the actuator executes such a
decision. Then, the state of the agent would be changed and a reward can be obtained.
By using interpreters, the agent can interpret the new state and the reward. Thus, a
closed loop can be formed.
1.8 Summary
This chapter introduced the basic concepts that will be widely used in the remainder of
the book. We used intuitive grid world examples to demonstrate these concepts and then
formalized them in the framework of MDPs. For more information about MDPs, readers
can see [1,2].
1.9 Q&A
Q: Can we set all the rewards as negative or positive?
A: In this chapter, we mentioned that a positive reward would encourage the agent
to take an action and that a negative reward would discourage the agent from taking
12

## 第26页

1.9. Q&A
the action. In fact, it is the relative reward values instead of the absolute values that
determine encouragement or discouragement.
More specically, we set rboundary = 1,rforbidden = 1,rtarget = +1, and rother= 0 in
this chapter. We can also add a common value to all these values without changing
the resulting optimal policy. For example, we can add  2 to all the rewards to obtain
rboundary = 3,rforbidden = 3,rtarget = 1, androther= 2. Although the rewards
are all negative, the resulting optimal policy is unchanged. That is because optimal
policies are invariant to ane transformations of the rewards. Details will be given in
Chapter 3.5.
Q: Is the reward a function of the next state?
A: We mentioned that the reward rdepends only on sandabut not the next state s0.
However, this may be counterintuitive since it is the next state that determines the
reward in many cases. For example, the reward is positive when the next state is the
target state. As a result, a question that naturally follows is whether a reward should
depend on the next state. A mathematical rephrasing of this question is whether we
should use p(rjs;a;s0) wheres0is the next state rather than p(rjs;a). The answer is
thatrdepends on s,a, ands0. However, since s0also depends on sanda, we can
equivalently write ras a function of sanda:p(rjs;a) =P
s0p(rjs;a;s0)p(s0js;a). In
this way, the Bellman equation can be easily established as shown in Chapter 2.
13

## 第27页

1.9. Q&A
14

## 第28页

Chapter 2
State Values and Bellman Equation
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
Figure 2.1: Where we are in this book.
This chapter introduces a core concept and an important tool . The core concept
is the state value , which is dened as the average reward that an agent can obtain if
it follows a given policy. The greater the state value is, the better the corresponding
policy is. State values can be used as a metric to evaluate whether a policy is good or
not. While state values are important, how can we analyze them? The answer is the
Bellman equation , which is an important tool for analyzing state values. In a nutshell,
the Bellman equation describes the relationships between the values of all states. By
solving the Bellman equation, we can obtain the state values. This process is called
policy evaluation , which is a fundamental concept in reinforcement learning. Finally, this
15

## 第29页

2.1. Motivating example 1: Why are returns important?
chapter introduces another important concept called the action value .
2.1 Motivating example 1: Why are returns impor-
tant?
The previous chapter introduced the concept of returns. In fact, returns play a funda-
mental role in reinforcement learning since they can evaluate whether a policy is good or
not. This is demonstrated by the following examples.
r= 0 r= 1
r= 1r= 1s1 s2
s3 s4
r=−1r= 1
r= 1r= 1s1 s2
s3 s4
p= 0.5
r=−1
r= 0
p= 0.5r= 1
r= 1r= 1s1 s2
s3 s4
Figure 2.2: Examples for demonstrating the importance of returns. The three examples have dierent
policies for s1.
Consider the three policies shown in Figure 2.2. It can be seen that the three policies
are dierent at s1. Which is the best and which is the worst? Intuitively, the leftmost
policy is the best because the agent starting from s1can avoid the forbidden area. The
middle policy is intuitively worse because the agent starting from s1moves to the forbid-
den area. The rightmost policy is in between the others because it has a probability of
0.5 to go to the forbidden area.
While the above analysis is based on intuition, a question that immediately follows is
whether we can use mathematics to describe such intuition. The answer is yes and relies
on the return concept. In particular, suppose that the agent starts from s1.
Following the rst policy, the trajectory is s1!s3!s4!s4. The corresponding
discounted return is
return 1= 0 +
1 +
21 +:::
=
(1 +
+
2+:::)
=

1 
;
where
2(0;1) is the discount rate.
Following the second policy, the trajectory is s1!s2!s4!s4. The discounted
16

## 第30页

2.2. Motivating example 2: How to calculate returns?
return is
return 2= 1 +
1 +
21 +:::
= 1 +
(1 +
+
2+:::)
= 1 +

1 
:
Following the third policy, two trajectories can possibly be obtained. One is s1!
s3!s4!s4, and the other is s1!s2!s4!s4. The probability of either
of the two trajectories is 0.5. Then, the average return that can be obtained starting
froms1is
return 3= 0:5
 1 +

1 

+ 0:5

1 

= 0:5 +

1 
:
By comparing the returns of the three policies, we notice that
return 1>return 3>return 2 (2.1)
for any value of 
. Inequality (2.1) suggests that the rst policy is the best because its
return is the greatest, and the second policy is the worst because its return is the smallest.
This mathematical conclusion is consistent with the aforementioned intuition: the rst
policy is the best since it can avoid entering the forbidden area, and the second policy is
the worst because it leads to the forbidden area.
The above examples demonstrate that returns can be used to evaluate policies: a
policy is better if the return obtained by following that policy is greater. Finally, it is
notable that return 3does not strictly comply with the denition of returns because it is
more like an expected value. It will become clear later that return 3is actually a state
value.
2.2 Motivating example 2: How to calculate returns?
While we have demonstrated the importance of returns, a question that immediately
follows is how to calculate the returns when following a given policy.
There are two ways to calculate returns.
The rst is simply by denition: a return equals the discounted sum of all the rewards
collected along a trajectory. Consider the example in Figure 2.3. Let videnote the
return obtained by starting from sifori= 1;2;3;4. Then, the returns obtained when
17

## 第31页

2.2. Motivating example 2: How to calculate returns?
r1
r2
r4
r3s1 s2
s4 s3
Figure 2.3: An example for demonstrating how to calculate returns. There are no target or forbidden
cells in this example.
starting from the four states in Figure 2.3 can be calculated as
v1=r1+
r2+
2r3+:::;
v2=r2+
r3+
2r4+:::;
v3=r3+
r4+
2r1+:::;
v4=r4+
r1+
2r2+::::(2.2)
The second way, which is more important, is based on the idea of bootstrapping . By
observing the expressions of the returns in (2.2), we can rewrite them as
v1=r1+
(r2+
r3+:::) =r1+
v2;
v2=r2+
(r3+
r4+:::) =r2+
v3;
v3=r3+
(r4+
r1+:::) =r3+
v4;
v4=r4+
(r1+
r2+:::) =r4+
v1:(2.3)
The above equations indicate an interesting phenomenon that the values of the returns
rely on each other. More specically, v1relies onv2,v2relies onv3,v3relies onv4,
andv4relies onv1. This re
ects the idea of bootstrapping, which is to obtain the
values of some quantities from themselves.
At rst glance, bootstrapping is an endless loop because the calculation of an unknown
value relies on another unknown value. In fact, bootstrapping is easier to understand
if we view it from a mathematical perspective. In particular, the equations in (2.3)
can be reformed into a linear matrix-vector equation:
2
6664v1
v2
v3
v43
7775
|{z}
v=2
6664r1
r2
r3
r43
7775+2
6664
v2

v3

v4

v13
7775=2
6664r1
r2
r3
r43
7775
|{z}
r+
2
66640 1 0 0
0 0 1 0
0 0 0 1
1 0 0 03
7775
|{z}
P2
6664v1
v2
v3
v43
7775
|{z}
v;
18

## 第32页

2.3. State values
which can be written compactly as
v=r+
Pv:
Thus, the value of vcan be calculated easily as v= (I 
P) 1r, whereIis the
identity matrix with appropriate dimensions. One may ask whether I 
Pis always
invertible. The answer is yes and explained in Section 2.7.1.
In fact, (2.3) is the Bellman equation for this simple example. Although it is simple,
(2.3) demonstrates the core idea of the Bellman equation: the return obtained by starting
from one state depends on those obtained when starting from other states. The idea of
bootstrapping and the Bellman equation for general scenarios will be formalized in the
following sections.
2.3 State values
We mentioned that returns can be used to evaluate policies. However, they are inappli-
cable to stochastic systems because starting from one state may lead to dierent returns.
Motivated by this problem, we introduce the concept of state value in this section.
First, we need to introduce some necessary notations. Consider a sequence of time
stepst= 0;1;2;:::. At timet, the agent is in state St, and the action taken following a
policyisAt. The next state is St+1, and the immediate reward obtained is Rt+1. This
process can be expressed concisely as
StAt !St+1;Rt+1:
Note thatSt;St+1;At;Rt+1are all random variables . Moreover, St;St+12S,At2A(St),
andRt+12R(St;At).
Starting from t, we can obtain a state-action-reward trajectory:
StAt !St+1;Rt+1At+1   !St+2;Rt+2At+2   !St+3;Rt+3::::
By denition, the discounted return along the trajectory is
Gt:=Rt+1+
Rt+2+
2Rt+3+:::;
where
2(0;1) is the discount rate. Note that Gtis a random variable since Rt+1;Rt+2;:::
are all random variables.
SinceGtis a random variable, we can calculate its expected value (also called the
expectation or mean):
v(s):=E[GtjSt=s]:
19

## 第33页

2.4. Bellman equation
Here,v(s) is called the state-value function or simply the state value ofs. Some impor-
tant remarks are given below.
v(s) depends on s. This is because its denition is a conditional expectation with
the condition that the agent starts from St=s.
v(s) depends on . This is because the trajectories are generated by following the
policy. For a dierent policy, the state value may be dierent.
v(s) does not depend on t. If the agent moves in the state space, trepresents the
current time step. The value of v(s) is determined once the policy is given.
The relationship between state values and returns is further claried as follows. When
both the policy and the system model are deterministic, starting from a state always leads
to the same trajectory. In this case, the return obtained starting from a state is equal
to the value of that state. By contrast, when either the policy or the system model is
stochastic, starting from the same state may generate dierent trajectories. In this case,
the returns of dierent trajectories are dierent, and the state value is the mean of these
returns.
Although returns can be used to evaluate policies as shown in Section 2.1, it is more
formal to use state values to evaluate policies: policies that generate greater state values
are better. Therefore, state values constitute a core concept in reinforcement learning.
While state values are important, a question that immediately follows is how to calculate
them. This question is answered in the next section.
2.4 Bellman equation
We now introduce the Bellman equation, a mathematical tool for analyzing state val-
ues. In a nutshell, the Bellman equation is a set of linear equations that describe the
relationships between the values of all the states.
We next derive the Bellman equation. First, note that Gtcan be rewritten as
Gt=Rt+1+
Rt+2+
2Rt+3+:::
=Rt+1+
(Rt+2+
Rt+3+:::)
=Rt+1+
Gt+1;
whereGt+1=Rt+2+
Rt+3+:::. This equation establishes the relationship between Gt
andGt+1. Then, the state value can be written as
v(s) =E[GtjSt=s]
=E[Rt+1+
Gt+1jSt=s]
=E[Rt+1jSt=s] +
E[Gt+1jSt=s]: (2.4)
20

## 第34页

2.4. Bellman equation
The two terms in (2.4) are analyzed below.
The rst term, E[Rt+1jSt=s], is the expectation of the immediate rewards. By using
the law of total expectation (Appendix A), it can be calculated as
E[Rt+1jSt=s] =X
a2A(ajs)E[Rt+1jSt=s;At=a]
=X
a2A(ajs)X
r2Rp(rjs;a)r: (2.5)
Here,AandRare the sets of possible actions and rewards, respectively. It should be
noted thatAmay be dierent for dierent states. In this case, Ashould be written as
A(s). Similarly,Rmay also depend on ( s;a). We drop the dependence on sor (s;a)
for the sake of simplicity in this book. Nevertheless, the conclusions are still valid in
the presence of dependence.
The second term, E[Gt+1jSt=s], is the expectation of the future rewards. It can be
calculated as
E[Gt+1jSt=s] =X
s02SE[Gt+1jSt=s;St+1=s0]p(s0js)
=X
s02SE[Gt+1jSt+1=s0]p(s0js) (due to the Markov property)
=X
s02Sv(s0)p(s0js)
=X
s02Sv(s0)X
a2Ap(s0js;a)(ajs): (2.6)
The above derivation uses the fact that E[Gt+1jSt=s;St+1=s0] =E[Gt+1jSt+1=s0],
which is due to the Markov property that the future rewards depend merely on the
present state rather than the previous ones.
Substituting (2.5)-(2.6) into (2.4) yields
v(s) =E[Rt+1jSt=s] +
E[Gt+1jSt=s];
=X
a2A(ajs)X
r2Rp(rjs;a)r
|{z}
mean of immediate rewards+
X
a2A(ajs)X
s02Sp(s0js;a)v(s0)
| {z }
mean of future rewards
=X
a2A(ajs)"X
r2Rp(rjs;a)r+
X
s02Sp(s0js;a)v(s0)#
;for alls2S: (2.7)
This equation is the Bellman equation , which characterizes the relationships of state
values. It is a fundamental tool for designing and analyzing reinforcement learning algo-
rithms.
21

## 第35页

2.5. Examples for illustrating the Bellman equation
The Bellman equation seems complex at rst glance. In fact, it has a clear structure.
Some remarks are given below.
v(s) andv(s0) are unknown state values to be calculated. It may be confusing to
beginners how to calculate the unknown v(s) given that it relies on another unknown
v(s0). It must be noted that the Bellman equation refers to a set of linear equations for
all states rather than a single equation. If we put these equations together, it becomes
clear how to calculate all the state values. Details will be given in Section 2.7.
(ajs) is a given policy. Since state values can be used to evaluate a policy, solving
the state values from the Bellman equation is a policy evaluation process, which is an
important process in many reinforcement learning algorithms, as we will see later in
the book.
p(rjs;a) andp(s0js;a) represent the system model. We will rst show how to calculate
the state values with this model in Section 2.7, and then show how to do that without
the model by using model-free algorithms later in this book.
In addition to the expression in (2.7), readers may also encounter other expressions
of the Bellman equation in the literature. We next introduce two equivalent expressions.
First, it follows from the law of total probability that
p(s0js;a) =X
r2Rp(s0;rjs;a);
p(rjs;a) =X
s02Sp(s0;rjs;a):
Then, equation (2.7) can be rewritten as
v(s) =X
a2A(ajs)X
s02SX
r2Rp(s0;rjs;a) [r+
v(s0)]:
This is the expression used in [3].
Second, the reward rmay depend solely on the next state s0in some problems. As a
result, we can write the reward as r(s0) and hence p(r(s0)js;a) =p(s0js;a), substituting
which into (2.7) gives
v(s) =X
a2A(ajs)X
s02Sp(s0js;a) [r(s0) +
v(s0)]:
2.5 Examples for illustrating the Bellman equation
We next use two examples to demonstrate how to write out the Bellman equation and
calculate the state values step by step. Readers are advised to carefully go through the
examples to gain a better understanding of the Bellman equation.
22

## 第36页

2.5. Examples for illustrating the Bellman equation
r= 0 r= 1
r= 1r= 1s1 s2
s3 s4
Figure 2.4: An example for demonstrating the Bellman equation. The policy in this example is deter-
ministic.
Consider the rst example shown in Figure 2.4, where the policy is deterministic. We
next write out the Bellman equation and then solve the state values from it.
First, consider state s1. Under the policy, the probabilities of taking the actions
are(a=a3js1) = 1 and (a6=a3js1) = 0. The state transition probabilities
arep(s0=s3js1;a3) = 1 and p(s06=s3js1;a3) = 0. The reward probabilities are
p(r= 0js1;a3) = 1 andp(r6= 0js1;a3) = 0. Substituting these values into (2.7) gives
v(s1) = 0 +
v(s3):
Interestingly, although the expression of the Bellman equation in (2.7) seems complex,
the expression for this specic state is very simple.
Similarly, it can be obtained that
v(s2) = 1 +
v(s4);
v(s3) = 1 +
v(s4);
v(s4) = 1 +
v(s4):
We can solve the state values from these equations. Since the equations are simple, we
can manually solve them. More complicated equations can be solved by the algorithms
presented in Section 2.7. Here, the state values can be solved as
v(s4) =1
1 
;
v(s3) =1
1 
;
v(s2) =1
1 
;
v(s1) =

1 
:
23

## 第37页

2.5. Examples for illustrating the Bellman equation
Furthermore, if we set 
= 0:9, then
v(s4) =1
1 0:9= 10;
v(s3) =1
1 0:9= 10;
v(s2) =1
1 0:9= 10;
v(s1) =0:9
1 0:9= 9:
p= 0.5
r=−1
r= 0
p= 0.5r= 1
r= 1r= 1s1 s2
s3 s4
Figure 2.5: An example for demonstrating the Bellman equation. The policy in this example is stochastic.
Consider the second example shown in Figure 2.5, where the policy is stochastic. We
next write out the Bellman equation and then solve the state values from it.
In states1, the probabilities of going right and down equal 0 :5. Mathematically, we
have(a=a2js1) = 0:5 and(a=a3js1) = 0:5. The state transition probability
is deterministic since p(s0=s3js1;a3) = 1 and p(s0=s2js1;a2) = 1. The reward
probability is also deterministic since p(r= 0js1;a3) = 1 andp(r= 1js1;a2) = 1.
Substituting these values into (2.7) gives
v(s1) = 0:5[0 +
v(s3)] + 0:5[ 1 +
v(s2)]:
Similarly, it can be obtained that
v(s2) = 1 +
v(s4);
v(s3) = 1 +
v(s4);
v(s4) = 1 +
v(s4):
The state values can be solved from the above equations. Since the equations are
24

## 第38页

2.6. Matrix-vector form of the Bellman equation
simple, we can solve the state values manually and obtain
v(s4) =1
1 
;
v(s3) =1
1 
;
v(s2) =1
1 
;
v(s1) = 0:5[0 +
v(s3)] + 0:5[ 1 +
v(s2)];
= 0:5 +

1 
:
Furthermore, if we set 
= 0:9, then
v(s4) = 10;
v(s3) = 10;
v(s2) = 10;
v(s1) = 0:5 + 9 = 8:5:
If we compare the state values of the two policies in the above examples, it can be
seen that
v1(si)v2(si); i= 1;2;3;4;
which indicates that the policy in Figure 2.4 is better because it has greater state values.
This mathematical conclusion is consistent with the intuition that the rst policy is better
because it can avoid entering the forbidden area when the agent starts from s1. As a
result, the above two examples demonstrate that state values can be used to evaluate
policies.
2.6 Matrix-vector form of the Bellman equation
The Bellman equation in (2.7) is in an elementwise form . Since it is valid for every state,
we can combine all these equations and write them concisely in a matrix-vector form ,
which will be frequently used to analyze the Bellman equation.
To derive the matrix-vector form, we rst rewrite the Bellman equation in (2.7) as
v(s) =r(s) +
X
s02Sp(s0js)v(s0); (2.8)
25

## 第39页

2.6. Matrix-vector form of the Bellman equation
where
r(s):=X
a2A(ajs)X
r2Rp(rjs;a)r;
p(s0js):=X
a2A(ajs)p(s0js;a):
Here,r(s) denotes the mean of the immediate rewards, and p(s0js) is the probability
of transitioning from stos0under policy .
Suppose that the states are indexed as siwithi= 1;:::;n , wheren=jSj. For state
si, (2.8) can be written as
v(si) =r(si) +
X
sj2Sp(sjjsi)v(sj): (2.9)
Letv= [v(s1);:::;v(sn)]T2Rn,r= [r(s1);:::;r(sn)]T2Rn, andP2Rnnwith
[P]ij=p(sjjsi). Then, (2.9) can be written in the following matrix-vector form:
v=r+
Pv; (2.10)
wherevis the unknown to be solved, and r;Pare known.
The matrix Phas some interesting properties. First, it is a nonnegative matrix,
meaning that all its elements are equal to or greater than zero. This property is denoted
asP0, where 0 denotes a zero matrix with appropriate dimensions. In this book, 
orrepresents an elementwise comparison operation. Second, Pis a stochastic matrix,
meaning that the sum of the values in every row is equal to one. This property is denoted
asP1=1, where 1= [1;:::; 1]Thas appropriate dimensions.
Consider the example shown in Figure 2.6. The matrix-vector form of the Bellman
equation is
2
6664v(s1)
v(s2)
v(s3)
v(s4)3
7775
|{z}
v=2
6664r(s1)
r(s2)
r(s3)
r(s4)3
7775
|{z}
r+
2
6664p(s1js1)p(s2js1)p(s3js1)p(s4js1)
p(s1js2)p(s2js2)p(s3js2)p(s4js2)
p(s1js3)p(s2js3)p(s3js3)p(s4js3)
p(s1js4)p(s2js4)p(s3js4)p(s4js4)3
7775
| {z }
P2
6664v(s1)
v(s2)
v(s3)
v(s4)3
7775
|{z}
v:
Substituting the specic values into the above equation gives
2
6664v(s1)
v(s2)
v(s3)
v(s4)3
7775=2
66640:5(0) + 0:5( 1)
1
1
13
7775+
2
66640 0:5 0:5 0
0 0 0 1
0 0 0 1
0 0 0 13
77752
6664v(s1)
v(s2)
v(s3)
v(s4)3
7775:
26

## 第40页

2.7. Solving state values from the Bellman equation
It can be seen that PsatisesP1=1.
p= 0.5
r=−1
r= 0
p= 0.5r= 1
r= 1r= 1s1 s2
s3 s4
Figure 2.6: An example for demonstrating the matrix-vector form of the Bellman equation.
2.7 Solving state values from the Bellman equation
Calculating the state values of a given policy is a fundamental problem in reinforcement
learning. This problem is often referred to as policy evaluation . In this section, we present
two methods for calculating state values from the Bellman equation.
2.7.1 Closed-form solution
Sincev=r+
Pvis a simple linear equation, its closed-form solution can be easily
obtained as
v= (I 
P) 1r:
Some properties of ( I 
P) 1are given below.
I 
Pis invertible. The proof is as follows. According to the Gershgorin circle
theorem [4], every eigenvalue of I 
Plies within at least one of the Gershgorin
circles. The ith Gershgorin circle has a center at [ I 
P]ii= 1 
p(sijsi) and
a radius equal toP
j6=i[I 
P]ij=P
j6=i
p(sjjsi). Since
 < 1, we know that
the radius is less than the magnitude of the center:P
j6=i
p(sjjsi)<1 
p(sijsi).
Therefore, all Gershgorin circles do not encircle the origin, and hence no eigenvalue
ofI 
Pis zero.
(I 
P) 1I, meaning that every element of ( I 
P) 1is nonnegative and,
more specically, no less than that of the identity matrix. This is because Phas
nonnegative entries, and hence ( I 
P) 1=I+
P+
2P2
+I0.
For any vector r0, it holds that ( I 
P) 1rr0. This property follows from
the second property because [( I 
P) 1 I]r0. As a consequence, if r1r2, we
have (I 
P) 1r1(I 
P) 1r2.
27

## 第41页

2.7. Solving state values from the Bellman equation
2.7.2 Iterative solution
Although the closed-form solution is useful for theoretical analysis purposes, it is not
applicable in practice because it involves a matrix inversion operation, which still needs
to be calculated by other numerical algorithms. In fact, we can directly solve the Bellman
equation using the following iterative algorithm:
vk+1=r+
Pvk; k = 0;1;2;::: (2.11)
This algorithm generates a sequence of values fv0;v1;v2;:::g, wherev02Rnis an initial
guess ofv. It holds that
vk!v= (I 
P) 1r;ask!1: (2.12)
Interested readers may see the proof in Box 2.1.
Box 2.1: Convergence proof of (2.12)
Dene the error as k=vk v. We only need to show that k!0. Substituting
vk+1=k+1+vandvk=k+vintovk+1=r+
Pvkgives
k+1+v=r+
P(k+v);
which can be rewritten as
k+1= v+r+
Pk+
Pv;
=
Pk v+ (r+
Pv);
=
Pk:
As a result,
k+1=
Pk=
2P2
k 1==
k+1Pk+1
0:
Since every entry of Pis nonnegative and no greater than one, we have that 0 
Pk
1 for anyk. That is, every entry of Pk
is no greater than 1. On the other hand,
since
 <1, we know that 
k!0, and hence k+1=
k+1Pk+1
0!0 ask!1 .
2.7.3 Illustrative examples
We next apply the algorithm in (2.11) to solve the state values of some examples.
The examples are shown in Figure 2.7. The orange cells represent forbidden areas.
The blue cell represents the target area. The reward settings are rboundary =rforbidden = 1
28

## 第42页

2.7. Solving state values from the Bellman equation
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
53.5 3.9 4.3 4.8 5.3
3.1 3.5 4.8 5.3 5.9
2.8 2.5 10.0 5.9 6.6
2.5 10.0 10.0 10.0 7.3
2.3 9.0 10.0 9.0 8.1
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
53.5 3.9 4.3 4.8 5.3
3.1 3.5 4.8 5.3 5.9
2.8 2.5 10.0 5.9 6.6
2.5 10.0 10.0 10.0 7.3
2.3 9.0 10.0 9.0 8.1
(a) Two \good" policies and their state values. The state values of the two policies are the same,
but the two policies are dierent at the top two states in the fourth column.
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
5-6.6 -7.3 -8.1 -9.0 -10.0
-8.5 -8.3 -8.1 -9.0 -10.0
-7.5 -8.3 -8.1 -9.0 -10.0
-7.5 -7.2 -9.1 -9.0 -10.0
-7.6 -7.3 -8.1 -9.0 -10.0
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
50.0 0.0 0.0 -10.0 -10.0
-9.0 -10.0 -0.4 -0.5 -10.0
-10.0 -0.5 0.5 -0.5 0.0
0.0 -1.0 -0.5 -0.5 -10.0
0.0 0.0 0.0 0.0 0.0
(b) Two \bad" policies and their state values. The state values are smaller than those of the
\good" policies.
Figure 2.7: Examples of policies and their corresponding state values.
andrtarget = 1. Here, the discount rate is 
= 0:9.
29

## 第43页

2.8. From state value to action value
Figure 2.7(a) shows two \good" policies and their corresponding state values obtained
by (2.11). The two policies have the same state values but dier at the top two states in
the fourth column. Therefore, we know that dierent policies may have the same state
values.
Figure 2.7(b) shows two \bad" policies and their corresponding state values. These
two policies are bad because the actions of many states are intuitively unreasonable.
Such intuition is supported by the obtained state values. As can be seen, the state values
of these two policies are negative and much smaller than those of the good policies in
Figure 2.7(a).
2.8 From state value to action value
While we have been discussing state values thus far in this chapter, we now turn to
theaction value , which indicates the \value" of taking an action at a state. While the
concept of action value is important, the reason why it is introduced in the last section
of this chapter is that it heavily relies on the concept of state values. It is important to
understand state values well rst before studying action values.
The action value of a state-action pair ( s;a) is dened as
q(s;a):=E[GtjSt=s;At=a]:
As can be seen, the action value is dened as the expected return that can be obtained
after taking an action at a state. It must be noted that q(s;a) depends on a state-action
pair (s;a) rather than an action alone. It may be more rigorous to call this value a
state-action value, but it is conventionally called an action value for simplicity.
What is the relationship between action values and state values?
First, it follows from the properties of conditional expectation that
E[GtjSt=s]|{z}
v(s)=X
a2AE[GtjSt=s;At=a]|{z}
q(s;a)(ajs):
It then follows that
v(s) =X
a2A(ajs)q(s;a): (2.13)
As a result, a state value is the expectation of the action values associated with that
state.
Second, since the state value is given by
v(s) =X
a2A(ajs)hX
r2Rp(rjs;a)r+
X
s02Sp(s0js;a)v(s0)i
;
30

## 第44页

2.8. From state value to action value
comparing it with (2.13) leads to
q(s;a) =X
r2Rp(rjs;a)r+
X
s02Sp(s0js;a)v(s0): (2.14)
It can be seen that the action value consists of two terms. The rst term is the mean
of the immediate rewards, and the second term is the mean of the future rewards.
Both (2.13) and (2.14) describe the relationship between state values and action val-
ues. They are the two sides of the same coin: (2.13) shows how to obtain state values
from action values, whereas (2.14) shows how to obtain action values from state values.
2.8.1 Illustrative examples
p= 0.5
r=−1
r= 0
p= 0.5r= 1
r= 1r= 1s1 s2
s3 s4
Figure 2.8: An example for demonstrating the process of calculating action values.
We next present an example to illustrate the process of calculating action values and
discuss a common mistake that beginners may make.
Consider the stochastic policy shown in Figure 2.8. We next only examine the actions
ofs1. The other states can be examined similarly. The action value of ( s1;a2) is
q(s1;a2) = 1 +
v(s2);
wheres2is the next state. Similarly, it can be obtained that
q(s1;a3) = 0 +
v(s3):
A common mistake that beginners may make is about the values of the actions that
the given policy does not select. For example, the policy in Figure 2.8 can only select
a2ora3and cannot select a1;a4;a5. One may argue that since the policy does not
selecta1;a4;a5, we do not need to calculate their action values, or we can simply set
q(s1;a1) =q(s1;a4) =q(s1;a5) = 0. This is wrong.
First, even if an action would not be selected by a policy, it still has an action value.
In this example, although policy does not take a1ats1, we can still calculate its
31

## 第45页

2.8. From state value to action value
action value by observing what we would obtain after taking this action. Specically,
after taking a1, the agent is bounced back to s1(hence, the immediate reward is  1)
and then continues moving in the state space starting from s1by following (hence,
the future reward is 
v(s1)). As a result, the action value of ( s1;a1) is
q(s1;a1) = 1 +
v(s1):
Similarly, for a4anda5, which cannot be possibly selected by the given policy either,
we have
q(s1;a4) = 1 +
v(s1);
q(s1;a5) = 0 +
v(s1):
Second, why do we care about the actions that the given policy would not select?
Although some actions cannot be possibly selected by a given policy, this does not
mean that these actions are not good. It is possible that the given policy is not good,
so it cannot select the best action. The purpose of reinforcement learning is to nd
optimal policies. To that end, we must keep exploring all actions to determine better
actions for each state.
Finally, after computing the action values, we can also calculate the state value ac-
cording to (2.13):
v(s1) = 0:5q(s1;a2) + 0:5q(s1;a3);
= 0:5[0 +
v(s3)] + 0:5[ 1 +
v(s2)]:
2.8.2 The Bellman equation in terms of action values
The Bellman equation that we previously introduced was dened based on state values.
In fact, it can also be expressed in terms of action values.
In particular, substituting (2.13) into (2.14) yields
q(s;a) =X
r2Rp(rjs;a)r+
X
s02Sp(s0js;a)X
a02A(s0)(a0js0)q(s0;a0);
which is an equation of action values. The above equation is valid for every state-action
pair. If we put all these equations together, their matrix-vector form is
q= ~r+
Pq; (2.15)
whereqis the action value vector indexed by the state-action pairs: its ( s;a)th element
is [q](s;a)=q(s;a). ~ris the immediate reward vector indexed by the state-action
pairs: [~r](s;a)=P
r2Rp(rjs;a)r:The matrix Pis the probability transition matrix, whose
32

## 第46页

2.9. Summary
row is indexed by the state-action pairs and whose column is indexed by the states:
[P](s;a);s0=p(s0js;a). Moreover,  is a block diagonal matrix in which each block is a
1jAj vector:  s0;(s0;a0)=(a0js0) and the other entries of  are zero.
Compared to the Bellman equation dened in terms of state values, the equation
dened in terms of action values has some unique features. For example, ~ randPare
independent of the policy and are merely determined by the system model. The policy
is embedded in . It can be veried that (2.15) is also a contraction mapping and has a
unique solution that can be iteratively solved. More details can be found in [5].
2.9 Summary
The most important concept introduced in this chapter is the state value. Mathematically,
a state value is the expected return that the agent can obtain by starting from a state.
The values of dierent states are related to each other. That is, the value of state s
relies on the values of some other states, which may further rely on the value of state s
itself. This phenomenon might be the most confusing part of this chapter for beginners.
It is related to an important concept called bootstrapping, which involves calculating
something from itself. Although bootstrapping may be intuitively confusing, it is clear if
we examine the matrix-vector form of the Bellman equation. In particular, the Bellman
equation is a set of linear equations that describe the relationships between the values of
all states.
Since state values can be used to evaluate whether a policy is good or not, the process
of solving the state values of a policy from the Bellman equation is called policy evalu-
ation. As we will see later in this book, policy evaluation is an important step in many
reinforcement learning algorithms.
Another important concept, action value, was introduced to describe the value of
taking one action at a state. As we will see later in this book, action values play a
more direct role than state values when we attempt to nd optimal policies. Finally, the
Bellman equation is not restricted to the reinforcement learning eld. Instead, it widely
exists in many elds such as control theories and operation research. In dierent elds,
the Bellman equation may have dierent expressions. In this book, the Bellman equation
is studied under discrete Markov decision processes. More information about this topic
can be found in [2].
2.10 Q&A
Q: What is the relationship between state values and returns?
A: The value of a state is the mean of the returns that can be obtained if the agent
starts from that state.
33

## 第47页

2.10. Q&A
Q: Why do we care about state values?
A: State values can be used to evaluate policies. In fact, optimal policies are dened
based on state values. This point will become clearer in the next chapter.
Q: Why do we care about the Bellman equation?
A: The Bellman equation describes the relationships among the values of all states.
It is the tool for analyzing state values.
Q: Why is the process of solving the Bellman equation called policy evaluation?
A: Solving the Bellman equation yields state values. Since state values can be used to
evaluate a policy, solving the Bellman equation can be interpreted as evaluating the
corresponding policy.
Q: Why do we need to study the matrix-vector form of the Bellman equation?
A: The Bellman equation refers to a set of linear equations established for all the
states. To solve state values, we must put all the linear equations together. The
matrix-vector form is a concise expression of these linear equations.
Q: What is the relationship between state values and action values?
A: On the one hand, a state value is the mean of the action values for that state. On
the other hand, an action value relies on the values of the next states that the agent
may transition to after taking the action.
Q: Why do we care about the values of the actions that a given policy cannot select?
A: Although a given policy cannot select some actions, this does not mean that these
actions are not good. On the contrary, it is possible that the given policy is not good
and misses the best action. To nd better policies, we must keep exploring dierent
actions even though some of them may not be selected by the given policy.
34

## 第48页

Chapter 3
Optimal State Values and Bellman
Optimality Equation
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
Figure 3.1: Where we are in this book.
The ultimate goal of reinforcement learning is to seek optimal policies . It is, therefore,
necessary to dene what optimal policies are. In this chapter, we introduce a core concept
and an important tool . The core concept is the optimal state value , based on which we
can dene optimal policies . The important tool is the Bellman optimality equation , from
which we can solve the optimal state values and policies.
The relationship between the previous, present, and subsequent chapters is as follows.
The previous chapter (Chapter 2) introduced the Bellman equation of any given policy.
35

## 第49页

3.1. Motivating example: How to improve policies?
The present chapter introduces the Bellman optimality equation, which is a special Bell-
man equation whose corresponding policy is optimal. The next chapter (Chapter 4) will
introduce an important algorithm called value iteration, which is exactly the algorithm
for solving the Bellman optimality equation as introduced in the present chapter.
Be prepared that this chapter is slightly mathematically intensive. However, it is
worth it because many fundamental questions can be clearly answered.
3.1 Motivating example: How to improve policies?
r=−1r= 1
r= 1r= 1s1 s2
s3 s4
Figure 3.2: An example for demonstrating policy improvement.
Consider the policy shown in Figure 3.2. Here, the orange and blue cells represent the
forbidden and target areas, respectively. The policy here is not good because it selects a2
(rightward) in state s1. How can we improve the given policy to obtain a better policy?
The answer lies in state values and action values.
Intuition: It is intuitively clear that the policy can improve if it selects a3(downward)
instead ofa2(rightward) at s1. This is because moving downward enables the agent
to avoid entering the forbidden area.
Mathematics: The above intuition can be realized based on the calculation of state
values and action values.
First, we calculate the state values of the given policy. In particular, the Bellman
equation of this policy is
v(s1) = 1 +
v(s2);
v(s2) = +1 +
v(s4);
v(s3) = +1 +
v(s4);
v(s4) = +1 +
v(s4):
36

## 第50页

3.2. Optimal state values and optimal policies
Let
= 0:9. It can be easily solved that
v(s4) =v(s3) =v(s2) = 10;
v(s1) = 8:
Second, we calculate the action values for state s1:
q(s1;a1) = 1 +
v(s1) = 6:2;
q(s1;a2) = 1 +
v(s2) = 8;
q(s1;a3) = 0 +
v(s3) = 9;
q(s1;a4) = 1 +
v(s1) = 6:2;
q(s1;a5) = 0 +
v(s1) = 7:2:
It is notable that action a3has the greatest action value:
q(s1;a3)q(s1;ai);for alli6= 3:
Therefore, we can update the policy to select a3ats1.
This example illustrates that we can obtain a better policy if we update the poli-
cy to select the action with the greatest action value . This is the basic idea of many
reinforcement learning algorithms.
This example is very simple in the sense that the given policy is only not good for
states1. If the policy is also not good for the other states, will selecting the action with
the greatest action value still generate a better policy? Moreover, whether there always
exist optimal policies? What does an optimal policy look like? We will answer all of
these questions in this chapter.
3.2 Optimal state values and optimal policies
While the ultimate goal of reinforcement learning is to obtain optimal policies, it is
necessary to rst dene what an optimal policy is. The denition is based on state
values. In particular, consider two given policies 1and2. If the state value of 1is
greater than or equal to that of 2for any state:
v1(s)v2(s);for alls2S;
then1is said to be better than 2. Furthermore, if a policy is better than all the other
possible policies, then this policy is optimal. This is formally stated below.
37

## 第51页

3.3. Bellman optimality equation
Denition 3.1 (Optimal policy and optimal state value) .A policyis optimal if
v(s)v(s)for alls2S and for any other policy . The state values of are the
optimal state values.
The above denition indicates that an optimal policy has the greatest state value
for every state compared to all the other policies. This denition also leads to many
questions:
Existence: Does the optimal policy exist?
Uniqueness: Is the optimal policy unique?
Stochasticity: Is the optimal policy stochastic or deterministic?
Algorithm: How to obtain the optimal policy and the optimal state values?
These fundamental questions must be clearly answered to thoroughly understand
optimal policies. For example, regarding the existence of optimal policies, if optimal
policies do not exist, then we do not need to bother to design algorithms to nd them.
We will answer all these questions in the remainder of this chapter.
3.3 Bellman optimality equation
The tool for analyzing optimal policies and optimal state values is the Bellman optimality
equation (BOE). By solving this equation, we can obtain optimal policies and optimal
state values. We next present the expression of the BOE and then analyze it in detail.
For everys2S, the elementwise expression of the BOE is
v(s) = max
(s)2(s)X
a2A(ajs) X
r2Rp(rjs;a)r+
X
s02Sp(s0js;a)v(s0)!
= max
(s)2(s)X
a2A(ajs)q(s;a); (3.1)
wherev(s);v(s0) are unknown variables to be solved and
q(s;a):=X
r2Rp(rjs;a)r+
X
s02Sp(s0js;a)v(s0):
Here,(s) denotes a policy for state s, and (s) is the set of all possible policies for s.
The BOE is an elegant and powerful tool for analyzing optimal policies. However,
it may be nontrivial to understand this equation. For example, this equation has two
unknown variables v(s) and(ajs). It may be confusing to beginners how to solve two
unknown variables from one equation. Moreover, the BOE is actually a special Bellman
equation. However, it is nontrivial to see that since its expression is quite dierent from
that of the Bellman equation. We also need to answer the following fundamental questions
about the BOE.
38

## 第52页

3.3. Bellman optimality equation
Existence: Does this equation have a solution?
Uniqueness: Is the solution unique?
Algorithm: How to solve this equation?
Optimality: How is the solution related to optimal policies?
Once we can answer these questions, we will clearly understand optimal state values and
optimal policies.
3.3.1 Maximization of the right-hand side of the BOE
We next clarify how to solve the maximization problem on the right-hand side of the
BOE in (3.1). At rst glance, it may be confusing to beginners how to solve twounknown
variablesv(s) and(ajs) from oneequation. In fact, these two unknown variables can
be solved one by one. This idea is illustrated by the following example.
Example 3.1. Consider two unknown variables x;y2Rthat satisfy
x= max
y2R(2x 1 y2):
The rst step is to solve yon the right-hand side of the equation. Regardless of the value
ofx, we always have maxy(2x 1 y2) = 2x 1, where the maximum is achieved when
y= 0. The second step is to solve x. Wheny= 0, the equation becomes x= 2x 1,
which leads to x= 1. Therefore, y= 0 andx= 1 are the solutions of the equation.
We now turn to the maximization problem on the right-hand side of the BOE. The
BOE in (3.1) can be written concisely as
v(s) = max
(s)2(s)X
a2A(ajs)q(s;a); s2S:
Inspired by Example 3.1, we can rst solve the optimal on the right-hand side. How to
do that? The following example demonstrates its basic idea.
Example 3.2. Givenq1;q2;q32R, we would like to nd the optimal values of c1;c2;c3
to maximize
3X
i=1ciqi=c1q1+c2q2+c3q3;
wherec1+c2+c3= 1 andc1;c2;c30.
Without loss of generality, suppose that q3q1;q2. Then, the optimal solution is
c
3= 1 andc
1=c
2= 0. This is because
q3= (c1+c2+c3)q3=c1q3+c2q3+c3q3c1q1+c2q2+c3q3
for anyc1;c2;c3.
39

## 第53页

3.3. Bellman optimality equation
Inspired by the above example, sinceP
a(ajs) = 1, we have
X
a2A(ajs)q(s;a)X
a2A(ajs) max
a2Aq(s;a) = max
a2Aq(s;a);
where equality is achieved when
(ajs) =(
1; a=a;
0; a6=a:
Here,a= arg max aq(s;a). In summary, the optimal policy (s) is the one that selects
the action that has the greatest value of q(s;a).
3.3.2 Matrix-vector form of the BOE
The BOE refers to a set of equations dened for all states. If we combine these equations,
we can obtain a concise matrix-vector form, which will be extensively used in this chapter.
The matrix-vector form of the BOE is
v= max
2(r+
Pv); (3.2)
wherev2RjSjand max is performed in an elementwise manner. The structures of r
andPare the same as those in the matrix-vector form of the normal Bellman equation:
[r]s:=X
a2A(ajs)X
r2Rp(rjs;a)r; [P]s;s0=p(s0js):=X
a2A(ajs)p(s0js;a):
Since the optimal value of is determined by v, the right-hand side of (3.2) is a function
ofv, denoted as
f(v):= max
2(r+
Pv):
Then, the BOE can be expressed in a concise form as
v=f(v): (3.3)
In the remainder of this section, we show how to solve this nonlinear equation.
3.3.3 Contraction mapping theorem
Since the BOE can be expressed as a nonlinear equation v=f(v), we next introduce
the contraction mapping theorem [6] to analyze it. The contraction mapping theorem is
a powerful tool for analyzing general nonlinear equations. It is also known as the xed-
point theorem. Readers who already know this theorem can skip this part. Otherwise,
the reader is advised to be familiar with this theorem since it is the key to analyzing the
40

## 第54页

3.3. Bellman optimality equation
BOE.
Consider a function f(x), wherex2Rdandf:Rd!Rd. A pointxis called a xed
point if
f(x) =x:
The interpretation of the above equation is that the map of xis itself. This is the
reason why xis called \xed". The function fis acontraction mapping (or contractive
function) if there exists 
2(0;1) such that
kf(x1) f(x2)k
kx1 x2k
for anyx1;x22Rd. In this book,kk denotes a vector or matrix norm.
Example 3.3. We present three examples to demonstrate xed points and contraction
mappings.
x=f(x) = 0:5x,x2R.
It is easy to verify that x= 0is a xed point since 0 = 0:50. Moreover, f(x) = 0:5x
is a contraction mapping because k0:5x1 0:5x2k= 0:5kx1 x2k
kx1 x2kfor
any
2[0:5;1).
x=f(x) =Ax, wherex2Rn;A2RnnandkAk
 <1.
It is easy to verify that x= 0 is a xed point since 0 =A0. To see the contraction
property,kAx1 Ax2k=kA(x1 x2)kkAkkx1 x2k
kx1 x2k. Therefore,
f(x) =Axis a contraction mapping.
x=f(x) = 0:5 sinx,x2R.
It is easy to see that x= 0 is a xed point since 0 = 0:5 sin 0 . Moreover, it follows
from the mean value theorem [7, 8] that
0:5 sinx1 0:5 sinx2
x1 x2=j0:5 cosx3j0:5; x 32[x1;x2]:
As a result,j0:5 sinx1 0:5 sinx2j0:5jx1 x2jand hence f(x) = 0:5 sinxis a
contraction mapping.
The relationship between a xed point and the contraction property is characterized
by the following classic theorem.
Theorem 3.1 (Contraction mapping theorem) .For any equation that has the form x=
f(x)wherexandf(x)are real vectors, if fis a contraction mapping, then the following
properties hold.
Existence: There exists a xed point xsatisfyingf(x) =x.
41

## 第55页

3.3. Bellman optimality equation
Uniqueness: The xed point xis unique.
Algorithm: Consider the iterative process:
xk+1=f(xk);
wherek= 0;1;2;:::. Then,xk!xask!1 for any initial guess x0. Moreover,
the convergence rate is exponentially fast.
The contraction mapping theorem not only can tell whether the solution of a nonlinear
equation exists but also suggests a numerical algorithm for solving the equation. The
proof of the theorem is given in Box 3.1.
The following example demonstrates how to calculate the xed points of some equa-
tions using the iterative algorithm suggested by the contraction mapping theorem.
Example 3.4. Let us revisit the abovementioned examples: x= 0:5x,x=Ax, and
x= 0:5 sinx. While it has been shown that the right-hand sides of these three equations
are all contraction mappings, it follows from the contraction mapping theorem that they
each have a unique xed point, which can be easily veried to be x= 0. Moreover, the
xed points of the three equations can be iteratively solved by the following algorithms:
xk+1= 0:5xk;
xk+1=Axk;
xk+1= 0:5 sinxk;
given any initial guess x0.
Box 3.1: Proof of the contraction mapping theorem
Part 1: We prove that the sequence fxkg1
k=1withxk=f(xk 1)is convergent.
The proof relies on Cauchy sequences . A sequence x1;x2;::: is called Cauchy
if for any small " >0, there exists Nsuch thatkxm xnk< "for allm;n > N .
The intuitive interpretation is that there exists a nite integer Nsuch that all the
elements after Nare suciently close to each other. Cauchy sequences are important
because it is guaranteed that a Cauchy sequence converges to a limit. Its convergence
property will be used to prove the contraction mapping theorem. Note that we must
havekxm xnk< " for allm;n > N . If we simply have xn+1 xn!0, it is
insucient to claim that the sequence is a Cauchy sequence. For example, it holds
thatxn+1 xn!0 forxn=pn, but apparently, xn=pndiverges.
We next show that fxk=f(xk 1)g1
k=1is a Cauchy sequence and hence converges.
42

## 第56页

3.3. Bellman optimality equation
First, since fis a contraction mapping, we have
kxk+1 xkk=kf(xk) f(xk 1)k
kxk xk 1k:
Similarly, we have kxk xk 1k
kxk 1 xk 2k, . . . ,kx2 x1k
kx1 x0k. Thus,
we have
kxk+1 xkk
kxk xk 1k

2kxk 1 xk 2k
...

kkx1 x0k:
Since
 <1, we know thatkxk+1 xkkconverges to zero exponentially fast as k!1
given anyx1;x0. Notably, the convergence of fkxk+1 xkkgis not sucient for
implying the convergence of fxkg. Therefore, we need to further consider kxm xnk
for anym>n . In particular,
kxm xnk=kxm xm 1+xm 1  xn+1+xn+1 xnk
kxm xm 1k++kxn+1 xnk

m 1kx1 x0k++
nkx1 x0k
=
n(
m 1 n++ 1)kx1 x0k

n(1 ++
m 1 n+
m n+
m n+1+:::)kx1 x0k
=
n
1 
kx1 x0k: (3.4)
As a result, for any ", we can always nd Nsuch thatkxm xnk<"for allm;n>N .
Therefore, this sequence is Cauchy and hence converges to a limit point denoted as
x= limk!1xk.
Part 2: We show that the limit x= limk!1xkis a xed point. To do that, since
kf(xk) xkk=kxk+1 xkk
kkx1 x0k;
we know thatkf(xk) xkkconverges to zero exponentially fast. Hence, we have
f(x) =xat the limit.
Part 3: We show that the xed point is unique. Suppose that there is another
xed point x0satisfyingf(x0) =x0. Then,
kx0 xk=kf(x0) f(x)k
kx0 xk:
43

## 第57页

3.3. Bellman optimality equation
Since
 <1, this inequality holds if and only if kx0 xk= 0. Therefore, x0=x.
Part 4: We show that xkconverges to xexponentially fast. Recall thatkxm 
xnk
n
1 
kx1 x0k, as proven in (3.4). Since mcan be arbitrarily large, we have
kx xnk= lim
m!1kxm xnk
n
1 
kx1 x0k:
Since
 <1, the error converges to zero exponentially fast as n!1 .
3.3.4 Contraction property of the right-hand side of the BOE
We next show that f(v) in the BOE in (3.3) is a contraction mapping. Thus, the con-
traction mapping theorem introduced in the previous subsection can be applied.
Theorem 3.2 (Contraction property of f(v)).The function f(v)on the right-hand side
of the BOE in (3.3) is a contraction mapping. In particular, for any v1;v22RjSj, it holds
that
kf(v1) f(v2)k1
kv1 v2k1;
where
2(0;1)is the discount rate, and kk1is the maximum norm, which is the
maximum absolute value of the elements of a vector.
The proof of the theorem is given in Box 3.2. This theorem is important because we
can use the powerful contraction mapping theorem to analyze the BOE.
Box 3.2: Proof of Theorem 3.2
Consider any two vectors v1;v22RjSj, and suppose that 
1:= arg max (r+
Pv1)
and
2:= arg max (r+
Pv2). Then,
f(v1) = max
(r+
Pv1) =r
1+
P
1v1r
2+
P
2v1;
f(v2) = max
(r+
Pv2) =r
2+
P
2v2r
1+
P
1v2;
whereis an elementwise comparison. As a result,
f(v1) f(v2) =r
1+
P
1v1 (r
2+
P
2v2)
r
1+
P
1v1 (r
1+
P
1v2)
=
P
1(v1 v2):
44

## 第58页

3.3. Bellman optimality equation
Similarly, it can be shown that f(v2) f(v1)
P
2(v2 v1). Therefore,

P
2(v1 v2)f(v1) f(v2)
P
1(v1 v2):
Dene
z:= max
j
P
2(v1 v2)j;j
P
1(v1 v2)j	
2RjSj;
where max(),jj, andare all elementwise operators. By denition, z0. On the
one hand, it is easy to see that
 z
P
2(v1 v2)f(v1) f(v2)
P
1(v1 v2)z;
which implies
jf(v1) f(v2)jz:
It then follows that
kf(v1) f(v2)k1kzk1; (3.5)
wherekk1is the maximum norm.
On the other hand, suppose that ziis theith entry of z, andpT
iandqT
iare the
ith row ofP
1andP
2, respectively. Then,
zi= maxf
jpT
i(v1 v2)j;
jqT
i(v1 v2)jg:
Sincepiis a vector with all nonnegative elements and the sum of the elements is
equal to one, it follows that
jpT
i(v1 v2)jpT
ijv1 v2jkv1 v2k1:
Similarly, we have jqT
i(v1 v2)jkv1 v2k1. Therefore, zi
kv1 v2k1and hence
kzk1= max
ijzij
kv1 v2k1:
Substituting this inequality to (3.5) gives
kf(v1) f(v2)k1
kv1 v2k1;
which concludes the proof of the contraction property of f(v).
45

## 第59页

3.4. Solving an optimal policy from the BOE
3.4 Solving an optimal policy from the BOE
With the preparation in the last section, we are ready to solve the BOE to obtain the
optimal state value vand an optimal policy .
Solvingv: Ifvis a solution of the BOE, then it satises
v= max
2(r+
Pv):
Clearly,vis a xed point because v=f(v). Then, the contraction mapping
theorem suggests the following results.
Theorem 3.3 (Existence, uniqueness, and algorithm) .For the BOE v=f(v) =
max2(r+
Pv), there always exists a unique solution v, which can be solved
iteratively by
vk+1=f(vk) = max
2(r+
Pvk); k = 0;1;2;::::
The value of vkconverges to vexponentially fast as k!1 given any initial guess
v0.
The proof of this theorem directly follows from the contraction mapping theorem since
f(v) is a contraction mapping. This theorem is important because it answers some
fundamental questions.
- Existence of v: The solution of the BOE always exists.
- Uniqueness of v: The solution vis always unique.
- Algorithm for solving v: The value of vcan be solved by the iterative algorithm
suggested by Theorem 3.3. This iterative algorithm has a specic name called
value iteration . Its implementation will be introduced in detail in Chapter 4. We
mainly focus on the fundamental properties of the BOE in the present chapter.
Solving: Once the value of vhas been obtained, we can easily obtain by solving
= arg max
2(r+
Pv): (3.6)
The value of will be given in Theorem 3.5. Substituting (3.6) into the BOE yields
v=r+
Pv:
Therefore,v=vis the state value of , and the BOE is a special Bellman equation
whose corresponding policy is .
46

## 第60页

3.4. Solving an optimal policy from the BOE
At this point, although we can solve vand, it is still unclear whether the solution
is optimal. The following theorem reveals the optimality of the solution.
Theorem 3.4 (Optimality of vand).The solution vis the optimal state value, and
is an optimal policy. That is, for any policy , it holds that
v=vv;
wherevis the state value of , andis an elementwise comparison.
Now, it is clear why we must study the BOE: its solution corresponds to optimal state
values and optimal policies. The proof of the above theorem is given in the following box.
Box 3.3: Proof of Theorem 3.4
For any policy , it holds that
v=r+
Pv:
Since
v= max
(r+
Pv) =r+
Pvr+
Pv;
we have
v v(r+
Pv) (r+
Pv) =
P(v v):
Repeatedly applying the above inequality gives v v
P(v v)
2P2
(v 
v)
nPn
(v v). It follows that
v vlim
n!1
nPn
(v v) = 0;
where the last equality is true because 
 <1 andPn
is a nonnegative matrix with
all its elements less than or equal to 1 (because Pn
1=1). Therefore, vvfor
any.
We next examine in (3.6) more closely. In particular, the following theorem shows
that there always exists a deterministic greedy policy that is optimal.
Theorem 3.5 (Greedy optimal policy) .For anys2S, the deterministic greedy policy
(ajs) =(
1; a=a(s);
0; a6=a(s);(3.7)
47

## 第61页

3.4. Solving an optimal policy from the BOE
is an optimal policy for solving the BOE. Here,
a(s) = arg max
aq(a;s);
where
q(s;a):=X
r2Rp(rjs;a)r+
X
s02Sp(s0js;a)v(s0):
Box 3.4: Proof of Theorem 3.5
While the matrix-vector form of the optimal policy is = arg max (r+
Pv), its
elementwise form is
(s) = arg max
2X
a2A(ajs) X
r2Rp(rjs;a)r+
X
s02Sp(s0js;a)v(s0)!
| {z }
q(s;a); s2S:
It is clear thatP
a2A(ajs)q(s;a) is maximized if (s) selects the action with the
greatestq(s;a).
The policy in (3.7) is called greedy because it seeks the actions with the greatest
q(s;a). Finally, we discuss two important properties of .
Uniqueness of optimal policies: Although the value of vis unique, the optimal policy
that corresponds to vmay not be unique. This can be easily veried by counterex-
amples. For example, the two policies shown in Figure 3.3 are both optimal.
Stochasticity of optimal policies: An optimal policy can be either stochastic or de-
terministic, as demonstrated in Figure 3.3. However, it is certain that there always
exists a deterministic optimal policy according to Theorem 3.5.
p= 0.5
p= 0.5
Figure 3.3: Examples for demonstrating that optimal policies may not be unique. The two policies are
dierent but are both optimal.
48

## 第62页

3.5. Factors that in
uence optimal policies
3.5 Factors that in
uence optimal policies
The BOE is a powerful tool for analyzing optimal policies. We next apply the BOE to
study what factors can in
uence optimal policies. This question can be easily answered
by observing the elementwise expression of the BOE:
v(s) = max
(s)2(s)X
a2A(ajs) X
r2Rp(rjs;a)r+
X
s02Sp(s0js;a)v(s0)!
; s2S:
The optimal state value and optimal policy are determined by the following param-
eters: 1) the immediate reward r, 2) the discount rate 
, and 3) the system model
p(s0js;a);p(rjs;a). While the system model is xed, we next discuss how the optimal
policy varies when we change the values of rand
. All the optimal policies presented
in this section can be obtained via the algorithm in Theorem 3.3. The implementation
details of the algorithm will be given in Chapter 4. The present chapter mainly focuses
on the fundamental properties of optimal policies.
A baseline example
Consider the example in Figure 3.4. The reward settings are rboundary =rforbidden = 1
andrtarget = 1. In addition, the agent receives a reward of rother= 0 for every movement
step. The discount rate is selected as 
= 0:9.
With the above parameters, the optimal policy and optimal state values are given in
Figure 3.4(a). It is interesting that the agent is not afraid of passing through forbidden
areas to reach the target area. More specically, starting from the state at (row=4,
column=1), the agent has two options for reaching the target area. The rst option is to
avoid all the forbidden areas and travel a long distance to the target area. The second
option is to pass through forbidden areas. Although the agent obtains negative rewards
when entering forbidden areas, the cumulative reward of the second trajectory is greater
than that of the rst trajectory. Therefore, the optimal policy is far-sighted due to the
relatively large value of 
.
Impact of the discount rate
If we change the discount rate from 
= 0:9 to
= 0:5 and keep other parameters
unchanged, the optimal policy becomes the one shown in Figure 3.4(b). It is interesting
that the agent does not dare to take risks anymore. Instead, it would travel a long
distance to reach the target while avoiding all the forbidden areas. This is because the
optimal policy becomes short-sighted due to the relatively small value of 
.
In the extreme case where 
= 0, the corresponding optimal policy is shown in
Figure 3.4(c). In this case, the agent is not able to reach the target area. This is
49

## 第63页

3.5. Factors that in
uence optimal policies
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
55.8 5.6 6.2 6.5 5.8
6.5 7.2 8.0 7.2 6.5
7.2 8.0 10.0 8.0 7.2
8.0 10.0 10.0 10.0 8.0
7.2 9.0 10.0 9.0 8.1
(a) Baseline example: rboundary =rforbidden = 1,rtarget = 1,
= 0:9.
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
50.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.1
0.0 0.0 2.0 0.1 0.1
0.0 2.0 2.0 2.0 0.2
0.0 1.0 2.0 1.0 0.5
(b) The discount rate is changed to 
= 0:5. The other parameters are the same as those in (a).
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
50.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 1.0 0.0 0.0
0.0 1.0 1.0 1.0 0.0
0.0 0.0 1.0 0.0 0.0
(c) The discount rate is changed to 
= 0. The other parameters are the same as those in (a).
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
53.5 3.9 4.3 4.8 5.3
3.1 3.5 4.8 5.3 5.9
2.8 2.5 10.0 5.9 6.6
2.5 10.0 10.0 10.0 7.3
2.3 9.0 10.0 9.0 8.1
(d)rforbidden is changed from 1 to 10. The other parameters are the same as those in (a).
Figure 3.4: The optimal policies and optimal state values given dierent parameter values.
50

## 第64页

3.5. Factors that in
uence optimal policies
because the optimal policy for each state is extremely short-sighted and merely selects
the action with the greatest immediate reward instead of the greatest total reward.
In addition, the spatial distribution of the state values exhibits an interesting pattern:
the states close to the target have greater state values, whereas those far away have lower
values. This pattern can be observed from all the examples shown in Figure 3.4. It can
be explained by using the discount rate: if a state must travel along a longer trajectory
to reach the target, its state value is smaller due to the discount rate.
Impact of the reward values
If we want to strictly prohibit the agent from entering any forbidden area, we can increase
the punishment received for doing so. For instance, if rforbidden is changed from 1 to
 10, the resulting optimal policy can avoid all the forbidden areas (see Figure 3.4(d)).
However, changing the rewards does not always lead to dierent optimal policies.
One important fact is that optimal policies are invariant to ane transformations of the
rewards. In other words, if we scale all the rewards or add the same value to all the
rewards, the optimal policy remains the same.
Theorem 3.6 (Optimal policy invariance) .Consider a Markov decision process with
v2RjSjas the optimal state value satisfying v= max2(r+
Pv). If every reward
r2R is changed by an ane transformation to r+, where;2Rand>0, then
the corresponding optimal state value v0is also an ane transformation of v:
v0=v+
1 
1; (3.8)
where
2(0;1)is the discount rate and 1= [1;:::; 1]T. Consequently, the optimal policy
derived from v0is invariant to the ane transformation of the reward values.
Box 3.5: Proof of Theorem 3.6
For any policy , dener= [:::;r(s);:::]Twhere
r(s) =X
a2A(ajs)X
r2Rp(rjs;a)r; s2S:
Ifr!r+, thenr(s)!r(s) +and hence r!r+1, where 1=
[1;:::; 1]T. In this case, the BOE becomes
v0= max
2(r+1+
Pv0): (3.9)
51

## 第65页

3.5. Factors that in
uence optimal policies
We next solve the new BOE in (3.9) by showing that v0=v+c1withc==(1 
)
is a solution of (3.9). In particular, substituting v0=v+c1into (3.9) gives
v+c1= max
2(r+1+
P(v+c1)) = max
2(r+1+
Pv+c
1);
where the last equality is due to the fact that P1=1. The above equation can be
reorganized as
v= max
2(r+
Pv) +1+c
1 c1;
which is equivalent to
1+c
1 c1= 0:
Sincec==(1 
), the above equation is valid and hence v0=v+c1is the solution
of (3.9). Since (3.9) is the BOE, v0is also the unique solution. Finally, since v0is
an ane transformation of v, the relative relationships between the action values
remain the same. Hence, the greedy optimal policy derived from v0is the same as
that fromv: arg max 2(r+
Pv0) is the same as arg max (r+
Pv).
Readers may refer to [9] for a further discussion on the conditions under which mod-
ications to the reward values preserve the optimal policy.
Avoiding meaningless detours
In the reward setting, the agent receives a reward of rother = 0 for every movement
step (unless it enters a forbidden area or the target area or attempts to go beyond the
boundary). Since a zero reward is not a punishment, would the optimal policy take
meaningless detours before reaching the target? Should we set rother to be negative to
encourage the agent to reach the target as quickly as possible?
1 2
1
2
1 2
1
29.0 10.0
10.0 10.0
(a) Optimal policy
1 2
1
2
1 2
1
29.0 8.1
10.0 10.0 (b) Non-optimal policy
Figure 3.5: Examples illustrating that optimal policies do not take meaningless detours due to the
discount rate.
Consider the examples in Figure 3.5, where the bottom-right cell is the target area
52

## 第66页

3.6. Summary
to reach. The two policies here are the same except for state s2. By the policy in
Figure 3.5(a), the agent moves downward at s2and the resulting trajectory is s2!s4.
By the policy in Figure 3.5(b), the agent moves leftward and the resulting trajectory is
s2!s1!s3!s4.
It is notable that the second policy takes a detour before reaching the target area. If
we merely consider the immediate rewards, taking this detour does not matter because
no negative immediate rewards will be obtained. However, if we consider the discounted
return, then this detour matters. In particular, for the rst policy, the discounted return
is
return = 1 + 
1 +
21 += 1=(1 
) = 10:
As a comparison, the discounted return for the second policy is
return = 0 + 
0 +
21 +
31 +=
2=(1 
) = 8:1:
It is clear that the shorter the trajectory is, the greater the return is. Therefore, although
the immediate reward of every step does not encourage the agent to approach the target
as quickly as possible, the discount rate does encourage it to do so.
A misunderstanding that beginners may have is that adding a negative reward (e.g.,
 1) on top of the rewards obtained for every movement is necessary to encourage the
agent to reach the target as quickly as possible. This is a misunderstanding because
adding the same reward on top of all rewards is an ane transformation, which preserves
the optimal policy. Moreover, optimal policies do not take meaningless detours due to
the discount rate, even though a detour may not receive any immediate negative rewards.
3.6 Summary
The core concepts in this chapter include optimal policies and optimal state values. In
particular, a policy is optimal if its state values are greater than or equal to those of any
other policy. The state values of an optimal policy are the optimal state values. The BOE
is the core tool for analyzing optimal policies and optimal state values. This equation
is a nonlinear equation with a nice contraction property. We can apply the contraction
mapping theorem to analyze this equation. It was shown that the solutions of the BOE
correspond to the optimal state value and optimal policy. This is the reason why we need
to study the BOE.
The contents of this chapter are important for thoroughly understanding many funda-
mental ideas of reinforcement learning. For example, Theorem 3.3 suggests an iterative
algorithm for solving the BOE. This algorithm is exactly the value iteration algorithm
that will be introduced in Chapter 4. A further discussion about the BOE can be found
in [2].
53

## 第67页

3.7. Q&A
3.7 Q&A
Q: What is the denition of optimal policies?
A: A policy is optimal if its corresponding state values are greater than or equal to
any other policy.
It should be noted that this specic denition of optimality is valid only for tabular
reinforcement learning algorithms. When the values or policies are approximated by
functions, dierent metrics must be used to dene optimal policies. This will become
clearer in Chapters 8 and 9.
Q: Why is the Bellman optimality equation important?
A: It is important because it characterizes both optimal policies and optimal state
values. Solving this equation yields an optimal policy and the corresponding optimal
state value.
Q: Is the Bellman optimality equation a Bellman equation?
A: Yes. The Bellman optimality equation is a special Bellman equation whose corre-
sponding policy is optimal.
Q: Is the solution of the Bellman optimality equation unique?
A: The Bellman optimality equation has two unknown variables. The rst unknown
variable is a value, and the second is a policy. The value solution, which is the optimal
state value, is unique. The policy solution, which is an optimal policy, may not be
unique.
Q: What is the key property of the Bellman optimality equation for analyzing its
solution?
A: The key property is that the right-hand side of the Bellman optimality equation is
a contraction mapping. As a result, we can apply the contraction mapping theorem
to analyze its solution.
Q: Do optimal policies exist?
A: Yes. Optimal policies always exist according to the analysis of the BOE.
Q: Are optimal policies unique?
A: No. There may exist multiple or innite optimal policies that have the same
optimal state values.
Q: Are optimal policies stochastic or deterministic?
A: An optimal policy can be either deterministic or stochastic. A nice fact is that
there always exist deterministic greedy optimal policies.
54

## 第68页

3.7. Q&A
Q: How to obtain an optimal policy?
A: Solving the BOE using the iterative algorithm suggested by Theorem 3.3 yields an
optimal policy. The detailed implementation of this iterative algorithm will be given
in Chapter 4. Notably, all the reinforcement learning algorithms introduced in this
book aim to obtain optimal policies under dierent settings.
Q: What is the general impact on the optimal policies if we reduce the value of the
discount rate?
A: The optimal policy becomes more short-sighted when we reduce the discount rate.
That is, the agent does not dare to take risks even though it may obtain greater
cumulative rewards afterward.
Q: What happens if we set the discount rate to zero?
A: The resulting optimal policy would become extremely short-sighted. The agent
would take the action with the greatest immediate reward, even though that action
is not good in the long run.
Q: If we increase all the rewards by the same amount, will the optimal state value
change? Will the optimal policy change?
A: Increasing all the rewards by the same amount is an ane transformation of the
rewards, which would not aect the optimal policies. However, the optimal state value
would increase, as shown in (3.8).
Q: If we hope that the optimal policy can avoid meaningless detours before reaching
the target, should we add a negative reward to every step so that the agent reaches
the target as quickly as possible?
A: First, introducing an additional negative reward to every step is an ane transfor-
mation of the rewards, which does not change the optimal policy. Second, the discount
rate can automatically encourage the agent to reach the target as quickly as possible.
This is because meaningless detours would increase the trajectory length and reduce
the discounted return.
55

## 第69页

3.7. Q&A
56

## 第70页

Chapter 4
Value Iteration and Policy Iteration
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
Figure 4.1: Where we are in this book.
With the preparation in the previous chapters, we are now ready to present the rst
algorithms that can nd optimal policies. This chapter introduces three algorithms that
are closely related to each other. The rst is the value iteration algorithm, which is
exactly the algorithm suggested by the contraction mapping theorem for solving the
Bellman optimality equation as discussed in the last chapter. We focus more on the
implementation details of this algorithm in the present chapter. The second is the policy
iteration algorithm, whose idea is widely used in reinforcement learning algorithms. The
third is the truncated policy iteration algorithm, which is a unied algorithm that includes
the value iteration and policy iteration algorithms as special cases.
57

## 第71页

4.1. Value iteration
The algorithms introduced in this chapter are called dynamic programming algorithms
[10,11], which require the system model. These algorithms are important foundations of
the model-free reinforcement learning algorithms introduced in the subsequent chapters.
For example, the Monte Carlo algorithms introduced in Chapter 5 can be immediately
obtained by extending the policy iteration algorithm introduced in this chapter.
4.1 Value iteration
This section introduces the value iteration algorithm. It is exactly the algorithm suggested
by the contraction mapping theorem for solving the Bellman optimality equation, as
introduced in the last chapter (Theorem 3.3). In particular, the algorithm is
vk+1= max
2(r+
Pvk); k = 0;1;2;:::
It is guaranteed by Theorem 3.3 that vkandkconverge to the optimal state value and
an optimal policy as k!1 , respectively.
This algorithm is iterative and has two steps in every iteration.
The rst step in every iteration is a policy update step. Mathematically, it aims to
nd a policy that can solve the following optimization problem:
k+1= arg max
(r+
Pvk);
wherevkis obtained in the previous iteration.
The second step is called a value update step. Mathematically, it calculates a new
valuevk+1by
vk+1=rk+1+
Pk+1vk; (4.1)
wherevk+1will be used in the next iteration.
The value iteration algorithm introduced above is in a matrix-vector form. To im-
plement this algorithm, we need to further examine its elementwise form. While the
matrix-vector form is useful for understanding the core idea of the algorithm, the ele-
mentwise form is necessary for explaining the implementation details.
4.1.1 Elementwise form and implementation
Consider the time step kand a state s.
58

## 第72页

4.1. Value iteration
First, the elementwise form of the policy update step k+1= arg max (r+
Pvk) is
k+1(s) = arg max
X
a(ajs) X
rp(rjs;a)r+
X
s0p(s0js;a)vk(s0)!
| {z }
qk(s;a); s2S:
We showed in Section 3.3.1 that the optimal policy that can solve the above optimiza-
tion problem is
k+1(ajs) =(
1; a=a
k(s);
0; a6=a
k(s);(4.2)
wherea
k(s) = arg max aqk(s;a). Ifa
k(s) = arg max aqk(s;a) has multiple solutions,
we can select any of them without aecting the convergence of the algorithm. Since
the new policy k+1selects the action with the greatest qk(s;a), such a policy is called
greedy.
Second, the elementwise form of the value update step vk+1=rk+1+
Pk+1vkis
vk+1(s) =X
ak+1(ajs) X
rp(rjs;a)r+
X
s0p(s0js;a)vk(s0)!
| {z }
qk(s;a); s2S:
Substituting (4.2) into the above equation gives
vk+1(s) = max
aqk(s;a):
In summary, the above steps can be illustrated as
vk(s)!qk(s;a)!new greedy policy k+1(s)!new valuevk+1(s) = max
aqk(s;a)
The implementation details are summarized in Algorithm 4.1.
One problem that may be confusing is whether vkin (4.1) is a state value. The
answer is no. Although vkeventually converges to the optimal state value, it is not
ensured to satisfy the Bellman equation of any policy. For example, it does not satisfy
vk=rk+1+
Pk+1vkorvk=rk+
Pkvkin general. It is merely an intermediate value
generated by the algorithm. In addition, since vkis not a state value, qkis not an action
value.
4.1.2 Illustrative examples
We next present an example to illustrate the step-by-step implementation of the value
iteration algorithm. This example is a two-by-two grid with one forbidden area (Fig-
59

## 第73页

4.1. Value iteration
Algorithm 4.1: Value iteration algorithm
Initialization: The probability models p(rjs;a)andp(s0js;a)for all (s;a)are known.
Initial guess v0.
Goal: Search for the optimal state value and an optimal policy for solving the Bellman
optimality equation.
Whilevkhas not converged in the sense that kvk vk 1kis greater than a predened
small threshold, for the kth iteration, do
For every state s2S, do
For every action a2A(s), do
q-value:qk(s;a) =P
rp(rjs;a)r+
P
s0p(s0js;a)vk(s0)
Maximum action value: a
k(s) = arg max aqk(s;a)
Policy update: k+1(ajs) = 1 ifa=a
k, andk+1(ajs) = 0 otherwise
Value update: vk+1(s) = max aqk(s;a)
q-table a1 a2 a3 a4 a5
s1 1 +
v(s1) 1 +
v(s2)0 +
v(s3) 1 +
v(s1)0 +
v(s1)
s2 1 +
v(s2) 1 +
v(s2)1 +
v(s4) 0 +
v(s1) 1 +
v(s2)
s3 0 +
v(s1) 1 +
v(s4) 1 +
v(s3) 1 +
v(s3)0 +
v(s3)
s4 1 +
v(s2) 1 +
v(s4) 1 +
v(s4)0 +
v(s3) 1 +
v(s4)
Table 4.1: The expression of q(s;a) for the example as shown in Figure 4.2.
ure 4.2). The target area is s4. The reward settings are rboundary =rforbidden = 1 and
rtarget = 1. The discount rate is 
= 0:9.
s1 s2
s3 s4
s1 s2
s3 s4
s1 s2
s3 s4
Figure 4.2: An example for demonstrating the implementation of the value iteration algorithm.
The expression of the q-value for each state-action pair is shown in Table 4.1.
k= 0:
Without loss of generality, select the initial values as v0(s1) =v0(s2) =v0(s3) =
v0(s4) = 0.
q-value calculation: Substituting v0(si) into Table 4.1 gives the q-values shown in
Table 4.2.
60

## 第74页

4.1. Value iteration
q-tablea1a2a3a4a5
s1 1 1 0 1 0
s2 1 1 1 0 1
s3 0 1 1 1 0
s4 1 1 1 0 1
Table 4.2: The value of q(s;a) atk= 0.
q-tablea1a2a3a4a5
s1 1 +
0 1 +
10 +
1 1 +
00 +
0
s2 1 +
1 1 +
11 +
1 0 +
0 1 +
1
s3 0 +
0 1 +
1 1 +
1 1 +
10 +
1
s4 1 +
1 1 +
1 1 +
10 +
1 1 +
1
Table 4.3: The value of q(s;a) atk= 1.
Policy update: 1is obtained by selecting the actions with the greatest q-values for
every state:
1(a5js1) = 1;  1(a3js2) = 1;  1(a2js3) = 1;  1(a5js4) = 1:
This policy is visualized in Figure 4.2 (the middle subgure). It is clear that this
policy is not optimal because it selects to stay still at s1. Notably, the q-values for
(s1;a5) and (s1;a3) are actually the same, and we can randomly select either action.
Value update: v1is obtained by updating the v-value to the greatest q-value for each
state:
v1(s1) = 0; v 1(s2) = 1; v 1(s3) = 1; v 1(s4) = 1:
k= 1:
q-value calculation: Substituting v1(si) into Table 4.1 yields the q-values shown in
Table 4.3.
Policy update: 2is obtained by selecting the greatest q-values:
2(a3js1) = 1;  2(a3js2) = 1;  2(a2js3) = 1;  2(a5js4) = 1:
This policy is visualized in Figure 4.2 (the right subgure).
Value update: v2is obtained by updating the v-value to the greatest q-value for each
state:
v2(s1) =
1; v 2(s2) = 1 +
1; v 2(s3) = 1 +
1; v 2(s4) = 1 +
1:
k= 2;3;4;:::
It is notable that policy 2, as illustrated in Figure 4.2, is already optimal. Therefore, we
61

## 第75页

4.2. Policy iteration
only need to run two iterations to obtain an optimal policy in this simple example. For
more complex examples, we need to run more iterations until the value of vkconverges
(e.g., untilkvk+1 vkkis smaller than a pre-specied threshold).
4.2 Policy iteration
This section presents another important algorithm: policy iteration . Unlike value itera-
tion, policy iteration is not for directly solving the Bellman optimality equation. However,
it has an intimate relationship with value iteration, as shown later. Moreover, the idea
of policy iteration is very important since it is widely utilized in reinforcement learning
algorithms.
4.2.1 Algorithm analysis
Policy iteration is an iterative algorithm. Each iteration has two steps.
The rst is a policy evaluation step. As its name suggests, this step evaluates a given
policy by calculating the corresponding state value. That is to solve the following
Bellman equation:
vk=rk+
Pkvk; (4.3)
wherekis the policy obtained in the last iteration and vkis the state value to be
calculated. The values of rkandPkcan be obtained from the system model.
The second is a policy improvement step. As its name suggests, this step is used to
improve the policy. In particular, once vkhas been calculated in the rst step, a new
policyk+1can be obtained as
k+1= arg max
(r+
Pvk):
Three questions naturally follow the above description of the algorithm.
In the policy evaluation step, how to solve the state value vk?
In the policy improvement step, why is the new policy k+1better than k?
Why can this algorithm nally converge to an optimal policy?
We next answer these questions one by one.
In the policy evaluation step, how to calculate vk?
We introduced two methods in Chapter 2 for solving the Bellman equation in (4.3).
We next revisit the two methods brie
y. The rst method is a closed-form solution:
62

## 第76页

4.2. Policy iteration
vk= (I 
Pk) 1rk. This closed-form solution is useful for theoretical analysis purposes,
but it is inecient to implement since it requires other numerical algorithms to compute
the matrix inverse. The second method is an iterative algorithm that can be easily
implemented:
v(j+1)
k=rk+
Pkv(j)
k; j = 0;1;2;::: (4.4)
wherev(j)
kdenotes the jth estimate of vk. Starting from any initial guess v(0)
k, it is
ensured that v(j)
k!vkasj!1 . Details can be found in Section 2.7.
Interestingly, policy iteration is an iterative algorithm with another iterative algorithm
(4.4) embedded in the policy evaluation step. In theory, this embedded iterative algorithm
requires an innite number of steps (that is, j!1 ) to converge to the true state value
vk. This is, however, impossible to realize. In practice, the iterative process terminates
when a certain criterion is satised. For example, the termination criterion can be that
kv(j+1)
k v(j)
kkis less than a prespecied threshold or that jexceeds a prespecied value.
If we do not run an innite number of iterations, we can only obtain an imprecise value
ofvk, which will be used in the subsequent policy improvement step. Would this cause
problems? The answer is no. The reason will become clear when we introduce the
truncated policy iteration algorithm later in Section 4.3.
In the policy improvement step, why is k+1better than k?
The policy improvement step can improve the given policy, as shown below.
Lemma 4.1 (Policy improvement) .Ifk+1= arg max (r+
Pvk), thenvk+1vk.
Here,vk+1vkmeans that vk+1(s)vk(s) for alls. The proof of this lemma is
given in Box 4.1.
Box 4.1: Proof of Lemma 4.1
Sincevk+1andvkare state values, they satisfy the Bellman equations:
vk+1=rk+1+
Pk+1vk+1;
vk=rk+
Pkvk:
Sincek+1= arg max (r+
Pvk), we know that
rk+1+
Pk+1vkrk+
Pkvk:
63

## 第77页

4.2. Policy iteration
It then follows that
vk vk+1= (rk+
Pkvk) (rk+1+
Pk+1vk+1)
(rk+1+
Pk+1vk) (rk+1+
Pk+1vk+1)

Pk+1(vk vk+1):
Therefore,
vk vk+1
2P2
k+1(vk vk+1):::
nPn
k+1(vk vk+1)
lim
n!1
nPn
k+1(vk vk+1) = 0:
The limit is due to the facts that 
n!0 asn!1 andPn
k+1is a nonnegative
stochastic matrix for any n. Here, a stochastic matrix refers to a nonnegative matrix
whose row sums are equal to one for all rows.
Why can the policy iteration algorithm eventually nd an optimal policy?
The policy iteration algorithm generates two sequences. The rst is a sequence of policies:
f0;1;:::;k;:::g. The second is a sequence of state values: fv0;v1;:::;vk;:::g.
Suppose that vis the optimal state value. Then, vkvfor allk. Since the policies
are continuously improved according to Lemma 4.1, we know that
v0v1v2vkv:
Sincevkis nondecreasing and always bounded from above by v, it follows from the
monotone convergence theorem [12] (Appendix C) that vkconverges to a constant value,
denoted as v1, whenk!1 . The following analysis shows that v1=v.
Theorem 4.1 (Convergence of policy iteration) .The state value sequence fvkg1
k=0gen-
erated by the policy iteration algorithm converges to the optimal state value v. As a
result, the policy sequence fkg1
k=0converges to an optimal policy.
The proof of this theorem is given in Box 4.2. The proof not only shows the conver-
gence of the policy iteration algorithm but also reveals the relationship between the policy
iteration and value iteration algorithms. Loosely speaking, if both algorithms start from
the same initial guess, policy iteration will converge faster than value iteration due to
the additional iterations embedded in the policy evaluation step. This point will become
clearer when we introduce the truncated policy iteration algorithm in Section 4.3.
64

## 第78页

4.2. Policy iteration
Box 4.2: Proof of Theorem 4.1
The idea of the proof is to show that the policy iteration algorithm converges faster
than the value iteration algorithm.
In particular, to prove the convergence of fvkg1
k=0, we introduce another sequence
fvkg1
k=0generated by
vk+1=f(vk) = max
(r+
Pvk):
This iterative algorithm is exactly the value iteration algorithm. We already know
thatvkconverges to vwhen given any initial value v0.
Fork= 0, we can always nd a v0such thatv0v0for any0.
We next show that vkvkvfor allkby induction.
Fork0, suppose that vkvk.
Fork+ 1, we have
vk+1 vk+1= (rk+1+
Pk+1vk+1) max
(r+
Pvk)
(rk+1+
Pk+1vk) max
(r+
Pvk)
 
becausevk+1vkby Lemma 4.1 and Pk+10
= (rk+1+
Pk+1vk) (r0
k+
P0
kvk)
 
suppose0
k= arg max
(r+
Pvk)
(r0
k+
P0
kvk) (r0
k+
P0
kvk)
 
becausek+1= arg max
(r+
Pvk)
=
P0
k(vk vk):
Sincevk vk0 andP0
kis nonnegative, we have P0
k(vk vk)0 and hence
vk+1 vk+10.
Therefore, we can show by induction that vkvkvfor anyk0. Sincevk
converges to v,vkalso converges to v.
4.2.2 Elementwise form and implementation
To implement the policy iteration algorithm, we need to study its elementwise form.
First, the policy evaluation step solves vkfromvk=rk+
Pkvkby using the
65

## 第79页

4.2. Policy iteration
Algorithm 4.2: Policy iteration algorithm
Initialization: The system model, p(rjs;a)andp(s0js;a)for all (s;a), is known. Initial
guess0.
Goal: Search for the optimal state value and an optimal policy.
Whilevkhas not converged, for the kth iteration, do
Policy evaluation:
Initialization: an arbitrary initial guess v(0)
k
Whilev(j)
khas not converged, for the jth iteration, do
For every state s2S, do
v(j+1)
k(s) =P
ak(ajs)hP
rp(rjs;a)r+
P
s0p(s0js;a)v(j)
k(s0)i
Policy improvement:
For every state s2S, do
For every action a2A , do
qk(s;a) =P
rp(rjs;a)r+
P
s0p(s0js;a)vk(s0)
a
k(s) = arg max aqk(s;a)
k+1(ajs) = 1 ifa=a
k, andk+1(ajs) = 0 otherwise
iterative algorithm in (4.4). The elementwise form of this algorithm is
v(j+1)
k(s) =X
ak(ajs) X
rp(rjs;a)r+
X
s0p(s0js;a)v(j)
k(s0)!
; s2S;
wherej= 0;1;2;:::.
Second, the policy improvement step solves k+1= arg max (r+
Pvk). The
elementwise form of this equation is
k+1(s) = arg max
X
a(ajs) X
rp(rjs;a)r+
X
s0p(s0js;a)vk(s0)!
| {z }
qk(s;a); s2S;
whereqk(s;a) is the action value under policy k. Leta
k(s) = arg max aqk(s;a).
Then, the greedy optimal policy is
k+1(ajs) =(
1; a=a
k(s);
0; a6=a
k(s):
The implementation details are summarized in Algorithm 4.2.
66

## 第80页

4.2. Policy iteration
4.2.3 Illustrative examples
A simple example
Consider a simple example shown in Figure 4.3. There are two states with three possible
actions:A=fa`;a0;arg. The three actions represent moving leftward, staying un-
changed, and moving rightward. The reward settings are rboundary = 1 andrtarget = 1.
The discount rate is 
= 0:9.
(b) (a)s1 s2 s1 s2
Figure 4.3: An example for illustrating the implementation of the policy iteration algorithm.
We next present the implementation of the policy iteration algorithm in a step-by-step
manner. When k= 0, we start with the initial policy shown in Figure 4.3(a). This policy
is not good because it does not move toward the target area. We next show how to apply
the policy iteration algorithm to obtain an optimal policy.
First, in the policy evaluation step, we need to solve the Bellman equation:
v0(s1) = 1 +
v0(s1);
v0(s2) = 0 +
v0(s1):
Since the equation is simple, it can be manually solved that
v0(s1) = 10; v0(s2) = 9:
In practice, the equation can be solved by the iterative algorithm in (4.4). For example,
select the initial state values as v(0)
0(s1) =v(0)
0(s2) = 0. It follows from (4.4) that
(
v(1)
0(s1) = 1 +
v(0)
0(s1) = 1;
v(1)
0(s2) = 0 +
v(0)
0(s1) = 0;
(
v(2)
0(s1) = 1 +
v(1)
0(s1) = 1:9;
v(2)
0(s2) = 0 +
v(1)
0(s1) = 0:9;
(
v(3)
0(s1) = 1 +
v(2)
0(s1) = 2:71;
v(3)
0(s2) = 0 +
v(2)
0(s1) = 1:71;
...
With more iterations, we can see the trend: v(j)
0(s1)!v0(s1) = 10 andv(j)
0(s2)!
v0(s2) = 9 asjincreases.
67

## 第81页

4.2. Policy iteration
Second, in the policy improvement step, the key is to calculate q0(s;a) for each
state-action pair. The following q-table can be used to demonstrate such a process:
qk(s;a)a` a0 ar
s1 1 +
vk(s1)0 +
vk(s1)1 +
vk(s2)
s2 0 +
vk(s1)1 +
vk(s2) 1 +
vk(s2)
Table 4.4: The expression of qk(s;a) for the example in Figure 4.3.
Substituting v0(s1) = 10;v0(s2) = 9 obtained in the previous policy evaluation
step into Table 4.4 yields Table 4.5.
q0(s;a)a`a0ar
s1 10 9 7:1
s2 9 7:1 9:1
Table 4.5: The value of qk(s;a) whenk= 0.
By seeking the greatest value of q0, the improved policy 1can be obtained as
1(arjs1) = 1;  1(a0js2) = 1:
This policy is illustrated in Figure 4.3(b). It is clear that this policy is optimal.
The above process shows that a single iteration is sucient for nding the optimal
policy in this simple example. More iterations are required for more complex examples.
A more complicated example
We next demonstrate the policy iteration algorithm using a more complicated example
shown in Figure 4.4. The reward settings are rboundary = 1,rforbidden = 10, andrtarget =
1. The discount rate is 
= 0:9. The policy iteration algorithm can converge to the
optimal policy (Figure 4.4(h)) when starting from a random initial policy (Figure 4.4(a)).
Two interesting phenomena are observed during the iteration process.
First, if we observe how the policy evolves, an interesting pattern is that the states
that are close to the target area nd the optimal policies earlier than those far away.
Only if the close states can nd trajectories to the target rst, can the farther states
nd trajectories passing through the close states to reach the target.
Second, the spatial distribution of the state values exhibits an interesting pattern: the
states that are located closer to the target have greater state values. The reason for
this pattern is that an agent starting from a farther state must travel for many steps
to obtain a positive reward. Such rewards would be severely discounted and hence
relatively small.
68

## 第82页

4.3. Truncated policy iteration
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
50.0 0.0 0.0 0.0 0.0
0.0 -100.0 -100.0 0.0 0.0
0.0 0.0 -100.0 0.0 0.0
0.0 -100.0 10.0 -100.0 0.0
0.0 -100.0 0.0 0.0 0.0
(a)0andv0
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
50.0 0.0 0.0 0.0 0.0
0.0 -100.0 -100.0 0.0 0.0
0.0 0.0 -100.0 0.0 0.0
0.0 -100.0 10.0 -100.0 0.0
0.0 -100.0 0.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 0.0 0.0 (b)1andv1
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
50.0 0.0 0.0 0.0 0.0
0.0 -100.0 -100.0 0.0 0.0
0.0 0.0 -100.0 0.0 0.0
0.0 -100.0 10.0 -100.0 0.0
0.0 -100.0 0.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 9.0 0.0
(c)2andv2
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
50.0 0.0 0.0 0.0 0.0
0.0 -100.0 -100.0 0.0 0.0
0.0 0.0 -100.0 0.0 0.0
0.0 -100.0 10.0 -100.0 0.0
0.0 -100.0 0.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 9.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.1 (d)3andv3
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
50.0 0.0 0.0 0.0 0.0
0.0 -100.0 -100.0 0.0 0.0
0.0 0.0 -100.0 0.0 0.0
0.0 -100.0 10.0 -100.0 0.0
0.0 -100.0 0.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 9.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.10.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.1
(e)4andv4
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
50.0 0.0 0.0 0.0 0.0
0.0 -100.0 -100.0 0.0 0.0
0.0 0.0 -100.0 0.0 0.0
0.0 -100.0 10.0 -100.0 0.0
0.0 -100.0 0.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 9.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.10.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.10.0 0.0 4.3 4.8 4.3
0.0 0.0 4.8 5.3 5.9
0.0 0.0 10.0 5.9 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.1 (f)5andv5
......
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
50.0 0.0 0.0 0.0 0.0
0.0 -100.0 -100.0 0.0 0.0
0.0 0.0 -100.0 0.0 0.0
0.0 -100.0 10.0 -100.0 0.0
0.0 -100.0 0.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 9.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.10.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.10.0 0.0 4.3 4.8 4.3
0.0 0.0 4.8 5.3 5.9
0.0 0.0 10.0 5.9 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.10.0 3.9 4.3 4.8 5.3
0.0 3.5 4.8 5.3 5.9
0.0 0.0 10.0 5.9 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.13.5 3.9 4.3 4.8 5.3
0.0 3.5 4.8 5.3 5.9
0.0 0.0 10.0 5.9 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.13.5 3.9 4.3 4.8 5.3
3.1 3.5 4.8 5.3 5.9
0.0 0.0 10.0 5.9 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.13.5 3.9 4.3 4.8 5.3
3.1 3.5 4.8 5.3 5.9
2.8 0.0 10.0 5.9 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.1
(g)9andv9
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
50.0 0.0 0.0 0.0 0.0
0.0 -100.0 -100.0 0.0 0.0
0.0 0.0 -100.0 0.0 0.0
0.0 -100.0 10.0 -100.0 0.0
0.0 -100.0 0.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 0.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 0.0
0.0 9.0 10.0 9.0 0.00.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 0.0
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.10.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 10.0 0.0 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.10.0 0.0 4.3 4.8 4.3
0.0 0.0 4.8 5.3 5.9
0.0 0.0 10.0 5.9 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.10.0 3.9 4.3 4.8 5.3
0.0 3.5 4.8 5.3 5.9
0.0 0.0 10.0 5.9 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.13.5 3.9 4.3 4.8 5.3
0.0 3.5 4.8 5.3 5.9
0.0 0.0 10.0 5.9 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.13.5 3.9 4.3 4.8 5.3
3.1 3.5 4.8 5.3 5.9
0.0 0.0 10.0 5.9 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.13.5 3.9 4.3 4.8 5.3
3.1 3.5 4.8 5.3 5.9
2.8 0.0 10.0 5.9 6.6
0.0 10.0 10.0 10.0 7.3
0.0 9.0 10.0 9.0 8.13.5 3.9 4.3 4.8 5.3
3.1 3.5 4.8 5.3 5.9
2.8 2.5 10.0 5.9 6.6
2.5 10.0 10.0 10.0 7.3
2.3 9.0 10.0 9.0 8.1 (h)10andv10
Figure 4.4: The evolution processes of the policies generated by the policy iteration algorithm.
69

## 第83页

4.3. Truncated policy iteration
4.3 Truncated policy iteration
We next introduce a more general algorithm called truncated policy iteration . We will
see that the value iteration and policy iteration algorithms are two special cases of the
truncated policy iteration algorithm.
4.3.1 Comparing value iteration and policy iteration
First of all, we compare the value iteration and policy iteration algorithms by listing their
steps as follows.
Policy iteration: Select an arbitrary initial policy 0. In thekth iteration, do the
following two steps.
- Step 1: Policy evaluation (PE). Given k, solvevkfrom
vk=rk+
Pkvk:
- Step 2: Policy improvement (PI). Given vk, solvek+1from
k+1= arg max
(r+
Pvk):
Value iteration: Select an arbitrary initial value v0. In thekth iteration, do the
following two steps.
- Step 1: Policy update (PU). Given vk, solvek+1from
k+1= arg max
(r+
Pvk):
- Step 2: Value update (VU). Given k+1, solvevk+1from
vk+1=rk+1+
Pk+1vk:
The above steps of the two algorithms can be illustrated as
Policy iteration: 0PE  !v0PI !1PE  !v1PI !2PE  !v2PI !:::
Value iteration: v0PU  !0
1VU  !v1PU  !0
2VU  !v2PU  !:::
It can be seen that the procedures of the two algorithms are very similar.
We examine their value steps more closely to see the dierence between the two
algorithms. In particular, let both algorithms start from the same initial condition :
v0=v0. The procedures of the two algorithms are listed in Table 4.6. In the rst
three steps, the two algorithms generate the same results since v0=v0. They become
70

## 第84页

4.3. Truncated policy iteration
Policy iteration algorithm Value iteration algorithm Comments
1) Policy: 0 N/A
2) Value: v0=r0+
P0v0 v0:=v0
3) Policy: 1= arg max (r+
Pv0)1= arg max (r+
Pv0)The two policies are
the same
4) Value: v1=r1+
P1v1 v1=r1+
P1v0 v1v1since
v1v0
5) Policy: 2= arg max (r+
Pv1)0
2= arg max (r+
Pv1)
............
Table 4.6: A comparison between the implementation steps of policy iteration and value iteration.
dierent in the fourth step. During the fourth step, the value iteration algorithm executes
v1=r1+
P1v0, which is a one-step calculation, whereas the policy iteration algorithm
solvesv1=r1+
P1v1, which requires an innite number of iterations. If we explicitly
write out the iterative process for solving v1=r1+
P1v1in the fourth step, everything
becomes clear. By letting v(0)
1=v0, we have
v(0)
1=v0
value iteration v1  v(1)
1=r1+
P1v(0)
1
v(2)
1=r1+
P1v(1)
1
...
truncated policy iteration  v1  v(j)
1=r1+
P1v(j 1)
1
...
policy iteration v1  v(1)
1=r1+
P1v(1)
1
The following observations can be obtained from the above process.
If the iteration is run only once , thenv(1)
1is actually v1, as calculated in the value
iteration algorithm.
If the iteration is run an innite number of times , thenv(1)
1is actuallyv1, as calcu-
lated in the policy iteration algorithm.
If the iteration is run a nite number of times (denoted as jtruncate ), then such an algo-
rithm is called truncated policy iteration . It is called truncated because the remaining
iterations from jtruncate to1are truncated.
As a result, the value iteration and policy iteration algorithms can be viewed as two
extreme cases of the truncated policy iteration algorithm: value iteration terminates
71

## 第85页

4.3. Truncated policy iteration
Algorithm 4.3: Truncated policy iteration algorithm
Initialization: The probability models p(rjs;a)andp(s0js;a)for all (s;a)are known.
Initial guess 0.
Goal: Search for the optimal state value and an optimal policy.
Whilevkhas not converged, for the kth iteration, do
Policy evaluation:
Initialization: select the initial guess as v(0)
k=vk 1. The maximum number of
iterations is set as jtruncate .
Whilej <j truncate , do
For every state s2S, do
v(j+1)
k(s) =P
ak(ajs)hP
rp(rjs;a)r+
P
s0p(s0js;a)v(j)
k(s0)i
Setvk=v(jtruncate )
k
Policy improvement:
For every state s2S, do
For every action a2A(s), do
qk(s;a) =P
rp(rjs;a)r+
P
s0p(s0js;a)vk(s0)
a
k(s) = arg max aqk(s;a)
k+1(ajs) = 1 ifa=a
k, andk+1(ajs) = 0 otherwise
atjtruncate = 1, and policy iteration terminates at jtruncate =1. It should be noted
that, although the above comparison is illustrative, it is based on the condition that
v(0)
1=v0=v0. The two algorithms cannot be directly compared without this condition.
4.3.2 Truncated policy iteration algorithm
In a nutshell, the truncated policy iteration algorithm is the same as the policy iteration
algorithm except that it merely runs a nite number of iterations in the policy evaluation
step. Its implementation details are summarized in Algorithm 4.3. It is notable that vk
andv(j)
kin the algorithm are not state values. Instead, they are approximations of the
true state values because only a nite number of iterations are executed in the policy
evaluation step.
Ifvkdoes not equal vk, will the algorithm still be able to nd optimal policies? The
answer is yes. Intuitively, truncated policy iteration is in between value iteration and
policy iteration. On the one hand, it converges faster than the value iteration algorithm
because it computes more than one iteration during the policy evaluation step. On
the other hand, it converges slower than the policy iteration algorithm because it only
computes a nite number of iterations. This intuition is illustrated in Figure 4.5. Such
intuition is also supported by the following analysis.
Proposition 4.1 (Value improvement) .Consider the iterative algorithm in the policy
72

## 第86页

4.3. Truncated policy iteration
kv*
v
k
vk
Policy iteration
Value iteration
Truncated policy iteration
Optimal state value
Figure 4.5: An illustration of the relationships between the value iteration, policy iteration, and truncated
policy iteration algorithms.
evaluation step:
v(j+1)
k=rk+
Pkv(j)
k; j = 0;1;2;:::
If the initial guess is selected as v(0)
k=vk 1, it holds that
v(j+1)
kv(j)
k
forj= 0;1;2;:::.
Box 4.3: Proof of Proposition 4.1
First, since v(j)
k=rk+
Pkv(j 1)
kandv(j+1)
k=rk+
Pkv(j)
k, we have
v(j+1)
k v(j)
k=
Pk(v(j)
k v(j 1)
k) ==
jPj
k(v(1)
k v(0)
k): (4.5)
Second, since v(0)
k=vk 1, we have
v(1)
k=rk+
Pkv(0)
k=rk+
Pkvk 1rk 1+
Pk 1vk 1=vk 1=v(0)
k;
where the inequality is due to k= arg max (r+
Pvk 1). Substituting v(1)
kv(0)
k
into (4.5) yields v(j+1)
kv(j)
k.
Notably, Proposition 4.1 requires the assumption that v(0)
k=vk 1. However, vk 1is
unavailable in practice, and only vk 1is available. Nevertheless, Proposition 4.1 still sheds
light on the convergence of the truncated policy iteration algorithm. A more in-depth
discussion of this topic can be found in [2, Section 6.5].
Up to now, the advantages of truncated policy iteration are clear. Compared to the
73

## 第87页

4.4. Summary
policy iteration algorithm, the truncated one merely requires a nite number of iterations
in the policy evaluation step and hence is more computationally ecient. Compared to
value iteration, the truncated policy iteration algorithm can speed up its convergence
rate by running for a few more iterations in the policy evaluation step.
4.4 Summary
This chapter introduced three algorithms that can be used to nd optimal policies.
Value iteration: The value iteration algorithm is the same as the algorithm suggested
by the contraction mapping theorem for solving the Bellman optimality equation. It
can be decomposed into two steps: value update and policy update.
Policy iteration: The policy iteration algorithm is slightly more complicated than the
value iteration algorithm. It also contains two steps: policy evaluation and policy
improvement.
Truncated policy iteration: The value iteration and policy iteration algorithms can
be viewed as two extreme cases of the truncated policy iteration algorithm.
A common property of the three algorithms is that every iteration has two steps.
One step is to update the value, and the other step is to update the policy. The idea
of interaction between value and policy updates widely exists in reinforcement learning
algorithms. This idea is also called generalized policy iteration [3].
Finally, the algorithms introduced in this chapter require the system model. Starting
in Chapter 5, we will study model-free reinforcement learning algorithms. We will see that
the model-free can be obtained by extending the algorithms introduced in this chapter.
4.5 Q&A
Q: Is the value iteration algorithm guaranteed to nd optimal policies?
A: Yes. This is because value iteration is exactly the algorithm suggested by the
contraction mapping theorem for solving the Bellman optimality equation in the last
chapter. The convergence of this algorithm is guaranteed by the contraction mapping
theorem.
Q: Are the intermediate values generated by the value iteration algorithm state values?
A: No. These values are not guaranteed to satisfy the Bellman equation of any policy.
Q: What steps are included in the policy iteration algorithm?
A: Each iteration of the policy iteration algorithm contains two steps: policy evalu-
ation and policy improvement. In the policy evaluation step, the algorithm aims to
solve the Bellman equation to obtain the state value of the current policy. In the
74

## 第88页

4.5. Q&A
policy improvement step, the algorithm aims to update the policy so that the newly
generated policy has greater state values.
Q: Is another iterative algorithm embedded in the policy iteration algorithm?
A: Yes. In the policy evaluation step of the policy iteration algorithm, an iterative
algorithm is required to solve the Bellman equation of the current policy.
Q: Are the intermediate values generated by the policy iteration algorithm state val-
ues?
A: Yes. This is because these values are the solutions of the Bellman equation of the
current policy.
Q: Is the policy iteration algorithm guaranteed to nd optimal policies?
A: Yes. We have presented a rigorous proof of its convergence in this chapter.
Q: What is the relationship between the truncated policy iteration and policy iteration
algorithms?
A: As its name suggests, the truncated policy iteration algorithm can be obtained
from the policy iteration algorithm by simply executing a nite number of iterations
during the policy evaluation step.
Q: What is the relationship between truncated policy iteration and value iteration?
A: Value iteration can be viewed as an extreme case of truncated policy iteration,
where a single iteration is run during the policy evaluation step.
Q: Are the intermediate values generated by the truncated policy iteration algorithm
state values?
A: No. Only if we run an innite number of iterations in the policy evaluation step,
can we obtain true state values. If we run a nite number of iterations, we can only
obtain approximates of the true state values.
Q: How many iterations should we run in the policy evaluation step of the truncated
policy iteration algorithm?
A: The general guideline is to run a few iterations but not too many. The use of a few
iterations in the policy evaluation step can speed up the overall convergence rate, but
running too many iterations would not signicantly speed up the convergence rate.
Q: What is generalized policy iteration?
A: Generalized policy iteration is not a specic algorithm. Instead, it refers to the
general idea of the interaction between value and policy updates. This idea is root-
ed in the policy iteration algorithm. Most of the reinforcement learning algorithms
introduced in this book fall into the scope of generalized policy iteration.
Q: What are model-based and model-free reinforcement learning?
75

## 第89页

4.5. Q&A
A: Although the algorithms introduced in this chapter can nd optimal policies, they
are usually called dynamic programming algorithms rather than reinforcement learn-
ing algorithms because they require the system model. Reinforcement learning al-
gorithms can be classied into two categories: model-based and model-free. Here,
\model-based" does not refer to the requirement of the system model. Instead, model-
based reinforcement learning uses data to estimate the system model and uses this
model during the learning process. By contrast, model-free reinforcement learning
does not involve model estimation during the learning process. More information
about model-based reinforcement learning can be found in [13{16].
76

## 第90页

Chapter 5
Monte Carlo Methods
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
Figure 5.1: Where we are in this book.
In the previous chapter, we introduced algorithms that can nd optimal policies based
on the system model. In this chapter, we start introducing model-free reinforcement
learning algorithms that do not presume system models.
While this is the rst time we introduce model-free algorithms in this book, we must
ll a knowledge gap: how can we nd optimal policies without models? The philosophy
is simple: If we do not have a model, we must have some data. If we do not have data,
we must have a model. If we have neither, then we are not able to nd optimal policies.
The \data" in reinforcement learning usually refers to the agent's interaction experiences
with the environment.
77

## 第91页

5.1. Motivating example: Mean estimation
To demonstrate how to learn from data rather than a model, we start this chapter by
introducing the mean estimation problem, where the expected value of a random variable
is estimated from some samples. Understanding this problem is crucial for understanding
the fundamental idea of learning from data .
Then, we introduce three algorithms based on Monte Carlo (MC) methods. These
algorithms can learn optimal policies from experience samples. The rst and simplest
algorithm is called MC Basic, which can be readily obtained by modifying the policy itera-
tion algorithm introduced in the last chapter. Understanding this algorithm is important
for grasping the fundamental idea of MC-based reinforcement learning. By extending
this algorithm, we further introduce another two algorithms that are more complicated
but more ecient.
5.1 Motivating example: Mean estimation
We next introduce the mean estimation problem to demonstrate how to learn from data
rather than a model. We will see that mean estimation can be achieved based on Monte
Carlo methods, which refer to a broad class of techniques that use stochastic samples
to solve estimation problems. The reader may wonder why we care about the mean
estimation problem. It is simply because state and action values are both dened as
the means of returns. Estimating a state or action value is actually a mean estimation
problem.
Consider a random variable Xthat can take values from a nite set of real numbers
denoted asX. Suppose that our task is to calculate the mean or expected value of X:
E[X]. Two approaches can be used to calculate E[X].
The rst approach is model-based . Here, the model refers to the probability distribu-
tion ofX. If the model is known, then the mean can be directly calculated based on
the denition of the expected value:
E[X] =X
x2Xp(x)x:
In this book, we use the terms expected value ,mean , and average interchangeably.
The second approach is model-free . When the probability distribution (i.e., the model)
ofXis unknown, suppose that we have some samples fx1;x2;:::;xngofX. Then,
the mean can be approximated as
E[X]x=1
nnX
j=1xj:
Whennis small, this approximation may not be accurate. However, as nincreases,
the approximation becomes increasingly accurate. When n!1 , we have x!E[X].
78

## 第92页

5.1. Motivating example: Mean estimation
This is guaranteed by the law of large numbers : the average of a large number of
samples is close to the expected value. The law of large numbers is introduced in
Box 5.1.
The following example illustrates the two approaches described above. Consider a
coin 
ipping game. Let random variable Xdenote which side is showing when the coin
lands.Xhas two possible values: X= 1 when the head is showing, and X= 1 when
the tail is showing. Suppose that the true probability distribution (i.e., the model) of X
is
p(X= 1) = 0:5; p(X= 1) = 0:5:
If the probability distribution is known in advance, we can directly calculate the mean as
E[X] = 0:51 + 0:5( 1) = 0:
If the probability distribution is unknown, then we can 
ip the coin many times and
record the sampling results fxign
i=1. By calculating the average of the samples, we can
obtain an estimate of the mean. As shown in Figure 5.2, the estimated mean becomes
increasingly accurate as the number of samples increases.
0 50 100 150 200
Sample index-2-1012
samples
average
Figure 5.2: An example for demonstrating the law of large numbers. Here, the samples are drawn from
f+1; 1gfollowing a uniform distribution. The average of the samples gradually converges to zero, which
is the true expected value, as the number of samples increases.
It is worth mentioning that the samples used for mean estimation must be independent
and identically distributed (i.i.d. or iid). Otherwise, if the sampling values correlate, it
may be impossible to correctly estimate the expected value. An extreme case is that
all the sampling values are the same as the rst one, whatever the rst one is. In this
case, the average of the samples is always equal to the rst sample, no matter how many
samples we use.
79

## 第93页

5.2. MC Basic: The simplest MC-based algorithm
Box 5.1: Law of large numbers
For a random variable X, suppose thatfxign
i=1are some i.i.d. samples. Let  x=
1
nPn
i=1xibe the average of the samples. Then,
E[x] =E[X];
var[x] =1
nvar[X]:
The above two equations indicate that  xis an unbiased estimate of E[X], and its
variance decreases to zero as nincreases to innity.
The proof is given below.
First, E[x] =EPn
i=1xi=n
=Pn
i=1E[xi]=n=E[X], where the last equability is
due to the fact that the samples are identically distributed (that is, E[xi] =E[X]).
Second, var( x) = varPn
i=1xi=n
=Pn
i=1var[xi]=n2= (nvar[X])=n2=
var[X]=n, where the second equality is due to the fact that the samples are indepen-
dent, and the third equability is a result of the samples being identically distributed
(that is, var[ xi] = var[X]).
5.2 MC Basic: The simplest MC-based algorithm
This section introduces the rst and the simplest MC-based reinforcement learning algo-
rithm. This algorithm is obtained by replacing the model-based policy evaluation step in
the policy iteration algorithm introduced in Section 4.2 with a model-free MC estimation
step.
5.2.1 Converting policy iteration to be model-free
There are two steps in every iteration of the policy iteration algorithm (see Section 4.2).
The rst step is policy evaluation , which aims to compute vkby solving vk=rk+

Pkvk. The second step is policy improvement , which aims to compute the greedy
policyk+1= arg max (r+
Pvk). The elementwise form of the policy improvement
step is
k+1(s) = arg max
X
a(ajs)"X
rp(rjs;a)r+
X
s0p(s0js;a)vk(s0)#
= arg max
X
a(ajs)qk(s;a); s2S:
It must be noted that the action values lie in the core of these two steps. Specically.
in the rst step, the state values are calculated for the purpose of calculating the action
80

## 第94页

5.2. MC Basic: The simplest MC-based algorithm
values. In the second step, the new policy is generated based on the calculated action
values. Let us reconsider how we can calculate the action values. Two approaches are
available.
The rst is a model-based approach. This is the approach adopted by the policy
iteration algorithm. In particular, we can rst calculate the state value vkby solving
the Bellman equation. Then, we can calculate the action values by using
qk(s;a) =X
rp(rjs;a)r+
X
s0p(s0js;a)vk(s0): (5.1)
This approach requires the system model fp(rjs;a);p(s0js;a)gto be known.
The second is a model-free approach. Recall that the denition of an action value is
qk(s;a) =E[GtjSt=s;At=a]
=E[Rt+1+
Rt+2+
2Rt+3+:::jSt=s;At=a];
which is the expected return obtained when starting from ( s;a). Sinceqk(s;a) is an
expectation, it can be estimated by MC methods as demonstrated in Section 5.1. To
do that, starting from ( s;a), the agent can interact with the environment by following
policykand then obtain a certain number of episodes. Suppose that there are n
episodes and that the return of the ith episode is g(i)
k(s;a). Then,qk(s;a) can be
approximated as
qk(s;a) =E[GtjSt=s;At=a]1
nnX
i=1g(i)
k(s;a): (5.2)
We already know that, if the number of episodes nis suciently large, the approxi-
mation will be suciently accurate according to the law of large numbers.
The fundamental idea of MC-based reinforcement learning is to use a model-free
method for estimating action values, as shown in (5.2), to replace the model-based method
in the policy iteration algorithm.
5.2.2 The MC Basic algorithm
We are now ready to present the rst MC-based reinforcement learning algorithm. S-
tarting from an initial policy 0, the algorithm has two steps in the kth iteration ( k=
0;1;2;:::).
Step 1: Policy evaluation. This step is used to estimate qk(s;a) for all (s;a). Specif-
ically, for every ( s;a), we collect suciently many episodes and use the average of the
returns, denoted as qk(s;a), to approximate qk(s;a).
81

## 第95页

5.2. MC Basic: The simplest MC-based algorithm
Algorithm 5.1: MC Basic (a model-free variant of policy iteration)
Initialization: Initial guess 0.
Goal: Search for an optimal policy.
For thekth iteration ( k= 0;1;2;::: ), do
For every state s2S, do
For every action a2A(s), do
Collect suciently many episodes starting from (s;a)by following k
Policy evaluation:
qk(s;a)qk(s;a) = the average return of all the episodes starting from
(s;a)
Policy improvement:
a
k(s) = arg max aqk(s;a)
k+1(ajs) = 1 ifa=a
k, andk+1(ajs) = 0 otherwise
Step 2: Policy improvement. This step solves k+1(s) = arg max P
a(ajs)qk(s;a) for
alls2S. The greedy optimal policy is k+1(a
kjs) = 1 where a
k= arg max aqk(s;a).
This is the simplest MC-based reinforcement learning algorithm, which is called MC
Basic in this book. The pseudocode of the MC Basic algorithm is given in Algorithm 5.1.
As can be seen, it is very similar to the policy iteration algorithm. The only dierence is
that it calculates action values directly from experience samples, whereas policy iteration
calculates state values rst and then calculates the action values based on the system
model. It should be noted that the model-free algorithm directly estimates action values.
Otherwise, if it estimates state values instead, we still need to calculate action values
from these state values using the system model, as shown in (5.1).
Since policy iteration is convergent, MC Basic is also convergent when given su-
cient samples. That is, for every ( s;a), suppose that there are suciently many episodes
starting from ( s;a). Then, the average of the returns of these episodes can accurately ap-
proximate the action value of ( s;a). In practice, we usually do not have sucient episodes
for every (s;a). As a result, the approximation of the action values may not be accurate.
Nevertheless, the algorithm usually can still work. This is similar to the truncated policy
iteration algorithm, where the action values are neither accurately calculated.
Finally, MC Basic is too simple to be practical due to its low sample eciency. The
reason why we introduce this algorithm is to let readers grasp the core idea of MC-
based reinforcement learning. It is important to understand this algorithm well before
studying more complex algorithms introduced later in this chapter. We will see that more
complex and sample-ecient algorithms can be readily obtained by extending the MC
Basic algorithm.
82

## 第96页

5.2. MC Basic: The simplest MC-based algorithm
5.2.3 Illustrative examples
A simple example: A step-by-step implementation
s1 s2 s3
s4 s5 s6
s7 s8 s9
Figure 5.3: An example for illustrating the MC Basic algorithm.
We next use an example to demonstrate the implementation details of the MC Basic
algorithm. The reward settings are rboundary =rforbidden = 1 andrtarget = 1. The
discount rate is 
= 0:9. The initial policy 0is shown in Figure 5.3. This initial policy
is not optimal for s1ors3.
While all the action values should be calculated, we merely present those of s1due
to space limitations. At s1, there are ve possible actions. For each action, we need
to collect many episodes that are suciently long to eectively approximate the action
value. However, since this example is deterministic in terms of both the policy and model,
running multiple times would generate the same trajectory. As a result, the estimation
of each action value merely requires a single episode.
Following0, we can obtain the following episodes by respectively starting from
(s1;a1), (s1;a2),:::, (s1;a5).
Starting from ( s1;a1), the episode is s1a1  !s1a1  !s1a1  !:::. The action value equals
the discounted return of the episode:
q0(s1;a1) = 1 +
( 1) +
2( 1) += 1
1 
:
Starting from ( s1;a2), the episode is s1a2  !s2a3  !s5a3  !:::. The action value equals
the discounted return of the episode:
q0(s1;a2) = 0 +
0 +
20 +
3(1) +
4(1) +=
3
1 
:
Starting from ( s1;a3), the episode is s1a3  !s4a2  !s5a3  !:::. The action value equals
83

## 第97页

5.2. MC Basic: The simplest MC-based algorithm
the discounted return of the episode:
q0(s1;a3) = 0 +
0 +
20 +
3(1) +
4(1) +=
3
1 
:
Starting from ( s1;a4), the episode is s1a4  !s1a1  !s1a1  !:::. The action value equals
the discounted return of the episode:
q0(s1;a4) = 1 +
( 1) +
2( 1) += 1
1 
:
Starting from ( s1;a5), the episode is s1a5  !s1a1  !s1a1  !:::. The action value equals
the discounted return of the episode:
q0(s1;a5) = 0 +
( 1) +
2( 1) += 

1 
:
By comparing the ve action values, we see that
q0(s1;a2) =q0(s1;a3) =
3
1 
>0
are the maximum values. As a result, the new policy can be obtained as
1(a2js1) = 1 or 1(a3js1) = 1:
It is intuitive that the improved policy, which takes either a2ora3ats1, is optimal.
Therefore, we can successfully obtain an optimal policy by using merely one iteration
for this simple example. In this simple example, the initial policy is already optimal for
all the states except s1ands3. Therefore, the policy can become optimal after merely
a single iteration. When the policy is nonoptimal for other states, more iterations are
needed.
A comprehensive example: Episode length and sparse rewards
We next discuss some interesting properties of the MC Basic algorithm by examining
a more comprehensive example. The example is a 5-by-5 grid world (Figure 5.4). The
reward settings are rboundary = 1,rforbidden = 10, andrtarget = 1. The discount rate is

= 0:9.
First, we demonstrate that the episode length greatly impacts the nal optimal poli-
cies. In particular, Figure 5.4 shows the nal results generated by the MC Basic algorithm
with dierent episode lengths. When the length of each episode is too short, neither the
policy nor the value estimate is optimal (see Figures 5.4(a)-(d)). In the extreme case
where the episode length is one, only the states that are adjacent to the target have
84

## 第98页

5.2. MC Basic: The simplest MC-based algorithm
1 2 3 4 5Episode length=1
1
2
3
4
50.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 1.0 0.0 0.0
0.0 1.0 1.0 1.0 0.0
0.0 0.0 1.0 0.0 0.0
1 2 3 4 5Episode length=1
1
2
3
4
5
(a) Final value and policy with episode length=1
1 2 3 4 5Episode length=2
1
2
3
4
50.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 1.9 0.0 0.0
0.0 1.9 1.9 1.9 0.0
0.0 0.9 1.9 0.9 0.0
1 2 3 4 5Episode length=2
1
2
3
4
5 (b) Final value and policy with episode length=2
1 2 3 4 5Episode length=3
1
2
3
4
50.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 2.7 0.0 0.0
0.0 2.7 2.7 2.7 0.0
0.0 1.7 2.7 1.7 0.8
1 2 3 4 5Episode length=3
1
2
3
4
5
(c) Final value and policy with episode length=3
1 2 3 4 5Episode length=4
1
2
3
4
50.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0
0.0 0.0 3.4 0.0 0.0
0.0 3.4 3.4 3.4 0.7
0.0 2.4 3.4 2.4 1.5
1 2 3 4 5Episode length=4
1
2
3
4
5 (d) Final value and policy with episode length=4
.........
1 2 3 4 5Episode length=14
1
2
3
4
51.2 1.6 2.0 2.5 3.0
0.9 1.2 2.5 3.0 3.6
0.5 0.3 7.7 3.6 4.3
0.3 7.7 7.7 7.7 5.0
0.0 6.7 7.7 6.7 5.8
1 2 3 4 5Episode length=14
1
2
3
4
5
(e) Final value and policy with episode length=14
1 2 3 4 5Episode length=15
1
2
3
4
51.4 1.8 2.2 2.7 3.3
1.1 1.4 2.7 3.3 3.8
0.8 0.5 7.9 3.8 4.5
0.5 7.9 7.9 7.9 5.2
0.2 6.9 7.9 6.9 6.0
1 2 3 4 5Episode length=15
1
2
3
4
5 (f) Final value and policy with episode length=15
1 2 3 4 5Episode length=30
1
2
3
4
53.1 3.5 3.9 4.4 4.9
2.7 3.1 4.4 4.9 5.5
2.4 2.1 9.6 5.5 6.1
2.1 9.6 9.6 9.6 6.9
1.9 8.6 9.6 8.6 7.7
1 2 3 4 5Episode length=30
1
2
3
4
5
(g) Final value and policy with episode length=30
1 2 3 4 5Episode length=100
1
2
3
4
53.5 3.9 4.3 4.8 5.3
3.1 3.5 4.8 5.3 5.9
2.8 2.5 10.0 5.9 6.6
2.5 10.0 10.0 10.0 7.3
2.3 9.0 10.0 9.0 8.1
1 2 3 4 5Episode length=100
1
2
3
4
5 (h) Final value and policy with episode length=100
Figure 5.4: The policies and state values obtained by the MC Basic algorithm when given dierent
episode lengths. Only if the length of each episode is suciently long, can the state values be accurately
estimated.
85

## 第99页

5.3. MC Exploring Starts
nonzero values, and all the other states have zero values since each episode is too short
to reach the target or get positive rewards (see Figure 5.4(a)). As the episode length
increases, the policy and value estimates gradually approach the optimal ones (see Fig-
ure 5.4(h)).
As the episode length increases, an interesting spatial pattern emerges. That is, the
states that are closer to the target possess nonzero values earlier than those that are
farther away. The reason for this phenomenon is as follows. Starting from a state, the
agent must travel at least a certain number of steps to reach the target state and then
receive positive rewards. If the length of an episode is less than the minimum desired
number of steps, it is certain that the return is zero, and so is the estimated state value. In
this example, the episode length must be no less than 15, which is the minimum number
of steps required to reach the target when starting from the bottom-left state.
While the above analysis suggests that each episode must be suciently long, the
episodes are not necessarily innitely long. As shown in Figure 5.4(g), when the length
is 30, the algorithm can nd an optimal policy, although the value estimate is not yet
optimal.
The above analysis is related to an important reward design problem, sparse reward ,
which refers to the scenario in which no positive rewards can be obtained unless the target
is reached. The sparse reward setting requires long episodes that can reach the target.
This requirement is challenging to satisfy when the state space is large. As a result,
the sparse reward problem downgrades the learning eciency. One simple technique for
solving this problem is to design nonsparse rewards . For instance, in the above grid world
example, we can redesign the reward setting so that the agent can obtain a small positive
reward when reaching the states near the target. In this way, an \attractive eld" can
be formed around the target so that the agent can nd the target more easily. More
information about sparse reward problems can be found in [17{19].
5.3 MC Exploring Starts
We next extend the MC Basic algorithm to obtain another MC-based reinforcement
learning algorithm that is slightly more complicated but more sample-ecient.
5.3.1 Utilizing samples more eciently
An important aspect of MC-based reinforcement learning is how to use samples more
eciently. Specically, suppose that we have an episode of samples obtained by following
a policy:
s1a2  !s2a4  !s1a2  !s2a3  !s5a1  !::: (5.3)
86

## 第100页

5.3. MC Exploring Starts
where the subscripts refer to the state or action indexes rather than time steps. Every
time a state-action pair appears in an episode, it is called a visit of that state-action pair.
Dierent strategies can be employed to utilize the visits.
The rst and simplest strategy is to use the initial visit . That is, an episode is only
used to estimate the action value of the initial state-action pair that the episode starts
from. For the example in (5.3), the initial-visit strategy merely estimates the action
value of (s1;a2). The MC Basic algorithm utilizes the initial-visit strategy. However, this
strategy is not sample-ecient because the episode also visits many other state-action
pairs such as ( s2;a4), (s2;a3), and (s5;a1). These visits can also be used to estimate the
corresponding action values. In particular, we can decompose the episode in (5.3) into
multiple subepisodes:
s1a2  !s2a4  !s1a2  !s2a3  !s5a1  !::: [original episode]
s2a4  !s1a2  !s2a3  !s5a1  !::: [subepisode starting from ( s2;a4)]
s1a2  !s2a3  !s5a1  !::: [subepisode starting from ( s1;a2)]
s2a3  !s5a1  !::: [subepisode starting from ( s2;a3)]
s5a1  !::: [subepisode starting from ( s5;a1)]
The trajectory generated after the visit of a state-action pair can be viewed as a new
episode. These new episodes can be used to estimate more action values. In this way,
the samples in the episode can be utilized more eciently.
Moreover, a state-action pair may be visited multiple times in an episode. For exam-
ple, (s1;a2) is visited twice in the episode in (5.3). If we only count the rst-time visit,
this is called a rst-visit strategy. If we count every visit of a state-action pair, such a
strategy is called every-visit [20].
In terms of sample usage eciency, the every-visit strategy is the best. If an episode
is suciently long such that it can visit all the state-action pairs many times, then this
single episode may be sucient for estimating all the action values using the every-visit
strategy. However, the samples obtained by the every-visit strategy are correlated because
the trajectory starting from the second visit is merely a subset of the trajectory starting
from the rst visit. Nevertheless, the correlation would not be strong if the two visits are
far away from each other in the trajectory.
5.3.2 Updating policies more eciently
Another aspect of MC-based reinforcement learning is when to update the policy. Two
strategies are available.
The rst strategy is, in the policy evaluation step, to collect all the episodes starting
from the same state-action pair and then approximate the action value using the
average return of these episodes . This strategy is adopted in the MC Basic algorithm.
87

## 第101页

5.3. MC Exploring Starts
Algorithm 5.2: MC Exploring Starts (an ecient variant of MC Basic)
Initialization: Initial policy 0(ajs)and initial value q(s;a)for all (s;a). Returns (s;a) =
0and Num (s;a) = 0 for all (s;a).
Goal: Search for an optimal policy.
For each episode, do
Episode generation: Select a starting state-action pair (s0;a0)and ensure that all
pairs can be possibly selected (this is the exploring-starts condition). Following the
current policy, generate an episode of length T:s0;a0;r1;:::;sT 1;aT 1;rT.
Initialization for each episode: g 0
For each step of the episode, t=T 1;T 2;:::; 0, do
g 
g+rt+1
Returns (st;at) Returns (st;at) +g
Num(st;at) Num(st;at) + 1
Policy evaluation:
q(st;at) Returns (st;at)=Num(st;at)
Policy improvement:
(ajst) = 1 ifa= arg max aq(st;a)and(ajst) = 0 otherwise
The drawback of this strategy is that the agent must wait until all the episodes have
been collected before the estimate can be updated.
The second strategy, which can overcome this drawback, is to use the return of a
single episode to approximate the corresponding action value. In this way, we can
immediately obtain a rough estimate when we receive an episode. Then, the policy
can be improved in an episode-by-episode fashion.
Since the return of a single episode cannot accurately approximate the corresponding
action value, one may wonder whether the second strategy is good. In fact, this strategy
falls into the scope of generalized policy iteration introduced in the last chapter. That is,
we can still update the policy even if the value estimate is not suciently accurate.
5.3.3 Algorithm description
We can use the techniques introduced in Sections 5.3.1 and 5.3.2 to enhance the
eciency of the MC Basic algorithm. Then, a new algorithm called MC Exploring Starts
can be obtained.
The details of MC Exploring Starts are given in Algorithm 5.2. This algorithm uses
the every-visit strategy. Interestingly, when calculating the discounted return obtained
by starting from each state-action pair, the procedure starts from the ending states and
travels back to the starting state. Such techniques can make the algorithm more ecient,
but it also makes the algorithm more complex. This is why the MC Basic algorithm,
88

## 第102页

5.4. MC-Greedy: Learning without exploring starts
which is free of such techniques, is introduced rst to reveal the core idea of MC-based
reinforcement learning.
The exploring starts condition requires suciently many episodes starting from every
state-action pair. Only if every state-action pair is well explored, can we accurately
estimate their action values (according to the law of large numbers) and hence successfully
nd optimal policies. Otherwise, if an action is not well explored, its action value may
be inaccurately estimated, and this action may not be selected by the policy even though
it is indeed the best action. Both MC Basic and MC Exploring Starts require this
condition. However, this condition is dicult to meet in many applications, especially
those involving physical interactions with environments. Can we remove the exploring
starts requirement? The answer is yes, as shown in the next section.
5.4 MC-Greedy: Learning without exploring starts
We next extend the MC Exploring Starts algorithm by removing the exploring starts
condition. This condition actually requires that every state-action pair can be visited
suciently many times, which can also be achieved based on soft policies.
5.4.1-greedy policies
A policy is softif it has a positive probability of taking any action at any state. Consider
an extreme case in which we only have a single episode. With a soft policy, a single
episode that is suciently long can visit every state-action pair many times (see the
examples in Figure 5.8). Thus, we do not need to generate a large number of episodes
starting from dierent state-action pairs, and then the exploring starts requirement can
be removed.
One type of common soft policies is -greedy policies. An -greedy policy is a stochastic
policy that has a higher chance of choosing the greedy action and the same nonzero
probability of taking any other action. Here, the greedy action refers to the action with
the greatest action value. In particular, suppose that 2[0;1]. The corresponding
-greedy policy has the following form:
(ajs) =8
>>><
>>>:1 
jA(s)j(jA(s)j 1);for the greedy action,

jA(s)j; for the otherjA(s)j 1 actions,
wherejA(s)jdenotes the number of actions associated with s.
When= 0,-greedy becomes greedy. When = 1, the probability of taking any
action equals1
jA(s)j.
The probability of taking the greedy action is always greater than that of taking any
89

## 第103页

5.4. MC-Greedy: Learning without exploring starts
other action because
1 
jA(s)j(jA(s)j 1) = 1 +
jA(s)j
jA(s)j
for any2[0;1].
While an-greedy policy is stochastic, how can we select an action by following such
a policy? We can rst generate a random number xin [0;1] by following a uniform
distribution. If x, then we select the greedy action. If x< , then we randomly select
an action inA(s) with the probability of1
jA(s)j(we may select the greedy action again).
In this way, the total probability of selecting the greedy action is 1  +
jA(s)j, and the
probability of selecting any other action is
jA(s)j.
5.4.2 Algorithm description
To integrate -greedy policies into MC learning, we only need to change the policy im-
provement step from greedy to -greedy.
In particular, the policy improvement step in MC Basic or MC Exploring Starts aims
to solve
k+1(s) = arg max
2X
a(ajs)qk(s;a); (5.4)
where  denotes the set of all possible policies . We know that the solution of (5.4) is a
greedy policy:
k+1(ajs) =(
1; a=a
k;
0; a6=a
k;
wherea
k= arg max aqk(s;a).
Now, the policy improvement step is changed to solve
k+1(s) = arg max
2X
a(ajs)qk(s;a); (5.5)
where  denotes the set of all -greedy policies with a given value of . In this way, we
force the policy to be -greedy. The solution of (5.5) is
k+1(ajs) =(
1 jA(s)j 1
jA(s)j; a =a
k;
1
jA(s)j; a6=a
k;
wherea
k= arg max aqk(s;a). With the above change, we obtain another algorithm
called MC-Greedy . The details of this algorithm are given in Algorithm 5.3. Here, the
every-visit strategy is employed to better utilize the samples.
90

## 第104页

5.4. MC-Greedy: Learning without exploring starts
Algorithm 5.3: MC -Greedy (a variant of MC Exploring Starts)
Initialization: Initial policy 0(ajs)and initial value q(s;a)for all (s;a). Returns (s;a) =
0and Num (s;a) = 0 for all (s;a).2(0;1]
Goal: Search for an optimal policy.
For each episode, do
Episode generation: Select a starting state-action pair (s0;a0)(the exploring starts
condition is not required). Following the current policy, generate an episode of length
T:s0;a0;r1;:::;sT 1;aT 1;rT.
Initialization for each episode: g 0
For each step of the episode, t=T 1;T 2;:::; 0, do
g 
g+rt+1
Returns (st;at) Returns (st;at) +g
Num(st;at) Num(st;at) + 1
Policy evaluation:
q(st;at) Returns (st;at)=Num(st;at)
Policy improvement:
Leta= arg max aq(st;a)and
(ajst) =(
1 jA(st)j 1
jA(st)j; a =a
1
jA(st)j; a6=a
If greedy policies are replaced by -greedy policies in the policy improvement step,
can we still guarantee to obtain optimal policies? The answer is both yes and no. By yes,
we mean that, when given sucient samples, the algorithm can converge to an -greedy
policy that is optimal in the set  . By no, we mean that the policy is merely optimal in
but may not be optimal in . However, if is suciently small, the optimal policies
in are close to those in .
5.4.3 Illustrative examples
Consider the grid world example shown in Figure 5.5. The aim is to nd the optimal
policy for every state. A single episode with one million steps is generated in every
iteration of the MC -Greedy algorithm. Here, we deliberately consider the extreme case
with merely one single episode. We set rboundary =rforbidden = 1,rtarget = 1, and
= 0:9.
The initial policy is a uniform policy that has the same probability 0.2 of taking
any action, as shown in Figure 5.5. The optimal -greedy policy with = 0:5 can be
obtained after two iterations. Although each iteration merely uses a single episode, the
policy gradually improves because all the state-action pairs can be visited and hence their
values can be accurately estimated.
91

## 第105页

5.5. Exploration and exploitation of -greedy policies
1 2 3 4 5
1
2
3
4
5
(a) Initial policy
1 2 3 4 5
1
2
3
4
5 (b) After the rst iteration
1 2 3 4 5
1
2
3
4
5 (c) After the second iteration
Figure 5.5: The evolution process of the MC -Greedy algorithm based on single episodes.
5.5 Exploration and exploitation of -greedy policies
Exploration andexploitation constitute a fundamental tradeo in reinforcement learning.
Here, exploration means that the policy can possibly take as many actions as possible.
In this way, all the actions can be visited and evaluated well. Exploitation means that
the improved policy should take the greedy action that has the greatest action value.
However, since the action values obtained at the current moment may not be accurate
due to insucient exploration, we should keep exploring while conducting exploitation
to avoid missing optimal actions.
-greedy policies provide one way to balance exploration and exploitation. On the
one hand, an -greedy policy has a higher probability of taking the greedy action so that
it can exploit the estimated values. On the other hand, the -greedy policy also has a
chance to take other actions so that it can keep exploring. -greedy policies are used
not only in MC-based reinforcement learning but also in other reinforcement learning
algorithms such as temporal-dierence learning as introduced in Chapter 7.
Exploitation is related to optimality because optimal policies should be greedy. The
fundamental idea of -greedy policies is to enhance exploration by sacricing optimal-
ity/exploitation. If we would like to enhance exploitation and optimality, we need to
reduce the value of . However, if we would like to enhance exploration, we need to
increase the value of .
We next discuss this tradeo based on some interesting examples. The reinforce-
ment learning task here is a 5-by-5 grid world. The reward settings are rboundary = 1,
rforbidden = 10, andrtarget = 1. The discount rate is 
= 0:9.
Optimality of -greedy policies
We next show that the optimality of -greedy policies becomes worse when increases.
First, a greedy optimal policy and the corresponding optimal state values are shown
in Figure 5.6(a). The state values of some consistent-greedy policies are shown in
92

## 第106页

5.5. Exploration and exploitation of -greedy policies
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
53.5 3.9 4.3 4.8 5.3
3.1 3.5 4.8 5.3 5.9
2.8 2.5 10.0 5.9 6.6
2.5 10.0 10.0 10.0 7.3
2.3 9.0 10.0 9.0 8.1
(a) A given -greedy policy and its state values: = 0
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
50.4 0.5 0.9 1.3 1.4
0.1 0.0 0.5 1.3 1.7
0.1 -0.4 3.4 1.4 1.9
-0.1 3.4 3.3 3.7 2.2
-0.3 2.6 3.7 3.1 2.7
(b) A given -greedy policy and its state values: = 0:1
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
5-2.2 -2.4 -2.1 -1.7 -1.8
-2.5 -3.0 -3.3 -2.3 -2.0
-2.3 -3.3 -2.5 -2.8 -2.2
-2.5 -2.5 -2.8 -2.0 -2.4
-2.8 -3.2 -2.1 -2.3 -2.2
(c) A given -greedy policy and its state values: = 0:2
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
5-8.0 -9.0 -8.4 -7.2 -7.8
-8.7 -10.8 -12.4 -9.6 -8.9
-8.3 -12.3 -15.3 -12.3 -10.5
-9.7 -15.5 -17.0 -14.4 -12.2
-10.9 -16.7 -15.2 -14.3 -12.4
(d) A given -greedy policy and its state values: = 0:5
Figure 5.6: The state values of some -greedy policies. These -greedy policies are consistent with each
other in the sense that the actions with the greatest probabilities are the same. It can be seen that,
when the value of increases, the state values of the -greedy policies decrease and hence their optimality
becomes worse.
93

## 第107页

5.5. Exploration and exploitation of -greedy policies
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
53.5 3.9 4.3 4.8 5.3
3.1 3.5 4.8 5.3 5.9
2.8 2.5 10.0 5.9 6.6
2.5 10.0 10.0 10.0 7.3
2.3 9.0 10.0 9.0 8.1
(a) The optimal -greedy policy and its state values: = 0
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
50.4 0.5 0.9 1.3 1.4
0.1 0.0 0.5 1.3 1.7
0.1 -0.4 3.4 1.4 1.9
-0.1 3.4 3.3 3.7 2.2
-0.3 2.6 3.7 3.1 2.7
(b) The optimal -greedy policy and its state values: = 0:1
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
5-1.1 -1.5 -1.1 -0.6 -0.6
-1.5 -2.2 -2.3 -1.0 -0.6
-1.2 -2.4 -2.2 -1.5 -0.6
-1.6 -2.3 -2.6 -1.4 -1.1
-2.0 -3.0 -1.8 -1.4 -1.0
(c) The optimal -greedy policy and its state values: = 0:2
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
5-4.3 -5.5 -4.5 -2.6 -2.3
-5.6 -7.7 -7.7 -4.1 -2.4
-5.5 -9.0 -8.0 -5.6 -2.8
-6.8 -8.9 -9.4 -5.5 -4.2
-7.9 -10.1 -6.7 -5.1 -3.7
(d) The optimal -greedy policy and its state values: = 0:5
Figure 5.7: The optimal -greedy policies and their corresponding state values under dierent values of
. Here, these -greedy policies are optimal among all -greedy ones (with the same value of ). It can
be seen that, when the value of increases, the optimal -greedy policies are no longer consistent with
the optimal one as in (a).
94

## 第108页

5.5. Exploration and exploitation of -greedy policies
Figures 5.6(b)-(d). Here, two -greedy policies are consistent if the actions with the
greatest probabilities in the policies are the same.
As the value of increases, the state values of the -greedy policies decrease, indicating
that the optimality of these -greedy policies becomes worse. Notably, the value of
the target state becomes the smallest when is as large as 0 :5. This is because, when
is large, the agent starting from the target area may enter the surrounding forbidden
areas and hence receive negative rewards with a higher probability.
Second, Figure 5.7 shows the optimal -greedy policies (they are optimal in  ). When
= 0, the policy is greedy and optimal among all policies. When is as small as 0.1,
the optimal -greedy policy is consistent with the optimal greedy one. However, when
increases to, for example, 0 :2, the obtained -greedy policies are not consistent with
the optimal greedy one. Therefore, if we want to obtain -greedy policies that are
consistent with the optimal greedy ones, the value of should be suciently small.
Why are the -greedy policies inconsistent with the optimal greedy one when is
large? We can answer this question by considering the target state. In the greedy
case, the optimal policy at the target state is to stay still to gain positive rewards.
However, when is large, there is a high chance of entering the forbidden areas and
receiving negative rewards. Therefore, the optimal policy at the target state in this
case is to escape instead of staying still.
Exploration abilities of -greedy policies
We next illustrate that the exploration ability of an -greedy policy is strong when is
large.
First, consider an -greedy policy with = 1 (see Figure 5.5(a)). In this case, the
exploration ability of the -greedy policy is strong since it has a 0.2 probability of taking
any action at any state. Starting from ( s1;a1), an episode generated by the -policy is
given in Figures 5.8(a)-(c). It can be seen that this single episode can visit all the state-
action pairs many times when the episode is suciently long due to the strong exploration
ability of the policy. Moreover, the numbers of times that all the state-action pairs are
visited are almost even, as shown in Figure 5.8(d).
Second, consider an -policy with = 0:5 (see Figure 5.6(d)). In this case, the -greedy
policy has a weaker exploration ability than the case of = 1. Starting from ( s1;a1), an
episode generated by the -policy is given in Figures 5.8(e)-(g). Although every action
can still be visited when the episode is suciently long, the distribution of the number
of visits may be extremely uneven. For example, given an episode with one million steps,
some actions are visited more than 250,000 times, while most actions are visited merely
hundreds or even tens of times, as shown in Figure 5.8(h).
The above examples demonstrate that the exploration abilities of -greedy policies
decrease when decreases. One useful technique is to initially set to be large to enhance
95

## 第109页

5.5. Exploration and exploitation of -greedy policies
1 2 3 4 5
1
2
3
4
5
(a)= 1, trajectory of 100 steps
1 2 3 4 5
1
2
3
4
5
(b)= 1, trajectory of 1,000 steps
1 2 3 4 5
1
2
3
4
5
(c)= 1, trajectory of 10,000 steps
20406080100120
State-action index76007700780079008000810082008300Visited times
(d)= 1, number of times each action is vis-
ited within 1 million steps
1 2 3 4 5
1
2
3
4
5(e)= 0:5, trajectory of 100 steps
1 2 3 4 5
1
2
3
4
5
(f)= 0:5, trajectory of 1,000 steps
1 2 3 4 5
1
2
3
4
5
(g)= 0:5, trajectory of 10,000 steps
20406080100120
State-action index00.511.522.53Visited times105
(h)= 0:5, number of times each action is
visited within 1 million steps
Figure 5.8: Exploration abilities of -greedy policies with dierent values of .
96

## 第110页

5.6. Summary
exploration and gradually reduce it to ensure the optimality of the nal policy [21{23].
5.6 Summary
The algorithms in this chapter are the rst model-free reinforcement learning algorithms
ever introduced in this book. We rst introduced the idea of MC estimation by exam-
ining an important mean estimation problem. Then, three MC-based algorithms were
introduced.
MC Basic: This is the simplest MC-based reinforcement learning algorithm. This al-
gorithm is obtained by replacing the model-based policy evaluation step in the policy
iteration algorithm with a model-free MC-based estimation component. Given su-
cient samples, it is guaranteed that this algorithm can converge to optimal policies
and optimal state values.
MC Exploring Starts: This algorithm is a variant of MC Basic. It can be obtained
from the MC Basic algorithm using the rst-visit or every-visit strategy to use samples
more eciently.
MC-Greedy: This algorithm is a variant of MC Exploring Starts. Specically, in the
policy improvement step, it searches for the best -greedy policies instead of greedy
policies. In this way, the exploration ability of the policy is enhanced and hence the
condition of exploring starts can be removed.
Finally, a tradeo between exploration and exploitation was introduced by examining
the properties of -greedy policies. As the value of increases, the exploration ability
of-greedy policies increases, and the exploitation of greedy actions decreases. On the
other hand, if the value of decreases, we can better exploit the greedy actions, but the
exploration ability is compromised.
5.7 Q&A
Q: What is Monte Carlo estimation?
A: Monte Carlo estimation refers to a broad class of techniques that use stochastic
samples to solve approximation problems.
Q: What is the mean estimation problem?
A: The mean estimation problem refers to calculating the expected value of a random
variable based on stochastic samples.
Q: How to solve the mean estimation problem?
A: There are two approaches: model-based and model-free. In particular, if the proba-
bility distribution of a random variable is known, the expected value can be calculated
97

## 第111页

5.7. Q&A
based on its denition. If the probability distribution is unknown, we can use Monte
Carlo estimation to approximate the expected value. Such an approximation is accu-
rate when the number of samples is large.
Q: Why is the mean estimation problem important for reinforcement learning?
A: Both state and action values are dened as expected values of returns. Hence,
estimating state or action values is essentially a mean estimation problem.
Q: What is the core idea of model-free MC-based reinforcement learning?
A: The core idea is to convert the policy iteration algorithm to a model-free one.
In particular, while the policy iteration algorithm aims to calculate values based on
the system model, MC-based reinforcement learning replaces the model-based policy
evaluation step in the policy iteration algorithm with a model-free MC-based policy
evaluation step.
Q: What are initial-visit, rst-visit, and every-visit strategies?
A: They are dierent strategies for utilizing the samples in an episode. An episode
may visit many state-action pairs. The initial-visit strategy uses the entire episode to
estimate the action value of the initial state-action pair. The every-visit and rst-visit
strategies can better utilize the given samples. If the rest of the episode is used to
estimate the action value of a state-action pair every time it is visited, such a strategy
is called every-visit. If we only count the rst time a state-action pair is visited in the
episode, such a strategy is called rst-visit.
Q: What is exploring starts? Why is it important?
A: Exploring starts requires an innite number of (or suciently many) episodes to be
generated when starting from every state-action pair. In theory, the exploring starts
condition is necessary to nd optimal policies. That is, only if every action value is
well explored, can we accurately evaluate all the actions and then correctly select the
optimal ones.
Q: What is the idea used to avoid exploring starts?
A: The fundamental idea is to make policies soft. Soft policies are stochastic, enabling
an episode to visit many state-action pairs. In this way, we do not need a large number
of episodes starting from every state-action pair.
Q: Can an -greedy policy be optimal?
A: The answer is both yes and no. By yes, we mean that, if given sucient samples,
the MC-Greedy algorithm can converge to an optimal -greedy policy. By no, we
mean that the converged policy is merely optimal among all -greedy policies (with
the same value of ).
Q: Is it possible to use one episode to visit all state-action pairs?
98

## 第112页

5.7. Q&A
A: Yes, it is possible. If the policy is soft (e.g., -greedy) and the episode is suciently
long.
Q: What is the relationship between MC Basic, MC Exploring Starts, and MC -
Greedy?
A: MC Basic is the simplest MC-based reinforcement learning algorithm. It is impor-
tant because it reveals the fundamental idea of model-free MC-based reinforcement
learning. MC Exploring Starts is a variant of MC Basic that adjusts the sample us-
age strategy. Furthermore, MC -Greedy is a variant of MC Exploring Starts that
removes the exploring starts requirement. Therefore, while the basic idea is simple,
complication appears when we want to achieve better performance. It is important
to split the core idea from the complications that may be distracting for beginners.
99

## 第113页

5.7. Q&A
100

## 第114页

Chapter 6
Stochastic Approximation
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
Figure 6.1: Where we are in this book.
Chapter 5 introduced the rst class of model-free reinforcement learning algorithms
based on Monte Carlo estimation. In the next chapter (Chapter 7), we will introduce an-
other class of model-free reinforcement learning algorithms: temporal-dierence learning.
However, before proceeding to the next chapter, we need to press the pause button to
better prepare ourselves. This is because temporal-dierence algorithms are very dierent
from the algorithms that we have studied so far. Many readers who see the temporal-
dierence algorithms for the rst time often wonder how these algorithms were designed
in the rst place and why they can work eectively. In fact, there is a knowledge gap
between the previous and subsequent chapters: the algorithms we have studied so far are
101

## 第115页

6.1. Motivating example: Mean estimation
non-incremental , but the algorithms that we will study in the subsequent chapters are
incremental .
We use the present chapter to ll this knowledge gap by introducing the basics of
stochastic approximation. Although this chapter does not introduce any specic rein-
forcement learning algorithms, it lays the necessary foundations for studying subsequen-
t chapters. We will see in Chapter 7 that the temporal-dierence algorithms can be
viewed as special stochastic approximation algorithms. The well-known stochastic gradi-
ent descent algorithms widely used in machine learning are also introduced in the present
chapter.
6.1 Motivating example: Mean estimation
We next demonstrate how to convert a non-incremental algorithm to an incremental one
by examining the mean estimation problem.
Consider a random variable Xthat takes values from a nite set X. Our goal is to
estimate E[X]. Suppose that we have a sequence of i.i.d. samples fxign
i=1. The expected
value ofXcan be approximated by
E[X]x:=1
nnX
i=1xi: (6.1)
The approximation in (6.1) is the basic idea of Monte Carlo estimation, as introduced in
Chapter 5. We know that  x!E[X] asn!1 according to the law of large numbers.
We next show that two methods can be used to calculate  xin (6.1). The rst non-
incremental method collects all the samples rst and then calculates the average. The
drawback of such a method is that, if the number of samples is large, we may have to
wait for a long time until all of the samples are collected. The second method can avoid
this drawback because it calculates the average in an incremental manner. Specically,
suppose that
wk+1:=1
kkX
i=1xi; k = 1;2;:::
and hence
wk=1
k 1k 1X
i=1xi; k = 2;3;:::
Then,wk+1can be expressed in terms of wkas
wk+1=1
kkX
i=1xi=1
k k 1X
i=1xi+xk!
=1
k((k 1)wk+xk) =wk 1
k(wk xk):
102

## 第116页

6.2. Robbins-Monro algorithm
Therefore, we obtain the following incremental algorithm:
wk+1=wk 1
k(wk xk): (6.2)
This algorithm can be used to calculate the mean  xin an incremental manner. It can be
veried that
w1=x1;
w2=w1 1
1(w1 x1) =x1;
w3=w2 1
2(w2 x2) =x1 1
2(x1 x2) =1
2(x1+x2);
w4=w3 1
3(w3 x3) =1
3(x1+x2+x3);
...
wk+1=1
kkX
i=1xi: (6.3)
The advantage of (6.2) is that the average can be immediately calculated every time we
receive a sample. This average can be used to approximate  xand hence E[X]. Notably,
the approximation may not be accurate at the beginning due to insucient samples.
However, it is better than nothing. As more samples are obtained, the estimation accuracy
can be gradually improved according to the law of large numbers. In addition, one
can also dene wk+1=1
1+kPk+1
i=1xiandwk=1
kPk
i=1xi. Doing so would not make
any signicant dierence. In this case, the corresponding iterative algorithm is wk+1=
wk 1
1+k(wk xk+1).
Furthermore, consider an algorithm with a more general expression:
wk+1=wk k(wk xk): (6.4)
This algorithm is important and frequently used in this chapter. It is the same as (6.2)
except that the coecient 1 =kis replaced by k>0. Since the expression of kis not
given, we are not able to obtain the explicit expression of wkas in (6.3). However, we
will show in the next section that, if fkgsatises some mild conditions, wk!E[X] as
k!1 . In Chapter 7, we will see that temporal-dierence algorithms have similar (but
more complex) expressions.
6.2 Robbins-Monro algorithm
Stochastic approximation refers to a broad class of stochastic iterative algorithms for
solving root-nding or optimization problems [24]. Compared to many other root-nding
103

## 第117页

6.2. Robbins-Monro algorithm
algorithms such as gradient-based ones, stochastic approximation is powerful in the sense
that it does not require the expression of the objective function or its derivative.
The Robbins-Monro (RM) algorithm is a pioneering work in the eld of stochastic
approximation [24{27]. The famous stochastic gradient descent algorithm is a special
form of the RM algorithm, as shown in Section 6.4. We next introduce the details of the
RM algorithm.
Suppose that we would like to nd the root of the equation
g(w) = 0;
wherew2Ris the unknown variable and g:R!Ris a function. Many problems can be
formulated as root-nding problems. For example, if J(w) is an objective function to be
optimized, this optimization problem can be converted to solving g(w):=rwJ(w) = 0.
In addition, an equation such as g(w) =c, wherecis a constant, can also be converted
to the above equation by rewriting g(w) cas a new function.
If the expression of gor its derivative is known, there are many numerical algorithms
that can be used. However, the problem we are facing is that the expression of the
functiongis unknown. For example, the function may be represented by an articial
neural network whose structure and parameters are unknown. Moreover, we can only
obtain a noisy observation of g(w):
~g(w;) =g(w) +;
where2Ris the observation error, which may or may not be Gaussian. In summary,
it is a black-box system where only the input wand the noisy output ~ g(w;) are known
(see Figure 6.2). Our aim is to solve g(w) = 0 using wand ~g.
2
g(w) +ηw ˜g(w,η)
Fig. 1: xx
Figure 6.2: An illustration of the problem of solving g(w) = 0 from wand ~g.
The RM algorithm that can solve g(w) = 0 is
wk+1=wk ak~g(wk;k); k = 1;2;3;::: (6.5)
wherewkis thekth estimate of the root, ~ g(wk;k) is thekth noisy observation, and akis
a positive coecient. As can be seen, the RM algorithm does not require any information
about the function. It only requires the input and output.
104

## 第118页

6.2. Robbins-Monro algorithm
0 10 20 30 40 50012Estimated root wk
0 10 20 30 40 50
Iteration index k-202Observation noise k
Figure 6.3: An illustrative example of the RM algorithm.
To illustrate the RM algorithm, consider an example in which g(w) =w3 5. The
true root is 51=31:71. Now, suppose that we can only observe the input wand the
output ~g(w) =g(w) +, whereis i.i.d. and obeys a standard normal distribution
with a zero mean and a standard deviation of 1. The initial guess is w1= 0, and the
coecient is ak= 1=k. The evolution process of wkis shown in Figure 6.3. Even though
the observation is corrupted by noise k, the estimate wkcan still converge to the true
root. Note that the initial guess w1must be properly selected to ensure convergence
for the specic function of g(w) =w3 5. In the following subsection, we present the
conditions under which the RM algorithm converges for any initial guesses.
6.2.1 Convergence properties
Why can the RM algorithm in (6.5) nd the root of g(w) = 0? We next illustrate the
idea with an example and then provide a rigorous convergence analysis.
Consider the example shown in Figure 6.4. In this example, g(w) = tanh(w 1). The
true root of g(w) = 0 isw= 1. We apply the RM algorithm with w1= 3 andak= 1=k.
To better illustrate the reason for convergence, we simply set k0, and consequently,
~g(wk;k) =g(wk). The RM algorithm in this case is wk+1=wk akg(wk). The resulting
fwkggenerated by the RM algorithm is shown in Figure 6.4. It can be seen that wk
converges to the true root w= 1.
This simple example can illustrate why the RM algorithm converges.
Whenwk>w, we haveg(wk)>0. Then,wk+1=wk akg(wk)<wk. Ifakg(wk) is
suciently small, we have w<wk+1<wk. As a result, wk+1is closer to wthanwk.
Whenwk<w, we haveg(wk)<0. Then,wk+1=wk akg(wk)>wk. Ifjakg(wk)jis
suciently small, we have w>wk+1>wk. As a result, wk+1is closer to wthanwk.
In either case, wk+1is closer to wthanwk. Therefore, it is intuitive that wkconverges
tow.
105

## 第119页

6.2. Robbins-Monro algorithm
0.511.522.533.54
w-1-0.500.511.5g(w)
w1w2w3w4......
Figure 6.4: An example for illustrating the convergence of the RM algorithm.
The above example is simple since the observation error is assumed to be zero. It
would be nontrivial to analyze the convergence in the presence of stochastic observation
errors. A rigorous convergence result is given below.
Theorem 6.1 (Robbins-Monro theorem) .In the Robbins-Monro algorithm in (6.5) , if
(a) 0<c1rwg(w)c2for allw;
(b)P1
k=1ak=1andP1
k=1a2
k<1;
(c)E[kjHk] = 0 andE[2
kjHk]<1;
whereHk=fwk;wk 1;:::g, thenwkalmost surely converges to the root wsatisfying
g(w) = 0 .
We postpone the proof of this theorem to Section 6.3.3. This theorem relies on the
notion of almost sure convergence, which is introduced in Appendix B.
The three conditions in Theorem 6.1 are explained as follows.
In the rst condition, 0 <c1rwg(w) indicates that g(w) is a monotonically increas-
ing function. This condition ensures that the root of g(w) = 0 exists and is unique. If
g(w) is monotonically decreasing, we can simply treat  g(w) as a new function that
is monotonically increasing.
As an application, we can formulate an optimization problem in which the objective
function is J(w) as a root-nding problem: g(w):=rwJ(w) = 0. In this case, the
condition that g(w) is monotonically increasing indicates that J(w) isconvex , which
is a commonly adopted assumption in optimization problems.
The inequalityrwg(w)c2indicates that the gradient of g(w) is bounded from
above. For example, g(w) = tanh(w 1) satises this condition, but g(w) =w3 5
does not.
106

## 第120页

6.2. Robbins-Monro algorithm
The second condition about fakgis interesting. We often see conditions like this in
reinforcement learning algorithms. In particular, the conditionP1
k=1a2
k<1means
that lim n!1Pn
k=1a2
kis bounded from above. It requires that akconverges to zero
ask!1 . The conditionP1
k=1ak=1means that lim n!1Pn
k=1akis innitely
large. It requires that akshould not converge to zero too fast. These conditions have
interesting properties, which will be analyzed in detail shortly.
The third condition is mild. It does not require the observation error kto be Gaussian.
An important special case is that fkgis an i.i.d. stochastic sequence satisfying
E[k] = 0 and E[2
k]<1. In this case, the third condition is valid because kis
independent ofHkand hence we have E[kjHk] =E[k] = 0 and E[2
kjHk] =E[2
k].
We next examine the second condition about the coecients fakgmore closely.
Why is the second condition important for the convergence of the RM algorithm?
This question can naturally be answered when we present a rigorous proof of the above
theorem later. Here, we would like to provide some insightful intuition.
First,P1
k=1a2
k<1indicates that ak!0 ask!1 . Why is this condition impor-
tant? Suppose that the observation ~ g(wk;k) is always bounded. Since
wk+1 wk= ak~g(wk;k);
ifak!0, thenak~g(wk;k)!0 and hence wk+1 wk!0, indicating that wk+1and
wkapproach each other when k!1 . Otherwise, if akdoes not converge, then wk
may still 
uctuate when k!1 .
Second,P1
k=1ak=1indicates that akshould not converge to zero too fast. Why
is this condition important? Summarizing both sides of the equations of w2 w1=
 a1~g(w1;1),w3 w2= a2~g(w2;2),w4 w3= a3~g(w3;3),:::gives
w1 w1=1X
k=1ak~g(wk;k):
IfP1
k=1ak<1, thenjP1
k=1ak~g(wk;k)jis also bounded. Let bdenote the nite
upper bound such that
jw1 w1j=1X
k=1ak~g(wk;k)b: (6.6)
If the initial guess w1is selected far away from wso thatjw1 wj> b, then it is
impossible to have w1=waccording to (6.6). This suggests that the RM algorithm
cannot nd the true solution win this case. Therefore, the conditionP1
k=1ak=1
is necessary to ensure convergency given an arbitrary initial guess.
107

## 第121页

6.2. Robbins-Monro algorithm
What kinds of sequences satisfyP1
k=1ak=1andP1
k=1a2
k<1?
One typical sequence is
ak=1
k:
On the one hand, it holds that
lim
n!1 nX
k=11
k lnn!
=;
where0:577 is called the Euler-Mascheroni constant (or Euler's constant) [28].
Since lnn!1 asn!1 , we have
1X
k=11
k=1:
In fact,Hn=Pn
k=11
kis called the harmonic number in number theory [29]. On the
other hand, it holds that
1X
k=11
k2=2
6<1:
Finding the value ofP1
k=11
k2is known as the Basel problem [30].
In summary, the sequence fak= 1=kgsatises the second condition in Theorem 6.1.
Notably, a slight modication, such as ak= 1=(k+ 1) orak=ck=kwhereckis
bounded, also preserves this condition.
In the RM algorithm, akis often selected as a suciently small constant in many
applications. Although the second condition is not satised anymore in this case becauseP1
k=1a2
k=1rather thanP1
k=1a2
k<1, the algorithm can still converge in a certain
sense [24, Section 1.5]. In addition, g(x) =x3 5 in the example shown in Figure 6.3
does not satisfy the rst condition, but the RM algorithm can still nd the root if the
initial guess is adequately (not arbitrarily) selected.
6.2.2 Application to mean estimation
We next apply the Robbins-Monro theorem to analyze the mean estimation problem,
which has been discussed in Section 6.1. Recall that
wk+1=wk+k(xk wk)
is the mean estimation algorithm in (6.4). When k= 1=k, we can obtain the analytical
expression of wk+1aswk+1= 1=kPk
i=1xi. However, we would not be able to obtain
an analytical expression when given general values of k. In this case, the convergence
analysis is nontrivial. We can show that the algorithm in this case is a special RM
108

## 第122页

6.2. Robbins-Monro algorithm
algorithm and hence its convergence naturally follows.
In particular, dene a function as
g(w):=w E[X]:
The original problem is to obtain the value of E[X]. This problem is formulated as a
root-nding problem to solve g(w) = 0. Given a value of w, the noisy observation that
we can obtain is ~ g:=w x, wherexis a sample of X. Note that ~ gcan be written as
~g(w;) =w x
=w x+E[X] E[X]
= (w E[X]) + (E[X] x):=g(w) +;
where:=E[X] x.
The RM algorithm for solving this problem is
wk+1=wk k~g(wk;k) =wk k(wk xk);
which is exactly the algorithm in (6.4). As a result, it is guaranteed by Theorem 6.1 that
wkconverges to E[X] almost surely ifP1
k=1k=1,P1
k=12
k<1, andfxkgis i.i.d.
It is worth mentioning that the convergence property does not rely on any assumption
regarding the distribution of X.
6.3 Dvoretzky's convergence theorem
Until now, the convergence of the RM algorithm has not yet been proven. To do that,
we next introduce Dvoretzky's theorem [31, 32], which is a classic result in the eld
of stochastic approximation. This theorem can be used to analyze the convergence
of the RM algorithm and many reinforcement learning algorithms.
This section is slightly mathematically intensive. Readers who are interested in
the convergence analyses of stochastic algorithms are recommended to study this
section. Otherwise, this section can be skipped.
Theorem 6.2 (Dvoretzky's theorem) .Consider a stochastic process
k+1= (1 k)k+kk;
wherefkg1
k=1;fkg1
k=1;fkg1
k=1are stochastic sequences. Here k0;k0for all
k. Then, kconverges to zero almost surely if the following conditions are satised:
109

## 第123页

6.2. Robbins-Monro algorithm
(a)P1
k=1k=1,P1
k=12
k<1, andP1
k=12
k<1uniformly almost surely;
(b)E[kjHk] = 0 andE[2
kjHk]Calmost surely;
whereHk=fk;k 1;:::;k 1;:::;k 1;:::;k 1;:::g.
Before presenting the proof of this theorem, we rst clarify some issues.
In the RM algorithm, the coecient sequence fkgis deterministic. However,
Dvoretzky's theorem allows fkg;fkgto be random variables that depend on
Hk. Thus, it is more useful in cases where korkis a function of  k.
In the rst condition, it is stated as \uniformly almost surely". This is because k
andkmay be random variables and hence the denition of their limits must be in
the stochastic sense. In the second condition, it is also stated as \almost surely".
This is becauseHkis a sequence of random variables rather than specic values.
As a result, E[kjHk] and E[2
kjHk] are random variables. The denition of the
conditional expectation in this case is in the \almost sure" sense (Appendix B).
The statement of Theorem 6.2 is slightly dierent from [32] in the sense that Theo-
rem 6.2 does not requireP1
k=1k=1in the rst condition. WhenP1
k=1k<1,
especially in the extreme case where k= 0 for all k, the sequence can still con-
verge.
6.3.1 Proof of Dvoretzky's theorem
The original proof of Dvoretzky's theorem was given in 1956 [31]. There are also other
proofs. We next present a proof based on quasimartingales. With the convergence
results of quasimartingales, the proof of Dvoretzky's theorem is straightforward. More
information about quasimartingales can be found in Appendix C.
Proof of Dvoretzky's theorem. Lethk:= 2
k. Then,
hk+1 hk= 2
k+1 2
k
= (k+1 k)(k+1+ k)
= ( kk+kk)[(2 k)k+kk]
= k(2 k)2
k+2
k2
k+ 2(1 k)kkk:
Taking expectations on both sides of the above equation yields
E[hk+1 hkjHk] =E[ k(2 k)2
kjHk] +E[2
k2
kjHk] +E[2(1 k)kkkjHk]:
(6.7)
First, since  kis included and hence determined by Hk, it can be taken out from
the expectation (see property (e) in Lemma B.1). Second, consider the simple case
110

## 第124页

6.2. Robbins-Monro algorithm
wherek;kis determined by Hk. This case is valid when, for example, fkgand
fkgare functions of  kor deterministic sequences. Then, they can also be taken
out of the expectation. Therefore, (6.7) becomes
E[hk+1 hkjHk] = k(2 k)2
k+2
kE[2
kjHk] + 2(1 k)kkE[kjHk]:(6.8)
For the rst term, sinceP1
k=12
k<1impliesk!0 almost surely, there exists a
nitensuch thatk1 almost surely for all kn. Without loss of generality, we
next merely consider the case of k1. Then, k(2 k)2
k0. For the second
term, we have 2
kE[2
kjHk]2
kCas assumed. The third term equals zero because
E[kjHk] = 0 as assumed. Therefore, (6.8) becomes
E[hk+1 hkjHk] = k(2 k)2
k+2
kE[2
kjHk]2
kC; (6.9)
and hence
1X
k=1E[hk+1 hkjHk]1X
k=12
kC <1:
The last inequality is due to the conditionP1
k=12
k<1. Then, based on the
quasimartingale convergence theorem in Appendix C, we conclude that hkconverges
almost surely.
We next determine what value  kconverges to. It follows from (6.9) that
1X
k=1k(2 k)2
k=1X
k=12
kE[2
kjHk] 1X
k=1E[hk+1 hkjHk]:
The rst term on the right-hand side is bounded as assumed. The second term
is also bounded because hkconverges and hence hk+1 hkis summable. Thus,P1
k=1k(2 k)2
kon the left-hand side is also bounded. Since we consider the case
ofk1, we have
1>1X
k=1k(2 k)2
k1X
k=1k2
k0:
Therefore,P1
k=1k2
kis bounded. SinceP1
k=1k=1, we must have  k!0
almost surely.
111

## 第125页

6.2. Robbins-Monro algorithm
6.3.2 Application to mean estimation
While the mean estimation algorithm, wk+1=wk+k(xk wk), has been analyzed
using the RM theorem, we next show that its convergence can also be directly proven
by Dvoretzky's theorem.
Proof. Letw=E[X]. The mean estimation algorithm wk+1=wk+k(xk wk) can
be rewritten as
wk+1 w=wk w+k(xk w+w wk):
Let :=w w. Then, we have
k+1= k+k(xk w k)
= (1 k)k+k(xk w)|{z}
k:
Sincefxkgis i.i.d., we have E[xkjHk] =E[xk] =w. As a result, E[kjHk] =E[xk 
wjHk] = 0 and E[2
kjHk] =E[x2
kjHk] (w)2=E[x2
k] (w)2are bounded if the
variance ofxkis nite. Following Dvoretzky's theorem, we conclude that  kconverges
to zero and hence wkconverges to w=E[X] almost surely.
6.3.3 Application to the Robbins-Monro theorem
We are now ready to prove the Robbins-Monro theorem using Dvoretzky's theorem.
Proof of the Robbins-Monro theorem. The RM algorithm aims to nd the root of
g(w) = 0. Suppose that the root is wsuch thatg(w) = 0. The RM algorithm is
wk+1=wk ak~g(wk;k)
=wk ak[g(wk) +k]:
Then, we have
wk+1 w=wk w ak[g(wk) g(w) +k]:
Due to the mean value theorem [7, 8], we have g(wk) g(w) =rwg(w0
k)(wk w),
112

## 第126页

6.2. Robbins-Monro algorithm
wherew0
k2[wk;w]. Let  k:=wk w. The above equation becomes
k+1= k ak[rwg(w0
k)(wk w) +k]
= k akrwg(w0
k)k+ak( k)
= [1 akrwg(w0
k)|{z}
k]k+ak( k):
Note thatrwg(w) is bounded as 0 <c1rwg(w)c2as assumed. SinceP1
k=1ak=
1andP1
k=1a2
k<1as assumed, we knowP1
k=1k=1andP1
k=12
k<1. Thus,
all the conditions in Dvoretzky's theorem are satised and hence  kconverges to
zero almost surely.
The proof of the RM theorem demonstrates the power of Dvoretzky's theorem.
In particular, kin the proof is a stochastic sequence depending on wkrather than a
deterministic sequence. In this case, Dvoretzky's theorem is still applicable.
6.3.4 An extension of Dvoretzky's theorem
We next extend Dvoretzky's theorem to a more general theorem that can handle
multiple variables. This general theorem, proposed by [32], can be used to analyze
the convergence of stochastic iterative algorithms such as Q-learning.
Theorem 6.3. Consider a nite set Sof real numbers. For the stochastic process
k+1(s) = (1 k(s))k(s) +k(s)k(s);
it holds that k(s)converges to zero almost surely for every s2S if the following
conditions are satised for s2S:
(a)P
kk(s) =1,P
k2
k(s)<1,P
k2
k(s)<1, and E[k(s)jHk]
E[k(s)jHk]uniformly almost surely;
(b)kE[k(s)jHk]k1
kkk1, where
2(0;1);
(c) var[k(s)jHk]C(1 +kk(s)k1)2, whereCis a constant.
Here,Hk=fk;k 1;:::;k 1;:::;k 1;:::;k 1;:::grepresents the historical in-
formation. The term kk1refers to the maximum norm.
Proof. As an extension, this theorem can be proven based on Dvoretzky's theorem.
Details can be found in [32] and are omitted here.
Some remarks about this theorem are given below.
113

## 第127页

6.4. Stochastic gradient descent
We rst clarify some notations in the theorem. The variable scan be viewed
as an index. In the context of reinforcement learning, it indicates a state or a
state-action pair. The maximum normkk1is dened over a set. It is similar
but dierent from the L1norm of vectors. In particular, kE[k(s)jHk]k1:=
maxs2SjE[k(s)jHk]jandkk(s)k1:= maxs2Sjk(s)j.
This theorem is more general than Dvoretzky's theorem. First, it can handle the
case of multiple variables due to the maximum norm operations. This is important
for a reinforcement learning problem where there are multiple states. Second,
while Dvoretzky's theorem requires E[k(s)jHk] = 0 and var[ k(s)jHk]C, this
theorem only requires that the expectation and variance are bounded by the error
k.
It should be noted that the convergence of ( s) for alls2S requires that the
conditions are valid for every s2S. Therefore, when applying this theorem to
prove the convergence of reinforcement learning algorithms, we need to show that
the conditions are valid for every state (or state-action pair).
6.4 Stochastic gradient descent
This section introduces stochastic gradient descent (SGD) algorithms, which are widely
used in the eld of machine learning. We will see that SGD is a special RM algorithm,
and the mean estimation algorithm is a special SGD algorithm.
Consider the following optimization problem:
min
wJ(w) =E[f(w;X )]; (6.10)
wherewis the parameter to be optimized, and Xis a random variable. The expectation
is calculated with respect to X. Here,wandXcan be either scalars or vectors. The
functionf() is a scalar.
A straightforward method for solving (6.10) is gradient descent . In particular, the
gradient of E[f(w;X )] isrwE[f(w;X )] =E[rwf(w;X )]. Then, the gradient descent
algorithm is
wk+1=wk krwJ(wk) =wk kE[rwf(wk;X)]: (6.11)
This gradient descent algorithm can nd the optimal solution wunder some mild con-
ditions such as the convexity of f. Preliminaries about gradient descent algorithms can
be found in Appendix D.
The gradient descent algorithm requires the expected value E[rwf(wk;X)]. One
way to obtain the expected value is based on the probability distribution of X. The
114

## 第128页

6.4. Stochastic gradient descent
distribution is, however, often unknown in practice. Another way is to collect a large
number of i.i.d. samples fxign
i=1ofXso that the expected value can be approximated as
E[rwf(wk;X)]1
nnX
i=1rwf(wk;xi):
Then, (6.11) becomes
wk+1=wk k
nnX
i=1rwf(wk;xi): (6.12)
One problem of the algorithm in (6.12) is that it requires all the samples in each iteration.
In practice, if the samples are collected one by one, then it is favorable to update wevery
time a sample is collected. To that end, we can use the following algorithm:
wk+1=wk krwf(wk;xk); (6.13)
wherexkis the sample collected at time step k. This is the well-known stochastic gradient
descent algorithm. This algorithm is called \stochastic" because it relies on stochastic
samplesfxkg.
Compared to the gradient descent algorithm in (6.11), SGD replaces the true gra-
dient E[rwf(w;X )] with the stochastic gradient rwf(wk;xk). Sincerwf(wk;xk)6=
E[rwf(w;X )], can such a replacement still ensure wk!wask!1 ? The answer
is yes. We next present an intuitive explanation and postpone the rigorous proof of the
convergence to Section 6.4.5.
In particular, since
rwf(wk;xk) =E[rwf(wk;X)] +
rwf(wk;xk) E[rwf(wk;X)]
:=E[rwf(wk;X)] +k;
the SGD algorithm in (6.13) can be rewritten as
wk+1=wk kE[rwf(wk;X)] kk:
Therefore, the SGD algorithm is the same as the regular gradient descent algorithm except
that it has a perturbation term kk. Sincefxkgis i.i.d., we have Exk[rwf(wk;xk)] =
EX[rwf(wk;X)]. As a result,
E[k] =Eh
rwf(wk;xk) E[rwf(wk;X)]i
=Exk[rwf(wk;xk)] EX[rwf(wk;X)] = 0:
Therefore, the perturbation term khas a zero mean, which intuitively suggests that it
may not jeopardize the convergence property. A rigorous proof of the convergence of
115

## 第129页

6.4. Stochastic gradient descent
SGD is given in Section 6.4.5.
6.4.1 Application to mean estimation
We next apply SGD to analyze the mean estimation problem and show that the mean
estimation algorithm in (6.4) is a special SGD algorithm. To that end, we formulate the
mean estimation problem as an optimization problem:
min
wJ(w) =E1
2kw Xk2
:=E[f(w;X )]; (6.14)
wheref(w;X ) =kw Xk2=2 and the gradient is rwf(w;X ) =w X. It can be
veried that the optimal solution is w=E[X] by solvingrwJ(w) = 0. Therefore, this
optimization problem is equivalent to the mean estimation problem.
The gradient descent algorithm for solving (6.14) is
wk+1=wk krwJ(wk)
=wk kE[rwf(wk;X)]
=wk kE[wk X]:
This gradient descent algorithm is not applicable since E[wk X] orE[X] on the
right-hand side is unknown (in fact, it is what we need to solve).
The SGD algorithm for solving (6.14) is
wk+1=wk krwf(wk;xk) =wk k(wk xk);
wherexkis a sample obtained at time step k. Notably, this SGD algorithm is the
same as the iterative mean estimation algorithm in (6.4). Therefore, (6.4) is an SGD
algorithm designed specically for solving the mean estimation problem.
6.4.2 Convergence pattern of SGD
The idea of the SGD algorithm is to replace the true gradient with a stochastic gradient.
However, since the stochastic gradient is random, one may ask whether the convergence
speed of SGD is slow or random. Fortunately, SGD can converge eciently in general.
An interesting convergence pattern is that it behaves similarly to the regular gradient
descent algorithm when the estimate wkis far from the optimal solution w. Only when
wkis close tow, does the convergence of SGD exhibit more randomness.
An analysis of this pattern and an illustrative example are given below.
116

## 第130页

6.4. Stochastic gradient descent
Analysis: The relative error between the stochastic and true gradients is
k:=jrwf(wk;xk) E[rwf(wk;X)]j
jE[rwf(wk;X)]j:
For the sake of simplicity, we consider the case where wandrwf(w;x) are both
scalars . Sincewis the optimal solution, it holds that E[rwf(w;X)] = 0. Then, the
relative error can be rewritten as
k=jrwf(wk;xk) E[rwf(wk;X)]j
jE[rwf(wk;X)] E[rwf(w;X)]j=jrwf(wk;xk) E[rwf(wk;X)]j
jE[r2
wf( ~wk;X)(wk w)]j;(6.15)
where the last equality is due to the mean value theorem [7, 8] and ~ wk2[wk;w].
Suppose that fis strictly convex such that r2
wfc >0 for allw;X . Then, the
denominator in (6.15) becomes
E[r2
wf( ~wk;X)(wk w)]=E[r2
wf( ~wk;X)](wk w)
cjwk wj:
Substituting the above inequality into (6.15) yields
kstochastic gradientz}|{
rwf(wk;xk) true gradientz}|{
E[rwf(wk;X)]
cjwk wj|{z}
distance to the optimal solution:
The above inequality suggests an interesting convergence pattern of SGD: the relative
errorkis inversely proportional to jwk wj. As a result, when jwk wjis large,k
is small. In this case, the SGD algorithm behaves like the gradient descent algorithm
and hencewkquickly converges to w. Whenwkis close tow, the relative error k
may be large, and the convergence exhibits more randomness.
Example: A good example for demonstrating the above analysis is the mean estima-
tion problem. Consider the mean estimation problem in (6.14). When wandXare
both scalar, we have f(w;X ) =jw Xj2=2 and hence
rwf(w;xk) =w xk;
E[rwf(w;xk)] =w E[X] =w w:
Thus, the relative error is
k=jrwf(wk;xk) E[rwf(wk;X)]j
jE[rwf(wk;X)]j=j(wk xk) (wk E[X])j
jwk wj=jE[X] xkj
jwk wj:
The expression of the relative error clearly shows that kisinversely proportional to
117

## 第131页

6.4. Stochastic gradient descent
-20 -15 -10 -5 0 5 10
x-505101520yMean
Samples
SGD (m=1)
MBGD (m=5)
MBGD (m=50)
0 5 10 15 20 25 30
Iteration step051015202530Distance to meanSGD (m=1) 
MBGD (m=5) 
MBGD (m=50)
Figure 6.5: An example for demonstrating stochastic and mini-batch gradient descent algorithms. The
distribution of X2R2is uniform in the square area centered at the origin with a side length as 20. The
mean is E[X] = 0. The mean estimation is based on 100 i.i.d. samples.
jwk wj. As a result, when wkis far from w, the relative error is small, and SGD
behaves like gradient descent. In addition, since kis proportional to jE[X] xkj, the
mean ofkis proportional to the variance of X.
The simulation results are shown in Figure 6.5. Here, X2R2represents a random
position in the plane. Its distribution is uniform in the square area centered at the
origin and E[X] = 0. The mean estimation is based on 100 i.i.d. samples. Although
the initial guess of the mean is far away from the true value, it can be seen that the
SGD estimate quickly approaches the neighborhood of the origin. When the estimate
is close to the origin, the convergence process exhibits certain randomness.
6.4.3 A deterministic formulation of SGD
The formulation of SGD in (6.13) involves random variables. One may often encounter
a deterministic formulation of SGD without involving any random variables.
In particular, consider a set of real numbers fxign
i=1, wherexidoes not have to be a
sample of any random variable. The optimization problem to be solved is to minimize
the average:
min
wJ(w) =1
nnX
i=1f(w;xi);
wheref(w;xi) is a parameterized function, and wis the parameter to be optimized. The
gradient descent algorithm for solving this problem is
wk+1=wk krwJ(wk) =wk k1
nnX
i=1rwf(wk;xi):
Suppose that the set fxign
i=1is large and we can only fetch a single number each time.
118

## 第132页

6.4. Stochastic gradient descent
In this case, it is favorable to update wkin an incremental manner:
wk+1=wk krwf(wk;xk): (6.16)
It must be noted that xkhere is the number fetched at time step kinstead of the kth
element in the set fxign
i=1.
The algorithm in (6.16) is very similar to SGD, but its problem formulation is subtly
dierent because it does not involve any random variables or expected values. Then,
many questions arise. For example, is this algorithm SGD? How should we use the nite
set of numbersfxign
i=1? Should we sort these numbers in a certain order and then use
them one by one, or should we randomly sample a number from the set?
A quick answer to the above questions is that, although no random variables are
involved in the above formulation, we can convert the deterministic formulation to the
stochastic formulation by introducing a random variable. In particular, let Xbe a random
variable dened on the set fxign
i=1. Suppose that its probability distribution is uniform
such thatp(X=xi) = 1=n. Then, the deterministic optimization problem becomes a
stochastic one:
min
wJ(w) =1
nnX
i=1f(w;xi) =E[f(w;X )]:
The last equality in the above equation is strict instead of approximate. Therefore, the
algorithm in (6.16) is SGD, and the estimate converges if xkisuniformly and indepen-
dently sampled from fxign
i=1. Note that xkmay repeatedly take the same number in
fxign
i=1since it is sampled randomly.
6.4.4 BGD, SGD, and mini-batch GD
While SGD uses a single sample in every iteration, we next introduce mini-batch gradient
descent (MBGD), which uses a few more samples in every iteration. When all samples
are used in every iteration, the algorithm is called batch gradient descent (BGD).
In particular, suppose that we would like to nd the optimal solution that can min-
imizeJ(w) =E[f(w;X )] given a set of random samples fxign
i=1ofX. The BGD, SGD,
and MBGD algorithms for solving this problem are, respectively,
wk+1=wk k1
nnX
i=1rwf(wk;xi); (BGD)
wk+1=wk k1
mX
j2Ikrwf(wk;xj); (MBGD)
wk+1=wk krwf(wk;xk): (SGD)
In the BGD algorithm, all the samples are used in every iteration. When nis large,
(1=n)Pn
i=1rwf(wk;xi) is close to the true gradient E[rwf(wk;X)]. In the MBGD al-
119

## 第133页

6.4. Stochastic gradient descent
gorithm,Ikis a subset off1;:::;ngobtained at time k. The size of the set is jIkj=m.
The samples inIkare also assumed to be i.i.d. In the SGD algorithm, xkis randomly
sampled fromfxign
i=1at timek.
MBGD can be viewed as an intermediate version between SGD and BGD. Compared
to SGD, MBGD has less randomness because it uses more samples instead of just one
as in SGD. Compared to BGD, MBGD does not require using all the samples in every
iteration, making it more 
exible. If m= 1, then MBGD becomes SGD. However, if
m=n, MBGD may notbecome BGD. This is because MBGD uses nrandomly fetched
samples, whereas BGD uses all nnumbers. These nrandomly fetched samples may
contain the same number multiple times and hence may not cover all nnumbers in
fxign
i=1.
The convergence speed of MBGD is faster than that of SGD in general. This is
because SGD uses rwf(wk;xk) to approximate the true gradient, whereas MBGD uses
(1=m)P
j2Ikrwf(wk;xj), which is closer to the true gradient because the randomness is
averaged out. The convergence of the MBGD algorithm can be proven similarly to the
SGD case.
A good example for demonstrating the above analysis is the mean estimation prob-
lem. In particular, given some numbers fxign
i=1, our goal is to calculate the mean
x=Pn
i=1xi=n. This problem can be equivalently stated as the following optimization
problem:
min
wJ(w) =1
2nnX
i=1kw xik2;
whose optimal solution is w= x. The three algorithms for solving this problem are,
respectively,
wk+1=wk k1
nnX
i=1(wk xi) =wk k(wk x); (BGD)
wk+1=wk k1
mX
j2Ik(wk xj) =wk k
wk x(m)
k
; (MBGD)
wk+1=wk k(wk xk); (SGD)
where x(m)
k=P
j2Ikxj=m. Furthermore, if k= 1=k, the above equations can be solved
120

## 第134页

6.4. Stochastic gradient descent
as follows:
wk+1=1
kkX
j=1x= x; (BGD)
wk+1=1
kkX
j=1x(m)
j; (MBGD)
wk+1=1
kkX
j=1xj: (SGD)
The derivation of the above equations is similar to that of (6.3) and is omitted here. It
can be seen that the estimate given by BGD at each step is exactly the optimal solution
w= x. MBGD converges to the mean faster than SGD because  x(m)
kis already an
average.
A simulation example is given in Figure 6.5 to demonstrate the convergence of MBGD.
Letk= 1=k. It is shown that all MBGD algorithms with dierent mini-batch sizes can
converge to the mean. The case with m= 50 converges the fastest, while SGD with m= 1
is the slowest. This is consistent with the above analysis. Nevertheless, the convergence
rate of SGD is still fast, especially when wkis far from w.
6.4.5 Convergence of SGD
The rigorous proof of the convergence of SGD is given as follows.
Theorem 6.4 (Convergence of SGD) .For the SGD algorithm in (6.13) , if the following
conditions are satised, then wkconverges to the root of rwE[f(w;X )] = 0 almost surely.
(a) 0<c1r2
wf(w;X )c2;
(b)P1
k=1ak=1andP1
k=1a2
k<1;
(c)fxkg1
k=1are i.i.d.
The three conditions in Theorem 6.4 are discussed below.
Condition (a) is about the convexity of f. It requires the curvature of fto be bounded
from above and below. Here, wis a scalar, and so is r2
wf(w;X ). This condition can
be generalized to the vector case. When wis a vector,r2
wf(w;X ) is the well-known
Hessian matrix.
Condition (b) is similar to that of the RM algorithm. In fact, the SGD algorithm is
a special RM algorithm (as shown in the proof in Box 6.1). In practice, akis often
selected as a suciently small constant . Although condition (b) is not satised in this
case, the algorithm can still converge in a certain sense [24, Section 1.5].
Condition (c) is a common requirement.
121

## 第135页

6.4. Stochastic gradient descent
Box 6.1: Proof of Theorem 6.4
We next show that the SGD algorithm is a special RM algorithm. Then, the conver-
gence of SGD naturally follows from the RM theorem.
The problem to be solved by SGD is to minimize J(w) =E[f(w;X )]. This
problem can be converted to a root-nding problem. That is, nding the root of
rwJ(w) =E[rwf(w;X )] = 0. Let
g(w) =rwJ(w) =E[rwf(w;X )]:
Then, SGD aims to nd the root of g(w) = 0. This is exactly the problem solved by
the RM algorithm. The quantity that we can measure is ~ g=rwf(w;x), wherexis
a sample of X. Note that ~ gcan be rewritten as
~g(w;) =rwf(w;x)
=E[rwf(w;X )] +rwf(w;x) E[rwf(w;X )]|{z}
:
Then, the RM algorithm for solving g(w) = 0 is
wk+1=wk ak~g(wk;k) =wk akrwf(wk;xk);
which is the same as the SGD algorithm in (6.13). As a result, the SGD algorithm
is a special RM algorithm. We next show that the three conditions in Theorem 6.1
are satised. Then, the convergence of SGD naturally follows from Theorem 6.1.
Sincerwg(w) =rwE[rwf(w;X )] = E[r2
wf(w;X )], it follows from c1
r2
wf(w;X )c2thatc1rwg(w)c2. Thus, the rst condition in Theo-
rem 6.1 is satised.
The second condition in Theorem 6.1 is the same as the second condition in this
theorem.
The third condition in Theorem 6.1 requires E[kjHk] = 0 and E[2
kjHk]<1.
Sincefxkgis i.i.d., we have Exk[rwf(w;xk)] =E[rwf(w;X )] for allk. Therefore,
E[kjHk] =E[rwf(wk;xk) E[rwf(wk;X)]jHk]:
SinceHk=fwk;wk 1;:::gandxkis independent of Hk, the rst term on the
right-hand side becomes E[rwf(wk;xk)jHk] =Exk[rwf(wk;xk)]. The second
term becomes E[E[rwf(wk;X)]jHk] =E[rwf(wk;X)] because E[rwf(wk;X)] is
122

## 第136页

6.5. Summary
a function of wk. Therefore,
E[kjHk] =Exk[rwf(wk;xk)] E[rwf(wk;X)] = 0:
Similarly, it can be proven that E[2
kjHk]<1ifjrwf(w;x)j<1for allwgiven
anyx.
Since the three conditions in Theorem 6.1 are satised, the convergence of the
SGD algorithm follows.
6.5 Summary
Instead of introducing new reinforcement learning algorithms, this chapter introduced the
preliminaries of stochastic approximation such as the RM and SGD algorithms. Com-
pared to many other root-nding algorithms, the RM algorithm does not require the
expression of the objective function or its derivative. It has been shown that the SGD al-
gorithm is a special RM algorithm. Moreover, an important problem frequently discussed
throughout this chapter is mean estimation. The mean estimation algorithm (6.4) is the
rst stochastic iterative algorithm we have ever introduced in this book. We showed that
it is a special SGD algorithm. We will see in Chapter 7 that temporal-dierence learn-
ing algorithms have similar expressions. Finally, the name \stochastic approximation"
was rst used by Robbins and Monro in 1951 [25]. More information about stochastic
approximation can be found in [24].
6.6 Q&A
Q: What is stochastic approximation?
A: Stochastic approximation refers to a broad class of stochastic iterative algorithms
for solving root-nding or optimization problems.
Q: Why do we need to study stochastic approximation?
A: This is because the temporal-dierence reinforcement learning algorithms that will
be introduced in Chapter 7 can be viewed as stochastic approximation algorithms.
With the knowledge introduced in this chapter, we can be better prepared, and it will
not be abrupt for us to see these algorithms for the rst time.
Q: Why do we frequently discuss the mean estimation problem in this chapter?
A: This is because the state and action values are dened as the means of random
variables. The temporal-dierence learning algorithms introduced in Chapter 7 are
similar to stochastic approximation algorithms for mean estimation.
123

## 第137页

6.6. Q&A
Q: What is the advantage of the RM algorithm over other root-nding algorithms?
A: Compared to many other root-nding algorithms, the RM algorithm is powerful
in the sense that it does not require the expression of the objective function or its
derivative. As a result, it is a black-box technique that only requires the input and
output of the objective function. The famous SGD algorithm is a special form of the
RM algorithm.
Q: What is the basic idea of SGD?
A: SGD aims to solve optimization problems involving random variables. When the
probability distributions of the given random variables are not known, SGD can solve
the optimization problems merely by using samples. Mathematically, the SGD algo-
rithm can be obtained by replacing the true gradient expressed as an expectation in
the gradient descent algorithm with a stochastic gradient.
Q: Can SGD converge quickly?
A: SGD has an interesting convergence pattern. That is, if the estimate is far from
the optimal solution, then the convergence process is fast. When the estimate is close
to the solution, the randomness of the stochastic gradient becomes in
uential, and
the convergence rate decreases.
Q: What is MBGD? What are its advantages over SGD and BGD?
A: MBGD can be viewed as an intermediate version between SGD and BGD. Com-
pared to SGD, it has less randomness because it uses more samples instead of just one
as in SGD. Compared to BGD, it does not require the use of all the samples, making
it more 
exible.
124

## 第138页

Chapter 7
Temporal-Dierence Methods
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
Figure 7.1: Where we are in this book.
This chapter introduces temporal-dierence (TD) methods for reinforcement learning.
Similar to Monte Carlo (MC) learning, TD learning is also model-free, but it has some
advantages due to its incremental form. With the preparation in Chapter 6, readers will
not feel alarmed when seeing TD learning algorithms. In fact, TD learning algorithms can
be viewed as special stochastic algorithms for solving the Bellman or Bellman optimality
equations.
Since this chapter introduces quite a few TD algorithms, we rst overview these
algorithms and clarify the relationships between them.
Section 7.1 introduces the most basic TD algorithm, which can estimate the state
125

## 第139页

7.1. TD learning of state values
values of a given policy. It is important to understand this basic algorithm rst
before studying the other TD algorithms.
Section 7.2 introduces the Sarsa algorithm, which can estimate the action values of a
given policy. This algorithm can be combined with a policy improvement step to nd
optimal policies. The Sarsa algorithm can be easily obtained from the TD algorithm
in Section 7.1 by replacing state value estimation with action value estimation.
Section 7.3 introduces the n-step Sarsa algorithm, which is a generalization of the
Sarsa algorithm. It will be shown that Sarsa and MC learning are two special cases
ofn-step Sarsa.
Section 7.4 introduces the Q-learning algorithm, which is one of the most classic
reinforcement learning algorithms. While the other TD algorithms aim to solve the
Bellman equation of a given policy, Q-learning aims to directly solve the Bellman
optimality equation to obtain optimal policies.
Section 7.5 compares the TD algorithms introduced in this chapter and provides a
unied point of view.
7.1 TD learning of state values
TD learning often refers to a broad class of reinforcement learning algorithms. For ex-
ample, all the algorithms introduced in this chapter fall into the scope of TD learning.
However, TD learning in this section specically refers to a classic algorithm for estimat-
ing state values.
7.1.1 Algorithm description
Given a policy , our goal is to estimate v(s) for alls2S. Suppose that we have
some experience samples ( s0;r1;s1;:::;st;rt+1;st+1;:::) generated following . Here,t
denotes the time step. The following TD algorithm can estimate the state values using
these samples:
vt+1(st) =vt(st) t(st)h
vt(st)  
rt+1+
vt(st+1)i
; (7.1)
vt+1(s) =vt(s);for alls6=st; (7.2)
wheret= 0;1;2;:::. Here,vt(st) is the estimate of v(st) at timet;t(st) is the learning
rate forstat timet.
It should be noted that, at time t, only the value of the visited state stis updated. The
values of the unvisited states s6=stremain unchanged as shown in (7.2). Equation (7.2)
is often omitted for simplicity, but it should be kept in mind because the algorithm would
be mathematically incomplete without this equation.
126

## 第140页

7.1. TD learning of state values
Readers who see the TD learning algorithm for the rst time may wonder why it
is designed like this. In fact, it can be viewed as a special stochastic approximation
algorithm for solving the Bellman equation. To see that, rst recall that the denition of
the state value is
v(s) =E
Rt+1+
Gt+1jSt=s
; s2S: (7.3)
We can rewrite (7.3) as
v(s) =E
Rt+1+
v(St+1)jSt=s
; s2S: (7.4)
That is because E[Gt+1jSt=s] =P
a(ajs)P
s0p(s0js;a)v(s0) =E[v(St+1)jSt=s].
Equation (7.4) is another expression of the Bellman equation. It is sometimes called the
Bellman expectation equation .
The TD algorithm can be derived by applying the Robbins-Monro algorithm (Chap-
ter 6) to solve the Bellman equation in (7.4). Interested readers can check the details in
Box 7.1.
Box 7.1: Derivation of the TD algorithm
We next show that the TD algorithm in (7.1) can be obtained by applying the
Robbins-Monro algorithm to solve (7.4).
For statest, we dene a function as
g(v(st)):=v(st) E
Rt+1+
v(St+1)jSt=st
:
Then, (7.4) is equivalent to
g(v(st)) = 0:
Our goal is to solve the above equation to obtain v(st) using the Robbins-Monro
algorithm. Since we can obtain rt+1andst+1, which are the samples of Rt+1and
St+1, the noisy observation of g(v(st)) that we can obtain is
~g(v(st)) =v(st) 
rt+1+
v(st+1)
=
v(st) E
Rt+1+
v(St+1)jSt=st
| {z }
g(v(st))
+
E
Rt+1+
v(St+1)jSt=st
 
rt+1+
v(st+1)
| {z }
:
127

## 第141页

7.1. TD learning of state values
Therefore, the Robbins-Monro algorithm (Section 6.2) for solving g(v(st)) = 0 is
vt+1(st) =vt(st) t(st)~g(vt(st))
=vt(st) t(st)
vt(st) 
rt+1+
v(st+1)
; (7.5)
wherevt(st) is the estimate of v(st) at timet, andt(st) is the learning rate.
The algorithm in (7.5) has a similar expression to that of the TD algorithm in
(7.1). The only dierence is that the right-hand side of (7.5) contains v(st+1),
whereas (7.1) contains vt(st+1). That is because (7.5) is designed to merely estimate
the state value of stby assuming that the state values of the other states are already
known. If we would like to estimate the state values of all the states, then v(st+1) on
the right-hand side should be replaced with vt(st+1). Then, (7.5) is exactly the same
as (7.1). However, can such a replacement still ensure convergence? The answer is
yes, and it will be proven later in Theorem 7.1.
7.1.2 Property analysis
Some important properties of the TD algorithm are discussed as follows.
First, we examine the expression of the TD algorithm more closely. In particular,
(7.1) can be described as
vt+1(st)|{z}
new estimate=vt(st)|{z}
current estimate t(st)TD errortz}|{
vt(st)  
rt+1+
vt(st+1)|{z}
TD target vt
; (7.6)
where
vt:=rt+1+
vt(st+1)
is called the TD target and
t:=v(st) vt=vt(st) (rt+1+
vt(st+1))
is called the TD error . It can be seen that the new estimate vt+1(st) is a combination of
the current estimate vt(st) and the TD error t.
Why is vtcalled the TD target?
This is because  vtis the target value that the algorithm attempts to drive v(st) to.
To see that, subtracting  vtfrom both sides of (7.6) gives
vt+1(st) vt=
vt(st) vt
 t(st)
vt(st) vt
= [1 t(st)]
vt(st) vt
:
128

## 第142页

7.1. TD learning of state values
Taking the absolute values of both sides of the above equation gives
jvt+1(st) vtj=j1 t(st)jjvt(st) vtj:
Sincet(st) is a small positive number, we have 0 <1 t(st)<1. It then follows
that
jvt+1(st) vtj<jvt(st) vtj:
The above inequality is important because it indicates that the new value vt+1(st) is
closer to vtthan the old value vt(st). Therefore, this algorithm mathematically drives
vt(st) toward vt. This is why  vtis called the TD target.
What is the interpretation of the TD error?
First, this error is called temporal-dierence becauset=vt(st) (rt+1+
vt(st+1))
re
ects the discrepancy between two time steps tandt+ 1. Second, the TD error is
zero in the expectation sense when the state value estimate is accurate. To see that,
whenvt=v, the expected value of the TD error is
E[tjSt=st] =E
v(St) (Rt+1+
v(St+1))jSt=st
=v(st) E
Rt+1+
v(St+1)jSt=st
= 0: (due to (7.3))
Therefore, the TD error re
ects not only the discrepancy between two time steps but
also, more importantly, the discrepancy between the estimate vtand the true state
valuev.
On a more abstract level, the TD error can be interpreted as the innovation , which
indicates new information obtained from the experience sample ( st;rt+1;st+1). The
fundamental idea of TD learning is to correct our current estimate of the state val-
ue based on the newly obtained information. Innovation is fundamental in many
estimation problems such as Kalman ltering [33,34].
Second, the TD algorithm in (7.1) can only estimate the state values of a given policy.
To nd optimal policies, we still need to further calculate the action values and then
conduct policy improvement. This will be introduced in Section 7.2. Nevertheless, the
TD algorithm introduced in this section is very basic and important for understanding
the other algorithms in this chapter.
Third, while both TD learning and MC learning are model-free, what are their ad-
vantages and disadvantages? The answers are summarized in Table 7.1.
129

## 第143页

7.1. TD learning of state values
TD learning MC learning
Incremental: TD learning is incremen-
tal. It can update the state/action values
immediately after receiving an experience
sample.Non-incremental: MC learning is non-
incremental. It must wait until an episode
has been completely collected. That is be-
cause it must calculate the discounted re-
turn of the episode.
Continuing tasks: Since TD learning is in-
cremental, it can handle both episodic and
continuing tasks. Continuing tasks may
not have terminal states.Episodic tasks: Since MC learning is non-
incremental, it can only handle episodic
tasks where the episodes terminate after a
nite number of steps.
Bootstrapping: TD learning bootstraps
because the update of a state/action val-
ue relies on the previous estimate of this
value. As a result, TD learning requires
an initial guess of the values.Non-bootstrapping: MC is not bootstrap-
ping because it can directly estimate s-
tate/action values without initial guesses.
Low estimation variance: The estimation
variance of TD is lower than that of M-
C because it involves fewer random vari-
ables. For instance, to estimate an ac-
tion valueq(st;at), Sarsa merely requires
the samples of three random variables:
Rt+1;St+1;At+1.High estimation variance: The estimation
variance of MC is higher since many ran-
dom variables are involved. For example,
to estimate q(st;at), we need samples of
Rt+1+
Rt+2+
2Rt+3+:::. Suppose that
the length of each episode is L. Assume
that each state has the same number of
actions asjAj. Then, there are jAjLpos-
sible episodes following a soft policy. If we
merely use a few episodes to estimate, it
is not surprising that the estimation vari-
ance is high.
Table 7.1: A comparison between TD learning and MC learning.
7.1.3 Convergence analysis
The convergence analysis of the TD algorithm in (7.1) is given below.
Theorem 7.1 (Convergence of TD learning) .Given a policy , by the TD algorithm in
(7.1) ,vt(s)converges almost surely to v(s)ast!1 for alls2S ifP
tt(s) =1andP
t2
t(s)<1for alls2S.
Some remarks about tare given below. First, the condition ofP
tt(s) =1andP
t2
t(s)<1must be valid for all s2S. Note that, at time t,t(s)>0 ifsis being
visited and t(s) = 0 otherwise. The conditionP
tt(s) =1requires the state sto
be visited an innite (or suciently many) number of times. This requires either the
condition of exploring starts or an exploratory policy so that every state-action pair can
possibly be visited many times. Second, the learning rate tis often selected as a small
130

## 第144页

7.1. TD learning of state values
positive constant in practice. In this case, the condition thatP
t2
t(s)<1is no longer
valid. When is constant, it can still be shown that the algorithm converges in the sense
of expectation [24, Section 1.5].
Box 7.2: Proof of Theorem 7.1
We prove the convergence based on Theorem 6.3 in Chapter 6. To do that, we need
rst to construct a stochastic process as that in Theorem 6.3. Consider an arbitrary
states2S. At timet, it follows from the TD algorithm in (7.1) that
vt+1(s) =vt(s) t(s)
vt(s) (rt+1+
vt(st+1))
;ifs=st, (7.7)
or
vt+1(s) =vt(s);ifs6=st. (7.8)
The estimation error is dened as
t(s):=vt(s) v(s);
wherev(s) is the state value of sunder policy . Deducting v(s) from both sides
of (7.7) gives
t+1(s) = (1 t(s))t(s) +t(s)(rt+1+
vt(st+1) v(s)|{z}
t(s))
= (1 t(s))t(s) +t(s)t(s); s =st: (7.9)
Deductingv(s) from both sides of (7.8) gives
t+1(s) = t(s) = (1 t(s))t(s) +t(s)t(s); s6=st;
whose expression is the same as that of (7.9) except that t(s) = 0 andt(s) = 0.
Therefore, regardless of whether s=st, we obtain the following unied expression:
t+1(s) = (1 t(s))t(s) +t(s)t(s):
This is the process in Theorem 6.3. Our goal is to show that the three conditions in
Theorem 6.3 are satised and hence the process converges.
The rst condition is valid as assumed in Theorem 7.1. We next show that the
second condition is valid. That is, kE[t(s)jHt]k1
kt(s)k1for alls2S. Here,
Htrepresents the historical information (see the denition in Theorem 6.3). Due to
the Markovian property, t(s) =rt+1+
vt(st+1) v(s) ort(s) = 0 does not depend
131

## 第145页

7.1. TD learning of state values
on the historical information once sis given. As a result, we have E[t(s)jHt] =
E[t(s)]. Fors6=st, we havet(s) = 0. Then, it is trivial to see that
jE[t(s)]j= 0
kt(s)k1: (7.10)
Fors=st, we have
E[t(s)] =E[t(st)]
=E[rt+1+
vt(st+1) v(st)jst]
=E[rt+1+
vt(st+1)jst] v(st):
Sincev(st) =E[rt+1+
v(st+1)jst], the above equation implies that
E[t(s)] =
E[vt(st+1) v(st+1)jst]
=
X
s02Sp(s0jst)[vt(s0) v(s0)]:
It follows that
jE[t(s)]j=
X
s02Sp(s0jst)[vt(s0) v(s0)]

X
s02Sp(s0jst) max
s02Sjvt(s0) v(s0)j
=
max
s02Sjvt(s0) v(s0)j
=
kvt(s0) v(s0)k1
=
kt(s)k1: (7.11)
Therefore, at time t, we know from (7.10) and (7.11) that jE[t(s)]j
kt(s)k1for
alls2Sregardless of whether s=st. Thus,
kE[t(s)]k1
kt(s)k1;
which is the second condition in Theorem 6.3. Finally, regarding the third condition,
we have var[ t(s)jHt] = var[rt+1+
vt(st+1) v(st)jst] = var[rt+1+
vt(st+1)jst] for
s=stand var[t(s)jHt] = 0 fors6=st. Sincert+1is bounded, the third condition
can be proven without diculty.
The above proof is inspired by [32].
132

## 第146页

7.2. TD learning of action values: Sarsa
7.2 TD learning of action values: Sarsa
The TD algorithm introduced in Section 7.1 can only estimate state values . This section
introduces another TD algorithm called Sarsa that can directly estimate action values .
Estimating action values is important because it can be combined with a policy improve-
ment step to learn optimal policies.
7.2.1 Algorithm description
Given a policy , our goal is to estimate the action values. Suppose that we have some
experience samples generated following : (s0;a0;r1;s1;a1;:::;st;at;rt+1;st+1;at+1;:::).
We can use the following Sarsa algorithm to estimate the action values:
qt+1(st;at) =qt(st;at) t(st;at)h
qt(st;at) (rt+1+
qt(st+1;at+1))i
; (7.12)
qt+1(s;a) =qt(s;a);for all (s;a)6= (st;at);
wheret= 0;1;2;::: andt(st;at) is the learning rate. Here, qt(st;at) is the estimate of
q(st;at). At time t, only the q-value of ( st;at) is updated, whereas the q-values of the
others remain the same.
Some important properties of the Sarsa algorithm are discussed as follows.
Why is this algorithm called \Sarsa"? That is because each iteration of the algorithm
requires (st;at;rt+1;st+1;at+1). Sarsa is an abbreviation for state-action-reward-state-
action. The Sarsa algorithm was rst proposed in [35] and its name was coined by
[3].
Why is Sarsa designed in this way? One may have noticed that Sarsa is similar to the
TD algorithm in (7.1). In fact, Sarsa can be easily obtained from the TD algorithm
by replacing state value estimation with action value estimation.
What does Sarsa do mathematically? Similar to the TD algorithm in (7.1), Sarsa
is a stochastic approximation algorithm for solving the Bellman equation of a given
policy:
q(s;a) =E[R+
q(S0;A0)js;a];for all (s;a): (7.13)
Equation (7.13) is the Bellman equation expressed in terms of action values. A proof
is given in Box 7.3.
133

## 第147页

7.2. TD learning of action values: Sarsa
Box 7.3: Showing that (7.13) is the Bellman equation
As introduced in Section 2.8.2, the Bellman equation expressed in terms of action
values is
q(s;a) =X
rrp(rjs;a) +
X
s0X
a0q(s0;a0)p(s0js;a)(a0js0)
=X
rrp(rjs;a) +
X
s0p(s0js;a)X
a0q(s0;a0)(a0js0): (7.14)
This equation establishes the relationships among the action values. Since
p(s0;a0js;a) =p(s0js;a)p(a0js0;s;a)
=p(s0js;a)p(a0js0) (due to conditional independence)
:=p(s0js;a)(a0js0);
(7.14) can be rewritten as
q(s;a) =X
rrp(rjs;a) +
X
s0X
a0q(s0;a0)p(s0;a0js;a):
By the denition of the expected value, the above equation is equivalent to (7.13).
Hence, (7.13) is the Bellman equation.
Is Sarsa convergent? Since Sarsa is the action-value version of the TD algorithm in
(7.1), the convergence result is similar to Theorem 7.1 and given below.
Theorem 7.2 (Convergence of Sarsa) .Given a policy , by the Sarsa algorithm in
(7.12) ,qt(s;a)converges almost surely to the action value q(s;a)ast!1 for all
(s;a)ifP
tt(s;a) =1andP
t2
t(s;a)<1for all (s;a).
The proof is similar to that of Theorem 7.1 and is omitted here. The condition ofP
tt(s;a) =1andP
t2
t(s;a)<1should be valid for all ( s;a). In particular,P
tt(s;a) =1requires that every state-action pair must be visited an innite (or
suciently many) number of times. At time t, if (s;a) = (st;at), thent(s;a)>0;
otherwise,t(s;a) = 0.
7.2.2 Optimal policy learning via Sarsa
The Sarsa algorithm in (7.12) can only estimate the action values of a given policy. To
nd optimal policies, we can combine it with a policy improvement step. The combination
is also often called Sarsa, and its implementation procedure is given in Algorithm 7.1.
134

## 第148页

7.2. TD learning of action values: Sarsa
Algorithm 7.1: Optimal policy learning by Sarsa
Initialization: t(s;a) =>0for all (s;a)and allt.2(0;1). Initialq0(s;a)for all
(s;a). Initial-greedy policy 0derived from q0.
Goal: Learn an optimal policy that can lead the agent to the target state from an initial
states0.
For each episode, do
Generatea0ats0following0(s0)
Ifst(t= 0;1;2;::: ) is not the target state, do
Collect an experience sample (rt+1;st+1;at+1)given (st;at): generatert+1;st+1
by interacting with the environment; generate at+1followingt(st+1).
Update q-value for (st;at):
qt+1(st;at) =qt(st;at) t(st;at)h
qt(st;at) (rt+1+
qt(st+1;at+1))i
Update policy for st:
t+1(ajst) = 1 
jA(st)j(jA(st)j 1)ifa= arg max aqt+1(st;a)
t+1(ajst) =
jA(st)jotherwise
st st+1,at at+1
As shown in Algorithm 7.1, each iteration has two steps. The rst step is to update
the q-value of the visited state-action pair. The second step is to update the policy to an
-greedy one. The q-value update step only updates the single state-action pair visited
at timet. Afterward, the policy of stis immediately updated. Therefore, we do not
evaluate a given policy suciently well before updating the policy. This is based on the
idea of generalized policy iteration. Moreover, after the policy is updated, the policy is
immediately used to generate the next experience sample. The policy here is -greedy so
that it is exploratory.
A simulation example is shown in Figure 7.2 to demonstrate the Sarsa algorithm.
Unlike all the tasks we have seen in this book, the task here aims to nd an optimal
path from a specic starting state to a target state. It does notaim to nd the optimal
policies for all states. This task is often encountered in practice where the starting state
(e.g., home) and the target state (e.g., workplace) are xed, and we only need to nd an
optimal path connecting them. This task is relatively simple because we only need to
explore the states that are close to the path and do not need to explore all the states.
However, if we do not explore all the states, the nal path may be locally optimal rather
than globally optimal.
The simulation setup and simulation results are discussed below.
Simulation setup: In this example, all the episodes start from the top-left state and ter-
minate at the target state. The reward settings are rtarget = 0,rforbidden =rboundary =
 10, androther = 1. Moreover, t(s;a) = 0:1 for alltand= 0:1. The initial
guesses of the action values are q0(s;a) = 0 for all ( s;a). The initial policy has a
135

## 第149页

7.2. TD learning of action values: Sarsa
1 2 3 4 5
1
2
3
4
5
0100200300400500-400-2000Total rewards
0100200300400500
Episode index0100200Episode length
Figure 7.2: An example for demonstrating Sarsa. All the episodes start from the top-left state and
terminate when reaching the target state (the blue cell). The goal is to nd an optimal path from the
starting state to the target state. The reward settings are rtarget = 0,rforbidden =rboundary = 10, and
rother = 1. The learning rate is = 0:1 and the value of is 0.1. The left gure shows the nal policy
obtained by the algorithm. The right gures show the total reward and length of every episode.
uniform distribution: 0(ajs) = 0:2 for alls;a.
Learned policy: The left gure in Figure 7.2 shows the nal policy learned by Sarsa.
As can be seen, this policy can successfully lead to the target state from the starting
state. However, the policies of some other states may not be optimal. That is because
the other states are not well explored.
Total reward of each episode: The top-right subgure in Figure 7.2 shows the to-
tal reward of each episode. Here, the total reward is the non-discounted sum of all
immediate rewards. As can be seen, the total reward of each episode increases grad-
ually. That is because the initial policy is not good and hence negative rewards are
frequently obtained. As the policy becomes better, the total reward increases.
Length of each episode: The bottom-right subgure in Figure 7.2 shows that the
length of each episode drops gradually. That is because the initial policy is not good
and may take many detours before reaching the target. As the policy becomes better,
the length of the trajectory becomes shorter. Notably, the length of an episode may
increase abruptly (e.g., the 460th episode) and the corresponding total reward also
drops sharply. That is because the policy is -greedy, and there is a chance for it to
take non-optimal actions. One way to resolve this problem is to use decaying whose
value converges to zero gradually.
Finally, Sarsa also has some variants such as Expected Sarsa. Interested readers may
check Box 7.4.
136

## 第150页

7.2. TD learning of action values: Sarsa
Box 7.4: Expected Sarsa
Given a policy , its action values can be evaluated by Expected Sarsa, which is a
variant of Sarsa. The Expected Sarsa algorithm is
qt+1(st;at) =qt(st;at) t(st;at)h
qt(st;at) (rt+1+
E[qt(st+1;A)])i
;
qt+1(s;a) =qt(s;a);for all (s;a)6= (st;at);
where
E[qt(st+1;A)] =X
at(ajst+1)qt(st+1;a):=vt(st+1)
is the expected value of qt(st+1;a) under policy t. The expression of the Ex-
pected Sarsa algorithm is very similar to that of Sarsa. They are dierent only
in terms of their TD targets. In particular, the TD target in Expected Sarsa is
rt+1+
E[qt(st+1;A)], while that of Sarsa is rt+1+
qt(st+1;at+1). Since the algorithm
involves an expected value, it is called Expected Sarsa. Although calculating the
expected value may increase the computational complexity slightly, it is benecial
in the sense that it reduces the estimation variances because it reduces the random
variables in Sarsa from fst;at;rt+1;st+1;at+1gtofst;at;rt+1;st+1g.
Similar to the TD learning algorithm in (7.1), Expected Sarsa can be viewed as
a stochastic approximation algorithm for solving the following equation:
q(s;a) =Eh
Rt+1+
E[q(St+1;At+1)jSt+1]St=s;At=ai
;for alls;a: (7.15)
The above equation may look strange at rst glance. In fact, it is another expression
of the Bellman equation. To see that, substituting
E[q(St+1;At+1)jSt+1] =X
A0q(St+1;A0)(A0jSt+1) =v(St+1)
into (7.15) gives
q(s;a) =Eh
Rt+1+
v(St+1)jSt=s;At=ai
;
which is clearly the Bellman equation.
The implementation of Expected Sarsa is similar to that of Sarsa. More details
can be found in [3,36,37].
137

## 第151页

7.3. TD learning of action values: n-step Sarsa
7.3 TD learning of action values: n-step Sarsa
This section introduces n-step Sarsa , an extension of Sarsa. We will see that Sarsa and
MC learning are two extreme cases of n-step Sarsa.
Recall that the denition of the action value is
q(s;a) =E[GtjSt=s;At=a]; (7.16)
whereGtis the discounted return satisfying
Gt=Rt+1+
Rt+2+
2Rt+3+::::
In fact,Gtcan also be decomposed into dierent forms:
Sarsa  G(1)
t=Rt+1+
q(St+1;At+1);
G(2)
t=Rt+1+
Rt+2+
2q(St+2;At+2);
...
n-step Sarsa  G(n)
t=Rt+1+
Rt+2++
nq(St+n;At+n);
...
MC  G(1)
t=Rt+1+
Rt+2+
2Rt+3+
3Rt+4:::
It should be noted that Gt=G(1)
t=G(2)
t=G(n)
t=G(1)
t, where the superscripts merely
indicate the dierent decomposition structures of Gt.
Substituting dierent decompositions of G(n)
tintoq(s;a) in (7.16) results in dierent
algorithms.
Whenn= 1, we have
q(s;a) =E[G(1)
tjs;a] =E[Rt+1+
q(St+1;At+1)js;a]:
The corresponding stochastic approximation algorithm for solving this equation is
qt+1(st;at) =qt(st;at) t(st;at)h
qt(st;at) (rt+1+
qt(st+1;at+1))i
;
which is the Sarsa algorithm in (7.12).
Whenn=1, we have
q(s;a) =E[G(1)
tjs;a] =E[Rt+1+
Rt+2+
2Rt+3+:::js;a]:
138

## 第152页

7.3. TD learning of action values: n-step Sarsa
The corresponding algorithm for solving this equation is
qt+1(st;at) =gt:=rt+1+
rt+2+
2rt+3+:::;
wheregtis a sample of Gt. In fact, this is the MC learning algorithm, which approx-
imates the action value of ( st;at) using the discounted return of an episode starting
from (st;at).
For a general value of n, we have
q(s;a) =E[G(n)
tjs;a] =E[Rt+1+
Rt+2++
nq(St+n;At+n)js;a]:
The corresponding algorithm for solving the above equation is
qt+1(st;at) =qt(st;at)
 t(st;at)h
qt(st;at)  
rt+1+
rt+2++
nqt(st+n;at+n)i
:(7.17)
This algorithm is called n-step Sarsa .
In summary, n-step Sarsa is a more general algorithm because it becomes the (one-
step) Sarsa algorithm when n= 1 and the MC learning algorithm when n=1(by
settingt= 1).
To implement the n-step Sarsa algorithm in (7.17), we need the experience samples
(st;at;rt+1;st+1;at+1;:::;rt+n;st+n;at+n). Since (rt+n;st+n;at+n) has not been collected
at timet, we have to wait until time t+nto update the q-value of ( st;at). To that end,
(7.17) can be rewritten as
qt+n(st;at) =qt+n 1(st;at)
 t+n 1(st;at)h
qt+n 1(st;at)  
rt+1+
rt+2++
nqt+n 1(st+n;at+n)i
;
whereqt+n(st;at) is the estimate of q(st;at) at timet+n.
Sincen-step Sarsa includes Sarsa and MC learning as two extreme cases, it is not
surprising that the performance of n-step Sarsa is between that of Sarsa and MC learning.
In particular, if nis selected as a large number, n-step Sarsa is close to MC learning:
the estimate has a relatively high variance but a small bias. If nis selected to be small,
n-step Sarsa is close to Sarsa: the estimate has a relatively large bias but a low variance.
Finally, the n-step Sarsa algorithm presented here is merely used for policy evaluation.
It must be combined with a policy improvement step to learn optimal policies. The
implementation is similar to that of Sarsa and is omitted here. Interested readers may
check [3, Chapter 7] for a detailed analysis of multi-step TD learning.
139

## 第153页

7.4. TD learning of optimal action values: Q-learning
7.4 TD learning of optimal action values: Q-learning
In this section, we introduce the Q-learning algorithm, one of the most classic reinforce-
ment learning algorithms [38,39]. Recall that Sarsa can only estimate the action values of
a given policy, and it must be combined with a policy improvement step to nd optimal
policies. By contrast, Q-learning can directly estimate optimal action values and nd
optimal policies.
7.4.1 Algorithm description
The Q-learning algorithm is
qt+1(st;at) =qt(st;at) t(st;at)
qt(st;at)  
rt+1+
max
a2A(st+1)qt(st+1;a)
;(7.18)
qt+1(s;a) =qt(s;a);for all (s;a)6= (st;at);
wheret= 0;1;2;:::. Here,qt(st;at) is the estimate of the optimal action value of ( st;at)
andt(st;at) is the learning rate for ( st;at).
The expression of Q-learning is similar to that of Sarsa. They are dierent only
in terms of their TD targets: the TD target of Q-learning is rt+1+
maxaqt(st+1;a),
whereas that of Sarsa is rt+1+
qt(st+1;at+1). Moreover, given ( st;at), Sarsa requires
(rt+1;st+1;at+1) in every iteration, whereas Q-learning merely requires ( rt+1;st+1).
Why is Q-learning designed as the expression in (7.18), and what does it do mathe-
matically? Q-learning is a stochastic approximation algorithm for solving the following
equation:
q(s;a) =Eh
Rt+1+
max
aq(St+1;a)St=s;At=ai
: (7.19)
This is the Bellman optimality equation expressed in terms of action values. The proof is
given in Box 7.5. The convergence analysis of Q-learning is similar to Theorem 7.1 and
omitted here. More information can be found in [32,39].
Box 7.5: Showing that (7.19) is the Bellman optimality equation
By the denition of expectation, (7.19) can be rewritten as
q(s;a) =X
rp(rjs;a)r+
X
s0p(s0js;a) max
a2A(s0)q(s0;a):
140

## 第154页

7.4. TD learning of optimal action values: Q-learning
Taking the maximum of both sides of the equation gives
max
a2A(s)q(s;a) = max
a2A(s)"X
rp(rjs;a)r+
X
s0p(s0js;a) max
a2A(s0)q(s0;a)#
:
By denoting v(s):= maxa2A(s)q(s;a), we can rewrite the above equation as
v(s) = max
a2A(s)"X
rp(rjs;a)r+
X
s0p(s0js;a)v(s0)#
= max
X
a2A(s)(ajs)"X
rp(rjs;a)r+
X
s0p(s0js;a)v(s0)#
;
which is clearly the Bellman optimality equation in terms of state values as introduced
in Chapter 3.
7.4.2 O-policy vs on-policy
We next introduce two important concepts: on-policy learning and o-policy learning .
What makes Q-learning slightly special compared to the other TD algorithms is that
Q-learning is o-policy while the others are on-policy.
Two policies exist in any reinforcement learning task: a behavior policy and a target
policy . The behavior policy is the one used to generate experience samples. The target
policy is the one that is constantly updated to converge to an optimal policy. When the
behavior policy is the same as the target policy, such a learning process is called on-policy .
Otherwise, when they are dierent, the learning process is called o-policy .
The advantage of o-policy learning is that it can learn optimal policies based on
the experience samples generated by other policies, which may be, for example, a policy
executed by a human operator. As an important case, the behavior policy can be selected
to be exploratory . For example, if we would like to estimate the action values of all state-
action pairs, we must generate episodes visiting every state-action pair suciently many
times. Although Sarsa uses -greedy policies to maintain certain exploration abilities, the
value ofis usually small and hence the exploration ability is limited. By contrast, if
we can use a policy with a strong exploration ability to generate episodes and then use
o-policy learning to learn optimal policies, the learning eciency would be signicantly
increased.
To determine if an algorithm is on-policy or o-policy, we can examine two aspects.
The rst is the mathematical problem that the algorithm aims to solve. The second is
the experience samples required by the algorithm.
Sarsa is on-policy.
141

## 第155页

7.4. TD learning of optimal action values: Q-learning
The reason is as follows. Sarsa has two steps in every iteration. The rst step is to
evaluate a policy by solving its Bellman equation. To do that, we need samples
generated by . Therefore, is the behavior policy. The second step is to obtain an
improved policy based on the estimated values of . As a result, is the target policy
that is constantly updated and eventually converges to an optimal policy. Therefore,
the behavior policy and the target policy are the same.
From another point of view, we can examine the samples required by the algorithm.
The samples required by Sarsa in every iteration include ( st;at;rt+1;st+1;at+1). How
these samples are generated is illustrated below:
stb   !atmodel   !rt+1;st+1b   !at+1
As can be seen, the behavior policy bis the one that generates atatstandat+1
atst+1. The Sarsa algorithm aims to estimate the action value of (st;at) of a policy
denoted as T, which is the target policy because it is improved in every iteration
based on the estimated values. In fact, Tis the same as bbecause the evaluation
ofTrelies on the samples ( rt+1;st+1;at+1), whereat+1is generated following b. In
other words, the policy that Sarsa evaluates is the policy used to generate samples.
Q-learning is o-policy.
The fundamental reason is that Q-learning is an algorithm for solving the Bellman
optimality equation , whereas Sarsa is for solving the Bellman equation of a given
policy. While solving the Bellman equation can evaluate the associated policy, solving
the Bellman optimality equation can directly generate the optimal values and optimal
policies.
In particular, the samples required by Q-learning in every iteration is ( st;at;rt+1;st+1).
How these samples are generated is illustrated below:
stb   !atmodel   !rt+1;st+1
As can be seen, the behavior policy bis the one that generates atatst. The Q-learning
algorithm aims to estimate the optimal action value of (st;at). This estimation process
relies on the samples ( rt+1;st+1). The process of generating ( rt+1;st+1) does not
involvebbecause it is governed by the system model (or by interacting with the
environment). Therefore, the estimation of the optimal action value of ( st;at) does
not involve band we can use any bto generate atatst. Moreover, the target
policyThere is the greedy policy obtained based on the estimated optimal values
(Algorithm 7.3). The behavior policy does not have to be the same as T.
MC learning is on-policy. The reason is similar to that of Sarsa. The target policy to
be evaluated and improved is the same as the behavior policy that generates samples.
142

## 第156页

7.4. TD learning of optimal action values: Q-learning
Another concept that may be confused with on-policy/o-policy is online/oine .
Online learning refers to the case where the agent updates the values and policies while
interacting with the environment. Oine learning refers to the case where the agent up-
dates the values and policies using pre-collected experience data without interacting with
the environment. If an algorithm is on-policy, then it can be implemented in an online
fashion, but cannot use pre-collected data generated by other policies. If an algorithm is
o-policy, then it can be implemented in either an online or oine fashion.
Algorithm 7.2: Optimal policy learning via Q-learning (on-policy version)
Initialization: t(s;a) =>0for all (s;a)and allt.2(0;1). Initialq0(s;a)for all
(s;a). Initial-greedy policy 0derived from q0.
Goal: Learn an optimal path that can lead the agent to the target state from an initial
states0.
For each episode, do
Ifst(t= 0;1;2;::: ) is not the target state, do
Collect the experience sample (at;rt+1;st+1)givenst: generate atfollowing
t(st); generatert+1;st+1by interacting with the environment.
Update q-value for (st;at):
qt+1(st;at) =qt(st;at) t(st;at)h
qt(st;at) (rt+1+
maxaqt(st+1;a))i
Update policy for st:
t+1(ajst) = 1 
jA(st)j(jA(st)j 1)ifa= arg max aqt+1(st;a)
t+1(ajst) =
jA(st)jotherwise
Algorithm 7.3: Optimal policy learning via Q-learning (o-policy version)
Initialization: Initial guess q0(s;a)for all (s;a). Behavior policy b(ajs)for all (s;a).
t(s;a) =>0for all (s;a)and allt.
Goal: Learn an optimal target policy Tfor all states from the experience samples
generated by b.
For each episodefs0;a0;r1;s1;a1;r2;:::ggenerated by b, do
For each step t= 0;1;2;::: of the episode, do
Update q-value for (st;at):
qt+1(st;at) =qt(st;at) t(st;at)h
qt(st;at) (rt+1+
maxaqt(st+1;a))i
Update target policy for st:
T;t+1(ajst) = 1 ifa= arg max aqt+1(st;a)
T;t+1(ajst) = 0 otherwise
143

## 第157页

7.4. TD learning of optimal action values: Q-learning
1 2 3 4 5
1
2
3
4
5
0100200300400500-400-2000Total rewards
0100200300400500
Episode index0100200Episode length
Figure 7.3: An example for demonstrating Q-learning. All the episodes start from the top-left state and
terminate after reaching the target state. The aim is to nd an optimal path from the starting state to
the target state. The reward settings are rtarget = 0,rforbidden =rboundary = 10, androther = 1. The
learning rate is = 0:1 and the value of is 0.1. The left gure shows the nal policy obtained by the
algorithm. The right gure shows the total reward and length of every episode.
7.4.3 Implementation
Since Q-learning is o-policy, it can be implemented in either an on-policy or o-policy
fashion.
The on-policy version of Q-learning is shown in Algorithm 7.2. This implementation
is similar to the Sarsa one in Algorithm 7.1. Here, the behavior policy is the same as the
target policy, which is an -greedy policy.
The o-policy version is shown in Algorithm 7.3. The behavior policy bcan be any
policy as long as it can generate sucient experience samples. It is usually favorable when
bis exploratory. Here, the target policy Tis greedy rather than -greedy since it is
not used to generate samples and hence is not required to be exploratory. Moreover, the
o-policy version of Q-learning presented here is implemented oine: all the experience
samples are collected rst and then processed.
7.4.4 Illustrative examples
We next present examples to demonstrate Q-learning.
The rst example is shown in Figure 7.3. It demonstrates on-policy Q-learning. The
goal here is to nd an optimal path from a starting state to the target state. The setup
is given in the caption of Figure 7.3. As can be seen, Q-learning can eventually nd an
optimal path. During the learning process, the length of each episode decreases, whereas
the total reward of each episode increases.
The second set of examples is shown in Figure 7.4 and Figure 7.5. They demonstrate
o-policy Q-learning. The goal here is to nd an optimal policy for all the states. The
reward setting is rboundary =rforbidden = 1, andrtarget = 1. The discount rate is 
= 0:9.
The learning rate is = 0:1.
144

## 第158页

7.5. A unied viewpoint
Ground truth: To verify the eectiveness of Q-learning, we rst need to know the
ground truth of the optimal policies and optimal state values. Here, the ground truth
is obtained by the model-based policy iteration algorithm. The ground truth is given
in Figures 7.4(a) and (b).
Experience samples: The behavior policy has a uniform distribution: the probability
of taking any action at any state is 0.2 (Figure 7.4(c)). A single episode with 100,000
steps is generated (Figure 7.4(d)). Due to the good exploration ability of the behavior
policy, the episode visits every state-action pair many times.
Learned results: Based on the episode generated by the behavior policy, the nal
target policy learned by Q-learning is shown in Figure 7.4(e). This policy is optimal
because the estimated state value error (root-mean-square error) converges to zero as
shown in Figure 7.4(f). In addition, one may notice that the learned optimal policy
is not exactly the same as that in Figure 7.4(a). In fact, there exist multiple optimal
policies that have the same optimal state values.
Dierent initial values: Since Q-learning bootstraps, the performance of the algorithm
depends on the initial guess for the action values. As shown in Figure 7.4(g), when the
initial guess is close to the true value, the estimate converges within approximately
10,000 steps. Otherwise, the convergence requires more steps (Figure 7.4(h)). Nev-
ertheless, these gures demonstrate that Q-learning can still converge rapidly even
though the initial value is not accurate.
Dierent behavior policies: When the behavior policy is not exploratory, the learning
performance drops signicantly. For example, consider the behavior policies shown
in Figure 7.5. They are -greedy policies with = 0:5 or 0:1 (the uniform policy in
Figure 7.4(c) can be viewed as -greedy with = 1). It is shown that, when decreases
from 1 to 0.5 and then to 0.1, the learning speed drops signicantly. That is because
the exploration ability of the policy is weak and hence the experience samples are
insucient.
7.5 A unied viewpoint
Up to now, we have introduced dierent TD algorithms such as Sarsa, n-step Sarsa, and
Q-learning. In this section, we introduce a unied framework to accommodate all these
algorithms and MC learning.
In particular, the TD algorithms (for action value estimation) can be expressed in a
unied expression:
qt+1(st;at) =qt(st;at) t(st;at)[qt(st;at) qt]; (7.20)
145

## 第159页

7.5. A unied viewpoint
1 2 3 4 5
1
2
3
4
5
(a) Optimal policy
1 2 3 4 5
1
2
3
4
55.8 5.6 6.2 6.5 5.8
6.5 7.2 8.0 7.2 6.5
7.2 8.0 10.0 8.0 7.2
8.0 10.0 10.0 10.0 8.0
7.2 9.0 10.0 9.0 8.1 (b) Optimal state value
1 2 3 4 5
1
2
3
4
5
(c) Behavior policy
1 2 3 4 5
1
2
3
4
5
 (d) Generated episode
1 2 3 4 5
1
2
3
4
5
(e) Learned policy
0246810
Step in the episode 10402468State value error (f) State value error when q0(s;a) = 0
0246810
Step in the episode 10400.511.522.53State value error
(g) State value error when q0(s;a) = 10
0246810
Step in the episode 104020406080100State value error (h) State value error when q0(s;a) = 100
Figure 7.4: Examples for demonstrating o-policy learning via Q-learning. The optimal policy and
optimal state values are shown in (a) and (b), respectively. The behavior policy and the generated
episode are shown in (c) and (d), respectively. The estimated policy and the estimation error evolution
are shown in (e) and (f), respectively. The cases with dierent initial values are shown in (g) and (h).
146

## 第160页

7.5. A unied viewpoint
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
5
0246810
Step in the episode 10402468State value error
(a)= 0:5
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
5
0246810
Step in the episode 1040246State value error
(b)= 0:1
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
5
0246810
Step in the episode 1040246State value error
(c)= 0:1
Figure 7.5: The performance of Q-learning drops when the behavior policy is not exploratory. The gures
in the left column show the behavior policies. The gures in the middle column show the generated
episodes following the corresponding behavior policies. The episode in each example has 100,000 steps.
The gures in the right column show the evolution of the root-mean-square error of the estimated state
values.
147

## 第161页

7.6. Summary
Algorithm Expression of the TD target qtin(7.20)
Sarsa qt=rt+1+
qt(st+1;at+1)
n-step Sarsa qt=rt+1+
rt+2++
nqt(st+n;at+n)
Q-learning qt=rt+1+
maxaqt(st+1;a)
Monte Carlo qt=rt+1+
rt+2+
2rt+3+:::
Algorithm Equation to be solved
Sarsa BE:q(s;a) =E[Rt+1+
q(St+1;At+1)jSt=s;At=a]
n-step Sarsa BE:q(s;a) =E[Rt+1+
Rt+2++
nq(St+n;At+n)jSt=s;At=a]
Q-learning BOE:q(s;a) =E
Rt+1+
maxaq(St+1;a)St=s;At=a
Monte Carlo BE:q(s;a) =E[Rt+1+
Rt+2+
2Rt+3+:::jSt=s;At=a]
Table 7.2: A unied point of view of TD algorithms. Here, BE and BOE denote the Bellman equation
and Bellman optimality equation, respectively.
where qtis the TD target . Dierent TD algorithms have dierent  qt. See Table 7.2 for a
summary. The MC learning algorithm can be viewed as a special case of (7.20): we can
sett(st;at) = 1 and then (7.20) becomes qt+1(st;at) = qt.
Algorithm (7.20) can be viewed as a stochastic approximation algorithm for solving
a unied equation: q(s;a) =E[qtjs;a]. This equation has dierent expressions with
dierent qt. These expressions are summarized in Table 7.2. As can be seen, all of the
algorithms aim to solve the Bellman equation except Q-learning, which aims to solve the
Bellman optimality equation.
7.6 Summary
This chapter introduced an important class of reinforcement learning algorithms called
TD learning. The specic algorithms that we introduced include Sarsa, n-step Sarsa, and
Q-learning. All these algorithms can be viewed as stochastic approximation algorithms
for solving Bellman or Bellman optimality equations.
The TD algorithms introduced in this chapter, except Q-learning, are used to eval-
uate a given policy. That is to estimate a given policy's state/action values from some
experience samples. Together with policy improvement, they can be used to learn opti-
mal policies. Moreover, these algorithms are on-policy: the target policy is used as the
behavior policy to generate experience samples.
Q-learning is slightly special compared to the other TD algorithms in the sense that
it is o-policy. The target policy can be dierent from the behavior policy in Q-learning.
The fundamental reason why Q-learning is o-policy is that Q-learning aims to solve the
Bellman optimality equation rather than the Bellman equation of a given policy.
148

## 第162页

7.7. Q&A
It is worth mentioning that there are some methods that can convert an on-policy
algorithm to be o-policy. Importance sampling is a widely used one [3, 40] and will be
introduced in Chapter 10. Finally, there are some variants and extensions of the TD
algorithms introduced in this chapter [41{45]. For example, the TD( ) method provides
a more general and unied framework for TD learning. More information can be found
in [3,20,46].
7.7 Q&A
Q: What does the term \TD" in TD learning mean?
A: Every TD algorithm has a TD error, which represents the discrepancy between the
new sample and the current estimate. Since this discrepancy is calculated between
dierent time steps, it is called temporal-dierence.
Q: What does the term \learning" in TD learning mean?
A: From a mathematical point of view, \learning" simply means \estimation". That
is to estimate state/action values from some samples and then obtain policies based
on the estimated values.
Q: While Sarsa can estimate the action values of a given policy, how can it be used
to learn optimal policies?
A: To obtain an optimal policy, the value estimation process should interact with
the policy improvement process. That is, after a value is updated, the corresponding
policy should be updated. Then, the updated policy generates new samples that can
be used to estimate values again. This is the idea of generalized policy iteration.
Q: Why does Sarsa update policies to be -greedy?
A: That is because the policy is also used to generate samples for value estimation.
Hence, it should be exploratory to generate sucient experience samples.
Q: While Theorems 7.1 and 7.2 require that the learning rate tconverges to zero
gradually, why is it often set to be a small constant in practice?
A: The fundamental reason is that the policy to be evaluated keeps changing (or called
nonstationary). In particular, a TD learning algorithm like Sarsa aims to estimate
the action values of a given policy. If the policy is xed, using a decaying learning
rate is acceptable. However, in the optimal policy learning process, the policy that
Sarsa aims to evaluate keeps changing after every iteration. We need a constant
learning rate in this case; otherwise, a decaying learning rate may be too small to
eectively evaluate policies. Although a drawback of constant learning rates is that
the value estimate may 
uctuate eventually, the 
uctuation is neglectable as long as
the constant learning rate is suciently small.
149

## 第163页

7.7. Q&A
Q: Should we learn the optimal policies for all states or a subset of the states?
A: It depends on the task. One may notice that some tasks considered in this chapter
(e.g., Figure 7.2) do notrequire nding the optimal policies for all states. Instead,
they only need to nd an optimal path from a given starting state to the target state.
Such tasks are not demanding in terms of data because the agent does not need to
visit every state-action pair suciently many times. It, however, must be noted that
the obtained path is not guaranteed to be optimal. That is because better paths may
be missed if not all state-action pairs are well explored. Nevertheless, given sucient
data, we can still nd a good or locally optimal path.
Q: Why is Q-learning o-policy while all the other TD algorithms in this chapter are
on-policy?
A: The fundamental reason is that Q-learning aims to solve the Bellman optimality
equation, whereas the other TD algorithms aim to solve the Bellman equation of a
given policy. Details can be found in Section 7.4.2.
Q: Why does the o-policy version of Q-learning update policies to be greedy instead
of-greedy?
A: That is because the target policy is not required to generate experience samples.
Hence, it is not required to be exploratory.
150

## 第164页

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

## 第165页

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

## 第166页

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

## 第167页

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

## 第168页

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

## 第169页

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

## 第170页

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

## 第171页

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

## 第172页

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

## 第173页

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

## 第174页

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

## 第175页

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

## 第176页

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

## 第177页

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

## 第178页

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

## 第179页

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

## 第180页

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

## 第181页

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

## 第182页

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

## 第183页

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

## 第184页

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

## 第185页

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

## 第186页

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

## 第187页

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

## 第188页

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

## 第189页

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

## 第190页

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

## 第191页

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

## 第192页

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

## 第193页

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

## 第194页

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

## 第195页

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

## 第196页

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

## 第197页

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

## 第198页

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

## 第199页

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

## 第200页

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

## 第201页

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

## 第202页

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

## 第203页

8.6. Q&A
190

## 第204页

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

## 第205页

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

## 第206页

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

## 第207页

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

## 第208页

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

## 第209页

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

## 第210页

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

## 第211页

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

## 第212页

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

## 第213页

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

## 第214页

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

## 第215页

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

## 第216页

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

## 第217页

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

## 第218页

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

## 第219页

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

## 第220页

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

## 第221页

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

## 第222页

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

## 第223页

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

## 第224页

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

## 第225页

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

## 第226页

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

## 第227页

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

## 第228页

Chapter 10
Actor-Critic Methods
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
Figure 10.1: Where we are in this book.
This chapter introduces actor-critic methods. From one point of view, \actor-critic"
refers to a structure that incorporates both policy-based and value-based methods. Here,
an \actor" refers to a policy update step. The reason that it is called an actor is that the
actions are taken by following the policy. Here, an \critic" refers to a value update step. It
is called a critic because it criticizes the actor by evaluating its corresponding values. From
another point of view, actor-critic methods are still policy gradient algorithms. They can
be obtained by extending the policy gradient algorithm introduced in Chapter 9. It is
important for the reader to well understand the contents of Chapters 8 and 9 before
studying this chapter.
215

## 第229页

10.1. The simplest actor-critic algorithm (QAC)
10.1 The simplest actor-critic algorithm (QAC)
This section introduces the simplest actor-critic algorithm. This algorithm can be easily
obtained by extending the policy gradient algorithm in (9.32).
Recall that the idea of the policy gradient method is to search for an optimal policy
by maximizing a scalar metric J(). The gradient-ascent algorithm for maximizing J()
is
t+1=t+rJ(t)
=t+ES;Ah
rln(AjS;t)q(S;A)i
; (10.1)
whereis a distribution of the states (see Theorem 9.1 for more information). Since the
true gradient is unknown, we can use a stochastic gradient to approximate it:
t+1=t+rln(atjst;t)qt(st;at): (10.2)
This is the algorithm given in (9.32).
Equation (10.2) is important because it clearly shows how policy-based and value-
based methods can be combined. On the one hand, it is a policy-based algorithm since it
directly updates the policy parameter. On the other hand, this equation requires knowing
qt(st;at), which is an estimate of the action value q(st;at). As a result, another value-
based algorithm is required to generate qt(st;at). So far, we have studied two ways to
estimate action values in this book. The rst is based on Monte Carlo learning and the
second is temporal-dierence (TD) learning.
Ifqt(st;at) is estimated by Monte Carlo learning, the corresponding algorithm is called
REINFORCE orMonte Carlo policy gradient , which has already been introduced in
Chapter 9.
Ifqt(st;at) is estimated by TD learning, the corresponding algorithms are usually
called actor-critic . Therefore, actor-critic methods can be obtained by incorporating
TD-based value estimation into policy gradient methods.
The procedure of the simplest actor-critic algorithm is summarized in Algorithm 10.1.
The critic corresponds to the value update step via the Sarsa algorithm presented in
(8.35). The action values are represented by a parameterized function q(s;a;w ). The
actor corresponds to the policy update step in (10.2). This actor-citric algorithm is
sometimes called Q actor-critic (QAC). Although it is simple, QAC reveals the core idea
of actor-critic methods. It can be extended to generate many advanced ones as shown in
the rest of this chapter.
216

## 第230页

10.2. Advantage actor-critic (A2C)
Algorithm 10.1: The simplest actor-critic algorithm (QAC)
Initialization: A policy function (ajs;0)where0is the initial parameter. A value
functionq(s;a;w 0)wherew0is the initial parameter. w;>0.
Goal: Learn an optimal policy to maximize J().
At time step tin each episode, do
Generateatfollowing(ajst;t), observert+1;st+1, and then generate at+1following
(ajst+1;t).
Actor (policy update):
t+1=t+rln(atjst;t)q(st;at;wt)
Critic (value update):
wt+1=wt+w
rt+1+
q(st+1;at+1;wt) q(st;at;wt)
rwq(st;at;wt)
10.2 Advantage actor-critic (A2C)
We now introduce the algorithm of advantage actor-critic . The core idea of this algorithm
is to introduce a baseline to reduce estimation variance.
10.2.1 Baseline invariance
One interesting property of the policy gradient is that it is invariant to an additional
baseline . That is
ES;Ah
rln(AjS;t)q(S;A)i
=ES;Ah
rln(AjS;t)(q(S;A) b(S))i
;
(10.3)
where the additional baseline b(S) is a scalar function of S. We next answer two questions
about the baseline.
First, why is (10.3) valid?
Equation (10.3) holds if and only if
ES;Ah
rln(AjS;t)b(S)i
= 0:
217

## 第231页

10.2. Advantage actor-critic (A2C)
This equation is valid because
ES;Ah
rln(AjS;t)b(S)i
=X
s2S(s)X
a2A(ajs;t)rln(ajs;t)b(s)
=X
s2S(s)X
a2Ar(ajs;t)b(s)
=X
s2S(s)b(s)X
a2Ar(ajs;t)
=X
s2S(s)b(s)rX
a2A(ajs;t)
=X
s2S(s)b(s)r1 = 0:
Second, why is the baseline useful?
The baseline is useful because it can reduce the approximation variance when we use
samples to approximate the true gradient. In particular, let
X(S;A):=rln(AjS;t)[q(S;A) b(S)]: (10.4)
Then, the true gradient is E[X(S;A)]. Since we need to use a stochastic sample xto
approximate E[X], it would be favorable if the variance var( X) is small. For example,
if var(X) is close to zero, then any sample xcan accurately approximate E[X]. On
the contrary, if var( X) is large, the value of a sample may be far from E[X].
Although E[X] is invariant to the baseline, the variance var( X) isnot. Our goal is to
design a good baseline to minimize var( X). In the algorithms of REINFORCE and
QAC, we set b= 0, which is not guaranteed to be a good baseline.
In fact, the optimal baseline that minimizes var( X) is
b(s) =EA
krln(Ajs;t)k2q(s;A)
EA
krln(Ajs;t)k2; s2S: (10.5)
The proof is given in Box 10.1.
Although the baseline in (10.5) is optimal, it is too complex to be useful in practice.
If the weightkrln(Ajs;t)k2is removed from (10.5), we can obtain a suboptimal
baseline that has a concise expression:
by(s) =EA[q(s;A)] =v(s); s2S:
Interestingly, this suboptimal baseline is the state value.
218

## 第232页

10.2. Advantage actor-critic (A2C)
Box 10.1: Showing that b(s)in(10.5) is the optimal baseline
Let x:=E[X], which is invariant for any b(s). IfXis a vector, its variance is a
matrix. It is common to select the trace of var( X) as a scalar objective function for
optimization:
tr[var(X)] = tr E[(X x)(X x)T]
= trE[XXT xXT XxT+ xxT]
=E[XTX XTx xTX+ xTx]
=E[XTX] xTx: (10.6)
When deriving the above equation, we use the trace property tr( AB) = tr(BA)
for any squared matrices A;B with appropriate dimensions. Since  xis invariant,
equation (10.6) suggests that we only need to minimize E[XTX]. WithXdened in
(10.4), we have
E[XTX] =E
(rln)T(rln)(q(S;A) b(S))2
=E
krlnk2(q(S;A) b(S))2
;
where(AjS;) is written as for short. Since SandA, the above equation
can be rewritten as
E[XTX] =X
s2S(s)EA
krlnk2(q(s;A) b(s))2
:
To ensurerbE[XTX] = 0,b(s) for anys2Sshould satisfy
EA
krlnk2(b(s) q(s;A))
= 0; s2S:
The above equation can be easily solved to obtain the optimal baseline:
b(s) =EA[krlnk2q(s;A)]
EA[krlnk2]; s2S:
More discussions on optimal baselines in policy gradient methods can be found in
[69,70].
219

## 第233页

10.2. Advantage actor-critic (A2C)
10.2.2 Algorithm description
Whenb(s) =v(s), the gradient-ascent algorithm in (10.1) becomes
t+1=t+Eh
rln(AjS;t)[q(S;A) v(S)]i
:=t+Eh
rln(AjS;t)(S;A)i
: (10.7)
Here,
(S;A):=q(S;A) v(S)
is called the advantage function , which re
ects the advantage of one action over the
others. More specically, note that v(s) =P
a2A(ajs)q(s;a) is the mean of the action
values. If(s;a)>0, it means that the corresponding action has a greater value than
the mean value.
The stochastic version of (10.7) is
t+1=t+rln(atjst;t)[qt(st;at) vt(st)]
=t+rln(atjst;t)t(st;at); (10.8)
wherest;atare samples of S;A at timet. Here,qt(st;at) andvt(st) are approximations of
q(t)(st;at) andv(t)(st), respectively. The algorithm in (10.8) updates the policy based
on the relative value ofqtwith respect to vtrather than the absolute value ofqt. This is
intuitively reasonable because, when we attempt to select an action at a state, we only
care about which action has the greatest value relative to the others.
Ifqt(st;at) andvt(st) are estimated by Monte Carlo learning, the algorithm in (10.8) is
called REINFORCE with a baseline . Ifqt(st;at) andvt(st) are estimated by TD learning,
the algorithm is usually called advantage actor-critic (A2C). The implementation of A2C
is summarized in Algorithm 10.2. It should be noted that the advantage function in this
implementation is approximated by the TD error:
qt(st;at) vt(st)rt+1+
vt(st+1) vt(st):
This approximation is reasonable because
q(st;at) v(st) =Eh
Rt+1+
v(St+1) v(St)jSt=st;At=ati
;
which is valid due to the denition of q(st;at). One merit of using the TD error is
that we only need to use a single neural network to represent v(s). Otherwise, if t=
qt(st;at) vt(st), we need to maintain two networks to represent v(s) andq(s;a),
respectively. When we use the TD error, the algorithm may also be called TD actor-
critic . In addition, it is notable that the policy (t) is stochastic and hence exploratory.
Therefore, it can be directly used to generate experience samples without relying on
220

## 第234页

10.3. O-policy actor-critic
Algorithm 10.2: Advantage actor-critic (A2C) or TD actor-critic
Initialization: A policy function (ajs;0)where0is the initial parameter. A value
functionv(s;w 0)wherew0is the initial parameter. w;>0.
Goal: Learn an optimal policy to maximize J().
At time step tin each episode, do
Generateatfollowing(ajst;t)and then observe rt+1;st+1.
Advantage (TD error):
t=rt+1+
v(st+1;wt) v(st;wt)
Actor (policy update):
t+1=t+trln(atjst;t)
Critic (value update):
wt+1=wt+wtrwv(st;wt)
techniques such as "-greedy. There are some variants of A2C such as asynchronous
advantage actor-critic (A3C). Interested readers may check [71,72].
10.3 O-policy actor-critic
The policy gradient methods that we have studied so far, including REINFORCE, QAC,
and A2C, are all on-policy . The reason for this can be seen from the expression of the
true gradient:
rJ() =ES;Ah
rln(AjS;t)(q(S;A) v(S))i
:
To use samples to approximate this true gradient, we must generate the action samples
by following (). Hence,() is the behavior policy. Since () is also the target policy
that we aim to improve, the policy gradient methods are on-policy.
In the case that we already have some samples generated by a given behavior policy,
the policy gradient methods can still be applied to utilize these samples. To do that,
we can employ a technique called importance sampling . It is worth mentioning that the
importance sampling technique is not restricted to the eld of reinforcement learning.
It is a general technique for estimating expected values dened over one probability
distribution using some samples drawn from another distribution.
10.3.1 Importance sampling
We next introduce the importance sampling technique. Consider a random variable
X2 X . Suppose that p0(X) is a probability distribution. Our goal is to estimate
EXp0[X]. Suppose that we have some i.i.d. samples fxign
i=1.
221

## 第235页

10.3. O-policy actor-critic
First, if the samples fxign
i=1are generated by following p0, then the average value
x=1
nPn
i=1xican be used to approximate EXp0[X] because xis an unbiased estimate
ofEXp0[X] and the estimation variance converges to zero as n!1 (see the law of
large numbers in Box 5.1 for more information).
Second, consider a new scenario where the samples fxign
i=1arenotgenerated by
p0. Instead, they are generated by another distribution p1. Can we still use these
samples to approximate EXp0[X]? The answer is yes. However, we can no longer use
x=1
nPn
i=1xito approximate EXp0[X] since xEXp1[X] rather than EXp0[X].
In the second scenario, EXp0[X] can be approximated based on the importance sam-
pling technique. In particular, EXp0[X] satises
EXp0[X] =X
x2Xp0(x)x=X
x2Xp1(x)p0(x)
p1(x)x
|{z}
f(x)=EXp1[f(X)]: (10.9)
Thus, estimating EXp0[X] becomes the problem of estimating EXp1[f(X)]. Let
f:=1
nnX
i=1f(xi):
Since fcan eectively approximate EXp1[f(X)], it then follows from (10.9) that
EXp0[X] =EXp1[f(X)]f=1
nnX
i=1f(xi) =1
nnX
i=1p0(xi)
p1(xi)|{z}
importance
weightxi: (10.10)
Equation (10.10) suggests that EXp0[X] can be approximated by a weighted average of
xi. Here,p0(xi)
p1(xi)is called the importance weight . Whenp1=p0, the importance weight
is 1 and fbecomes x. Whenp0(xi)p1(xi),xican be sampled more frequently by p0
but less frequently by p1. In this case, the importance weight, which is greater than one,
emphasizes the importance of this sample.
Some readers may ask the following question: while p0(x) is required in (10.10), why
do we not directly calculate EXp0[X] using its denition EXp0[X] =P
x2Xp0(x)x?
The answer is as follows. To use the denition, we need to know either the analytical
expression of p0or the value of p0(x) for everyx2X. However, it is dicult to obtain
theanalytical expression of p0when the distribution is represented by, for example, a
neural network. It is also dicult to obtain the value of p0(x) for everyx2X whenX
is large. By contrast, (10.10) merely requires the values of p0(xi) for some samples and
is much easier to implement in practice.
222

## 第236页

10.3. O-policy actor-critic
An illustrative example
We next present an example to demonstrate the importance sampling technique. Consider
X2X:=f+1; 1g. Suppose that p0is a probability distribution satisfying
p0(X= +1) = 0:5; p 0(X= 1) = 0:5:
The expectation of Xoverp0is
EXp0[X] = (+1)0:5 + ( 1)0:5 = 0:
Suppose that p1is another distribution satisfying
p1(X= +1) = 0:8; p 1(X= 1) = 0:2:
The expectation of Xoverp1is
EXp1[X] = (+1)0:8 + ( 1)0:2 = 0:6:
Suppose that we have some samples fxigdrawn over p1. Our goal is to estimate
EXp0[X] using these samples. As shown in Figure 10.2, there are more samples of +1
than 1. That is because p1(X= +1) = 0:8>p 1(X= 1) = 0:2. If we directly calculate
the average valuePn
i=1xi=nof the samples, this value converges to EXp1[X] = 0:6 (see
the dotted line in Figure 10.2). By contrast, if we calculate the weighted average value
as in (10.10), this value can successfully converge to EXp0[X] = 0 (see the solid line in
Figure 10.2).
0 50 100 150 200
Sample index-2-1012 samples
average
importance sampling
Figure 10.2: An example for demonstrating the importance sampling technique. Here, X2f+1; 1gand
p0(X= +1) =p0(X= 1) = 0:5. The samples are generated according to p1wherep1(X= +1) = 0:8
andp1(X= 1) = 0:2. The average of the samples converges to EXp1[X] = 0:6, but the weighted
average calculated by the importance sampling technique in (10.10) converges to EXp0[X] = 0.
223

## 第237页

10.3. O-policy actor-critic
Finally, the distribution p1, which is used to generate samples, must satisfy that
p1(x)6= 0 whenp0(x)6= 0. Ifp1(x) = 0 while p0(x)6= 0, the estimation result may be
problematic. For example, if
p1(X= +1) = 1; p 1(X= 1) = 0;
then the samples generated by p1are all positive: fxig=f+1;+1;:::; +1g. These
samples cannot be used to correctly estimate EXp0[X] = 0 because
1
nnX
i=1p0(xi)
p1(xi)xi=1
nnX
i=1p0(+1)
p1(+1)1 =1
nnX
i=10:5
110:5;
no matter how large nis.
10.3.2 The o-policy policy gradient theorem
With the importance sampling technique, we are ready to present the o-policy policy
gradient theorem. Suppose that is a behavior policy. Our goal is to use the samples
generated by to learn a target policy that can maximize the following metric:
J() =X
s2Sd(s)v(s) =ESd[v(S)];
wheredis the stationary distribution under policy andvis the state value under
policy. The gradient of this metric is given in the following theorem.
Theorem 10.1 (O-policy policy gradient theorem) .In the discounted case where 
2
(0;1), the gradient of J()is
rJ() =ES;A(AjS;)
(AjS)|{z}
importance
weightrln(AjS;)q(S;A)
; (10.11)
where the state distribution is
(s):=X
s02Sd(s0)Pr(sjs0); s2S;
where Pr(sjs0) =P1
k=0
k[Pk
]s0s= [(I 
P) 1]s0sis the discounted total probability of
transitioning from s0tosunder policy .
The gradient in (10.11) is similar to that in the on-policy case in Theorem 9.1, but
there are two dierences. The rst dierence is the importance weight. The second
dierence is that Ainstead ofA. Therefore, we can use the action samples
224

## 第238页

10.3. O-policy actor-critic
generated by following to approximate the true gradient. The proof of the theorem is
given in Box 10.2.
Box 10.2: Proof of Theorem 10.1
Sincedis independent of , the gradient of J() satises
rJ() =rX
s2Sd(s)v(s) =X
s2Sd(s)rv(s): (10.12)
According to Lemma 9.2, the expression of rv(s) is
rv(s) =X
s02SPr(s0js)X
a2Ar(ajs0;)q(s0;a); (10.13)
where Pr (s0js):=P1
k=0
k[Pk
]ss0= [(In 
P) 1]ss0. Substituting (10.13) into
(10.12) yields
rJ() =X
s2Sd(s)rv(s) =X
s2Sd(s)X
s02SPr(s0js)X
a2Ar(ajs0;)q(s0;a)
=X
s02S X
s2Sd(s)Pr(s0js)!X
a2Ar(ajs0;)q(s0;a)
:=X
s02S(s0)X
a2Ar(ajs0;)q(s0;a)
=X
s2S(s)X
a2Ar(ajs;)q(s;a) (change s0tos)
=ES"X
a2Ar(ajS;)q(S;a)#
:
By using the importance sampling technique, the above equation can be further
rewritten as
ES"X
a2Ar(ajS;)q(S;a)#
=ES"X
a2A(ajS)(ajS;)
(ajS)r(ajS;)
(ajS;)q(S;a)#
=ES"X
a2A(ajS)(ajS;)
(ajS)rln(ajS;)q(S;a)#
=ES;A(AjS;)
(AjS)rln(AjS;)q(S;A)
:
The proof is complete. The above proof is similar to that of Theorem 9.1.
225

## 第239页

10.3. O-policy actor-critic
10.3.3 Algorithm description
Based on the o-policy policy gradient theorem, we are ready to present the o-policy
actor-critic algorithm. Since the o-policy case is very similar to the on-policy case, we
merely present some key steps.
First, the o-policy policy gradient is invariant to any additional baseline b(s). In
particular, we have
rJ() =ES;A(AjS;)
(AjS)rln(AjS;) 
q(S;A) b(S)
;
because Eh
(AjS;)
(AjS)rln(AjS;)b(S)i
= 0. To reduce the estimation variance, we can
select the baseline as b(S) =v(S) and obtain
rJ() =E(AjS;)
(AjS)rln(AjS;) 
q(S;A) v(S)
:
The corresponding stochastic gradient-ascent algorithm is
t+1=t+(atjst;t)
(atjst)rln(atjst;t) 
qt(st;at) vt(st)
;
where>0. Similar to the on-policy case, the advantage function qt(s;a) vt(s) can
be replaced by the TD error. That is
qt(st;at) vt(st)rt+1+
vt(st+1) vt(st):=t(st;at):
Then, the algorithm becomes
t+1=t+(atjst;t)
(atjst)rln(atjst;t)t(st;at):
The implementation of the o-policy actor-critic algorithm is summarized in Algorith-
m 10.3. As can be seen, the algorithm is the same as the advantage actor-critic algorithm
except that an additional importance weight is included in both the critic and the actor.
It must be noted that, in addition to the actor, the critic is also converted from on-policy
to o-policy by the importance sampling technique. In fact, importance sampling is a
general technique that can be applied to both policy-based and value-based algorithms.
Finally, Algorithm 10.3 can be extended in various ways to incorporate more techniques
such as eligibility traces [73].
226

## 第240页

10.4. Deterministic actor-critic
Algorithm 10.3: O-policy actor-critic based on importance sampling
Initialization: A given behavior policy (ajs). A target policy (ajs;0)where0is the
initial parameter. A value function v(s;w 0)wherew0is the initial parameter. w;>0.
Goal: Learn an optimal policy to maximize J().
At time step tin each episode, do
Generateatfollowing(st)and then observe rt+1;st+1.
Advantage (TD error):
t=rt+1+
v(st+1;wt) v(st;wt)
Actor (policy update):
t+1=t+(atjst;t)
(atjst)trln(atjst;t)
Critic (value update):
wt+1=wt+w(atjst;t)
(atjst)trwv(st;wt)
10.4 Deterministic actor-critic
Up to now, the policies used in the policy gradient methods are all stochastic since it is
required that (ajs;)>0 for every ( s;a). This section shows that deterministic policies
can also be used in policy gradient methods. Here, \deterministic" indicates that, for
any state, a single action is given a probability of one and all the other actions are given
probabilities of zero. It is important to study the deterministic case since it is naturally
o-policy and can eectively handle continuous action spaces.
We have been using (ajs;) to denote a general policy, which can be either stochastic
or deterministic. In this section, we use
a=(s;)
to specically denote a deterministic policy. Dierent from which gives the probability
of an action, directly gives the action since it is a mapping from StoA. This deter-
ministic policy can be represented by, for example, a neural network with sas its input,
aas its output, and as its parameter. For the sake of simplicity, we often write (s;)
as(s) for short.
10.4.1 The deterministic policy gradient theorem
The policy gradient theorem introduced in the last chapter is only valid for stochastic
policies. When we require the policy to be deterministic, a new policy gradient theorem
must be derived.
227

## 第241页

10.4. Deterministic actor-critic
Theorem 10.2 (Deterministic policy gradient theorem) .The gradient of J()is
rJ() =X
s2S(s)r(s) 
raq(s;a)
ja=(s)
=ES
r(S) 
raq(S;a)
ja=(S)
; (10.14)
whereis a distribution of the states.
Theorem 10.2 is a summary of the results presented in Theorem 10.3 and Theorem 10.4
since the gradients in the two theorems have similar expressions. The specic expressions
ofJ() andcan be found in Theorems 10.3 and 10.4.
Unlike the stochastic case, the gradient in the deterministic case shown in (10.14)
does not involve the action random variable A. As a result, when we use samples to
approximate the true gradient, it is not required to sample actions. Therefore, the de-
terministic policy gradient method is o-policy . In addition, some readers may wonder
why 
raq(S;a)
ja=(S)cannot be written as raq(S;(S)), which seems more concise.
That is simply because, if we do that, it is unclear how q(S;(S)) is a function of a. A
concise yet less confusing expression may be raq(S;a=(S)).
In the rest of this subsection, we present the derivation details of Theorem 10.2. In
particular, we derive the gradients of two common metrics: the rst is the average value
and the second is the average reward. Since these two metrics have been discussed in
detail in Section 9.2, we sometimes use their properties without proof. For most readers,
it is sucient to be familiar with Theorem 10.2 without knowing its derivation details.
Interested readers can selectively examine the details in the remainder of this section.
Metric 1: Average value
We rst derive the gradient of the average value:
J() =E[v(s)] =X
s2Sd0(s)v(s); (10.15)
whered0is the probability distribution of the states. Here, d0is selected to be independent
offor simplicity. There are two special yet important cases of selecting d0. The rst
case is that d0(s0) = 1 and d0(s6=s0) = 0, where s0is a specic state of interest. In
this case, the policy aims to maximize the discounted return that can be obtained when
starting from s0. The second case is that d0is the distribution of a given behavior policy
that is dierent from the target policy.
To calculate the gradient of J(), we need to rst calculate the gradient of v(s) for
anys2S. Consider the discounted case where 
2(0;1).
228

## 第242页

10.4. Deterministic actor-critic
Lemma 10.1 (Gradient of v(s)).In the discounted case, it holds for any s2S that
rv(s) =X
s02SPr(s0js)r(s0) 
raq(s0;a)
ja=(s0); (10.16)
where
Pr(s0js):=1X
k=0
k[Pk
]ss0=
(I 
P) 1
ss0
is the discounted total probability of transitioning from stos0under policy . Here, []ss0
denotes the entry in the sth row and s0th column of a matrix.
Box 10.3: Proof of Lemma 10.1
Since the policy is deterministic, we have
v(s) =q(s;(s)):
Since both qandare functions of , we have
rv(s) =rq(s;(s)) = 
rq(s;a)
ja=(s)+r(s) 
raq(s;a)
ja=(s):(10.17)
By the denition of action values, for any given ( s;a), we have
q(s;a) =r(s;a) +
X
s02Sp(s0js;a)v(s0);
wherer(s;a) =P
rrp(rjs;a). Sincer(s;a) is independent of , we have
rq(s;a) = 0 +
X
s02Sp(s0js;a)rv(s0):
Substituting the above equation into (10.17) yields
rv(s) =
X
s02Sp(s0js;(s))rv(s0) +r(s) 
raq(s;a)
ja=(s)|{z}
u(s); s2S:
229

## 第243页

10.4. Deterministic actor-critic
Since the above equation is valid for all s2S, we can combine these equations to
obtain a matrix-vector form:
2
664...
rv(s)
...3
775
|{z}
rv2Rmn=2
664...
u(s)
...3
775
|{z}
u2Rmn+
(P
Im)2
664...
rv(s0)
...3
775
|{z}
rv2Rmn;
wheren=jSj,mis the dimensionality of ,Pis the state transition matrix with
[P]ss0=p(s0js;(s)), and
is the Kronecker product. The above matrix-vector
form can be written concisely as
rv=u+
(P
Im)rv;
which is a linear equation of rv. Then,rvcan be solved as
rv= (Imn 
P
Im) 1u
= (In
Im 
P
Im) 1u
=
(In 
P) 1
Im
u: (10.18)
The elementwise form of (10.18) is
rv(s) =X
s02S
(I 
P) 1
ss0u(s0)
=X
s02S
(I 
P) 1
ss0h
r(s0) 
raq(s0;a)
ja=(s0)i
: (10.19)
The quantity [( I 
P) 1]ss0has a clear probabilistic interpretation. Since ( I 

P) 1=I+
P+
2P2
+, we have

(I 
P) 1
ss0= [I]ss0+
[P]ss0+
2[P2
]ss0+=1X
k=0
k[Pk
]ss0:
Note that [Pk
]ss0is the probability of transitioning from stos0using exactly ksteps
(see Box 8.1 for more information). Therefore, [( I 
P) 1]ss0is the discounted
total probability of transitioning from stos0using any number of steps. By denoting
[(I 
P) 1]ss0:= Pr(s0js), equation (10.19) leads to (10.16).
With the preparation in Lemma 10.1, we are ready to derive the gradient of J().
Theorem 10.3 (Deterministic policy gradient theorem in the discounted case) .In the
230

## 第244页

10.4. Deterministic actor-critic
discounted case where 
2(0;1), the gradient of J()in(10.15) is
rJ() =X
s2S(s)r(s) 
raq(s;a)
ja=(s)
=ES
r(S) 
raq(S;a)
ja=(S)
;
where the state distribution is
(s) =X
s02Sd0(s0)Pr(sjs0); s2S:
Here, Pr(sjs0) =P1
k=0
k[Pk
]s0s= [(I 
P) 1]s0sis the discounted total probability of
transitioning from s0tosunder policy .
Box 10.4: Proof of Theorem 10.3
Sinced0is independent of , we have
rJ() =X
s2Sd0(s)rv(s):
Substituting the expression of rv(s) given by Lemma 10.1 into the above equation
yields
rJ() =X
s2Sd0(s)rv(s)
=X
s2Sd0(s)X
s02SPr(s0js)r(s0) 
raq(s0;a)
ja=(s0)
=X
s02S X
s2Sd0(s)Pr(s0js)!
r(s0) 
raq(s0;a)
ja=(s0)
:=X
s02S(s0)r(s0) 
raq(s0;a)
ja=(s0)
=X
s2S(s)r(s) 
raq(s;a)
ja=(s) (changes0tos)
=ES
r(S) 
raq(S;a)
ja=(S)
:
The proof is complete. The above proof is consistent with the proof of Theorem 1
in [74]. Here, we consider the case in which the states and actions are nite. When
they are continuous, the proof is similar, but the summations should be replaced by
integrals [74].
231

## 第245页

10.4. Deterministic actor-critic
Metric 2: Average reward
We next derive the gradient of the average reward:
J() = r=X
s2Sd(s)r(s)
=ESd[r(S)]; (10.20)
where
r(s) =E[Rjs;a=(s)] =X
rrp(rjs;a=(s))
is the expectation of the immediate rewards. More information about this metric can be
found in Section 9.2.
The gradient of J() is given in the following theorem.
Theorem 10.4 (Deterministic policy gradient theorem in the undiscounted case) .In the
undiscounted case, the gradient of J()in(10.20) is
rJ() =X
s2Sd(s)r(s) 
raq(s;a)
ja=(s)
=ESd
r(S) 
raq(S;a)
ja=(S)
;
wheredis the stationary distribution of the states under policy .
Box 10.5: Proof of Theorem 10.4
Since the policy is deterministic, we have
v(s) =q(s;(s)):
Since both qandare functions of , we have
rv(s) =rq(s;(s)) = 
rq(s;a)
ja=(s)+r(s) 
raq(s;a)
ja=(s):(10.21)
In the undiscounted case, it follows from the denition of action value (Section 9.3.2)
that
q(s;a) =E[Rt+1 r+v(St+1)js;a]
=X
rp(rjs;a)(r r) +X
s0p(s0js;a)v(s0)
=r(s;a) r+X
s0p(s0js;a)v(s0):
232

## 第246页

10.4. Deterministic actor-critic
Sincer(s;a) =P
rrp(rjs;a) is independent of , we have
rq(s;a) = 0 rr+X
s0p(s0js;a)rv(s0):
Substituting the above equation into (10.21) gives
rv(s) = rr+X
s0p(s0js;(s))rv(s0) +r(s) 
raq(s;a)
ja=(s)|{z}
u(s); s2S:
While the above equation is valid for all s2S, we can combine these equations to
obtain a matrix-vector form:
2
664...
rv(s)
...3
775
|{z}
rv2Rmn= 1n
rr+ (P
Im)2
664...
rv(s0)
...3
775
|{z}
rv2Rmn+2
664...
u(s)
...3
775
|{z}
u2Rmn;
wheren=jSj,mis the dimension of ,Pis the state transition matrix with
[P]ss0=p(s0js;(s)), and
is the Kronecker product. The above matrix-vector
form can be written concisely as
rv=u 1n
rr+ (P
Im)rv;
and hence
1n
rr=u+ (P
Im)rv rv: (10.22)
Sincedis the stationary distribution, we have dT
P=dT
. Multiplying dT

Imon
both sides of (10.22) gives
(dT
1n)
rr=dT

Imu+ (dT
P)
Imrv dT

Imrv
=dT

Imu+dT

Imrv dT

Imrv
=dT

Imu:
233

## 第247页

10.4. Deterministic actor-critic
SincedT
1n= 1, the above equations become
rr=dT

Imu
=X
s2Sd(s)u(s)
=X
s2Sd(s)r(s) 
raq(s;a)
ja=(s)
=ESd
r(S) 
raq(S;a)
ja=(S)
:
The proof is complete.
10.4.2 Algorithm description
Based on the gradient given in Theorem 10.2, we can apply the gradient-ascent algorithm
to maximize J():
t+1=t+ES
r(S) 
raq(S;a)
ja=(S)
:
The corresponding stochastic gradient-ascent algorithm is
t+1=t+r(st) 
raq(st;a)
ja=(st):
The implementation is summarized in Algorithm 10.4. It should be noted that this
algorithm is o-policy since the behavior policy may be dierent from . First, the
actor is o-policy. We already explained the reason when presenting Theorem 10.2.
Second, the critic is also o-policy. Special attention must be paid to why the critic is
o-policy but does not require the importance sampling technique. In particular, the
experience sample required by the critic is ( st;at;rt+1;st+1;~at+1), where ~at+1=(st+1).
The generation of this experience sample involves two policies. The rst is the policy
for generating atatst, and the second is the policy for generating ~ at+1atst+1. The
rst policy that generates atis the behavior policy since atis used to interact with the
environment. The second policy must be because it is the policy that the critic aims
to evaluate. Hence, is the target policy. It should be noted that ~ at+1is not used to
interact with the environment in the next time step. Hence, is not the behavior policy.
Therefore, the critic is o-policy.
How to select the function q(s;a;w )? The original research work [74] that proposed
the deterministic policy gradient method adopted linear functions: q(s;a;w ) =T(s;a)w
where(s;a) is the feature vector. It is currently popular to represent q(s;a;w ) using
neural networks, as suggested in the deep deterministic policy gradient (DDPG) method
[75].
234

## 第248页

10.5. Summary
Algorithm 10.4: Deterministic policy gradient or deterministic actor-critic
Initialization: A given behavior policy (ajs). A deterministic target policy (s;0)
where0is the initial parameter. A value function q(s;a;w 0)wherew0is the initial
parameter. w;>0.
Goal: Learn an optimal policy to maximize J().
At time step tin each episode, do
Generateatfollowingand then observe rt+1;st+1.
TD error:
t=rt+1+
q(st+1;(st+1;t);wt) q(st;at;wt)
Actor (policy update):
t+1=t+r(st;t) 
raq(st;a;wt)
ja=(st)
Critic (value update):
wt+1=wt+wtrwq(st;at;wt)
How to select the behavior policy ? It can be any exploratory policy. It can also be
a stochastic policy obtained by adding noise to [75]. In this case, is also the behavior
policy and hence this way is an on-policy implementation.
10.5 Summary
In this chapter, we introduced actor-critic methods. The contents are summarized as
follows.
Section 10.1 introduced the simplest actor-critic algorithm called QAC. This algo-
rithm is similar to the policy gradient algorithm, REINFORCE, introduced in the
last chapter. The only dierence is that the q-value estimation in QAC relies on TD
learning while REINFORCE relies on Monte Carlo estimation.
Section 10.2 extended QAC to advantage actor-critic. It was shown that the policy
gradient is invariant to any additional baseline. It was then shown that an optimal
baseline could help reduce the estimation variance.
Section 10.3 further extended the advantage actor-critic algorithm to the o-policy
case. To do that, we introduced an important technique called importance sampling.
Finally, while all the previously presented policy gradient algorithms rely on stochastic
policies, we showed in Section 10.4 that the policy can be forced to be determinis-
tic. The corresponding gradient was derived, and the deterministic policy gradient
algorithm was introduced.
Policy gradient and actor-critic methods are widely used in modern reinforcement
learning. There exist a large number of advanced algorithms in the literature such as
SAC [76,77], TRPO [78], PPO [79], and TD3 [80]. In addition, the single-agent case can
235

## 第249页

10.6. Q&A
also be extended to the case of multi-agent reinforcement learning [81{85]. Experience
samples can also be used to t system models to achieve model-based reinforcement learn-
ing [15, 86, 87]. Distributional reinforcement learning provides a fundamentally dierent
perspective from the conventional one [88, 89]. The relationships between reinforcement
learning and control theory have been discussed in [90{95]. This book is not able to cov-
er all these topics. Hopefully, the foundations laid by this book can help readers better
study them in the future.
10.6 Q&A
Q: What is the relationship between actor-critic and policy gradient methods?
A: Actor-critic methods are actually policy gradient methods. Sometimes, we use
them interchangeably. It is required to estimate action values in any policy gradient
algorithm. When the action values are estimated using temporal-dierence learning
with value function approximation, such a policy gradient algorithm is called actor-
critic. The name \actor-critic" highlights its algorithmic structure that combines the
components of policy update and value update. This structure is also the fundamental
structure used in all reinforcement learning algorithms.
Q: Why is it important to introduce additional baselines to actor-critic methods?
A: Since the policy gradient is invariant to any additional baseline, we can utilize the
baseline to reduce estimation variance. The resulting algorithm is called advantage
actor-critic.
Q: Can importance sampling be used in value-based algorithms other than policy-
based ones?
A: The answer is yes. That is because importance sampling is a general technique
for estimating the expectation of a random variable over one distribution using some
samples drawn from another distribution . The reason why this technique is useful
in reinforcement learning is that the many problems in reinforcement learning are
to estimate expectations. For example, in value-based methods, the action or state
values are dened as expectations. In the policy gradient method, the true gradient is
also an expectation. As a result, importance sampling can be applied in both value-
based and policy-based algorithms. In fact, it has been applied in the value-based
component of Algorithm 10.3.
Q: Why is the deterministic policy gradient method o-policy?
A: The true gradient in the deterministic case does not involve the action random
variable. As a result, when we use samples to approximate the true gradient, it is
not required to sample actions and hence any policy can be used. Therefore, the
deterministic policy gradient method is o-policy .
236

## 第250页

Appendix A
Preliminaries for Probability Theory
Reinforcement learning heavily relies on probability theory. We next summarize some
concepts and results frequently used in this book.
Random variable : The term \variable" indicates that a random variable can take
values from a set of numbers. The term \random" indicates that taking a value must
follow a probability distribution.
A random variable is usually denoted by a capital letter. Its value is usually denoted
by a lowercase letter. For example, Xis a random variable, and xis a value that X
can take.
This book mainly considers the case where a random variable can only take a nite
number of values. A random variable can be a scalar or a vector.
Like normal variables, random variables have normal mathematical operations such
as summation, product, and absolute value. For example, if X;Y are two random
variables, we can calculate X+Y,X+ 1, andXY.
A stochastic sequence is a sequence of random variables.
One scenario we often encounter is collecting a stochastic sampling sequence fxign
i=1
of a random variable X. For example, consider the task of tossing a die ntimes.
Letxibe a random variable representing the value obtained for the ith toss. Then,
fx1;x2;:::;xngis a stochastic process.
It may be confusing to beginners why xiis a random variable instead of a deterministic
value. In fact, if the sampling sequence is f1,6,3,5,...g, then this sequence is not a
stochastic sequence because all the elements are already determined. However, if we
use a variable xito represent the values that can possibly be sampled, it is a random
variable since xican take any value in f1;:::; 6g. Although xiis a lowercase letter, it
still represents a random variable.
Probability : The notation p(X=x) orpX(x) describes the probability of the random
variableXtaking the value x. When the context is clear, p(X=x) is often written
asp(x) for short.
237

## 第251页

Joint probability : The notation p(X=x;Y =y) orp(x;y) describes the probability
of the random variable Xtaking the value xandYtaking the value y. One useful
identity is as follows:X
yp(x;y) =p(x):
Conditional probability : The notation p(X=xjA=a) describes the probability of the
random variable Xtaking the value xgiven that the random variable Ahas already
taken the value a. We often write p(X=xjA=a) asp(xja) for short.
It holds that
p(x;a) =p(xja)p(a)
and
p(xja) =p(x;a)
p(a):
Sincep(x) =P
ap(x;a), we have
p(x) =X
ap(x;a) =X
ap(xja)p(a);
which is called the law of total probability .
Independence : Two random variables are independent if the sampling value of one
random variable does not aect the other. Mathematically, XandYare independent
if
p(x;y) =p(x)p(y):
Sincep(x;y) =p(xjy)p(y), the above equation implies
p(xjy) =p(x):
Conditional independence: LetX;A;B be three random variables. Xis said to be
conditionally independent of AgivenBif
p(X=xjA=a;B=b) =p(X=xjB=b):
In the context of reinforcement learning, consider three consecutive states: st;st+1;st+2.
Since they are obtained consecutively, st+2is dependent on st+1and alsost. However,
ifst+1is already given, then st+2is conditionally independent of st. That is
p(st+2jst+1;st) =p(st+2jst+1):
This is also the memoryless property of Markov processes.
Law of total probability : The law of total probability was already mentioned when we
238

## 第252页

introduced the concept of conditional probability. Due to its importance, we list it
again below:
p(x) =X
yp(x;y)
and
p(xja) =X
yp(x;yja):
Chain rule of conditional probability and joint probability. By the denition of con-
ditional probability, we have
p(a;b) =p(ajb)p(b):
This can be extended to
p(a;b;c ) =p(ajb;c)p(b;c) =p(ajb;c)p(bjc)p(c);
and hence p(a;b;c )=p(c) =p(a;bjc) =p(ajb;c)p(bjc). The fact that p(a;bjc) =
p(ajb;c)p(bjc) implies the following property:
p(xja) =X
bp(x;bja) =X
bp(xjb;a)p(bja):
Expectation/expected value/mean : Suppose that Xis a random variable and the prob-
ability of taking the value xisp(x). The expectation, expected value, or mean of X
is dened as
E[X] =X
xp(x)x:
The linearity property of expectation is
E[X+Y] =E[X] +E[Y];
E[aX] =aE[X]:
The second equation above can be trivially proven by denition. The rst equation
is proven below:
E[X+Y] =X
xX
y(x+y)p(X=x;Y =y)
=X
xxX
yp(x;y) +X
yyX
xp(x;y)
=X
xxp(x) +X
yyp(y)
=E[X] +E[Y]:
239

## 第253页

Due to the linearity of expectation, we have the following useful fact:
E"X
iaiXi#
=X
iaiE[Xi]:
Similarly, it can be proven that
E[AX] =AE[X];
whereA2Rnnis a deterministic matrix and X2Rnis a random vector.
Conditional expectation : The denition of conditional expectation is
E[XjA=a] =X
xxp(xja):
Similar to the law of total probability, we have the law of total expectation :
E[X] =X
aE[XjA=a]p(a):
The proof is as follows. By the denition of expectation, it holds that
X
aE[XjA=a]p(a) =X
a"X
xp(xja)x#
p(a)
=X
xX
ap(xja)p(a)x
=X
x"X
ap(xja)p(a)#
x
=X
xp(x)x
=E[X]:
The law of total expectation is frequently used in reinforcement learning.
Similarly, conditional expectation satises
E[XjA=a] =X
bE[XjA=a;B=b]p(bja):
This equation is useful in the derivation of the Bellman equation. A hint of its proof
is the chain rule: p(xja;b)p(bja) =p(x;bja).
Finally, it is worth noting that E[XjA=a] is dierent from E[XjA]. The former is
a value, whereas the latter is a random variable. In fact, E[XjA] is a function of the
random variable A. We need rigorous probability theory to dene E[XjA].
240

## 第254页

Gradient of expectation : Letf(X;) be a scalar function of a random variable Xand
a deterministic parameter vector . Then,
rE[f(X;)] =E[rf(X;)]:
Proof: Since E[f(X;)] =P
xf(x;)p(x), we haverE[f(X;)] =rP
xf(x;)p(x) =P
xrf(x;)p(x) =E[rf(X;)].
Variance, covariance, covariance matrix : For a single random variable X, itsvariance
is dened as var( X) =E[(X x)2], where x=E[X]. For two random variables
X;Y , their covariance is dened as cov( X;Y ) =E[(X x)(Y y)]. For a random
vectorX= [X1;:::;Xn]T, the covariance matrix of Xis dened as var( X):=  =
E[(X x)(X x)T]2Rnn. Theijth entry of  is [] ij=E[[X x]i[X x]j] =E[(Xi 
xi)(Xj xj)] = cov(Xi;Xj). One trivial property is var( a) = 0 ifais deterministic.
Moreover, it can be veried that var( AX+a) = var(AX) =Avar(X)AT=AAT.
Some useful facts are summarized below.
- Fact: E[(X x)(Y y)] =E[XY] xy=E[XY] E[X]E[Y].
Proof: E[(X x)(Y y)] =E[XY Xy xY+xy] =E[XY] E[X]y xE[Y]+xy=
E[XY] E[X]E[Y] E[X]E[Y] +E[X]E[Y] =E[XY] E[X]E[Y].
- Fact: E[XY] =E[X]E[Y] ifX;Y are independent.
Proof: E[XY] =P
xP
yp(x;y)xy=P
xP
yp(x)p(y)xy=P
xp(x)xP
yp(y)y=
E[X]E[Y].
- Fact: cov( X;Y ) = 0 ifX;Y are independent.
Proof: When X;Y are independent, cov( X;Y ) =E[XY] E[X]E[Y] =E[X]E[Y] 
E[X]E[Y] = 0.
241

## 第255页

242

## 第256页

Appendix B
Measure-Theoretic Probability
Theory
We now brie
y introduce measure-theoretic probability theory, which is also called rig-
orous probability theory. We only present basic notions and results. Comprehensive
introductions can be found in [96{98]. Moreover, measure-theoretic probability theory
requires some basic knowledge of measure theory, which is not covered here. Interested
readers may refer to [99].
The reader may wonder if it is necessary to understand measure-theoretic probability
theory before studying reinforcement learning. The answer is yes if the reader is interested
in rigorously analyzing the convergence of stochastic sequences. For example, we often
encounter the notion of almost sure convergence in Chapter 6 and Chapter 7. This notion
is taken from measure-theoretic probability theory. If the reader is not interested in the
convergence of stochastic sequences, it is okay to skip this part.
Probability triples
Aprobability triple is fundamental for establishing measure-theoretic probability theory.
It is also called a probability space or probability measure space. A probability triple
consists of three ingredients.

: This is a set called the sample space (or outcome space). Any element (or point)
in 
, denoted as !, is called an outcome . This set contains all the possible outcomes
of a random sampling process.
Example: When playing a game of dice, we have six possible outcomes f1;2;3;4;5;6g.
Hence, 
 =f1;2;3;4;5;6g.
 F : This is a set called the event space . In particular, it is a -algebra (or -eld) of

. The denition of a -algebra is given in Box B.1. An element in F, denoted as
A, is called an event . An elementary event refers to a single outcome in the sample
space. An event may be an elementary event or a combination of multiple elementary
events.
243

## 第257页

Example: Consider the game of dice. An example of an elementary event is \the num-
ber you get is i", wherei2f1;:::; 6g. An example of a nonelementary event is \the
number you get is greater than 3". We care about such an event in practice because,
for example, we can win the game if this event occurs. This event is mathematically
expressed as A=f!2
 :! > 3g. Since 
 =f1;2;3;4;5;6gin this case, we have
A=f4;5;6g.
P: This is a probability measure, which is a mapping from Fto [0;1]. AnyA2F is
a set that contains some points in 
. Then, P(A) is the measure of this set.
Example: If A= 
, which contains all !values, then P(A) = 1; ifA=;, then
P(A) = 0. In the game of dice, consider the event \the number you get is greater
than 3". In this case, A=f!2
 :! >3g, and 
 =f1;2;3;4;5;6g. Then, we have
A=f4;5;6gand hence P(A) = 1=2. That is, the probability of us rolling a number
greater than 3 is 1/2.
Box B.1: Denition of a -algebra
Analgebra of 
 is a set of some subsets of 
 that satisfy certain conditions. A
-algebra is a specic and important type of algebra. In particular, denote Fas a
-algebra. Then, it must satisfy the following conditions.
 F contains;and 
;
 F is closed under complements;
 F is closed under countable unions and intersections.
The-algebras of a given 
 are not unique. Fmay contain all the subsets of

, and it may also merely contain some of them as long as it satises the above
three conditions (see the examples below). Moreover, the three conditions are not
independent. For example, if Fcontains 
 and is closed under complements, then it
naturally contains ;. More information can be found in [96{98].
Example: When playing the dice game, we have 
 = f1;2;3;4;5;6g. Then,
F=f
;;;f1;2;3g;f4;5;6ggis a-algebra. The above three conditions can be
easily veried. There are also other -algebras such as f
;;;f1;2;3;4;5g;f6gg.
Moreover, for any 
 with nite elements, the collection of all the subsets of 
 is
a-algebra.
Random variables
Based on the notion of probability triples, we can formally dene random variables. They
are called variables, but they are actually functions that map from 
 to R. In particular,
244

## 第258页

a random variable assigns each outcome in 
 a numerical value, and hence it is a function:
X(!) : 
!R.
Not all mappings from 
 to Rare random variables. The formal denition of a random
variable is as follows. A function X: 
!Ris a random variable if
A=f!2
jX(!)xg2F
for allx2R. This denition indicates that Xis a random variable only if X(!)xis
an event inF. More information can be found in [96, Section 3.1].
Expectation of random variables
The denition of the expectation of general random variables is sophisticated. Here, we
only consider the special yet important case of simple random variables. In particular,
a random variable is simple ifX(!) only takes a nite number of values. Let Xbe the
set of all the possible values that Xcan take. A simple random variable is a function:
X(w) : 
!X . It can be dened in a closed form as
X(!):=X
x2Xx 1Ax(!);
where
Ax=f!2
jX(!) =xg:=X 1(x)
and
1Ax(!):=(
1; !2Ax;
0;otherwise:(B.1)
Here, 1Ax(!) is an indicator function 1Ax(!) : 
!f0;1g. If!is mapped to x, the
indicator function equals one; otherwise, it equals zero. It is possible that multiple !'s
in 
 map to the same value in X, but a single !cannot be mapped to multiple values in
X.
With the above preparation, the expectation of a simple random variable is dened
as
E[X]:=X
x2XxP(Ax); (B.2)
where
Ax=f!2
jX(!) =xg:
The denition in (B.2) is similar to but more formal than the denition of expectation
in the nonmeasure-theoretic case: E[X] =P
x2Xxp(x).
As a demonstrative example, we next calculate the expectation of the indicator func-
245

## 第259页

tion in (B.1). It is notable that the indicator function is also a random variable that
maps 
 tof0;1g[96, Proposition 3.1.5]. As a result, we can calculate its expectation. In
particular, consider the indicator function 1AwhereAdenotes any event. We have
E[ 1A] =P(A):
To prove that, we have
E[ 1A] =X
z2f0;1gzP( 1A=z)
= 0P( 1A= 0) + 1P( 1A= 1)
=P( 1A= 1)
=P(A):
More properties of indicator functions can be found in [100, Chapter 24].
Conditional expectation as a random variable
While the expectation in (B.2) maps random variables to a specic value, we next intro-
duce a conditional expectation that maps random variables to another random variable.
Suppose that X;Y;Z are all random variables. Consider three cases. First, a condi-
tional expectation like E[XjY= 2] or E[XjY= 5] is specic number . Second, E[XjY=y],
whereyis a variable, is a function ofy. Third, E[XjY], whereYis a random variable,
is a function of Yand hence also a random variable . Since E[XjY] is also a random
variable, we can calculate, for example, its expectation.
We next examine the third case closely since it frequently emerges in the convergence
analyses of stochastic sequences. The rigorous denition is not covered here and can be
found in [96, Chapter 13]. We merely present some useful properties [101].
Lemma B.1 (Basic properties) .LetX;Y;Z be random variables. The following proper-
ties hold.
(a)E[ajY] =a, whereais a given number.
(b)E[aX+bZjY] =aE[XjY] +bE[ZjY].
(c)E[XjY] =E[X]ifX;Y are independent.
(d)E[Xf(Y)jY] =f(Y)E[XjY].
(e)E[f(Y)jY] =f(Y).
(f)E[XjY;f(Y)] =E[XjY].
(g) IfX0, then E[XjY]0.
(h) IfXZ, then E[XjY]E[ZjY].
246

## 第260页

Proof. We only prove some properties. The others can be proven similarly.
To prove E[ajY] =aas in (a), we can show that E[ajY=y] =ais valid for any y
thatYcan possibly take. This is clearly true, and the proof is complete.
To prove the property in (d), we can show that E[Xf(Y)jY=y] =f(Y=y)E[XjY=
y] for anyy. This is valid because E[Xf(Y)jY=y] =P
xxf(y)p(xjy) =f(y)P
xxp(xjy) =
f(y)E[XjY=y].
Since E[XjY] is a random variable, we can calculate its expectation. The related
properties are presented below. These properties are useful for analyzing the convergence
of stochastic sequences.
Lemma B.2. LetX;Y;Z be random variables. The following properties hold.
(a)E
E[XjY]
=E[X].
(b)E
E[XjY;Z]
=E[X].
(c)E
E[XjY]jY
=E[XjY].
Proof. To prove the property in (a), we need to show that E
E[XjY=y]
=E[X] for
anyythatYcan possibly take. To that end, considering that E[XjY] is a function of Y,
we denote it as f(Y) =E[XjY]. Then,
E
E[XjY]
=E
f(Y)
=X
yf(Y=y)p(y)
=X
yE[XjY=y]p(y)
=X
y X
xxp(xjy)!
p(y)
=X
xxX
yp(xjy)p(y)
=X
xxX
yp(x;y)
=X
xxp(x)
=E[X]:
The proof of the property in (b) is similar. In particular, we have
E
E[XjY;Z]
=X
y;zE[Xjy;z]p(y;z) =X
y;zX
xxp(xjy;z)p(y;z) =X
xxp(x) =E[X]:
The proof of the property in (c) follows immediately from property (e) in Lemma B.1.
That is because E[XjY] is a function of Y. We denote this function as f(Y). It then
follows that E[E[XjY]jY] =E[f(Y)jY] =f(Y) =E[XjY].
247

## 第261页

Denitions of stochastic convergence
One main reason why we care about measure-theoretic probability theory is that it can
rigorously describe the convergence properties of stochastic sequences.
Consider the stochastic sequence fXkg:=fX1;X2;:::;Xk;:::g. Each element in this
sequence is a random variable dened on a triple (
 ;F;P). When we sayfXkgconverges
to a random variable X, we should be careful since there are dierent types of convergence
as shown below.
Sure convergence:
Denition:fXkgconverges surely (oreverywhere orpointwise ) toXif
lim
k!1Xk(!) =X(!);for all!2
:
It means that lim k!1Xk(!) =X(!) is valid for allpoints in 
. This denition can
be equivalently stated as
A= 
 where A=n
!2
 : lim
k!1Xk(!) =X(!)o
:
Almost sure convergence:
Denition:fXkgconverges almost surely (oralmost everywhere orwith probability 1
orw.p.1 ) toXif
P(A) = 1 where A=n
!2
 : lim
k!1Xk(!) =X(!)o
: (B.3)
It means that lim k!1Xk(!) =X(!) is valid for almost all points in 
. The points,
for which this limit is invalid, form a set of zero measure. For the sake of simplicity,
(B.3) is often written as
P
lim
k!1Xk=X
= 1:
Almost sure convergence can be denoted as Xka:s:  !X:
Convergence in probability:
Denition:fXkgconverges in probability toXif for any>0,
lim
k!1P(Ak) = 0 where Ak=f!2
 :jXk(!) X(!)j>g: (B.4)
For simplicity, (B.4) can be written as
lim
k!1P(jXk Xj>) = 0:
248

## 第262页

The dierence between convergence in probability and (almost) sure convergence is
as follows. Both sure convergence and almost sure convergence rst evaluate the
convergence of every point in 
 and then check the measure of these points that
converge. By contrast, convergence in probability rst checks the points that satisfy
jXk Xj>and then evaluates if the measure will converge to zero as k!1 .
Convergence in mean:
Denition:fXkgconverges in ther-th mean (orin theLrnorm ) toXif
lim
k!1E[jXk Xjr] = 0:
The most frequently used cases are r= 1 andr= 2. It is worth mentioning that
convergence in mean is not equivalent to lim k!1E[Xk X] = 0 or lim k!1E[Xk] =
E[X], which indicates that E[Xk] converges but the variance may not.
Convergence in distribution:
Denition: The cumulative distribution function ofXkis dened as P(Xka) where
a2R. Then,fXkgconverges to Xin distribution if the cumulative distribution
function converges:
lim
k!1P(Xka) =P(Xa);for alla2R:
A compact expression is
lim
k!1P(Ak) =P(A);
where
Ak:=f!2
 :Xk(!)ag; A:=f!2
 :X(!)ag:
The relationships between the above types of convergence are given below:
almost sure convergence )convergence in probability )convergence in distribution
convergence in mean )convergence in probability )convergence in distribution
Almost sure convergence and convergence in mean do not imply each other. More infor-
mation can be found in [102].
249

## 第263页

250

## 第264页

Appendix C
Convergence of Sequences
We next introduce some results about the convergence of deterministic and stochastic se-
quences. These results are useful for analyzing the convergence of reinforcement learning
algorithms such as those in Chapters 6 and 7.
We rst consider deterministic sequences and then stochastic sequences.
C.1 Convergence of deterministic sequences
Convergence of monotonic sequences
Consider a sequence fxkg:=fx1;x2;:::;xk;:::gwherexk2R. Suppose that this se-
quence is deterministic in the sense that xkis not a random variable.
One of the most well-known convergence results is that a nonincreasing sequence with
a lower bound converges. The following is a formal statement of this result.
Theorem C.1 (Convergence of monotonic sequences) .If the sequencefxkgis nonin-
creasing and bounded from below:
Nonincreasing: xk+1xkfor allk;
Lower bound: xkfor allk;
thenxkconverges to a limit, which is the inmum of fxkg, ask!1 .
Similarly, iffxkgisnondecreasing and bounded from above, then the sequence is
convergent.
Convergence of nonmonotonic sequences
We next analyze the convergence of nonmonotonic sequences.
251

## 第265页

C.1. Convergence of deterministic sequences
To analyze the convergence of nonmonotonic sequences, we introduce the following
useful operator [103]. For any z2R, dene
z+:=(
z;ifz0;
0;ifz <0;
z :=(
z;ifz0;
0;ifz >0:
It is obvious that z+0 andz 0 for anyz. Moreover, it holds that
z=z++z 
for allz2R.
To analyze the convergence of fxkg, we rewrite xkas
xk=xk xk 1+xk 1 xk 2+ x2+x2 x1+x1
=k 1X
i=1(xi+1 xi) +x1
:=Sk+x1; (C.1)
whereSk:=Pk 1
i=1(xi+1 xi). Note that Skcan be decomposed as
Sk=k 1X
i=1(xi+1 xi) =S+
k+S 
k;
where
S+
k=k 1X
i=1(xi+1 xi)+0; S 
k=k 1X
i=1(xi+1 xi) 0:
Some useful properties of S+
kandS 
kare given below.
 fS+
k0gis a nondecreasing sequence since S+
k+1S+
kfor allk.
 fS 
k0gis a nonincreasing sequence since S 
k+1S 
kfor allk.
IfS+
kis bounded from above, then S 
kis bounded from below. This is because
S 
k S+
k x1due to the fact that S 
k+S+
k+x1=xk0.
With the above preparation, we can show the following result.
Theorem C.2 (Convergence of nonmonotonic sequences) .For any nonnegative sequence
252

## 第266页

C.1. Convergence of deterministic sequences
fxk0g, if
1X
k=1(xk+1 xk)+<1; (C.2)
thenfxkgconverges as k!1 .
Proof. First, the conditionP1
k=1(xk+1 xk)+<1indicates that S+
k=Pk 1
i=1(xi+1 
xi)+is bounded from above for all k. SincefS+
kgis nondecreasing, the convergence
offS+
kgimmediately follows from Theorem C.1. Suppose that S+
kconverges to S+
.
Second, the boundedness of S+
kimplies that S 
kis bounded from below since
S 
k S+
k x1. SincefS 
kgis nonincreasing, the convergence of fS 
kgimmediately
follows from Theorem C.1. Suppose that S 
kconverges to S 
.
Finally, since xk=S+
k+S 
k+x1, as shown in (C.1), the convergence of S+
kand
S 
kimplies thatfxkgconverges to S+
+S 
+x1.
Theorem C.2 is more general than Theorem C.1 because it allows xkto increase as
long as the increase is damped as in (C.2). In the monotonic case, Theorem C.2 still
applies. In particular, if xk+1xk, thenP1
k=1(xk+1 xk)+= 0. In this case, (C.2) is
still satised and the convergence follows.
We next consider a special yet importance case. Suppose that fxk0gis a nonneg-
ative sequence satisfying
xk+1xk+k:
Whenk= 0, we have xk+1xk, meaning that the sequence is monotonic. When k0,
the sequence is notmonotonic because xk+1may be greater than xk. Nevertheless, we can
still ensure the convergence of the sequence under some mild conditions. The following
result is an immediate corollary of Theorem C.2.
Corollary C.1. For any nonnegative sequence fxk0g, if
xk+1xk+k
andfk0gsatises
1X
k=1k<1;
thenfxk0gconverges.
253

## 第267页

C.2. Convergence of stochastic sequences
Proof. Sincexk+1xk+k, we have (xk+1 xk)+kfor allk. Then, we have
1X
k=1(xk+1 xk)+1X
k=1k<1:
As a result, (C.2) is satised and the convergence follows from Theorem C.2.
C.2 Convergence of stochastic sequences
We now consider stochastic sequences. While various denitions of stochastic sequences
have been given in Appendix B, how to determine the convergence of a given stochastic
sequence has not yet been discussed. We next present an important class of stochastic
sequences called martingales . If a sequence can be classied as a martingale (or one of
its variants), then the convergence of the sequence immediately follows.
Convergence of martingale sequences
Denition: A stochastic sequence fXkg1
k=1is called a martingale ifE[jXkj]<1and
E[Xk+1jX1;:::;Xk] =Xk (C.3)
almost surely for all k.
Here,E[Xk+1jX1;:::;Xk] is a random variable rather than a deterministic value. The
term \almost surely" in the second condition is due to the denition of such expecta-
tions. In addition, E[Xk+1jX1;:::;Xk] is often written as E[Xk+1jHk] for short where
Hk=fX1;:::;Xkgrepresents the \history" of the sequence. Hkhas a specic name
called a ltration . More information can be found in [96, Chapter 14] and [104].
Example: An example that can demonstrate martingales is random walk , which is a
stochastic process describing the position of a point that moves randomly. Specically,
letXkdenote the position of the point at time step k. Starting from Xk, the expecta-
tion of the next position Xk+1equalsXkif the mean of the one-step displacement is
zero. In this case, we have E[Xk+1jX1;:::;Xk] =Xkand hencefXkgis a martingale.
A basic property of martingales is that
E[Xk+1] =E[Xk]
for allkand hence
E[Xk] =E[Xk 1] ==E[X2] =E[X1]:
254

## 第268页

C.2. Convergence of stochastic sequences
This result can be obtained by calculating the expectation on both sides of (C.3)
based on property (b) in Lemma B.2.
While the expectation of a martingale is constant, we next extend martingales to
submartingales and supermartingales, whose expectations vary monotonically.
Denition: A stochastic sequence fXkgis called a submartingale if it satises E[jXkj]<
1and
E[Xk+1jX1;:::;Xk]Xk (C.4)
for allk.
Taking the expectation on both sides of (C.4) yields E[Xk+1]E[Xk]. In particular,
the left-hand side leads to E[E[Xk+1jX1;:::;Xk]] =E[Xk+1] due to property (b) in
Lemma B.2. By induction, we have
E[Xk]E[Xk 1] E[X2]E[X1]:
Therefore, the expectation of a submartingale is nondecreasing.
It may be worth mentioning that, for two random variables XandY,XYmeans
X(!)Y(!) for all!2
. It does not mean the maximum of Xis less than the
minimum of Y.
Denition: A stochastic sequence fXkgis called a supermartingale if it satises
E[jXkj]<1and
E[Xk+1jX1;:::;Xk]Xk (C.5)
for allk.
Taking expectation on both sides of (C.5) gives E[Xk+1]E[Xk]. By induction, we
have
E[Xk]E[Xk 1] E[X2]E[X1]:
Therefore, the expectation of a supmartingale is nonincreasing.
The names \submartingale" and \supmartingale" are standard, but it may not be easy
for beginners to distinguish them. Some tricks can be employed to do so. For example,
since \supermartingale" has a letter \p" that points down, its expectation decreases;
since submartingale has a letter \b" that points up, its expectation increases [104].
A supermartingale or submartingale is comparable to a deterministic monotonic se-
quence. While the convergence result for monotonic sequences has been given in Theo-
rem C.1, we provide a similar convergence result for martingales as follows.
255

## 第269页

C.2. Convergence of stochastic sequences
Theorem C.3 (Martingale convergence theorem) .IffXkgis a submartingale (or super-
martingale), then there is a nite random variable Xsuch thatXk!Xalmost surely.
The proof is omitted. A comprehensive introduction to martingales can be found in
[96, Chapter 14] and [104].
Convergence of quasimartingale sequences
We next introduce quasimartingales, which can be viewed as a generalization of martin-
gales since their expectations are not monotonic. They are comparable to nonmonotonic
deterministic sequences. The rigorous denition and convergence results of quasimartin-
gales are nontrivial. We merely list some useful results.
The event Akis dened as Ak:=f!2
 :E[Xk+1 XkjHk]0g, whereHk=
fX1;:::;Xkg. Intuitively, Akindicates that Xk+1is greater than Xkin expectation.
Let 1Akbe an indicator function:
1Ak=(
1;E[Xk+1 XkjHk]0;
0;E[Xk+1 XkjHk]<0:
The indicator function has a property that
1 = 1A+ 1Ac
for any event AwhereAcdenotes the complementary event of A. As a result, it holds
for any random variable that
X= 1AX+ 1AcX:
Although quasimartingales do not have monotonic expectations, their convergence is
still ensured under some mild conditions as shown below.
Theorem C.4 (Quasimartingale convergence theorem) .For a nonnegative stochastic
sequencefXk0g, if
1X
k=1E[(Xk+1 Xk) 1Ak]<1;
thenP1
k=1E[(Xk+1 Xk) 1Ac
k]> 1 and there is a nite random variable such that
Xk!Xalmost surely as k!1 .
Theorem C.4 can be viewed as an analogy of Theorem C.2, which is for nonmono-
tonic deterministic sequences. The proof of this theorem can be found in [105, Proposi-
tion 9.5]. Note that Xkhere is required to be nonnegative. As a result, the boundedness
ofP1
k=1E[(Xk+1 Xk) 1Ak] implies the boundedness ofP1
k=1E[(Xk+1 Xk) 1Ac
k].
256

## 第270页

C.2. Convergence of stochastic sequences
Summary and comparison
We nally summarize and compare the results for deterministic and stochastic sequences.
Deterministic sequences:
- Monotonic sequences: As shown in Theorem C.1, if a sequence is monotonic and
bounded, then it converges.
- Nonmonotonic sequences: As shown in Theorem C.2, given a nonnegative se-
quence, even if it is nonmonotonic, it can still converge as long as its variation is
damped in the sense thatP1
k=1(xk+1 xk)+<1.
Stochastic sequences:
- Supermartingale/submartingale sequences: As shown in Theorem C.3, the expec-
tation of a supermartingale or submartingale is monotonic. If a sequence is a
supermartingale or submartingale, then the sequence converges almost surely.
- Quasimartingale sequences: As shown in Theorem C.4, even if a sequence's expec-
tation is nonmonotonic, it can still converge as long as its variation is damped in
the sense thatP1
k=1E[(Xk+1 Xk)1E[Xk+1 XkjHk]>0]<1.
The above properties are summarized in Table C.1.
Variants of martingales Monotonicity of E[Xk]
Martingale Constant: E[Xk+1] =E[Xk]
Submartingale Increasing: E[Xk+1]E[Xk]
Supermartingale Decreasing: E[Xk+1]E[Xk]
Quasimartingale Non-monotonic
Table C.1: Summary of the monotonicity of dierent variants of martingales.
257

## 第271页

C.2. Convergence of stochastic sequences
258

## 第272页

Appendix D
Preliminaries for Gradient Descent
We next present some preliminaries for the gradient descent method, which is one of the
most frequently used optimization methods. The gradient descent method is also the
foundation for the stochastic gradient descent method introduced in Chapter 6.
Convexity
Denitions:
- Convex set: Suppose that Dis a subset of Rn. This set is convex ifz:=cx+ (1 
c)y2D for anyx;y2D and anyc2[0;1].
- Convex function: Suppose f:D!RwhereDis convex. Then, the function f(x)
isconvex if
f(cx+ (1 c)y)cf(x) + (1 c)f(y)
for anyx;y2D andc2[0;1].
Convex conditions:
- First-order condition: Consider a function f:D!RwhereDis convex. Then, f
is convex if [106, 3.1.3]
f(y) f(x)rf(x)T(y x);for allx;y2D: (D.1)
Whenxis a scalar,rf(x) represents the slope of the tangent line of f(x) atx.
The geometric interpretation of (D.1) is that the point ( y;f(y)) is always located
above the tangent line.
- Second-order condition: Consider a function f:D!RwhereDis convex. Then,
fis convex if
r2f(x)0;for allx2D;
wherer2f(x) is the Hessian matrix.
259

## 第273页

Degree of convexity:
Given a convex function, it is often of interest how strong its convexity is. The Hessian
matrix is a useful tool for describing the degree of convexity. If r2f(x) is close to rank
deciency at a point, then the function is 
ataround that point and hence weakly
convex . Otherwise, if the minimum singular value of r2f(x) is positive and large,
the function is curly around that point and hence strongly convex . The degree of
convexity in
uences the step size selection in gradient descent algorithms.
The lower and upper bounds of r2f(x) play an important role in characterizing the
function convexity.
- Lower bound of r2f(x): A function is called strongly convex orstrictly convex if
r2f(x)`In, where`>0 for allx.
- Upper bound of r2f(x): Ifr2f(x) is bounded from above so that r2f(x)LIn,
then the change in the rst-order derivative rf(x) cannot be arbitrarily fast;
equivalently, the function cannot be arbitrarily convex at a point.
The upper bound can be implied by a Lipschitz condition of rf(x), as shown
below.
Lemma D.1. Suppose that fis a convex function. If rf(x)is Lipschitz contin-
uous with a constant Lso that
krf(x) rf(y)kLkx yk;for allx;y;
thenr2f(x)LInfor allx. Here,kk denotes the Euclidean norm.
Gradient descent algorithms
Consider the following optimization problem:
min
xf(x)
wherex2D Rnandf:D!R. The gradient descent algorithm is
xk+1=xk krf(xk); k = 0;1;2;::: (D.2)
wherekis a positive coecient that may be xed or time-varying. Here, kis called
thestep size orlearning rate . Some remarks about (D.2) are given below.
Direction of change: rf(xk) is a vector that points in the direction along which f(xk)
increases the fastest. Hence, the term  krf(xk) changesxkin the direction along
whichf(xk)decreases the fastest.
Magnitude of change: The magnitude of the change  krf(xk) is jointly determined
by the step size kand the magnitude of rf(xk).
260

## 第274页

- Magnitude ofrf(xk):
Whenxkis close to the optimum xwhererf(x) = 0, the magnitude krf(xk)k
is small. In this case, the update process of xkis slow, which is reasonable because
we do not want to update xtoo aggressively and miss the optimum.
Whenxkis far from the optimum, the magnitude of rf(xk) may be large, and
hence the update process of xkis fast. This is also reasonable because we hope
that the estimate can approach the optimum as quickly as possible.
- Step size k:
Ifkis small, the magnitude of  krf(xk) is small, and hence the convergence
process is slow. If kis too large, the update process of xkis aggressive, which
leads to either fast convergence or divergence.
How to select k? The selection of kshould depend on the degree of convexity
off(xk). If the function is curly around the optimum (the degree of convexity is
strong), then the step size kshould be small to guarantee convergence. If the
function is 
ataround the optimum (the degree of convexity is weak), then the
step size could be large so that xkcan quickly approach the optimum. The above
intuition will be veried in the following convergence analysis.
Convergence analysis
We next present a proof of the convergence of the gradient descent algorithm in (D.2).
That is to show xkconverges to the optimum xwhererf(x) = 0. First of all, we make
some assumptions.
Assumption 1: f(x) is strongly convex such that
r2f(x)`I;
where`>0.
Assumption 2:rf(x) is Lipschitz continuous with a constant L. This assumption
implies the following inequality according to Lemma D.1:
r2f(x)LIn:
The convergence proof is given below.
Proof. For anyxk+1andxk, it follows from [106, Section 9.1.2] that
f(xk+1) =f(xk) +rf(xk)T(xk+1 xk) +1
2(xk+1 xk)Tr2f(zk)(xk+1 xk);(D.3)
261

## 第275页

wherezkis a convex combination of xkandxk+1. Since it is assumed that r2f(zk)LIn,
we havekr2f(zk)kL. (D.3) implies
f(xk+1)f(xk) +rf(xk)T(xk+1 xk) +1
2kr2f(zk)kkxk+1 xkk2
f(xk) +rf(xk)T(xk+1 xk) +L
2kxk+1 xkk2:
Substituting xk+1=xk krf(xk) into the above inequality yields
f(xk+1)f(xk) +rf(xk)T( krf(xk)) +L
2kkrf(xk)k2
=f(xk) kkrf(xk)k2+2
kL
2krf(xk)k2
=f(xk) k
1 kL
2
|{z}
kkrf(xk)k2: (D.4)
We next show that if we select
0<k<2
L; (D.5)
then the sequence ff(xk)g1
k=1converges to f(x) whererf(x) = 0. First, (D.5) implies
thatk>0. Then, (D.4) implies that f(xk+1)f(xk). Therefore,ff(xk)gis a nonin-
creasing sequence. Second, since f(xk) is always bounded from below by f(x), we know
thatff(xk)gconverges as k!1 according to the monotone convergence theorem in
Theorem C.1. Suppose that the limit of the sequence is f. Then, taking the limit on
both sides of (D.4) gives
lim
k!1f(xk+1)lim
k!1f(xk) lim
k!1kkrf(xk)k2
,ff lim
k!1kkrf(xk)k2
,0  lim
k!1kkrf(xk)k2:
Sincekkrf(xk)k20, the above inequality implies that lim k!1kkrf(xk)k2= 0. As
a result,xconverges to xwhererf(x) = 0. The proof is complete. The above proof is
inspired by [107].
The inequality in (D.5) provides valuable insights into how kshould be selected. If
the function is 
at ( Lis small), the step size can be large; otherwise, if the function
is strongly convex ( Lis large), then the step size must be suciently small to ensure
convergence. There are also many other ways to prove the convergence such as the
contraction mapping theorem [108, Lemma 3]. A comprehensive introduction to convex
optimization can be found in [106].
262

## 第276页

Bibliography
[1] M. Pinsky and S. Karlin, An introduction to stochastic modeling (3rd Edition) .
Academic Press, 1998.
[2] M. L. Puterman, Markov decision processes: Discrete stochastic dynamic program-
ming . John Wiley & Sons, 2014.
[3] R. S. Sutton and A. G. Barto, Reinforcement learning: An introduction (2nd Edi-
tion) . MIT Press, 2018.
[4] R. A. Horn and C. R. Johnson, Matrix analysis . Cambridge University Press, 2012.
[5] D. P. Bertsekas and J. N. Tsitsiklis, Neuro-dynamic programming . Athena Scientic,
1996.
[6] H. K. Khalil, Nonlinear systems (3rd Edition) . Patience Hall, 2002.
[7] G. Strang, Calculus . Wellesley-Cambridge Press, 1991.
[8] A. Besenyei, \A brief history of the mean value theorem," 2012. Lecture notes.
[9] A. Y. Ng, D. Harada, and S. Russell, \Policy invariance under reward transforma-
tions: Theory and application to reward shaping," in International Conference on
Machine Learning , vol. 99, pp. 278{287, 1999.
[10] R. E. Bellman, Dynamic programming . Princeton University Press, 2010.
[11] R. E. Bellman and S. E. Dreyfus, Applied dynamic programming . Princeton Uni-
versity Press, 2015.
[12] J. Bibby, \Axiomatisations of the average and a further generalisation of monotonic
sequences," Glasgow Mathematical Journal , vol. 15, no. 1, pp. 63{65, 1974.
[13] A. S. Polydoros and L. Nalpantidis, \Survey of model-based reinforcement learning:
Applications on robotics," Journal of Intelligent & Robotic Systems , vol. 86, no. 2,
pp. 153{173, 2017.
263

## 第277页

Bibliography
[14] T. M. Moerland, J. Broekens, A. Plaat, and C. M. Jonker, \Model-based reinforce-
ment learning: A survey," Foundations and Trends in Machine Learning , vol. 16,
no. 1, pp. 1{118, 2023.
[15] F.-M. Luo, T. Xu, H. Lai, X.-H. Chen, W. Zhang, and Y. Yu, \A survey on model-
based reinforcement learning," arXiv:2206.09328 , 2022.
[16] X. Wang, Z. Zhang, and W. Zhang, \Model-based multi-agent reinforcement learn-
ing: Recent progress and prospects," arXiv:2203.10603 , 2022.
[17] M. Riedmiller, R. Hafner, T. Lampe, M. Neunert, J. Degrave, T. Wiele, V. Mnih,
N. Heess, and J. T. Springenberg, \Learning by playing solving sparse reward tasks
from scratch," in International Conference on Machine Learning , pp. 4344{4353,
2018.
[18] J. Ibarz, J. Tan, C. Finn, M. Kalakrishnan, P. Pastor, and S. Levine, \How to
train your robot with deep reinforcement learning: Lessons we have learned," The
International Journal of Robotics Research , vol. 40, no. 4-5, pp. 698{721, 2021.
[19] S. Narvekar, B. Peng, M. Leonetti, J. Sinapov, M. E. Taylor, and P. Stone, \Cur-
riculum learning for reinforcement learning domains: A framework and survey,"
The Journal of Machine Learning Research , vol. 21, no. 1, pp. 7382{7431, 2020.
[20] C. Szepesv ari, Algorithms for reinforcement learning . Springer, 2010.
[21] A. Maroti, \RBED: Reward based epsilon decay," arXiv:1910.13701 , 2019.
[22] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare,
A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski, S. Petersen, C. Beattie,
A. Sadik, I. Antonoglou, H. King, D. Kumaran, D. Wierstra, S. Legg, and D. Hass-
abis, \Human-level control through deep reinforcement learning," Nature , vol. 518,
no. 7540, pp. 529{533, 2015.
[23] W. Dabney, G. Ostrovski, and A. Barreto, \Temporally-extended epsilon-greedy
exploration," arXiv:2006.01782 , 2020.
[24] H.-F. Chen, Stochastic approximation and its applications , vol. 64. Springer Science
& Business Media, 2006.
[25] H. Robbins and S. Monro, \A stochastic approximation method," The Annals of
Mathematical Statistics , pp. 400{407, 1951.
[26] J. Venter, \An extension of the Robbins-Monro procedure," The Annals of Mathe-
matical Statistics , vol. 38, no. 1, pp. 181{190, 1967.
264

## 第278页

Bibliography
[27] D. Ruppert, \Ecient estimations from a slowly convergent Robbins-Monro pro-
cess," tech. rep., Cornell University Operations Research and Industrial Engineer-
ing, 1988.
[28] J. Lagarias, \Euler's constant: Euler's work and modern developments," Bulletin
of the American Mathematical Society , vol. 50, no. 4, pp. 527{628, 2013.
[29] J. H. Conway and R. Guy, The book of numbers . Springer Science & Business
Media, 1998.
[30] S. Ghosh, \The Basel problem," arXiv:2010.03953 , 2020.
[31] A. Dvoretzky, \On stochastic approximation," in The Third Berkeley Symposium
on Mathematical Statistics and Probability , 1956.
[32] T. Jaakkola, M. I. Jordan, and S. P. Singh, \On the convergence of stochastic
iterative dynamic programming algorithms," Neural Computation , vol. 6, no. 6,
pp. 1185{1201, 1994.
[33] T. Kailath, A. H. Sayed, and B. Hassibi, Linear estimation . Prentice Hall, 2000.
[34] C. K. Chui and G. Chen, Kalman ltering . Springer, 2017.
[35] G. A. Rummery and M. Niranjan, On-line Q-learning using connectionist systems .
Technical Report, Cambridge University, 1994.
[36] H. Van Seijen, H. Van Hasselt, S. Whiteson, and M. Wiering, \A theoretical and
empirical analysis of Expected Sarsa," in IEEE Symposium on Adaptive Dynamic
Programming and Reinforcement Learning , pp. 177{184, 2009.
[37] M. Ganger, E. Duryea, and W. Hu, \Double Sarsa and double expected Sarsa with
shallow and deep learning," Journal of Data Analysis and Information Processing ,
vol. 4, no. 4, pp. 159{176, 2016.
[38] C. J. C. H. Watkins, Learning from delayed rewards . PhD thesis, King's College,
1989.
[39] C. J. Watkins and P. Dayan, \Q-learning," Machine learning , vol. 8, no. 3-4, p-
p. 279{292, 1992.
[40] T. C. Hesterberg, Advances in importance sampling . PhD Thesis, Stanford Univer-
sity, 1988.
[41] H. Hasselt, \Double Q-learning," Advances in Neural Information Processing Sys-
tems, vol. 23, 2010.
265

## 第279页

Bibliography
[42] H. Van Hasselt, A. Guez, and D. Silver, \Deep reinforcement learning with double
Q-learning," in AAAI Conference on Articial Intelligence , vol. 30, 2016.
[43] C. Dann, G. Neumann, and J. Peters, \Policy evaluation with temporal dierences:
A survey and comparison," Journal of Machine Learning Research , vol. 15, pp. 809{
883, 2014.
[44] J. Clifton and E. Laber, \Q-learning: Theory and applications," Annual Review of
Statistics and Its Application , vol. 7, pp. 279{301, 2020.
[45] B. Jang, M. Kim, G. Harerimana, and J. W. Kim, \Q-learning algorithms: A
comprehensive classication and applications," IEEE Access , vol. 7, pp. 133653{
133667, 2019.
[46] R. S. Sutton, \Learning to predict by the methods of temporal dierences," Machine
Learning , vol. 3, no. 1, pp. 9{44, 1988.
[47] G. Strang, Linear algebra and its applications (4th Edition) . Belmont, CA: Thom-
son, Brooks/Cole, 2006.
[48] C. D. Meyer and I. Stewart, Matrix analysis and applied linear algebra . SIAM,
2023.
[49] M. Pinsky and S. Karlin, An introduction to stochastic modeling . Academic Press,
2010.
[50] M. G. Lagoudakis and R. Parr, \Least-squares policy iteration," The Journal of
Machine Learning Research , vol. 4, pp. 1107{1149, 2003.
[51] R. Munos, \Error bounds for approximate policy iteration," in International Con-
ference on Machine Learning , vol. 3, pp. 560{567, 2003.
[52] A. Geramifard, T. J. Walsh, S. Tellex, G. Chowdhary, N. Roy, and J. P. How,
\A tutorial on linear function approximators for dynamic programming and rein-
forcement learning," Foundations and Trends in Machine Learning , vol. 6, no. 4,
pp. 375{451, 2013.
[53] B. Scherrer, \Should one compute the temporal dierence x point or minimize the
Bellman residual? the unied oblique projection view," in International Conference
on Machine Learning , 2010.
[54] D. P. Bertsekas, Dynamic programming and optimal control: Approximate dynamic
programming (Volume II) . Athena Scientic, 2011.
[55] S. Abramovich, G. Jameson, and G. Sinnamon, \Rening Jensen's inequality,"
Bulletin math ematique de la Soci et e des Sciences Math ematiques de Roumanie ,
pp. 3{14, 2004.
266

## 第280页

Bibliography
[56] S. S. Dragomir, \Some reverses of the Jensen inequality with applications," Bulletin
of the Australian Mathematical Society , vol. 87, no. 2, pp. 177{194, 2013.
[57] S. J. Bradtke and A. G. Barto, \Linear least-squares algorithms for temporal dif-
ference learning," Machine Learning , vol. 22, no. 1, pp. 33{57, 1996.
[58] K. S. Miller, \On the inverse of the sum of matrices," Mathematics Magazine ,
vol. 54, no. 2, pp. 67{72, 1981.
[59] S. A. U. Islam and D. S. Bernstein, \Recursive least squares for real-time imple-
mentation," IEEE Control Systems Magazine , vol. 39, no. 3, pp. 82{85, 2019.
[60] V. Mnih, K. Kavukcuoglu, D. Silver, A. Graves, I. Antonoglou, D. Wierstra, and
M. Riedmiller, \Playing Atari with deep reinforcement learning," arXiv preprint
arXiv:1312.5602 , 2013.
[61] J. Fan, Z. Wang, Y. Xie, and Z. Yang, \A theoretical analysis of deep Q-learning,"
inLearning for Dynamics and Control , pp. 486{489, 2020.
[62] L.-J. Lin, Reinforcement learning for robots using neural networks . 1992. Technical
report.
[63] J. N. Tsitsiklis and B. Van Roy, \An analysis of temporal-dierence learning with
function approximation," IEEE Transactions on Automatic Control , vol. 42, no. 5,
pp. 674{690, 1997.
[64] R. S. Sutton, D. McAllester, S. Singh, and Y. Mansour, \Policy gradient meth-
ods for reinforcement learning with function approximation," Advances in Neural
Information Processing Systems , vol. 12, 1999.
[65] P. Marbach and J. N. Tsitsiklis, \Simulation-based optimization of Markov reward
processes," IEEE Transactions on Automatic Control , vol. 46, no. 2, pp. 191{209,
2001.
[66] J. Baxter and P. L. Bartlett, \Innite-horizon policy-gradient estimation," Journal
of Articial Intelligence Research , vol. 15, pp. 319{350, 2001.
[67] X.-R. Cao, \A basic formula for online policy gradient algorithms," IEEE Trans-
actions on Automatic Control , vol. 50, no. 5, pp. 696{699, 2005.
[68] R. J. Williams, \Simple statistical gradient-following algorithms for connectionist
reinforcement learning," Machine Learning , vol. 8, no. 3, pp. 229{256, 1992.
[69] J. Peters and S. Schaal, \Reinforcement learning of motor skills with policy gradi-
ents," Neural Networks , vol. 21, no. 4, pp. 682{697, 2008.
267

## 第281页

Bibliography
[70] E. Greensmith, P. L. Bartlett, and J. Baxter, \Variance reduction techniques for
gradient estimates in reinforcement learning," Journal of Machine Learning Re-
search , vol. 5, no. 9, 2004.
[71] V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. Lillicrap, T. Harley, D. Silver,
and K. Kavukcuoglu, \Asynchronous methods for deep reinforcement learning," in
International Conference on Machine Learning , pp. 1928{1937, 2016.
[72] M. Babaeizadeh, I. Frosio, S. Tyree, J. Clemons, and J. Kautz, \Reinforce-
ment learning through asynchronous advantage actor-critic on a GPU," arX-
iv:1611.06256 , 2016.
[73] T. Degris, M. White, and R. S. Sutton, \O-policy actor-critic," arXiv:1205.4839 ,
2012.
[74] D. Silver, G. Lever, N. Heess, T. Degris, D. Wierstra, and M. Riedmiller, \De-
terministic policy gradient algorithms," in International Conference on Machine
Learning , pp. 387{395, 2014.
[75] T. P. Lillicrap, J. J. Hunt, A. Pritzel, N. Heess, T. Erez, Y. Tassa, D. Silver,
and D. Wierstra, \Continuous control with deep reinforcement learning," arX-
iv:1509.02971 , 2015.
[76] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, \Soft actor-critic: O-policy maxi-
mum entropy deep reinforcement learning with a stochastic actor," in International
Conference on Machine Learning , pp. 1861{1870, 2018.
[77] T. Haarnoja, A. Zhou, K. Hartikainen, G. Tucker, S. Ha, J. Tan, V. Kumar, H. Zhu,
A. Gupta, and P. Abbeel, \Soft actor-critic algorithms and applications," arX-
iv:1812.05905 , 2018.
[78] J. Schulman, S. Levine, P. Abbeel, M. Jordan, and P. Moritz, \Trust region policy
optimization," in International Conference on Machine Learning , pp. 1889{1897,
2015.
[79] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, \Proximal policy
optimization algorithms," arXiv:1707.06347 , 2017.
[80] S. Fujimoto, H. Hoof, and D. Meger, \Addressing function approximation error in
actor-critic methods," in International Conference on Machine Learning , pp. 1587{
1596, 2018.
[81] J. Foerster, G. Farquhar, T. Afouras, N. Nardelli, and S. Whiteson, \Counterfac-
tual multi-agent policy gradients," in AAAI Conference on Articial Intelligence ,
vol. 32, 2018.
268

## 第282页

Bibliography
[82] R. Lowe, Y. I. Wu, A. Tamar, J. Harb, O. Pieter Abbeel, and I. Mordatch, \Multi-
agent actor-critic for mixed cooperative-competitive environments," Advances in
Neural Information Processing Systems , vol. 30, 2017.
[83] Y. Yang, R. Luo, M. Li, M. Zhou, W. Zhang, and J. Wang, \Mean eld multi-
agent reinforcement learning," in International Conference on Machine Learning ,
pp. 5571{5580, 2018.
[84] O. Vinyals, I. Babuschkin, W. M. Czarnecki, M. Mathieu, A. Dudzik, J. Chung,
D. H. Choi, R. Powell, T. Ewalds, P. Georgiev, et al. , \Grandmaster level in Star-
Craft II using multi-agent reinforcement learning," Nature , vol. 575, no. 7782, p-
p. 350{354, 2019.
[85] Y. Yang and J. Wang, \An overview of multi-agent reinforcement learning from
game theoretical perspective," arXiv:2011.00583 , 2020.
[86] S. Levine and V. Koltun, \Guided policy search," in International Conference on
Machine Learning , pp. 1{9, 2013.
[87] M. Janner, J. Fu, M. Zhang, and S. Levine, \When to trust your model: Model-
based policy optimization," Advances in Neural Information Processing Systems ,
vol. 32, 2019.
[88] M. G. Bellemare, W. Dabney, and R. Munos, \A distributional perspective on re-
inforcement learning," in International Conference on Machine Learning , pp. 449{
458, 2017.
[89] M. G. Bellemare, W. Dabney, and M. Rowland, Distributional Reinforcement
Learning . MIT Press, 2023.
[90] H. Zhang, D. Liu, Y. Luo, and D. Wang, Adaptive dynamic programming for control:
algorithms and stability . Springer Science & Business Media, 2012.
[91] F. L. Lewis, D. Vrabie, and K. G. Vamvoudakis, \Reinforcement learning and
feedback control: Using natural decision methods to design optimal adaptive con-
trollers," IEEE Control Systems Magazine , vol. 32, no. 6, pp. 76{105, 2012.
[92] F. L. Lewis and D. Liu, Reinforcement learning and approximate dynamic program-
ming for feedback control . John Wiley & Sons, 2013.
[93] Z.-P. Jiang, T. Bian, and W. Gao, \Learning-based control: A tutorial and some
recent results," Foundations and Trends in Systems and Control , vol. 8, no. 3,
pp. 176{284, 2020.
[94] S. Meyn, Control systems and reinforcement learning . Cambridge University Press,
2022.
269

## 第283页

Bibliography
[95] S. E. Li, Reinforcement learning for sequential decision and optimal control .
Springer, 2023.
[96] J. S. Rosenthal, First look at rigorous probability theory (2nd Edition) . World
Scientic Publishing Company, 2006.
[97] D. Pollard, A user's guide to measure theoretic probability . Cambridge University
Press, 2002.
[98] P. J. Spreij, \Measure theoretic probability," UvA Course Notes , 2012.
[99] R. G. Bartle, The elements of integration and Lebesgue measure . John Wiley &
Sons, 2014.
[100] M. Taboga, Lectures on probability theory and mathematical statistics (2nd Edition) .
CreateSpace Independent Publishing Platform, 2012.
[101] T. Kennedy, \Theory of probability," 2007. Lecture notes.
[102] A. W. Van der Vaart, Asymptotic statistics . Cambridge University Press, 2000.
[103] L. Bottou, \Online learning and stochastic approximations," Online Learning in
Neural Networks , vol. 17, no. 9, p. 142, 1998.
[104] D. Williams, Probability with martingales . Cambridge University Press, 1991.
[105] M. M etivier, Semimartingales: A course on stochastic processes . Walter de Gruyter,
1982.
[106] S. Boyd, S. P. Boyd, and L. Vandenberghe, Convex optimization . Cambridge Uni-
versity Press, 2004.
[107] S. Bubeck et al. , \Convex optimization: Algorithms and complexity," Foundations
and Trends in Machine Learning , vol. 8, no. 3-4, pp. 231{357, 2015.
[108] A. Jung, \A xed-point of view on gradient methods for big data," Frontiers in
Applied Mathematics and Statistics , vol. 3, p. 18, 2017.
270

## 第284页

Symbols
In this book, a matrix or a random variable is represented by capital letters. A vector, a
scalar, or a sample is represented by a lowercase letter. The mathematical symbols that
are frequently used in this book are listed below.
= equality
 approximation
:= equality by denition
,>,,< elementwise comparison
2 is an element of
kk 2 Euclidean norm of a vector or the corresponding in-
duced matrix norm
kk1 maximum norm of a vector or the corresponding in-
duced matrix norm
ln natural logarithm
R set of real numbers
Rnset ofn-dimensional real vectors
Rnmset of allnm-dimensional real matrices
A0 (A0) matrix Ais positive semidenite (denite)
A0 (A0) matrix Ais negative semidenite (denite)
jxj absolute value of real scalar x
jSj number of elements in set S
rxf(x) gradient of scalar function f(x) with respect to vector
x. It may be written as rf(x) for short.
[A]ij element in the ith row and jth column of matrix A
[x]i ith element of vector x
Xp p is the probability distribution of random variable
X.
p(X=x), Pr(X=x) probability of X=x. They are often written as p(x)
or Pr(x) for short.
p(xjy) conditional probability
EXp[X] expectation or expected value of random variable X.
It is often written as E[X] for short when the distri-
bution ofXis clear.
271

## 第285页

Bibliography
var(X) variance of random variable X
arg maxxf(x) maximizer of function f(x)
1n vector of all ones. It is often written as 1for short
when its dimension is clear.
In nn-dimensional identity matrix. It is often written
asIfor short when its dimensions are clear.
272

## 第286页

Index
-greedy policy, 89
n-step Sarsa, 138
action, 2
action space, 2
action value, 30
illustrative examples, 31
relationship to state value, 30
undiscounted case, 205
actor-critic, 216
advantage actor-critic, 217
deterministic actor-critic, 227
o-policy actor-critic, 221
QAC, 216
advantage actor-critic, 217
advantage function, 220
baseline invariance, 217
optimal baseline, 218
pseudocode, 221
agent, 12
Bellman equation, 20
closed-form solution, 27
elementwise expression, 21
equivalent expressions, 22
expression in action values, 32
illustrative examples, 22
iterative solution, 28
matrix-vector expression, 26
policy evaluation, 27
Bellman error, 173
Bellman expectation equation, 127
Bellman optimality equation, 38contraction property, 44
elementwise expression, 38
matrix-vector expression, 40
optimal policy, 47
optimal state value, 47
solution and properties, 46
bootstrapping, 18
Cauchy sequence, 42
contraction mapping, 41
contraction mapping theorem, 42
deterministic actor-critic, 227
policy gradient theorem, 228
pseudocode, 235
deterministic policy gradient, 235
discount rate, 9
discounted return, 9
Dvoretzky's convergence theorem, 109
environment, 12
episode, 10
episodic tasks, 10
expected Sarsa, 137
experience replay, 183
exploration and exploitation, 92
policy gradient, 212
feature vector, 152
xed point, 41
grid world example, 1
importance sampling, 221
illustrative examples, 223
273

## 第287页

Index
importance weight, 222
law of large numbers, 80
least-squares TD, 177
recursive least squares, 178
Markov decision process, 11
model and dynamics, 11
Markov process, 12
Markov property, 11
mean estimation, 78
incremental manner, 102
metrics for policy gradient
average reward, 195
average value, 193
equivalent expressions, 197
metrics for value function approximation
Bellman error, 173
projected Bellman error, 174
Monte Carlo methods, 78
MC-Greedy, 90
MC Basic, 81
MC Exploring Starts, 86
comparison with TD learning, 129
on-policy, 142
o-policy, 141
o-policy actor-critic, 221
importance sampling, 221
policy gradient theorem, 224
pseudocode, 226
on-policy, 141
online and oine, 130
optimal policy, 37
greedy is optimal, 47
impact of the discount rate, 49
impact of the reward values, 51
optimal state value, 37
Poisson equation, 205
policy, 4
function representation, 192deterministic policy, 5
stochastic policy, 5
tabular representation, 6
policy evaluation
illustrative examples, 17
solving the Bellman equation, 27
policy gradient theorem, 198
deterministic case, 228
o-policy case, 224
policy iteration algorithm, 62
comparison with value iteration, 70
convergence analysis, 64
pseudocode, 66
projected Bellman error, 174
Q-learning (deep Q-learning), 182
experience replay, 183
illustrative examples, 184
main network, 182
pseudocode, 184
replay buer, 183
target network, 182
Q-learning (function representation), 180
Q-learning (tabular representation), 140
illustrative examples, 144
pseudocode, 143
o-policy, 141
QAC, 216
REINFORCE, 210
replay buer, 183
return, 8
reward, 6
Robbins-Monro algorithm, 103
application to mean estimation, 108
convergence analysis, 106
Sarsa (function representation), 179
Sarsa (tabular representation), 133
convergence analysis, 134
on-policy, 141
variant:n-step Sarsa, 138
274

## 第288页

Index
variant: expected Sarsa, 137
algorithm, 133
optimal policy learning, 135
state, 2
state space, 2
state transition, 3
state value, 19
function representation, 152
relationship to action value, 30
undiscounted case, 205
stationary distribution, 157
metrics for policy gradient, 193
metrics for value function approxima-
tion, 156
stochastic gradient descent, 114
application to mean estimation, 116
comparison with batch gradient de-
scent, 119
convergence analysis, 121
convergence pattern, 116
deterministic formulation, 118
TD error, 128
TD target, 128
temporal-dierence methods, 125
n-step Sarsa, 138
Q-learning, 140Sarsa, 133
TD learning of state values, 126
a unied viewpoint, 145
expected Sarsa, 137
value function approximation, 151
trajectory, 8
truncated policy iteration, 70
comparison with value iteration and
policy iteration, 74
pseudocode, 72
value function approximation
Q-learning with function approxima-
tion, 180
Sarsa with function approximation,
179
TD learning of state values, 155
deep Q-learning, 182
function approximators, 162
illustrative examples, 164
least-squares TD, 177
linear function, 155
theoretical analysis, 167
value iteration algorithm, 58
comparison with policy iteration, 70
pseudocode, 60
275

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_Book-Mathematical-Foundation-of-Reinforcement-Learning-main_课程MOC|Book-Mathematical-Foundation-of-Reinforcement-Learning-main MOC]]
