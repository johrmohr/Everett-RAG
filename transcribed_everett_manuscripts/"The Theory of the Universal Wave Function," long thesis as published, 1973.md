# Everett long thesis as published 1973.pdf

The Many-Worlds Interpretation of Quantum Mechanics  

A Fundamental Exposition by HUGH EVERETT, III, with Papers by J. A. WHEELER, B. S. DEWITT, L. N. COOPER and D. VAN VECHTEN, and N. GRAHAM  

Edited by BRYCE S. DEWITT and NEILL GRAHAM  

Princeton Series in Physics  

Princeton University Press Princeton, New Jersey, 1973

---

Copyright © 1973, by Princeton University Press  

All Rights Reserved  

LC Card: 72- 12116  

ISBN: 0- 691- 08126- 3 (hard cover edition)ISBN: 0- 691- 88131- X (paperback edition)  

Library of Congress Cataloguing in Publication data will be found on the last printed page of this book.  

The following papers have been included in this volume with the permission of the copyright owners: "Relative State' Formulation of Quantum Mechanics" by Hugh Everett III, and "Assessment of Everett's 'Relative State' Formulation of Quantum Theory," by John A. Wheeler, copyright July 1957 by The Review of Modern Physics; "Quantum Mechanics and Reality," by Bryce S. DeWitt, copyright September 1970 by Physics Today; "The Many- Universes Interpretation of Quantum Mechanics," by Bryce S. DeWitt, in Proceedings of the International School of Physics "Enrico Fermi" Course IL: Foundations of Quantum Mechanics, copyright 1972 by Academic Press; "On the Interpretation of Measurement within the Quantum Theory," by Leon N. Cooper and Deborah van Vechten, copyright December 1969 by American Journal of Physics. The epigraph is taken from "The Garden of Forking Paths," from Ficciones by Jorge Luis Borges, copyright 1962 by Grove Press, Inc.; translated from the Spanish, copyright 1956 by Emece Editores, SA, Buenos Aires.  

Printed in the United States of America by Princeton University Press

---

## PREFACE  

In 1957, in his Princeton doctoral dissertation, Hugh Everett, III, proposed a new interpretation of quantum mechanics that denies the existence of a separate classical realm and asserts that it makes sense to talk about a state vector for the whole universe. This state vector never collapses, and hence reality as a whole is rigorously deterministic. This reality, which is described jointly by the dynamical variables and the state vector, is not the reality we customarily think of, but is a reality composed of many worlds. By virtue of the temporal development of the dynamical variables the state vector decomposes naturally into orthogonal vectors, reflecting a continual splitting of the universe into a multitude of mutually unobservable but equally real worlds, in each of which every good measurement has yielded a definite result and in most of which the familiar statistical quantum laws hold.  

In addition to his short thesis Everett wrote a much larger exposition of his ideas, which was never published. The present volume contains both of these works, together with a handful of papers by others on the same theme. Looked at in one way, Everett's interpretation calls for a return to naive realism and the old fashioned idea that there can be a direct correspondence between formalism and reality. Because physicists have become more sophisticated than this, and above all because the implications of his approach appear to them so bizarre, few have taken Everett seriously. Nevertheless his basic premise provides such a stimulating framework for discussions of the quantum theory of measurement that this volume should be on every quantum theoretician's shelf.

---

"... a picture, incomplete yet not false, of the universe as Ts'ui Pên conceived it to be. Differing from Newton and Schopenhauer,... [he] did not think of time as absolute and uniform. He believed in an infinite series of times, in a dizzily growing, ever spreading network of diverging, converging and parallel times. This web of time - the strands of which approach one another, bifurcate, intersect or ignore each other through the centuries - embraces every possibility. We do not exist in most of them. In some you exist and not I, while in others I do, and you do not, and in yet others both of us exist. In this one, in which chance has favored me, you have come to my gate. In another, you, crossing the garden, have found me dead. In yet another, I say these very same words, but am an error, a phantom."  

Jorge Luis Borges, The Garden of Forking Paths  

"Actualities seem to float in a wider sea of possibilities from out of which they were chosen; and somewhere, indeterminism says, such possibilities exist, and form part of the truth."  

William James

---

CONTENTS 

PREFACE ................................................................................................................................. v 

THE THEORY OF THE UNIVERSAL WAVE FUNCTION ............................ 
by Hugh Everett, III 

I. Introduction ......................................................................................................... 3 

II. Probability, Information, and Correlation ................................................. 13 

1. Finite joint distributions ........................................................................ 13 

2. Information for finite distributions ........................................................ 15 

3. Correlation for finite distributions ........................................................ 17 

4. Generalization and further properties of correlation ........................ 20 

5. Information for general distributions ................................................. 25 

6. Example: Information decay in stochastic processes .................... 28 

7. Example: Conservation of information in classical
mechanics ......................................................................................... 30 

III. Quantum Mechanics .................................................................................... 33 

1. Composite systems ................................................................................. 35 

2. Information and correlation in quantum mechanics ........................ 43 

3. Measurement ......................................................................................... 53 

IV. Observation .................................................................................................. 63 

1. Formulation of the problem ................................................................. 63 

2. Deductions ............................................................................................. 66 

3. Several observers .................................................................................... 78 

V. Supplementary Topics ................................................................................. 85 

1. Macroscopic objects and classical mechanics .................................. 86 

2. Amplification processes ........................................................................ 90 

3. Reversibility and irreversibility ............................................................ 94 

4. Approximate measurement ................................................................. 100 

5. Discussion of a spin measurement example ........................................ 103 

VI. Discussion .................................................................................................. 109 

Appendix I ....................................................................................................... 121 

1. Proof of Theorem 1 ................................................................................. 121 

2. Convex function inequalities ................................................................. 122 

3. Refinement theorems ............................................................................. 124 

4. Monotone decrease of information for stochastic
processes ............................................................................................ 126 

5. Proof of special inequality for Chapter IV (1.7) ................................ 128 

6. Stationary point of \(I_K + I_X\) ................................................................. 129 

Appendix II ....................................................................................................... 133 

References ....................................................................................................... 139

---

"RELATIVE STATE" FORMULATION OF QUANTUM MECHANICS by Hugh Everett, III 141 ASSESSMENT OF EVERETT'S "RELATIVE STATE" FORMULATION OF QUANTUM THEORY by John A. Wheeler 151 QUANTUM MECHANICS AND REALITY by Bryce S. DeWitt 155 THE MANY- UNIVERSES INTERPRETATION OF QUANTUM MECHANICS by Bryce S. DeWitt 167 ON THE INTERPRETATION OF MEASUREMENT WITHIN THE QUANTUM THEORY by Leon N. Cooper and Deborah van Vechten 219 THE MEASUREMENT OF RELATIVE FREQUENCY by Neill Graham 229

---

# The Many-Worlds Interpretation of Quantum Mechanics

---

\[ \text{1} \]

---

# THE THEORY OF THE UNIVERSAL WAVE FUNCTION  

Hugh Everett, III  

### I. INTRODUCTION  

We begin, as a way of entering our subject, by characterizing a particular interpretation of quantum theory which, although not representative of the more careful formulations of some writers, is the most common form encountered in textbooks and university lectures on the subject.  

A physical system is described completely by a state function \(\psi\) , which is an element of a Hilbert space, and which furthermore gives information only concerning the probabilities of the results of various observations which can be made on the system. The state function \(\psi\) is thought of as objectively characterizing the physical system, i.e., at all times an isolated system is thought of as possessing a state function, independently of our state of knowledge of it. On the other hand, \(\psi\) changes in a causal manner so long as the system remains isolated, obeying a differential equation. Thus there are two fundamentally different ways in which the state function can change: \(^{1}\)  

Process 1: The discontinuous change brought about by the observation of a quantity with eigenstates \(\phi_{1}, \phi_{2}, \ldots\) , in which the state \(\psi\) will be changed to the state \(\phi_{j}\) with probability \(|\langle \psi , \phi_{j} \rangle |^{2}\) .  

Process 2: The continuous, deterministic change of state of the (isolated) system with time according to a wave equation \(\frac{\partial \psi}{\partial t} = \mathbf{U} \psi\) , where \(\mathbf{U}\) is a linear operator.

---

The question of the consistency of the scheme arises if one contemplates regarding the observer and his object- system as a single (composite) physical system. Indeed, the situation becomes quite paradoxical if we allow for the existence of more than one observer. Let us consider the case of one observer A, who is performing measurements upon a system S, the totality \((A + S)\) in turn forming the object- system for another observer, B.  

If we are to deny the possibility of B's use of a quantum mechanical description (wave function obeying wave equation) for \(A + S\) , then we must be supplied with some alternative description for systems which contain observers (or measuring apparatus). Furthermore, we would have to have a criterion for telling precisely what type of systems would have the preferred positions of "measuring apparatus" or "observer" and be subject to the alternate description. Such a criterion is probably not capable of rigorous formulation.  

On the other hand, if we do allow B to give a quantum description to \(A + S\) , by assigning a state function \(\psi^{A + S}\) , then, so long as B does not interact with \(A + S\) , its state changes causally according to Process 2, even though A may be performing measurements upon S. From B's point of view, nothing resembling Process 1 can occur (there are no discontinuities), and the question of the validity of A's use of Process 1 is raised. That is, apparently either A is incorrect in assuming Process 1, with its probabilistic implications, to apply to his measurements, or else B's state function, with its purely causal character, is an inadequate description of what is happening to \(A + S\) .  

To better illustrate the paradoxes which can arise from strict adherence to this interpretation we consider the following amusing, but extremely hypothetical drama.  

Isolated somewhere out in space is a room containing an observer,  

A, who is about to perform a measurement upon a system S. After performing his measurement he will record the result in his notebook. We assume that he knows the state function of S (perhaps as a result

---

of previous measurement), and that it is not an eigenstate of the measurement he is about to perform. A, being an orthodox quantum theorist, then believes that the outcome of his measurement is undetermined and that the process is correctly described by Process 1.  

In the meantime, however, there is another observer, B, outside the room, who is in possession of the state function of the entire room, including S, the measuring apparatus, and A, just prior to the measurement. B is only interested in what will be found in the notebook one week hence, so he computes the state function of the room for one week in the future according to Process 2. One week passes, and we find B still in possession of the state function of the room, which this equally orthodox quantum theorist believes to be a complete description of the room and its contents. If B's state function calculation tells beforehand exactly what is going to be in the notebook, then A is incorrect in his belief about the indeterminacy of the outcome of his measurement. We therefore assume that B's state function contains non- zero amplitudes over several of the notebook entries.  

