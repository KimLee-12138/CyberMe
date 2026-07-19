---
id: extract-rlmath-5b8a7905
type: extract
status: extracted
course: RLMATH
source:
  - "[[91_Raw-Archive/PDF/RLMATH_2 - Overview of this book.pdf_课件_未知日期_5b8a7905.pdf]]"
source_pages: all
source_hash: "5b8a7905bd39ada5d22d48fc646890783fa7dc38fd9f47b1fc55571d2022b097"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 2 - Overview of this book.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

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

## 第2页

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

## 第3页

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

## 第4页

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

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_Book-Mathematical-Foundation-of-Reinforcement-Learning-main_课程MOC|Book-Mathematical-Foundation-of-Reinforcement-Learning-main MOC]]