At this point, B opens the door to the room and looks at the notebook (performs his observation). Having observed the notebook entry, he turns to A and informs him in a patronizing manner that since his (B's) wave function just prior to his entry into the room, which he knows to have been a complete description of the room and its contents, had non- zero amplitude over other than the present result of the measurement, the result must have been decided only when B entered the room, so that A, his notebook entry, and his memory about what occurred one week ago had no independent objective existence until the intervention by B. In short, B implies that A owes his present objective existence to B's generous nature which compelled him to intervene on his behalf. However, to B's consternation, A does not react with anything like the respect and gratitude he should exhibit towards B, and at the end of a somewhat heated reply, in which A conveys in a colorful manner his opinion of B and his beliefs, he

---

rudely punctures B's ego by observing that if B's view is correct, then he has no reason to feel complacent, since the whole present situation may have no objective existence, but may depend upon the future actions of yet another observer.  

It is now clear that the interpretation of quantum mechanics with which we began is untenable if we are to consider a universe containing more than one observer. We must therefore seek a suitable modification of this scheme, or an entirely different system of interpretation. Several alternatives which avoid the paradox are:  

Alternative 1: To postulate the existence of only one observer in the universe. This is the solipsist position, in which each of us must hold the view that he alone is the only valid observer, with the rest of the universe and its inhabitants obeying at all times Process 2 except when under his observation.  

This view is quite consistent, but one must feel uneasy when, for example, writing textbooks on quantum mechanics, describing Process 1, for the consumption of other persons to whom it does not apply.  

Alternative 2: To limit the applicability of quantum mechanics by asserting that the quantum mechanical description fails when applied to observers, or to measuring apparatus, or more generally to systems approaching macroscopic size.  

If we try to limit the applicability so as to exclude measuring apparatus, or in general systems of macroscopic size, we are faced with the difficulty of sharply defining the region of validity. For what \(n\) might a group of \(n\) particles be construed as forming a measuring device so that the quantum description fails? And to draw the line at human or animal observers, i.e., to assume that all mechanical aparata obey the usual laws, but that they are somehow not valid for living observers, does violence to the so- called

---

principle of psycho- physical parallelism, \(^{2}\) and constitutes a view to be avoided, if possible. To do justice to this principle we must insist that we be able to conceive of mechanical devices (such as servomechanisms), obeying natural laws, which we would be willing to call observers.  

Alternative 3: To admit the validity of the state function description, but to deny the possibility that B could ever be in possession of the state function of A + S. Thus one might argue that a determination of the state of A would constitute such a drastic intervention that A would cease to function as an observer.  

The first objection to this view is that no matter what the state of A + S is, there is in principle a complete set of commuting operators for which it is an eigenstate, so that, at least, the determination of these quantities will not affect the state nor in any way disrupt the operation of A. There are no fundamental restrictions in the usual theory about the knowability of any state functions, and the introduction of any such restrictions to avoid the paradox must therefore require extra postulates.  

The second objection is that it is not particularly relevant whether or not B actually knows the precise state function of A + S. If he merely believes that the system is described by a state function, which he does not presume to know, then the difficulty still exists. He must then believe that this state function changed deterministically, and hence that there was nothing probabilistic in A's determination.

---

Alternative 4: To abandon the position that the state function is a complete description of a system. The state function is to be regarded not as a description of a single system, but of an ensemble of systems, so that the probabilistic assertions arise naturally from the incompleteness of the description.  

It is assumed that the correct complete description, which would presumably involve further (hidden) parameters beyond the state function alone, would lead to a deterministic theory, from which the probabilistic aspects arise as a result of our ignorance of these extra parameters in the same manner as in classical statistical mechanics.  

Alternative 5: To assume the universal validity of the quantum description, by the complete abandonment of Process 1. The general validity of pure wave mechanics, without any statistical assertions, is assumed for all physical systems, including observers and measuring apparata. Observation processes are to be described completely by the state function of the composite system which includes the observer and his object- system, and which at all times obeys the wave equation (Process 2).  

This brief list of alternatives is not meant to be exhaustive, but has been presented in the spirit of a preliminary orientation. We have, in fact, omitted one of the foremost interpretations of quantum theory, namely the position of Niels Bohr. The discussion will be resumed in the final chapter, when we shall be in a position to give a more adequate appraisal of the various alternate interpretations. For the present, however, we shall concern ourselves only with the development of Alternative 5.  

It is evident that Alternative 5 is a theory of many advantages. It has the virtue of logical simplicity and it is complete in the sense that it is applicable to the entire universe. All processes are considered equally (there are no "measurement processes" which play any preferred role), and the principle of psycho- physical parallelism is fully maintained. Since

---

the universal validity of the state function description is asserted, one can regard the state functions themselves as the fundamental entities, and one can even consider the state function of the whole universe. In this sense this theory can be called the theory of the "universal wave function," since all of physics is presumed to follow from this function alone. There remains, however, the question whether or not such a theory can be put into correspondence with our experience.  

The present thesis is devoted to showing that this concept of a universal wave mechanics, together with the necessary correlation machinery for its interpretation, forms a logically self consistent description of a universe in which several observers are at work.  

We shall be able to introduce into the theory systems which represent observers. Such systems can be conceived as automatically functioning machines (servomechanisms) possessing recording devices (memory) and which are capable of responding to their environment. The behavior of these observers shall always be treated within the framework of wave mechanics. Furthermore, we shall deduce the probabilistic assertions of Process 1 as subjective appearances to such observers, thus placing the theory in correspondence with experience. We are then led to the novel situation in which the formal theory is objectively continuous and causal, while subjectively discontinuous and probabilistic. While this point of view thus shall ultimately justify our use of the statistical assertions of the orthodox view, it enables us to do so in a logically consistent manner, allowing for the existence of other observers. At the same time it gives a deeper insight into the meaning of quantized systems, and the role played by quantum mechanical correlations.  

In order to bring about this correspondence with experience for the pure wave mechanical theory, we shall exploit the correlation between subsystems of a composite system which is described by a state function. A subsystem of such a composite system does not, in general, possess an independent state function. That is, in general a composite system cannot be represented by a single pair of subsystem states, but can be repre

---

sented only by a superposition of such pairs of subsystem states. For example, the Schrodinger wave function for a pair of particles, \(\psi (x_{1}, x_{2})\) , cannot always be written in the form \(\psi = \phi (x_{1}) \eta (x_{2})\) , but only in the form \(\psi = \sum_{i,j} a_{ij} \phi^{i}(x_{1}) \eta^{j}(x_{2})\) . In the latter case, there is no single state for Particle 1 alone or Particle 2 alone, but only the superposition of such cases.  

In fact, to any arbitrary choice of state for one subsystem there will correspond a relative state for the other subsystem, which will generally be dependent upon the choice of state for the first subsystem, so that the state of one subsystem is not independent, but correlated to the state of the remaining subsystem. Such correlations between systems arise from interaction of the systems, and from our point of view all measurement and observation processes are to be regarded simply as interactions between observer and object- system which produce strong correlations.  

Let one regard an observer as a subsystem of the composite system: observer + object- system. It is then an inescapable consequence that after the interaction has taken place there will not, generally, exist a single observer state. There will, however, be a superposition of the composite system states, each element of which contains a definite observer state and a definite relative object- system state. Furthermore, as we shall see, each of these relative object- system states will be, approximately, the eigenstates of the observation corresponding to the value obtained by the observer which is described by the same element of the superposition. Thus, each element of the resulting superposition describes an observer who perceived- a definite and generally different result, and to whom it appears that the object- system state has been transformed into the corresponding eigenstate. In this sense the usual assertions of Process 1 appear to hold on a subjective level to each observer described by an element of the superposition. We shall also see that correlation plays an important role in preserving consistency when several observers are present and allowed to interact with one another (to "consult" one another) as well as with other object- systems.

---

In order to develop a language for interpreting our pure wave mechanics for composite systems we shall find it useful to develop quantitative definitions for such notions as the "sharpness" or "definiteness" of an operator A for a state \(\psi\) , and the "degree of correlation" between the subsystems of a composite system or between a pair of operators in the subsystems, so that we can use these concepts in an unambiguous manner. The mathematical development of these notions will be carried out in the next chapter (II) using some concepts borrowed from Information Theory. \(^{3}\) We shall develop there the general definitions of information and correlation, as well as some of their more important properties. Throughout Chapter II we shall use the language of probability theory to facilitate the exposition, and because it enables us to introduce in a unified manner a number of concepts that will be of later use. We shall nevertheless subsequently apply the mathematical definitions directly to state functions, by replacing probabilities by square amplitudes, without, however, making any reference to probability models.  

Having set the stage, so to speak, with Chapter II, we turn to quantum mechanics in Chapter III. There we first investigate the quantum formalism of composite systems, particularly the concept of relative state functions, and the meaning of the representation of subsystems by noninterfering mixtures of states characterized by density matrices. The notions of information and correlation are then applied to quantum mechanics. The final section of this chapter discusses the measurement process, which is regarded simply as a correlation- inducing interaction between subsystems of a single isolated system. A simple example of such a measurement is given and discussed, and some general consequences of the superposition principle are considered.

---

This will be followed by an abstract treatment of the problem of Observation (Chapter IV). In this chapter we make use only of the superposition principle, and general rules by which composite system states are formed of subsystem states, in order that our results shall have the greatest generality and be applicable to any form of quantum theory for which these principles hold. (Elsewhere, when giving examples, we restrict ourselves to the non-relativistic Schrödinger Theory for simplicity.) The validity of Process 1 as a subjective phenomenon is deduced, as well as the consistency of allowing several observers to interact with one another.  

Chapter V supplements the abstract treatment of Chapter IV by discussing a number of diverse topics from the point of view of the theory of pure wave mechanics, including the existence and meaning of macroscopic objects in the light of their atomic constitution, amplification processes in measurement, questions of reversibility and irreversibility, and approximate measurement.  

The final chapter summarizes the situation, and continues the discussion of alternate interpretations of quantum mechanics.

---

## II. PROBABILITY, INFORMATION, AND CORRELATION  

The present chapter is devoted to the mathematical development of the concepts of information and correlation. As mentioned in the introduction we shall use the language of probability theory throughout this chapter to facilitate the exposition, although we shall apply the mathematical definitions and formulas in later chapters without reference to probability models. We shall develop our definitions and theorems in full generality, for probability distributions over arbitrary sets, rather than merely for distributions over real numbers, with which we are mainly interested at present. We take this course because it is as easy as the restricted development, and because it gives a better insight into the subject.  

The first three sections develop definitions and properties of information and correlation for probability distributions over finite sets only. In section four the definition of correlation is extended to distributions over arbitrary sets, and the general invariance of the correlation is proved. Section five then generalizes the definition of information to distributions over arbitrary sets. Finally, as illustrative examples, sections seven and eight give brief applications to stochastic processes and classical mechanics, respectively.  

## §1. Finite joint distributions  

We assume that we have a collection of finite sets, \(\mathcal{X},\mathcal{Y},\ldots ,\mathcal{Z}\) , whose elements are denoted by \(\mathbf{x}_{i}\in \mathcal{X}\) , \(\mathbf{y}_{j}\in \mathcal{Y},\ldots\) , \(\mathbf{z}_{\mathbf{k}}\in \mathcal{Z}\) , etc., and that we have a joint probability distribution, \(\mathrm{P} = \mathrm{P}(\mathbf{x}_{1},\mathbf{y}_{1},\ldots ,\mathbf{z}_{\mathbf{k}})\) , defined on the cartesian product of the sets, which represents the probability of the combined event \(\mathbf{x}_{i},\mathbf{y}_{j},\ldots\) , and \(\mathbf{z}_{\mathbf{k}}\) . We then denote by \(\mathbf{X},\mathbf{Y},\ldots ,\mathbf{Z}\) the random variables whose values are the elements of the sets \(\mathcal{X},\mathcal{Y},\ldots ,\mathcal{Z}\) , with probabilities given by \(\mathrm{P}\) .

---

For any subset \(Y, \ldots , Z\) , of a set of random variables \(W, \ldots , X, Y, \ldots , Z\) , with joint probability distribution \(P(w_{i}, \ldots , x_{j}, y_{k}, \ldots , z_{q})\) , the marginal distribution, \(P(y_{k}, \ldots , z_{q})\) , is defined to be:  

\[\mathrm{P}(y_{k},\ldots ,z_{q}) = \sum_{i,\ldots ,j}\mathrm{P}(w_{i},\ldots ,x_{j},y_{k},\ldots ,z_{q}), \quad (1.1)\]  

which represents the probability of the joint occurrence of \(y_{k}, \ldots , z_{q}\) , with no restrictions upon the remaining variables.  

For any subset \(Y, \ldots , Z\) of a set of random variables the conditional distribution, conditioned upon the values \(W = w_{i}, \ldots , X = x_{j}\) for any remaining subset \(W, \ldots , X\) , and denoted by \(P(w_{i}, \ldots , x_{j}, y_{k}, \ldots z_{q})\) , is defined to be:  

\[\mathrm{P}^{w_{i}, \ldots , x_{j}}(y_{k}, \ldots , z_{q}) = \frac{P(w_{i}, \ldots , x_{j}, y_{k}, \ldots , z_{\ell})}{P(w_{i}, \ldots , x_{j})}, \quad (1.2)\]  

which represents the probability of the joint event \(Y = y_{k}, \ldots , Z = z_{\ell}\) , conditioned by the fact that \(W, \ldots , X\) are known to have taken the values \(w_{i}, \ldots , x_{j}\) , respectively.  

For any numerical valued function \(F(y_{k}, \ldots , z_{q})\) , defined on the elements of the cartesian product of \(y, \ldots , z\) , the expectation, denoted by \(\mathrm{Exp}[\mathrm{F}]\) , is defined to be:  

\[\mathrm{Exp}[\mathrm{F}] = \sum_{k, \ldots , \ell} P(y_{k}, \ldots , z_{\ell}) F(y_{k}, \ldots , z_{\ell}). \quad (1.3)\]  

We note that if \(P(y_{k}, \ldots , z_{q})\) is a marginal distribution of some larger distribution \(P(w_{i}, \ldots , x_{j}, y_{k}, \dots , z_{q})\) then  

\[\mathrm{Exp}[\mathrm{F}] = \sum_{k, \dots , \ell} \left(\sum_{\ell, \dots , j} P(w_{i}, \dots , x_{j}, y_{k}, \dots , z_{\ell})\right) F(y_{k}, \dots , z_{\ell})\] \[= \sum_{i, \dots , j, k, \dots , \ell} P(w_{i}, \dots , x_{j}, y_{k}, \dots z_{\ell}) F(y_{k}, \dots , z_{\ell}),\]

---

so that if we wish to compute \(\mathbf{Exp}[\mathbf{F}]\) with respect to some joint distribution it suffices to use any marginal distribution of the original distribution which contains at least those variables which occur in \(\mathbf{F}\) .  

We shall also occasionally be interested in conditional expectations, which we define as:  

\[\mathbf{Exp}^{w_{1},\dots ,x_{j}}[\mathbf{F}] = \sum_{\mathbf{k},\dots ,\ell}\mathbf{P}^{w_{1},\dots ,x_{j}}(\mathbf{y}_{\mathbf{k}},\dots ,z_{\ell})\mathbf{F}(\mathbf{y}_{\mathbf{k}},\dots ,z_{\ell}), \quad (1.5)\]  

and we note the following easily verified rules for expectations:  

\[\begin{array}{r l} & {\mathrm{Exp}[\mathrm{Exp}[\mathrm{F}]] = \mathrm{Exp}[\mathrm{F}],}\\ & {\mathrm{Exp}^{u_{1},\dots ,v_{j}}[\mathrm{Exp}^{u_{1},\dots ,v_{j},w_{k},\dots ,x_{\ell}}[\mathrm{F}]] = \mathrm{Exp}^{u_{1},\dots ,v_{j}}[\mathrm{F}],}\\ & {\mathrm{Exp}[\mathrm{F} + \mathrm{G}] = \mathrm{Exp}[\mathrm{F}] + \mathrm{Exp}[\mathrm{G}].} \end{array} \quad (1.7)\]  

We should like finally to comment upon the notion of independence. Two random variables \(\mathbf{X}\) and \(\mathbf{Y}\) with joint distribution \(\mathbf{P}(\mathbf{x}_{i}, \mathbf{y}_{j})\) will be said to be independent if and only if \(\mathbf{P}(\mathbf{x}_{i}, \mathbf{y}_{j})\) is equal to \(\mathbf{P}(\mathbf{x}_{i}) \mathbf{P}(\mathbf{y}_{j})\) for all \(i, j\) . Similarly, the groups of random variables \((\mathbf{U} \dots \mathbf{V}), (\mathbf{W} \dots \mathbf{X}), \dots , (\mathbf{Y} \dots \mathbf{Z})\) will be called mutually independent groups if and only if \(\mathbf{P}(\mathbf{u}_{i}, \dots , \mathbf{v}_{j}, \mathbf{w}_{k}, \dots , \mathbf{x}_{\ell}, \dots , \mathbf{y}_{m}, \dots , \mathbf{z}_{n})\) is always equal to \(\mathbf{P}(\mathbf{u}_{i}, \dots , \mathbf{v}_{j})\) \(\mathbf{P}(\mathbf{w}_{k}, \dots , \mathbf{x}_{\ell}) \dots \mathbf{P}(\mathbf{y}_{m}, \dots , \mathbf{z}_{n})\) .  

Independence means that the random variables take on values which are not influenced by the values of other variables with respect to which they are independent. That is, the conditional distribution of one of two independent variables, \(\mathbf{Y}\) , conditioned upon the value \(\mathbf{x}_{i}\) for the other, is independent of \(\mathbf{x}_{i}\) , so that knowledge about one variable tells nothing of the other.  

## \(\S 2\) . Information for finite distributions  

Suppose that we have a single random variable \(\mathbf{X}\) , with distribution \(\mathbf{P}(\mathbf{x}_{i})\) . We then define \(^2\) a number, \(\mathbf{I}_{\mathbf{X}}\) , called the information of \(\mathbf{X}\) , to be:

---

\[I_{X} = \sum_{i} P(x_{i})\ln P(x_{i}) = \exp [\ln P(x_{i})]~,\]  

which is a function of the probabilities alone and not of any possible numerical values of the \(x_{i}\) 's themselves. \(^{3}\)  

The information is essentially a measure of the sharpness of a probability distribution, that is, an inverse measure of its "spread." In this respect information plays a role similar to that of variance. However, it has a number of properties which make it a superior measure of the "sharpness" than the variance, not the least of which is the fact that it can be defined for distributions over arbitrary sets, while variance is defined only for distributions over real numbers.  

Any change in the distribution \(P(x_{i})\) which "levels out" the probabilities decreases the information. It has the value zero for "perfectly sharp" distributions, in which the probability is one for one of the \(x_{i}\) and zero for all others, and ranges downward to \(- \ln n\) for distributions over \(n\) elements which are equal over all of the \(x_{i}\) . The fact that the information is nonpositive is no liability, since we are seldom interested in the absolute information of a distribution, but only in differences.  

We can generalize (2.1) to obtain the formula for the information of a group of random variables \(X, Y, \ldots , Z\) , with joint distribution \(P(x_{i}, y_{j}, \ldots , z_{k})\) , which we denote by \(I_{XY \ldots Z}\) :  

\[\begin{array}{r l} & {I_{X Y\ldots Z} = \sum_{i,j,\ldots ,k}P(x_{i},y_{j},\ldots ,z_{k})\ln P(x_{i},y_{j},\ldots ,z_{k})}\\ & {\qquad = \mathrm{Exp}\left[\ln P(x_{i},y_{j},\ldots ,z_{k})\right],} \end{array} \quad (2.2)\]

---

which follows immediately from our previous definition, since the group of random variables \(X, Y, \ldots , Z\) may be regarded as a single random variable \(W\) which takes its values in the cartesian product \(\mathcal{X} \times \mathcal{Y} \times \cdots \times \mathcal{Z}\) .  

Finally, we define a conditional information, \(I_{\mathrm{XY}\ldots \mathrm{Z}}^{\mathrm{v}_{\mathrm{m}},\ldots ,\mathrm{w}_{\mathrm{n}}}\) , to be:  

\[\begin{array}{r l} & {I_{\mathrm{XY}\ldots \mathrm{Z}}^{\mathrm{v}_{\mathrm{m}},\ldots ,w_{\mathrm{n}}} = \sum_{\mathrm{i},\mathrm{j},\ldots ,\mathrm{k}}\mathrm{P}^{\mathrm{v}_{\mathrm{m}},\ldots ,w_{\mathrm{n}}}(\mathrm{x}_{\mathrm{i}},\mathrm{y}_{\mathrm{j}},\ldots ,\mathrm{z}_{\mathrm{k}})\mathrm{ln}\mathrm{P}^{\mathrm{v}_{\mathrm{m}},\ldots ,w_{\mathrm{n}}}(\mathrm{x}_{i},\mathrm{y}_{j},\ldots ,\mathrm{z}_{\mathrm{k}})}\\ & {\qquad = \mathrm{Exp}^{\mathrm{v}_{\mathrm{m}},\ldots ,w_{\mathrm{n}}}[\mathrm{ln}\mathrm{P}^{\mathrm{v}_{\mathrm{m}},\ldots ,w_{\mathrm{n}}} (\mathrm{x}_{i},\mathrm{y}_{j},\ldots ,\mathrm{z}_{\mathrm{k}})]~,} \end{array} \quad (2.3)\]  

a quantity which measures our information about \(X, Y, \ldots , Z\) given that we know that \(V \ldots W\) have taken the particular values \(v_{\mathrm{m}}, \ldots , w_{\mathrm{n}}\) .  

For independent random variables \(X, Y, \ldots , Z\) , the following relationship is easily proved:  

\[I_{X Y\ldots Z} = I_{X} + I_{Y} + \ldots +I_{Z}\quad (X,Y,\ldots ,Z \text{ independent}), \quad (2.4)\]  

so that the information of \(X Y \ldots Z\) is the sum of the individual quantities of information, which is in accord with our intuitive feeling that if we are given information about unrelated events, our total knowledge is the sum of the separate amounts of information. We shall generalize this definition later, in §5.  

## §3. Correlation for finite distributions  

Suppose that we have a pair of random variables, \(X\) and \(Y\) , with joint distribution \(P(x_{i}, y_{j})\) . If we say that \(X\) and \(Y\) are correlated, what we intuitively mean is that one learns something about one variable when he is told the value of the other. Let us focus our attention upon the variable \(X\) . If we are not informed of the value of \(Y\) , then our information concerning \(X\) , \(I_{X}\) , is calculated from the marginal distribution \(P(x_{i})\) . However, if we are now told that \(Y\) has the value \(y_{j}\) , then our information about \(X\) changes to the information of the conditional distribution \(P^{y_{j}}(x_{i}), I_{X}^{y_{j}}\) . According to what we have said, we wish the degree correlation to measure how much we learn about \(X\) by being informed of

---

Y's value. However, since the change of information, \(I_{X}^{y j} - I_{X}\) , may depend upon the particular value, \(y_{j}\) , of \(Y\) which we are told, the natural thing to do to arrive at a single number to measure the strength of correlation is to consider the expected change in information about \(X\) , given that we are to be told the value of \(Y\) . This quantity we call the correlation information, or for brevity, the correlation, of \(X\) and \(Y\) , and denote it by \(\{X, Y\}\) . Thus:  

\[\{X,Y\} = \mathrm{Exp}\left[Y_{X}^{y} - I_{X}\right] = \mathrm{Exp}\left[Y_{X}^{y}\right] - I_{X}. \quad (3.1)\]  

Expanding the quantity \(\mathrm{Exp}\left[Y_{X}^{y}\right]\) using (2.3) and the rules for expectations (1.6) - (1.8) we find:  

\[\begin{array}{r l} & {\mathrm{Exp}\left[Y_{X}^{y}\right] = \mathrm{Exp}\left[\mathrm{Exp}^{y_{j}}\mathrm{ln}\mathrm{P}^{y_{j}}(x_{i})\right]}\\ & {= \mathrm{Exp}\left[\mathrm{ln}\frac{\mathrm{P}(x_{i},y_{j})}{\mathrm{P}(y_{j})}\right] = \mathrm{Exp}\left[\mathrm{ln}\mathrm{P}(x_{i},y_{j})\right] - \mathrm{Exp}\left[\mathrm{ln}\mathrm{P}(y_{j})\right]}\\ & {= I_{X Y} - I_{Y},} \end{array} \quad (3.2)\]  

and combining with (3.1) we have:  

\[\{X,Y\} = I_{X Y} - I_{X} - I_{Y}. \quad (3.3)\]  

Thus the correlation is symmetric between \(X\) and \(Y\) , and hence also equal to the expected change of information about \(Y\) given that we will be told the value of \(X\) . Furthermore, according to (3.3) the correlation corresponds precisely to the amount of "missing information" if we possess only the marginal distributions, i.e., the loss of information if we choose to regard the variables as independent.  

THEOREM 1. \(\{X, Y\} = 0\) if and only if \(X\) and \(Y\) are independent, and is otherwise strictly positive. (Proof in Appendix I.)

---

In this respect the correlation so defined is superior to the usual correlation coefficients of statistics, such as covariance, etc., which can be zero even when the variables are not independent, and which can assume both positive and negative values. An inverse correlation is, after all, quite as useful as a direct correlation. Furthermore, it has the great advantage of depending upon the probabilities alone, and not upon any numerical values of \(\mathbf{x}_{i}\) and \(\mathbf{y}_{j}\) , so that it is defined for distributions over sets whose elements are of an arbitrary nature, and not only for distributions over numerical properties. For example, we might have a joint probability distribution for the political party and religious affiliation of individuals. Correlation and information are defined for such distributions, although they possess nothing like covariance or variance.  

We can generalize (3.3) to define a group correlation for the groups of random variables (U...V), (W...X),..., (Y...Z), denoted by {U...V, W...X, ..., Y...Z} (where the groups are separated by commas), to be:  

\[\{U\dots V,W\dots X,\dots ,Y\dots Z\} = \mathrm{I}_{U\dots V}W\dots X\dots Y\dots Z\] \[-\mathrm{I}_{U\dots V} - \mathrm{I}_{W\dots X} - \dots -\mathrm{I}_{Y\dots Z},\]  

again measuring the information deficiency for the group marginals. Theorem 1 is also satisfied by the group correlation, so that it is zero if and only if the groups are mutually independent. We can, of course, also define conditional correlations in the obvious manner, denoting these quantities by appending the conditional values as superscripts, as before.  

We conclude this section by listing some useful formulas and inequalities which are easily proved:  

\[\{U,V,\dots,W\} = \mathrm{Exp}\left[\mathrm{ln}\frac{\mathrm{P}(\mathbf{u}_{i},\mathbf{v}_{j},\dots,\mathbf{w}_{k})}{\mathrm{P}(\mathbf{u}_{i})\mathrm{P}(\mathbf{v}_{j})\dots\mathrm{P}(\mathbf{w}_{k})}\right], \quad (3.5)\]  

\[\{U,V,\dots,W\}^{\mathbf{x}_{1}\dots \mathbf{y}_{j}} =\] \[\qquad \mathrm{Exp}\frac{\mathbf{x}_{1}\dots \mathbf{y}_{j}}{\mathrm{ln}\frac{\mathbf{P}^{\mathbf{x}_{1}\dots \mathbf{y}_{j}}(\mathbf{u}_{k},\mathbf{v}_{1},\dots,\mathbf{w}_{m})}{\mathbf{P}^{\mathbf{x}_{1}\dots \mathbf{y}_{j}}(\mathbf{u}_{k})\mathbf{P}^{\mathbf{x}_{1}\dots \mathbf{y}_{j}}(\mathbf{v}_{1})\dots\mathbf{P}^{\mathbf{x}_{1}\dots \mathbf{y}_{j}}(\mathbf{w}_{m})}} \quad (3.6)\]

---

\[\begin{array}{r}{\{\ldots ,\mathbf{U},\mathbf{V},\ldots \} = \{\ldots ,\mathbf{U}\mathbf{V},\ldots \} +\{\mathbf{U},\mathbf{V}\} ,} \end{array} \quad (3.7)\]  

\[\{\ldots ,\mathbf{U},\mathbf{V},\ldots ,\mathbf{W},\ldots \} = \{\ldots ,\mathbf{U}\mathbf{V},\ldots \mathbf{W},\ldots \} +\{\mathbf{U},\mathbf{V},\ldots ,\mathbf{W}\} (\mathrm{comma~removal}) \quad (3.8)\]  

\[\{\ldots ,\mathbf{U},\mathbf{V}\mathbf{W},\ldots \} - \{\ldots ,\mathbf{U}\mathbf{V},\mathbf{W},\ldots \} = \{\mathbf{U},\mathbf{V}\} - \{\mathbf{V},\mathbf{W}\} (\mathrm{commutator}), \quad (3.9)\]  

(3.9) \(\{X\} = 0\) (definition of bracket with no commas),  

\[\{\ldots ,\mathbf{X}\mathbf{X}\mathbf{V},\ldots \} = \{\ldots ,\mathbf{X}\mathbf{V},\ldots \} \quad (3.10)\]  

\[\{\ldots ,\mathbf{U}\mathbf{V},\mathbf{V}\mathbf{W},\ldots \} = \{\ldots ,\mathbf{U}\mathbf{V},\mathbf{W},\ldots \} - \{\mathbf{V},\mathbf{W}\} - \mathbf{I}_{\mathbf{V}} \quad (3.11)\]  

\[\begin{array}{r l} & {\{X,X\} = -\mathrm{I}_{X}\quad (\mathrm{self~correlation}),}\\ & {\{U,\mathrm{VW},X\}^{\dots \dots \mathrm{W}\dots \dots} = \{\mathrm{U},\mathrm{V},X\}^{\dots \dots \mathrm{W}\dots \dots},}\\ & {\{U,\mathrm{W},X\}^{\dots \dots \mathrm{W}\dots \dots} = \{\mathrm{u},X\}^{\dots \dots \mathrm{W}\dots \dots}}\\ & {\{U,\mathrm{W},X\}^{\dots \dots \mathrm{W}\dots} = \{\mathrm{u},X\}^{\dots \dots \mathrm{W}\dots}.} \end{array} \quad (3.13)\]  

\[\{X Y,Z\} \geq \{X,Z\} , \quad (3.14)\]  

\[\{X Y,Z\} \geq \{X,Z\} +\{Y,Z\} -\{X,Y\} , \quad (3.15)\]  

\[\{X,Y,Z\} \geq \{X,Y\} +\{X,Z\} . \quad (3.16)\]  

Note that in the above formulas any random variable \(\mathbf{W}\) may be replaced by any group \(\mathbf{X}\mathbf{Y}\ldots \mathbf{Z}\) and the relation holds true, since the set \(\mathbf{X}\mathbf{Y}\ldots \mathbf{Z}\) may be regarded as the single random variable \(\mathbf{W}\) , which takes its values in the cartesian product \(\mathcal{X}\times \mathcal{Y}\times \ldots \times \mathcal{Z}\) .  

## §4. Generalization and further properties of correlation  

Until now we have been concerned only with finite probability distributions, for which we have defined information and correlation. We shall now generalize the definition of correlation so as to be applicable to joint probability distributions over arbitrary sets of unrestricted cardinality.

---

We first consider the effects of refinement of a finite distribution. For example, we may discover that the event \(x_{i}\) is actually the disjunction of several exclusive events \(\widetilde{x}_{i}^{1},\ldots ,\widetilde{x}_{i}^{n}\) , so that \(x_{i}\) occurs if any one of the \(\widetilde{x}_{i}^{\mu}\) occurs, i.e., the single event \(x_{i}\) results from failing to distinguish between the \(\widetilde{x}_{i}^{\mu}\) . The probability distribution which distinguishes between the \(\widetilde{x}_{i}^{\mu}\) will be called a refinement of the distribution which does not. In general, we shall say that a distribution \(P^{\prime} = P^{\prime}(\widetilde{x}_{i}^{\mu},\ldots ,\widetilde{y}_{j}^{\nu})\) is a refinement of \(P = P(x_{i},\ldots ,y_{j})\) if  

\[P(x_{i},\ldots ,y_{j}) = \sum_{\mu ,\ldots ,\nu}P^{\prime}(\widetilde{x}_{i}^{\mu},\ldots ,\widetilde{y}_{j}^{\nu})\quad (\mathrm{all~}i,\ldots ,j). \quad (4.1)\]  

We now state an important theorem concerning the behavior of correlation under a refinement of a joint probability distributions:  

THEOREM 2. \(P^{\prime}\) is a refinement of \(P \Rightarrow \{X, \ldots , Y \mid \geq \{X, \ldots , Y\} \text{ so that}\) correlations never decrease upon refinement of a distribution. (Proof in Appendix I, §3. )  

As an example, suppose that we have a continuous probability density \(P(x, y)\) . By division of the axes into a finite number of intervals, \(\bar{x}_{i}, \bar{y}_{j}\) , we arrive at a finite joint distribution \(P_{ij}\) , by integration of \(P(x, y)\) over the rectangle whose sides are the intervals \(\bar{x}_{i}\) and \(\bar{y}_{j}\) , and which represents the probability that \(X \in \bar{x}_{i}\) and \(Y \in \bar{y}_{j}\) . If we now subdivide the intervals, the new distribution \(P^{\prime}\) will be a refinement of \(P\) , and by Theorem 2 the correlation \(\{X, Y\}\) computed from \(P^{\prime}\) will never be less than that computed from \(P\) . Theorem 2 is seen to be simply the mathematical verification of the intuitive notion that closer analysis of a situation in which quantities \(X\) and \(Y\) are dependent can never lessen the knowledge about \(Y\) which can be obtained from \(X\) .  

This theorem allows us to give a general definition of correlation which will apply to joint distributions over completely arbitrary sets, i.e.,

---

for any probability measure<sup>4</sup> on an arbitrary product space, in the following manner:  

Assume that we have a collection of arbitrary sets \(\mathcal{X},\mathcal{Y},\ldots ,\mathcal{Z}\) , and a probability measure, \(\mathbf{M}_{\mathcal{P}}(\mathcal{X}\times \mathcal{Y}\times \dots \times \mathcal{Z})\) , on their cartesian product. Let \(\mathcal{P}^{\mu}\) be any finite partition of \(\mathcal{X}\) into subsets \(\mathcal{X}_{i}^{\mu}\) , \(\mathcal{Y}\) into subsets \(\mathcal{Y}_{j}^{\mu}\) , ..., and \(\mathcal{Z}\) into subsets \(\mathcal{Z}_{k}^{\mu}\) , such that the sets \(\mathcal{X}_{i}^{\mu}\times \mathcal{Y}_{j}^{\mu}\times \dots \times \mathcal{Z}_{k}^{\mu}\) of the cartesian product are measurable in the probability measure \(\mathbf{M}_{\mathcal{P}}\) . Another partition \(\mathcal{P}^{\nu}\) is a refinement of \(\mathcal{P}^{\mu}\) , \(\mathcal{P}^{\nu} \subseteq \mathcal{P}^{\mu}\) , if \(\mathcal{P}^{\nu}\) results from \(\mathcal{P}^{\mu}\) by further subdivision of the subsets \(\mathcal{X}_{i}^{\mu},\mathcal{Y}_{j}^{\mu},\ldots ,\mathcal{Z}_{k}^{\mu}\) . Each partition \(\mathcal{P}^{\mu}\) results in a finite probability distribution, for which the correlation, \(\{X,Y,\ldots ,Z\}^{\mathcal{P}^{\mu}}\) , is always defined through (3.3). Furthermore a refinement of a partition leads to a refinement of the probability distribution, so that by Theorem 2:  

\[\mathcal{P}^{\nu} \subseteq \mathcal{P}^{\mu} \Rightarrow \{X,Y,\ldots ,Z\}^{\mathcal{P}^{\nu}} \geq \{X,Y,\ldots ,Z\}^{\mathcal{P}^{\mu}} \quad (4.8)\]  

Now the set of all partitions is partially ordered under the refinement relation. Moreover, because for any pair of partitions \(\mathcal{P}, \mathcal{P}^{\prime}\) there is always a third partition \(\mathcal{P}^{\prime \prime}\) which is a refinement of both (common lower bound), the set of all partitions forms a directed set.<sup>5</sup> For a function, \(f\) , on a directed set, \(\mathcal{S}\) , one defines a directed set limit, \(\lim f\) :  

DEFINITION. \(\lim f\) exists and is equal to \(a \Leftrightarrow\) for every \(\epsilon > 0\) there exists an \(a \in \mathcal{S}\) such that \(|f(\beta) - a| < \epsilon\) for every \(\beta \in \mathcal{S}\) for which \(\beta \leq a\) .  

It is easily seen from the directed set property of common lower bounds that if this limit exists it is necessarily unique.

---

By (4.8) the correlation \(\{X,Y,\ldots ,Z\}^{\mathcal{P}}\) is a monotone function on the directed set of all partitions. Consequently the directed set limit, which we shall take as the basic definition of the correlation \(\{X,Y,\ldots ,Z\}\) , always exists. (It may be infinite, but it is in every case well defined.) Thus:  

DEFINITION. \(\{X,Y,\ldots ,Z\} = \lim \{X,Y,\ldots ,Z\}^{\mathcal{P}}\) ,  

and we have succeeded in our endeavor to give a completely general definition of correlation, applicable to all types of distributions.  

It is an immediate consequence of (4.8) that this directed set limit is the supremum of \(\{X,Y,\ldots ,Z\}^{\mathcal{P}}\) , so that:  

\[\{X,Y,\ldots ,Z\} = \sup_{\mathcal{P}}\{X,Y,\ldots ,Z\}^{\mathcal{P}}, \quad (4.9)\]  

which we could equally well have taken as the definition.  

Due to the fact that the correlation is defined as a limit for discrete distributions, Theorem 1 and all of the relations (3.7) to (3.15), which contain only correlation brackets, remain true for arbitrary distributions. Only (3.11) and (3.12), which contain information terms, cannot be extended.  

We can now prove an important theorem about correlation which concerns its invariant nature. Let \(\mathcal{X},\mathcal{Y},\ldots ,\mathcal{Z}\) be arbitrary sets with probability measure \(\mathbf{M}_{\mathbf{P}}\) on their cartesian product. Let \(\mathbf{f}\) be any one- one mapping of \(\mathcal{X}\) onto a set \(\mathfrak{U}\) , \(\mathbf{g}\) a one- one map of \(\mathcal{Y}\) onto \(\mathfrak{O},\ldots\) , and \(\mathbf{h}\) a map of \(\mathcal{Z}\) onto \(\mathfrak{O}\) . Then a joint probability distribution over \(\mathcal{X}\times \mathcal{Y}\times \ldots \times \mathcal{Z}\) leads also to one over \(\mathfrak{U}\times \mathfrak{O}\times \ldots \times \mathfrak{O}\) where the probability \(\mathbf{M}_{\mathbf{P}}^{\prime}\) induced on the product \(\mathfrak{U}\times \mathfrak{O}\times \ldots \times \mathfrak{O}\) is simply the measure which assigns to each subset of \(\mathfrak{U}\times \mathfrak{O}\times \ldots \times \mathfrak{O}\) the measure which is the measure of its image set in \(\mathcal{X}\times \mathcal{Y}\times \ldots \times \mathcal{Z}\) for the original measure \(\mathbf{M}_{\mathbf{P}}\) . (We have simply transformed to a new set of random variables: \(\mathbf{U} = \mathbf{f}(\mathbf{X})\) , \(\mathbf{V} = \mathbf{g}(\mathbf{Y})\) , ..., \(\mathbf{W} = \mathbf{h}(\mathbf{Z})\) .) Consider any partition \(\mathcal{P}\) of \(\mathcal{X},\mathcal{Y},\ldots ,\mathcal{Z}\) into the subsets \(\{\mathcal{X}_{i}\} ,\{\mathcal{Y}_{j}\} ,\ldots ,\{\mathcal{Z}_{k}\}\) with probability distribution \(\mathbf{P}_{\mathbf{i}\mathbf{j}\ldots \mathbf{k}} = \mathbf{M}_{\mathbf{P}}(\mathcal{X}_{i}\times \mathcal{Y}_{j}\times \ldots \times \mathcal{Z}_{k})\) . Then there is a corresponding partition \(\mathcal{P}^{\prime}\) of \(\mathfrak{U},\mathfrak{O},\ldots ,\mathfrak{O}\) into the image

---

sets of the sets of \(\mathcal{P},\{U_{i}\} ,\{U_{j}\} ,\ldots ,\{U_{k}\} ,\) where \(U_{i} = f(\mathcal{X}_{i}),U_{j} = g(\mathcal{Y}_{j}),\ldots ,\) \(U_{k} = h(\mathcal{Z}_{k})\) . But the probability distribution for \(\mathcal{P}^{\prime}\) is the same as that for \(\mathcal{P}\) , since \(\mathrm{P}_{ij\ldots k}^{\prime} = \mathrm{M}_{\mathrm{P}}^{\prime}(\mathrm{U}_{i}\times \mathrm{U}_{j}\times \dots \times \mathrm{U}_{k}) = \mathrm{M}_{\mathrm{P}}(\mathcal{X}_{i}\times \mathrm{y}_{j}\times \dots \times \mathcal{Z}_{k}) =\) \(\mathrm{P}_{ij\ldots k}\) , so that:  

\[\{X,Y,\ldots ,Z\}^{\mathcal{P}} = \{U,V,\ldots ,W\}^{\mathcal{P}^{\prime}} \quad (4.10)\]  

Due to the correspondence between the \(\mathcal{P}\) 's and \(\mathcal{P}\) 's we have that:  

\[\sup_{\mathcal{P}}\{X,Y,\ldots ,Z\}^{\mathcal{P}} = \sup_{\mathcal{P}^{\prime}}\{U,V,\ldots ,W\}^{\mathcal{P}^{\prime}}, \quad (4.11)\]  

and by virtue of (4.9) we have proved the following theorem:  

THEOREM 3. \(\{X,Y,\ldots ,Z\} = \{U,V,\ldots ,W\}\) , where \(U,U,\ldots ,U\) are any one- one images of \(\mathcal{X},\mathcal{Y},\ldots ,\mathcal{Z}\) , respectively. In other notation: \(\{X,Y,\ldots ,Z\} =\) \(\{f(X),g(Y),\ldots ,h(Z)\}\) for all one- one functions \(f,g,\ldots ,h\) .  

This means that changing variables to functionally related variables preserves the correlation. Again this is plausible on intuitive grounds, since a knowledge of \(f(x)\) is just as good as knowledge of \(x\) , provided that \(f\) is one- one.  

A special consequence of Theorem 3 is that for any continuous probability density \(P(x,y)\) over real numbers the correlation between \(f(x)\) and \(g(y)\) is the same as between \(x\) and \(y\) , where \(f\) and \(g\) are any real valued one- one functions. As an example consider a probability distribution for the position of two particles, so that the random variables are the position coordinates. Theorem 3 then assures us that the position correlation is independent of the coordinate system, even if different coordinate systems are used for each particle! Also for a joint distribution for a pair of events in space- time the correlation is invariant to arbitrary space- time coordinate transformations, again even allowing different transformations for the coordinates of each event.

---

These examples illustrate clearly the intrinsic nature of the correlation of various groups for joint probability distributions, which is implied by its invariance against arbitrary (one- one) transformations of the random variables. These correlation quantities are thus fundamental properties of probability distributions. A correlation is an absolute rather than relative quantity, in the sense that the correlation between (numerical valued) random variables is completely independent of the scale of measurement chosen for the variables.  

## §5. Information for general distributions  

Although we now have a definition of correlation applicable to all probability distributions, we have not yet extended the definition of information past finite distributions. In order to make this extension we first generalize the definition that we gave for discrete distributions to a definition of relative information for a random variable, relative to a given underlying measure, called the information measure, on the values of the random variable.  

If we assign a measure to the set of values of a random variable, \(X\) , which is simply the assignment of a positive number \(a_{i}\) to each value \(x_{i}\) in the finite case, we define the information of a probability distribution \(P(x_{i})\) relative to this information measure to be:  

\[\mathrm{I}_{X} = \sum_{\mathrm{i}}\mathrm{P}(x_{\mathrm{i}})\ln \frac{\mathrm{P}(x_{\mathrm{i}})}{a_{\mathrm{i}}} = \mathrm{Exp}\left[\ln \frac{\mathrm{P}(x_{\mathrm{i}})}{a_{\mathrm{i}}}\right] \quad (5.1)\]  

If we have a joint distribution of random variables \(X, Y, \ldots , Z\) , with information measures \(\{a_{i}\} , \{b_{j}\} , \ldots , \{c_{k}\}\) on their values, then we define the total information relative to these measures to be:  

\[\mathrm{I}_{X Y\ldots Z} = \sum_{\mathrm{i j}\ldots \mathrm{k}}\mathrm{P}(x_{\mathrm{i}},y_{\mathrm{j}},\ldots ,z_{\mathrm{k}})\ln \frac{\mathrm{P}(x_{\mathrm{i}},y_{\mathrm{j}},\ldots ,z_{\mathrm{k}}\mathrm{)}}{a_{\mathrm{i}}b_{\mathrm{j}}\ldots c_{\mathrm{k}}}\] \[\qquad = \mathrm{Exp}\left[\ln \frac{\mathrm{P}(x_{\mathrm{i}},y_{\mathrm{j}},\ldots ,\mathrm{z}_{\mathrm{k}})}{a_{\mathrm{i}}b_{\mathrm{j}}\ldots c_{\mathrm{k}}}\right],\]

---

so that the information measure on the cartesian product set is always taken to be the product measure of the individual information measures.  

We shall now alter our previous position slightly and consider information as always being defined relative to some information measure, so that our previous definition of information is to be regarded as the information relative to the measure for which all the \(\mathbf{a}_{1}\) 's, \(\mathbf{b}_{j}\) 's,... and \(\mathbf{c}_{k}\) 's are taken to be unity, which we shall henceforth call the uniform measure.  

Let us now compute the correlation \(\{X,Y,\ldots ,Z\}\) by (3.4) using the relative information:  

\[\begin{array}{r l} & {\{X,Y,\ldots ,Z\} ' = I_{X Y\ldots Z}^{\prime} - I_{X}^{\prime} - I_{Y}^{\prime} - \ldots -I_{Z}^{\prime}}\\ & {\qquad = \mathrm{Exp}\left[\ln \frac{\mathrm{P}(x_{1},y_{1},\ldots,z_{k})}{\mathrm{a}_{1}\mathrm{b}_{1}\ldots\mathrm{c}_{k}}\right] - \mathrm{Exp}\left[\ln \frac{\mathrm{P}(x_{1})}{\mathrm{a}_{1}}\right] - \ldots -}\\ & {\qquad \mathrm{Exp}\left[\ln \frac{\mathrm{P}(s_{k})}{\mathrm{c}_{k}}\right]}\\ & {\qquad = \mathrm{Exp}\left[\ln \frac{\mathrm{P}(x_{\mathrm{i}},y_{\mathrm{j}},\ldots,z_{k})}{\mathrm{P}(x_{\mathrm{i}})\mathrm{P}(y_{\mathrm{j}})\ldots\mathrm{P}(z_{\mathrm{k}})}\right] = \{X,Y,\ldots ,Z\} ,} \end{array} \quad (5.3)\]  

so that the correlation for discrete distributions, as defined by (3.4), is independent of the choice of information measure, and the correlation remains an absolute, not relative quantity. It can, however, be computed from the information relative to any information measure through (3.4).  

If we consider refinements, of our distributions, as before, and realize that such a refinement is also a refinement of the information measure, then we can prove a relation analogous to Theorem 2:  

THEOREM 4. The information of a distribution relative to a given information measure never decreases under refinement. (Proof in Appendix I.)  

Therefore, just as for correlation, we can define the information of a probability measure \(\mathbf{M}_{\mathbf{P}}\) on the cartesian product of arbitrary sets

---

\(\mathcal{X}, \mathcal{Y}, \ldots , \mathcal{Z}\) , relative to the information measures \(\mu_{X}, \mu_{Y}, \ldots , \mu_{Z}\) , on the individual sets, by considering finite partitions \(\mathcal{P}\) into subsets \(\{\mathcal{X}_{i}\} , \{\mathcal{Y}_{j}\} , \ldots , \{\mathcal{Z}_{k}\}\) , for which we take as the definition of the information:  

\[\mathrm{I}_{X Y\ldots Z}^{\mathcal{P}} = \sum_{\mathbf{i j}\ldots \mathbf{k}}\mathrm{M}_{\mathcal{P}}(\mathcal{X}_{i},\mathcal{Y}_{j},\ldots ,\mathcal{Z}_{k})\ln \frac{\mathrm{M}_{\mathcal{P}}(\mathcal{X}_{i},\mathcal{Y}_{j},\ldots ,\mathbb{Z}_{k})}{\mu_{X}(\mathcal{X}_{i})\mu_{Y}(\mathcal{Y}_{j})\ldots\mu_{Z}(\mathcal{Z}_{k})} \quad (5.4)\]  

Then \(\mathrm{I}_{X Y\ldots Z}^{\mathcal{P}}\) is, as was \(\{X,Y,\ldots ,Z\}^{\mathcal{P}}\) , a monotone function upon the directed set of partitions (by Theorem 4), and as before we take the directed set limit for our definition:  

\[\mathrm{I}_{X Y\ldots Z}^{\mathcal{P}} = \lim_{\mathcal{P}}\mathrm{I}_{X Y\ldots Z}^{\mathcal{P}} = \sup_{\mathcal{P}}\mathrm{I}_{X Y\ldots Z}^{\mathcal{P}} \quad (5.5)\]  

which is then the information relative to the information measures \(\mu_{X}, \mu_{Y}, \ldots , \nu_{Z}\) .  

Now, for functions \(f, g\) on a directed set the existence of \(\lim f\) and \(\lim g\) is a sufficient condition for the existence of \(\lim (f + g)\) , which is then \(\lim f + \lim g\) , provided that this is not indeterminate. Therefore:  

THEOREM 5. \(\{X, \ldots , Y\} = \lim \{X, \ldots , Y\}^{\mathcal{P}} = \lim \left[\mathrm{I}_{X \ldots Y}^{\mathcal{P}} - \mathrm{I}_{X}^{\mathcal{P}} - \ldots - \mathrm{I}_{Y}^{\mathcal{P}}\right] = \mathrm{I}_{X \ldots Y} - \mathrm{I}_{X} - \ldots - \mathrm{I}_{Y}\) , where the information is taken relative to any information measure for which the expression is not indeterminate. It is sufficient for the validity of the above expression that the basic measures \(\mu_{X}, \ldots , \mu_{Y}\) be such that none of the marginal informations \(\mathrm{I}_{X} \ldots \mathrm{I}_{Y}\) shall be positively infinite.  

The latter statement holds since, because of the general relation \(\mathrm{I}_{X \ldots Y} \geq \mathrm{I}_{X} + \ldots + \mathrm{I}_{Y}\) , the determinateness of the expression is guaranteed so long as all of the \(\mathrm{I}_{X}, \ldots , \mathrm{I}_{Y}\) are \(< +\infty\) .  

Henceforth, unless otherwise noted, we shall understand that information is to be computed with respect to the uniform measure for discrete distributions, and Lebesgue measure for continuous distributions over real

---

numbers. In case of a mixed distribution, with a continuous density \(\mathbf{P}(\mathbf{x}, \mathbf{y}, \ldots , \mathbf{z})\) plus discrete "lumps" \(\mathbf{P}'(x_i, y_j, \ldots , z_k)\) , we shall understand the information measure to be the uniform measure over the discrete range, and Lebesgue measure over the continuous range. These conventions then lead us to the expressions:  

\[\mathrm{I}_{X Y\ldots Z} = \left\{ \begin{array}{l l}{\sum_{\mathrm{i},\ldots ,\mathrm{k}}\mathrm{P}(\mathrm{x}_{\mathrm{i}},\mathrm{y}_{\mathrm{j}},\ldots ,\mathrm{z}_{\mathrm{k}})\ln \mathrm{P}(\mathrm{x}_{\mathrm{i}},\mathrm{y}_{\mathrm{j}},\ldots ,\mathrm{x}_{\mathrm{k}})\Big\} (\mathrm{discrete})}\\ {\int \mathrm{P}(\mathrm{x},\mathrm{y},\ldots ,\mathrm{z})\ln \mathrm{P}(\mathrm{x},\mathrm{y},\ldots ,\mathrm{z})\mathrm{d}\mathrm{x}\mathrm{d}\mathrm{y}\ldots \mathrm{d}\mathrm{z}\Big\} (\mathrm{cont.})}\\ {\sum_{\mathrm{i},\ldots ,\mathrm{k}}\mathrm{P}'(x_{\mathrm{i}},\ldots ,\mathrm{z}_{\mathrm{k}})\ln \mathrm{P}(x_{\mathrm{i}},\ldots ,\mathrm{z}_{\mathrm{k}})\Big\} (\mathrm{mixed})}\\ {+\int \mathrm{P}(\mathrm{x},\ldots ,\mathrm{z})\ln \mathrm{P}(\mathrm{x},\ldots ,\mathrm{z})\mathrm{d}\mathrm{x}\ldots \mathrm{d}\mathrm{z}\Big\} (\mathrm{unlesstherwise noted})} \end{array} \right. \quad (5.6)\]  

The mixed case occurs often in quantum mechanics, for quantities which have both a discrete and continuous spectrum.  

## §6. Example: Information decay in stochastic processes  

As an example illustrating the usefulness of the concept of relative information we shall consider briefly stochastic processes. Suppose that we have a stationary Markov process with a finite number of states \(\mathbf{S}_i\) , and that the process occurs at discrete (integral) times \(1, 2, \ldots , n, \ldots\) , at which times the transition probability from the state \(\mathbf{S}_i\) to the state \(\mathbf{S}_j\) is \(T_{ij}\) . The probabilities \(T_{ij}\) then form what is called a stochastic

---

matrix, i.e., the elements are between 0 and 1, and \(\sum_{i} T_{ij} = 1\) for all i. If at any time k the probability distribution over the states is \(\{P_{i}^{k}\}\) then at the next time the probabilities will be \(P_{j}^{k + 1} = \sum_{i} P_{i}^{k} T_{ij}\) .  

In the special case where the matrix is doubly- stochastic, which means that \(\sum_{i} T_{ij}\) , as well as \(\sum_{j} T_{ij}\) , equals unity, and which amounts to a principle of detailed balancing holding, it is known that the entropy of a probability distribution over the states, defined as \(H = - \sum_{i} P_{i} \ln P_{i}\) , is a monotone increasing function of the time. This entropy is, however, simply the negative of the information relative to the uniform measure.  

One can extend this result to more general stochastic processes only if one uses the more general definition of relative information. For an arbitrary stationary process the choice of an information measure which is stationary, i.e., for which  

\[\mathbf{a}_{\mathbf{j}} = \sum_{i} \mathbf{a}_{\mathbf{i}} T_{\mathbf{i}\mathbf{j}} \quad (\mathbf{all} \mathbf{j}) \quad (6.1)\]  

leads to the desired result. In this case the relative information,  

\[\mathrm{I} = \sum_{i} \mathrm{P}_{i} \ln \frac{\mathrm{P}_{i}}{\mathrm{a}_{i}}, \quad (6.2)\]  

is a monotone decreasing function of time and constitutes a suitable basis for the definition of the entropy \(H = - I\) . Note that this definition leads to the previous result for doubly- stochastic processes, since the uniform measure, \(\mathbf{a}_{i} = 1\) (all i), is obviously stationary in this case.  

One can furthermore drop the requirement that the stochastic process be stationary, and even allow that there are completely different sets of states, \(\{S_{i}^{n}\}\) , at each time \(n\) , so that the process is now given by a sequence of matrices \(T_{ij}^{n}\) representing the transition probability at time \(n\) from state \(S_{i}^{n}\) to state \(S_{j}^{n + 1}\) . In this case probability distributions change according to:

---

\[\mathrm{P_{j}^{n + 1} = \sum_{i}P_{i}^{n}T_{ij}^{n}.} \quad (6.3)\]  

If we then choose any time- dependent information measure which satisfies the relations:  

\[\mathrm{a_{j}^{n + 1} = \sum a_{i}^{n}T_{ij}^{n}\quad (all j,n),} \quad (6.4)\]  

then the information of a probability distribution is again monotone decreasing with time. (Proof in Appendix I.)  

All of these results are easily extended to the continuous case, and we see that the concept of relative information allows us to define entropy for quite general stochastic processes.  

\(\S 7\) . Example: Conservation of information in classical mechanics  

As a second illustrative example we consider briefly the classical mechanics of a group of particles. The system at any instant is represented by a point, \((x^{1},y^{1},z^{1},p_{x}^{1},p_{y}^{1},p_{z}^{1},\dots ,x^{n},y^{n},z^{n},p_{x}^{n},p_{y}^{n},p_{z}^{n})\) , in the phase space of all position and momentum coordinates. The natural motion of the system then carries each point into another, defining a continuous transformation of the phase space into itself. According to Liouville's theorem the measure of a set of points of the phase space is invariant under this transformation. This invariance of measure implies that if we begin with a probability distribution over the phase space, rather than a single point, the total information  

\[I_{\mathrm{total}} = I_{X}^{1}Y^{1}Z^{1}P_{x}^{1}P_{y}^{1}P_{z}^{1}\dots x^{n}Y^{n}Z^{n}P_{x}^{n}P_{y}^{n}P_{z}^{n}, \quad (7.1)\]  

which is the information of the joint distribution for all positions and momenta, remains constant in time.

---

In order to see that the total information is conserved, consider any partition \(\mathcal{P}\) of the phase space at one time, \(t_0\) , with its information relative to the phase space measure, \(\Gamma^{\mathcal{P}}(t_0)\) . At a later time \(t_1\) a partition \(\mathcal{P}'\) , into the image sets of \(\mathcal{P}\) under the mapping of the space into itself, is induced, for which the probabilities for the sets of \(\mathcal{P}'\) are the same as those of the corresponding sets of \(\mathcal{P}\) , and furthermore for which the measures are the same, by Liouville's theorem. Thus corresponding to each partition \(\mathcal{P}\) at time \(t_0\) with information \(\Gamma^{\mathcal{P}}(t_0)\) , there is a partition \(\mathcal{P}'\) at time \(t_1\) with information \(\Gamma^{\mathcal{P}'}(t_1)\) , which is the same:  

\[\Gamma^{\mathcal{P}'}(t_1) = \Gamma^{\mathcal{P}}(t_0). \quad (7.2)\]  

Due to the correspondence of the \(\mathcal{P}\) 's and \(\mathcal{P}'\) 's the supremums of each over all partitions must be equal, and by (5.5) we have proved that  

\[I_{\mathrm{total}}(t_1) = I_{\mathrm{total}}(t_0), \quad (7.3)\]  

and the total information is conserved.  

Now it is known that the individual (marginal) position and momentum distributions tend to decay, except for rare fluctuations, into the uniform and Maxwellian distributions respectively, for which the classical entropy is a maximum. This entropy is, however, except for the factor of Boltzmann's constant, simply the negative of the marginal information  

\[I_{\mathrm{marginal}} = I_{X_1} + I_{Y_1} + I_{Z_1} + \dots + I_{P_n} + I_{P_n} + I_{P_n}, \quad (7.4)\]  

which thus tends towards a minimum. But this decay of marginal information is exactly compensated by an increase of the total correlation information  

\[\{total\} = I_{\mathrm{total}} - I_{\mathrm{marginal}}, \quad (7.5)\]  

since the total information remains constant. Therefore, if one were to define the total entropy to be the negative of the total information, one could replace the usual second law of thermodynamics by a law of

---

conservation of total entropy, where the increase in the standard (marginal) entropy is exactly compensated by a (negative) correlation entropy. The usual second law then results simply from our renunciation of all correlation knowledge (stosszahlansatz), and not from any intrinsic behavior of classical systems. The situation for classical mechanics is thus in sharp contrast to that of stochastic processes, which are intrinsically irreversible.

---

## III. QUANTUM MECHANICS  

Having mathematically formulated the ideas of information and correlation for probability distributions, we turn to the field of quantum mechanics. In this chapter we assume that the states of physical systems are represented by points in a Hilbert space, and that the time dependence of the state of an isolated system is governed by a linear wave equation.  

It is well known that state functions lead to distributions over eigenvalues of Hermitian operators (square amplitudes of the expansion coefficients of the state in terms of the basis consisting of eigenfunctions of the operator) which have the mathematical properties of probability distributions (non- negative and normalized). The standard interpretation of quantum mechanics regards these distributions as actually giving the probabilities that the various eigenvalues of the operator will be observed, when a measurement represented by the operator is performed.  

A feature of great importance to our interpretation is the fact that a state function of a composite system leads to joint distributions over subsystem quantities, rather than independent subsystem distributions, i.e., the quantities in different subsystems may be correlated with one another. The first section of this chapter is accordingly devoted to the development of the formalism of composite systems, and the connection of composite system states and their derived joint distributions with the various possible subsystem conditional and marginal distributions. We shall see that there exist relative state functions which correctly give the conditional distributions for all subsystem operators, while marginal distributions can not generally be represented by state functions, but only by density matrices.  

In Section 2 the concepts of information and correlation, developed in the preceding chapter, are applied to quantum mechanics, by defining

---

information and correlation for operators on systems with prescribed states. It is also shown that for composite systems there exists a quantity which can be thought of as the fundamental correlation between subsystems, and a closely related canonical representation of the composite system state. In addition, a stronger form of the uncertainty principle, phrased in information language, is indicated.  

The third section takes up the question of measurement in quantum mechanics, viewed as a correlation producing interaction between physical systems. A simple example of such a measurement is given and discussed. Finally some general consequences of the superposition principle are considered.  

It is convenient at this point to introduce some notational conventions. We shall be concerned with points \(\psi\) in a Hilbert space \(\mathcal{H}\) , with scalar product \((\psi_{1}, \psi_{2})\) . A state is a point \(\psi\) for which \((\psi, \psi) = 1\) . For any linear operator \(A\) we define a functional, \(< A > \psi\) , called the expectation of \(A\) for \(\psi\) , to be:  

\[< A > \psi = (\psi , A \psi) .\]  

A class of operators of particular interest is the class of projection operators. The operator \([\phi ]\) , called the projection on \(\phi\) , is defined through:  

\[[\phi ]\psi = (\phi ,\psi)\phi .\]  

For a complete orthonormal set \(\{\phi_{i}\}\) and a state \(\psi\) we define a square- amplitude distribution, \(\mathbf{P}_{i}\) , called the distribution of \(\psi\) over \(\{\phi_{i}\}\) through:  

\[\mathbf{P}_{i} = |(\phi_{i}, \psi)|^{2} = < [\phi_{i}] > \psi .\]  

In the probabilistic interpretation this distribution represents the probability distribution over the results of a measurement with eigenstates \(\phi_{i}\) , performed upon a system in the state \(\psi\) . (Hereafter when referring to the probabilistic interpretation we shall say briefly "the probability that the system will be found in \(\phi_{i}\) ", rather than the more cumbersome phrase "the probability that the measurement of a quantity \(B\) , with eigenfunc-

---

tions \(\{\phi_{i}\} ,\) shall yield the eigenvalue corresponding to \(\phi_{i},^{\prime \prime}\) which is meant.)  

For two Hilbert spaces \(\mathcal{H}_{1}\) and \(\mathcal{H}_{2}\) , we form the direct product Hilbert space \(\mathcal{H}_{3} = \mathcal{H}_{1}\otimes \mathcal{H}_{2}\) (tensor product) which is taken to be the space of all possible sums of formal products of points of \(\mathcal{H}_{1}\) and \(\mathcal{H}_{2}\) , i.e., the elements of \(\mathcal{H}_{3}\) are those of the form \(\sum_{i}\mathbf{a}_{i}\xi_{i}\eta_{i}\) where \(\xi_{i}\in \mathcal{H}_{1}\) and \(\eta_{i}\in \mathcal{H}_{2}\) . The scalar product in \(\mathcal{H}_{3}\) is taken to be \(\left(\sum_{i}\mathbf{a}_{i}\xi_{i}\eta_{i},\sum_{j}\mathbf{b}_{j}\xi_{j}\eta_{j}\right) =\) \(\sum_{i,j}\mathbf{a}_{i}^{*}\mathbf{b}_{j}(\xi_{i},\xi_{j})(\eta_{i},\eta_{j})\) . It is then easily seen that if \(\{\xi_{i}\}\) and \(\{\eta_{i}\}\) form complete orthonormal sets in \(\mathcal{H}_{1}\) and \(\mathcal{H}_{2}\) respectively, then the set of all formal products \(\{\xi_{i}\eta_{j}\}\) is a complete orthonormal set in \(\mathcal{H}_{3}\) . For any pair of operators \(A,B\) , in \(\mathcal{H}_{1}\) and \(\mathcal{H}_{2}\) there corresponds an operator \(\mathbf{C} = \mathbf{A}\otimes \mathbf{B}\) , the direct product of \(A\) and \(B\) , in \(\mathcal{H}_{3}\) , which can be defined by its effect on the elements \(\xi_{i}\eta_{j}\) of \(\mathcal{H}_{3}\) :  

\[\mathbf{C}\xi_{i}\eta_{j} = \mathbf{A}\otimes \mathbf{B}\xi_{i}\eta_{j} = (\mathbf{A}\xi_{i})(\mathbf{B}\eta_{j}).\]  

## \(\S 1\) . Composite systems  

It is well known that if the states of a pair of systems \(S_{1}\) and \(S_{2}\) , are represented by points in Hilbert spaces \(\mathcal{H}_{1}\) and \(\mathcal{H}_{2}\) respectively, then the states of the composite system \(S = S_{1} + S_{2}\) (the two systems \(S_{1}\) and \(S_{2}\) regarded as a single system \(S\) ) are represented correctly by points of the direct product \(\mathcal{H}_{1}\otimes \mathcal{H}_{2}\) . This fact has far reaching consequences which we wish to investigate in some detail. Thus if \(\{\xi_{i}\}\) is a complete orthonormal set for \(\mathcal{H}_{1}\) , and \(\{\eta_{j}\}\) for \(\mathcal{H}_{2}\) , the general state of \(S = S_{1} + S_{2}\) has the form:  

\[\psi^{S} = \sum_{i j}\mathbf{a}_{i j}\xi_{i}\eta_{j}\quad \left(\sum_{i j}\mathbf{a}_{i j}^{*}\mathbf{a}_{i j} = 1\right). \quad (1.1)\]

---

In this case we shall call \(\mathbf{P}_{\mathrm{ij}} = \mathbf{a}_{\mathrm{ij}}^* \mathbf{a}_{\mathrm{ij}}\) the joint square-amplitude distribution of \(\psi^S\) over \(\{\xi_i\}\) and \(\{\eta_j\}\) . In the standard probabilistic interpretation \(\mathbf{a}_{\mathrm{ij}}^* \mathbf{a}_{\mathrm{ij}}\) represents the joint probability that \(S_1\) will be found in the state \(\xi_i\) and \(S_2\) will be found in the state \(\eta_i\) . Following the probabilistic model we now derive some distributions from the state \(\psi^S\) . Let \(A\) be a Hermitian operator in \(S_1\) with eigenfunctions \(\phi_i\) and eigenvalues \(\lambda_i\) , and \(B\) an operator in \(S_2\) with eigenfunctions \(\theta_j\) and eigenvalues \(\mu_j\) . Then the joint distribution of \(\psi^S\) over \(\{\phi_i\}\) and \(\{\phi_j\}\) , \(P_{\mathrm{ij}}\) , is:  

\[\mathrm{P_{ij} = P(\phi_i and \theta_j) = |(\phi_i\theta_j,\psi^S)|^2.} \quad (1.2)\]  

The marginal distributions, of \(\psi^S\) over \(\{\phi_i\}\) and of \(\psi^S\) over \(\{\phi_j\}\) , are:  

\[\begin{array}{l}{\mathrm{P}_{\mathrm{i}} = \mathrm{P}(\phi_{\mathrm{i}}) = \sum_{\mathrm{j}}\mathrm{P}_{\mathrm{ij}} = \sum_{\mathrm{j}}|(\phi_{\mathrm{i}}\theta_{\mathrm{j}},\psi^{\mathrm{S}})|^{2},}\\ {\mathrm{P}_{\mathrm{j}} = \mathrm{P}(\theta_{\mathrm{j}}) = \sum_{\mathrm{i}}\mathrm{P}_{\mathrm{ij}} = \sum_{\mathrm{i}}|(\phi_{\mathrm{i}}\theta_{\mathrm{j}},\psi^{\mathrm{S}})|^{\mathrm{2}},} \end{array} \quad (1.3)\]  

and the conditional distributions \(\mathbf{P}_{\mathrm{i}}^{\mathrm{j}}\) and \(\mathbf{P}_{\mathrm{j}}^{\mathrm{j}}\) are:  

\[\begin{array}{l}{\mathrm{P}_{\mathrm{i}}^{\mathrm{j}} = \mathrm{P}(\phi_{\mathrm{i}}\mathrm{~conditioned~on~}\phi_{\mathrm{j}}) = \frac{\mathrm{P}_{\mathrm{ij}}}{\mathrm{P}_{\mathrm{j}}},}\\ {\mathrm{P}_{\mathrm{j}}^{\mathrm{j}} = \mathrm{P}(\phi_{\mathrm{j}}\mathrm{~conditioned~on~}\phi_{\mathrm{i}}) = \frac{\mathrm{P}_{\mathrm{ij}}}{\mathrm{P}_{\mathrm{i}}}.} \end{array} \quad (1.4)\]  

We now define the conditional expectation of an operator \(A\) on \(S_1\) , conditioned on \(\theta_j\) in \(S_2\) , denoted by \(\exp^{\theta_j}[A]\) , to be:  

\[\begin{array}{r l} & {\mathrm{Exp}^{\theta_{j}}[A] = \sum_{\mathrm{i}}\lambda_{\mathrm{i}}\mathrm{P}_{\mathrm{i}}^{\mathrm{j}} = (1 / \mathrm{P}_{\mathrm{j}})\sum_{\mathrm{i}}\mathrm{P}_{\mathrm{i j}}\lambda_{\mathrm{i}}}\\ & {\qquad = (1 / \mathrm{P}_{\mathrm{j}})\sum_{\mathrm{i}}\lambda_{\mathrm{i}}|(\phi_{\mathrm{i}}\theta_{\mathrm{j}},\psi^{\mathrm{s}})|^{2}}\\ & {\qquad = (1 / \mathrm{P}_{\mathrm{j}})\sum_{\mathrm{i}}|(\phi_{\mathrm{i}}\theta_{\mathrm{j}},\psi^{\mathsf{S}})|^{2}(\phi_{\mathrm{i}},\mathrm{A}\phi_{\mathrm{i}}),} \end{array} \quad (1.5)\]

---

and we define the marginal expectation of A on \(S_{1}\) to be: 

\[(1.6) \quad \text{Exp} [A] = \sum_{i} P_{i} \lambda_{i} = \sum_{ij} \lambda_{i} P_{ij} = \sum_{ij} |(\phi_{i} \theta_{j}, \psi S)|^{2} (\phi_{i}, A \phi_{i})\]

We shall now introduce projection operators to get more convenient forms of the conditional and marginal expectations, which will also exhibit more clearly the degree of dependence of these quantities upon the chosen basis \(\{\phi_{i} \theta_{j}\}\). Let the operators \(\{\phi_{i}\}\) and \(\{\phi_{j}\}\) be the projections on \(\phi_{i}\) in \(S_{1}\) and \(\phi_{j}\) in \(S_{2}\) respectively, and let \(I^{1}\) and \(I^{2}\) be the identity operators in \(S_{1}\) and \(S_{2}\). Then, making use of the identity \(\psi S = \sum_{ij} (\phi_{i} \theta_{j}, \psi S) \phi_{i} \theta_{j}\) for any complete orthonormal set \(\{\phi_{i} \theta_{j}\}\), we have: 

\[(1.7) <[\phi_{i}][\theta_{j}]>\psi S = (\psi S, [\phi_{i}][\theta_{j}]\psi S) =\]

\[(\sum_{kl} (\phi_{k} \theta_{l}, \psi S) \phi_{k} \theta_{l}, [\phi_{i}][\theta_{j}] \sum_{mn} (\phi_{m} \theta_{n}, \psi S) \phi_{m} \theta_{n}) \\
= \sum_{klmn} (\phi_{k} \theta_{l}, \psi S)^{*} (\phi_{m} \theta_{n}, \psi S) \delta_{km} \delta_{ln} \delta_{im} \delta_{jn} \\
= (\phi_{i} \theta_{j}, \psi S)^{*} (\phi_{i} \theta_{j}, \psi S) = P_{ij},\]

so that the joint distribution is given simply by \(<[\phi_{i}][\phi_{j}]>\psi S\). 

For the marginal distribution we have: 

\[(1.8) P_{i} = \sum_{j} P_{ij} = \sum_{j} <[\phi_{i}][\theta_{j}]>\psi S = <[\phi_{i}](\sum_{j} [\theta_{j}])>\psi S = <[\phi_{i}]I^{2}>\psi S,\]

and we see that the marginal distribution over the \(\phi_{i}\) is independent of the set \(\{\theta_{j}\}\) chosen in \(S_{2}\). This result has the consequence in the ordinary interpretation that the expected outcome of measurement in one subsystem of a composite system is not influenced by the choice of quantity to be measured in the other subsystem. This expectation is, in fact, the expectation for the case in which no measurement at all (identity operator) is performed in the other subsystem. Thus no measurement in \(S_{2}\) can

---

affect the expected outcome of a measurement in \(S_{1}\) , so long as the result of any \(S_{2}\) measurement remains unknown. The case is quite different, however, if this result is known, and we must turn to the conditional distributions and expectations in such a case.  

We now introduce the concept of a relative state- function, which will play a central role in our interpretation of pure wave mechanics. Consider a composite system \(S = S_{1} + S_{2}\) in the state \(\psi^{S}\) . To every state \(\eta\) of \(S_{2}\) we associate a state of \(S_{1}\) , \(\psi_{\mathrm{rel}}^{\eta}\) , called the relative state in \(S_{1}\) for \(\eta\) in \(S_{2}\) , through:  

\[\mathrm{DEFINITION.} \psi_{\mathrm{rel}}^{\eta} = \mathrm{N} \sum_{\mathrm{i}} (\phi_{\mathrm{i}} \eta , \psi^{S}) \phi_{\mathrm{i}}, \quad (1.9)\]  

where \(\{\phi_{\mathrm{i}}\}\) is any complete orthonormal set in \(S_{1}\) and \(N\) is a normalization constant. \(^{2}\)  

The first property of \(\psi_{\mathrm{rel}}^{\eta}\) is its uniqueness, \(^{3}\) i.e., its dependence upon the choice of the basis \(\{\phi_{\mathrm{i}}\}\) is only apparent. To prove this, choose another basis \(\{\xi_{\mathrm{k}}\}\) , with \(\phi_{\mathrm{i}} = \sum_{\mathrm{k}} b_{\mathrm{ik}} \xi_{\mathrm{k}}\) . Then \(\sum_{\mathrm{i}} b_{\mathrm{ij}}^{*} b_{\mathrm{ik}} = \delta_{\mathrm{jk}}\) , and:  

\[\sum_{\mathrm{i}}(\phi_{\mathrm{i}}\eta ,\psi^{S})\phi_{\mathrm{i}} = \sum_{\mathrm{i}}\left(\sum_{\mathrm{j}}b_{\mathrm{ij}}\xi_{\mathrm{j}}\eta ,\psi^{S}\right)\left(\sum_{\mathrm{k}}b_{\mathrm{ik}}\xi_{\mathrm{k}}\right)\] \[\qquad = \sum_{\mathrm{jk}}\left(\sum_{\mathrm{i}}b_{\mathrm{ij}}^{*}b_{\mathrm{ik}}\right)\left(\xi_{\mathrm{j}}\eta ,\psi^{S}\xi_{\mathrm{k}} = \sum_{\mathrm{jk}}\delta_{\mathrm{jk}}\left(\xi_{\mathrm{j}}\eta ,\psi^{S}\right)\xi_{\mathrm{k}}\right.\] \[\qquad = \sum_{\mathrm{k}}\left(\xi_{\mathrm{k}}\eta ,\psi^{S}\right)\xi_{\mathrm{k}}.\]  

The second property of the relative state, which justifies its name, is that \(\psi_{\mathrm{rel}}^{\theta_{\mathrm{j}}}\) correctly gives the conditional expectations of all operators in \(S_{1}\) , conditioned by the state \(\theta_{\mathrm{j}}\) in \(S_{2}\) . As before let \(A\) be an operator in \(S_{1}\) with eigenstates \(\phi_{\mathrm{i}}\) and eigenvalues \(\lambda_{\mathrm{i}}\) . Then:

---

\[< \mathsf{A} > \psi_{\mathrm{rel}}^{0} = \left(\psi_{\mathrm{rel}}^{0},\mathsf{A}\psi_{\mathrm{rel}}^{0}\right)\] \[\qquad = \left(\mathsf{N}\sum_{\mathrm{i}}\left(\phi_{\mathrm{i}}\theta_{\mathrm{j}},\psi^{\mathrm{S}}\right)\phi_{\mathrm{i}},\mathsf{A}\mathsf{N}\sum_{\mathrm{im}}\left(\phi_{\mathrm{m}}\theta_{\mathrm{j}},\psi^{\mathrm{S}}\right)\phi_{\mathrm{m}}\right)\] \[\qquad = \mathsf{N}^{2}\sum_{\mathrm{im}}\left(\phi_{\mathrm{i}}\theta_{\mathrm{j}},\psi^{\mathrm{S}}\right)^{*}\left(\phi_{\mathrm{m}}\theta_{\mathrm{j}},\psi^{\mathrm{S}}\right)\lambda_{\mathrm{m}}\delta_{\mathrm{im}}\] \[\qquad = \mathsf{N}^{2}\sum_{\mathrm{i}}\lambda_{\mathrm{i}}\mathsf{P}_{\mathrm{ij}}.\]  

At this point the normalizer \(\mathsf{N}^{2}\) can be conveniently evaluated by using (1.10) to compute: \(< \mathsf{I}^{1} > \psi_{\mathrm{rel}}^{0} = \mathsf{N}^{2}\sum_{\mathrm{i}}1\mathsf{P}_{\mathrm{ij}} = \mathsf{N}^{2}\mathsf{P}_{\mathrm{j}} = 1\) , so that  

\[\mathsf{N}^{2} = 1 / \mathsf{P}_{\mathrm{j}}. \quad (1.11)\]  

Substitution of (1.11) in (1.10) yields:  

\[\langle \mathsf{A} > \psi_{\mathrm{rel}}^{0} = (1 / \mathsf{P}_{\mathrm{j}})\sum_{\mathrm{i}}\lambda_{\mathrm{i}}\mathsf{P}_{\mathrm{ij}} = \sum_{\mathrm{i}}\lambda_{\mathrm{i}}\mathsf{P}_{\mathrm{j}}^{\mathrm{i}} = \mathsf{Exp}^{\mathrm{j}}[\mathsf{A}], \quad (1.12)\]  

and we see that the conditional expectations of operators are given by the relative states. (This includes, of course, the conditional distributions themselves, since they may be obtained as expectations of projection operators.)  

An important representation of a composite system state \(\psi^{\mathrm{S}}\) , in terms of an orthonormal set \(\{\theta_{\mathrm{j}}\}\) in one subsystem \(S_{2}\) and the set of relative states \(\left\{\psi_{\mathrm{rel}}^{0}\right\}\) in \(S_{1}\) is:  

\[\psi^{\mathrm{S}} = \sum_{\mathrm{ij}}\left(\phi_{\mathrm{i}}\theta_{\mathrm{j}},\psi^{\mathrm{S}}\right)_{\mathrm{i}}\phi_{\mathrm{i}}\theta_{\mathrm{j}} = \sum_{\mathrm{j}}\left(\sum_{\mathrm{i}}\left(\phi_{\mathrm{i}}\theta_{\mathrm{j}},\psi^{\prime}\right)_{\mathrm{i}}\phi_{\mathrm{i}}\right)\theta_{\mathrm{j}}\] \[\qquad = \sum_{\mathrm{j}}\frac{1}{\mathrm{N}_{\mathrm{j}}}\left[\mathrm{N}_{\mathrm{j}}\sum_{\mathrm{i}}\left(\phi_{\mathrm{i}}\theta_{\mathrm{j}},\psi^{\ast}\right)_{\mathrm{i}}\theta_{\mathrm{j}}\right]\] \[\qquad = \sum_{\mathrm{j}}\frac{1}{\mathrm{N}_{\mathrm{j}}}\psi_{\mathrm{rel}}^{0}\theta_{\mathrm{j}},\mathrm{~where~}1 / \mathrm{N}_{\mathrm{j}}^{2} = \mathrm{P}_{\mathrm{j}} = < \mathrm{I}^{1}[\theta_{\mathrm{j}}] > \psi^{\mathrm{S}}\]

---

Thus, for any orthonormal set in one subsystem, the state of the composite system is a single superposition of elements consisting of a state of the given set and its relative state in the other subsystem. (The relative states, however, are not necessarily orthogonal.) We notice further that a particular element, \(\psi_{\mathrm{rel}}^{\theta_{\mathrm{j}}}\theta_{\mathrm{j}}\) , is quite independent of the choice of basis \(\{\theta_{\mathrm{k}}\}\) , \(k \neq j\) , for the orthogonal space of \(\theta_{\mathrm{j}}\) , since \(\psi_{\mathrm{rel}}^{\theta_{\mathrm{j}}}\) depends only on \(\theta_{\mathrm{j}}\) and not on the other \(\theta_{\mathrm{k}}\) for \(k \neq j\) . We remark at this point that the ambiguity in the relative state which arises when \(\sum_{i} (\phi_{i} \theta_{j}, \psi^{S}) \phi_{i} = 0\) (see p. 38) is unimportant for this representation, since although any state \(\psi_{\mathrm{rel}}^{\theta_{\mathrm{j}}}\) can be regarded as the relative state in this case, the term \(\psi_{\mathrm{rel}}^{\theta_{\mathrm{j}}}\theta_{\mathrm{j}}\) will occur in (1.13) with coefficient zero. 

Now that we have found subsystem states which correctly give conditional expectations, we might inquire whether there exist subsystem states which give marginal expectations. The answer is, unfortunately, no. Let us compute the marginal expectation of \(A\) in \(S_1\) using the representation (1.13): 

\[
\begin{align*}
(1.14) \quad \text{Exp} [A] &= <A I^2 > \psi^S = \left( \sum_j \frac{1}{N_j} \psi_{\text{rel}}^{\theta_j} \theta_j, A I^2 \sum_k \frac{1}{N_k} \psi_{\text{rel}}^{\theta_k} \theta_k \right) \\
&= \sum_{jk} \frac{1}{N_j N_k} \left( \psi_{\text{rel}}^{\theta_j} A \psi_{\text{rel}}^{\theta_j} \right) \delta_{jk} \\
&= \sum_j \frac{1}{N_j^2} \left( \psi_{\text{rel}}^{\theta_j} A \psi_{\textrel}^{\theta_j} \right) = \sum_j P_j < A > \psi_{\text{rel}}^{\theta_j}.
\end{align*}
\]

Now suppose that there exists a state in \(S_1, \psi'\), which correctly gives the marginal expectation (1.14) for all operators \(A\) (i.e., such that \(\text{Exp}[A] = <A > \psi'\) for all \(A\)). One such operator is \([\psi']\), the projection on \(\psi'\), for which \(<[\psi'] > \psi' = 1\). But, from (1.14) we have that \(\sum_j P_j < \psi' > \psi_{\text{rel}}^{\theta_j}\), which is \(<1\) unless, for all \(j, P_j = 0\) or \(\psi_{\text{rel}}^{\theta_j} = \psi'\), a condition which is not generally true. Therefore there exists in general no state for \(S_1\) which correctly gives the marginal expectations for all operators in \(S_1\).

---

However, even though there is generally no single state describing marginal expectations, we see that there is always a mixture of states, namely the states \(\psi_{\mathrm{rel}}^{\theta_{j}}\) weighted with \(\mathbf{P}_{\mathbf{j}}\) , which does yield the correct expectations. The distinction between a mixture, \(\mathbf{M}\) , of states \(\phi_{\mathbf{i}}\) , weighted by \(\mathbf{P}_{\mathbf{i}}\) , and a pure state \(\psi\) which is a superposition, \(\psi = \sum \mathbf{a}_{\mathbf{i}}\phi_{\mathbf{i}}\) , is that there are no interference phenomena between the various states of a mixture. The expectation of an operator \(\mathbf{A}\) for the mixture is \(\mathrm{Exp}^{\mathrm{M}}[\mathbf{A}] = \sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}< \mathbf{A} > \phi_{\mathbf{i}} = \sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}(\phi_{\mathbf{i}},\mathbf{A}\phi_{\mathbf{i}})\) , while the expectation for the pure state \(\psi\) is \(< \mathbf{A} > \psi = \left(\sum_{\mathbf{i}}\mathbf{a}_{\mathbf{i}}\phi_{\mathbf{i}},\mathbf{A}\sum_{\mathbf{j}}\mathbf{a}_{\mathbf{j}}\phi_{\mathbf{j}}\right) = \sum_{\mathbf{i}\mathbf{j}}\mathbf{a}_{\mathbf{i}}^{*}\mathbf{a}_{\mathbf{j}}(\phi_{\mathbf{i}},\mathbf{A}\phi_{\mathbf{j}})\) , which is not the same as that of the mixture with weights \(\mathbf{P}_{\mathbf{i}} = \mathbf{a}_{\mathbf{i}}^{*}\mathbf{a}_{\mathbf{i}}\) , due to the presence of the interference terms \((\phi_{\mathbf{i}},\mathbf{A}\phi_{\mathbf{j}})\) for \(\mathbf{j} \neq \mathbf{i}\) .  

It is convenient to represent such a mixture by a density matrix, \(^{4}\) \(\rho\) . If the mixture consists of the states \(\psi_{\mathbf{j}}\) weighted by \(\mathbf{P}_{\mathbf{j}}\) , and if we are working in a basis consisting of the complete orthonormal set \(\{\phi_{\mathbf{i}}\}\) , where \(\psi_{\mathbf{j}} = \sum_{\mathbf{i}}\mathbf{a}_{\mathbf{i}}^{\mathbf{j}}\phi_{\mathbf{i}}\) , then we define the elements of the density matrix for the mixture to be:  

\[\rho_{\mathbf{k}\ell} = \sum_{\mathbf{j}}\mathbf{P}_{\mathbf{j}}\mathbf{a}_{\mathbf{k}}^{\mathbf{j}*}\mathbf{a}_{\mathbf{k}}^{\mathbf{j}}\quad (\mathbf{a}_{\mathbf{i}}^{\mathbf{j}} = (\phi_{\mathbf{i}},\psi_{\mathbf{j}}))~. \quad (1.15)\]  

Then if \(\mathbf{A}\) is any operator, with matrix representation \(\mathbf{A}_{\mathbf{i}\ell} = (\phi_{\mathbf{i}},\mathbf{A}\phi_{\ell})\) in the chosen basis, its expectation for the mixture is:  

\[\begin{array}{r l} & {\mathrm{Exp}^{\mathrm{M}}[\mathbf{A}] = \sum_{\mathbf{j}}\mathbf{P}_{\mathbf{j}}(\psi_{\mathbf{j}},\mathbf{A}\psi_{\mathbf{j}}) = \sum_{\mathbf{j}}\mathbf{P}_{\mathbf{j}}\left[\sum_{\mathbf{i}\ell}\mathbf{a}_{\mathbf{i}}^{\mathbf{j}*}\mathbf{a}_{\mathbf{j}}^{\mathbf{j}}(\phi_{\mathbf{i}},\mathbf{A}\phi_{\ell})\right]}\\ & {\qquad = \sum_{\mathbf{i}\ell}\left(\sum_{\mathbf{j}}\mathbf{P}_{\mathbf{j}}\mathbf{a}_{\mathbf{i}}^{\mathbf{j}*}\mathbf{a}_{\mathbf{j}}^{\mathbf{j}}\right)(\phi_{\mathbf{i}},\mathbf{A}\phi_{\ell}) = \sum_{\mathbf{i},\ell}\rho_{\ell \mathbf{i}}\mathbf{A}_{\mathbf{i}\ell}}\\ & {\qquad = \mathrm{Trace}(\rho \mathbf{A}).} \end{array} \quad (1.16)\]

---

Therefore any mixture is adequately represented by a density matrix. \(^{5}\) Note also that \(\rho_{kl}^{*} = \rho_{lk}\) , so that \(\rho\) is Hermitian. 

Let us now find the density matrices \(\rho^1\) and \(\rho^2\) for the subsystems \(S_1\) and \(S_2\) of a system \(S = S_1 + S_2\) in the state \(\psi^S\). Furthermore, let us choose the orthonormal bases \(\{\xi_i\}\) and \(\{\eta_j\}\) in \(S_1\) and \(S_2\) respectively, and let \(A\) be an operator in \(S_1\), \(B\) an operator in \(S_2\). Then: 

\[
\begin{align*}
(1.17) & \exp[A] = <A|^2 > \psi^S = \left( \sum_{ij} (\xi_i \eta_j, \psi^S) \xi_i \eta_j, A| \sum_{\ell m} (\xi_\ell \eta_m, \psi^S) \xi_\ell \eta_m \right) \\
& = \sum_{ij \ell m} (\xi_i \eta_j, \psi^S)^* (\xi_\ell \eta_m, \psi^S) (\xi_i, A \xi_\ell) (\eta_j, \eta_m) \\
& = \sum_{ij} \left[ \sum_j (\xi_i \eta_j, \psi^S)^* (\xi_\ell \eta_j, \psi^S) \right] (\xi_i, A \xi_\ell) \\
& = \text{Trace } (\rho^1 A),
\end{align*}
\]

where we have defined \(\rho^1\) in the \(\{\xi_i\}\) basis to be: 

\[
(1.18) \quad \rho_{\ell i}^1 = \sum_j (\xi_i \eta_j, \psi^S)^* (\xi_\eta \eta_j, \psi^S).
\]

In a similar fashion we find that \(\rho^2\) is given, in the \(\{\eta_j\}\) basis, by: 

\[
(1.19) \quad \rho_{\text{mn}}^2 = \sum_i (\xi_i \eta_n, \psi^S)^* (\xi_i \eta_m, \psi^S).
\]

It can be easily shown that here again the dependence of \(\rho^1\) upon the choice of basis \(\{\eta_j\}\) in \(S_2\), and of \(\rho^2\) upon \(\{\xi_i\}\), is only apparent.

---

In summary, we have seen in this section that a state of a composite system leads to joint distributions over subsystem quantities which are generally not independent. Conditional distributions and expectations for subsystems are obtained from relative states, and subsystem marginal distributions and expectations are given by density matrices.  

There does not, in general, exist anything like a single state for one subsystem of a composite system. That is, subsystems do not possess states independent of the states of the remainder of the system, so that the subsystem states are generally correlated. One can arbitrarily choose a state for one subsystem, and be led to the relative state for the other subsystem. Thus we are faced with a fundamental relativity of states, which is implied by the formalism of composite systems. It is meaningless to ask the absolute state of a subsystem - one can only ask the state relative to a given state of the remainder of the system.  

## \(\S 2\) . Information and correlation in quantum mechanics  

We wish to be able to discuss information and correlation for Hermitian operators \(\mathbf{A}, \mathbf{B}, \ldots\) , with respect to a state function \(\psi\) . These quantities are to be computed, through the formulas of the preceding chapter, from the square amplitudes of the coefficients of the expansion of \(\psi\) in terms of the eigenstates of the operators.  

We have already seen (p. 34) that a state \(\psi\) and an orthonormal basis \(\{\phi_{i}\}\) leads to a square amplitude distribution of \(\psi\) over the set \(\{\phi_{i}\}\) :  

\[\mathrm{P}_{\mathrm{i}} = |(\phi_{\mathrm{i}},\psi)|^{2} = < [\phi_{\mathrm{i}}] > \psi , \quad (2.1)\]  

so that we can define the information of the basis \(\{\phi_{i}\}\) for the state \(\psi\) , \(\mathrm{I}_{\{\phi_{i}\}}(\psi)\) , to be simply the information of this distribution relative to the uniform measure:  

\[\mathrm{I}_{\{\phi_{i}\}}(\psi) = \sum_{\mathrm{i}}\mathrm{P}_{\mathrm{i}}\ln \mathrm{P}_{\mathrm{i}} = \sum_{\mathrm{i}}|(\phi_{\mathrm{i}},\psi)|^{2}\ln |(\phi_{\mathrm{i}},\psi)|^{2}. \quad (2.2)\]

---

We define the information of an operator A, for the state \(\psi\) , \(I_A(\psi)\) , to be the information in the square amplitude distribution over its eigenvalues, i.e., the information of the probability distribution over the results of a determination of A which is prescribed in the probabilistic interpretation. For a non-degenerate operator A this distribution is the same as the distribution (2.1) over the eigenstates. But because the information is dependent only on the distribution, and not on numerical values, the information of the distribution over eigenvalues of A is precisely the information of the eigenbasis of A, \(\{\phi_i\}\) . Therefore:  

\[I_{\mathbf{A}}(\psi) = I_{\{\phi_i\}}(\psi) = \sum_i < [\phi_i] > \psi \ln < [\phi_i] > \psi \quad (\mathrm{A~non - degenerate}). \quad (2.3)\]  

We see that for fixed \(\psi\) , the information of all non- degenerate operators having the same set of eigenstates is the same.  

In the case of degenerate operators it will be convenient to take, as the definition of information, the information of the square amplitude distribution over the eigenvalues relative to the information measure which consists of the multiplicity of the eigenvalues, rather than the uniform measure. This definition preserves the choice of uniform measure over the eigenstates, in distinction to the eigenvalues. If \(\phi_{ij}\) (j from 1 to \(m_i\) ) are a complete orthonormal set of eigenstates for A', with distinct eigenvalues \(\lambda_i\) (degenerate with respect to j), then the multiplicity of the ith eigenvalue is \(m_i\) and the information \(I_A(\psi)\) is defined to be:  

\[I_A(\psi) = \sum_i \left(\sum_j < [\phi_{ij}] > \psi \right) \ln \frac{\sum_j < [\phi_{ij}] > \psi}{m_i}. \quad (2.4)\]  

The usefulness of this definition lies in the fact that any operator A' which distinguishes further between any of the degenerate states of A' leads to a refinement of the relative density, in the sense of Theorem 4, and consequently has equal or greater information. A non- degenerate operator thus represents the maximal refinement and possesses maximal information.

---

It is convenient to introduce a new notation for the projection operators which are relevant for a specified operator. As before let A have eigenfunctions \(\phi_{ij}\) and distinct eigenvalues \(\lambda_{i}\) . Then define the projections \(A_{i}\) , the projections on the eigenspaces of different eigenvalues of A, to be:  

\[A_{i} = \sum_{j = 1}^{m_{i}}\left[\phi_{ij}\right].\]  

To each such projection there is associated a number \(m_{i}\) , the multiplicity of the degeneracy, which is the dimension of the \(i^{\text{th}}\) eigenspace. In this notation the distribution over the eigenvalues of A for the state \(\psi\) , \(P_{i}\) , becomes simply:  

\[P_{i} = P(\lambda_{i}) = < A_{i} > \psi , \quad (2.6)\]  

and the information, given by (2.4), becomes:  

\[I_{A} = \sum_{i} < A_{i} > \psi \ln \frac{< A_{i} > \psi}{m_{i}}. \quad (2.7)\]  

Similarly, for a pair of operators, A in \(S_{1}\) and B in \(S_{2}\) , for the composite system \(S = S_{1} + S_{2}\) with state \(\psi^{S}\) , the joint distribution over eigenvalues is:  

\[P_{ij} = P(\lambda_{i},\mu_{j}) = < A_{i}B_{j} > \psi^{S}, \quad (2.8)\]  

and the marginal distributions are:  

\[\begin{array}{l}{{ P_{i}=\sum_{j}P_{i j}=\langle A_{i}\Big(\sum_{j}B_{j}\Big)\rangle\psi^{S}=\langle A_{i}I^{2}\rangle\psi^{S},}}\\ {{ P_{j}=\sum_{i}P_{i j}=\langle\Big(\sum_{i}A_{i}\Big)B_{j}\rangle\psi^{S}=\langle I^{1}B_{j}\rangle\psi^{S}.}}\end{array} \quad (2.9)\]  

The joint information, \(I_{AB}\) , is given by:  

\[I_{AB} = \sum_{ij} P_{ij} \ln \frac{P_{ij}}{m_i n_j} = \sum_{ij} < A_i B_j > \psi^S \ln \frac{< A_i B_j > \psi^S}{m_i n_j}, \quad (2.10)\]

---

where \(\mathbf{m}_{\mathrm{i}}\) and \(\mathbf{n}_{\mathrm{j}}\) are the multiplicities of the eigenvalues \(\lambda_{\mathrm{i}}\) and \(\mu_{\mathrm{j}}\) . The marginal information quantities are given by:  

\[\mathrm{I}_{\mathrm{A}} = \sum_{\mathrm{i}}\langle \mathrm{A}_{\mathrm{i}}\mathrm{I}^{2}\rangle \psi^{\mathrm{S}}\ln \frac{\langle\mathrm{A}_{\mathrm{i}}\mathrm{I}^{2}\rangle\psi^{\mathrm{S}}}{\mathrm{m}_{\mathrm{i}}}, \quad (2.11)\]  

and finally the correlation, \(\{\mathrm{A},\mathrm{B}|\psi^{\mathrm{S}}\) is given by:  

\[\{\mathrm{A},\mathrm{B}|\psi^{\mathrm{S}} = \sum_{\mathrm{i}\mathrm{j}}\mathrm{P}_{\mathrm{i}\mathrm{j}}\ln \frac{\mathrm{P}_{\mathrm{i}\mathrm{j}}}{\mathrm{P}_{\mathrm{i}}\mathrm{P}_{\mathrm{j}}} = \sum_{\mathrm{i}\mathrm{j}}\langle \mathrm{A}_{\mathrm{i}}\mathrm{B}_{\mathrm{j}}\rangle \psi^{\mathrm{S}}\ln \frac{\langle\mathrm{A}_{\mathrm{i}}\mathrm{B}_{\mathrm{j}}\rangle\psi^{\mathrm{S}}}{\langle\mathrm{A}_{\mathrm{i}}\mathrm{I}\rangle\psi^{\mathrm{S}}\langle\mathrm{I}\mathrm{B}_{\mathrm{j}}\rangle\psi^{\mathrm{S}}}, \quad (2.12)\]  

where we note that the expression does not involve the multiplicities, as do the information expressions, a circumstance which simply reflects the independence of correlation on any information measure. These expressions of course generalize trivially to distributions over more than two variables (composite systems of more than two subsystems).  

In addition to the correlation of pairs of subsystem operators, given by (2.12), there always exists a unique quantity \(\{S_{1}, S_{2}\}\) , the canonical correlation, which has some special properties and may be regarded as the fundamental correlation between the two subsystems \(S_{1}\) and \(S_{2}\) of the composite system \(S\) . As we remarked earlier a density matrix is Hermitian, so that there is a representation in which it is diagonal. \(^{6}\) In

---

particular, for the decomposition of \(S\) (with state \(\psi^{S}\) ) into \(S_{1}\) and \(S_{2}\) , we can choose a representation in which both \(\rho^{S_{1}}\) and \(\rho^{S_{2}}\) are diagonal. (This choice is always possible because \(\rho^{S_{1}}\) is independent of the basis in \(S_{2}\) and vice-versa.) Such a representation will be called a canonical representation. This means that it is always possible to represent the state \(\psi^{S}\) by a single superposition:  

\[\psi^{S} = \sum_{\mathbf{i}}\mathbf{a}_{\mathbf{i}}\xi_{\mathbf{i}}\eta_{\mathbf{i}}, \quad (2.13)\]  

where both the \(\{\xi_{i}\}\) and the \(\{\eta_{i}\}\) constitute orthonormal sets of states for \(S_{1}\) and \(S_{2}\) respectively.  

To construct such a representation choose the basis \(\{\eta_{i}\}\) for \(S_{2}\) so that \(\rho^{S_{2}}\) is diagonal:  

\[\rho_{i j}^{S} = \lambda_{i}\delta_{i j}, \quad (2.14)\]  

and let the \(\xi_{i}\) be the relative states in \(S_{1}\) for the \(\eta_{i}\) in \(S_{2}\) :  

\[\xi_{i} = \mathrm{N}_{i}\sum_{\mathrm{j}}(\phi_{\mathrm{j}}\eta_{\mathrm{i}},\psi^{S})\phi_{\mathrm{j}}\quad (\mathrm{any~basis~}\{\phi_{\mathrm{j}}\})~. \quad (2.15)\]  

Then, according to (1.13), \(\psi^{S}\) is represented in the form (2.13) where the \(\{\eta_{i}\}\) are orthonormal by choice, and the \(\{\xi_{i}\}\) are normal since they are relative states. We therefore need only show that the states \(\{\xi_{i}\}\) are orthogonal:  

\[\begin{array}{r l} & {(\xi_{j},\xi_{k}) = \left(\mathrm{N}_{j}\sum_{\ell}(\phi_{\ell}\eta_{j},\psi^{S})\phi_{\ell},\mathrm{N}_{k}\sum_{\mathrm{m}}(\phi_{\mathrm{m}}\eta_{k},\psi^{S})\phi_{\mathrm{m}}\right)}\\ & {\qquad = \sum_{\ell \mathrm{m}}\mathrm{N}_{j}^{*}\mathrm{N}_{k}(\phi_{\ell}\eta_{j},\psi^{S})^{*}(\phi_{\mathrm{m}}\eta_{k},\psi^{S})\delta_{\ell \mathrm{m}}}\\ & {\qquad = \mathrm{N}_{j}^{*}\mathrm{N}_{k}\sum_{\ell}(\phi_{\ell}\eta_{j},\psi^{S})^{*}(\phi_{\ell}\eta_{k},\psi^{S})}\\ & {\qquad = \mathrm{N}_{j}^{*}\mathrm{N}_{k}\rho_{k j}^{S^{2}} = \mathrm{N}_{j}^{*}\mathrm{N}_{k}\lambda_{k}\delta_{k j} = 0,\mathrm{for} j\neq k,} \end{array} \quad (2.16)\]

---

since we supposed \(\rho^{S_2}\) to be diagonal in this representation. We have therefore constructed a canonical representation (2.13). 

The density matrix \(\rho^{S_1}\) is also automatically diagonal, by the choice of representation consisting of the basis in \(S_2\) which makes \(\rho^{S_2}\) diagonal and the corresponding relative states in \(S_1\). Since \(\{\xi_i\}\) are orthonormal we have: 

\[
\begin{align*}
\rho^{S_1} &= \sum_k (\xi_i \eta_k, \psi S)^* (\xi_j \eta_k, \psi S) = \\
&\quad \sum_k (\xi_i \eta_k, \sum_m a_m \xi_m \eta_m)^* (\xi_j \eta_k, \sum_l a_l \xi_l \eta_l) \\
&= \sum_{klm} a_m^* a_l \delta_{im} \delta_{km} \delta_{jl} \delta_{kl} = \sum_k a_i^* a_j \delta_{ki} \delta_{kj} \\
&= a_i^* a_i \delta_{ij} = P_i \delta_{ij},
\end{align*}
\]

where \(P_i = a_i^* a_i\) is the marginal distribution over the \(\{\xi_i\}\). Similar computation shows that the elements of \(\rho^{S_2}\) are the same: 

\[
\rho_{kl}^{S_2} = a_k^* a_k \delta_{kl} = P_k \delta_{kl}.
\tag{2.18}
\]

Thus in the canonical representation both density matrices are diagonal
and have the same elements, \(P_k\), which give the marginal square ampli-
tude distribution over both of the sets \(\{\xi_i\}\) and \(\{\eta_i\}\) forming the basis
of the representation. 

Now, any pair of operators, \(\tilde{A}\) in \(S_1\) and \(\tilde{B}\) in \(S_2\), which have as
non-degenerate eigenfunctions the sets \(\{\xi_i\}\) and \(\{\eta_j\}\) (i.e., operators
which define the canonical representation), are “perfectly” correlated in
the sense that there is a one-one correspondence between their eigen-
values. The joint square amplitude distribution for eigenvalues \(\lambda_i\) of \(\tilde{A}\)
and \(\mu_j\) of \(\tilde{B}\) is: 

\[
P(\lambda_i \text{ and } \mu_j) = P(\xi_i \text{ and } \eta_j) = P_{ij} = a_i^* a_i \delta_{ij} = P_i \delta_{ij}.
\tag{2.19}
\]

---

Therefore, the correlation between these operators, \(\{\widetilde{\mathbf{A}},\widetilde{\mathbf{B}}\} \psi^{\mathbf{S}}\) is:  

\[\begin{array}{l}{{\{\widetilde{\mathbf{A}},\widetilde{\mathbf{B}}\} \psi^{\mathbf{S}}=\sum_{\mathbf{i}\mathbf{j}}\mathbf{P}(\lambda_{\mathbf{i}}\ \mathbf{a}\ \mu_{\mathbf{j}})\ln\frac{\mathbf{P}(\lambda_{\mathbf{i}}\& \mu_{\mathbf{j}})}{\mathbf{P}(\lambda_{\mathbf{i}})\mathbf{P}(\mu_{\mathbf{j}})}=\sum_{\mathbf{i}\mathbf{j}}\mathbf{P}_{\mathbf{i}}\delta_{\mathbf{i}\mathbf{j}}\ln\frac{\mathbf{P}_{\mathbf{i}}\delta_{\mathbf{i}\mathbf{j}}}{\mathbf{P}_{\mathbf{i}}\mathbf{P}_{\mathbf{j}}}}\\ {{=-\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}\ln\mathbf{P}_{\mathbf{i}}\ .}}\end{array} \quad (2.20)\]  

We shall denote this quantity by \(\{S_{1},S_{2}\} \psi^{\mathbf{S}}\) and call it the canonical correlation of the subsystems \(S_{1}\) and \(S_{2}\) for the system state \(\psi^{\mathbf{S}}\) . It is the correlation between any pair of non- degenerate subsystem operators which define the canonical representation.  

In the canonical representation, where the density matrices are diagonal ((2.17) and (2.18)), the canonical correlation is given by:  

\[\begin{array}{r l r}{{\{S_{1},S_{2}\} \psi^{S}=-\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}\ln\mathbf{P}_{\mathbf{i}}=-\mathrm{Trace}(\rho^{S_{1}}\ln\rho^{S_{1}})}}\\ &{}&\\ &{}&{=-\mathrm{Trace}(\rho^{S_{2}}\ln\rho^{S_{2}}).}\end{array} \quad (2.21)\]  

But the trace is invariant for unitary transformations, so that (2.21) holds independently of the representation, and we have therefore established the uniqueness of \(\{S_{1},S_{2}\} \psi^{\mathbf{S}}\) .  

It is also interesting to note that the quantity \(-\mathrm{Trace}(\rho \ln \rho)\) is (apart from a factor of Boltzman's constant) just the entropy of a mixture of states characterized by the density matrix \(\rho\) . Therefore the entropy of the mixture characteristic of a subsystem \(S_{1}\) for the state \(\psi^{\mathbf{S}} = \psi^{S_{1} + S_{2}}\) is exactly matched by a correlation information \(\{S_{1},S_{2}\}\) , which represents the correlation between any pair of operators \(\widetilde{\mathbf{A}}\) , \(\widetilde{\mathbf{B}}\) , which define the canonical representation. The situation is thus quite similar to that of classical mechanics.

---

Another special property of the canonical representation is that any operators \(\tilde{\mathbf{A}}, \tilde{\mathbf{B}}\) defining a canonical representation have maximum marginal information, in the sense that for any other discrete spectrum operators, A on \(S_{1}, \mathbf{B}\) on \(S_{2}, \mathbf{I}_{\mathbf{A}} \leq \mathbf{I}_{\mathbf{A}}^{\infty}\) and \(\mathbf{I}_{\mathbf{B}} \leq \mathbf{I}_{\mathbf{B}}^{\infty}\) . If the canonical representation is (2.13), with \(\{\xi_{i}\}, \{\eta_{i}\}\) non-degenerate eigenfunctions of \(\tilde{\mathbf{A}}, \tilde{\mathbf{B}}\) , respectively, and \(\mathbf{A}, \mathbf{B}\) any pair of non-degenerate operators with eigenfunctions \(\{\phi_{k}\}\) and \(\{\theta_{\ell}\}\) , where \(\xi_{i} = \sum_{k} c_{i k} \phi_{k}, \eta_{i} = \sum_{\ell} d_{i \ell} \theta_{\ell}\) , then \(\psi^{S}\) in \(\phi, \theta\) representation is:  

\[\psi^{S} = \sum_{i k \ell} a_{i} c_{i k} d_{i \ell} \phi_{k} \theta_{\ell} = \sum_{k \ell} \left(\sum_{i} a_{i} c_{i k} d_{i \ell}\right) \phi_{k} \theta_{\ell}, \quad (2.22)\]  

and the joint square amplitude distribution for \(\phi_{k}, \theta_{\ell}\) is:  

\[\mathrm{P}_{\mathbf{k}\ell} = \left|\left(\sum_{i} a_{i} c_{i k} d_{i \bar{\ell}}\right)\right|^{2} = \sum_{i m} a_{i}^{*} a_{m} c_{i k}^{*} c_{m k} d_{i \bar{\ell}}^{*} d_{m \ell}, \quad (2.23)\]  

while the marginals are:  

\[\begin{array}{r l r}{{\mathrm{P}_{\mathbf{k}}=\sum_{\ell}\mathrm{P}_{\mathbf{k}\ell}=\sum_{i m}a_{i}^{*}a_{m}c_{i k}^{*}c_{m k}\sum_{\ell}d_{i\ell}^{*}d_{m\ell}}}\\ &{}&{=\sum_{i m}a_{i}^{*}a_{m}c_{i k}^{*}c_{\mathrm{m}k}\delta_{i m}=\sum_{i}a_{i}^{*}a_{i}c_{i k}^{*}c_{i k},}\end{array} \quad (2.24)\]  

and similarly  

\[\mathrm{P}_{\ell} = \sum_{k} \mathrm{P}_{\ell} = \sum_{i} a_{i}^{*} a_{i} d_{i \ell}^{*} d_{i \ell}. \quad (2.25)\]  

Then the marginal information \(\mathbf{I}_{\mathbf{A}}\) is:  

\[\begin{array}{r l r}{{\mathrm{I}}_{\mathbf{A}}=\sum_{\mathbf{k}}\mathrm{P}_{\mathbf{k}}\ln\mathrm{P}_{\mathbf{k}}=\sum_{\mathbf{k}}\left(\sum_{i}a_{i}^{*}a_{i}c_{i k}^{*}c_{k}\right)\ln\left(\sum_{i}a_{i}^{*}a_{i}c_{i k}^{*}c_{\mathbf{k}}\right)}\\ &{}&{=\sum_{\mathbf{k}}\left(\sum_{i}a_{i}^{*}a_{i}T_{i\mathbf{k}}\right)\ln\left(\sum_{i}a_{i}^{*}a_{i}T_{i\mathbf{k}}\right),}\end{array} \quad (2.26)\]  

where \(\mathbf{T}_{i \mathbf{k}} = c_{i \mathbf{k}}^{*} c_{i \mathbf{k}}\) is doubly- stochastic \(\left(\sum_{i} \mathbf{T}_{i \mathbf{k}} = \sum_{k} \mathbf{T}_{i \mathbf{k}} = 1\right.\) follows from unitary nature of the \(c_{i \mathbf{k}}\) . Therefore (by Corollary 2, §4, Appendix I):

---

\[{I_{\mathbf{A}}=\sum_{\mathbf{k}}\left(\sum_{\mathbf{i}}\mathbf{a}_{\mathbf{i}}^{*}\mathbf{a}_{\mathbf{i}}\mathrm{T}_{\mathbf{i}\mathbf{k}}\right)\ln\left(\sum_{\mathbf{i}}\mathbf{a}_{\mathbf{i}}^{*}\mathbf{a}_{\mathbf{i}}^{\mathrm{T}}\mathrm{T}_{\mathbf{i}\mathbf{k}}\right)}\] \[{\leq\sum_{\mathbf{i}}\mathbf{a}_{\mathbf{i}}^{*}\mathbf{a}_{\mathbf{i}}\ln\mathbf{a}_{\mathbf{i}}^{*}\mathbf{a}_{\mathbf{i}}=\mathrm{I}_{\mathbf{A}}^{\infty},}\]  

and we have proved that \(\tilde{\mathbf{A}}\) has maximal marginal information among the discrete spectrum operators. Identical proof holds for \(\tilde{\mathbf{B}}\) .  

While this result was proved only for non- degenerate operators, it is immediately extended to the degenerate case, since as a consequence of our definition of information for a degenerate operator, (2.4), its information is still less than that of an operator which removes the degeneracy. We have thus proved:  

THEOREM. \(\mathbf{I}_{\mathbf{A}} \leq \mathbf{I}_{\tilde{\mathbf{A}}}^{\infty}\) , where \(\tilde{\mathbf{A}}\) is any non- degenerate operator defining the canonical representation, and \(\mathbf{A}\) is any operator with discrete spectrum.  

We conclude the discussion of the canonical representation by conjecturing that in addition to the maximum marginal information properties of \(\tilde{\mathbf{A}}\) , \(\tilde{\mathbf{B}}\) , which define the representation, they are also maximally correlated, by which we mean that for any pair of operators \(\mathbf{C}\) in \(S_{1}\) , \(\mathbf{D}\) in \(S_{2}\) , \(\{\mathbf{C}, \mathbf{D} \} \leq \{\tilde{\mathbf{A}}, \tilde{\mathbf{B}}\}\) , i.e.,:  

\[\mathrm{CONJECTURE.}^{9}\{\mathbf{C},\mathbf{D}|\psi^{\mathbf{S}}\leq \{\tilde{\mathbf{A}},\tilde{\mathbf{B}}|\psi^{\mathbf{S}} = \{\mathbf{S}_{1},\mathbf{S}_{2}\} |\psi^{\mathbf{S}} \quad (2.28)\]  

As a final topic for this section we point out that the uncertainty principle can probably be phrased in a stronger form in terms of information. The usual form of this principle is stated in terms of variances, namely:

---

\[\sigma_{\mathbf{x}}^{2}\sigma_{\mathbf{k}}^{2}\geq \frac{1}{4}\qquad \mathrm{for~all~}\psi (\mathbf{x}), \quad (2.29)\]  

where \(\sigma_{\mathbf{x}}^{2} = < \mathbf{x}^{2} > \psi - [< \mathbf{x} > \psi ]^{2}\) and  

\[\sigma_{\mathbf{k}}^{2} = < \left(-i\frac{\partial}{\partial\mathbf{x}}\right)^{2} > \psi -\left[< -i\frac{\partial}{\partial\mathbf{x}} > \psi \right]^{2} = < \left(\frac{\mathbf{P}}{\hbar}\right)^{2} > \psi -\left[< \frac{\mathbf{P}}{\hbar} > \psi \right]^{2}.\]  

The conjectured information form of this principle is:  

\[\mathrm{I}_{\mathbf{x}} + \mathrm{I}_{\mathbf{k}}\leq \ln (1 / \pi \mathrm{e})\qquad \mathrm{for~all~}\psi (\mathbf{x}). \quad (2.30)\]  

Although this inequality has not yet been proved with complete rigor, it is made highly probable by the circumstance that equality holds for \(\psi (\mathbf{x})\) of the form \(\psi (\mathbf{x}) = (1 / 2\pi)^{4}\) exponent \(\left[\frac{\mathbf{x}^{2}}{4\sigma_{\mathbf{x}}^{2}}\right]\) the so called "minimum uncertainty packets" which give normal distributions for both position and momentum, and that furthermore the first variation of \((\mathrm{I}_{\mathbf{x}} + \mathrm{I}_{\mathbf{k}})\) vanishes for such \(\psi (\mathbf{x})\) . (See Appendix I, §6. ) Thus, although \(\ln (1 / \pi \mathrm{e})\) has not been proved an absolute maximum of \(\mathrm{I}_{\mathbf{x}} + \mathrm{I}_{\mathbf{k}}\) , it is at least a stationary value.  

The principle (2.30) is stronger than (2.29), since it implies (2.29) but is not implied by it. To see that it implies (2.29) we use the well known fact (easily established by a variation calculation: that, for fixed variance \(\sigma^{2}\) , the distribution of minimum information is a normal distribution, which has information \(\mathrm{I} = \ln (1 / \sigma \sqrt{2\pi \mathrm{e}})\) . This gives us the general inequality involving information and variance:  

\[\mathrm{I}\geq \ln (1 / \sigma \sqrt{2\pi \mathrm{e}})\qquad (\mathrm{for~all~distributions}). \quad (2.31)\]  

Substitution of (2.31) into (2.30) then yields:  

\[\ln (1 / \sigma_{\mathbf{x}}\sqrt{2\pi \mathrm{e}}) + \ln (1 / \sigma_{\mathbf{k}}\sqrt{2\pi \mathrm{e}})\leq \mathrm{I}_{\mathbf{x}} + \mathrm{I}_{\mathbf{k}}\leq \ln (1/\pi \mathrm{e})\] \[\Rightarrow (1 / \sigma_{\mathbf{x}}\sigma_{\mathbf{k}}2\pi \mathrm{e})\leq (1 / \pi \mathrm{e})\Rightarrow \sigma_{\mathbf{x}}^{2}\sigma_{\mathbf{k}}^{2}\geq \frac{1}{\mathrm{4}},\]  

so that our principle implies the standard principle (2.29).

---

To show that (2.29) does not imply (2.30) it suffices to give a counterexample. The distributions \(\mathrm{P}(\mathbf{x}) = \frac{1}{2}\delta (\mathbf{x}) + \frac{1}{2}\delta (\mathbf{x} - 10)\) and \(\mathrm{P}(\mathbf{k}) = \frac{1}{2}\delta (\mathbf{k}) + \frac{1}{2}\delta (\mathbf{k} - 10)\) , which consist simply of spikes at 0 and 10, clearly satisfy (2.29), while they both have infinite information and thus do not satisfy (2.30). Therefore it is possible to have arbitrarily high information about both \(\mathbf{x}\) and \(\mathbf{k}\) (or \(\mathbf{p}\) ) and still satisfy (2.13). We have, then, another illustration that information concepts are more powerful and more natural than the older measures based upon variance.  

## §3. Measurement  

We now consider the question of measurement in quantum mechanics, which we desire to treat as a natural process within the theory of pure wave mechanics. From our point of view there is no fundamental distinction between "measuring apparata" and other physical systems. For us, therefore, a measurement is simply a special case of interaction between physical systems - an interaction which has the property of correlating a quantity in one subsystem with a quantity in another.  

Nearly every interaction between systems produces some correlation however. Suppose that at some instant a pair of systems are independent, so that the composite system state function is a product of subsystem states \((\psi^{S} = \psi^{S_{1}}\psi^{S_{2}})\) . Then this condition obviously holds only instantaneously if the systems are interacting \(^{10}\) - the independence is immediately destroyed and the systems become correlated. We could, then, take the position that the two interacting systems are continually "measuring" one another, if we wished. At each instant \(\mathbf{t}\) we could put the composite system into canonical representation, and choose a pair of operators \(\hat{\mathcal{A}} (\mathbf{t})\)

---

in \(S_{1}\) and \(\tilde{\mathbf{B}} (\mathbf{t})\) in \(S_{2}\) which define this representation. We might then reasonably assert that the quantity \(\tilde{\mathbf{A}}\) in \(S_{1}\) is measured by \(\tilde{\mathbf{B}}\) in \(S_{2}\) (or vice- versa), since there is a one- one correspondence between their values.  

Such a viewpoint, however, does not correspond closely with our intuitive idea of what constitutes "measurement," since the quantities \(\tilde{\mathbf{A}}\) and \(\tilde{\mathbf{B}}\) which turn out to be measured depend not only on the time, but also upon the initial state of the composite system. A more reasonable position is to associate the term "measurement" with a fixed interaction \(\mathbf{H}\) between systems, \(^{11}\) and to define the "measured quantities" not as those quantities \(\tilde{\mathbf{A}} (\mathbf{t})\) , \(\tilde{\mathbf{B}} (\mathbf{t})\) which are instantaneously canonically correlated, but as the limit of the instantaneous canonical operators as the time goes to infinity, \(\tilde{\mathbf{A}}_{\infty}\) , \(\tilde{\mathbf{B}}_{\infty}\) - provided that this limit exists and is independent of the initial state. \(^{12}\) In such a case we are able to associate the "measured quantities," \(\tilde{\mathbf{A}}_{\infty}\) , \(\tilde{\mathbf{B}}_{\infty}\) , with the interaction \(\mathbf{H}\) independently of the actual system states and the time. We can therefore say that \(\mathbf{H}\) is an interaction which causes the quantity \(\tilde{\mathbf{A}}_{\infty}\) in \(S_{1}\) to be measured by \(\tilde{\mathbf{B}}_{\infty}\) in \(S_{2}\) . For finite times of interaction the measurement is only approximate, approaching exactness as the time of interaction increases indefinitely.  

There is still one more requirement that we must impose on an interaction before we shall call it a measurement. If \(\mathbf{H}\) is to produce a measurement of \(\mathbf{A}\) in \(S_{1}\) by \(\mathbf{B}\) in \(S_{2}\) , then we require that \(\mathbf{H}\) shall

---

never decrease the information in the marginal distribution of A. If H is to produce a measurement of A by correlating it with B, we expect that a knowledge of B shall give us more information about A than we had before the measurement took place, since otherwise the measurement would be useless. Now, H might produce a correlation between A and B by simply destroying the marginal information of A, without improving the expected conditional information of A given B, so that a knowledge of B would give us no more information about A than we possessed originally. Therefore in order to be sure that we will gain information about A by knowing B, when B has become correlated with A, it is necessary that the marginal information about A has not decreased. The expected information gain in this case is assured to be not less than the correlation {A,B}.  

The restriction that H shall not decrease the marginal information of A has the interesting consequence that the eigenstates of A will not be disturbed, i.e., initial states of the form \(\psi_{0}^{\mathrm{S}} = \phi \eta_{0}\) , where \(\phi\) is an eigenfunction of A, must be transformed after any time interval into states of the form \(\psi_{\mathrm{t}}^{\mathrm{S}} = \phi \eta_{\mathrm{t}}\) , since otherwise the marginal information of A, which was initially perfect, would be decreased. This condition, in turn, is connected with the repeatability of measurements, as we shall subsequently see, and could alternately have been chosen as the condition for measurement.  

We shall therefore accept the following definition. An interaction H is a measurement of A in \(S_{1}\) by B in \(S_{2}\) if H does not destroy the marginal information of A (equivalently: if H does not disturb the eigenstates of A in the above sense) and if furthermore the correlation {A,B} increases toward its maximum \(^{13}\) with time.

---

We now illustrate the production of correlation with an example of a simplified measurement due to von Neumann. \(^{14}\) Suppose that we have a system of only one coordinate, \(q\) , (such as position of a particle), and an apparatus of one coordinate \(r\) (for example the position of a meter needle). Further suppose that they are initially independent, so that the combined wave function is \(\psi_{0}^{\mathrm{S} + \mathrm{A}} = \phi (q)\eta (r)\) , where \(\phi (q)\) is the initial system wave function, and \(\eta (r)\) is the initial apparatus function. Finally suppose that the masses are sufficiently large or the time of interaction sufficiently small that the kinetic portion of the energy may be neglected, so that during the time of measurement the Hamiltonian shall consist only of an interaction, which we shall take to be:  

\[\mathrm{H}_{\mathrm{I}} = -\mathrm{i}\hbar \mathrm{q}\frac{\partial}{\partial t}. \quad (3.1)\]  

Then it is easily verified that the state \(\psi_{\mathrm{t}}^{\mathrm{S} + \mathrm{A}}(\mathrm{q}, \mathrm{r})\) :  

\[\psi_{\mathrm{t}}^{\mathrm{S} + \mathrm{A}}(\mathrm{q}, \mathrm{r}) = \phi (\mathrm{q}) \eta (\mathrm{r} - \mathrm{qt}). \quad (3.2)\]  

is a solution of the Schrödinger equation  

\[\mathrm{i}\hbar \frac{\partial \psi_{\mathrm{t}}^{\mathrm{S} + \mathrm{A}}}{\partial t} = \mathrm{H}_{\mathrm{I}} \psi_{\mathrm{t}}^{\mathrm{S} + \mathrm{A}} \quad (3.3)\]  

for the specified initial conditions at time \(t = 0\) .  

Translating (3.2) into square amplitudes we get:  

\[\mathrm{P}_{\mathrm{t}}(\mathrm{q}, \mathrm{r}) = \mathrm{P}_{1}(\mathrm{q}) \mathrm{P}_{2}(\mathrm{r} - \mathrm{qt}), \quad (3.4)\]  

where \(\mathrm{P}_{1}(\mathrm{q}) = \phi^{*}(\mathrm{q}) \phi (\mathrm{q}), \mathrm{P}_{2}(\mathrm{r}) = \eta^{*}(\mathrm{r}) \eta (\mathrm{r}),\)  

and \(\mathrm{P}_{\mathrm{t}}(\mathrm{q}, \mathrm{r}) = \psi_{\mathrm{t}}^{\mathrm{S} + \mathrm{A}^{*}}(\mathrm{q}, \mathrm{r}) \psi_{\mathrm{t}}^{\mathrm{S} + \mathrm{A}}(\mathrm{q}, \mathrm{r}),\)

---

and we note that for a fixed time, t, the conditional square amplitude distribution for r has been translated by an amount depending upon the value of q, while the marginal distribution for q has been unaltered. We see thus that a correlation has been introduced between q and r by this interaction, which allows us to interpret it as a measurement. It is instructive to see quantitatively how fast this correlation takes place. We note that:  

\[{\mathrm{IQR(t)}=\iint\mathrm{P_{t}(q,r)}\ln\mathrm{P_{t}(q,r)}\mathrm{dqdr}}\] \[{=\iint\mathrm{P_{1}(q)P_{2}(r-q t)}\ln\mathrm{P_{1}(q)P_{2}(r-q t)}\mathrm{dqdr}}\] \[{=\iint\mathrm{P_{1}(q)P_{1}(q)}\ln\mathrm{P_{1}(q)P_{2}(w)}\mathrm{dqdw}}\] \[{=\mathrm{IQR(0)~,}}\]  

so that the information of the joint distribution does not change. Furthermore, since the marginal distribution for q is unchanged:  

\[\mathrm{IQ(t) = I_{Q}(0)~,} \quad (3.6)\]  

and the only quantity which can change is the marginal information, \(\mathbf{I}_{\mathbf{R}}\) of r, whose distribution is:  

\[\mathrm{P_{t}(r) = \int P_{t}(r,q)dq = \int P_{1}(q)P_{2}(r - qt)dq~.} \quad (3.7)\]  

Application of a special inequality (proved in §5, Appendix I) to (3.7) yields the relation:  

\[\mathrm{I_{R}(t)\leq I_{Q}(0) - \ln t~,} \quad (3.8)\]  

so that, except for the additive constant \(\mathrm{I_{Q}(0)}\) , the marginal information \(\mathbf{I}_{\mathbf{R}}\) tends to decrease at least as fast as \(\ln \mathrm{t}\) with time during the interaction. This implies the relation for the correlation:

---

\[\{Q,R\}_{\mathrm{t}} = \mathrm{I}_{QR}(t) - \mathrm{I}_{Q}(t) - \mathrm{I}_{R}(t)\geq \mathrm{I}_{RQ}(t) - \mathrm{I}_{Q}(t) - \mathrm{I}_{Q}(0) + \ln t. \quad (3.9)\]  

But at \(t = 0\) the distributions for \(R\) and \(Q\) were independent, so that \(\mathrm{I}_{RQ}(0) = \mathrm{I}_{R}(0) + \mathrm{I}_{Q}(0)\) . Substitution of this relation, (3.5), and (3.6) into (3.9) then yields the final result:  

\[\{Q,R\}_{\mathrm{t}}\geq \mathrm{I}_{R}(0) - \mathrm{I}_{Q}(0) + \ln t. \quad (3,10)\]  

Therefore the correlation is built up at least as fast as \(\ln t\) , except for an additive constant representing the difference of the information of the initial distributions \(\mathrm{P}_{2}(r)\) and \(\mathrm{P}_{1}(q)\) . Since the correlation goes to infinity with increasing time, and the marginal system distribution is not changed, the interaction (3.1) satisfies our definition of a measurement of \(q\) by \(r\) .  

Even though the apparatus does not indicate any definite system value (since there are no independent system or apparatus states), one can nevertheless look upon the total wave function (3.2) as a superposition of pairs of subsystem states, each element of which has a definite \(q\) value and a correspondingly displaced apparatus state. \(^{15}\) Thus we can write (3.2) as:  

\[\psi_{\mathrm{t}}^{\mathrm{S + A}} = \int \phi (q^{\prime})\delta (q - q^{\prime})\eta (r - q^{\prime})\mathrm{d}q^{\prime}, \quad (3.11)\]  

which is a superposition of states \(\psi_{q^{\prime}} = \delta (q - q^{\prime})\eta (r - q^{\prime}t)\) . Each of these elements, \(\psi_{q^{\prime}}\) , of the superposition describes a state in which the system has the definite value \(q = q^{\prime}\) , and in which the apparatus has a state that is displaced from its original state by the amount \(q^{\prime}t\) . These elements \(\psi_{q^{\prime}}\) are then superposed with coefficients \(\phi (q^{\prime})\) to form the total state (3.11).

---

Conversely, if we transform to the representation where the apparatus is definite, we write (3.2) as:  

\[\psi_{\mathrm{r}}^{\mathrm{S} + \mathrm{A}} = \int (1 / \mathrm{N}_{\mathrm{r}})\xi^{\mathrm{r}}(\mathrm{q})\delta (\mathrm{r} - \mathrm{r}^{\prime})\mathrm{d}\mathrm{r}^{\prime}, \quad (3.12)\]  

where  

\[\xi^{\mathrm{r}}(\mathbf{q}) = \mathrm{N}_{\mathrm{r}}\phi (\mathbf{q})\eta (\mathbf{r}^{\prime} - \mathbf{q}\mathbf{t})\]  

and  

\[(1 / \mathrm{N}_{\mathrm{r}})^{2} = \int \phi^{*}(\mathbf{q})\phi (\mathbf{q})\eta^{*}(\mathbf{r}^{\prime} - \mathbf{q}\mathbf{t})\eta (\mathbf{r} - \mathbf{q}\mathbf{t})\mathrm{d}\mathbf{q}.\]  

Then the \(\xi^{\mathrm{r}}(\mathbf{q})\) are the relative system state functions for the apparatus states \(\delta (\mathbf{r} - \mathbf{r}^{\prime})\) of definite value \(\mathbf{r} = \mathbf{r}^{\prime}\) .  

We notice that these relative system states, \(\xi^{\mathrm{r}}(\mathbf{q})\) , are nearly eigenstates for the values \(\mathbf{q} = \mathbf{r}^{\prime} / \mathbf{t}\) , if the degree of correlation between \(\mathbf{q}\) and \(\mathbf{r}\) is sufficiently high, i.e., if \(\mathbf{t}\) is sufficiently large, or \(\eta (\mathbf{r})\) sufficiently sharp (near \(\delta (\mathbf{r})\) ) then \(\xi^{\mathrm{r}}(\mathbf{q})\) is nearly \(\delta (\mathbf{q} - \mathbf{r}^{\prime} / \mathbf{t})\) .  

This property, that the relative system states become approximate eigenstates of the measurement, is in fact common to all measurements. If we adopt as a measure of the nearness of a state \(\psi\) to being an eigenfunction of an operator \(\mathbf{A}\) the information \(\mathbf{I}_{\mathbf{A}}(\psi)\) , which is reasonable because \(\mathbf{I}_{\mathbf{A}}(\psi)\) measures the sharpness of the distribution of \(\mathbf{A}\) for \(\psi\) , then it is a consequence of our definition of a measurement that the relative system states tend to become eigenstates as the interaction proceeds. Since \(\exp [\mathbf{I}_{\mathbf{Q}}^{\mathrm{r}}] = \mathbf{I}_{\mathbf{Q}} + \{\mathbf{Q},\mathbf{R}\}\) , and \(\mathbf{I}_{\mathbf{Q}}\) remains constant while \(\{\mathbf{Q},\mathbf{R}\}\) tends toward its maximum (or infinity) during the interaction, we have that \(\exp [\mathbf{I}_{\mathbf{Q}}^{\mathrm{r}}]\) tends to a maximum (or infinity). But \(\mathbf{I}_{\mathbf{Q}}^{\mathrm{r}}\) is just the information in the relative system states, which we have adopted as a measure of the nearness to an eigenstate. Therefore, at least in expectation, the relative system states approach eigenstates.  

We have seen that (3.12) is a superposition of states \(\psi_{\mathrm{r}}^{\prime}\) , for each of which the apparatus has recorded a definite value \(\mathbf{r}^{\prime}\) , and the system is left in approximately the eigenstate of the measurement corresponding to \(\mathbf{q} = \mathbf{r}^{\prime} / \mathbf{t}\) . The discontinuous "jump" into an eigenstate is thus only a

---

relative proposition, dependent upon our decomposition of the total wave function into the superposition, and relative to a particularly chosen apparatus value. So far as the complete theory is concerned all elements of the superposition exist simultaneously, and the entire process is quite continuous.  

We have here only a special case of the following general principle which will hold for any situation which is treated entirely wave mechanically:  

PRINCIPLE. For any situation in which the existence of a property \(\mathbf{R}_{\mathrm{i}}\) for a subsystem \(\mathbf{S}_{\mathrm{i}}\) of a composite system S will imply the later property \(\mathbf{Q}_{\mathrm{i}}\) for \(\mathbf{S}\) , then it is also true that an initial state for \(\mathbf{S}_{\mathrm{i}}\) of the form \(\psi^{\mathbf{S}_{1}} = \sum \mathbf{a}_{\mathrm{i}}\psi_{[\mathbf{R}_{\mathrm{i}}]}^{\mathbf{S}_{1}}\) which is a superposition of states with the properties \(\mathbf{R}_{\mathrm{i}}\) , will result in a later state for S of the form \(\psi^{\mathbf{S}} = \sum_{\mathrm{i}}\mathbf{a}_{\mathrm{i}}\psi_{[\mathbf{Q}_{\mathrm{i}}]}^{\mathbf{S}}\) which is also a superposition, of states with the property \(\mathbf{Q}_{\mathrm{i}}\) . That is, for any arrangement of an interaction between two systems \(\mathbf{S}_{\mathrm{i}}\) and \(\mathbf{S}_{\mathrm{2}}\) , which has the property that each initial state \(\phi_{\mathrm{i}}^{\mathbf{S}_{1}}\psi^{\mathbf{S}_{2}}\) will result in a final situation with total state \(\psi_{\mathrm{i}}^{\mathbf{S}_{1} + \mathbf{S}_{2}}\) , an initial state of \(\mathbf{S}_{\mathrm{i}}\) of the form \(\sum_{\mathrm{i}}\mathbf{a}_{\mathrm{i}}\psi_{\mathrm{i}}^{\mathbf{S}_{1}}\) will lead, after interaction, to the superposition  

This follows immediately from the superposition principle for solutions of a linear wave equation. It therefore holds for any system of quantum mechanics for which the superposition principle holds, both particle and field theories, relativistic or not, and is applicable to all physical systems, regardless of size.  

This principle has the far reaching implication that for any possible measurement, for which the initial system state is not an eigenstate, the resulting state of the composite system leads to no definite system state nor any definite apparatus state. The system will not be put into one or another of its eigenstates with the apparatus indicating the corresponding value, and nothing resembling Process 1 can take place.

---

To see that this is indeed the case, suppose that we have a measuring arrangement with the following properties. The initial apparatus state is \(\psi_{0}^{\mathrm{A}}\) . If the system is initially in an eigenstate of the measurement, \(\phi_{1}^{\mathrm{S}}\) , then after a specified time of interaction the total state \(\phi_{1}^{\mathrm{S}}\psi_{0}^{\mathrm{A}}\) will be transformed into a state \(\phi_{1}^{\mathrm{S}}\psi_{1}^{\mathrm{A}}\) , i.e., the system eigenstate shall not be disturbed, and the apparatus state is changed to \(\psi_{1}^{\mathrm{A}}\) , which is different for each \(\phi_{1}^{\mathrm{S}}\) . \((\psi_{1}^{\mathrm{A}}\) may for example be a state describing the apparatus as indicating, by the position of a meter needle, the eigenvalue of \(\phi_{1}^{\mathrm{S}}\) . However, if the initial system state is not an eigenstate but a superposition \(\sum_{i} a_{i} \phi_{1}^{\mathrm{S}}\) , then the final composite system state is also a superposition, \(\sum_{i} a_{i} \phi_{1}^{\mathrm{S}} \psi_{1}^{\mathrm{A}}\) . This follows from the superposition principle since all we need do is superpose our solutions for the eigenstates, \(\phi_{1}^{\mathrm{S}} \psi_{0}^{\mathrm{A}} \rightarrow \phi_{1}^{\mathrm{S}} \psi_{1}^{\mathrm{A}}\) , to arrive at the solution, \(\sum_{i} a_{i} \phi_{1}^{\mathrm{S}} \phi_{0}^{\mathrm{A}} \rightarrow \sum_{i} a_{i} \phi_{1}^{\mathrm{S}} \psi_{i}^{\mathrm{A}}\) , for the general case. Thus in general after a measurement has been performed there will be no definite system state nor any definite apparatus state, even though there is a correlation. It seems as though nothing can ever be settled by such a measurement. Furthermore this result is independent of the size of the apparatus, and remains true for apparatus of quite macroscopic dimensions.  

Suppose, for example, that we coupled a spin measuring device to a cannonball, so that if the spin is up the cannonball will be shifted one foot to the left, while if the spin is down it will be shifted an equal distance to the right. If we now perform a measurement with this arrangement upon a particle whose spin is a superposition of up and down, then the resulting total state will also be a superposition of two states, one in which the cannonball is to the left, and one in which it is to the right. There is no definite position for our macroscopic cannonball!  

This behavior seems to be quite at variance with our observations, since macroscopic objects always appear to us to have definite positions. Can we reconcile this prediction of the purely wave mechanical theory

---

with experience, or must we abandon it as untenable? In order to answer this question we must consider the problem of observation itself within the framework of the theory.

---

## IV. OBSERVATION  

We shall now give an abstract treatment of the problem of observation. In keeping with the spirit of our investigation of the consequences of pure wave mechanics we have no alternative but to introduce observers, considered as purely physical systems, into the theory.  

We saw in the last chapter that in general a measurement (coupling of system and apparatus) had the outcome that neither the system nor the apparatus had any definite state after the interaction - a result seemingly at variance with our experience. However, we do not do justice to the theory of pure wave mechanics until we have investigated what the theory itself says about the appearance of phenomena to observers, rather than hastily concluding that the theory must be incorrect because the actual states of systems as given by the theory seem to contradict our observations.  

We shall see that the introduction of observers can be accomplished in a reasonable manner, and that the theory then predicts that the appearance of phenomena, as the subjective experience of these observers, is precisely in accordance with the predictions of the usual probabilistic interpretation of quantum mechanics.  

## §1. Formulation of the problem  

We are faced with the task of making deductions about the appearance of phenomena on a subjective level, to observers which are considered as purely physical systems and are treated within the theory. In order to accomplish this it is necessary to identify some objective properties of such an observer (states) with subjective knowledge (i.e., perceptions). Thus, in order to say that an observer O has observed the event \(\alpha\) , it

---

is necessary that the state of O has become changed from its former state to a new state which is dependent upon \(\alpha\) .  

It will suffice for our purposes to consider our observers to possess memories (i.e., parts of a relatively permanent nature whose states are in correspondence with the past experience of the observer). In order to make deductions about the subjective experience of an observer it is sufficient to examine the contents of the memory.  

As models for observers we can, if we wish, consider automatically functioning machines, possessing sensory apparata and coupled to recording devices capable of registering past sensory data and machine configurations. We can further suppose that the machine is so constructed that its present actions shall be determined not only by its present sensory data, but by the contents of its memory as well. Such a machine will then be capable of performing a sequence of observations (measurements), and furthermore of deciding upon its future experiments on the basis of past results. We note that if we consider that current sensory data, as well as machine configuration, is immediately recorded in the memory, then the actions of the machine at a given instant can be regarded as a function of the memory contents only, and all relevant experience of the machine is contained in the memory.  

For such machines we are justified in using such phrases as "the machine has perceived A" or "the machine is aware of A" if the occurrence of A is represented in the memory, since the future behavior of the machine will be based upon the occurrence of A. In fact, all of the customary language of subjective experience is quite applicable to such machines, and forms the most natural and useful mode of expression when dealing with their behavior, as is well known to individuals who work with complex automata.  

When dealing quantum mechanically with a system representing an observer we shall ascribe a state function, \(\psi^{\mathrm{O}}\) , to it. When the State \(\psi^{\mathrm{O}}\) describes an observer whose memory contains representations of the

---

events A,B,...,C we shall denote this fact by appending the memory sequence in brackets as a subscript, writing:  

\[\psi_{\mathrm{[A,B,\ldots,C]}}^{0}.\]  

The symbols A,B,...,C, which we shall assume to be ordered time wise, shall therefore stand for memory configurations which are in correspondence with the past experience of the observer. These configurations can be thought of as punches in a paper tape, impressions on a magnetic reel, configurations of a relay switching circuit, or even configurations of brain cells. We only require that they be capable of the interpretation "The observer has experienced the succession of events A,B,...,C." (We shall sometimes write dots in a memory sequence, [...A,B,...,C], to indicate the possible presence of previous memories which are irrelevant to the case being considered.)  

Our problem is, then, to treat the interaction of such observer- systems with other physical systems (observations), within the framework of wave mechanics, and to deduce the resulting memory configurations, which we can then interpret as the subjective experiences of the observers.  

We begin by defining what shall constitute a "good" observation. A good observation of a quantity A, with eigenfunctions \(\{\phi_{i}\}\) for a system S, by an observer whose initial state is \(\psi_{\mathrm{[...]}}^{0}\) , shall consist of an interaction which, in a specified period of time, transforms each (total) state  

\[\psi^{S + O} = \phi_{i}\psi_{\mathrm{[...]}}^{O}\]  

into a new state  

\[\psi^{S + O^{\prime}} = \phi_{i}\psi_{\mathrm{[...},a_{i}]}^{O},\]  

where \(a_{i}\) characterizes the state \(\phi_{i}\) . (It might stand for a recording of the eigenvalue, for example.) That is, our requirement is that the system state, if it is an eigenstate, shall be unchanged, and that the observer

---

state shall change so as to describe an observer that is "aware" of which eigenfunction it is, i.e., some property is recorded in the memory of the observer which characterizes \(\phi_{i}\) , such as the eigenvalue. The requirement that the eigenstates for the system be unchanged is necessary if the observation is to be significant (repeatable), and the requirement that the observer state change in a manner which is different for each eigenfunction is necessary if we are to be able to call the interaction an observation at all.  

## \(\S 2\) . Deductions  

From these requirements we shall first deduce the result of an observation upon a system which is not in an eigenstate of the observation. We know, by our previous remark upon what constitutes a good observation that the interaction transforms states \(\phi_{i}\psi_{[..]}^{0}\) into states \(\phi_{i}\psi_{[..,\alpha_{i}]}^{0}\) . Consequently we can simply superpose these solutions of the wave equation to arrive at the final state for the case of an arbitrary initial system state. Thus if the initial system state is not an eigenstate, but a general state \(\sum_{i} a_{i} \phi_{i}\) , we get for the final total state:  

\[\psi^{S + O} = \sum_{i} a_{i} \phi_{i} \psi_{[..,\alpha_{i}]}^{0}. \quad (2.1)\]  

This remains true also in the presence of further systems which do not interact for the time of measurement. Thus, if systems \(S_{1}, S_{2}, \ldots , S_{n}\) are present as well as \(O\) , with original states \(\psi^{S_{1}}, \psi^{S_{2}}, \ldots , \psi^{S_{n}}\) , and the only interaction during the time of measurement is between \(S_{1}\) and \(O\) , the result of the measurement will be the transformation of the initial total state:  

\[\psi^{S_{1} + S_{2} + \ldots + S_{n} + O} = \psi^{S_{1}} \psi^{S_{2}} \ldots \psi^{S_{n}} \psi_{[..]}^{O}\]  

into the final state:  

\[\psi^{S_{1} + S_{2} + \ldots +S_{n} + O} = \sum_{i} a_{i} \phi_{i}^{S_{1}} \psi^{S_{2}} \ldots \psi^{S_{n}}\psi_{[..,\alpha_{i}]}^{O} \quad (2.2)\]

---

where \(\mathbf{a}_{\mathbf{i}} = \left(\phi_{\mathbf{i}}^{S_{1}},\psi_{\mathbf{i}}^{S_{1}}\right)\) and \(\phi_{\mathbf{i}}^{S_{1}}\) are eigenfunctions of the observation.  

Thus we arrive at the general rule for the transformation of total state functions which describe systems within which observation processes occur:  

Rule 1. The observation of a quantity A, with eigenfunctions \(\phi_{\mathbf{i}}^{S_{1}}\) , in a system \(S_{1}\) by the observer O, transforms the total state according to:  

\[\psi^{S_{1}}\psi^{S_{2}}\dots \psi^{S_{n}}\psi_{[\dots ]}^{0}\rightarrow \sum_{\mathbf{i}}\mathbf{a}_{\mathbf{i}}\phi_{\mathbf{i}}^{S_{1}}\psi^{S_{2}}\dots \psi^{S_{n}}\psi_{\mathbf{i}[\dots ,\alpha_{\mathbf{i}}]}^{0},\] \[\mathrm{where~}\mathbf{a}_{\mathbf{i}} = \left(\phi_{\mathbf{i}}^{S_{1}},\phi_{\mathbf{i}}^{S_{1}}\right).\]  

If we next consider a second observation to be made, where our total state is now a superposition, we can apply Rule 1 separately to each element of the superposition, since each element separately obeys the wave equation and behaves independently of the remaining elements, and then superpose the results to obtain the final solution. We formulate this as:  

Rule 2. Rule 1 may be applied separately to each element of a superposition of total system states, the results being superposed to obtain the final total state. Thus, a determination of B, with eigenfunctions \(\eta_{j}^{S_{2}}\) , on \(S_{2}\) by the observer O transforms the total state  

\[\sum_{\mathbf{i}}\mathbf{a}_{\mathbf{i}}\phi_{\mathbf{i}}^{S_{1}}{\psi}^{S_{2}}\dots \psi^{S_{n}}{\psi}_{\mathbf{i}[\dots ,\alpha_{\mathbf{i}}]}^{0}\]  

into the state  

\[\sum_{\mathbf{i},\mathbf{j}}\mathbf{a}_{\mathbf{i}}\mathbf{b}_{\mathbf{j}}\phi_{\mathbf{i}}^{S_{1}}\eta_{\mathbf{j}}^{S_{2}}\psi^{S_{3}}\dots \psi^{S_{n}}\psi_{\mathbf{i}[\dots ,\alpha_{j},\beta_{j}]}^{0}\]  

where \(\mathbf{b}_{\mathbf{j}} = \left(\eta_{\mathbf{j}}^{S_{2}},\psi^{S_{2}}\right)\) , which follows from the application of Rule 1 to each element \(\phi_{\mathbf{i}}^{S_{1}}\psi^{S_{2}}\dots \psi^{s_{n}}\psi_{\mathbf{i}[\dots ,\alpha_{\mathbf{i}}]}^{O}\) , and then superposing the results with the coefficients \(\mathbf{a}_{\mathbf{i}}\) .

---

These two rules, which follow directly from the superposition principle, give us a convenient method for determining final total states for any number of observation processes in any combinations. We must now seek the interpretation of such final total states.  

Let us consider the simple case of a single observation of a quantity A, with eigenfunctions \(\phi_{\mathrm{i}}\) , in the system S with initial state \(\psi^{\mathrm{S}}\) , by an observer O whose initial state is \(\psi_{\left[\dots \right]}^{\mathrm{O}}\) . The final result is, as we have seen, the superposition:  

\[\psi^{\prime}\mathrm{S} + \mathrm{O} = \sum_{\mathrm{i}}\mathrm{a}_{\mathrm{i}}\phi_{\mathrm{i}}\psi_{\mathrm{i}\left[\dots ,\alpha_{\mathrm{i}}\right]}^{\mathrm{O}}. \quad (2.3)\]  

We note that there is no longer any independent system state or observer state, although the two have become correlated in a one- one manner. However, in each element of the superposition (2.3), \(\phi_{\mathrm{i}}\psi_{\mathrm{i}\left[\dots ,\alpha_{\mathrm{i}}^{\prime}\right]}^{\mathrm{O}}\) , the object- system state is a particular eigenstate of the observer, and furthermore the observer- system state describes the observer as definitely perceiving that particular system state.\(^1\) It is this correlation which allows one to maintain the interpretation that a measurement has been performed.  

We now carry the discussion a step further and allow the observer- system to repeat the observation. Then according to Rule 2 we arrive at the total state after the second observation:

---

\[\psi^{\sim \mathrm{S} + \mathrm{O}} = \sum_{\mathrm{i}}\mathrm{a}_{\mathrm{i}}\phi_{\mathrm{i}}\psi_{\mathrm{ii}[\ldots ,\alpha_{\mathrm{i}},\alpha_{\mathrm{i}}]}^{\mathrm{O}}~. \quad (2.4)\]  

Again, we see that each element of (2.4), \(\phi_{\mathrm{i}}\psi_{\mathrm{ii}[\ldots ,\alpha_{\mathrm{i}}, \alpha_{\mathrm{i}}]}^{\mathrm{O}}\), describes a system eigenstate, but this time also describes the observer as having obtained the same result for each of the two observations. Thus for every separate state of the observer in the final superposition, the result of the observation was repeatable, even though different for different states. This repeatability is, of course, a consequence of the fact that after an observation the relative system state for a particular observer state is the corresponding eigenstate.  

Let us suppose now that an observer- system \(\mathbf{O}\) , with initial state \(\psi_{\mathrm{[...]}}^{\mathrm{O}}\) measures the same quantity A in a number of separate identical systems which are initially in the same state, \(\psi_{1}^{\mathrm{S}_{1}} = \psi_{2}^{\mathrm{S}_{2}} = \ldots = \psi_{n}^{\mathrm{S}_{n}} = \sum_{\mathrm{i}}\mathrm{a}_{\mathrm{i}}\phi_{\mathrm{i}}\) (where the \(\phi_{\mathrm{i}}\) are, as usual, eigenfunctions of A). The initial total state function is then  

\[\psi_{0}^{\mathrm{S}_{1} + \mathrm{S}_{2} + \ldots +\mathrm{S}_{n} + \mathrm{O}} = \psi^{\mathrm{S}_{1}}\psi^{\mathrm{S}_{2}}\ldots \psi^{\mathrm{S}_{n}}\psi_{\mathrm{[...]}}^{\mathrm{O}}. \quad (2.3)\]  

We shall assume that the measurements are performed on the systems in the order \(\mathbf{S}_{1}, \mathbf{S}_{2}, \ldots , \mathbf{S}_{n}\) . Then the total state after the first measurement will be, by Rule 1,  

\[\psi_{1}^{\mathrm{S}_{1} + \mathrm{S}_{2} + \ldots +\mathrm{S}_{\mathrm{n}} + \mathrm{O}} = \sum_{\mathrm{i}}\mathrm{a}_{\mathrm{i}}\phi_{1}^{\mathrm{S}_{1}}\psi^{\mathrm{S}_{2}}\ldots \psi^{\mathrm{S}_{\mathrm{n}}}\psi_{\mathrm{i}[\ldots ,\alpha_{\mathrm{i}}]}^{\mathrm{O}} \quad (2.4)\]  

After the second measurement it will be, by Rule 2,  

\[\psi_{2}^{\mathrm{S}_{1} + \mathrm{S}_{2} + \ldots \mathrm{S}_{\mathrm{n}} + \mathrm{O}} = \sum_{\mathrm{i},\mathrm{j}}\mathrm{a}_{\mathrm{i}}\mathrm{a}_{\mathrm{j}}\phi_{\mathrm{i}}^{\mathrm{S}_{1}}\phi_{\mathrm{j}}^{\mathrm{S}_{2}}\psi^{\mathrm{S}_{3}}\ldots \psi^{\mathrm{S}_{\mathrm{n}}}\psi_{\mathrm{i}[\ldots , \alpha_{\mathrm{i}}]}^{\mathrm{O}}\phi_{\mathrm{j}}^{\mathrm{S}_{1}}\phi_{\mathrm{j}}^{\mathrm{S}_{2}}\psi^{\mathrm{s}_{3}}\ldots \psi^{\mathrm{S}_{\mathrm{n}}}\psi_{\mathrm{i}[\dots , \alpha_{\mathrm{i}}]}^{\mathrm{O}}\phi_{\mathrm{j}}^{\mathrm{S}_{\mathrm{n}}}\psi_{\mathrm{i}[\dots , \alpha_{\mathrm{i}}} \psi_{\mathrm{i}[\dots , \alpha_{\mathrm{i}}]}^{\mathrm{O}}\psi_{\mathrm{i}[\dots , \alpha_{\mathrm{i}}]}^{\mathrm{O}}\]

---

and in general, after \(r\) measurements have taken place \((r \leq n)\) Rule 2 gives the result:  

\[\psi_{r} = \sum_{i,j,\ldots ,k}a_{i}a_{j}\ldots a_{k}\phi_{1}^{S_{1}}\phi_{j}^{S_{2}}\ldots \phi_{k}^{S_{r}}\psi^{S_{r + 1}}\ldots \psi^{S_{n}}\psi_{i j\ldots k[\ldots ,a_{1}^{1},a_{2}^{2},\ldots ,a_{k}^{1}]}^{O}. \quad (2.6)\]  

We can give this state, \(\psi_{r}\) , the following interpretation. It consists of a superposition of states:  

\[\psi_{i j\ldots k}^{\prime} = \phi_{1}^{S_{1}}\phi_{j}^{S_{2}}\ldots \phi_{\mathrm{k}}^{S_{r}}\psi^{S_{r + 1}}\ldots \psi^{S_{r}}\psi_{i j\ldots k[\ldots ,a_{1}^{1},a_{j}^{2},\ldots ,a_{k}^{1}]}^{O} \quad (2.7)\]  

each of which describes the observer with a definite memory sequence \([ \ldots , a_{1}^{1}, a_{2}^{2}, \ldots , a_{k}^{1} ]\) , and relative to whom the (observed system states are the corresponding eigenfunctions \(\phi_{1}^{S_{1}}, \phi_{j}^{S_{2}}, \ldots , \phi_{k}^{S_{r}}\) , the remaining systems, \(S_{r + 1}, \ldots , S_{n}\) , being unaltered.  

In the language of subjective experience, the observer which is described by a typical element, \(\psi_{i j\ldots k}^{\prime}\) of the superposition has perceived an apparently random sequence of definite results for the observations. It is furthermore true, since in each element the system has been left in an eigenstate of the measurement, that if at this stage a redetermination of an earlier system observation \((S_{p})\) takes place, every element of the resulting final superposition will describe the observer with a memory configuration of the form \([ \ldots , a_{1}^{1}, \ldots , a_{k}^{f}, \ldots , a_{k}^{f}, a_{k}^{f}]\) in which the earlier memory coincides with the later - i.e., the memory states are correlated. It will thus appear to the observer which is described by a typical element of the superposition that each initial observation on a system caused the system to "jump" into an eigenstate in a random fashion and thereafter remain there for subsequent measurements on the same system. Therefore, qualitatively, at least, the probabilistic assertions of Process 1 appear to be valid to the observer described by a typical element of the final superposition.  

In order to establish quantitative results, we must put some sort of measure (weighting) on the elements of a final superposition. This is

---

necessary to be able to make assertions which will hold for almost all of the observers described by elements of a superposition. In order to make quantitative statements about the relative frequencies of the different possible results of observation which are recorded in the memory of a typical observer we must have a method of selecting a typical observer.  

Let us therefore consider the search for a general scheme for assigning a measure to the elements of a superposition of orthogonal states \(\sum \mathbf{a}_{i} \phi_{i}\) . We require then a positive function \(\mathcal{M}\) of the complex coefficients of the elements of the superposition, so that \(\mathcal{M}(\mathbf{a}_{i})\) shall be the measure assigned to the element \(\phi_{i}\) . In order that this general scheme shall be unambiguous we must first require that the states themselves always be normalized, so that we can distinguish the coefficients from the states. However, we can still only determine the coefficients, in distinction to the states, up to an arbitrary phase factor, and hence the function \(\mathcal{M}\) must be a function of the amplitudes of the coefficients alone, (i.e., \(\mathcal{M}(\mathbf{a}_{i}) = \mathcal{M}(\sqrt{\mathbf{a}_{i}^{*} \mathbf{a}_{i}})\) ), in order to avoid ambiguities.  

If we now impose the additivity requirement that if we regard a subset of the superposition, say \(\sum_{i = 1}^{n} \mathbf{a}_{i} \phi_{i}\) , as a single element \(\alpha \phi^{\prime}\) :  

\[\alpha \phi^{\prime} = \sum_{i = 1}^{n} \mathbf{a}_{i} \phi_{i}, \quad (2.8)\]  

then the measure assigned to \(\phi^{\prime}\) shall be the sum of the measures assigned to the \(\phi_{i}\) (i from 1 to n):  

\[\mathcal{M}(\alpha) = \sum_{i} \mathcal{M}(\mathbf{a}_{i}), \quad (2.9)\]  

then we have already restricted the choice of \(\mathcal{M}\) to the square amplitude alone. \(\mathcal{M}(\mathbf{a}_{i}) = \mathbf{a}_{i}^{*} \mathbf{a}_{i}\) , apart from a multiplicative constant.)  

To see this we note that the normality of \(\phi^{\prime}\) requires that \(|\alpha | = \sqrt{\sum_{i = 1}^{n} \mathbf{a}_{i}^{*} \mathbf{a}_{i}}\) . From our remarks upon the dependence of \(\mathcal{M}\) upon the amplitude alone, we replace the \(\mathbf{a}_{i}\) by their amplitudes \(\mu_{i} = |\mathbf{a}_{i}|\) .

---

(2.9) then requires that  

\[\mathfrak{M}(a) = \mathfrak{M}\left(\sqrt{\sum\mathbf{a}_{1}^{*}\mathbf{a}_{1}}\right) = \mathfrak{M}\left(\sqrt{\sum\mathbf{\mu}_{1}^{2}}\right) = \sum \mathfrak{M}(\mu_{1}) = \sum \mathfrak{M}(\sqrt{\mu_{1}^{2}}). \quad (2.10)\]  

Defining a new function \(\mathbf{g}(\mathbf{x})\) :  

\[\mathbf{g}(\mathbf{x}) = \mathfrak{M}(\sqrt{\mathbf{x}}), \quad (2.11)\]  

we see that (2.10) requires that  

\[\mathbf{g}\left(\sum \mu_{1}^{2}\right) = \sum \mathbf{g}(\mu_{1}^{2}), \quad (2.12)\]  

so that \(\mathbf{g}\) is restricted to be linear and necessarily has the form:  

\[\mathbf{g}(\mathbf{x}) = \mathbf{c}\mathbf{x}\qquad (\mathbf{c}\mathrm{~constant}). \quad (2.13)\]  

Therefore \(\mathbf{g}(\mathbf{x}^{2}) = \mathbf{c}\mathbf{x}^{2} = \mathfrak{M}\sqrt{\mathbf{x}^{2}} = \mathfrak{M}(\mathbf{x})\) and we have deduced that \(\mathfrak{M}\) is restricted to the form  

\[\mathfrak{M}(\mathbf{a}_{i}) = \mathfrak{M}(\mu_{i}) = \mathbf{c}\mu_{i}^{2} = \mathbf{c}\mathbf{a}_{i}^{*}\mathbf{a}_{i}, \quad (2.14)\]  

and we have shown that the only choice of measure consistent with our additivity requirement is the square amplitude measure, apart from an arbitrary multiplicative constant which may be fixed, if desired, by normalization requirements. (The requirement that the total measure be unity implies that this constant is 1. )  

The situation here is fully analogous to that of classical statistical mechanics, where one puts a measure on trajectories of systems in the phase space by placing a measure on the phase space itself, and then making assertions which hold for "almost all" trajectories (such as ergodicity, quasi- ergodicity, etc). This notion of "almost all" depends here also upon the choice of measure, which is in this case taken to be Lebesgue measure on the phase space. One could, of course, contradict

---

the statements of classical statistical mechanics by choosing a measure for which only the exceptional trajectories had nonzero measure. Nevertheless the choice of Lebesgue measure on the phase space can be justified by the fact that it is the only choice for which the "conservation of probability" holds, (Liouville's theorem) and hence the only choice which makes possible any reasonable statistical deductions at all.  

In our case, we wish to make statements about "trajectories" of observers. However, for us a trajectory is constantly branching (transforming from state to superposition) with each successive measurement. To have a requirement analogous to the "conservation of probability" in the classical case, we demand that the measure assigned to a trajectory at one time shall equal the sum of the measures of its separate branches at a later time. This is precisely the additivity requirement which we imposed and which leads uniquely to the choice of square- amplitude measure. Our procedure is therefore quite as justified as that of classical statistical mechanics.  

Having deduced that there is a unique measure which will satisfy our requirements, the square- amplitude measure, we continue our deduction. This measure then assigns to the \(\mathbf{i},\mathbf{j},\dots ,\mathbf{k}^{\mathrm{th}}\) element of the superposition (2.6),  

\[\phi_{1}^{S_{1}}\phi_{2}^{S_{2}}\dots \phi_{k}^{S_{r}}\psi^{S_{r + 1}}\dots \psi^{S_{n}}\psi_{i j\dots k}^{O}\dots \alpha_{1}^{1}\alpha_{j}^{2}\dots \alpha_{k}^{r}\} , \quad (2.15)\]  

the measure (weight)  

\[\mathbf{M}_{\mathbf{i}\mathbf{j}\dots \mathbf{k}} = (\mathbf{a}_{\mathbf{i}}\mathbf{a}_{\mathbf{j}}\dots \mathbf{a}_{\mathbf{k}})^{*}(\mathbf{a}_{\mathbf{i}}\mathbf{a}_{\mathbf{j}}\dots \mathbf{a}_{\mathbf{k}})~, \quad (2.16)\]  

so that the observer state with memory configuration \([\dots ,\alpha_{1}^{1},\alpha_{j}^{2},\dots ,\alpha_{k}^{r}]\) is assigned the measure \(\mathbf{a}_{1}^{*}\mathbf{a}_{1}\mathbf{a}_{j}^{*}\mathbf{a}_{j}\dots \mathbf{a}_{k}^{*}\mathbf{a}_{k} = \mathbf{M}_{\mathbf{i}\mathbf{j}\dots \mathbf{k}}\) . We see immediately that this is a product measure, namely  

\[\mathbf{M}_{\mathbf{i}\mathbf{j}\dots \mathbf{k}} = \mathbf{M}_{\mathbf{i}}\mathbf{M}_{\mathbf{j}}\dots \mathbf{M}_{\mathbf{k}}~, \quad (2.17)\]  

where  

\[\mathbf{M}_{\ell} = \mathbf{a}_{\ell}^{*}\mathbf{a}_{\ell}~,\]

---

so that the measure assigned to a particular memory sequence \([ \dots , a_1^1, a_2^2, \dots , a_k^1 ]\) is simply the product of the measures for the individual components of the memory sequence.  

We notice now a direct correspondence of our measure structure to the probability theory of random sequences. Namely, if we were to regard the \(\mathbf{M}_{\mathrm{ij}\dots \mathbf{k}}\) as probabilities for the sequences \([ \dots , a_1^1, a_2^2, \dots ,a_k^1 ]\) , then the sequences are equivalent to the random sequences which are generated by ascribing to each term the independent probabilities \(\mathbf{M}_{\ell} = \mathbf{a}_{\ell}^{\ast}\mathbf{a}_{\ell}\) . Now the probability theory is equivalent to measure theory mathematically, so that we can make use of it, while keeping in mind that all results should be translated back to measure theoretic language.  

Thus, in particular, if we consider the sequences to become longer and longer (more and more observations performed) each memory sequence of the final superposition will satisfy any given criterion for a randomly generated sequence, generated by the independent probabilities \(\mathbf{a}_1^*\mathbf{a}_1\) , except for a set of total measure which tends toward zero as the number of observations becomes unlimited. Hence all averages of functions over any memory sequence, including the special case of frequencies, can be computed from the probabilities \(\mathbf{a}_1^*\mathbf{a}_1\) , except for a set of memory sequences of measure zero. We have therefore shown that the statistical assertions of Process 1 will appear to be valid to almost all observers described by separate elements of the superposition (2.6), in the limit as the number of observations goes to infinity.  

While we have so far considered only sequences of observations of the same quantity upon identical systems, the result is equally true for arbitrary sequences of observations. For example, the sequence of observations of the quantities \(\mathbf{A}^1\) , \(\mathbf{A}^2\) ,..., \(\mathbf{A}^n\) ,... with (generally different) eigenfunction sets \(\{\phi_1^1, \{\phi_2^2\} , \dots , \{\phi_k^n\} , \dots\) applied successively to the systems \(S_1, S_2, \dots , S_n, \dots\) , with (arbitrary) initial states \(\psi^{S_1}, \psi^{S_2}, \dots , \psi^{S_n}\) ,... transforms the total initial state:  

\[\psi^{S_1 + \dots +S_n + O} = \psi^{S_1}\psi^{S_2}\dots \psi^{S_n}\psi_{[..]}^{O} \quad (2.18)\]

---

by rules 1 and 2, into the final state:  

\[\psi^{S_{1} + S_{2} + \dots +S_{n} + O} = \sum_{i,j,\dots ,k}(\phi_{i}^{1}\psi^{S_{1}})(\phi_{j}^{2}\psi^{S_{2}})\dots (\phi_{k}^{n}\psi^{S_{n}})\] \[\qquad \dots \phi_{i}^{1}\phi_{j}^{2}\dots \phi_{k}^{n}\dots \psi_{[}\dots \alpha_{i}^{1}\alpha_{j}^{2}\dots \alpha_{k}^{n}\dots ]^{\prime}\]  

where the memory sequence element \(\alpha_{\ell}^{\mathrm{r}}\) characterizes the \(\ell^{\mathrm{th}}\) eigenfunction, \(\phi_{\ell}^{\mathrm{r}}\) of the operator \(\mathbf{A}^{\mathrm{r}}\) . Again the square amplitude measure for each element of the superposition (2.19) reduces to the product measure of the individual memory element measures, \(\left|(\phi_{\ell}^{\mathrm{r}}\psi^{\mathrm{S}_{\mathrm{r}}})\right|^{2}\) for the memory sequence element \(\alpha_{\ell}^{\mathrm{r}}\) . Therefore, the memory sequence of a typical element of (2.19) has all the characteristics of a random sequence, with individual, independent (and now different), probabilities \(\left|(\phi_{\ell}^{\mathrm{r}}\psi^{\mathrm{S}_{\mathrm{r}}})^{\mathrm{2}}\right|^{2}\) for the \(\mathrm{r}^{\mathrm{th}}\) memory state.  

Finally, we can generalize to the case where several observations are allowed to be performed upon the same system. For example, if we permit the observation of a new quantity \(\mathbf{B}\) , (eigenfunctions \(\eta_{\mathrm{m}}\) , memory characterization \(\beta_{\mathrm{i}}\) ) upon the system \(\mathbf{S}_{\mathrm{r}}\) for which \(\mathbf{A}^{\mathrm{r}}\) has already been observed, then the state (2.19):  

\[\psi^{\prime} = \sum_{i,\ell ,\dots ,k}(\phi_{i}^{1}\psi^{S_{1}})\dots (\phi_{\ell}^{\mathrm{r}}\psi^{S_{\mathrm{r}}})\dots (\phi_{k}^{n}\psi^{S_{\mathrm{n}}})\] \[\phi_{i}^{1}\dots \phi_{\ell}^{\mathrm{r}}\dots \phi_{k}^{\mathrm{n}}\dots \psi_{[}\dots \alpha_{i}^{1}\dots \alpha_{\ell}^{\mathrm{r}}\dots \alpha_{k}^{\mathrm{n}}\dots ]\]  

is transformed by Rule 2 into the state:  

\[\psi^{\prime} = \sum_{i,\dots ,\ell ,\dots ,k,m}(\phi_{i}^{1}\psi^{S_{1}})\dots (\phi_{\ell}^{r}\psi^{S_{r}})\dots (\phi_{k}^{n}\psi^{S_{n}})(\eta_{\mathrm{m}}^{r}\phi_{\ell}^{r})\] \[\phi_{i}^{1}\dots \phi_{\mu}^{r - 1}\dots \eta_{\mu}^{r}\dots \phi_{\nu}^{r + 1}\dots \phi_{\nu}^{r}\dots \psi_{[}\dots \alpha_{i}^{1}\dots \alpha_{\ell}^{r}\dots \alpha_{k}^{n}\dots \beta_{\mathrm{m}}^{r}\dots ]\]

---

The relative system states for \(S\) have been changed from the eigenstates of \(A^{r}, \{\phi_{i}^{r}\}_{i}\) , to the eigenstates of \(B^{r}, \{\eta_{m}^{r}\}_{m}\) . We notice further that, with respect to our measure on the superposition, the memory sequences still have the character of random sequences, but of random sequences for which the individual terms are no longer independent. The memory states \(\beta_{m}^{r}\) now depend upon the memory states \(a_{\ell}^{r}\) which represent the result of the previous measurement upon the same system, \(S_{r}\) . The joint (normalized) measure for this pair of memory states, conditioned by fixed values for remaining memory states is:  

\[\begin{array}{r l} & {M_{1}^{1}\dots a_{\mu}^{r - 1}a_{\nu}^{r + 1}\dots a_{k}^{r}(a_{\ell}^{r}\beta_{m}^{r}) = \frac{\mathrm{M}(a_{1}^{1},\dots,a_{\ell}^{1},\dots,a_{k}^{n},\beta_{m}^{r})}{\sum_{\ell,m}\mathrm{M}(a_{1}^{2},\dots,a_{\ell}^{2},\dots,a_{k}^{n},\beta_{m}^{r})}}\\ & {= \frac{|\langle\phi_{1}^{1},\psi^{S_{1}}\rangle\dots\langle\phi_{\ell}^{1},\psi^{S_{r}}\rangle\dots\langle\phi_{k}^{n},\psi^{S_{n}}\rangle(\eta_{m}^{r},\phi_{\ell}^{r})|^{2}}{\sum_{\ell,m}|\langle\phi_{1}^{1},\psi^{S_{1}}\rangle\dots\langle\phi_{\nu}^{r},\psi^{S_{r}}\rangle\dots\langle\phi_{k}^{n},\psi^{s_{n}}\rangle(\eta_{m}^{r},\phi_{\ell}^{r})|^{2}}}\\ & {= |\langle\phi_{\ell}^{r},\psi^{S_{r}}\rangle|^{2}|\langle\eta_{m}^{r},\phi_{\ell}^{r}\rangle|^{2}.} \end{array} \quad (2.22)\]  

The joint measure (2.15) is, first of all, independent of the memory states for the remaining systems \((S_{1} \dots S_{n}\) excluding \(S_{r}\) ). Second, the dependence of \(\beta_{m}^{r}\) on \(a_{\ell}^{r}\) is equivalent, measure theoretically, to that given by the stochastic process \(^{3}\) which converts the states \(\phi_{\ell}^{r}\) into the states \(\eta_{m}^{r}\) with transition probabilities:  

\[T_{\ell m} = \cdot \mathrm{Prob.} (\phi_{\ell}^{r} \to \eta_{m}^{r}) = |(\eta_{m}^{r}, \phi_{\ell}^{r})|^{2}. \quad (2.23)\]

---

If we were to allow yet another quantity C to be measured in \(\mathbf{S}_{\mathbf{r}}\) , the new memory states \(a_{\mathbf{p}}^{\mathbf{r}}\) corresponding to the eigenfunctions of C would have a similar dependence upon the previous states \(\beta_{\mathbf{m}}^{\mathbf{r}}\) , but no direct dependence on the still earlier states \(a_{\mathbf{f}}^{\mathbf{r}}\) . This dependence upon only the previous result of observation is a consequence of the fact that the relative system states are completely determined by the last observation.  

We can therefore summarize the situation for an arbitrary sequence of observations, upon the same or different systems in any order, and for which the number of observations of each quantity in each system is very large, with the following result:  

Except for a set of memory sequences of measure nearly zero, the averages of any functions over a memory sequence can be calculated approximately by the use of the independent probabilities given by Process 1 for each initial observation, on a system, and by the use of the transition probabilities (2.23) for succeeding observations upon the same system. In the limit, as the number of all types of observations goes to infinity the calculation is exact, and the exceptional set has measure zero.  

This prescription for the calculation of averages over memory sequences by probabilities assigned to individual elements is precisely that of the orthodox theory (Process 1). Therefore all predictions of the usual theory will appear to be valid to the observer in almost all observer states, since these predictions hold for almost all memory sequences.  

In particular, the uncertainty principle is never violated, since, as above, the latest measurement upon a system supplies all possible information about the relative system state, so that there is no direct correlation between any earlier results of observation on the system, and the succeeding observation. Any observation of a quantity B, between two successive observations of quantity A (all on the same system) will destroy the one- one correspondence between the earlier and later memory states for the result of A. Thus for alternating observations of different quantities there are fundamental limitations upon the correlations between memory states for the same observed quantity, these limitations expressing the content of the uncertainty principle.

---

In conclusion, we have described in this section processes involving an idealized observer, processes which are entirely deterministic and continuous from the over- all viewpoint (the total state function is presumed to satisfy a wave equation at all times) but whose result is a superposition, each element of which describes the observer with a different memory state. We have seen that in almost all of these observer states it appears to the observer that the probabilistic aspects of the usual form of quantum theory are valid. We have thus seen how pure wave mechanics, without any initial probability assertions, can lead to these notions on a subjective level, as appearances to observers.  

## \(\S 3\) . Several observers  

We shall now consider the consequences of our scheme when several observers are allowed to interact with the same systems, as well as with one another (communication). In the following discussion observers shall be denoted by \(\mathbf{O}_1,\mathbf{O}_2,\dots\) , other systems by \(\mathbf{S}_1,\mathbf{S}_2,\dots\) , and observables by operators A, B, C, with eigenfunctions \(\{\phi_i\},\{\eta_j\},\{\xi_k\}\) respectively. The symbols \(a_i,\beta_j,\gamma_k\) , occurring in memory sequences shall refer to characteristics of the states \(\phi_i,\eta_j,\xi_k\) , respectively. \((\psi_{i\dots ,\alpha_i}^{O})\) is interpreted as describing an observer, \(\mathbf{O}_j\) , who has just observed the eigenvalue corresponding to \(\phi_i\) , i.e., who is "aware" that the system is in state \(\phi_i\) .)  

We shall also wish to allow communication among the observers, which we view as an interaction by means of which the memory sequences of different observers become correlated. (For example, the transfer of impulses from the magnetic tape memory of one mechanical observer to that of another constitutes such a transfer of information.)<sup>4</sup> We shall regard these processes as observations made by one observer on another and shall use the notation that

---

\[\psi_{i[ \dots ,a_{i}]}^{O_{j}}O_{k}\]  

represents a state function describing an observer \(O_{j}\) who has obtained the information \(a_{i}\) from another observer, \(O_{k}\) . Thus the obtaining of information about \(A\) from \(O_{1}\) by \(O_{2}\) will transform the state  

\[\psi_{i[ \dots ,a_{i}]}^{O_{1}}\psi_{[ \dots ,a_{i}]}^{O_{2}}\]  

into the state  

\[\psi_{i[ \dots ,a_{i}]}^{O_{1}} \psi_{[ \dots ,a_{i}]}^{O_{2}} \psi_{[ \dots ,a_{i}]}^{O_{1}} \psi_{[ \dots,a_{i}]}^{O_{2}} \psi_{[ \dots,a_{i}]}^{O_{1}} \psi_{[ \dots,a_{i}]}^{0_{2}} \psi_{[ \dots,a_{i}]}^{0_{2}} \psi_{i[ \dots,a_{i}]}^{0_{2}} \psi_{i[ \dots, a_{i}]}^{0_{2}} \psi_{i[ \dots,a_{i}]} \psi_{i[ \dots,a_{i}]} \psi_{i[ \dots, a_{i}]} \psi_{i[ \dots,a_{i}]} \psi_{[ \dots,a_{i}]} \psi_{i[ \dots,a_{i}]}\]  

Rules 1 and 2 are, of course, equally applicable to these interactions. We shall now illustrate the possibilities for several observers, by considering several cases.  

Case 1: We allow two observers to separately observe the same quantity in a system, and then compare results.  

We suppose that first observer \(O_{1}\) observes the quantity \(A\) for the system \(S\) . Then by Rule 1 the original state  

\[\psi^{S + O_{1} + O_{2}} = \psi^{S}\psi_{[ \dots ]}^{O_{1}}\psi_{[ \dots ]}^{O_{2}}\]  

is transformed into the state  

\[\psi^{\prime} = \sum_{i}\left(\phi_{i}^{S}\psi^{S}\right)\phi_{i}^{S}\psi_{i[ \dots ,a_{i}]}^{O_{1}}\psi_{[  \dots ]}^{O_{2}} \quad (3.2)\]  

We now suppose that \(O_{2}\) observes \(A\) , and by Rule 2 the state becomes:  

\[\psi^{\prime \prime} = \sum_{i}\left(\phi_{i}^{S}\psi^{S})\phi_{i}^{S}\psi_{i[ \dots ,a_{i}]}^{O1}\psi_{i[ \dots ,a_{i}]}^{O2} \quad (3.3)\]

---

We now allow \(O_2\) to "consult" \(O_1\) , which leads in the same fashion from (3.1) and Rule 2 to the final state  

\[\psi^{\prime \prime} = \sum_{\mathbf{i}}(\phi_{\mathbf{i}}^{\mathrm{S}}\psi^{\mathrm{S}})\phi_{\mathbf{i}}^{\mathrm{S}}\psi_{\mathbf{i}[1,\dots ,a_{\mathbf{i}}]}^{\mathrm{O}_{1}}\psi_{\mathbf{i}[2,\dots ,a_{\mathbf{i}},a_{\mathbf{i}}]}^{\mathrm{O}_{2}}. \quad (3.4)\]  

Thus, for every element of the superposition the information obtained from \(O_1\) agrees with that obtained directly from the system. This means that observers who have separately observed the same quantity will always agree with each other.  

Furthermore, it is obvious at this point that the same result, (4.4), is obtained if \(O_2\) first consults \(O_1\) , then performs the direct observation, except that the memory sequence for \(O_2\) is reversed \(\{\ldots ,a_{\mathbf{i}},a_{\mathbf{i}}\}\) instead of \(\{\ldots ,a_{\mathbf{i}},a_{\mathbf{i}}^{- 1}\}\) . There is still perfect agreement in every element of the superposition. Therefore, information obtained from another observer is always reliable, since subsequent direct observation will always verify it. We thus see the central role played by correlations in wave functions for the preservation of consistency in situations where several observers are allowed to consult one another. It is the transitivity of correlation in these cases (that if \(S_1\) is correlated to \(S_2\) , and \(S_2\) to \(S_3\) , then so is \(S_1\) to \(S_2\) ) which is responsible for this consistency.  

Case 2: We allow two observers to measure separately two different, noncommuting quantities in the same system.  

Assume that first \(O_1\) observes A for the system, so that, as before, the initial state \(\psi^{\mathrm{S}}\psi^{\mathrm{O_1}}\psi^{\mathrm{O_2}}\) is transformed to:  

\[\psi^{\prime} = \sum_{\mathbf{i}}(\phi_{\mathbf{i}}\psi^{\mathrm{S}})\phi_{\mathbf{i}}\psi_{\mathbf{i}[1,\dots ,a_{\mathbf{i}}]}^{\mathrm{O_{1}}}\psi_{\mathbf{i}[2,\dots ,a_{\mathbf{i}}]}^{\mathrm{O_{2}}}. \quad (3.5)\]  

Next let \(O_2\) determine \(\beta\) for the system, where \(\{\eta_j\}\) are the eigenfunctions of \(\beta\) . Then by application of Rule 2 the result is

---

\[\psi^{\prime \prime} = \sum_{\mathbf{i},\mathbf{j}}(\phi_{\mathbf{i}},\psi^{\mathbf{S}})(\eta_{\mathbf{j}},\phi_{\mathbf{i}})(\eta_{\mathbf{j}}\psi_{\mathbf{i}\dots ,\alpha_{\mathbf{i}}}^{0}\psi_{\mathbf{j}\dots ,\beta_{\mathbf{j}}}^{0}) \quad (3.6)\]  

\(O_{2}\) is now perfectly correlated with the system, since a redetermination by him will lead to agreeing results. This is no longer the case for \(O_{1}\) , however, since a redetermination of \(A\) by him will result in (by Rule 2)  

\[\psi^{\prime \prime} = \sum_{\mathbf{i},\mathbf{j},\mathbf{k}}(\phi_{\mathbf{i}},\psi^{\mathbf{S}})(\eta_{\mathbf{j}},\phi_{i})(\phi_{\mathbf{k}},\eta_{\mathbf{j}})\phi_{\mathbf{k}}^{\mathbf{S}}\psi_{\mathbf{j}\dots ,\beta_{\mathbf{j}}}^{0}\psi_{\mathbf{i}\mathbf{k}\dots ,\alpha_{\mathbf{i}},\alpha_{\mathbf{k}}}^{0}. \quad (3.7)\]  

Hence the second measurement of \(O_{1}\) does not in all cases agree with the first, and has been upset by the intervention of \(O_{2}\) .  

We can deduce the statistical relation between \(O_{1}\) 's first and second results \((\alpha_{\mathbf{i}}\) and \(\alpha_{\mathbf{k}}\) ) by our previous method of assigning a measure to the elements of the superposition (3.7). The measure assigned to the \((\mathbf{i},\mathbf{j},\mathbf{k})^{\mathrm{th}}\) element is then:  

\[\mathrm{M}_{\mathrm{i j k}} = |(\phi_{\mathrm{i}},\psi^{\mathrm{S}})(\eta_{\mathrm{j}},\phi_{\mathrm{i}})(\phi_{\mathrm{k}},\eta_{\mathrm{j}})|^{2}. \quad (3.8)\]  

This measure is equivalent, in this case, to the probabilities assigned by the orthodox theory (Process 1), where \(O_{2}\) 's observation is regarded as having converted each state \(\phi_{\mathbf{i}}\) into a non- interfering mixture of states \(\eta_{\mathbf{j}}\) , weighted with probabilities \(|(\eta_{\mathbf{j}},\phi_{\mathbf{i}})|^{2}\) , upon which \(O_{1}\) makes his second observation.  

Note, however, that this equivalence with the statistical results obtained by considering that \(O_{2}\) 's observation changed the system state into a mixture, holds true only so long as \(O_{1}\) 's second observation is restricted to the system. If he were to attempt to simultaneously determine a property of the system as well as of \(O_{2}\) , interference effects might become important. The description of the states relative to \(O_{1}\) , after \(O_{2}\) 's observation, as non- interfering mixtures is therefore incomplete.

---

Case 3: We suppose that two systems \(S_{1}\) and \(S_{2}\) are correlated but no longer interacting, and that \(O_{1}\) measures property \(A\) in \(S_{1}\) , and \(O_{2}\) property \(\beta\) in \(S_{2}\) .  

We wish to see whether \(O_{2}\) 's intervention with \(S_{2}\) can in any way affect \(O_{1}\) 's results in \(S_{1}\) , so that perhaps signals might be sent by these means. We shall assume that the initial state for the system pair is  

\[\psi_{1}^{S_{1} + S_{2}} = \sum_{i} a_{i} \phi_{i}^{S_{1}} \phi_{i}^{S_{2}}. \quad (3.9)\]  

We now allow \(O_{1}\) to observe \(A\) in \(S_{1}\) , so that after this observation the total state becomes:  

\[\psi_{1}^{S_{1} + S_{2} + O_{1} + O_{2}} = \sum_{i} a_{i} \phi_{i}^{S_1} \phi_{i}^{S_2} \psi_{i}[1, \dots , a_{i}] \psi_{[2, \dots ]}^{O_2}. \quad (3.10)\]  

\(O_{1}\) can of course continue to repeat the determination, obtaining the same result each time.  

We now suppose that \(O_{2}\) determines \(\beta\) in \(S_{2}\) , which results in  

\[\psi^{\prime \prime} = \sum_{i,j} a_{i} \{\eta_{j}^{2}, \phi_{i}^{2}\} \phi_{i}^{1} \eta_{j}^{2} \psi_{i}[1, \dots , a_{i}] \psi_{j}[2, \dots , \beta_{j}]. \quad (3.11)\]  

However, in this case, as distinct from Case 2, we see that the intervention of \(O_{2}\) in no way affects \(O_{1}\) 's determinations, since \(O_{1}\) is still perfectly correlated to the states \(\phi_{i}^{S_{1}}\) of \(S_{1}\) , and any further observations by \(O_{1}\) will lead to the same results as the earlier observations. Thus each memory sequence for \(O_{1}\) continues without change due to \(O_{2}\) 's observation, and such a scheme could not be used to send any signals.  

Furthermore, we see that the result (3.11) is arrived at even in the case that \(O_{2}\) should make his determination before that of \(O_{1}\) . Therefore any expectations for the outcome of \(O_{1}\) 's first observation are in no way affected by whether or not \(O_{2}\) performs his observation before that

---

of \(\mathbf{O}_{1}\) . This is true because the expectation of the outcome for \(\mathbf{O}_{1}\) can be computed from (4.10), which is the same whether or not \(\mathbf{O}_{2}\) performs his measurement before or after \(\mathbf{O}_{1}\) .  

It is therefore seen that one observer's observation upon one system of a correlated, but non- interacting pair of systems, has no effect on the remote system, in the sense that the outcome or expected outcome of any experiments by another observer on the remote system are not affected. Paradoxes like that of Einstein- Rosen- Podolsky \(^{5}\) which are concerned with such correlated, non- interacting, systems are thus easily understood in the present scheme.  

Many further combinations of several observers and systems can be easily studied in the present framework, and all questions answered by first writing down the final state for the situation with the aid of the Rules 1 and 2, and then noticing the relations between the elements of the memory sequences.

---

\[ \text{1} \]

---

## V. SUPPLEMENTARY TOPICS  

We have now completed the abstract treatment of measurement and observation, with the deduction that the statistical predictions of the usual form of quantum theory (Process 1) will appear to be valid to all observers. We have therefore succeeded in placing our theory in correspondence with experience, at least insofar as the ordinary theory correctly represents experience.  

We should like to emphasize that this deduction was carried out by using only the principle of superposition, and the postulate that an observation has the property that if the observed variable has a definite value in the object- system then it will remain definite and the observer will perceive this value. This treatment is therefore valid for any possible quantum interpretation of observation processes, i.e., any way in which one can interpret wave functions as describing observers, as well as for any form of quantum mechanics for which the superposition principle for states is maintained. Our abstract discussion of observation is therefore logically complete, in the sense that our results for the subjective experience of observers are correct, if there are any observers at all describable by wave mechanics.<sup>1</sup>  

In this chapter we shall consider a number of diverse topics from the point of view of our pure wave mechanics, in order to supplement the abstract discussion and give a feeling for the new viewpoint. Since we are now mainly interested in elucidating the reasonableness of the theory, we shall often restrict ourselves to plausibility arguments, rather than detailed proofs.

---

## \(\S 1\) . Macroscopic objects and classical mechanics  

In the light of our knowledge about the atomic constitution of matter, any "object" of macroscopic size is composed of an enormous number of constituent particles. The wave function for such an object is then in a space of fantastically high dimension (3N, if N is the number of particles). Our present problem is to understand the existence of macroscopic objects, and to relate their ordinary (classical) behavior in the three dimensional world to the underlying wave mechanics in the higher dimensional space.  

Let us begin by considering a relatively simple case. Suppose that we place in a box an electron and a proton, each in a definite momentum state, so that the position amplitude density of each is uniform over the whole box. After a time we would expect a hydrogen atom in the ground state to form, with ensuing radiation. We notice, however, that the position amplitude density of each particle is still uniform over the whole box. Nevertheless the amplitude distributions are now no longer independent, but correlated. In particular, the conditional amplitude density for the electron, conditioned by any definite proton (or centroid) position, is not uniform, but is given by the familiar ground state wave function for the hydrogen atom. What we mean by the statement, "a hydrogen atom has formed in the box," is just that this correlation has taken place - a correlation which insures that the relative configuration for the electron, for a definite proton position, conforms to the customary ground state configuration.  

The wave function for the hydrogen atom can be represented as a product of a centroid wave function and a wave function over relative coordinates, where the centroid wave function obeys the wave equation for a particle with mass equal to the total mass of the proton- electron system. Therefore, if we now open our box, the centroid wave function will spread with time in the usual manner of wave packets, to eventually occupy a vast region of space. The relative configuration (described by the relative coordinate state function) has, however, a permanent nature, since

---

it represents a bound state, and it is this relative configuration which we usually think of as the object called the hydrogen atom. Therefore, no matter how indefinite the positions of the individual particles become in the total state function (due to the spreading of the centroid), this state can be regarded as giving (through the centroid wave function) an amplitude distribution over a comparatively definite object, the tightly bound electron- proton system. The general state, then, does not describe any single such definite object, but a superposition of such cases with the object located at different positions.  

In a similar fashion larger and more complex objects can be built up through strong correlations which bind together the constituent particles. It is still true that the general state function for such a system may lead to marginal position densities for any single particle (or centroid) which extend over large regions of space. Nevertheless we can speak of the existence of a relatively definite object, since the specification of a single position for a particle, or the centroid, leads to the case where the relative position densities of the remaining particles are distributed closely about the specified one, in a manner forming the comparatively definite object spoken of.  

Suppose, for example, we begin with a cannonball located at the origin, described by a state function:  

\[\psi_{[c_{j}(0,0,0)]},\]  

where the subscript indicates that the total state function \(\psi\) describes a system of particles bound together so as to form an object of the size and shape of a cannonball, whose centroid is located (approximately) at the origin, say in the form of a real gaussian wave packet of small dimensions, with variance \(\sigma_{0}^{2}\) for each dimension.  

If we now allow a long lapse of time, the centroid of the system will spread in the usual manner to occupy a large region of space. (The spread in each dimension after time \(t\) will be given by \(\sigma_{t}^{2} = \sigma_{0}^{2} + (\hbar^{2}t^{2} / 4\sigma_{0}^{2}m^{2})\) ,

---

where m is the mass.) Nevertheless, for any specified centroid position, the particles, since they remain in bound states, have distributions which again correspond to the fairly well defined size and shape of the cannonball. Thus the total state can be regarded as a (continuous) superposition of states  

\[\psi = \int \mathbf{a}_{\mathbf{x}\mathbf{y}\mathbf{z}}\psi [\mathbf{c}_{\mathbf{j}}(\mathbf{x},\mathbf{y},\mathbf{z})]\mathrm{d}\mathbf{x}\mathrm{d}\mathbf{y}\mathrm{d}\mathbf{z},\]  

each of which \((\psi_{[\mathbf{c}_{\mathbf{j}}(\mathbf{x},\mathbf{y},\mathbf{z})]})\) describes a cannonball at the position \((\mathbf{x},\mathbf{y},\mathbf{z})\) . The coefficients \(\mathbf{a}_{\mathbf{x}\mathbf{y}\mathbf{z}}\) of the superposition then correspond to the centroid distribution.  

It is not true that each individual particle spreads independently of the rest, in which case we would have a final state which is a grand superposition of states in which the particles are located independently everywhere. The fact that they are in bound states restricts our final state to a superposition of "cannonball" states. The wave function for the centroid can therefore be taken as a representative wave function for the whole object.  

It is thus in this sense of correlations between constituent particles that definite macroscopic objects can exist within the framework of pure wave mechanics. The building up of correlations in a complex system supplies us with a mechanism which also allows us to understand how condensation phenomena (the formation of spatial boundaries which separate phases of different physical or chemical properties) can be controlled by the wave equation, answering a point raised by Schrödinger  

Classical mechanics, also, enters our scheme in the form of correlation laws. Let us consider a system of objects (in the previous sense), such that the centroid of each object has initially a fairly well defined position and momentum (e.g., let the wave function for the centroids consist of a product of gaussian wave packets). As time progresses, the

---

centers of the square amplitude distributions for the objects will move in a manner approximately obeying the laws of motion of classical mechanics, with the degree of approximation depending upon the masses and the length of time considered, as is well known. (Note that we do not mean to imply that the wave packets of the individual objects remain independent if they are interacting. They do not. The motion that we refer to is that of the centers of the marginal distributions for the centroids of the bodies.)  

The general state of a system of macroscopic objects does not, however, ascribe any nearly definite positions and momenta to the individual bodies. Nevertheless, any general state can at any instant be analyzed into a superposition of states each of which does represent the bodies with fairly well defined positions and momenta. Each of these states then propagates approximately according to classical laws, so that the general state can be viewed as a superposition of quasi- classical states propagating according to nearly classical trajectories. In other words, if the masses are large or the time short, there will be strong correlations between the initial (approximate) positions and momenta and those at a later time, with the dependence being given approximately by classical mechanics.  

Since large scale objects obeying classical laws have a place in our theory of pure wave mechanics, we have justified the introduction of

---

models for observers consisting of classically describable, automatically functioning machinery, and the treatment of observation of Chapter IV is non- vacuous.  

Let us now consider the result of an observation (considered along the lines of Chapter IV) performed upon a system of macroscopic bodies in a general state. The observer will not become aware of the fact that the state does not correspond to definite positions and momenta (i.e., he will not see the objects as "smeared out" over large regions of space) but will himself simply become correlated with the system - after the observation the composite system of objects + observer will be in a superposition of states, each element of which describes an observer who has perceived that the objects have nearly definite positions and momenta, and for whom the relative system state is a quasi- classical state in the previous sense, and furthermore to whom the system will appear to behave according to classical mechanics if his observation is continued. We see, therefore, how the classical appearance of the macroscopic world to us can be explained in the wave theory.  

## \(\S 2\) . Amplification processes  

In Chapter III and IV we discussed abstract measuring processes, which were considered to be simply a direct coupling between two systems, the object- system and the apparatus (or observer). There is, however, in actuality a whole chain of intervening systems linking a microscopic system to a macroscopic observer. Each link in the chain of intervening systems becomes correlated to its predecessor, so that the result is an amplification of effects from the microscopic object- system to a macroscopic apparatus, and then to the observer.  

The amplification process depends upon the ability of the state of one micro- system (particle, for example) to become correlated with the states of an enormous number of other microscopic systems, the totality of which we shall call a detection system. For example, the totality of gas atoms in a Geiger counter, or the water molecules in a cloud chamber, constitute such a detection system.

---

The amplification is accomplished by arranging the condition of the detection system so that the states of the individual micro- systems of the detector are metastable, in a way that if one micro- system should fall from its metastable state it would influence the reduction of others. This type of arrangement leaves the entire detection system metastable against chain reactions which involve a large number of its constituent systems. In a Geiger counter, for example, the presence of a strong electric field leaves the gas atoms metastable against ionization. Furthermore, the products of the ionization of one gas atom in a Geiger counter can cause further ionizations, in a cascading process. The operation of cloud chambers and photographic films is also due to metastability against such chain reactions.  

The chain reactions cause large numbers of the micro- systems of the detector to behave as a unit, all remaining in the metastable state, or all discharging. In this manner the states of a sufficiently large number of micro- systems are correlated, so that one can speak of the whole ensemble being in a state of discharge, or not.  

For example, there are essentially only two macroscopically distinguishable states for a Geiger counter; discharged or undischarged. The correlation of large numbers of gas atoms, due to the chain reaction effect, implies that either very few, or else very many of the gas atoms are ionized at a given time. Consider the complete state function \(\psi^{\mathbf{G}}\) of a Geiger counter, which is a function of all the coordinates of all of the constituent particles. Because of the correlation of the behavior of a large number of the constituent gas atoms, the total state \(\psi^{\mathbf{G}}\) can always be written as a superposition of two states  

\[\psi^{\mathbf{G}} = \mathbf{a}_{1}\psi_{[\mathbf{U}]}^{1} + \mathbf{a}_{2}\psi_{[\mathbf{D}]}^{2}, \quad (2.1)\]  

where \(\psi_{[\mathbf{U}]}^{1}\) signifies a state where only a small number of gas atoms are ionized, and \(\psi_{[\mathbf{D}]}^{2}\) a state for which a large number are ionized.

---

To see that the decomposition (2.1) is valid, expand \(\psi^{\mathbf{G}}\) in terms of individual gas atom stationary states:  

\[\psi^{\mathbf{G}} = \sum_{\mathbf{i},\mathbf{j},\ldots ,\mathbf{k}}\mathbf{a}_{\mathbf{i}\mathbf{j}\ldots \mathbf{k}}\psi_{\mathbf{i}}^{\mathbf{S}_{1}}\psi_{\mathbf{j}}^{\mathbf{S}_{2}}\ldots \psi_{\mathbf{k}}^{\mathbf{S}_{\mathbf{n}}}, \quad (2.2)\]  

where \(\psi_{\ell}^{\mathbf{r}}\) is the \(\ell^{\mathrm{th}}\) state of atom r. Each element of the superposition (2.2)  

\[\psi_{\mathrm{i}}^{\mathrm{S}_{1}}\psi_{\mathrm{j}}^{\mathrm{S}_{2}}\ldots \psi_{\mathrm{k}}^{\mathrm{S}_{\mathrm{n}}} \quad (2.3)\]  

must contain either a very large number of atoms in ionized states, or else a very small number, because of the chain reaction effect. By choosing some medium- sized number as a dividing line, each element of (2.2) can be placed in one of the two categories, high number of low number of ionized atoms. If we then carry out the sum (2.2) over only those elements of the first category, we get a state (and coefficient)  

\[\mathbf{a}_{1}\psi_{\mathrm{[D]}}^{1} = \sum_{\mathbf{i}\mathbf{j}\ldots \mathbf{k}}\mathbf{a}_{\mathbf{i}\mathbf{j}\ldots \mathbf{k}}\psi_{\mathrm{i}}^{\mathbf{S}_{1}}\psi_{\mathrm{j}}^{\mathbf{S}_{2}}\ldots \psi_{\mathbf{k}}^{\mathbf{S}_{\mathbf{n}}} \quad (2.4)\]  

The state \(\psi_{\mathrm{[D]}}^{1}\) is then a state where a large number of particles are ionized. The subscript [D] indicates that it describes a Geiger counter which has discharged. If we carry out the sum over the remaining terms of (2.2) we get in a similar fashion:  

\[\mathbf{a}_{2}\psi_{\mathrm{[U]}}^{2} = \sum_{\mathbf{i}\mathbf{j}\ldots \mathbf{k}}\mathbf{a}_{\mathrm{i}\mathbf{j}\ldots \mathbf{k}}\psi_{\mathrm{i}}^{\mathbf{S}_{1}}{\psi_{\mathrm{j}}^{\mathbf{S}_{2}}}\ldots \psi_{\mathrm{k}}^{\mathbf{S}_{\mathbf{n}}} \quad (2.5)\]  

where [U] indicates the undischarged condition. Combining (2.4) and (2.5) we arrive at the desired relation (2.1). So far, this method of decomposition can be applied to any system, whether or not it has the chain reaction property. However, in our case, more is implied, namely that the spread of the number of ionized atoms in both \(\psi_{\mathrm{[D]}}\) and \(\psi_{\mathrm{[U]}}\) will be small compared to the separation of their averages, due to the fact that

---

the existence of the chain reactions means that either many or else few atoms will be ionized, with the middle ground virtually excluded.  

This type of decomposition is also applicable to all other detection devices which are based upon this chain reaction principle (such as cloud chambers, photo plates, etc.).  

We consider now the coupling of such a detection device to another micro- system (object- system) for the purpose of measurement. If it is true that the initial object- system state \(\phi_{1}\) will at some time \(t\) trigger the chain reaction, so that the state of the counter becomes \(\psi_{[D]}^{1}\) , while the object- system state \(\phi_{2}\) will not, then it is still true that the initial object- system state \(a_{1}\phi_{1} + a_{2}\phi_{2}\) will result in the superposition  

\[a_{1}\phi_{1}^{'} \psi_{[D]}^{1} + a_{2}\phi_{2}^{'} \psi_{[U]}^{2} \quad (2.6)\]  

at time \(t\) .  

For example, let us suppose that a particle whose state is a wave packet \(\phi\) , of linear extension greater than that of our Geiger counter, approaches the counter. Just before it reaches the counter, it can be decomposed into a superposition \(\phi = a_{1}\phi_{1} + a_{2}\phi_{2} (\phi_{1}, \phi_{2}\) orthogonal) where \(\phi_{1}\) has non- zero amplitude only in the region before the counter and \(\phi_{2}\) has non- zero amplitude elsewhere (so that \(\phi_{1}\) is a packet which will entirely pass through the counter while \(\phi_{2}\) will entirely miss the counter). The initial total state for the system particle + counter is then:  

\[\phi \psi_{[U]} = (a_{1}\phi_{1} + a_{2}\phi_{2})\psi_{[U]},\]  

where \(\psi_{[U]}\) is the initial (assumed to be undischarged) state of the counter.  

But at a slightly later time \(\phi_{1}\) is changed to \(\phi_{1}^{'}\) , after traversing the counter and causing it to go into a discharged state \(\psi_{[D]}^{1}\) , while \(\phi_{2}\) passes by into a state \(\phi_{2}^{'}\) leaving the counter in an undischarged state \(\psi_{[U]}^{2}\) . Superposing these results, the total state at the later time is

---

\[a_{1}\phi_{1}^{\prime}\psi_{[D]}^{1} + a_{2}\phi_{2}^{\prime}\psi_{[U]}^{2}\]  

in accordance with (2.6). Furthermore, the relative particle state for \(\psi_{[D]}^{1}\) , \(\phi_{1}^{\prime}\) , is a wave packet emanating from the counter, while the relative state for \(\psi_{[U]}^{2}\) is a wave with a "shadow" cast by the counter. The counter therefore serves as an apparatus which performs an approximate position measurement on the particle.  

No matter what the complexity or exact mechanism of a measuring process, the general superposition principle as stated in Chapter III, §3, remains valid, and our abstract discussion is unaffected. It is a vain hope that somewhere embedded in the intricacy of the amplification process is a mechanism which will somehow prevent the macroscopic apparatus state from reflecting the same indefiniteness as its object- system.  

## §3. Reversibility and irreversibility  

Let us return, for the moment, to the probabilistic interpretation of quantum mechanics based on Process 1 as well as Process 2. Suppose that we have a large number of identical systems (ensemble), and that the \(j^{\mathrm{th}}\) system is in the state \(\psi^{\mathrm{j}}\) . Then for purposes of calculating expectation values for operators over the ensemble, the ensemble is represented by the mixture of states \(\psi^{\mathrm{j}}\) weighted with \(1 / \mathrm{N}\) , where \(\mathrm{N}\) is the number of systems, for which the density operator \(^3\) is:  

\[\rho = \frac{1}{\mathrm{N}}\sum_{j}[\psi^{\mathrm{j}}], \quad (3.1)\]  

where \([\psi^{\mathrm{j}}]\) denotes the projection operator on \(\psi^{\mathrm{j}}\) . This density operator, in turn, is equivalent to a density operator which is a sum of projections on orthogonal states (the eigenstates of \(\rho\) ): \(^4\)

---

\[\rho = \sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}[\eta_{\mathbf{i}}],\quad (\eta_{\mathbf{i}},\eta_{\mathbf{j}}) = \delta_{\mathbf{i}\mathbf{j}},\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}} = 1, \quad (3.2)\]  

so that any ensemble is always equivalent to a mixture of orthogonal states, which representation we shall henceforth assume.  

Suppose that a quantity A, with (non- degenerate) eigenstates \(\{\phi_{j}\}\) is measured in each system of the ensemble. This measurement has the effect of transforming each state \(\eta_{i}\) into the state \(\phi_{j}\) , with probability \(|(\phi_{j}, \eta_{i})|^{2}\) ; i.e., it will transform a large ensemble of systems in the state \(\eta_{i}\) into an ensemble represented by the mixture whose density operator is \(\sum_{j} |(\phi_{j}, \eta_{i})|^{2} [\phi_{j}]\) . Extending this result to the case where the original ensemble is a mixture of the \(\eta_{i}\) weighted by \(\mathbf{P}_{\mathbf{i}}\) ((3.2)), we find that the density operator \(\rho\) is transformed by the measurement of A into the new density operator \(\rho^{\prime}\) :  

\[\rho^{\prime} = \sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}\sum_{\mathbf{j}}|(\eta_{\mathbf{i}},\phi_{\mathbf{j}})|^{2}[\phi_{\mathbf{j}}] = \sum_{\mathbf{j}}\Big(\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}(\phi_{\mathbf{j}},(\eta_{\mathbf{i}},\phi_{\mathbf{j}})\eta_{\mathbf{i}})\Big)[\phi_{\mathbf{j}}]\] \[\qquad = \sum_{\mathbf{j}}\Big(\phi_{\mathbf{j}},\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}[\eta_{\mathbf{i}}]\phi_{\mathbf{j}})\Big)[\phi_{\mathbf{j}}] = \sum_{\mathbf{j}}\big(\phi_{\mathbf{j}},\rho \phi_{\mathbf{j}}\big)[\phi_{\mathbf{j}}]~.\]  

This is the general law by which mixtures change through Process 1.  

However, even when no measurements are taking place, the states of an ensemble are changing according to Process 2, so that after a time interval t each state \(\psi\) will be transformed into a state \(\psi^{\prime} = \mathbf{U}_{\mathbf{t}}\psi\) , where \(\mathbf{U}_{\mathbf{t}}\) is a unitary operator. This natural motion has the consequence that each mixture \(\rho = \sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}[\eta_{\mathbf{i}}\) is carried into the mixture \(\rho^{\prime} = \sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}[\mathbf{U}_{\mathbf{t}}\eta_{\mathbf{i}}]\) after a time t. But for every state \(\xi\) ,  

\[\rho^{\prime}\xi = \sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}[\mathbf{U}_{\mathbf{t}}{\eta}_{\mathbf{i}}]\xi = \sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}(\mathbf{U}_{\mathbf{t}}{\eta}_{\mathbf{i}},\xi)\mathbf{U}_{\mathbf{t}}{\eta}_{\mathbf{i}}\] \[\qquad = \mathbf{U}_{\mathbf{t}}\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}({\eta}_{\mathbf{i}},\mathbf{U}_{\mathbf{t}}^{-1}\xi){\eta}_{\mathbf{i}} = \mathbf{U}_{\mathbf{t}}\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}[{\eta}_{\mathbf{i}}](\mathbf{U}_{\mathbf{t}}^{-1}\xi)\] \[\qquad = (\mathbf{U}_{\mathbf{t}}\rho \mathbf{U}_{\mathbf{t}}^{-1})\xi .\]

---

Therefore  

\[\rho^{\prime} = \mathsf{U}_{\mathsf{t}}\rho \mathsf{U}_{\mathsf{t}}^{-1}, \quad (3.5)\]  

which is the general law for the change of a mixture according to Process 2.  

We are now interested in whether or not we get from any mixture to another by means of these two processes, i.e., if for any pair \(\rho , \rho^{\prime}\) , there exist quantities A which can be measured and unitary (time dependence) operators U such that \(\rho\) can be transformed into \(\rho^{\prime}\) by suitable applications of Processes 1 and 2. We shall see that this is not always possible, and that Process 1 can cause irreversible changes in mixtures.  

For each mixture \(\rho\) we define a quantity \(\mathbf{I}_{\rho}\) :  

\[\mathbf{I}_{\rho} = \mathrm{Trace}\left(\rho \ln \rho\right). \quad (3.6)\]  

This number, \(\mathbf{I}_{\rho}\) , has the character of information. If \(\rho = \sum_{i} \mathbf{P}_{i}[\eta_{i}]\) , a mixture of orthogonal states \(\eta_{i}\) weighted with \(\mathbf{P}_{i}\) , then \(\mathbf{I}_{\rho}\) is simply the information of the distribution \(\mathbf{P}_{i}\) over the eigenstates of \(\rho\) (relative to the uniform measure). (Trace \((\rho \ln \rho)\) is a unitary invariant and is proportional to the negative of the entropy of the mixture, as discussed in Chapter III, §2.)  

Process 2 therefore has the property that it leaves \(\mathbf{I}_{\rho}\) unchanged, because  

\[\begin{array}{r l} & {\mathrm{I}_{\rho^{\prime}} = \mathrm{Trace}\left(\rho^{\prime}\ln \rho^{\prime}\right) = \mathrm{Trace}\left(\mathrm{U}_{\mathrm{t}}\rho \mathrm{U}_{\mathrm{t}}^{-1}\ln \mathrm{U}_{\mathrm{t}}\rho \mathrm{U}_{\mathrm{t}}^{-1}\right)}\\ & {\qquad = \mathrm{Trace}\left(\mathrm{U}_{\mathrm{t}}\rho \ln \rho \mathrm{U}_{\mathrm{t}}^{-1}\right) = \mathrm{Trace}\left(\rho \ln \rho\right) = \mathrm{I}_{\rho}.} \end{array} \quad (3.7)\]  

Process 1, on the other hand, can decrease \(\mathbf{I}_{\rho}\) but never increase it. According to (3.3):  

\[\rho^{\prime} = \sum_{j}\left(\phi_{j},\rho \phi_{j}\right)\left[\phi_{j}\right] = \sum_{i,j}\mathbf{P}_{i}\left|(\eta_{i},\phi_{j})\right|^{2}\left[\phi_{j}\right] = \sum_{j}\mathbf{P}_{j}^{\prime}\left[\phi_{j}\right], \quad (3.8)\]

---

where \(\rho_{j}^{\prime} \sum_{i} \mathbf{P}_{i} \mathbf{T}_{ij}\) and \(\mathbf{T}_{ij} = |(\eta_{i}, \phi_{j})|^{2}\) is a doubly- stochastic matrix.\(^{5}\) But \(\mathbf{I}_{\rho^{\prime}} = \sum_{j} \mathbf{P}_{j}^{\prime} \ln \mathbf{P}_{j}^{\prime}\) and \(\mathbf{I}_{\rho} = \sum_{i} \mathbf{P}_{i} \ln \mathbf{P}_{i}\) , with the \(\mathbf{P}_{i}, \mathbf{P}_{j}^{\prime}\) connected by \(\mathbf{T}_{ij}\) , implies, by the theorem of information decrease for stochastic processes (II- §6), that:  

\[\mathbf{I}_{\rho^{\prime}} \leq \mathbf{I}_{\rho} \quad (3.9)\]  

Moreover, it can easily be shown by a slight strengthening of the theorems of Chapter II, §6 that strict inequality must hold unless (for each i such that \(\rho_{i} > 0\) ) \(\mathbf{T}_{ij} = 1\) for one j and 0 for the rest \((\mathbf{T}_{ij} = \delta_{ijk})\) . This means that \(|(\eta_{i}, \phi_{j})|^{2} = \delta_{ijk}\) , which implies that the original mixture was already a mixture of eigenstates of the measurement.  

We have answered our question, and it is not possible to get from any mixture to another by means of Processes 1 and 2. There is an essential irreversibility to Process 1, since it corresponds to a stochastic process, which cannot be compensated by Process 2, which is reversible, like classical mechanics.\(^{6}\)  

Our theory of pure wave mechanics, to which we now return, must give equivalent results on the subjective level, since it leads to Process 1 there. Therefore, measuring processes will appear to be irreversible to any observers (even though the composite system including the observer changes its state reversibly).

---

There is another way of looking at this apparent irreversibility within our theory which recognizes only Process 2. When an observer performs an observation the result is a superposition, each element of which describes an observer who has perceived a particular value. From this time forward there is no interaction between the separate elements of the superposition (which describe the observer as having perceived different results), since each element separately continues to obey the wave equation. Each observer described by a particular element of the superposition behaves in the future completely independently of any events in the remaining elements, and he can no longer obtain any information whatsoever concerning these other elements (they are completely unobservable to him).  

The irreversibility of the measuring process is therefore, within our framework, simply a subjective manifestation reflecting the fact that in observation processes the state of the observer is transformed into a superposition of observer states, each element of which describes an observer who is irrevocably cut off from the remaining elements. While it is conceivable that some outside agency could reverse the total wave function, such a change cannot be brought about by any observer which is represented by a single element of a superposition, since he is entirely powerless to have any influence on any other elements.  

There are, therefore, fundamental restrictions to the knowledge that an observer can obtain about the state of the universe. It is impossible for any observer to discover the total state function of any physical system, since the process of observation itself leaves no independent state for the system or the observer, but only a composite system state in which the object- system states are inextricably bound up with the observer states. As soon as the observation is performed, the composite state is split into a superposition for which each element describes a different object- system state and an observer with (different) knowledge of it. Only the totality of these observer states, with their diverse knowledge, contains complete information about the original object- system state – but there is no possible communication between the observers described by these separate

---

states. Any single observer can therefore possess knowledge only of the relative state function (relative to his state) of any systems, which is in any case all that is of any importance to him.  

We conclude this section by commenting on another question which might be raised concerning irreversible processes: Is it necessary for the existence of measuring apparata, which can be correlated to other systems, to have frictional processes which involve systems of a large number of degrees of freedom? Are such thermodynamically irreversible processes possible in the framework of pure wave mechanics with a reversible wave equation, and if so, does this circumstance pose any difficulties for our treatment of measuring processes?  

In the first place, it is certainly not necessary for dissipative processes involving additional degrees of freedom to be present before an interaction which correlates an apparatus to an object- system can take place. The counter- example is supplied by the simplified measuring process of III- §3, which involves only a system of one coordinate and an apparatus of one coordinate and no further degrees of freedom.  

To the question whether such processes are possible within reversible wave mechanics, we answer yes, in the same sense that they are present in classical mechanics, where the microscopic equations of motion are also reversible. This type of irreversibility, which might be called macroscopic irreversibility, arises from a failure to separate "macroscopically indistinguishable" states into "true" microscopic states. It has a fundamentally different character from the irreversibility of Process 1, which applies to micro- states as well and is peculiar to quantum mechanics. Macroscopically irreversible phenomena are common to both classical and quantum mechanics, since they arise from our incomplete information concerning a system, not from any intrinsic behavior of the system.

---

Finally, even when such frictional processes are involved, they present no new difficulties for the treatment of measuring and observation processes given here. We imposed no restrictions on the complexity or number of degrees of freedom of measuring apparatus or observers, and if any of these processes are present (such as heat reservoirs, etc.) then these systems are to be simply included as part of the apparatus or observer.  

## §4. Approximate measurement  

A phenomenon which is difficult to understand within the framework of the probabilistic interpretation of quantum mechanics is the result of an approximate measurement. In the abstract formulation of the usual theory there are two fundamental processes; the discontinuous, probabilistic Process 1 corresponding to precise measurement, and the continuous, deterministic Process 2 corresponding to absence of any measurement. What mixture of probability and causality are we to apply to the case where only an approximate measurement is effected (i.e., where the apparatus or observer interacts only weakly and for a finite time with the object- system)?  

In the case of approximate measurement, we need to be supplied with rules which will tell us, for any initial object- system state, first, with what probability can we expect the various possible apparatus readings, and second, what new state to ascribe to the system after the value has been observed. We shall see that it is generally impossible to give these rules within a framework which considers the apparatus or observer as performing an (abstract) observation subject to Process 1, and that it is necessary, in order to give a full account of approximate measurements, to treat the entire system, including apparatus or observer, wave mechanically.  

The position that an approximate measurement results in the situation that the object- system state is changed into an eigenstate of the exact measurement, but for which particular one the observer has only imprecise

---

information, is manifestly false. It is a fact that we can make successive approximate position measurements of particles (in cloud chambers, for example) and use the results for somewhat reliable predictions of future positions. However, if either of these measurements left the particle in an "eigenstate" of position ( \(\delta\) function), even though the particular one remained unknown, the momentum would have such a variance that no such prediction would be possible. (The possibility of such predictions lies in the correlations between position and momentum at one time with position and momentum at a later time for wave packets \(^{9}\) – correlations which are totally destroyed by precise measurements of either quantity.)  

Instead of continuing the discussion of the inadequacy of the probabilistic formulation, let us first investigate what actually happens in approximate measurements, from the viewpoint of pure wave mechanics. An approximate measurement consists of an interaction, for a finite time, which only imperfectly correlates the apparatus (or observer) with the object- system. We can deduce the desired rules in any particular case by the following method: For fixed interaction and initial apparatus state and for any initial object- system state we solve the wave equation for the time of interaction in question. The result will be a superposition of apparatus (observer) states and relative object- system states. Then (according to the method of Chapter IV for assigning a measure to a superposition) we assign a probability to each observed result equal to the square- amplitude of the coefficient of the element which contains the apparatus (observer) state representing the registering of that result. Finally, the object- system is assigned the new state which is its relative state in that element.  

For example, let us consider the measuring process described in Chapter III- §3, which is an excellent model for an approximate measurement. After the interaction, the total state was found to be (III- (3.12)):

---

\[\psi_{\mathrm{t}}^{\mathrm{S} + \mathrm{A}} = \int \frac{1}{N_{\mathrm{r}}^{\prime}}\xi^{\mathrm{r}^{\prime}}(\mathbf{q})\delta (\mathbf{r} - \mathbf{r}^{\prime})\mathrm{d}\mathbf{r}^{\prime}. \quad (4.1)\]  

Then, according to our prescription, we assign the probability density \(\mathbf{P}(\mathbf{r}^{\prime})\) to the observation of the apparatus coordinate \(\mathbf{r}^{\prime}\)  

\[\mathbf{P}(\mathbf{r}^{\prime}) = \left|\frac{1}{N_{\mathbf{r}}^{\prime}}\right|^{2} = \int \phi^{*}\phi (\mathbf{q})\eta^{*}\eta (\mathbf{r}^{\prime} - \mathbf{q}\mathbf{t})\mathrm{d}\mathbf{q}, \quad (4.2)\]  

which is the square amplitude of the coefficient \(\left(\frac{1}{N_{\mathrm{r}}^{\prime}}\right)\) of the element \(\xi^{\mathrm{r}^{\prime}}(\mathbf{q})\delta (\mathbf{r} - \mathbf{r^{\prime}})\) of the superposition (4.1) in which the apparatus coordinate has the value \(\mathbf{r} = \mathbf{r}^{\prime}\) . Then, depending upon the observed apparatus coordinate \(\mathbf{r}^{\prime}\) , we assign the object- system the new state  

\[\xi^{\mathrm{r}^{\prime}}(\mathbf{q}) = N_{\mathbf{r}^{\prime}}\phi (\mathbf{q})\eta (\mathbf{r}^{\prime} - \mathbf{q}\mathbf{t}) \quad (4.3)\]  

(where \(\phi (\mathbf{q})\) is the old state, and \(\eta (\mathbf{r})\) is the initial apparatus state) which is the relative object- system state in (4.1) for apparatus coordinate \(\mathbf{r}^{\prime}\) .  

This example supplies the counter- example to another conceivable method of dealing with approximate measurement within the framework of Process 1. This is the position that when an approximate measurement of a quantity \(\mathbf{Q}\) is performed, in actuality another quantity \(\mathbf{Q}^{\prime}\) is precisely measured, where the eigenstates of \(\mathbf{Q}^{\prime}\) correspond to fairly well- defined (i.e., sharply peaked distributions for) \(\mathbf{Q}\) values. \(^{10}\) However, any such scheme based on Process 1 always has the prescription that after the measurement, the (unnormalized) new state function results from the old by a projection (on an eigenstate or eigenspace), which depends upon the observed value. If this is true, then in the above example the new state \(\xi^{\mathrm{r}^{\prime}}(\mathbf{q})\) must result from the old, \(\phi (\mathbf{q})\) , by a projection \(\mathbf{E}\) :  

\[\xi^{\mathrm{r}^{\prime}}(\mathbf{q}) = \mathbf{N}\mathbf{E}\phi (\mathbf{q}) = N_{\mathbf{r}^{\prime}}\phi (\mathbf{q})\eta (\mathbf{\Delta}\mathbf{r}^{\prime} - \mathbf{q}\mathbf{t}) \quad (4.4)\]

---

where \(\mathbf{N}, \mathbf{N}_{\mathbf{r}^{\prime}}\) are normalization constants). But \(\mathbf{E}\) is only a projection if \(\mathbf{E}^{2} = \mathbf{E}\) . Applying the operation (4.4) twice, we get:  

\[\begin{array}{r l} & {\mathrm{E}(\mathrm{N}\mathrm{E}\phi (\mathrm{q})) = \mathrm{N}\mathrm{E}^{2}\phi (\mathrm{q}) = \mathrm{N}^{\prime}\phi (\mathrm{q})\eta^{2}(\mathrm{r}^{\prime} - \mathrm{qt})\Rightarrow \mathrm{E}^{2}\phi (\mathrm{q})}\\ & {\qquad = \frac{\mathrm{N}^{\prime}}{\mathrm{N}}\phi (\mathrm{q})\eta^{2}(\mathrm{r}^{\prime} - \mathrm{qt}),} \end{array} \quad (4.5)\]  

and we see that \(\mathbf{E}\) cannot be a projection unless \(\eta (\mathbf{q}) = \eta^{2}(\mathbf{q})\) for all \(\mathbf{q}\) (i.e., \(\eta (\mathbf{q}) = 0\) or 1 for all \(\mathbf{q}\) ) and we have arrived at a contradiction to the assumption that in all cases the changes of states for approximate measurements are governed by projections. (In certain special cases, such as approximate position measurements with slits or Geiger counters, \(^{11}\) the new functions arise from the old by multiplication by sharp cutoff functions which are 1 over the slit or counter and 0 elsewhere, so that these measurements can be handled by projections.)  

One cannot, therefore, account for approximate measurements by any scheme based on Process 1, and it is necessary to investigate these processes entirely wave- mechanically. Our viewpoint constitutes a framework in which it is possible to make precise deductions about such measurements and observations, since we can follow in detail the interaction of an observer or apparatus with an object- system.  

## \(\S 5\) . Discussion of a spin measurement example  

We shall conclude this chapter with a discussion of an instructive example of Bohm. \(^{12}\) Bohm considers the measurement of the z component of the angular momentum of an atom, whose total angular momentum is \(\frac{\hbar}{2}\) , which is brought about by a Stern- Gerlach experiment. The measurement

---

is accomplished by passing an atomic beam through an inhomogeneous magnetic field, which has the effect of giving the particle a momentum which is directed up or down depending upon whether the spin was up or down.  

The measurement is treated as impulsive, so that during the time that the atom passes through the field the Hamiltonian is taken to be simply the interaction:  

\[\mathrm{H}_{\mathrm{I}} = \mu \left(\vec{\delta}\cdot \vec{\mathcal{H}}\right),\quad \mu = -\frac{e\hbar}{2mc} \quad (5.1)\]  

where \(\mathcal{H}\) is the magnetic field and \(\vec{\delta}\) the spin operator for the atom. The particle is presumed to pass through a region of the field where the field is in the \(\mathbf{z}\) direction, so that during the time of transit the field is approximately \(\mathcal{H}_{\mathrm{z}}\cong \mathcal{H}_{0} + \mathrm{z}\mathcal{H}_{0}^{\prime}\left(\mathcal{H}_{0} = \left(\mathcal{H}_{\mathrm{z}}\right)_{\mathrm{z} = 0}\right.\) and \(\mathcal{H}_{0}^{\prime} = \left(\frac{\partial\mathcal{H}_{\mathrm{z}}}{\partial\mathbf{z}}\right)_{\mathbf{z} = 0})\) , and hence the interaction is approximately:  

\[\mathrm{H}_{\mathrm{I}}\cong \mu \left(\mathcal{H}_{0} + \mathrm{z}\mathcal{H}_{0}^{\prime}\right)\mathrm{S}_{\mathrm{z}}, \quad (5.2)\]  

where \(\mathbf{S}_{\mathbf{z}}\) denotes the operator for the \(\mathbf{z}\) component of the spin.  

It is assumed that the state of the atom, just prior to entry into the field, is a wave packet of the form:  

\[\psi_{0} = \mathrm{f}_{0}(\mathrm{z})(\mathrm{c}_{+}\mathrm{v}_{+} + \mathrm{c}_{-}\mathrm{v}_{-}) \quad (5.3)\]  

where \(\mathbf{v}_{+}\) and \(\mathbf{v}_{- }\) are the spin functions for \(\mathbf{S}_{\mathbf{z}} = 1\) and \(- 1\) respectively. Solving the Schrödinger equation for the Hamiltonian (5.2) and initial condition (5.3) yields the state for a later time \(t\) :  

\[\psi = \mathrm{f}_{0}(\mathrm{z})\left(\mathrm{c}_{+}\mathrm{e}^{-\mathrm{i}\mu (\mathcal{H}_{0} + \mathrm{z}\mathcal{H}_{0}^{\prime})\mathrm{t} / \hbar}\mathrm{v}_{+} + \mathrm{c}_{-}\mathrm{e}^{+\mathrm{i}\mu (\mathcal{H}_{0} + \mathrm{z}\mathcal{H}_{0}^{'})\mathrm{t} / \hbar}\mathrm{v}_{-}\right). \quad (5.4)\]  

Therefore, if \(\Delta t\) is the time that it takes the atom to traverse the field,13 each component of the wave packet has been multiplied by a phase factor

---

\(\pm \mathrm{i}\mu (\mathrm{H}_{0} + \mathrm{z}\mathrm{H}_{0}^{\prime})\Delta \mathrm{t} / \hbar\) , i.e., has had its mean momentum in the z direction changed by an amount \(\pm \mathrm{H}_{0}^{\prime}\mu \Delta \mathrm{t}\) , depending upon the spin direction. Thus the initial wave packet (with mean momentum zero) is split into a superposition of two packets, one with mean z- momentum \(+\mathrm{H}_{0}^{\prime}\mu \Delta \mathrm{t}\) and spin up, and the other with spin down and mean z- momentum \(-\mathrm{H}_{0}^{\prime}\mu \Delta \mathrm{t}\) .  

The interaction (5.2) has therefore served to correlate the spin with the momentum in the z- direction. These two packets of the resulting superposition now move in opposite z- directions, so that after a short time they become widely separated (provided that the momentum changes \(\pm \mathrm{H}_{0}^{\prime}\mu \Delta \mathrm{t}\) are large compared to the momentum spread of the original packet), and the z- coordinate is itself then correlated with the spin - representing the "apparatus" coordinate in this case. The Stern- Gerlach apparatus therefore splits an incoming wave packet into a superposition of two diverging packets, corresponding to the two spin values.  

We take this opportunity to caution against a certain viewpoint which can lead to difficulties. This is the idea that, after an apparatus has interacted with a system, in "actuality" one or another of the elements of the resultant superposition described by the composite state- function has been realized to the exclusion of the rest, the existing one simply being unknown to an external observer (i.e., that instead of the superposition there is a genuine mixture). This position must be erroneous since there is always the possibility for the external observer to make use of interference properties between the elements of the superposition.  

In the present example, for instance, it is in principle possible to deflect the two beams back toward one another with magnetic fields and recombine them in another inhomogeneous field, which duplicates the first, in such a manner that the original spin state (before entering the apparatus) is restored. \(^{14}\) This would not be possible if the original Stern- Gerlach apparatus performed the function of converting the original wave

---

packet into a non- interfering mixture of packets for the two spin cases. Therefore the position that after the atom has passed through the inhomogeneous field it is "really" in one or the other beam with the corresponding spin, although we are ignorant of which one, is incorrect.  

After two systems have interacted and become correlated it is true that marginal expectations for subsystem operators can be calculated correctly when the composite system is represented by a certain noninterfering mixture of states. Thus if the composite system state is \(\psi_{S_1 + S_2} = \sum_{i} \mathbf{a}_i^{\dagger} \phi_i^{S_1} \eta_i^{S_2}\) , where the \(\{\eta_i\}\) are orthogonal, then for purposes of calculating the expectations of operators on \(S_1\) the state \(\psi_{S_1 + S_2}\) is equivalent to the non- interfering mixture of states \(\phi_i^{S_1} \eta_i^{S_2}\) weighted by \(\mathbf{P}_i = \mathbf{a}_i^{\dagger} \mathbf{a}_i\) , and one can take the picture that one or another of the cases \(\phi_i^{S_1} \eta_i^{S_2}\) has been realized to the exclusion of the rest, with probabilities \(\mathbf{P}_i^{15}\) .  

However, this representation by a mixture must be regarded as only a mathematical artifice which, although useful in many cases, is an incomplete description because it ignores phase relations between the separate elements which actually exist, and which become important in any interactions which involve more than just a subsystem.  

In the present example, the "composite system" is made of the "subsystems" spin value (object- system) and z- coordinate (apparatus), and the superposition of the two diverging wave packets is the state after interaction. It is only correct to regard this state as a mixture so long as any contemplated future interactions or measurements will involve only the spin value or only the z- coordinate, but not both simultaneously. As we saw, phase relations between the two packets are present and become important when they are deflected back and recombined in another inhomogeneous field - a process involving the spin values and z- coordinate simultaneously.

---

It is therefore improper to attribute any less validity or "reality" to any element of a superposition than any other element, due to this ever present possibility of obtaining interference effects between the elements. All elements of a superposition must be regarded as simultaneously existing.  

At this time we should like to add a few remarks concerning the notion of transition probabilities in quantum mechanics. Often one considers a system, with Hamiltonian H and stationary states \(\{\phi_{i}\}\) , to be perturbed for a time by a time- dependent addition to the Hamiltonian, \(\mathbf{H}_{\mathrm{I}}(\mathbf{t})\) . Then under the action of the perturbed Hamiltonian \(\mathbf{H}^{\prime} = \mathbf{H} + \mathbf{H}_{\mathrm{I}}(\mathbf{t})\) the states \(\{\phi_{i}\}\) are generally no longer stationary but change after time \(\mathbf{t}\) into new states \(\{\psi_{i}(\mathbf{t})\}\) :  

\[\phi_{i} \to \psi_{i}(\mathbf{t}) = \sum_{j} (\phi_{j}, \psi_{i}(\mathbf{t})) \phi_{j} = \sum_{j} a_{ij}(\mathbf{t}) \phi_{j}, \quad (5.5)\]  

which can be represented as a superposition of the old stationary states with time- dependent coefficients \(a_{ij}(\mathbf{t})\) .  

If at time \(r\) a measurement with eigenstates \(\phi_{j}\) is performed, such as an energy measurement (whose operator is the original \(\mathbf{H}\) ), then according to the probabilistic interpretation the probability for finding the state \(\phi_{j}\) , given that the state was originally \(\phi_{i}\) , is \(\mathbf{P}_{ij}(r) = |a_{ij}(r)|^{2}\) . The quantities \(|a_{ij}(r)|^{2}\) are often referred to as transition probabilities. In this case, however, the name is a misnomer, since it carries the connotation that the original state \(\phi_{i}\) is transformed into a mixture (of the \(\phi_{j}\) weighted by \(\mathbf{P}_{ij}(r)\) ), and gives the erroneous impression that the quantum formalism itself implies the existence of quantum- jumps (stochastic processes) independent of acts of observation. This is incorrect since there is still a pure state \(\sum_{j} a_{ij}(r) \phi_{j}\) with phase relations between the \(\phi_{j}\) , and expectations of operators other than the energy must be calculated from the superposition and not the mixture.  

There is another case, however, the one usually encountered in fact, where the transition probability concept is somewhat more justified. This

---

is the case in which the perturbation is due to interaction of the system \(\mathbf{s}_{1}\) with another system \(\mathbf{s}_{2}\) , and not simply a time dependence of \(\mathbf{s}_{1}\) 's Hamiltonian as in the case just considered. In this situation the interaction produces a composite system state, for which there are in general no independent subsystem states. However, as we have seen, for purposes of calculating expectations of operators on \(\mathbf{s}_{1}\) alone, we can regard \(\mathbf{s}_{1}\) as being represented by a certain mixture. According to this picture the states of subsystem \(\mathbf{s}_{1}\) are gradually converted into mixtures by the interaction with \(\mathbf{s}_{2}\) and the concept of transition probability makes some sense. Of course, it must be remembered that this picture is only justified so long as further measurements on \(\mathbf{s}_{1}\) alone are contemplated, and any attempt to make a simultaneous determination in \(\mathbf{s}_{1}\) and \(\mathbf{s}_{2}\) involves the composite state where interference properties may be important.  

An example is a hydrogen atom interacting with the electromagnetic field. After a time of interaction we can picture the atom as being in a mixture of its states, so long as we consider future measurements on the atom only. But in actuality the state of the atom is dependent upon (correlated with) the state of the field, and some process involving both atom and field could conceivably depend on interference effects between the states of the alleged mixture. With these restrictions, however, the concept of transition probability is quite useful and justified.

---

## VI. DISCUSSION  

We have shown that our theory based on pure wave mechanics, which takes as the basic description of physical systems the state function - supposed to be an objective description (i.e., in one- one, rather than statistical, correspondence to the behavior of the system) - can be put in satisfactory correspondence with experience. We saw that the probabilistic assertions of the usual interpretation of quantum mechanics can be deduced from this theory, in a manner analogous to the methods of classical statistical mechanics, as subjective appearances to observers - observers which were regarded simply as physical systems subject to the same type of description and laws as any other systems, and having no preferred position. The theory is therefore capable of supplying us with a complete conceptual model of the universe, consistent with the assumption that it contains more than one observer.  

Because the theory gives us an objective description, it constitutes a framework in which a number of puzzling subjects (such as classical level phenomena, the measuring process itself, the inter- relationship of several observers, questions of reversibility and irreversibility, etc.) can be investigated in detail in a logically consistent manner. It supplies a new way of viewing processes, which clarifies many apparent paradoxes of the usual interpretation<sup>1</sup> - indeed, it constitutes an objective framework in which it is possible to understand the general consistency of the ordinary view.

---

We shall now resume our discussion of alternative interpretations. There has been expressed lately a great deal of dissatisfaction with the present form of quantum theory by a number of authors, and a wide variety of new interpretations have sprung into existence. We shall now attempt to classify briefly a number of these interpretations, and comment upon them.  

a. The "popular" interpretation. This is the scheme alluded to in the introduction, where \(\psi\) is regarded as objectively characterizing the single system, obeying a deterministic wave equation when the system is isolated but changing probabilistically and discontinuously under observation.  

In its unrestricted form this view can lead to paradoxes like that mentioned in the introduction, and is therefore untenable. However, this view is consistent so long as it is assumed that there is only one observer in the universe (the solipsist position - Alternative 1 of the Introduction). This consistency is most easily understood from the viewpoint of our own theory, where we were able to show that all phenomena will seem to follow the predictions of this scheme to any observer. Our theory therefore justifies the personal adoption of this probabilistic interpretation, for purposes of making practical predictions, from a more satisfactory framework.  

b. The Copenhagen interpretation. This is the interpretation developed by Bohr. The \(\psi\) function is not regarded as an objective description of a physical system (i.e., it is in no sense a conceptual model), but is regarded as merely a mathematical artifice which enables one to make statistical predictions, albeit the best predictions which it is possible to make. This interpretation in fact denies the very possibility of a single conceptual model applicable to the quantum realm, and asserts that the totality of phenomena can only be understood by the use of different, mutually exclusive (i.e., "complementary") models in different situations. All state

---

ments about microscopic phenomena are regarded as meaningless unless accompanied by a complete description (classical) of an experimental arrangement.  

While undoubtedly safe from contradiction, due to its extreme conservatism, it is perhaps overcautious. We do not believe that the primary purpose of theoretical physics is to construct "safe" theories at severe cost in the applicability of their concepts, which is a sterile occupation, but to make useful models which serve for a time and are replaced as they are outworn.²  

Another objectionable feature of this position is its strong reliance upon the classical level from the outset, which precludes any possibility of explaining this level on the basis of an underlying quantum theory. (The deduction of classical phenomena from quantum theory is impossible simply because no meaningful statements can be made without pre- existing classical apparatus to serve as a reference frame.) This interpretation suffers from the dualism of adhering to a "reality" concept (i.e., the possibility of objective description) on the classical level but renouncing the same in the quantum domain.  

c. The "hidden variables" interpretation. This is the position (Alternative 4 of the Introduction) that \(\psi\) is not a complete description of a single system. It is assumed that the correct complete description, which would involve further (hidden) parameters, would lead to a deterministic theory, from which the probabilistic aspects arise as a result of our ignorance of these extra parameters in the same manner as in classical statistical mechanics.

---

The \(\psi\) - function is therefore regarded as a description of an ensemble of systems rather than a single system. Proponents of this interpretation include Einstein, \(^{3}\) Bohm, \(^{4}\) Wiener and Siegal. \(^{5}\)  

Einstein hopes that a theory along the lines of his general relativity, where all of physics is reduced to the geometry of space- time could satisfactorily explain quantum effects. In such a theory a particle is no longer a simple object but possesses an enormous amount of structure (i.e., it is thought of as a region of space- time of high curvature). It is conceivable that the interactions of such "particles" would depend in a sensitive way upon the details of this structure, which would then play the role of the "hidden variables." \(^{6}\) However, these theories are non- linear and it is enormously difficult to obtain any conclusive results. Nevertheless, the possibility cannot be discounted.  

Bohm considers \(\psi\) to be a real force field acting on a particle which always has a well- defined position and momentum (which are the hidden variables of this theory). The \(\psi\) - field satisfying Schrödinger's equation is pictured as somewhat analogous to the electromagnetic field satisfying Maxwell's equations, although for systems of \(n\) particles the \(\psi\) - field is in a 3n- dimensional space. With this theory Bohm succeeds in showing that in all actual cases of measurement the best predictions that can be made are those of the usual theory, so that no experiments could ever rule out his interpretation in favor of the ordinary theory. Our main criticism of this view is on the grounds of simplicity – if one desires to hold the view that \(\psi\) is a real field then the associated particle is superfluous since, as we have endeavored to illustrate, the pure wave theory is itself satisfactory.

---

Wiener and Siegal have developed a theory which is more closely tied to the formalism of quantum mechanics. From the set \(N\) of all nondegenerate linear Hermitian operators for a system having a complete set of eigenstates, a subset \(I\) is chosen such that no two members of \(I\) commute and every element outside \(I\) commutes with at least one element of \(I\) . The set \(I\) therefore contains precisely one operator for every orientation of the principal axes of the Hilbert space for the system. It is postulated that each of the operators of \(I\) corresponds to an independent observable which can take any of the real numerical values of the spectrum of the operator. This theory, in its present form, is a theory of infinitely many "hidden variables," since a system is pictured as possessing (at each instant) a value for every one of these "observables" simultaneously, with the changes in these values obeying precise (deterministic) dynamical laws. However, the change of any one of these variables with time depends upon the entire set of observables, so that it is impossible ever to discover by measurement the complete set of values for a system (since only one "observable" at a time can be observed). Therefore, statistical ensembles are introduced, in which the values of all of the observables are related to points in a "differential space," which is a Hilbert space containing a measure for which each (differential space) coordinate has an independent normal distribution. It is then shown that the resulting statistical dynamics is in accord with the usual form of quantum theory.  

It cannot be disputed that these theories are often appealing, and might conceivably become important should future discoveries indicate serious inadequacies in the present scheme (i.e., they might be more easily modified to encompass new experience). But from our viewpoint they are usually more cumbersome than the conceptually simpler theory based on pure wave mechanics. Nevertheless, these theories are of great theoretical importance because they provide us with examples that "hidden variables" theories are indeed possible.

---

d. The stochastic process interpretation. This is the point of view which holds that the fundamental processes of nature are stochastic (i.e., probabilistic) processes. According to this picture physical systems are supposed to exist at all times in definite states, but the states are continually undergoing probabilistic changes. The discontinuous probabilistic "quantum-jumps" are not associated with acts of observation, but are fundamental to the systems themselves.  

A stochastic theory which emphasizes the particle, rather than wave, aspects of quantum theory has been investigated by Bopp. The particles do not obey deterministic laws of motion, but rather probabilistic laws, and by developing a general "correlation statistics" Bopp shows that his quantum scheme is a special case which gives results in accord with the usual theory. (This accord is only approximate and in principle one could decide between the theories. The approximation is so close, however, that it is hardly conceivable that a decision would be practically feasible.)  

Bopp's theory seems to stem from a desire to have a theory founded upon particles rather than waves, since it is this particle aspect (highly localized phenomena) which is most frequently encountered in present day high- energy experiments (cloud chamber tracks, etc.). However, it seems to us to be much easier to understand particle aspects from a wave picture (concentrated wave packets) than it is to understand wave aspects (diffraction, interference, etc.) from a particle picture.  

Nevertheless, there can be no fundamental objection to the idea of a stochastic theory, except on grounds of a naked prejudice for determinism. The question of determinism or indeterminism in nature is obviously forever undecidable in physics, since for any current deterministic [probabilistic] theory one could always postulate that a refinement of the theory

---

would disclose a probabilistic [deterministic] substructure, and that the current deterministic [probabilistic] theory is to be explained in terms of the refined theory on the basis of the law of large numbers [ignorance of hidden variables]. However, it is quite another matter to object to a mixture of the two where the probabilistic processes occur only with acts of observation.  

e. The wave interpretation. This is the position proposed in the present thesis, in which the wave function itself is held to be the fundamental entity, obeying at all times a deterministic wave equation.  

This view also corresponds most closely with that held by Schrödinger. However, this picture only makes sense when observation processes themselves are treated within the theory. It is only in this manner that the apparent existence of definite macroscopic objects, as well as localized phenomena, such as tracks in cloud chambers, can be satisfactorily explained in a wave theory where the waves are continually diffusing. With the deduction in this theory that phenomena will appear to observers to be subject to Process 1, Heisenberg's criticism \(^{10}\) of Schrödinger's opinion - that continuous wave mechanics could not seem to explain the discontinuities which are everywhere observed - is effectively met. The "quantum-jumps" exist in our theory as relative phenomena (i.e., the states of an object-system relative to chosen observer states show this effect), while the absolute states change quite continuously.  

The wave theory is definitely tenable and forms, we believe, the simplest complete, self- consistent theory.

---

We should like now to comment on some views expressed by Einstein. Einstein's \(^{11}\) criticism of quantum theory (which is actually directed more against what we have called the "popular" view than Bohr's interpretation) is mainly concerned with the drastic changes of state brought about by simple acts of observation (i.e., the infinitely rapid collapse of wave functions), particularly in connection with correlated systems which are widely separated so as to be mechanically uncoupled at the time of observation. \(^{12}\) At another time he put his feeling colorfully by stating that he could not believe that a mouse could bring about drastic changes in the universe simply by looking at it. \(^{13}\)  

However, from the standpoint of our theory, it is not so much the system which is affected by an observation as the observer, who becomes correlated to the system.  

In the case of observation of one system of a pair of spatially separated, correlated systems, nothing happens to the remote system to make any of its states more "real" than the rest. It had no independent states to begin with, but a number of states occurring in a superposition with corresponding states for the other (near) system. Observation of the near system simply correlates the observer to this system, a purely local process - but a process which also entails automatic correlation with the remote system. Each state of the remote system still exists with the same amplitude in a superposition, but now a superposition for which element contains, in addition to a remote system state and correlated near system state, an observer state which describes an observer who perceives the state of the near system. \(^{14}\) From the present viewpoint all elements of

---

this superposition are equally "real." Only the observer state has changed, so as to become correlated with the state of the near system and hence naturally with that of the remote system also. The mouse does not affect the universe - only the mouse is affected.  

Our theory in a certain sense bridges the positions of Einstein and Bohr, since the complete theory is quite objective and deterministic ("God does not play dice with the universe"), and yet on the subjective level, of assertions relative to observer states, it is probabilistic in the strong sense that there is no way for observers to make any predictions better than the limitations imposed by the uncertainty principle. \(^{15}\)  

In conclusion, we have seen that if we wish to adhere to objective descriptions then the principle of the psycho- physical parallelism requires that we should be able to consider some mechanical devices as representing observers. The situation is then that such devices must either cause the probabilistic discontinuities of Process 1, or must be transformed into the superpositions we have discussed. We are forced to abandon the former possibility since it leads to the situation that some physical systems would obey different laws from the rest, with no clear means for distinguishing between these two types of systems. We are thus led to our present theory which results from the complete abandonment of Process 1 as a basic process. Nevertheless, within the context of this theory, which is objectively deterministic, it develops that the probabilistic aspects of Process 1 reappear at the subjective level, as relative phenomena to observers.  

One is thus free to build a conceptual model of the universe, which postulates only the existence of a universal wave function which obeys a linear wave equation. One then investigates the internal correlations in this wave function with the aim of deducing laws of physics, which are

---

statements that take the form: Under the conditions C the property A of a subsystem of the universe (subset of the total collection of coordinates for the wave function) is correlated with the property B of another subsystem (with the manner of correlation being specified). For example, the classical mechanics of a system of massive particles becomes a law which expresses the correlation between the positions and momenta (approximate) of the particles at one time with those at another time. \(^{16}\) All statements about subsystems then become relative statements, i.e., statements about the subsystem relative to a prescribed state for the remainder (since this is generally the only way a subsystem even possesses a unique state), and all laws are correlation laws.  

The theory based on pure wave mechanics is a conceptually simple causal theory, which fully maintains the principle of the psycho- physical parallelism. It therefore forms a framework in which it is possible to discuss (in addition to ordinary phenomena) observation processes themselves, including the inter- relationships of several observers, in a logical, unambiguous fashion. In addition, all of the correlation paradoxes, like that of Einstein, Rosen, and Podolsky, \(^{17}\) find easy explanation.  

While our theory justifies the personal use of the probabilistic interpretation as an aid to making practical predictions, it forms a broader frame in which to understand the consistency of that interpretation. It transcends the probabilistic theory, however, in its ability to deal logically with questions of imperfect observation and approximate measurement.  

Since this viewpoint will be applicable to all forms of quantum mechanics which maintain the superposition principle, it may prove a fruitful framework for the interpretation of new quantum formalisms. Field theories, particularly any which might be relativistic in the sense of general rela

---

tivity, might benefit from this position, since one is free to construct formal (non- probabilistic) theories, and supply any possible statistical interpretations later. (This viewpoint avoids the necessity of considering anomalous probabilistic jumps scattered about space- time, and one can assert that field equations are satisfied everywhere and everywhere, then deduce any statistical assertions by the present method.)  

By focusing attention upon questions of correlations, one may be able to deduce useful relations (correlation laws analogous to those of classical mechanics) for theories which at present do not possess known classical counterparts. Quantized fields do not generally possess pointwise independent field values, the values at one point of space- time being correlated with those at neighboring points of space- time in a manner, it is to be expected, approximating the behavior of their classical counterparts. If correlations are important in systems with only a finite number of degrees of freedom, how much more important they must be for systems of infinitely many coordinates.  

Finally, aside from any possible practical advantages of the theory, it remains a matter of intellectual interest that the statistical assertions of the usual interpretation do not have the status of independent hypotheses, but are deducible (in the present sense) from the pure wave mechanics, which results from their omission.

---

APPENDIX I 

We shall now supply the proofs of a number of assertions which have been made in the text. 

§1. Proof of Theorem 1 

We now show that \(\{X, Y, \ldots, Z\} > 0\) unless \(X, Y, \ldots, Z\) are independent random variables. Abbreviate \(P(x_i, y_j, \ldots, z_k)\) by \(P_{ij \ldots k}\), and let 

\[
Q_{ij \ldots k} = \begin{cases} \frac{P_{ij \ldots k}}{P_i P_j \ldots P_k} & \text{if } P_i P_j \ldots P_k > 0 \\ 1 & \text{if } P_i P_j \ldots P_k = 0 \end{cases}
\]

(Note that \(P_i P_j \ldots P_k = 0\) implies that also \(P_{ij \ldots k} = 0\).) Then always 

\[
P_{ij \ldots k} = Q_{ij \ldots k} P_i P_j \ldots P_k,
\]

and we have 

\[
\begin{align*}
\{X, Y, \ldots, Z\} &= \exp \left[ \ln \frac{P_{ij \ldots k}}{P_i P_j \ldots P_k} \right] = \exp \left[ \ln Q_{ij \ldots k} \right] \\
&= \sum_{ij \ldots k} P_i P_j \ldots P_k Q_{ij \ldots k} \ln Q_{ij \ldots k}.
\end{align*}
\]

Applying the inequality for \(x \ge 0\): 

\[
x \ln x > x - 1 \quad (\text{except for } x = 1)
\]

(which is easily established by calculating the minimum of \(x \ln x - (x-1)\))
to (1.3) we have:

---

\[\mathrm{P_{i}P_{j}\cdots P_{k}Q_{ij\ldots k}\ln Q_{ij\ldots k} > P_{i}P_{j}\cdots P_{k}(Q_{ij\ldots k} - 1)}\] \[\mathrm{(unless~Q_{ij\ldots k} = 1)~.}\]  

Therefore we have for the sum:  

\[\begin{array}{r l} & {\sum_{\mathbf{i j},\dots \mathbf{k}}\mathbf{P}_{\mathbf{i}}\mathbf{P}_{\mathbf{j}}\dots \mathbf{P}_{\mathbf{k}}\mathbf{Q}_{\mathbf{i j},\dots \mathbf{k}}\ln \mathbf{Q}_{\mathbf{i j},\dots \mathbf{k}} > \sum_{\mathbf{i j},\dots \mathbf{k}}\mathbf{P}_{\mathbf{i}}\mathbf{P}_{j}\dots \mathbf{P}_{\mathbf{k}}\mathbf{Q}_{\mathbf{i j},\dots \mathbf{k}} - \sum_{\mathbf{i j},\dots \mathbf{k}}\mathbf{P}_{\mathbf{i}}\mathbf{\bar{P}}_{j}\dots \mathbf{P}_{\mathbf{k}},}\\ & {\mathrm{unless~all~}\mathbf{Q}_{\mathbf{i j},\dots \mathbf{k}} = 1.~\mathrm{But~}\sum_{\mathbf{i j},\dots \mathbf{k}}\mathbf{P}_{\mathbf{i}}\mathbf{P_{j}}\dots \mathbf{P}_{\mathbf{k}}\mathbf{Q}_{\mathbf{i j},\dots \mathbf k} = \sum_{\mathbf{i j},\dots \mathbf{k}}\mathbf{P}_{\mathbf{i j},\dots \mathbf{k}} = 1,~\mathrm{and}}\\ & {\sum_{\mathbf{i j},\dots \mathbf{k}}\mathbf{P}_{\mathbf{i}}\mathrm{P}_{j}\dots \mathbf{P}_{\mathbf{k}} = 1,~\mathrm{so~that~the~right~side~of~}(1.6)\mathrm{vanishes.~The~left}}\\ & {\mathrm{side~is,~by~}(1.3)\mathrm{the~correlation~}\{\mathbf{X},\mathbf{Y},\dots ,\mathbf{Z}\} ,~\mathrm{and~the~condition~that~all~of~}}\\ & {\mathrm{the~}\mathbf{Q}_{\mathbf{i j},\dots \mathbf{k}}\mathrm{~equal~one~is~precisely~the~independence~condition~that~}}\\ & {\mathbf{P}_{\mathbf{i j},\dots \mathbf{k}} = \mathbf{P}_{\mathbf{i}}\mathbf{P}_{j}\dots \mathbf{P}_{\mathbf{k}}~\mathrm{for~all~}\mathbf{i},\mathbf{j},\dots ,\mathbf{k}.~\mathrm{We~have~therefore~proved~that~}}\\ & {\mathrm{otherwise~}\{\mathbf{X},\mathbf{Y},\dots ,\mathbf{Z}\} >0} \end{array} \quad (1.7)\]  

(1.7) \(\{\mathbf{X},\mathbf{Y},\dots ,\mathbf{Z}\} >0\)  

unless \(\mathbf{X},\mathbf{Y},\dots ,\mathbf{Z}\) are mutually independent.  

## \(\S 2\) . Convex function inequalities  

We shall now establish some basic inequalities which follow from the convexity of the function \(\mathbf{x}\ln \mathbf{x}\) .  

LEMMA 1.  

\[\begin{array}{r l} & {\mathbf{x}_{\mathrm{i}}\geq 0,\quad \mathbf{P}_{\mathrm{i}}\geq 0,\quad \sum_{\mathrm{i}}\mathbf{P}_{\mathrm{i}} = 1}\\ & {\Rightarrow \left(\sum_{\mathrm{i}}\mathbf{P}_{\mathrm{i}}\mathbf{x}_{\mathrm{i}}\right)\ln \left(\sum_{\mathrm{i}}\mathbf{P}_{\mathrm{i}}\mathbf{x}_{\mathrm{i}}{\bf \Phi}\right)\leq \sum_{\mathrm{i}}\mathbf{P}_{\mathrm{i}}\mathbf{x}_{\mathrm{i}}\ln \mathbf{x}_{\mathrm{i}}.} \end{array} \quad (1.8)\]  

This property is usually taken as the definition of a convex function, but follows from the fact that the second derivative of \(\mathbf{x}\ln \mathbf{x}\) is positive for all positive \(\mathbf{x}\) , which is the elementary notion of convexity. There is also an immediate corollary for the continuous case:

---

\[{\mathrm{COROLLARY~1.~}} {\mathrm{g(x)}\geq0,} {\mathrm{P(x)}\geq0,} {\int_{\mathrm{~\scriptstyle~P(x)~}}P(x)\mathrm{d}x=1}\] \[{\Rightarrow\left[\int_{\mathrm{~\scriptstyle~P(x)~}}P(x)\mathrm{g(x)}\mathrm{d}x\right]\ln\left[\int_{\mathrm{~\scriptstyle~P(x)~}}P(x)\mathrm{\mathrm{g(x)}}\mathrm{d}x\right]\leq\int_{\mathrm{~\scriptstyle~P(x)~}}P(x)\mathrm{g(x)}\ln\mathrm{g(x)}\mathrm{d}x.}\]  

We can now derive a more general and very useful inequality from Lemma 1:  

LEMMA 2. \(x_{i} \geq 0, \quad a_{i} \geq 0 \quad (\text{all} i)\)  

\[\Rightarrow \left(\sum_{i} x_{i}\right) \ln \left(\frac{\sum_{i} x_{i}}{\sum_{i} a_{i}}\right) \leq \sum_{i} x_{i} \ln \left(\frac{x_{i}}{a_{i}}\right).\]  

Proof: Let \(\mathrm{P_{i} = a_{i} / \sum_{i}a_{i}}\) , so that \(\mathrm{P_{i} \geq 0}\) and \(\sum_{i} \mathrm{P_{i} = 1}\) . Then by Lemma 1:  

\[\left[\sum_{i} \mathrm{P_{i}} \left(\frac{x_{i}}{a_{i}}\right)\right] \ln \left[\sum_{i} \mathrm{P_{i}} \left(\frac{x_{i}}{\bar{a_{i}}}\right)\right] \leq \sum_{i} \mathrm{P_{i}} \left(\frac{x_{i}}{a_{\bar{i}}}\right) \ln \left(\frac{x_{i}}{a_{\bar{i}}}\right). \quad (2.1)\]  

Substitution for \(\mathrm{P_{i}}\) yields:  

\[\left[\sum_{i} \frac{a_{i}}{\left(\sum_{i} a_{i}\right)} \left(\frac{x_{i}}{a_{i}}\right)\right] \ln \Bigg[\sum_{i} \frac{a_{i}}{\left(\sum_{i} a_{1}\right)} \left(\frac{x_{i}}{a_{1}}\right)\Bigg] \leq \sum_{i} \frac{a_{i}}{\left(\sum_{i} a_{1} \right)} \left(\frac{x_{i}}{a_{1}}\right) \ln \left(\frac{x_{i}}{a_{1}}\right), \quad (2.2)\]  

which reduces to  

\[\left(\sum_{i} x_{i}\right) \ln \left(\frac{\left(\sum_{i} x_{i}\right)}{\left(\sum_{i} a_{i}\right)}\right) \leq \sum_{i} x_{i} \ln \left(\frac{\left(x_{i}\right)}{a_{i}}\right), \quad (2.3)\]  

and we have proved the lemma.

---

We also mention the analogous result for the continuous case: 

\[COROLLARY 2. \( f(x) \ge 0, \quad g(x) \ge 0 \) (all x) \]

\[ \Rightarrow \left[ \int f(x) dx \right] \ln \left[ \frac{\int f(x) dx}{\int g(x) dx} \right] \le \int f(x) \ln \left( \frac{f(x)}{g(x)} \right) dx. \]

## §3. Refinement theorems 

We now supply the proof for Theorems 2 and 4 of Chapter II, which concern the behavior of correlation and information upon refinement of the distributions. We suppose that the original (unrefined) distribution is \(P_{ij...k} = P(x_i, y_j, ..., z_k)\), and that the refined distribution is \(P_{ij...k}^{\mu_i, \nu_j, ..., \eta_k}\), where the original value \(x_i\) for \(X\) has been resolved into a number of values \(x_i^{\mu_i}\), and similarly for \(Y, ..., Z\). Then: 

\[ (3.1) \quad P_{ij...k} = \sum_{\mu_i, \nu_j, ..., \eta_k} P_{ij...k}^{\mu_i, \nu_j, ..., \eta_k}, \quad P_i = \sum_{\mu_i} P_i^{\mu_i}, \quad \text{etc.} \]

Computing the new correlation \(\{X, Y, ..., Z\}'\) for the refined distribution \(P_{ij...k}^{\mu_i, \nu_j, ..., \eta_k}\) we find: 

\[ (3.2) \quad \{X, Y, ..., Z\}' = \sum_{ij...k} \sum_{\mu_i, \nu_j, ..., \eta_k} P_{ij... k}^{\mu_i, \nu_j, ..., \eta_k} \ln \left( \frac{P_{ij...k}^{\mu_i, \nu_j, ..., \eta_k}}{P_i^{\mu_i} P_j^{\nu_j} \cdots P_k^{\eta_k}} \right). \]

However, by Lemma 2, §2: 

\[ (3.3) \quad \left( \sum_{\mu_i, \cdots, \eta_k} P_{i \cdots k}^{\mu_i, \cdots, \eta_k} \right) \ln \left( \frac{\sum_{\mu_i, \cdots, \eta_k} P_{i \cdots k}^{\cdots, \eta_k}}{\sum_{\mu_i, \cdots, \eta_k} P_i^{\mu_i} P_j^{\nu_j} \cdots P_k^{\eta_k}}  \right) \le \sum_{\mu_i, \cdots, \eta_k} P_{i \cdots k}^{ \mu_i, \cdots, \eta_k} \ln \left( \frac{P_{i \cdots k}^{\mu_i, \cdots, \eta_k}}{P_i^{\mu_i} P_j^{\nu_j} \cdots P_{k}^{\eta_k}} \right). \]

---

Substitution of (3.3) into (3.2), noting that \(\sum_{\mu_{1}\dots \eta_{k}} \mathrm{P}_{i}^{\mu_{1}} \mathrm{P}_{j}^{\nu_{1}} \dots \mathrm{P}_{k}^{\nu_{k}}\) is equal to \(\left(\sum_{\mu_{1}} \mathrm{P}_{i}^{\mu_{1}}\right) \left(\sum_{\nu_{j}} \mathrm{P}_{j}^{\nu_{j}}\right) \dots \left(\sum_{\eta_{k}} \mathrm{P}_{k}^{\eta_{k}}\right)\) , leads to:  

\[\begin{array}{r l} & {\mathrm{i}\mathbf{X},\mathbf{Y},\dots,\mathbf{Z}\mathbf{Y}\overset {\geq}{=}\left(\sum_{\mathbf{i}\mathbf{j}\dots \mathbf{k}}\sum_{\mu_{1}\dots \eta_{k}}\mathrm{P}_{i j\dots \mathbf{k}}^{\mu_{1}\dots \eta_{k}}\right)\ln \left[\frac{\sum_{\mu_{1}\dots \eta_{k}}\mathrm{P}_{i j\dots\mathbf{k}}^{\mu_{1}\dots\eta_{k}}}{\left(\sum_{\mu_{1}}\mathrm{P}_{i}^{\mu_{1}}\right)\left(\sum_{\nu_{j}}\mathrm{P}_{j}^{\nu_{j}}\right)\dots\left(\sum_{\eta_{k}}\mathrm{P}_{k}^{\eta_{k}}\right)}\right]}\\ & {\qquad = \sum_{\mathbf{i}\mathbf{j}\dots \mathbf{k}}\mathrm{P}_{i j\dots \mathbf{k}}\ln \frac{\mathrm{P}_{i j\dots\mathbf{k}}}{\mathrm{P}_{i}\mathrm{P}_{j}\dots\mathrm{P}_{k}} = \{\mathbf{X},\mathbf{Y},\dots,\mathbf{Z}\} ,} \end{array} \quad (3.4)\]  

and we have completed the proof of Theorem 2 (Chapter II), which asserts that refinement never decreases the correlation.²  

We now consider the effect of refinement upon the relative information. We shall use the previous notation, and further assume that \(\mathbf{a}_{i}^{\mu_{1}} \mathbf{b}_{j}^{\nu_{1}} \dots , \mathbf{c}_{k}^{\nu_{k}}\) are the information measures for which we wish to compute the relative information of \(\mathrm{P}_{i j \dots \mathbf{k}}^{\mu_{1} \nu_{1} \nu_{2} \dots \nu_{k}}\) and of \(\mathrm{P}_{i j \dots \mathbf{k}}\) . The information measures for the unrefined distribution \(\mathrm{P}_{i j \dots \mathbf{k}}\) then satisfy the relations:  

\[\mathbf{a}_{i} = \sum_{\mu_{i}} \mathbf{a}_{i}^{\mu_{i}}, \quad \mathbf{b}_{j} = \sum_{\nu_{j}} \mathbf{b}_{j}^{\nu_{j}}, \dots . \quad (3.5)\]  

The relative information of the refined distribution is  

\[\mathrm{I}_{X Y\dots Z}^{\prime} = \sum_{\mathbf{i}\dots \mathbf{j}}\sum_{\mu_{\mathbf{i}}\dots \eta_{\mathbf{k}}}\mathrm{P}_{i j\dots \mathbf{k}}^{\mu_{\mathbf{i}}\dots \eta_{\mathbf{k}}}\ln \left[\frac{\mathrm{P}_{i j\dots\mathbf{k}}^{\mu_{\mathbf{i}}\dots\eta_{\mathbf{k}}}}{\mathbf{a}_{i}^{\mu_{\mathbf{i}}}\mathbf{b}_{j}^{\nu_{\mathbf{j}}}\dots\mathbf{c}_{k}^{\nu_{\mathbf{k}}}}\right], \quad (3.6)\]  

and by exactly the same procedure as we have just used for the correlation we arrive at the result:

---

\[I_{XY\dots Z}^{\mathrm{n}}\geq \sum_{\mathbf{i}\dots \mathbf{k}}\mathrm{P}_{\mathbf{i}\mathbf{j}\dots \mathbf{k}}\ln \frac{\mathrm{P}_{\mathbf{i}\mathbf{j}\dots \mathbf{k}}}{\mathrm{a}_{\mathbf{i}\mathbf{b}\mathbf{j}\dots \mathbf{c}_{\mathbf{k}}}} = I_{XY\dots Z}^{\mathrm{n}}~, \quad (3.7)\]  

and we have proved that refinement never decreases the relative information (Theorem 4, Chapter II).  

It is interesting to note that the relation (3.4) for the behavior of correlation under refinement can be deduced from the behavior of relative information, (3.7). This deduction is an immediate consequence of the fact that the correlation is a relative information - the information of the joint distribution relative to the product measure of the marginal distributions.  

§4. Monotone decrease of information for stochastic processes  

We consider a sequence of transition-probability matrices \(\mathbf{T_{ij}^{\mathrm{n}}} (\sum_{j} \mathbf{T_{ij}^{\mathrm{n}}} = 1\) for all \(\mathbf{n}\) , \(\mathbf{i}\) , and \(0 \leq \mathbf{T_{ij}^{\mathrm{n}}} \leq 1\) for all \(\mathbf{n}\) , \(\mathbf{i}\) , \(\mathbf{j}\) ), and a sequence of measures \(\mathbf{a_{i}^{\mathrm{n}}} (\mathbf{a_{i}^{\mathrm{n}}} \geq 0)\) having the property that  

\[\mathbf{a_{j}^{\mathrm{n} + 1}} = \sum_{\mathbf{i}}\mathbf{a_{i}^{\mathrm{n}}\mathbf{T_{ij}^{\mathrm{n}}}}. \quad (4.1)\]  

We further suppose that we have a sequence of probability distributions, \(\mathbf{P_{i}^{\mathrm{n}}}\) , such that  

\[\mathbf{P_{j}^{\mathrm{n} + 1}} = \sum_{\mathbf{i}}\mathbf{P_{i}^{\mathrm{n}}\mathbf{T_{ij}^{\mathrm{n}}}}. \quad (4,2)\]  

For each of these probability distributions the relative information \(\mathbf{I}^{\mathrm{n}}\) (relative to the \(\mathbf{a_{i}^{\mathrm{n}}}\) measure) is defined:  

\[\mathbf{I}^{\mathrm{n}} = \sum_{\mathbf{i}}\mathbf{P_{i}^{\mathrm{n}}}\ln \left(\frac{\mathbf{P_{i}^{\mathrm{n}}}}{\mathbf{a_{i}^{\mathrm{n}}}}\right). \quad (4.3)\]  

Under these circumstances we have the following theorem:  

THEOREM. \(\mathbf{I}^{\mathrm{n} + 1} \leq \mathbf{I}^{\mathrm{n}}\) .

---

Proof: Expanding \(\mathbf{I}^{\mathbf{n} + 1}\) we get:  

\[\mathbf{I}^{\mathbf{n} + 1} = \sum_{\mathbf{j}}\mathbf{P}_{\mathbf{j}}^{\mathbf{n} + 1}\ln \left(\frac{\mathbf{P}_{\mathbf{j}}^{\mathbf{n} + 1}}{\mathbf{a}_{\mathbf{j}}^{\mathbf{n} + 1}}\right) = \sum_{\mathbf{j}}\left(\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}\mathbf{T}_{\mathbf{i}\mathbf{j}}^{\mathbf{n}}\right)\ln \left(\frac{\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}\mathbf{T}_{\mathbf{i}j}^{\mathbf{n}}}{\sum_{\mathbf{i}}\mathbf{a}_{\mathbf{i}}^{\mathbf{n}}\mathbf{T}_{\mathbf{i}j}^{\mathbf{n}}}\right). \quad (4.4)\]  

However, by Lemma 2 (S2, Appendix I) we have the inequality  

\[\left(\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}\mathbf{T}_{\mathrm{ij}}^{\mathbf{n}}\right)\ln \frac{\left(\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}\mathbf{T}_{\mathfrak{i}\mathfrak{j}}^{\mathbf{n}}\right)}{\left(\sum_{\mathbf{i}}\mathbf{a}_{\mathbf{i}}^{\mathbf{n}}\mathbf{T}_{\mathfrak{i}\mathfrak{j}}^{\mathbf{n}}\mathbf{\right)}}\leq \sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}\mathbf{T}_{\mathfrak{i}j}^{\mathbf{n}}\ln \frac{\mathbf{P}_{\mathfrak{i}}^{\mathbf{n}}\mathbf{T}_{\mathfrak{i}\mathfrak{j}}^{\mathbf{n}}}{\mathbf{a}_{\mathfrak{i}}^{\mathbf{n}}\mathbf{T}_{\mathfrak{i}\mathfrak{j}}^{\mathbf{n}}}. \quad (4.5)\]  

Substitution of (4.5) into (4.4) yields:  

\[\begin{array}{r l r}{{\mathbf{I}^{\mathbf{n}+1}\leq\sum_{\mathbf{j}}\left(\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}{\mathbf{T}}_{\mathbf{i}\mathbf{j}}^{\mathbf{n}}\ln\frac{\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}}{\mathbf{a}_{\mathbf{i}}^{\mathbf{n}}}\right)=\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}\left(\sum_{\mathbf{j}}{\mathbf{T}}_{\mathbf{i}\mathbf{j}}^{\mathbf{n}}\right)\ln\left(\frac{\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}}{\mathbf{a}_{\mathbf{i}}^{\mathbf{n}}}}\right)}}\\ &{}&{=\sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}\ln\left(\frac{\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}}{\mathbf{a}_{\mathbf{j}}^{\mathbf{n}}}\right)=\mathbf{I}^{\mathbf{n}},}\end{array} \quad (4.6)\]  

and the proof is completed.  

This proof can be successively specialized to the case where \(\mathbf{T}\) is stationary \((\mathbf{T}_{\mathbf{i}\mathbf{j}}^{\mathbf{n}} = \mathbf{T}_{\mathbf{i}\mathbf{j}}\) for all \(\mathbf{n}\) ) and then to the case where \(\mathbf{T}\) is doubly- stochastic \(\left(\sum_{\mathbf{i}}\mathbf{T}_{\mathbf{i}\mathbf{j}} = 1\right.\) for all \(\mathbf{j}\) ):  

COROLLARY 1. \(\mathbf{T}_{\mathbf{i}\mathbf{j}}^{\mathbf{n}}\) is stationary \((\mathbf{T}_{\mathbf{i}\mathbf{j}}^{\mathbf{n}} = \mathbf{T}_{i\mathbf{j}}\) , all \(\mathbf{n}\) ), and the measure \(\mathbf{a}_{\mathbf{i}}\) is a stationary measure \(\left(\mathbf{a}_{\mathbf{j}} = \sum_{\mathbf{i}}\mathbf{a}_{\mathbf{i}}\mathbf{T}_{\mathbf{i}\mathbf{j}}\right)\) , imply that the information, \(\mathbf{I}^{\mathbf{n}} = \sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}\ln \left(\mathbf{P}_{\mathbf{i}}^{\mathbf{n}} / \mathbf{a}_{\mathbf{i}}^{\mathbf{n}}\right)\) , is monotone decreasing. (As before, \(\mathbf{P}_{\mathbf{j}}^{\mathbf{n} + 1} = \sum_{\mathbf{i}}\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}\mathbf{T}_{\mathbf{i},\mathbf{j}}^{\mathbf{n}}\) .)  

Proof: Immediate consequence of preceding theorem.

---

COROLLARY 2. \(\mathbf{T}_{\mathbf{ij}}\) is doubly-stochastic \((\sum_{i}\mathbf{T}_{\mathbf{ij}} = 1\) , all j) implies that the information relative to the uniform measure \((\mathbf{a}_{\mathbf{i}} = 1\) , all i), \(\mathbf{I}^{\mathbf{n}} = \sum_{i}\mathbf{P}_{\mathbf{i}}^{\mathbf{n}}\ln \mathbf{P}_{\mathbf{i}}^{\mathbf{n}}\) , is monotone decreasing.  

Proof: For \(\mathbf{a}_{\mathbf{i}} = 1\) (all i) we have that \(\sum_{i}\mathbf{a}_{\mathbf{i}}\mathbf{T}_{\mathbf{ij}} = \sum_{i}\mathbf{T}_{\mathbf{ij}} = 1 = \mathbf{a}_{\mathbf{j}}\) . Therefore the uniform measure is stationary in this case and the result follows from Corollary 1.  

These results hold for the continuous case also, and may be easily verified by replacing the above summations by integrations, and by replacing Lemma 2 by its corollary.  

§5. Proof of special inequality for Chapter IV (1.7)  

LEMMA. Given probability densities \(\mathbf{P}(\mathbf{r})\) , \(\mathbf{P}_{1}(\mathbf{x})\) , \(\mathbf{P}_{2}(\mathbf{r})\) , with \(\mathbf{P}(\mathbf{r}) = \int \mathbf{P}_{1}(\mathbf{x})\mathbf{P}_{2}(\mathbf{r} - \mathbf{x}\mathbf{r})\mathrm{d}\mathbf{x}\) . Then \(\mathbf{I}_{\mathbf{R}} \leq \mathbf{I}_{\mathbf{X}} - \ln \mathbf{r}\) , where \(\mathbf{I}_{\mathbf{X}} = \int \mathbf{P}_{1}(\mathbf{x})\ln \mathbf{P}_{1}(\mathbf{x})\mathrm{d}\mathbf{x}\) and \(\mathbf{I}_{\mathbf{R}} = \int \mathbf{P}(\mathbf{r})\ln \mathbf{P}(\mathbf{r})\mathrm{d}\mathbf{r}\) .  

Proof: We first note that:  

\[\int \mathbf{P}_{2}(\mathbf{r} - \mathbf{x}\mathbf{r})\mathrm{d}\mathrm{x} = \int \mathbf{P}_{2}(\omega)\frac{\mathrm{d}\omega}{r} = \frac{1}{r} \quad (all r) \quad (5.1)\]  

and that furthermore  

\[\int \mathbf{P}_{2}(\mathbf{r} - \mathbf{x}\boldsymbol {r})\mathrm{d}\boldsymbol {r} = \int \mathbf{P}_{2}(\omega)\mathrm{d}\omega = 1 \quad (all x). \quad (5.2)\]  

We now define the density \(\widetilde{\mathbf{P}}^{\mathbf{r}}(\mathbf{x})\) :  

\[\widetilde{\mathbf{P}}^{\mathbf{r}}(\mathbf{x}) = r\mathbf{P}_{2}(\mathbf{r} - \mathbf{x}\mathbf{r}), \quad (5.3)\]  

which is normalized, by (5.1). Then, according to §2, Corollary 1 Appendix IX), we have the relation:

---

\[(\int \widetilde{\mathbf{P}}^{\mathrm{r}}(\mathbf{x})\mathbf{P}_{1}(\mathbf{x})\mathrm{d}\mathbf{x})\ln \left(\int \widetilde{\mathbf{P}}^{\mathrm{r}}(\mathbf{x})\mathbf{P}_{1}(\mathrm{x})\mathrm{d}\mathbf{x}\right)\leq \int \widetilde{\mathbf{P}}^{\mathrm{r}}(\mathbf{x})\mathbf{P}_{1}(\mathbf{\boldsymbol{x}})\mathrm{d}\mathbf{x}~.\]  

Substitution from (5.3) gives  

\[\left(r\int \mathrm{P}_{2}(\mathrm{r} - \mathrm{x}r)\mathrm{P}_{1}(\mathrm{x})\mathrm{d}\mathrm{x}\right)\ln \left(r\int \mathrm{P}_{2}(\mathrm{r} - \mathrm{x}r)\mathrm{\bf P}_{1}(\mathrm{x})\mathrm{d}\mathrm{x}\right)\] \[\qquad \leq r\int \mathrm{P}_{2}(\mathrm{r} - \mathrm{x}r)\mathrm{\bf{P}}_{1}(\mathrm{x})\ln \mathrm{\bf{P}}_{1}(\mathrm{x})\mathrm{d}\mathrm{x}~.\]  

The relation \(\mathbf{P}(\mathbf{r}) = \int \mathbf{P}_{1}(\mathbf{x})\mathbf{P}_{2}(\mathbf{r} - \mathbf{x}\mathbf{r})\mathrm{d}\mathbf{x}\) , together with (5.5) then implies  

\[\mathbf{P}(\mathbf{r})\ln \mathbf{r}\mathbf{P}(\mathbf{r})\leq \int \mathbf{P}_{2}(\mathbf{r} - \mathbf{x}\mathbf{r})\mathbf{P}_{1}(\mathbf{x})\ln \mathbf{P}_{1}(\mathbf{x})\mathrm{d}\mathbf{x}~, \quad (5.6)\]  

which is the same as:  

\[\mathbf{P}(\mathbf{r})\ln \mathbf{P}(\mathbf{r})\leq \int \mathbf{P}_{2}(\mathbf{r} - x\mathbf{r})\mathbf{P}_{1}(\mathbf{x})\ln \mathbf{P}_{1}(\mathbf{x}) \mathrm{d}\mathbf{x} - \mathbf{P}(\mathbf{r})\ln \mathbf{r}~. \quad (5.7)\]  

Integrating with respect to \(\mathbf{r}\) , and interchanging the order of integration on the right side gives:  

\[\mathrm{I}_{\mathrm{R}} = \int \mathrm{P}(\mathrm{r})\ln \mathrm{P}(\mathrm{r})\mathrm{d}\mathrm{r}\leq \int \left[\int \mathrm{P}_{2}(\mathrm{r} - \mathrm{x}\mathrm{r})\mathrm{d}\mathrm{r}\right]\mathrm{P}_{1}(\mathrm{x})\ln \mathrm{P}_{1}(\mathrm{x})\mathrm{d}\mathrm{x}\] \[\qquad -(\ln \mathrm{r})\int \mathrm{P}(\mathrm{r})\mathrm{d}\mathrm{r}~.\]  

But using (5.2) and the fact that \(\int \mathbf{P}(\mathbf{r})\mathrm{d}\mathbf{r} = 1\) this means that  

\[\mathrm{I}_{\mathrm{R}}\leq \int \mathrm{P}_{1}(\mathbf{x})\ln \mathrm{P}_{1}(\mathbf{x})\mathrm{d}\mathbf{x} - \ln \mathbf{r} = \mathrm{I}_{\mathrm{X}} - \ln \mathbf{r}~, \quad (5.9)\]  

and the proof of the lemma is completed.  

\(\S 6\) . Stationary point of \(\mathrm{I}_{\mathrm{K}} + \mathrm{I}_{\mathrm{X}}\)  

We shall show that the information sum:  

\[\mathrm{I}_{\mathrm{K}} + \mathrm{I}_{\mathrm{X}} = \int_{-\infty}^{\infty}\phi^{*}\phi (\mathrm{k})\ln \phi^{*}\phi (\mathrm{k})\mathrm{d}\mathrm{k} + \int_{-\infty}^{\infty}\psi^{*}\psi (\mathrm{x})\ln \psi^{*}\psi (\mathrm{x})\mathrm{d}\mathrm{x}~,\] \[\mathrm{where~}\phi (\mathrm{k}) = (1 / \sqrt{2\pi})\int_{-\infty}^{\infty}\mathrm{e}^{-\mathrm{i}\mathrm{k}\mathrm{x}}\psi (\mathrm{x})\mathrm{d}\mathrm{x}\]

---

is stationary for the functions:  

\[\psi_{0}(\mathbf{x}) = (1 / 2\pi \sigma_{\mathbf{x}}^{2})^{\frac{1}{4}}\mathrm{e}^{-x^{2} / 4\sigma_{\mathbf{x}}^{2}},\phi_{0}(\mathbf{k}) = (2\sigma_{\mathbf{x}}^{2} / \pi)^{\frac{1}{4}}\mathrm{e}^{-k^{2}\sigma_{\mathbf{x}}^{2}}, \quad (6.2)\]  

with respect to variations of \(\psi\) , \(\delta \psi\) , which preserve the normalization:  

\[\int_{-\infty}^{\infty}\delta (\psi^{*}\psi)\mathrm{d}x = 0. \quad (6.3)\]  

The variation \(\delta \psi\) gives rise to a variation \(\delta \phi\) of \(\phi (\mathbf{k})\) :  

\[\delta \phi = (1 / \sqrt{2\pi})\int_{-\infty}^{\infty}\mathrm{e}^{-\mathrm{i}k x}\delta \psi \mathrm{d}x. \quad (6.4)\]  

To avoid duplication of effort we first calculate the variation \(\delta I_{\xi}\) for an arbitrary wave function \(u(\xi)\) . By definition,  

\[\mathrm{I}_{\xi} = \int_{-\infty}^{\infty}u^{*}(\xi)u(\xi)\ln u^{*}(\xi)u(\xi)\mathrm{d}\xi , \quad (6.5)\]  

so that  

\[\begin{array}{l}{\delta \mathrm{I}_{\xi} = \int_{-\infty}^{\infty}[\mathrm{u}^{*}\mathrm{u}\delta (\ln \mathrm{u}^{*}\mathrm{u}) + \delta (\mathrm{u}^{*}\mathrm{u})\ln \mathrm{u}^{*}\mathrm{u}]\mathrm{d}\xi}\\ {= \int_{-\infty}^{\infty}(1 + \ln \mathrm{u}^{*}\mathrm{u})(\mathrm{u}^{*}\delta \mathrm{u}\mathrm{u}\delta \mathrm{u}^{*})\mathrm{d}\xi .} \end{array} \quad (6.6)\]  

We now suppose that \(u\) has the real form:  

\[u(\xi) = \mathrm{a}\mathrm{e}^{-\mathrm{b}\xi^{2}} = \mathrm{u}^{*}(\xi), \quad (6.7)\]  

and from (6.6) we get  

\[\delta \mathrm{I}_{\xi} = \int_{-\infty}^{\infty}(1 + \ln \mathrm{a}^{2} - 2\mathrm{b}\xi^{2})\mathrm{a}\mathrm{e}^{-\mathrm{b}\xi^{2}}(\delta \mathrm{u})\mathrm{d}\xi +\mathrm{complex~conjugate}. \quad (6.8)\]  

We now compute \(\delta \mathrm{I}_{\mathrm{K}}\) for \(\phi_{0}\) using (6.8), (6.2), and (6.4):  

\[\delta \mathrm{I}_{\mathrm{K}}\Big|_{\phi_{0}} = \int_{-\infty}^{\infty}(1 + \ln \mathrm{a}^{2} - \mathrm{2b}\mathrm{k}^{2})\mathrm{a}\mathrm{e}^{-\mathrm{b}\mathrm{k}^{2}}\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\mathrm{e}^{-\mathrm{i}\mathrm{k}\mathrm{x}}\delta \psi \mathrm{d}x\mathrm{d}\mathrm{k} + \mathrm{c.c.}, \quad (6.9)\]

---

where  

\[\mathbf{a} = (2\sigma_{\mathbf{x}}^{2} / \pi)^{4},\quad \mathbf{b}^{\prime} = \sigma_{\mathbf{x}}^{2}.\]  

Interchanging the order of integration and performing the definite integration over \(\mathbf{k}\) we get:  

\[\delta \mathrm{I}_{\mathrm{K}}\Big|_{\phi_{0}} = \int_{-\infty}^{\infty}\frac{\mathrm{a}^{\prime}}{\sqrt{2b^{2}}}\Big(\ln \mathrm{a}^{\prime 2} + \frac{\mathrm{x}^{2}}{2b^{2}}\Big)\mathrm{e}^{-(\mathrm{x}^{2} / 4b^{\prime})}\delta \psi (\mathrm{x})\mathrm{d}\mathrm{x} + \mathrm{c.c.}~, \quad (6.10)\]  

while application of (6.8) to \(\psi_{0}\) gives  

\[\delta \mathrm{I}_{\mathrm{X}}\Big|_{\psi_{0}} = \int_{-\infty}^{\infty}(1 + \ln \mathrm{a}^{\prime 2} - 2\mathrm{b}^{\prime}\mathrm{x}^{2})\mathrm{a}^{\prime \prime}\mathrm{e}^{-\mathrm{b}^{\prime}\mathrm{x}^{2}}\delta \psi (\mathrm{x})\mathrm{d}\mathrm{x} + \mathrm{c.c.}, \quad (6.11)\]  

where  

\[\mathrm{a}^{\prime \prime} = (1 / 2\pi \sigma_{\mathrm{x}}^{2})^{\frac{1}{4}},\quad \mathrm{b}^{\prime \prime} = (1 / 4\sigma_{\mathrm{x}}^{2}).\]  

Adding (6.10) and (6.11), and substituting for \(\mathbf{a}^{\prime}\) , \(\mathbf{b}^{\prime}\) , \(\mathbf{a}^{\prime \prime}\) , \(\mathbf{b}^{\prime \prime}\) , yields:  

\[\delta (\mathrm{I}_{\mathrm{K}} + \mathrm{I}_{\mathrm{X}})\Big|_{\psi_{0}} = (1 - \ln \pi)\int_{-\infty}^{\infty}(1 / 2\pi \sigma_{\mathrm{x}}^{2})^{\frac{1}{4}}\mathrm{e}^{-(\mathrm{x}^{2} / 4\sigma_{\mathrm{x}}^{2})}\delta \psi (\mathrm{x})\mathrm{d}\mathrm{x} + \mathrm{c}. \quad (6.12)\]  

But the integrand of (6.12) is simply \(\psi_{0}(\mathrm{x})\delta \psi (\mathrm{x})\) , so that  

\[\delta (\mathrm{I}_{\mathrm{K}} + \mathrm{I}_{\mathrm{X}}) \Big|_{\psi_{0}} = (1 - \ln \pi) \int_{-\infty}^{\infty} \psi_{0} \delta \psi \mathrm{d}x + \mathrm{c.c.} \quad (6.13)\]  

Since \(\psi_{0}\) is real, \(\psi_{0} \delta \psi + \mathrm{c.c.} = \psi_{0}^{*} \delta \psi + \mathrm{c.c.} = \psi_{0}^{*}  \delta \psi + \psi_{0} \delta \psi^{*} = \delta (\psi^{*} \psi)\) , so that  

\[\delta (\mathrm{I}_{\mathrm{K}} + \mathrm{I}_{\mathrm{X}}\Big|_{\psi_{0}} = (1 - \ln \pi)\int_{-\infty}^{0}\delta (\psi^{*}\psi)\mathrm{d}x = 0~, \quad (6.14)\]  

due to the normality restriction (6.3), and the proof is completed.

---

\[
\begin{align*}
& \text{1. } \text{1. } \text{1. } \text{1. } \dots \text{1. } \text{1. } \dots \text{1. }
\end{align*}
\]

\[
\begin{align*}
& \text{1. } \text{1. } \dots \text{1.} \dots \text{1.} \dots \text{1.} \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \text{1.} \dots \dots \dots \dots \dots \text{1.} \dots \text{1.} \dots \end{align*}
\]

\[
\begin{align*}
& \text{1. } \text{1} \dots \text{1} \dots \text{1} \dots \text{1} \\
& \text{1. } \text{1} \dots \text{1} \\
& \text{1. }
\end{align*}
\]

\[
\begin{align*}
& \text{2. } \text{2. } \text{2. } \dots \text{2. } \dots \text{2.} \dots \text{2.} \dots \dots \dots \dots \dots \dots \dots \dots \text{2.} \dots \dots \dots \dots \dots \text{2.} \dots \text{2.} \dots \end{align*}
\]

\[
\begin{align*}
& \text{2. } \text{2} \dots \text{2} \dots \text{2} \dots \text{2} \\
& \text{2. } \text{2} \dots \text{2} \\
& \text{2. }
\end{align*}
\]

\[
\begin{align*}
& \text{2. } \dots \text{2} \dots \text{2} \dots \text{1} \dots \dots \dots \dots \dots \dots \dots \dots \dots \\
& \text{2. } \dots \text{2} \dots \dots \dots \dots \dots \dots \dots \dots \dots
\end{align*}
\]

\[
\begin{align*}
& \text{2. } \dots \dots \dots \dots \dots \dots \dots \dots \dots \end{align*}
\]

\[
\begin{align*}
& \text{2. } \\
& \text{2. } \\
& \text{2. } \\
& \text{\dots} \dots \dots \dots \dots \dots \dots \dots \dots \dots\\
& \text{2. } \\
& \text{2. } \\
& \text{} \dots \dots \dots \dots \dots \dots \dots \dots \dots \cdots \dots \dots \dots \dots \dots \dots \dots \dots \dots \ldots \dots \dots \dots \dots \dots \dots \dots \dots \dots \vdots \dots \dots \dots \dots \dots \dots \dots \dots \dots \ddots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dotsc \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \\
\end{align*}
\]

\[
\begin{align*}
& \text{2. } \\
& \text{} \dots \dots \dots \dotsc \dots \dots \dots \dots \dots \\
& \text{2. } \\
& \text{} \dots \dots \dots \\
& \text{2. } \\
& \text{} \\
& \text{} \\
& \text{} \\
& \text{} \\
& \text{2. } \\
& \text{} \\
& \text{} \\
\end{align*}
\]

\[
\begin{align*}
& \text{2. } \\
& \\
& \text{2. } \\
& \text{} \\
& \text{} \\
&\text{2. } \\
& \text{} \\
& \text{} \\
& \text{2. } \\
&\text{} \\
& \text{} \\
& \text{} \\
& \text{} \\
& \\
& \text{} \\
& \text{} \\
& \text{} \\
& \text{}
\end{align*}
\]

\[
\begin{align*}
& \text{2. } \\
& \dots \dots \dots \dots \dots \dots \dots \dots \dots \qquad \dots \dots \dots \dots \dots \dots \dots \dots \dots \quad \dots \dots \dots \dots \dots \dots \dots \dots \dots \ \dots \dots \dots \dots \dots \dots \dots \dots \dots \
\end{align*}
\]

\[
\begin{align*}
& \text{2. } \\
& \qquad \dots \dots \dots \dots \dots \dots \dots \dots \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \dots \dots \dots \dots \dots \dots \dots \dots \quad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \dots \dots \dots \dots \dots \dots \dots \dots \qquad \quad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \qquad \quad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \dots \dots \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \qquad \dots \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \quad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \dots \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \quad \quad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \quad \dots \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \dots \quad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \dots \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \dots \quad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \dots \quad \quad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \dots \qquad \quad \qquad \qquad \qquad \qquad \qquad \qquad \quad \quad \qquad \quad \qquad \qquad \qquad \qquad \qquad \qquad \quad \qquad \qquad \quad \qquad \qquad \qquad \qquad \qquad \qquad \quad \dots \qquad \quad \qquad \qquad \qquad \qquad \qquad \qquad \dots \quad \qquad \quad \qquad \qquad \qquad \qquad \qquad \qquad \dots \qquad \quad \quad \qquad \qquad \qquad \qquad \qquad \qquad \quad \quad \quad \quad \qquad \qquad \qquad \qquad \qquad \qquad \quad \qquad \quad \quad \qquad \qquad \qquad \qquad \qquad \quad \quad \quad \quad \quad \qquad \qquad \qquad \qquad \qquad \quad \quad \qquad \quad \quad \qquad \qquad \qquad \qquad \quad \quad \quad \quad \quad \quad \qquad \qquad \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \qquad \quad \quad \quad \quad \quad \quad \quad \quad \qquad \qquad \quad \quad \quad \quad \quad \quad \quad \qquad \quad \qquad \quad \quad \quad \quad \quad \quad \quad \qquad \qquad \qquad \qquad \quad \quad \quad \qquad \qquad \quad \quad \quad \quad \qquad \quad \quad \quad \quad \qquad \quad \quad \quad \qquad \quad \quad \quad \quad \quad \qquad \quad \quad \quad \qquad \qquad \quad \quad \quad \qquad \quad \quad \quad \quad \qquad \qquad \quad \quad \quad \qquad \qquad \quad \quad \qquad \quad \quad \quad \quad \quad \quad \qquad \quad \quad \qquad \quad \quad \quad \quad \quad \qquad \qquad \quad \quad \qquad \quad \qquad \quad \quad \quad \quad \qquad \quad \quad \qquad \quad \qquad \quad \quad \quad \qquad \quad \quad \quad \qquad \quad \qquad \quad \quad \quad \qquad \qquad \quad \quad \qquad \qquad \quad \quad \quad \quad \quad \qquad \quad \quad \qquad \qquad \quad \quad \quad \quad \qquad \qquad \quad \quad \qquad \qquad \qquad \quad \quad \quad \quad \qquad \qquad \quad \qquad \quad \quad \quad \quad \qquad \quad \qquad \quad \quad \qquad \quad \quad \quad \quad \qquad \quad \qquad \qquad \quad \quad \quad \quad \qquad \quad \qquad \quad \qquad \quad \quad \quad \quad \qquad \qquad \quad \qquad \qquad \quad \quad \quad \quad \qquad \qquad \qquad \quad \quad \qquad \quad \quad \quad \quad \qquad \qquad \qquad \quad \qquad \quad \quad \quad \quad \qquad \qquad \qquad \qquad \quad \qquad \qquad \quad \quad \quad \quad \quad \qquad \qquad \quad \qquad \qquad \qquad \qquad \qquad \quad \quad \quad \qquad \quad \qquad \qquad \qquad \qquad \qquad \quad \quad \qquad \qquad \quad \qquad \qquad \qquad \qquad \quad \qquad \qquad \qquad \qquad \quad \qquad \quad \qquad \qquad \quad \qquad \qquad \qquad \qquad \quad \quad \qquad \qquad \qquad \quad \qquad \qquad \qquad \qquad \qquad \quad \qquad \qquad \qquad \quad \qquad \qquad \qquad \qquad \quad \quad \quad \qquad \quad \quad \qquad \qquad \qquad \qquad \qquad \qquad \q

---

## APPENDIX II  

## REMARKS ON THE ROLE OF THEORETICAL PHYSICS  

There have been lately a number of new interpretations of quantum mechanics, most of which are equivalent in the sense that they predict the same results for all physical experiments. Since there is therefore no hope of deciding among them on the basis of physical experiments, we must turn elsewhere, and inquire into the fundamental question of the nature and purpose of physical theories in general. Only after we have investigated and come to some sort of agreement upon these general questions, i.e., of the role of theories themselves, will we be able to put these alternative interpretations in their proper perspective.  

Every theory can be divided into two separate parts, the formal part, and the interpretive part. The formal part consists of a purely logico- mathematical structure, i.e., a collection of symbols together with rules for their manipulation, while the interpretive part consists of a set of "associations," which are rules which put some of the elements of the formal part into correspondence with the perceived world. The essential point of a theory, then, is that it is a mathematical model, together with an isomorphism<sup>1</sup> between the model and the world of experience (i.e., the sense perceptions of the individual, or the "real world" - depending upon one's choice of epistemology).

---

The model nature is quite apparent in the newest theories, as in nuclear physics, and particularly in those fields outside of physics proper, such as the Theory of Games, various economic models, etc., where the degree of applicability of the models is still a matter of considerable doubt. However, when a theory is highly successful and becomes firmly established, the model tends to become identified with "reality" itself, and the model nature of the theory becomes obscured. The rise of classical physics offers an excellent example of this process. The constructs of classical physics are just as much fictions of our own minds as those of any other theory we simply have a great deal more confidence in them. It must be deemed a mistake, therefore, to attribute any more "reality" here than elsewhere.  

Once we have granted that any physical theory is essentially only a model for the world of experience, we must renounce all hope of finding anything like "the correct theory." There is nothing which prevents any number of quite distinct models from being in correspondence with experience (i.e., all "correct"), and furthermore no way of ever verifying that any model is completely correct, simply because the totality of all experience is never accessible to us.  

Two types of prediction can be distinguished; the prediction of phenomena already understood, in which the theory plays simply the role of a device for compactly summarizing known results (the aspect of most interest to the engineer), and the prediction of new phenomena and effects, unsuspected before the formulation of the theory. Our experience has shown that a theory often transcends the restricted field in which it was formulated. It is this phenomenon (which might be called the "inertia" of theories) which is of most interest to the theoretical physicist, and supplies a greater motive to theory construction than that of aiding the engineer.  

From the viewpoint of the first type of prediction we would say that the "best" theory is the one from which the most accurate predictions can be most easily deduced - two not necessarily compatible ideals.

---

Classical physics, for example, permits deductions with far greater ease than the more accurate theories of relativity and quantum mechanics, and in such a case we must retain them all. It would be the worst sort of folly to advocate that the study of classical physics be completely dropped in favor of the newer theories. It can even happen that several quite distinct models can exist which are completely equivalent in their predictions, such that different ones are most applicable in different cases, a situation which seems to be realized in quantum mechanics today. It would seem foolish to attempt to reject all but one in such a situation, where it might be profitable to retain them all.  

Nevertheless, we have a strong desire to construct a single all- embracing theory which would be applicable to the entire universe. From what stems this desire? The answer lies in the second type of prediction - the discovery of new phenomena - and involves the consideration of inductive inference and the factors which influence our confidence in a given theory (to be applicable outside of the field of its formulation). This is a difficult subject, and one which is only beginning to be studied seriously. Certain main points are clear, however, for example, that our confidence increases with the number of successes of a theory. If a new theory replaces several older theories which deal with separate phenomena, i.e., a comprehensive theory of the previously diverse fields, then our confidence in the new theory is very much greater than the confidence in either of the older theories, since the range of success of the new theory is much greater than any of the older ones. It is therefore this factor of confidence which seems to be at the root of the desire for comprehensive theories.  

A closely related criterion is simplicity - by which we refer to conceptual simplicity rather than ease in use, which is of paramount interest to the engineer. A good example of the distinction is the theory of general relativity which is conceptually quite simple, while enormously cumbersome in actual calculations. Conceptual simplicity, like comprehensiveness, has the property of increasing confidence in a theory. A theory

---

containing many ad hoc constants and restrictions, or many independent hypotheses, in no way impresses us as much as one which is largely free of arbitrariness.  

It is necessary to say a few words about a view which is sometimes expressed, the idea that a physical theory should contain no elements which do not correspond directly to observables. This position seems to be founded on the notion that the only purpose of a theory is to serve as a summary of known data, and overlooks the second major purpose, the discovery of totally new phenomena. The major motivation of this viewpoint appears to be the desire to construct perfectly "safe" theories which will never be open to contradiction. Strict adherence to such a philosophy would probably seriously stifle the progress of physics.  

The critical examination of just what quantities are observable in a theory does, however, play a useful role, since it gives an insight into ways of modification of a theory when it becomes necessary. A good example of this process is the development of Special Relativity. Such successes of the positivist viewpoint, when used merely as a tool for deciding which modifications of a theory are possible, in no way justify its universal adoption as a general principle which all theories must satisfy.  

In summary, a physical theory is a logical construct (model), consisting of symbols and rules for their manipulation, some of whose elements are associated with elements of the perceived world. The fundamental requirements of a theory are logical consistency and correctness. There is no reason why there cannot be any number of different theories satisfying these requirements, and further criteria such as usefulness, simplicity, comprehensiveness, pictorability, etc., must be resorted to in such cases to further restrict the number. Even so, it may be impossible to give a total ordering of the theories according to "goodness," since different ones may rate highest according to the different criteria, and it may be most advantageous to retain more than one.  

As a final note, we might comment upon the concept of causality. It should be clearly recognized that causality is a property of a model, and

---

not a property of the world of experience. The concept of causality only makes sense with reference to a theory, in which there are logical dependences among the elements. A theory contains relations of the form "A implies B," which can be read as "A causes B," while our experience, uninterpreted by any theory, gives nothing of the sort, but only a correlation between the event corresponding to B and that corresponding to A.

---

REFERENCES 

[1] D. Bohm, Quantum Theory. Prentice-Hall, New York: 1951. 

[2] D. Bohm, Phys. Rev. 84, 166, 1952 and 85, 180, 1952. 

[3] N. Bohr, in Albert Einstein, Philosopher-Scientist. The Library of Living Philosophers, Inc., Vol. 7, p. 199. Evanston: 1949. 

[4] N. Bohr, Atomic Theory and the Description of Nature. 

[5] F. Bopp, Z. Naturforsch. 2a(4), 202, 1947; 7a 82, 1952; 8a, 6, 1953. 

[6] J. L. Doob, Stochastic Processes. Wiley, New York: 1953. 

[7] A. Einstein, in Albert Einstein, Philosopher-Scientist. The Library of Living Philosophers, Inc. Vol. 7, p. 665. Evanston: 1949. 

[8] A. Einstein, B. Podolsky, N. Rosen, Phys. Rev. 47, 777, 1935. 

[9] A. Einstein, N. Rosen, Phys. Rev. 48, 73, 1935. 

[10] W. Feller, An Introduction to Probability Theory and its Applications. Wiley, New York: 1950. 

[11] D. ter Haar, Elements of Statistical Mechanics. Rinehart, New York, 1954. 

[12] P. R. Halmos, Measure Theory. Van Nostrand, New York: 1950. 

[13] G. H. Hardy, J. E. Littlewood, G. Pólya, Inequalities. Cambridge University Press: 1952. 

[14] W. Heisenberg, in Niels Bohr and the Development of Physics. McGraw-Hill, p. 12. New York: 1955.

---

[15] J. Kelley, General Topology. Van Nostrand, New York: 1955.  

[16] A. I. Khinchin, Mathematical Foundations of Statistical Mechanics. (Translated by George Gamow) Dover, New York: 1949.  

[17] J. von Neumann, Mathematical Foundations of Quantum Mechanics. (Translated by R. T. Beyer) Princeton University Press: 1955.  

[18] E. Schrödinger, Brit. J. Phil. Sci. 3, 109, 233, 1952.  

[19] C. E. Shannon, W. Weaver, The Mathematical Theory of Communication. University of Illinois Press: 1949.  

[20] N. Wiener, I. E. Siegal, Nuovo Cimento Suppl. 2, 982 (1955).  

[21] P. M. Woodward, Probability and Information Theory, with Applications to Radar. McGraw-Hill, New York: 1953.