# Everett long thesis with handwritten corrections 1956-1973.pdf

TABLE OF CONTENTS 

I - INTRODUCTION 

II - PROBABILITY, INFORMATION, AND CORRELATION 

1. Finite Joint Distributions 11 

2. Information For Finite Distributions 13 

3. Correlation For Finite Distributions 15 

4. Generalization and Further Properties of Correlation 18 

5. Information for General Distributions 23 

6. Example: Information Decay in Stochastic Processes 26 

7. Example: Conservation of Information in Classical 

Mechanics 28 

III. - QUANTUM MECHANICS 

1. Composite Systems 34 

2. Information and Correlation in Quantum Mechanics 42 

3. Measurement 53 

IV - OBSERVATION 

1. Formulation of the Problem 63 

2. Deductions 67 

3. Remarks on the Choice of Square-amplitude Measure 79 

4. Several Observers 83

---

V - SUPPLEMENTARY TOPICS 

<table><tr><td>1.</td><td>Macroscopic Objects and Classical Mechanics</td><td>89</td></tr><tr><td>2.</td><td>Amplification Processes</td><td>94</td></tr><tr><td>3.</td><td>Reversibility and Irreversibility</td><td>98</td></tr><tr><td>4.</td><td>Approximate Measurement</td><td>103</td></tr><tr><td>5.</td><td>Discussion of a Spin Measurement Example</td><td>107</td></tr></table>

VI - DISCUSSION 

<table><tr><td>Appendix I</td><td>122</td></tr><tr><td>Appendix II</td><td>132</td></tr><tr><td>List of References</td><td>137</td></tr></table>

---

## I. INTRODUCTION  

We begin, as a way of entering our subject, by characterizing a particular interpretation of quantum theory which, although not representative of the more careful formulations of some writers, is the most common form encountered in textbooks and university lectures on the subject.  

A physical system is described completely by a state function \(\mathcal{V}\) which is an element of a Hilbert space, and which furthermore gives information only concerning the probabilities of the results of various observations which can be made on the system. The state function \(\mathcal{V}\) is thought of as objectively characterizing the physical system, i.e., at all times an isolated system is thought of as possessing a state function, independently of our state of knowledge of it. On the other hand, \(\mathcal{V}\) changes in a causal manner so long as the system remains isolated, obeying a differential equation. Thus there are two fundamentally different ways in which the state function can change:  

Process 1: The discontinuous change brought about by the observation of a quantity with eigenstates \(\hat{p}_1, \hat{p}_2, \dots\) in which the state \(\mathcal{V}\) will be changed to the state \(\hat{p}_1\) with probability \(|\langle \mathcal{V}, \phi \rangle |^2\) .  

Process 2: The continuous, deterministic change of state of the (isolated) system with time according to a wave equation \(\hat{\mathcal{V}} = \mathcal{U}\hat{\mathcal{V}}\) , where \(\mathcal{U}\) is a linear operator.  

The question of the consistency of the scheme arises if one contemplates regarding the observer and his object- system as a single (composite) physical system. Indeed, the situation becomes quite paradoxical if we allow for the existence of more than one observer. Let us consider the case of one observer A, who is performing

---

1 We use here the terminology of von Neumann [17]. 

1.1.1.1.1.1.1.1.1.1.1.
1.1.1.1.1.1.1.1.1.1
1.1.1.1.1.1.1.1.1.2
1.1.1.1.1.1.1.1.1.3
1.1.1.1.1.1.1.1.1.4
1.1.1.1.1.1.1.1.1.5
1.1.1.1.1.1.1.1.1.6
1.1.1.1.1.1.1.1.1.7
1.1.1.1.1.1.1.1.1.8
1.1.1.1.1.1.1.1.1.9
1.1.1.1.1.1.1.1.1.0
1.1.1.1.1.1.1.1.1.

---

measurements upon a system S, the totality (A + S) in turn forming the object- system for another observer, B.  

If we are to deny the possibility of B's use of a quantum mechanical description (wave function obeying wave equation) for A + S, then we must be supplied with some alternative description for systems which contain observers (or measuring apparatus). Furthermore, we would have to have a criterion for telling precisely what type of systems would have the preferred positions of "measuring apparatus" or "observer" and be subject to the alternate description. Such a criterion is probably not capable of rigorous formulation.  

On the other hand, if we do allow B to give a quantum description to A + S, by assigning a state function \(\psi^{A + S}\) , then, so long as B does not interact with A + S, its state changes causally according to Process 2, even though A may be performing measurements upon S. From B's point of view, nothing resembling Process 1 can occur (there are no discontinuities), and the question of the validity of A's use of Process 1 is raised. That is, apparently either A is incorrect in assuming Process 1, with its probabilistic implications, to apply to his measurements, or else B's state function, with its purely causal character, is an inadequate description of what is happening to A + S.  

To better illustrate the paradoxes, which can arise from strict adherence to this interpretation we consider the following amusing, but extremely hypothetical drama.  

Isolated somewhere out in space is a room containing an observer, A, who is about to perform a measurement upon a system S. After performing his measurement he will record the result in his notebook. We assume that he knows the state function of S (perhaps as a result of previous measurement), and that it is not an eigenstate of the measurement he is about to perform. A, being an orthodox quantum theorist, then believes that the outcome of his measurement is undetermined and that the process is correctly described by Process 1.

---

In the meantime, however, there is another observer, B, outside the room, who is in possession of the state function of the entire room, including S, the measuring apparatus, and A, just prior to the measurement. B is only interested in what will be found in the notebook one week hence, so he computes the state function of the room for one week in the future according to Process 2. One week passes, and we find B still in possession of the state function of the room, which this equally orthodox quantum theorist believes to be a complete description of the room and its contents. If B's state function calculation tells beforehand exactly what is going to be in the notebook, then A is incorrect in his belief about the indeterminacy of the outcome of his measurement. We therefore assume that B's state function contains non- zero amplitudes over several of the notebook entries.  

At this point, B opens the door to the room and looks at the notebook (performs his observation). Having observed the notebook entry, he turns to A and informs him in a patronizing manner that since his (B's) wave function just prior to his entry into the room, which he knows to have been a complete description of the room and its contents, had non- zero amplitude over other than the present result of the measurement, the result must have been decided only when B entered the room, so that A, his notebook entry, and his memory about what occurred one week ago had no independent objective existence until the intervention by B. In short, B implies that A owes his present objective existence to B's generous nature which compelled him to intervene on his behalf. However, to B's consternation, A does not react with anything like the respect and gratitude he should exhibit towards B, and at the end of a somewhat heated reply, in which A conveys in a colorful manner his opinion of B and his beliefs, he rudely punctures B's ego by observing that

---

if B's view is correct, then he has no reason to feel complacent, since the whole present situation may have no objective existence, but may depend upon the future actions of yet another observer.  

It is now clear that the interpretation of quantum mechanics with which we began is untenable if we are to consider a universe containing more than one observer. We must therefore seek a suitable modification of this scheme, or an entirely different system of interpretation. Several alternatives which avoid the paradox are:  

Alternative 1: To postulate the existence of only one observer in the universe. This is the solipsist position, in which each of us must hold the view that we alone are the only valid observer, with the rest of the universe and its inhabitants obeying at all times Process 2 except when under our observation.  

This view is quite consistent, but one must feel uneasy when, for example, writing textbooks on quantum mechanics, describing Process 1, for the consumption of other persons to whom it does not apply.  

Alternative 2: To limit the applicability of quantum mechanics by asserting that the quantum mechanical description fails when applied to observers, or to measuring apparatus, or more generally to systems approaching macroscopic size.  

If we try to limit the applicability so as to exclude measuring apparatus, or in general systems of macroscopic size, we are faced with the difficulty of sharply defining the region of validity. For what might a group of n particles be construed as forming a measuring device so that the quantum description fails? And to draw

---

the line at human or animal observers, i.e., to assume that all mechanical apparatus obeys the usual laws, but that they are somehow not valid for living observers, does violence to the so- called principle of psycho- physical parallelism<sup>2</sup>, and constitutes a view to be avoided, if possible. To do justice to this principle we must insist that we be able to conceive of mechanical devices (such a servomechanisms), obeying natural laws, which we would be willing to call observers.  

Alternative 3: To admit the validity of the state function description, but to deny the possibility that B could ever be in possession of the state function of A \(\nleftrightarrow\) S. Thus one might argue that a determination of the state of A would constitute such a drastic intervention that A would cease to function as an observer.  

The first objection to this view is that no matter what the state of A \(\nleftrightarrow\) S is, there is in principle a complete set of commuting operators for which it is an eigenstate, so that, at least, the determination of these quantities will not affect the state nor in any way disrupt the operation of A. There are no fundamental restrictions in the usual theory about the knowability of any state functions, and the introduction of any such restrictions to avoid the paradox must therefore require extra postulates.  

The second objection is that it is not particularly relevant whether or not B actually knows the precise state function of A \(\nleftrightarrow\) S. If he merely believes that the system is described by a state function, which he does not presume to know, then the difficulty still exists. He must then believe that this state function changed deterministically, and hence that there was nothing probabilistic in A's determination.  

Alternative 4: To abandon the position that the state function is a complete description of a system. The state function is

---

2In the words of von Neumann ([17], pg. 418): "...it is a fundamental requirement of the scientific viewpoint--- the so- called principle of the psycho- physical parallelism--- that it must be possible so to describe the extra- physical process of the subjective perception as if it were in  

reality in the physical world---i.e., to assign to its parts equivalent physical processes in the objective environment, in ordinary space.

---

to be regarded not as a description of a single system, but of an ensemble of systems, so that the probabilistic assertions arise naturally from the incompleteness of the description.  

It is assumed that the correct complete description, which would presumably involve further (hidden) parameters beyond the state function alone, would lead to a deterministic theory, from which the probabilistic aspects arise as a result of our ignorance of these extra parameters in the same manner as in classical statistical mechanics.  

Alternative 5: To assume the universal validity of the quantum description, by the complete abandonment of Process 1. The general validity of pure wave mechanics, without any statistical assertions, is assumed for all physical systems, including observers and measuring apparatus. Observation processes are to be described completely by the state function of the composite system which includes the observer and his object- system, and which at all times obeys the wave equation (Process 2).  

This brief list of alternatives is not meant to be exhaustive, but has been presented in the spirit of a preliminary orientation. We have, in fact, omitted one of the foremost interpretations of quantum theory, namely the position of Niels Bohr. The discussion will be resumed in the final chapter, when we shall be in a position to give a more adequate appraisal of the various alternate interpretations. For the present, however, we shall concern ourselves only with the development of Alternative 5.  

It is evident that Alternative 5 is a theory of many advantages. It has the virtue of logical simplicity and it is complete in the

---

sense that it is applicable to the entire universe. All processes are considered equally (there are no "measurement processes" which play any preferred role), and the principle of psycho- physical parallelism is fully maintained. Since the universal validity of the state function description is asserted, one can regard the state functions themselves as the fundamental entities, and one can even consider the state function of the whole universe. In this sense this theory can be called the theory of the "universal wave function," since all of physics is presumed to follow from this function alone. There remains, however, the question of whether or not such a theory can be put into correspondence with our experience.  

The present thesis is devoted to showing that this concept of a universal wave mechanics, together with the necessary correlation machinery for its interpretation, forms a logically self consistent description of a universe in which several observers are at work.  

We shall be able to introduce into the theory systems which represent observers. Such systems can be conceived as automatically functioning machines (servomechanisms) possessing recording devices (memory) and which are capable of responding to their environment. The behavior of these observers shall always be treated within the framework of wave mechanics. Furthermore, we shall deduce the probabilistic assertions of Process 1 as subjective appearances to such observers, thus placing the theory in correspondence with experience. We are then led to the novel situation in which the formal theory is objectively continuous and causal, while subjectively discontinuous and probabilistic. While this point of view thus shall ultimately justify our use of the statistical assertions of the orthodox view, it enables us to do so in a logically consistent manner, allowing for the existence of other observers. At the same time it gives a deeper insight into the meaning of quantized systems, and the role played by quantum mechanical correlations.

---

In order to bring about this correspondence with experience for the pure wave mechanical theory, we shall explat the correlation between subsystems of a composite system which is described by a state function. A subsystem of such a composite system does not, in general, possess an independent state function. That is, in general a composite system cannot be represented by a single pair of subsystem states, but can be represented only by a superposition of such pairs of subsystem states. For example, the Schrodinger wave function for a pair of particles, \(\Psi (z_1, z_2)\) , cannot always be written in the form \(\Psi = \phi (z_1) \eta (z_2)\) , but only in the form \(\Psi = \sum_{i} a_i \phi (z_1) \eta (z_2)\) . In the latter case, there is no single state for Part: i.e. I alone or Particle 2 alone, but only the superposition of such cases.  

In fact, to any arbitrary choice of state for one subsystem there will correspond a relative state for the other subsystem, which will generally be dependent upon the choice of state for the first subsystem, so that the state of one subsystem is not independent, but correlated to the state of the remaining subsystem. Such correlations between systems arise from interaction of the systems, and from our point of view all measurement and observation processes are to be regarded simply as interactions between observer and object- system which produce strong correlations.  

Let one regard an observer as a subsystem of the composite system: observer \(\phi\) object- system. It is then an inescapable consequence that after the interaction has taken place there will not, generally, exist a single observer state. There will, however, be a superposition of the composite system states, each element of which contains a definite observer state and a definite relative object- system state. Furthermore, as we shall see, each of these relative object- system states will be, approximately, the eigenstates of the observation corresponding to the value obtained by the observer which is described by the same element of the superposition. Thus, each element of the resulting superposition describes an

---

observer who perceived a definite and generally different result, and to whom it appears that the object- system state has been transformed into the corresponding eigenstate. In this sense the usual assertions of Process 1 appear to hold on a subjective level to each observer described by an element of the superposition. We shall also see that correlation plays an important role in preserving consistency when several observers are present and allowed to interact with one another (to "consult" one another) as well as with other object- systems.  

In order to develop a language for interpreting our pure wave mechanics for composite systems we shall find it useful to develop quantitative definitions for such notions as the "sharpness" or "definiteness" of an operator A for a state \(\gamma\) , and the "degree of correlation" between the subsystems of a composite system or between a pair of operators in the subsystems, so that we can use these concepts in an unambiguous manner. The mathematical development of these notions will be carried out in the next chapter (II) using some concepts borrowed from Information Theory<sup>3</sup>. We shall develop there the general definitions of information and correlation, as well as some of their more important properties. Throughout Chapter II we shall use the language of probability theory to facilitate the exposition, and because it enables us to introduce in a unified manner a number of concepts that will be of later use. We shall nevertheless subsequently apply the mathematical definitions directly to state functions, by replacing probabilities by square amplitudes, without, however, making any reference to probability models.  

Having set the stage, so to speak, with Chapter II, we turn to quantum mechanics in Chapter III. There we first investigate the quantum formalism of composite systems, particularly the concept of relative state functions, and the meaning of the representation of subsystems by non- interfering mixtures of states characterized by density matrices. The notions of information and correlation are

---

3The theory originated by Claude E. Shannon [19].

---

then applied to quantum mechanics. The final section of this chapter discusses the measurement process, which is regarded simply as a correlation- inducing interaction between subsystems of a single isolated system. A simple example of such a measurement is given and discussed, and some general consequences of the superposition principle are considered.  

This will be followed by an abstract treatment of the problem of Observation (Chapter IV). In this chapter we make use only of the superposition principle, and general rules by which composite system states are formed of subsystem states, in order that our results shall have the greatest generality and be applicable to any form of quantum theory for which these principles hold. (Elsewhere, when giving examples, we restrict ourselves to the non- relativistic Schrödinger Theory for simplicity.) The validity of Process 1 as a subjective phenomenon is deduced, as well as the consistency of allowing several observers to interact with one another.  

Chapter V supplements the abstract treatment of Chapter IV by discussing a number of diverse topics from the point of view of the theory of pure wave mechanics, including the existence and meaning of macroscopic objects in the light of their atomic constitution, amplification processes in measurement, questions of reversibility and irreversibility, and approximate measurement.  

The final chapter summarizes the situation, and continues the discussion of alternate interpretations of quantum mechanics.

---

## II. PROBABILITY, INFORMATION, AND CORRELATION  

The present chapter is devoted to the mathematical development of the concepts of information and correlation. As mentioned in the introduction we shall use the language of, probability theory throughout this chapter to facilitate the exposition, although we shall apply the mathematical definitions and formulas in later chapters without reference to probability models. We shall develop our definitions and theorems in full generality, for probability distributions over arbitrary sets, rather than merely for distributions over real numbers, with which we are mainly interested at present. We take this course because it is easy as the restricted development, and because it gives a better insight into the subject.  

The first three sections develop definitions and properties of information and correlation for probability distributions over finite sets only. In section four the definition of correlation is extended to distributions over arbitrary sets, and the general invariance of the correlation is proved. Section five then generalizes the definition of information to distributions over arbitrary sets. Finally, as illustrative examples, sections seven and eight give brief applications to stochastic processes and classical mechanics, respectively.  

## §1. Finite Joint Distributions  

We assume that we have a collection of finite sets, \(\chi ,\chi ,\ldots ,\chi\) whose elements are denoted by \(x_{1}\times x_{2}\times \ldots \times x_{n}\in \mathcal{Y}\) , etc., and that we have a joint probability distribution, \(P = P(x_{1},y_{1},\ldots ,z_{k})\) , defined on the cartesian product of the sets, which represents the probability of the combined event \(x_{1},y_{1},\ldots ,\) and \(z_{k}\) . We then denote by \(x_{1},y_{1},\ldots ,z\) the random variables whose values are the elements of the sets \(x,y,\ldots ,y\) , with probabilities given by \(P\) .  

For any subset \(Y,\ldots ,Z\) , of a set of random variables \(W,\ldots ,X,Y,\ldots ,Z\) , with joint probability distribution \(P(w_{1},\ldots ,x_{j},y_{k},\ldots ,z_{1})\) , the marginal distribution, \(P(y_{k},\ldots ,z_{1})\) , is defined to be:

---

\[P(y_{k},\ldots z_{1}) = \sum_{j,j}P(w_{1},\ldots x_{j},y_{k},\ldots z_{1}) \quad (1.1)\]  

which represents the probability of the joint occurence of \(y_{k},\ldots z_{1}\) with no restrictions upon the remaining variables.  

For any subset \(Y,\ldots Z\) of a set of random variables the conditional distribution, conditioned upon the values \(W = w_{1},\ldots X = x_{j}\) for any remaining subset \(w,\ldots X\) , and denoted by \(P^{w_{1},\ldots x_{j}}(y_{k},\ldots z_{1})\) , is defined to be:  

\[P^{w_{1},\ldots x_{j}}(y_{k},\ldots z_{1}) = \frac{P(w_{1},\ldots x_{j},y_{k},\ldots z_{1})}{P(w_{1},\ldots,x_{j})} \quad (1.2)\]  

which represents the probability of the joint event \(Y = y_{k},\ldots Z = z_{1}\) , conditioned by the fact that \(w,\ldots X\) are known to have taken the values \(w_{1},\ldots ,x_{j}\) , respectively.  

For any numerical valued function \(P(y_{k},\ldots z_{1})\) , defined on the elements of the cartesian product of \(\mathcal{Y}_{1},\ldots ,\mathcal{Y}_{j}\) , the expectation, denoted by \(\operatorname {Exp}\left[\bar{F}\right]\) , is defined to be:  

\[\operatorname {Exp}\left[\bar{F}\right] = \sum_{k,j}P(y_{k},\ldots z_{1})F(y_{k},\ldots z_{1}) \quad (1.3)\]  

We note that if \(P(y_{k},\ldots z_{1})\) is a marginal distribution of some larger distribution \(P(w_{1},\ldots x_{j},y_{k},\ldots z_{1})\) then  

\[\operatorname {Exp}\left[\bar{F}\right] = \sum_{i,j}\left(\sum_{k,j}P(w_{1},\ldots x_{j},y_{k},\ldots z_{1})\right)F(y_{k},\ldots z_{1})\\ = \sum_{k,j}\sum_{i,j}P(w_{1},\ldots x_{j},y_{k},\ldots z_{1})(F(y_{k},\ldots z_{1}) \quad (1.4)\]  

so that if we wish to compute \(\operatorname {Exp}\left[\bar{F}\right]\) with respect to some joint distribution is suffices to use any marginal distribution of the original distribution which contains at least those variables which occur in \(F\) .  

We shall also occasionally be interested in conditional expectations, which we define as:

---

1 We regard it as undefined if \(P(w_1, \ldots, x_j) = 0\). In this case \(P(w_1, \ldots, x_j, y_k, \ldots, z_1)\) is necessarily zero also.

---

\[\mathrm{Exp}^{v_{1},\dots ,x_{j}}\left[\bar{F}\right] = \sum_{k}\mathrm{P}^{v_{1},\dots ,x_{j}}(y_{k},\dots ,z_{1})\mathrm{F}(y_{k},\dots ,z_{1}) \quad (1.5)\]  

and we note the following easily verified rules for expectations:  

\[\mathrm{Exp}\left[\mathrm{Exp}\left[\bar{F}\right]\right] = \mathrm{Exp}\left[\bar{F}\right]\] \[\mathrm{Exp}^{u_{1},\dots ,v_{j}}\left[\mathrm{Exp}^{u_{1},\dots ,v_{j},v_{k},\dots ,x_{1}}\left[\bar{F}\right]\right] = \mathrm{Exp}^{u_{1},\dots ,v_{j}}\left[\bar{F}\right]\] \[\mathrm{Exp}\left[\bar{F} +\bar{G}\right] = \mathrm{Exp}\left[\bar{F}\right] + \mathrm{Exp}\left[\bar{G}\right]\]  

We should like finally to comment upon the notion of independence. Two random variables \(X\) and \(Y\) with joint distribution \(P(x_{1}, y_{1})\) will be said to be independent if and only if \(P(x_{1}, y_{1})\) is equal to \(P(x_{1})P(y_{1})\) for all \(i, j\) . Similarly, the groups of random variables \((U, V), (W, X), \ldots , (Y, Z)\) will be called mutually independent groups if and only if \(P(u_{1}, \ldots , v_{j}, w_{k}, \ldots , x_{1}, \ldots , y_{m}, \ldots , z_{n})\) is always equal to \(P(u_{1}, \ldots , v_{j})P(w_{k}, \ldots , x_{1}) \ldots P(y_{m}, \ldots , z_{n})\) .  

Independence means that the random variables take on values which are not influenced by the values of other variables with respect to which they are independent. That is, the conditional distribution of one of two independent variables, \(Y\) , conditioned upon the value \(x_{1}\) for the other, is independent of \(x_{1}\) , so that knowledge about one variable tells nothing of the other.  

## §2. Information for Finite Distributions  

Suppose that we have a single random variable \(X\) , with distribution \(P(x_{1})\) . We then define a number, \(I_{X}\) , called the information of \(X\) , to be:  

\[I_{X} = \sum_{i} P(x_{1}) \ln P(x_{1}) = \exp \left[\ln P(x_{1})\right] \quad (2.1)\]  

which is a function of the probabilities alone and not of any possible numerical values of the \(x_{1}\) 's themselves.  

The information is essentially a measure of the sharpness of a probability distribution, that is, an inverse measure of its "spread". In this respect information plays a role similar to that of variance. However, it has a number of properties which

---

1 This definition corresponds to the negative of the entropy of a probability distribution as defined by Shannon [9].

---

make it a superior measure of the "sharpness" than the variance, not the least of which is the fact that it can be defined for distributions over arbitrary sets, while variance is defined only for distributions over real numbers.  

Any change in the distribution \(\mathbf{P}(\mathbf{x}_{\mathbf{i}})\) which "levels out" the probabilities decreases the information. It has the value zero for "perfectly sharp" distributions, in which the probability is one for one of the \(\mathbf{x}_{\mathbf{i}}\) and zero for all others, and ranges downward to - 1n n for distributions over n elements which are equal over all of the \(\mathbf{x}_{\mathbf{i}}\) . The fact that the information is non- positive is not liability, since we are seldom interested in the absolute information of a distribution, but only in differences.  

We can generalize (2.1) to obtain the formula for the information of a group of random variables \(\mathbf{X},\mathbf{Y},\ldots ,\mathbf{Z}\) , with joint distribution \(\mathbf{P}(\mathbf{x}_{\mathbf{i}},\mathbf{y}_{\mathbf{j}},\ldots ,\mathbf{z}_{\mathbf{k}})\) , which we denote by \(\mathbf{I}_{\mathbf{X}\mathbf{Y}\ldots \mathbf{Z}}\)  

\[\mathrm{I}_{\mathbf{X}\mathbf{Y}\ldots \mathbf{Z}} = \sum_{\mathbf{i},\mathbf{k}}\mathrm{P}(\mathbf{x}_{\mathbf{i}},\mathbf{y}_{\mathbf{j}},\ldots ,\mathbf{z_{\mathbf{k}}})\mathrm{ln}\mathrm{P}(\mathbf{x}_{\mathbf{i}},\mathbf{y}_{\mathbf{j}},\ldots ,\mathbf{\bar{z_{\mathbf{k}}}})\] \[= \mathrm{Exp}\Big[\mathrm{ln}\mathrm{P}(\mathbf{x}_{\mathbf{i}},\mathbf{y}_{\mathbf{j}},\mathbf{\bar{z_{\mathbf{k}}}})\Big]\]  

which follows immediately from our previous definition, since the group of random variables \(\mathbf{X},\mathbf{Y},\ldots ,\mathbf{Z}\) may be regarded as a single random variable \(\mathbf{W}\) which takes its values in the cartesian product \(\mathbf{X}\times \mathbf{Y}\times \ldots \times \mathbf{Z}\) .  

Finally, we define a conditional information, \(\mathbf{I}_{\mathbf{X}\mathbf{Y}\ldots \mathbf{Z}}^{\mathbf{V}\mathbf{w}}\) , to be: \(\mathrm{I}_{\mathbf{X}\mathbf{Y}\ldots \mathbf{Z}}^{\mathbf{V}\mathbf{w}} = \sum_{\mathbf{i},\mathbf{j},\mathbf{k}}\mathrm{P}^{\mathbf{V}\mathbf{w}\ldots \mathbf{w}}(\mathbf{x}_{\mathbf{i}},\mathbf{y}_{\mathbf{j}},\ldots ,\mathbf{z}_{\mathbf{i}})\ln \mathrm{P}^{\mathbf{V}\mathbf{w}\ldots \mathbf{w}}(\mathbf{x}_{\mathbf{i},\mathbf{j}},\ldots ,\mathbf{z}_{\mathbf{k}})\)  

a quantity which measures our information about \(\mathbf{X},\mathbf{Y},\ldots \mathbf{Z}\) given that we know that \(\mathbf{V},\ldots \mathbf{W}\) have taken the particular values \(\mathbf{V}_{\mathbf{m}},\ldots \mathbf{V}_{\mathbf{a}}\) .  

For independent random variables \(\mathbf{X},\mathbf{Y},\ldots \mathbf{Z}\) , the following relationship is easily proved:

---

\[I_{X_{1}...Z} = I_{X} + I_{Y} + \dots + I_{Z} \qquad (X,Y,\dots,Z \text{ independent}) \quad (2.4)\]  

so that the information of \(X_{1}...Z\) is the sum of the individual quantities of information, which is in accord with our intuitive feeling that if we are given information about unrelated events, our total knowledge is the sum of the separate amounts of information. We shall generalize this definition later, in §5.  

## §3. Correlation for Finite Distributions  

Suppose that we have a pair of random variables, \(X\) , and \(Y\) , with joint distribution \(P(x_{1}, y_{1})\) . If we say that \(X\) and \(Y\) are correlated, what we intuitively mean is that one learns something about one variable when he is told the value of the other. Let us focus our attention upon the variable \(X\) . If we are not informed of the value of \(Y\) , then our information concerning \(X\) , \(I_{X}\) , is calculated from the marginal distribution \(P(x_{1})\) . However, if we are now told that \(Y\) has the value \(y_{1}\) , then our information about \(X\) changes to the information of the conditional distribution \(P^{Y|X}(x_{1})\) , \(I_{X}^{Y}\) . According to what we have said, we wish the degree correlation to measure how much we learn about \(X\) by being informed of \(Y\) 's value. However, since the change of information, \(I_{X}^{Y} - I_{X}\) , may depend upon the particular value, \(y_{1}\) , of \(Y\) which we are told, the natural thing to do to arrive at a single number to measure the strength of correlation is to consider the expected change in information about \(X\) , given that we are to be told the value of \(Y\) . This quantity we call the correlation information, or for brevity, the correlation, of \(X\) and \(Y\) , and denote it by \(\{x, Y\}\) . Thus  

\[\{x, Y\} = \exp \left[I_{X}^{Y} - I_{X}\right] = \exp \left[I_{X}^{Y}\right] - I_{X} \quad (3.1)\]

---

1A good discussion of information is to be found in Shannon [19], or Woodward [21]. Note, however, that in the theory of communication one defines the information ofstate \(\mathcal{K}_i\) , which has apriori probability \(P_i\) , to be \(- \mu_i\) . We prefer, however, to regard information as a property of the distribution itself.

---

Expanding the quantity Exp \(\left[\mathbf{I}_{x}^{y}\right]\) using (2.3) and the rules for expectations (1.6) - (1.8) we find:  

\[\begin{array}{r l} & {\mathrm{Exp}\left[\mathbf{I}_{x}^{y}\right] = \mathrm{Exp}\left[\mathrm{Exp}^{y}\mathbf{j}\left[\ln \mathbf{P}^{y}\mathbf{j}(\mathbf{x}_{1})\right]\right]}\\ & {\quad = \mathrm{Exp}\left[\ln \frac{\mathbf{P}(\mathbf{x}_{1},\mathbf{y}_{1})}{\mathbf{P}(\mathbf{y}_{1})}\right] = \mathrm{Exp}\left[\ln \mathbf{P}(\mathbf{x}_{1},\mathbf{y}_{1})\right] - \mathrm{Exp}\left[\ln \mathbf{P}(\mathbf{y}_{1})\right]}\\ & {\quad = \mathbf{I}_{X Y} - \mathbf{I}_{Y}} \end{array} \quad (3.2)\]  

and combining with (3.1) we have:  

\[\left\{x,Y\right\} = \mathrm{I}_{X Y} - \mathrm{I}_{X} - \mathrm{I}_{Y} \quad (3.3)\]  

Thus the correlation is symmetric between X and Y, and hence also equal to the expected change of information about Y given that we will be told the value of X. Furthermore, according to (3.3) the correlation corresponds precisely to the amount of "missing information" if we possess only the marginal distributions, i.e., the loss of information if we choose to regard the variables as independent.  

Theorem 1: \(\left\{X,Y\right\} = 0\) if and only if X and Y are independent, and is otherwise strictly positive. (Proof in appendix)  

In this respect the correlation so defined is superior to the usual correlation coefficients of statistics, such as covariance, etc., which can be zero even when the variables are not independent, and which can assume both positive and negative values. An inverse correlation is, after all, quiteus useful as a direct correlation. Furthermore, it has the great advantage of depending upon the probabilities alone, and not upon any numerical values of \(x_{1}\) and \(y_{1}\) , so that it is defined for distributions over sets whose elements are of an arbitrary nature, and not only for distributions over numerical properties. For example, we might have a joint probability distribution for the

---

political party and religious affiliation of individuals. Correlation and information are defined for such distributions, although they possess nothing like covariance or variance. 

We can generalize (3.3) to define a group correlation for the groups of random variables (U...V), (W...X), ..., (Y...Z), denoted by {U...V,W...X, ..., Y...Z} (where the groups are separated by commas), to be: 

\[
\begin{align*}
(3.4) \quad \{U...V,W...X, \dots, Y...Z\} &= I_{U...VW...X \dots Y...Z} \\
&\quad - I_{U...V} - I_{W...X} - \dots - I_{Y...Z}
\end{align*}
\]

again measuring the information deficiency for the group
marginals. Theorem 1 is also satisfied by the group correlation,
so that it is zero if and only if the groups are mutually indepen-
dent. We can, of course, also define conditional correlations
in the obvious manner, denoting these quantities by appending
the conditional values as superscripts, as before. 

We conclude this section by listing some useful formulas
and inequalities which are easily proved: 

\[
(3.5) \quad \{U, V, \dots, W\} = \exp \left[ \ln \frac{P(u_1, v_1, \dots, w_k)}{P(u_1)P(v_j) \dots P(w_k)} \right]
\]

\[
(3.6) \quad \{U, V, \dots, W\} x_1 \cdots y_j = \exp x_1 \cdots y_j \left[ \ln \frac{P(x_1 \cdots y_j(u_k, v_1, \dots, w_m)}{P(x_1 \cdots y_j(u_k)P(x_1 \cdots y_j(v_1) \dots P(x_1 \cdots y_j(w_m)}}} \right]
\]

(conditional correlation) 

\[
\begin{align*}
(3.7) \quad \{ \dots, U, V, \dots \} &= \{ \dots, UV, \dots \} + \{ U, V \} \\
&\quad \{ \dots, U, V, \dots, W, \dots \} = \{ \dots, UV, \dots, W, \dots \} + \{ U, V, \dots, W \} \\
&\quad \text{(comma removal)}
\end{align*}
\]

\[
(3.8) \quad \{ \dots, U, V, \dots \} - \{ \dots, UV, \dots \} = \{ U, V \} - \{ V, W \}
\]

(commutator)

---

(3.9) \(\{x\} = 0\) (definition of bracket with no comma) 

(3.10) \(\{\ldots, xv, \ldots\} = \{\ldots, xv, \ldots\}\) 

(removal of repeated variable within a group) 

(3.11) \(\{\ldots, uv, vw, \ldots\} = \{\ldots, uv, v, \ldots\} + \{v, w\} - I_v\) 

(removal of repeated variable in separate groups) 

(3.12) \(\{x, x\} = -I_x\) (self correlation) 

(3.13) \(\{u, v, x\} \cdots vj \cdots = \{u, v, x\} \cdots vj \cdots\)
\(\{u, w, x\} \cdots wj \cdots = \{u, x\} \cdots wj \cdots\) 

(removal of conditioned variables) 

(3.14) \(\{X, Z\} \cong \{x, Z\}\) 

(3.15) \(\{X, Z\} \cong \{x, Z\} + \{x, Z\} - \{x, Y\}\) 

(3.16) \(\{x, Y, Z\} \cong \{x, Y\} + \{x, Z\}\) 

Note that in the above formulas any random variable W may be replaced by any group XY..Z and the relation holds true, since the set XY..Z may be regarded as the single random variable W, which takes its values in the cartesian product X x Y x ... x Z. 

## § 4. Generalization and further properties of Correlation 

Until now we have been concerned only with finite probability distributions, for which we have defined information and correlation. We shall now generalize the definition of correlation so as to be applicable to joint probability distributions over arbitrary sets of unrestricted cardinality. 

We first consider the effects of refinement of a finite distribution. For example, we may discover that the event \(x_1\) is actually the disjunction of several exclusive events \(\tilde{x}_1, \ldots, \tilde{x}_n\), so that \(x_1\) occurs if any one of the \(\tilde{x}_1\) occurs, i.e. the single event \(x_1\) results from failing to distinguish between the \(\tilde{x}_1\). The probability distribution which distinguishes between the \(\tilde{x}_1\)

---

will be called a refinement of the distribution which does not. In general, we shall say that a distribution \(\mathbf{P}^{\prime} = \mathbf{P}^{\prime}(\mathbf{X}_{1}^{\prime},\mathbf{\bar{y}}_{j}^{\prime})\) is a refinement of \(\mathbf{P} = \mathbf{P}(\mathbf{x}_{1},\ldots \mathbf{y}_{j})\) if  

\[P(x_{1},\ldots y_{j}) = \sum_{A\ldots y}P^{\prime}(\mathbf{x}_{1}^{\prime},\ldots \mathbf{y}_{j}^{\prime}) \quad (all i,\ldots j)\]  

We now state an important theorem concerning the behavior of correlation under a refinement of a joint probability distributions:  

Theorem 2: \(\mathbf{P}^{\prime}\) is a refinement of \(\mathbf{P} \Rightarrow \mathbf{f}(\mathbf{x}, \ldots , \mathbf{y}) \stackrel{\text{def}}{=} \mathbf{f}(\mathbf{x}, \ldots , \mathbf{y})\) so that correlations never decrease upon refinement of a distribution. (Proof in appendix, §3)  

As an example, suppose that we have a continuous probability density \(\mathbf{P}(\mathbf{x}, \mathbf{y})\) . By division of the axes into a finite number of intervals, \(\mathbf{X}_{1}, \mathbf{Y}_{j}\) , we arrive at a finite joint distribution \(\mathbf{P}_{ij}\) , by integration of \(\mathbf{P}(\mathbf{x}, \mathbf{y})\) over the rectangle whose sides are the intervals \(\mathbf{X}_{1}\) and \(\mathbf{Y}_{j}\) , and which represents the probability that \(\mathbf{X} \in \mathbf{X}_{1}\) and \(\mathbf{Y} \in \mathbf{Y}_{j}\) . If we now subdivide the intervals, the new distribution \(\mathbf{P}^{\prime}\) will be a refinement of \(\mathbf{P}\) , and by theorem 2 the correlation \(\{\mathbf{X}, \mathbf{Y}\}\) computed from \(\mathbf{P}^{\prime}\) will never be less than that computed from \(\mathbf{P}\) . Theorem 2 is seen to be simply the mathematical verification of the intuitive notion that closer analysis of a situation in which quantities \(\mathbf{X}\) and \(\mathbf{Y}\) are dependent can never lessen the knowledge about \(\mathbf{Y}\) which can be obtained from \(\mathbf{X}\) .  

This theorem allows us to give a general definition of correlation which will apply to joint distributions over completely arbitrary sets, i.e. for any probability measure on an arbitrary product space, in the following manner:  

Assume that we have a collection of arbitrary sets \(\mathbf{X}, \mathbf{Y}, \ldots , \mathbf{Y}\) and a probability measure, \(\mathbf{P}(\mathbf{X} \mathbf{Y} \mathbf{X} \ldots \mathbf{X} \mathbf{Y})\) , on their cartesian product. Let \(\mathbf{P}^{\prime}\) be any finite partition of \(\mathbf{X}\) into subsets \(\mathbf{X}_{1}^{\prime}\) , \(\mathbf{Y}\) into subsets \(\mathbf{Y}_{1}^{\prime}, \ldots ,\) and \(\mathbf{Y}\) into subsets \(\mathbf{Y}_{k}^{\prime}\) , such that the sets \(\mathbf{X}_{1}^{\prime} \mathbf{X} \mathbf{Y}_{1}^{\prime} \mathbf{X} \ldots \mathbf{X}_{k}^{\prime} \mathbf{Y}_{k}^{\prime}\) of the cartesian product are measurable in the probability measure \(\mathbf{P}\) . Another partition \(\mathbf{P}^{\prime}\) is a

---

1 A measure is a non- negative, countably additive set function, defined on some subsets of a given set. It is a probability measure if the measure of the entire set is unity. See Halmos [2].

---

refinement of \(P^{\prime}, \mathcal{P}^{\prime} \subset P^{\prime \prime}\) if \(\mathcal{P}^{\prime \prime}\) results from \(\mathcal{P}^{\prime \prime}\) by further subdivision of the subsets \(\chi_{1}, \chi_{2}, \ldots , \chi_{k}\) . Each partition \(\mathcal{P}^{\prime \prime}\) results in a finite probability distribution, for which the correlation, \(\{\chi_{1}, \chi_{2}, \ldots , \chi_{k}\}\) , is always defined through (3.3). Furthermore a refinement of a partition leads to a refinement of the probability distribution, so that by theorem 2:  

\[(4.8) \qquad \mathcal{P}^{\prime} \subseteq \mathcal{P}^{\prime \prime} \Rightarrow \{x, y, \ldots , z\} \cong \{x, y, \ldots , z\} \quad (4.8)\]  

Now the set of all partitions is partially ordered under the refinement relation. Moreover, because for any pair of partitions \(\mathcal{P}, \mathcal{P}^{\prime \prime}\) there is always a third partition \(\mathcal{P}^{\prime \prime \prime}\) which is a refinement of both (common lower bound), the set of all partitions forms a directed set. For a function, \(f\) , on a directed set, \(\mathcal{B}\) , one defines a directed set limit, \(\lim f\) ;  

Def: \(\lim f\) exists and is equal to a \(\Leftrightarrow\) for every \(\epsilon > 0\) there exists an \(\alpha \in \mathcal{B}\) such that \(|f(\beta) - a|\in \mathcal{E}\) for every \(\beta \in \mathcal{B}\) for which \(\beta \in \alpha\) .  

It is easily seen from the directed set property of common lower bounds that if this limit exists it is necessarily unique.  

By (4.8) the correlation \(\{x, y, \ldots , z\}\) is a monotone function on the directed set of all partitions. Consequently the directed set limit, which we shall take as the basic definition of the correlation \(\{x, y, \ldots , z\}\) , always exists. (It may be infinite, but it is in every case well defined.) Thus:  

\[\mathsf{D e f} \qquad \{x, y, \ldots , z\} = \lim \{x, y, \ldots , z\}^{\mathcal{P}}\]  

and we have succeeded in our endeavor to give a completely general definition of correlation, applicable to all types of distributions.  

It is an immediate consequence of (4.8) that this directed set limit is the supremum of \(\{x, y, \ldots , z\}^{\mathcal{P}}\) , so that:  

\[(4.9) \qquad \{x, y, \ldots , z\} = \sup \{x, y, \ldots , z\}^{\mathcal{P}}\]

---

1 See Kelley [15], pg. 65.

---

which we could equally well have taken as the definition.  

Due to the fact that the correlation is defined as a limit for discrete distributions, theorem 1 and all of the relations (3.7) to (3.15), which contain only correlation brackets, remain true for arbitrary distributions. Only (3.11) and (3.12), which contain information terms, cannot be extended.  

We can now prove an important theorem about correlation which concerns its invariant nature. Let \(X, Y, \ldots , Z\) be arbitrary sets with probability measure \(M_p\) on their cartesian product. Let \(f\) be any one- one mapping of \(X\) onto a set \(U\) , \(g\) a one- one map of \(Y\) onto \(U\) , ..., and \(h\) a map of \(Z\) onto \(U\) . Then a joint probability distribution over \(X \times Y \times \ldots \times Z\) leads also to one over \(U \times U \times \ldots \times U\) where the probability \(M_p\) induced on the product \(U \times U \times \ldots \times U\) is simply the measure which assigns to each subset of \(U \times U \times \ldots \times U\) the measure which is the measure of its image set in \(X \times Y \times \ldots \times Z\) for the original measure \(M_p\) . (We have simply transformed to a new set of random variables: \(U = f(X)\) , \(V = g(Y)\) , ..., \(W = h(Z)\) .) Consider any partition \(\mathcal{P}\) of \(X, Y, \ldots , Z\) into the subsets \(\{X_i\}, \{Y_i\}, \ldots , \{Z_k\}\) with probability distribution \(P_{ij \ldots k} = M_p(X_i X_j X_k \ldots X_k)\) . Then there is a corresponding partition \(\mathcal{P}'\) of \(U, U, \ldots , U\) into the image sets of the sets of \(P\) , \(\{U_i\}, \{U_j\}, \ldots , \{U_k\}\) , where \(U_i = f(X_i)\) , \(U_j = g(Y_j)\) , ..., \(U_k = h(Z_k)\) . But the probability distribution for \(\mathcal{P}'\) is the same as that for \(\mathcal{P}\) , since \(P_{ij \ldots k} = M_p(U_i U_j U_k \ldots U_k)\) = \(M_p(X_i X_j X_k \ldots X_k) = P_{ij \ldots k}\) so that:  

\[\{X,Y,\ldots ,Z\}^{\mathcal{P}} = \{U,V,\ldots ,W\}^{\mathcal{P}}\]  

Due to the correspondence between the \(\mathcal{P}\) and \(\mathcal{P}_k\) we have that:  

\[\sup_{\mathcal{P}}\{X,Y,\ldots ,Z\}^{\mathcal{P}} = \sup_{\mathcal{P}}\{U,V,\ldots ,W\}^{\mathcal{P}} \quad (4.11)\]  

and by virtue of (4.9) we have proved the following theorems:

---

Theorem 3i. \(\{x, y, \ldots , z\} = \{u, v, \ldots , w\}\) where \(u, v, \ldots , w\) are any one- one images of \(X, Y, \ldots , Z\) , respectively. In other notation: \(\{x, y, \ldots , z\} = \{f(x), g(y), \ldots , h(z)\}\) for all one- one functions \(f, g, \ldots , h\) .  

This means that changing variables to functionally related variables preserves the correlation. Again this is plausible on intuitive grounds, since a knowledge of \(f(x)\) is just as good as knowledge of \(x\) , provided that \(f\) is one- one.  

A special consequence of theorem 3 is that for any continuous probability density \(P(x, y)\) over real numbers the correlation between \(f(x)\) and \(g(y)\) is the same as between \(x\) and \(y\) , where \(f\) and \(g\) are any real valued one- one functions. As an example consider a probability distribution for the position of two particles, so that the random variables are the position coordinates. Theorem 3 then assures us that the position correlation is independent of the coordinate system, even if different coordinate systems are used for each particle! Also for a joint distribution for a pair of events in space- time the correlation is invariant to arbitrary space- time coordinate transformations, again even allowing different transformations for the coordinates of each event.  

These examples illustrate clearly the intrinsic nature of the correlation of various groups for joint probability distributions, which is implied by its invariance against arbitrary (one- one) transformations of the random variables. These correlation quantities are thus fundamental properties of probability distributions. A correlation is an absolute rather than relative quantity, in the sense that the correlation between (numerical valued) random variables is completely independent of the scale of measurement chosen for the quantities.

---

## § 5. Information for General Distributions  

Although we now have a definition of correlation applicable to all probability distributions, we have not yet extended the definition of information past finite distributions. In order to make this extension we first generalize the definition that we gave for discrete distributions to a definition of relative information, for a random variable, relative to a given underlying measure, called the information measure, on the values of the random variable.  

If we assign a measure to the set of values of a random variable, \(X\) , which is simply the assignment of a positive number \(a_{i}\) to each value \(x_{i}\) in the finite case, we define the information of a probability distribution \(P(x_{i})\) relative to this information measure to be:  

\[I_{X} = \sum_{i}\frac{P(x_{i})}{a_{i}}\ln \frac{P(x_{i})}{a_{i}} = \exp \left[\ln \frac{P(x_{i})}{a_{i}}\right] \quad (5.1)\]  

If we have a joint distribution of random variables \(X, Y, \ldots , Z\) , with information measures \(\{a_{i}\}, \{b_{j}\}, \ldots , \{c_{k}\}\) on their values, then we define the total information relative to these measures to be:  

\[I_{X Y\ldots Z} = \sum_{i j\ldots k}\frac{P(x_{i},y_{j},\ldots z_{k})}{a_{i}b_{j}\ldots c_{k}}\ln \frac{P(x_{i},y_{j},\ldots z_{k})}{a_{i}\ldots c_{k}}\] \[\qquad = \exp \left[\ln \frac{P(x_{i},y_{j},\ldots z_{k})}{a\ldots c_{k}}\right]\]  

so that the information measure on the cartesian product set is always taken to be the product measure of the individual information measures.  

We shall now alter our previous position slightly and consider information as always being defined relative to some information measure, so that our previous definition of information is to be regarded as the information relative to the measure

---

for which all the \(a_{1}\) 's, \(b_{1}\) 's, ... and \(c_{k}\) 's are taken to be unity, which we shall henceforth call the uniform measure. 

Let us now compute the correlation \(\left\{x, y, \ldots, z\right\}\) by (3.4) using the relative information: 

\[
\begin{align*}
(5.3) \quad & \left\{x, y, \ldots, z\right\}' = I_{xy \ldots z} - I_x - I_y - \cdots - I_z \\
&= \exp \left[ \ln \frac{P(x_1, y_1, \ldots, z_k)}{a_1 b_1 \ldots c_k} \right] - \exp \left[ \ln \frac{P(x_1)}{a_1} \right] - \cdots - \exp \left[ \ln \frac{P(z_k)}{a_k} \right] \\
&= \exp \left[ \ln \frac{P(x_1, y_1 \ldots z_k)}{P(x_1) P(y_1) \ldots P(z_k)} \right] = \left\{x, y, \ldots, z\right\}
\end{align*}
\]

so that the correlation for discrete distributions, as defined
by (3.4), is independent of the choice of information measure,
and the correlation remains an absolute, not relative quantity.
It can, however, be computed from the information relative to
any information measure through (3.4). 

If we consider refinements, of our distributions, as before,
and realize that such a refinement is also a refinement of the
information measure, then we can prove a relation analogous to
theorem 2: 

Theorem 4: The information of a distribution relative
to a given information measure never decreases under
refinement. (Proof in Appendix) 

Therefore, just as for correlation, we can define the
information of a probability measure \(M_p\) on the cartesian product
of arbitrary sets \(X, Y, \ldots, Z\), relative to the information
measures \(M_x, M_y, \ldots, M_z\) on the individual sets, by considering
finite partitions \(P\) into subsets \(\{X_i\}, \{Y_i\}, \ldots, \{Z_k\}\), for which
we take as the definition of the information:

---

\[I_{X Y..Z}^{\rho} = \sum_{i,j = 1}^{n}I_{X_{i},Y_{j},\ldots ,Y_{j}}^{n}(x_{i},y_{j},\ldots ,y_{j})\ln \frac{I_{X_{i},Y_{j},\ldots ,Y_{j}}^{n}(x_{j},y_{j},\ldots ,y_{j})}{I_{X_{i},Y_{j},\ldots ,Y_{j}}^{n}(x,y_{j},\ldots ,y_{j})} \quad (5.4)\]  

\(I_{X Y..Z}^{\rho}\) is then, as was \([X,Y,\ldots ,z]^{\rho}\) , a monotone function upon the directed set of partitions (by thm. 4), and as before we take the directed set limit for our definition:  

\[I_{X Y..Z} = \lim_{I_{X Y..Z}^{\rho}}I_{X Y..Z}^{\rho} = \sup_{I_{X Y..Z}^{\rho}}I_{X Y..Z}^{\rho} \quad (5.5)\]  

which is then the information relative to the information measures \(\mu_{X}, \mu_{Y}, \ldots , \mu_{Z}\) .  

Now, for functions \(f, g\) on a directed set the existence of \(\lim f\) and \(\lim g\) is a sufficient condition for the existence of \(\lim (f + g)\) , which is then \(\lim f + \lim g\) , provided that this is \(\sigma\) of indeterminate. Therefore:  

\[\begin{array}{r l r}{{\mathrm{Theorem~5:}}}&{\{x,\ldots,y\}=\lim _{x}\{x,\ldots,y\}=\lim _{x}\left[\prod_{x,\ldots y}^{y}-I_{x}^{y}-\ldots-I_{y}^{y}\right]}\\ &{}&{=\ I_{x,\ldots y}-I_{x}-\ldots-I_{y}}\end{array} \quad (5.5)\]  

where the information is taken relative to any information measure for which the expression is not indeterminate. It is sufficient for the validity of the above expression that the basic measures \(\mu_{x}, \ldots , \mu_{y}\) be such that none of the marginal informations \(I_{x} \ldots I_{y}\) shall be positively infinite.  

The latter statement holds since, because of the general relation \(I_{x, y} \geq I_{x} + \ldots + I_{y}\) , the determinateness of the expression is guaranteed so long as all of the \(I_{x}, \ldots I_{y}\) are \(\mathcal{L} + \infty\) .  

Henceforth, unless otherwise noted, we shall understand that information is to be computed with respect to the uniform measure

---

for discrete distributions, and Lebesgue measure for continuous distributions over real numbers. In case of a mixed distribution, with a continuous density \(P(x, y, \ldots , z)\) plus discrete "lumps" \(P'(x, y, \ldots , z_k)\) , we shall understand the information measure to be the uniform measure over the discrete range, and Lebesgue measure over the continuous range. These conventions then lead us to the expressions:  

\[\mathrm{I}_{X Y..Z} = \left\{ \begin{array}{l l}{\sum_{k = 1}^{n}P(x_{1},y_{1},\ldots z_{k})\ln P(x_{1},y_{1},\ldots z_{k})}\\ {\sum_{k = 1}^{n}P(x_{1},y_{1},\ldots z)\ln P(x_{1},y_{1},\ldots z)\mathrm{d}x\mathrm{d}y\ldots\mathrm{d}z}\\ {\sum_{k = 1}^{n}P'(x_{1},\ldots z_{k})\ln P(x_{1},\ldots z_{k})}\\ {+\int_{k = 1}^{n}P(x_{1},\ldots z)\mathrm{d}x\mathrm{d}z} \end{array} \right\} \quad (mixed) \quad (5.6)\]  

The mixed case occurs often in quantum mechanics, for quantities which have both a discrete and continuous spectrum.  

## §6. Example: Information Decay in Stochastic Processes  

As an example illustrating the usefulness of the concept of relative information we shall consider briefly stochastic processes. Suppose that we have a stationary Markov process with a finite number of states \(S_1\) , and that the process occurs at discrete (integral) times \(1, 2, \ldots , n, \ldots\) , at which times the transition probability from the state \(S_1\) to the state \(S_j\) is \(T_{ij}\) . The probabilities \(T_{ij}\) then form what is called a stochastic matrix, i.e. the elements are between 0 and 1, and \(\sum T_{ij} = 1\) for all \(i\) . If at any time \(k\) the probability distribution over the states is \(\left\{ \begin{array}{l} P_k \\ P_j \end{array} \right\}\) then at the next time the probabilities will be \(P_k^{k+1} = \sum_{i} P_i^{k+1} P_{ij}\) .

---

1 See Feller [6], or Doob [6].  

2 A Markov process is a stochastic process whose future development depends only upon its present state, and not on its past history.

---

In the special case where the matrix is doubly- stochastic, which means that \(\sum_{i} \mathbf{P}_{ij}\) , as well as \(\sum_{j} \mathbf{P}_{ij}\) , equals unity, and which amounts to a principle of detailed balancing holding, it is known that the entropy of a probability distribution over the states, defined as \(H = - \sum_{i} \mathbf{P}_{i} \ln \mathbf{P}_{i}\) , is a monotone increasing function of the time. This entropy is, however, simply the negative of the information relative to the uniform measure.  

One can extend this result to more general stochastic processes only if one uses the more general definition of relative information. For an arbitrary stationary process the choice of an information measure which is stationary, i.e. for which.  

\[(6.1) \qquad \mathbf{a}_{\mathbf{j}} = \sum_{i} \mathbf{a}_{i} \mathbf{P}_{i j} \qquad \text{(all j)} \quad (6.1)\]  

leads to the desired result. In this case the relative information  

\[I = \sum_{i} \mathbf{P}_{i} \ln \frac{\mathbf{P}_{i}}{\mathbf{a}_{i}} \quad (6.2)\]  

is a monotone decreasing function of time and constitutes a suitable basis for the definition of the entropy \(H = - I\) . Note that this definition leads to the previous result for doubly- stochastic processes, since the uniform measure, \(\mathbf{a}_{i} = 1\) (all i), is obviously stationary in this case.  

One can furthermore drop the requirement that the stochastic process be stationary, and even allow that there are completely different sets of states, \(\{\mathbf{S}_{i}^{n}\}\) , at each time \(n\) , so that the process is now given by a sequence of matrices \(\mathbf{T}_{i j}^{n}\) representing the transition probability at time \(n\) from state \(\mathbf{S}_{i}^{n}\) to state \(\mathbf{S}_{j}^{n + 1}\) . In this case probability distributions change according to:  

\[(6.3) \qquad \mathbf{P}_{i}^{n + 1} = \sum_{j} \mathbf{P}_{i}^{n} \mathbf{P}_{i j}^{n} \quad (6.3)\]  

If we then choose any time- dependent information measure which satisfies the relations:  

\[(6.4) \qquad \mathbf{a}_{j}^{n + 1} = \sum_{i} \mathbf{a}_{i}^{n} \mathbf{P}_{i j}^{n} \qquad \text{(all j, n)} \quad (6.4)\]

---

then the information of a probability distribution is again monotone decreasing with time. (Proof in appendix.)  

All of these results are easily extended to the continuous case, and we see that the concept of relative information allows us to define entropy for quite general stochastic processes.  

## 7. Example: Conservation of Information in Classical Mechanics  

As a second illustrative example we consider briefly the classical mechanics of a group of particles. The system at any instant is represented by a point, \((x_{1}y_{1}z_{1}p_{1},p_{1},p_{1}, \ldots ,x_{1}y_{1}z_{1}p_{1},p_{1},p_{2},p_{1},p_{2})\) in the phase space of all position and momentum coordinates. The natural motion of the system then carries each point into another, defining a continuous transformation of the phase space into itself. According to Liouville's theorem the measure of a set of points of the phase space is invariant under this transformation. This invariance of measure implies that if we begin with a probability distribution over the phase space, rather than a single point, the total information  

\[I_{\mathrm{total}} = \mathbf{I}_{x_{1}y_{1}z_{1}p_{1}p_{1}p_{1}}\ldots \mathbf{x}_{1}y_{1}z_{1}p_{1}p_{1}p_{1}p_{1}p_{1}p_{1}p_{2} \quad (7.1)\]  

which is the information of the joint distribution for all positions and momenta, remains constant in time.  

In order to see that the total information is conserved, consider any partition of the phase space at one time, \(t_{0}\) , with its information relative to the phase space measure, \(I^{0}(t_{0})\) . At a later time \(t_{1}\) a partition \(\mathcal{P}^{\prime}\) , into the image sets of \(\mathcal{P}\) under the mapping of the space into itself, is induced, for which the probabilities for the sets of \(\mathcal{P}^{\prime}\) are the same as those of the corresponding sets of \(\mathcal{P}\) , and furthermore for which the measures

---

1 See Khinchin [16], pg. 15.

---

are the same, by Liouville's theorem. Thus corresponding to each partition \(\mathcal{P}\) at time \(t_0\) with information \(I^P(t_0)\) , there is a partition \(\mathcal{P}\) at time \(t_1\) with information \(I^P(t_1)\) , which is the same:  

\[I^{\mathcal{P}}(t_1) = I^{\mathcal{P}}(t_0) \quad (7.2)\]  

Due to the correspondence of the \(\mathcal{P}\) 's and \(\mathcal{P}\) 's the supremums of each over all partitions must be equal, and by (5.5) we have proved that  

\[I_{\mathrm{total}}(t_1) = I_{\mathrm{total}}(t_0) \quad (7.3)\]  

and the total information is conserved.  

Now it is known that the individual (mariginal) position and momentum distributions tend to decay, except for rare fluctuations, into the uniform and Maxwellian distributions respectively, for which the classical entropy is a maximum. This entropy is, however, except for the factor of Boltzmann's constant, simply the negative of the marginal information  

\[I_{\mathrm{marginal}} = I_{x1} + I_{y1} + I_{z1} + \ldots +I_{x n} + I_{y n} + I_{z n} \quad (7.4)\]  

which thus tends towards a minimum. But this decay of marginal information is exactly compensated by an increase of the total correlation information  

\[\{total\} = I_{\mathrm{total}} - I_{\mathrm{marginal}} \quad (7.5)\]  

since the total information remains constant. Therefore, if one were to define the total entropy to be the negative of the total information, one could replace the usual second law of thermodynamics by a law of conservation of total entropy, where the increase in the standard (marginal) entropy is exactly

---

compensated by a (negative) correlation entropy. The usual second law then results simply from our renunciation of all correlation knowledge (stosszahlansatz), and not from any intrinsic behavior of classical systems. The situation for classical mechanics is thus in sharp contrast to that of stochastic processes, which are intrinsically irreversible.

---

## LIL - QUANTUM MECHANICS  

Having mathematically formulated the ideas of information and correlation for probability distributions, we turn to the field of quantum mechanics. In this chapter we assume that the states of physical systems are represented by points in a Hilbert space, and that the time dependence of the state of an isolated system is governed by a linear wave equation.  

It is well known that state functions lead to distributions over eigenvalues of Hermitian operators (square amplitudes of the expansion coefficients of the state in terms of the basis consisting of eigenfunctions of the operator) which have the mathematical properties of probability distributions (non- negative and normalized). The standard interpretation of quantum mechanics regards these distributions as actually giving the probabilities that the various eigenvalues of the operator will be observed, when a measurement represented by the operator is performed.  

A feature of great importance to our interpretation is the fact that a state function of a composite system leads to joint distributions over subsystem quantities, rather than independent subsystem distributions, i.e. the quantities in different subsystems may be correlated with one another. The first section of this chapter is accordingly devoted to the development of the formalism of composite systems, and the connection of composite system states and their derived joint distributions with the various possible subsystem- term conditional and marginal distributions. We shall see that there exist relative state functions which correctly give the

---

conditional distributions for all subsystem operators, while marginal distributions can not generally be represented by state functions, but only by density matrices.  

In section 2 the concepts of information and correlation, developed in the preceeding chapter, are applied to quantum mechanics, by defining information and correlation for operators on systems with prescribed states. It is also shown that for composite systems there exists a quantity which can be thought of as the fundamental correlation between subsystems, and a closely related canonical representation of the composite system state. In addition, a stronger form of the uncertainty principle, phrased in information language, is indicated.  

The third section takes up the question of measurement in quantum mechanics, viewed as a correlation producing interaction between physical systems. A simple example of such a measurement is given and discussed. Finally some general consequences of the superposition principle are considered.  

It is convenient at this point to introduce some notational conventions. We shall be concerned with points \(\mathcal{V}\) in a Hilbert space \(\mathcal{H}\) , with scalar product \((\mathcal{V}_1, \mathcal{V}_2)\) . A state is a point \(\mathcal{V}\) for which \((\mathcal{V}, \mathcal{V}) = 1\) . For any linear operator \(A\) we define a functional, \(\langle A \rangle \mathcal{V}\) , called the expectation of \(A\) for \(\mathcal{V}\) , to be:  

\[\langle A\rangle \mathcal{V} = (\mathcal{V},A\mathcal{V})\]  

A class of operators of particular interest is the class of projection operators. The operator \([\phi ]\) , called the projection on \(\phi\)

---

is defined through:  

\[[\phi ]\psi = (\phi ,\psi)\phi\]  

For a complete orthonormal set \(\{\phi_{i}\}\) and a state \(\psi\) we define a square- amplitude distribution, \(P_{1}\) , called the distribution of \(\psi\) over \(\{\phi_{i}\}\) through:  

\[P_{1} = |(\phi_{1},\psi)|^{2} = \langle [\phi_{1}]\rangle \psi\]  

In the probabilistic interpretation this distribution represents the probability distribution over the results of a measurement with eigenstates \(\phi_{1}\) , performed upon a system in the state \(\psi\) . (Hereafter when referring to the probabilistic interpretation we shall say briefly "the probability that the system will be found in \(\phi_{1}\) ", rather than the more cumbersome phrase "the probability that the measurement of a quantity \(B\) , with eigenfunctions \(\{\phi_{i}\}\) , shall yield the eigenvalue corresponding to \(\phi_{1}\) ", which is meant.)  

For two Hilbert spaces \(\mathcal{H}_{1}\) and \(\mathcal{H}_{2}\) , we form the direct product Hilbert space \(\mathcal{H}_{3} = \mathcal{H}_{1} \otimes \mathcal{H}_{2}\) (tensor product) which is taken to be the space of all possible sums of formal products of points of \(\mathcal{H}_{1}\) and \(\mathcal{H}_{2}\) , i.e. the elements of \(\mathcal{H}_{3}\) are those of the form \(\sum_{i} a_{i} \prod_{j} n_{i}\) where \(f_{i} \in \mathcal{H}_{1}\) and \(n_{i} \in \mathcal{H}_{2}\) . The scalar product in \(\mathcal{H}_{3}\) is taken to be \((\sum_{i} a_{i} \prod_{j} n_{i}, \sum_{j} b_{j} f_{j} n_{j}) = \sum_{i} a_{i} b_{j} (f_{i}, f_{j}) (n_{i}, n_{j})\) . It is then easily seen that if \(\{f_{i}\}\) and \(\{n_{i}\}\) form complete orthonormal sets in \(\mathcal{H}_{1}\) and \(\mathcal{H}_{2}\) respectively, then the set of all formal products \(\{\{n_{i}\} \}\) is a complete orthonormal set in \(\mathcal{H}_{3}\) . For any pair of operators \(A, B\) , in \(\mathcal{H}_{1}\) and \(\mathcal{H}_{2}\) there corresponds an operator \(C = A \otimes B\) , the direct product of \(A\) and \(B\) , in \(\mathcal{H}_{3}\) , which can be defined by its effect on the elements \(f_{i} \in \mathcal{H}_{3}\) :  

\[c\{n_{i}\} = A\otimes B\{n_{j}\} = (A\{i\})(B\{j\})\]

---

1 More rigorously, one considers only finite sums, then completes the resulting space to arrive at \(\mathcal{H}_1 \oplus \mathcal{H}_2\) .

---

## 4. Composite systems  

It is well known that if the states of a pair of systems, \(S_{1}\) and \(S_{2}\) , are represented by points in Hilbert spaces \(\mathcal{H}_{1}\) and \(\mathcal{H}_{2}\) respectively, then the states of the composite system \(S = S_{1} + S_{2}\) (the two systems \(S_{1}\) and \(S_{2}\) regarded as a single system \(S\) ) are represented correctly by points of the direct product \(\mathcal{H}_{1} \otimes \mathcal{H}_{2}\) .  

This fact has far reaching consequences which we wish to investigate in some detail. Thus if \(\{\hat{\mathbf{f}}_{i}\}\) is a complete orthonormal set for \(\mathcal{H}_{1}\) , and \(\{\mathcal{H}_{i}\}\) for \(\mathcal{H}_{2}\) , the general state of \(S = S_{1} + S_{2}\) has the form:  

\[(1.1) \quad \mathcal{V}^{S} = \sum_{i,j} a_{ij} \hat{\mathbf{f}}_{i} \hat{\mathbf{f}}_{j} \qquad (\sum_{i} a_{ij} a_{ij} = 1) \quad (1.1)\]  

In this case we shall call \(P_{ij} = a_{ij} a_{ij}\) the joint square- amplitude distribution of \(\mathcal{V}^{S}\) over \(\{\hat{\mathbf{f}}_{i}\}\) and \(\{\mathcal{H}_{i}\}\) . In the standard probabilistic interpretation \(a_{ij} a_{ij}\) represents the joint probability that \(S_{1}\) will be found in the state \(\hat{\mathbf{f}}_{i}\) and \(S_{2}\) will be found in the state \(\mathcal{H}_{i}\) . Following the probabilistic model we now derive some distributions from the state \(\mathcal{V}^{S}\) . Let \(A\) be a Hermitian operator in \(S_{1}\) with eigenfunctions \(\phi_{1}\) and eigenvalues \(\lambda_{1}\) , and \(B\) an operator in \(S_{2}\) with eigenfunctions \(\Theta_{j}\) and eigenvalues \(\lambda_{j}\) . Then the joint distribution of \(\mathcal{V}^{S}\) over \(\{\hat{\mathbf{f}}_{i}\}\) and \(\{a_{ij}\}\) , \(P_{ij}\) , is:  

\[P_{ij} = P(\phi_{i} \text{ and } \Theta_{j}) = |(\phi_{i} \Theta_{j} \mathcal{V}^{S})|^{2} \quad (1.2)\]  

The marginal distributions, of \(\mathcal{V}^{S}\) over \(\{\hat{\mathbf{f}}_{i}\}\) and of \(\mathcal{V}^{S}\) over \(\{a_{ij}\}\) , are:  

\[P_{1} = P(\phi_{1}) = \sum_{i} P_{1j} = \sum_{i} |(\phi_{1} \Theta_{j} \mathcal{V}^{S})|^{2} \quad (1,3)\]

---

and the conditional distributions. \(\mathbf{P}_{j}^{1}\) and \(\mathbf{P}_{j}^{2}\) are: 

\[
\begin{align*}
(1.4) \quad \mathbf{P}_1^1 &= \mathbf{P}(\phi_1 \text{conditioned on } \Theta_1) = \frac{\mathbf{P}_1^1}{\mathbf{P}_1^1} \\
\mathbf{P}_j^1 &= \mathbf{P}(\Theta_1 \text{conditioned on } \phi_j) = \frac{\mathbf{P}_j^1}{\mathbf{P}_1^1}
\end{align*}
\]

we now define the conditional expectation of an operator 

A on \(S_1\), conditioned on \(\Theta_1\) in \(S_2\), denoted by \(\text{Exp} \Theta_1^1 [A]\), to be: 

\[
\begin{align*}
(1.5) \quad \text{Exp} \Theta_1^1 [A] &= \sum_i \lambda_i \mathbf{P}_1^1 = (1/\mathbf{P}_1) \sum_i \mathbf{P}_1^1 \lambda_i \\
&= (1/\mathbf{P}_1) \sum_i \lambda_i (\phi_j \psi^s)^2 = (1/\mathbf{P}_j) \sum_i (\phi_j \phi_j \psi^s)^2 (\phi_j A \phi_j)
\end{align*}
\]

and we define the marginal expectation of A on \(S_1\) to be: 

\[
(1.6) \quad \text{Exp} [A] = \sum_i \mathbf{P}_1 \lambda_i = \sum_{ij} \lambda_i \mathbf{P}_{ij} = \sum_{ij} |(\phi_j \phi_{ij} \psi^s)|^2 (\phi_j A \phi_j)
\]

We shall now introduce projection operators to get more
convenient forms of the conditional and marginal expectations,
which will also exhibit more clearly the degree of dependence of
these quantities upon the chosen basis \(\{\phi_j\}\). Let the operators
\([\phi_j]\) and \([\Theta_j]\) be the projections on \(\phi_j\) in \(S_1\) and \(\Theta_j\) in \(S_2\) respectively,
and let \(I^1\) and \(I^2\) be the identity operators in \(S_1\) and \(S_2\). Then,
making use of the identity \(\psi_j^s [\phi_j \psi^s] \phi_j\) for any complete
orthonormal set \(\{\phi_j\}\), we have: 

\[
(1.7) \quad \langle [\phi_j] [\Theta_j] \rangle \psi^s = (\psi_j^s [\phi_j] [\Theta_j] \psi^s) = (\sum_{kk} (\phi_k \phi_k \psi^s) \phi_k \Theta_j [\Theta_j] \sum_{nn} (\phi_n \phi_n \psi^s) \phi_n \Theta_j) \\
= \sum_{kknn} (\phi_k \phi_k \psi^s) (\phi_n \phi_n \psi^s) \delta_{kk} \delta_{nn} \delta_{jj} \delta_{nn} \\
= (\phi_j \phi_j \psi^s) (\phi_j \phi_j \psi^s) = \mathbf{P}_{jj}
\]

---

So that the joint distribution is given simply by \(\langle [e] \rangle \gamma^s\) . For the marginal distribution we have:  

\[P_{1} = \sum_{j} P_{1j} = \sum_{j} \langle [e] \rangle \gamma^{s} = \langle [e] \langle [e] \rangle \gamma^{s} = \langle [e] \Gamma^{s} \gamma^{s} \gamma^{s} \gamma^{s} \gamma^{s} \rangle \gamma^{s} \gamma^{s} \gamma^{s} \gamma^{s}\]  

and we see that the marginal distribution over the \(\mathcal{E}_i\) is independent of the set \([e_i]\) chosen in \(S_2\) . This result has the consequence in the ordinary interpretation that the expected outcome of measurement in one subsystem of a composite system is not influenced by the choice of quantity to be measured in the other subsystem. This expectation is, in fact, the expectation for the case in which no measurement at all (identity operator) is performed in the other subsystem. Thus no measurement in \(S_2\) can affect the expected outcome of a measurement in \(S_1\) , so long as the result of any \(S_2\) - measurement remains unknown. The case is quite different, however, if this result is known, and we must turn to the conditional distributions and expectations in such a case.  

We now introduce the concept of a relative state- function, which will play a central role in our interpretation of pure wave mechanics. Consider a composite system \(S = S_1 + S_2\) in the state \(\gamma^s\) . To every state \(\eta\) of \(S_2\) we associate a state of \(S_1\) , \(\gamma^r\) rel, called the relative state in \(S_1\) for \(\eta\) in \(S_2\) , through:  

\[P_{1} = \sum_{j} P_{1j} \gamma^{s} = \sum_{j} \langle [e] \rangle \gamma^{s} \gamma^{s} \gamma^{s} \gamma_{j}^{s} \gamma_{j}^{s} \gamma_{j}^{s} \gamma_{i}^{s} \gamma_{i}^{s} \gamma_{i}^{s} \gamma^{s} \gamma_{i}^{s} \gamma_{i}^{s} \gamma_{j}^{s} \gamma_{i}^{s} \gamma^{s} \gamma_{i} \gamma_{i} \gamma_{i} \gamma_{i} \gamma_{j} \gamma_{i} \gamma_{i} \gamma_{i} \gamma_{s} \gamma_{i} \gamma_{i} \gamma_{i} \gamma_{\gamma_{i}} \gamma_{i} \gamma_{i} \gamma_{i} \gamma_{i}\]  

where \([e_i]\) is any complete orthonormal set in \(S_1\) and \(\mathcal{H}\) is a normalization constant.

---

1 In case \(\sum_{1}(\phi_{1}\eta ,\eta^{5})\phi_{1} = 0\) (unnormalizable) then choose any function for the relative function. This ambiguity has no consequences of any importance to us. See in this connection the remarks on pg. (8.38).

---

The first property of \(\psi_{\mathrm{rel}}^{\infty}\) is its uniqueness, i.e. its dependence upon the choice of the basis \(\{\phi_i\}\) only apparent. To prove this, choose another basis \(\{f_k\}\) with \(\phi_i = \sum b_{ik} f_k\). Then \(\sum b_{ij} b_{ik} = \delta_{jk}\), and: 

\[
\begin{align*}
\sum_i (\phi_i \eta \psi^*) \phi_i &= \sum_i \left( \sum_j b_{ij} \phi_j \eta \psi^*) \right) \left( \sum_k b_{ik} f_k \right) \\
&= \sum_{jk} \left( \sum_i b_{ij} b_{ik} \right) \left( \sum_j \eta \psi^*) f_k = \sum_{jk} \delta_{jk} \left( \sum_j \eta \psi^*) f_k \\
&= \sum_k \left( \sum_j \eta \psi^*) f_k
\end{align*}
\]

The second property of the relative state, which justifies its name, is that \(\psi_{\mathrm{rel}}^{\infty}\) correctly gives the conditional expectations of all operators in \(S_1\), conditioned by the state \(\Theta_j\) in \(S_2\). As before let \(A\) be an operator in \(S_1\) with eigenstates \(\phi_i\) and eigenvalues \(\lambda_1\). Then: 

\[
\begin{align*}
(1.10) \quad & \langle A \rangle \psi_{\mathrm{rel}}^{\infty} = \left( \psi_{\mathrm{rel}}^{\infty} A \psi_{\mathrm{rel}}^{\infty} \right) \\
& = \left( N \sum_i (\phi_i \Theta_j \psi^*) \phi_{ij} A N \sum_m (\phi_m \Theta_{ij} \psi^*) \phi_m \right) \\
& = N^2 \sum_{im} (\phi_i \Theta_j \psi^*) (\phi_m \Theta_{ij} \psi^*) \lambda_m \sum_{im} \\
& = N^2 \sum_i \lambda_i P_{ij}
\end{align*}
\]

At this point the normalizer \(\mathbb{H}^2\) can be conveniently evaluated by
using (1.10) to compute: \(\langle \hat{\psi}_{\mathrm{rel}}^{\infty} \rangle = \mathbb{H}^2 \sum_i P_{ij} = \mathbb{H}^2 P_j = 1\), so that 

\[
(1.11) \quad \mathbb{H}^2 = 1/P_j
\]

Substitution of (1.11) in (1.10) yields: 

\[
(1.12) \quad \langle A \rangle \psi_{\mathrm{rel}}^{\infty} = (1/P_j) \sum_i \lambda_i P_{ij} = \sum_i \lambda_i P_j = \exp \Theta_j [A]
\]

---

1 Except if \(\sum_{1}(\phi_{1}^{2}n,\psi^{S})\phi_{1} = 0\) . There is still, of course, no dependence upon the basis.

---

and we see that the conditional expectations of operators are given by the relative states. (This includes, of course, the conditional distributions themselves, since they may be obtained as expectations of projection operators.)  

An important representation of a composite system state \(\psi^{\mathrm{s}}\) in terms of an orthonormal set \(\{\hat{e}_{j}\}\) in one subsystem \(S_{2}\) and the set of relative states \(\{\psi_{\mathrm{rel}}^{\mathrm{e}_{j}}\}\) in \(S_{1}\) is:  

\[\begin{array}{r l r}{{\gamma^{\mathrm{s}s}\sum_{j}\left(\phi_{j}\phi_{j}\psi^{\mathrm{s}}\right)\phi_{j}\Theta_{j}=\sum_{j}\left(\sum_{i}\left(\phi_{j}\phi_{j}\psi^{\mathrm{s}}\right)\phi_{\mathrm{s}}\right)\Theta_{j}}}\\ &{}&{=\sum_{j}\frac{1}{N_{j}}\left[N_{j}\sum_{i}\left(\phi_{j}\phi_{j}\psi^{\mathrm{s}}\phi_{\mathrm{s}}\right)\phi_{\mathrm{s}}\right]}\Theta_{j}}\\ &{}&{=\sum_{j}\frac{1}{N_{j}}\gamma_{\mathrm{rel}}^{\mathrm{e}_{j}}\Theta_{j}\qquad\mathrm{where~}1/N_{j}^{2}=\mathrm{P}_{j}=\left\langle1^{\mathrm{s}}\left[\Theta_{j}\right]\right\rangle\psi^{\mathrm{s}}}\end{array} \quad (1.13)\]  

Thus, for any orthonormal set in one subsystem, the state of the composite system is a single superposition of elements consisting of a state of the given set and its relative state in the other subsystem. (The relative states, however, are not necessarily orthogonal.) We notice further that a particular element, \(\gamma_{\mathrm{rel}}^{\mathrm{e}_{j}}\Theta_{j}\) , is quite independent of the choice of basis \(\{\phi_{j}, k \neq j\}\) , for the orthogonal space of \(\Theta_{j}\) , since \(\gamma_{\mathrm{rel}}^{\mathrm{e}_{j}}\) depends only on \(\Theta_{j}\) and not on the other \(\Theta_{k}\) for \(k \neq j\) . We remark at this point that the ambiguity in the relative state which arises when \(\sum_{j} \left(\phi_{j} \phi_{j} \psi^{\mathrm{s}}\right) \phi_{j} = 0\) (see 36 ftn.1) is unimportant for this representation, since although any state \(\gamma_{\mathrm{rel}}^{\mathrm{e}_{j}}\) can be regarded as the relative state in this case, the term \(\gamma_{\mathrm{rel}}^{\mathrm{e}_{j}} \Theta_{j}\) will occur in (1.13) with coefficient zero.  

Now that we have found subsystem states which correctly give conditional expectations, we might inquire as to whether there exist

---

subsystem states which give marginal expectations. The answer is, unfortunately, no. Let us compute the marginal expectation of A in \(S_1\) using the representation (1.13): 

\[
\begin{align*}
(1.14) \quad \text{Exp} [A] &= \langle A | \mathcal{V} \rangle = \left( \sum_j \frac{1}{N_j} \mathcal{V}_{rel}^o \Theta_j A \right)^2 \sum_k \frac{1}{N_k} \mathcal{V}_{rel}^o \Theta_k \right) \\
&= \sum_{jk} \frac{1}{N_k} \left( \mathcal{V}_{rel}^o A \mathcal{V}_{rel}^o \right) S_{jk} \\
&= \sum_j \frac{1}{N_j} \left( \mathcal{V}_{rel}^o A \mathcal{V}_{rel}^o A \right) = \sum_j P_j \langle A \rangle \mathcal{V}_{rel}^o
\end{align*}
\]

Now suppose that there exists a state in \(S_1, \mathcal{V}'\), which correctly
gives the marginal expectation (1.14) for all operators A (i.e.
such that \(\text{Exp} [A] = \langle A \rangle \mathcal{V}'\) for all A). One such operator is \([\mathcal{V}]\), the
projection on \(\mathcal{V}'\), for which \(\langle [\mathcal{V}] \rangle_{rel} = 1\). But, from (1.14) we have
that \(\text{Exp} [[\mathcal{V}]] = \sum_j P_j \langle \mathcal{V} \rangle \mathcal{V}_{rel}^o\), which is 4l unless for all j \(P_j = 0\)
or \(\mathcal{V}_{rel}^o \mathcal{V}'\), a condition which is not generally true. Therefore there
exists in general no state for \(S_1\) which correctly gives the marginal
expectations for all operators in \(S_1\). 

However, even though there is generally no single state describing
marginal expectations, we cannot see that there is always a mixture of
states, namely the states \(\mathcal{V}_{rel}^o\) weighted with \(P_j\), which does yield
the correct expectations. The distinction between a mixture, \(M\), of
states \(\phi\), weighted by \(P_1\), and a pure state \(\mathcal{V}\) which is a superposition,
\(\mathcal{V} = \sum a_i \phi_i\), is that there are no interference phenomena between the
various states of a mixture. The expectation of an operator A for the
mixture is \(\text{Exp}^M[A] = \sum P_i \langle A \rangle \phi_i = \sum P_i \langle \phi_i A \phi_i \rangle\), while the expectation
for the pure state \(\mathcal{V}\) is \(\langle A \rangle \mathcal{V} = \langle \mathcal{V} a_i \phi_i A \mathcal{V} a_i \phi_i \rangle = \sum a_i \langle \phi_i A \phi_i \rangle\), which is
not the same as that of the mixture with weights \(P_i a_i a_i\), due to the

---

presence of the interference terms \((\rho ,A\rho)\) for \(j \neq i\) . 

It is convenient to represent such a mixture by a density matrix \(\rho\). If the mixture consists of the states \(\psi_j\) weighted by \(P_j\), and if we are working in a basis consisting of the complete orthonormal set \(\{\phi_i\}\), where \(\psi_j = \sum_j a_j \phi_i\), then we define the elements of the density matrix for the mixture to be: 

\[ (1.15) \quad \rho_{kl} = \sum_j P_j a_j^* a_k^* \quad (a_j = (\phi_j, \psi_j)) \]

Then if \(A\) is any operator, with matrix representation \(A_{11} = (\phi, A\phi)\) in the chosen basis, its expectation for the mixture is: 

\[ (1.16) \quad \text{Exp}^M[A] = \sum_j P_j (\psi_j, A\psi_j) = \sum_j P_j \left[ \sum_i a_i^* a_i (\phi_i, A\phi_i) \right] \\ = \sum_{i,j} \left( \sum_j P_j a_i^* a_j \right) (\phi_i, A\phi_i) = \sum_{i,j} f_{ij} A_{ij} \\ = \text{Trace} (\rho A) \]

Therefore any mixture is adequately represented by a density matrix.
Note also that \(\rho_{kl} = \rho_{lk}\), so that \(\rho\) is Hermitian. 

Let us now find the density matrices \(\rho^A\) and \(\rho^2\) for the subsystems \(S_1\) and \(S_2\) of a system \(S = S_1 + S_2\) in the state \(\psi^A\). Furthermore, let us choose the orthonormal bases \(\{\xi_i\}\) and \(\{\eta_j\}\) in \(S_1\) and \(S_2\) respectively, and let \(A\) be an operator in \(S_1\), \(B\) an operator in \(S_2\). Then: 

\[ (1.17) \quad \text{Exp}[A] = \langle A \rangle \psi^S = \left( \sum_{ij} (\xi_i \eta_j, \psi^S) (\xi_j \eta_i, A \sum_{k,m} (\xi_k \eta_m, \psi^S) (\xi_m \eta_k, A \xi_k) (\eta_i, \eta_m) \right) \\ = \sum_{ij} (\xi_i \eta_j, \psi^S)^* (\xi_j \eta_i, \psi^S) (\xi_k \eta_k, \psi^S) (\xi_k, A \xi_k) \\ = \text{Trace} (\rho^A) \]

---

1 Also called a statistical operator (von Neumann [17]).  

2A better, coordinate free representation of a mixture is in terms of the operator which the density matrix represents. For a mixture of states \(\psi_{m}\) (not necessarily orthogonal) with weights \(\rho_{m}\) , the density operator is \(\rho = \sum_{m} \rho_{m} [\psi_{m}]\) , where \([\psi_{m}]\) stands for the projection operator on \(\psi_{m}\) .

---

where we have defined \(\rho^{1}\) in the \(\{\bar{\xi}\}\) basis to be:  

\[\rho_{\lambda i}^{1} = \sum_{i}\left(\{\xi_{i}\eta_{i}\nu^{2}\right)^{*}\left(\xi_{i}\eta_{i}\nu^{s}\right) \quad (1.18)\]  

In a similar fashion we find that \(\rho^{2}\) is given, in the \(\{\bar{\eta}_{i}\}\) basis, by:  

\[\rho_{m n}^{2} = \sum_{i}\left(\{\bar{\eta}_{m}\nu^{s}\right)^{*}\left(\bar{\xi}_{i}\eta_{m}\nu^{s}\right) \quad (1.19)\]  

It can be easily shown that here again the dependence of \(\rho^{1}\) upon the choice of basis \(\{\bar{\eta}_{i}\}\) in \(S_{2}\) , and of \(\rho^{2}\) upon \(\{\bar{\xi}_{i}\}\) , is only apparent.  

In summary, we have seen in this section that a state of a composite system leads to joint distributions over subsystem quantities which are generally not independent. Conditional distributions and expectations for subsystems are obtained from relative states, and subsystem marginal distributions and expectations are given by density matrices.  

There does not, in general, exist anything like a single state for one subsystem of a composite system. That is, subsystems do not possess states independent of the states of the remainder of the system, so that the subsystem states are generally correlated. One can arbitrarily choose a state for one subsystem, and be led to the relative states for the other subsystem. Thus we are faced with a fundamental relativity of states, which is implied by the formalism of composite systems. It is meaningless to ask the absolute state of a subsystem - - one can only ask the state relative to a given state of the remainder of the system.

---

## §2. Information and Correlation in Quantum Mechanics  

We wish to be able to discuss information and correlation for Hermitian operators A, B, ..., with respect to a state function \(\mathcal{V}\) . These quantities are to be computed, through the formulas of the preceeding chapter, from the square amplitudes of the coefficients of the expansion of \(\mathcal{V}\) in terms of the eigenstates of the operators.  

We have already seen \((\rho_{33})\) that a state \(\mathcal{V}\) and an orthonormal basis \(\{\phi_{i}\}\) leads to a square amplitude distribution of \(\mathcal{V}\) over the set \(\{\phi_{i}\}\) :  

\[P_{i} = |(\phi_{i}, \psi)|^{2} = \langle [\phi_{i}] \rangle \mathcal{V} \quad (2.1)\]  

so that we can define the information of the basis \(\{\phi_{i}\}\) for the state \(\mathcal{V}\) , \(I_{\{\phi_{i}\}}(\mathcal{V})\) , to be simply the information of this distribution relative to the uniform measure:  

\[I_{\{\phi_{i}\}}(\mathcal{V}) = \sum_{i} p_{i} \ln p_{i} = \sum_{i} |(\phi_{i}, \psi)|^{2} \ln |(\phi_{i}, \psi)|^{2} \quad (2.2)\]  

We define the information of an operator A, for the state \(\mathcal{V}\) , \(I_{A}(\mathcal{V})\) , to be the information in the square amplitude distribution over its eigenvalues, i.e. the information of the probability distribution over the results of a determination of A which is prescribed in the probabilistic interpretation. For a non- degenerate operator A this distribution is the same as the distribution (2.1) over the eigenstates. But because the information is dependent only on the distribution, and not on numerical values, the information of the distribution over eigenvalues of A is precisely the information of the eigenbasis of A, \(\{\phi_{i}\}\) . Therefore:

---

\[I_{A}(\mathcal{V}) = I_{[a]}(\mathcal{V}) = \sum_{i}\langle [a]\rangle \mathcal{V} = \sum_{i}\langle [a]\rangle \mathcal{V} = \sum_{j}\langle [a]\rangle \mathcal{V} \quad (A_{m a - d e g n})\]  

We see that for fixed \(\mathcal{V}\) , the information of all non- degenerate operators having the same set of eigenstates is the same.  

In the case of degenerate operators it will be convenient to take, as the definition of information, the information of the square amplitude distribution over the eigenvalues relative to the information measure which consists of the multiplicity of the eigenvalues, rather than the uniform measure. This definition preserves the choice of uniform measure over the eigenstates, in distinction to the eigenvalues. If \(\hat{\rho}_{ij}\) (j from 1 to \(m_j\) ) are a complete orthonormal set of eigenstates for \(A^*\) , with distinct eigenvalues \(\lambda_i\) (degenerate with respect to \(j\) ), then the multiplicity of the \(i\) th eigenvalue is \(m_i\) and the information \(I_{A^*}(\mathcal{V})\) is defined to be:  

\[I_{A^*}(\mathcal{V}) = \sum_{i}\left(\sum_{j}\langle [a_j]\rangle \mathcal{V}\right) \ln \frac{\sum_{j}\langle [a_j]\rangle \mathcal{V}}{m_i} \quad (2.4)\]  

The usefulness of this definition lies in the fact that any operator \(A^*\) which distinguishes further between any of the degenerate states of \(A^*\) leads to a refinement of the relative density, in the sense of theorem 4, and consequently has equal or greater information. A non- degenerate operator thus represents the maximal refinement and possesses maximal information.  

It is convenient to introduce a new notation for the projection operators which are relevant for a specified operator. As before let \(A\) have eigenfunctions \(\hat{\rho}_{ij}\) and distinct eigenvalues \(\lambda_i\) . Then define the projections \(A_i\) , the projections on the eigenspaces of

---

different eigenvalues of A, to be:  

\[A_{1} = \sum_{i = 1}^{m_{1}}\left[\mathcal{A}_{i}\right] \quad (2.5)\]  

To each such projection there is associated a number \(m_{1}\) , the multiplicity of the degeneracy, which is the dimension of the \(i\) th eigenspace. In this notation the distribution over the eigenvalues of A for the state \(\mathcal{V}\) , \(P_{1}\) , becomes simply:  

\[P_{1} = P(\lambda_{1}) = \langle \lambda_{1}\rangle \mathcal{V} \quad (2.6)\]  

and the information, given by (2.4), becomes:  

\[I_{A} = \sum_{4}\langle \lambda_{1}\rangle \mathcal{V}\ln \frac{\langle\lambda_{1}\rangle\mathcal{V}}{B_{1}} \quad (2.7)\]  

Similarly, for a pair of operators, A in \(S_{1}\) and B in \(S_{2}\) , for the composite system \(S = S_{1} + S_{2}\) with state \(\mathcal{V}^{s}\) , the joint distribution over eigenvalues is:  

\[P_{i j} = P(\lambda_{1},\mathcal{N}_{j}) = \langle \lambda_{1}B_{j}\rangle \mathcal{V}^{s} \quad (2.8)\]  

and the marginal distributions are:  

\[P_{1} = \sum_{i}P_{1j} = \langle \lambda_{1}(\sum_{i}B_{j})\rangle \mathcal{V}^{s} = \langle \lambda_{1}I^{2}\rangle \mathcal{V}^{s\] \[P_{j} = \sum_{i}P_{1j} = \langle (\sum_{i}A_{1})B_{j}\rangle \mathcal{V}^{s} = \langle I^{1}B_{j}\rangle \mathcal{V}^{s\]  

The joint information, \(I_{AB}\) , is given by:  

\[I_{AB} = \sum_{i,j}P_{1j}\ln \frac{P_{1i}}{m_{1j}} = \sum_{i,j}\langle \lambda_{1}B_{j}\rangle \mathcal{V}^{s}\ln \frac{\langle\lambda_{1}B_{j}\rangle\mathcal{V}^{s}}{m_{1j}} \quad (2.10)\]  

where \(m_{1}\) and \(n_{j}\) are the multiplicities of the eigenvalues \(\lambda_{1}\) and \(\mathcal{N}_{j}\) .

---

The marginal information quantities are given by :  

\[I_{\mathrm{A}} = \sum_{i}\langle A_{i}I^{2}\rangle \gamma^{s}\ln \frac{\langle A_{i}I^{2}\rangle^{\gamma^{s}}}{n_{j}}\] \[I_{\mathrm{B}} = \sum_{j}\langle I^{1}B_{j}\rangle \gamma^{s}\ln \frac{\langle I^{1}B_{j}\rangle^{\gamma^{s}}}{n_{j}}\]  

and finally the correlation, \(\{A,B\}^{\gamma^{s}}\) is given by:  

\[\{A,B\}^{\gamma^{s}} = \sum_{i,j}P_{i,j}\ln \frac{P_{i,j}}{E_{i,j}^{2}} = \sum_{i,j}\langle A_{i}B_{j}\rangle^{\gamma^{s}}\ln \frac{\langle A_{i}B_{j}\rangle^{\gamma^{s}}}{\langle A_{i}\rangle^{\gamma^{s}}\langle B_{j}\rangle^{\gamma^{s}}} \quad (2.12)\]  

where we note that the expression does not involve the multiplicities, as do the information expressions, a circumstance which simply reflects the independence of correlation on any information measure. These expressions of course generalize trivially to distributions over more than two variables (composite systems of more than two subsystems).  

In addition to the correlation of pairs of subsystem operators, given by (2.12), there always exists a unique quantity \(\{S_{1},S_{2}\}\) , the canonical correlation, which has some special properties and may be regarded as the fundamental correlation between the two subsystems \(S_{1}\) and \(S_{2}\) of the composite system \(S\) . As we remarked earlier a density matrix is Hermitian, so that there is a representation in which it is diagonal. In particular, for the decomposition of \(S\) (with state \(\gamma^{s}\) ) into \(S_{1}\) and \(S_{2}\) , we can choose a representation in which both \(f^{s}\) and \(f^{s}\) are diagonal. (This choice is always possible because \(f^{s}\) is independent of the basis in \(S_{2}\) and vice-versa.) Such a representation will be called a canonical representation. This means that it is always possible to represent the state \(\gamma^{s}\) by a single superposition.

---

1 The density matrix of a subsystem always has a pure discrete spectrum, if the composite system is in a state. To see this we note that the choice of any orthonormal basis in \(S_{2}\) leads to a discrete (i.e., denumerable) set of relative states in \(S_{1}\) . The density matrix in \(S_{1}\) then represents this discrete mixture, \(\frac{V_{j}^{0}}{V_{j}^{0}}\) weighted by \(P_{j}\) . This means that the expectation of the identity, \(\mathrm{Exp}[I] = \sum_{j} \frac{V_{j}^{0}}{V_{j}^{0}} (\frac{V_{j}^{0}}{V_{j}^{0}}, I \frac{V_{j}^{0}}{V_{j}^{0}}) = \sum_{j} P_{j}\) \(= 1 = \mathrm{Trace}(I) = \mathrm{Trace}(f)\) . Therefore \(f\) has a finite trace and is a completely continuous operator, having necessarily a pure discrete spectrum. (See von Neumann [V], pg.89, footnote 115. )

---

\[V^{\mathrm{s}} = \sum_{i} a_{i} f_{i} n_{i}\]  

where both the \(\{\mathbf{f}_{i}\}\) and the \(\{\mathbf{n}_{i}\}\) constitute orthonormal sets of states for \(S_{1}\) and \(S_{2}\) respectively.  

To construct such a representation choose the basis \(\{\mathbf{n}_{i}\}\) for \(S_{2}\) so that \(\mathcal{P}_{i}^{s_{2}}\) is diagonal:  

\[\mathcal{P}_{i j}^{s_{2}} = \lambda_{i} \mathcal{S}_{i j} \quad (2.14)\]  

and let the \(\mathbf{f}_{i}\) be the relative states in \(S_{1}\) for the \(\mathcal{N}_{i}\) in \(S_{2}\) :  

\[\hat{\mathbf{f}}_{i} = \mathbf{N}_{i} \sum_{j} (\phi_{j} \mathbf{n}_{i} \psi^{-j}) \phi_{j} \quad (any basis \{\phi_{j}\}) \quad (2.15)\]  

Then, according to (1.13), \(\psi^{- s_{2}}\) is represented in the form (2.13) where the \(\{\mathbf{n}_{i}\}\) are orthonormal by choice, and the \(\{\mathbf{f}_{i}\}\) are normal since they are relative states. We therefore need only show that the states \(\{\mathbf{f}_{i}\}\) are orthogonal:  

\[\begin{array}{r l r}{{(\xi_{j},\xi_{k})~=~(\mathbf{N}_{j}\sum_{i}(\xi_{j}\mathbf{n}_{i},\psi^{-s})\phi_{j},\mathbf{N}_{k}\sum_{i}(\phi_{j}\mathbf{n}_{i},\psi^{-s})\phi_{m})}}\\ &{}&{=\sum_{i m}\mathbf{N}_{j}^{s_{2}}\mathbf{N}_{k}(\phi_{j}\mathbf{n}_{i},\psi^{-s})(\phi_{m}\mathbf{n}_{i},\psi^{-s})\xi_{i m}=\mathbf{N}_{j}^{s_{2}}\mathbf{N}_{k}\sum_{i}(\phi_{j}\mathbf{n}_{i},\psi^{s})(\phi_{m}\mathbf{n}_{i},\psi^{s})}\\ &{}&{=\mathbf{N}_{j}^{s_{2}}\mathbf{N}_{k}\int_{k j}^{s_{2}}=\mathbf{N}_{j}^{s_{2}}\mathbf{N}_{k}\lambda_{k}\xi_{k j}=\mathbf{O}\mathrm{~for~}j\neq k}\end{array} \quad (2.16)\]  

since we supposed \(\mathcal{P}_{i}^{s_{2}}\) to be diagonal in this representation. We have therefore constructed a canonical representation (2.13).  

The density matrix \(\mathcal{P}_{i}^{s_{2}}\) is also automatically diagonal, by the choice of representation consisting of the basis in \(S_{2}\) which makes \(\mathcal{P}_{i}^{s_{2}}\) diagonal and the corresponding relative states in \(S_{1}\) . Since \(\{\mathbf{f}_{i}\}\) are orthonormal we have:

---

\[{\begin{array}{r l}{\mathcal{F}_{i i}^{s_{2}}=\sum_{k}(\xi_{i k},\psi^{s})(\xi_{i k},\psi^{s})=\sum_{k}(\xi_{i k}\sum_{l}\alpha_{i k l}\eta_{l})(\xi_{i k}\sum_{l}\xi_{i k}\eta_{l})}\\ {=\sum_{k i k}\alpha_{i k}\xi_{i k}\xi_{i k}\xi_{i k}=\sum_{k}\alpha_{i k}\xi_{i k}\xi_{i k}}\\ {=\alpha_{i k}\xi_{i j}=\mathcal{P}_{i}\xi_{i j}}\end{array}} \quad (2.17)\]  

where \(P_{i} = \alpha_{i} \alpha_{i}\) is the marginal distribution over the \(\{\xi_{i}\}\) . Similar computation shows that the elements of \(\mathcal{F}^{s_{2}}\) are the same:  

\[\mathcal{F}_{\mathbf{k}\mathbf{l}}^{s_{2}} = \alpha_{\mathbf{k}\mathbf{k}}^{s_{2}}\xi_{\mathbf{k}\mathbf{l}} = \mathcal{P}_{\mathbf{k}}\xi_{\mathbf{k}\mathbf{l}} \quad (2.18)\]  

Thus in the canonical representation both density matrices are diagonal and have the same elements, \(P_{k}\) , which give the marginal square amplitude distribution over both of the sets \(\{\xi_{i}\}\) and \(\{\mathcal{M}_{i}\}\) forming the basis of the representation.  

Now, any pair of operators, \(\hat{\mathcal{A}}\) in \(s_{1}\) and \(\hat{\mathcal{B}}\) in \(s_{2}\) , which have as non- degenerate eigenfunctions the sets \(\{\xi_{i}\}\) and \(\{\mathcal{M}_{i}\}\) (i.e. operators which define the canonical representation), are "perfectly" correlated in the sense that there is a one- one correspondence between their eigenvalues. The joint square amplitude distribution for eigenvalues \(\lambda_{i}\) of \(\hat{\mathcal{A}}\) and \(\mathcal{M}_{i}\) of \(\hat{\mathcal{B}}\) is:  

\[P(\lambda_{1} \text{ and } \mathcal{M}_{j}) = P(\{\xi_{1} \text{ and } \mathcal{M}_{j}\} = P_{1j} = \alpha_{1} \xi_{1j} = P_{1} \xi_{1j} \quad (2.19)\]  

Therefore, the correlation between these operators, \(\{\hat{\mathcal{A}}, \hat{\mathcal{B}}\}^{\mathcal{V}^{s}}\) is:  

\[\begin{array}{r l r}{{\{\hat{\mathcal{A}},\hat{\mathcal{B}}\}^{\mathcal{V}^{s}}=\sum_{i,j}P(\lambda_{1}\mathrm{~and~}\mathcal{M}_{j})\ln\frac{P(\lambda_{1}\mathrm{~and~}\mathcal{M}_{j})}{P(\lambda_{1})P(\mathcal{M}_{j})}=\sum_{i,j}P_{1}\xi_{1j}\ln\frac{P_{1}\xi_{1j}}{P_{1}P_{j}}}}\\ &{}&{=-\sum_{i}P_{1}\ln P_{1}}\end{array} \quad (2.20)\]  

We shall denote this quantity by \(\{\xi_{1}, \xi_{2}\}^{\mathcal{V}^{s}}\) and call it the  

canonical correlation of the subsystems \(s_{1}\) and \(s_{2}\) for the system state \(\mathcal{P}^{s}\) .

---

It is the correlation between any pair of non- degenerate subsystem operators which define the canonical representation.  

In the canonical representation, where the density matrices are diagonal ((2.17)and(2.18)), the canonical correlation is given by:  

\[\{S_{1},S_{2}\}^{\psi^{s}} = -\sum_{i}^{r}P_{i}\ln P_{i}^{s} - \mathrm{trace}(f^{s}\ln f^{s}) = -\mathrm{trace}(f^{s}\ln f^{s}) \quad (2.21)\]  

But the trace is invariant for unitary transformations, so that (2.21) holds independently of the representation, and we have therefore established the uniqueness of \(\{S_{1},S_{2}\}^{\psi^{s}}\) .  

It is also interesting to note that the quantity - Trace(flnf) is (apart from a factor of Boltzmann's constant) just the entropy of a mixture of states characterized by the density matrix \(f\) . Therefore the entropy of the mixture characteristic of a subsystem \(S_{1}\) for the state \(\psi^{s} = \psi^{s_{1}s_{2}}\) is exactly matched by a correlation information \(\{S_{1},S_{2}\}\) , which represents the correlation between any pair of operators \(\hat{A}\) , \(\hat{B}\) , which define the canonical representation. The situation is thus quite similar to that of classical mechanics.  

Another special property of the canonical representation is that any operators \(\hat{A}\) , \(\hat{B}\) defining a canonical representation have maximum marginal information, in the sense that for any other discrete spectrum operators, A on \(S_{1}\) , B on \(S_{2}\) , \(I_{A} \in I_{A}\) and \(I_{B} \in I_{B}\) . If the canonical representation is (2.13), with \(\{f_{i}^{s}, \{N_{i}^{s}\} \}\) non- degenerate eigenfunctions of \(\hat{A}\) , \(\hat{B}\) , respectively, and \(A\) , \(B\) any pair of non- degenerate operators with eigenfunctions \(\{\phi_{k}\}\) and \(\{\Theta_{i}\}\) , where \(f_{i} = \sum_{k} c_{i k} \phi_{k}\) , \(N_{i} = \sum_{k} d_{i i} \Theta_{i}\) , then \(\psi^{s} \ln \phi_{j} \in\) representation is: (2.22)  

\[\psi^{s} = \sum_{i k a} a_{i} a_{i k} \Theta_{i} \Theta_{k} \Theta_{i} = \sum_{i k a} \left(\sum_{k} a_{i} a_{i k} \Theta_{i}\right) \phi_{k} \Theta_{i} \Theta_{i} \Theta_{i} \Theta_{i} \Theta_{k} \Theta_{i} \Theta_{i} \Theta_{i} \theta_{i} \Theta_{i} \Theta_{i} \Theta_{i} \theta_{k} \Theta_{i} \Theta_{i} \Theta_{i} \phi_{k} \Theta_{i} \Theta_{i} \Theta_{i}\]

---

1 See von Neumann [17], pg. 2 Cf. Chap. II, 7.

---

and the joint square amplitude distribution for \(A, \Theta_{\alpha}\) is: 

\[(2.23) \quad P_{kl} = |(\sum_{i} a_{i1} c_{ik} d_{il})|^2 = \sum_{lm} a_{i1} a_{i1} c_{ik} c_{ik} d_{il} d_{il}\]

while the marginals are: 

\[(2.24) \quad P_k = \sum_l P_{kl} = \sum_{lm} a_{i1} a_{i1} c_{ik c_{ik}} \sum_l d_{il} d_{il} \\
= \sum_{lm} a_{i1} a_{i1} c_{ik} \delta_{lm} = \sum_l a_{i1} a_{i1} c_{ik} c_{ik}\]

and similarly 

\[(2.25) \quad P_1 = \sum_k P_{k1} = \sum_i a_{i1} d_{i1} d_{i1}\]

Then the marginal information \(I_{A}\) is: 

\[(2.26) \quad I_A = \sum_k P_{k1} \ln P_k = \sum_k \left( \sum_i a_{i1} c_{ik} c_{ik} \right) \ln \left( \sum_i a_{i1} c_{ik} c_{ik} c_{ik} \right) \\
= \sum_k \left( \sum_i a_{i1} a_{i1} c_{ik} \right) \ln \left( \sum_i a_{i2} a_{i2} c_{ik} \right)\]

where \(T_{ik} = c_{ik} c_{ik}\) is doubly-stochastic (\(\sum_i T_{ik} = \sum_i T_{ik} = 1\) follows from unitary nature of the \(c_{ik}\)). Therefore (by corollary 2.9, App. A): 

\[(2.27) \quad I_A = \sum_k \left( \sum_i a_{i1} a_{i1} \right) \ln \left( \sum_i a_{i1} a_{i1} c_{ik}\right) \\
\leq \sum_i a_{i1} a_{i1} \ln a_{i1} = I_A\]

and we have proved that \(X\) has maximal marginal information among the discrete spectrum operators. Identical proof holds for \(B\). 

While this result was proved only for non-degenerate operators, it is immediately extended to the degenerate case, since as a consequence of our definition of information for a degenerate operator, (2.4), its information is still less than that of an operator which

---

removes the degeneracy. We have thus proved: 

Theorem: \(I_A \triangleq I_X\) 

where \(X\) is any non-degenerate operator defining the canonical representation, and \(A\) is any operator with discrete spectrum. 

We conclude the discussion of the canonical representation by conjecturing that in addition to the maximum marginal information properties of \(X, \bar{B},\) which define the representation, they are also maximally correlated, by which we mean that for any pair of operators \(C\) in \(S_1, D\) in \(S_2, \{C, D\} \triangleq \{A, B\}\) i.e.: (2.28) Conjecture: \(\{C, D\}^{S_1} \triangleq \{A, B\}^{S_1} \triangleq \{S_1, S_2\}^{S_1}\) for all \(C\) on \(S_1, D\) on \(S_2\). 

As a final topic for this section we point out that the uncertainty principle can probably be phrased in a stronger form in terms of information. The usual form of this principle is stated in terms of variance, namely: 

\[ (2.29) \qquad \nabla_x^2 \nabla_k^2 \geq \frac{1}{4} \qquad \text{for all } \mathcal{V}(x) \\ \text{where } \nabla_x^2 = \langle x^2 \rangle \mathcal{V} - \langle x \rangle \mathcal{V} \rangle^2 \text{ and } \\ \nabla_k^2 = \langle (-i \frac{\partial}{\partial x})^2 \rangle \mathcal{V} - \langle (-i \frac{\partial}{\partial x}) \mathcal{V} \rangle^2 = \langle (\frac{\mathcal{P}_k}{\mathcal{V}}) \rangle \mathcal{V} - \langle (\frac{\mathcal{P}_k}{\mathcal{V}}) \rangle^2 \]

The conjectured information form of this principle is: 

\[ (2.30) \qquad I_x + I_k \triangleq \ln (1/\eta e) \qquad \text{for all } \mathcal{V}(x) \]

Although this inequality has not yet been proved with complete rigor, it is made highly probable by the circumstance that equality

---

1 The relations \(\{\overline{C},\overline{B}\} \in \{\overline{A},\overline{B}\} = \{\overline{S}_1,S_2\}\) and \(\{\overline{A},\overline{D}\} \in \{\overline{S}_1,S_2\}\) for all C on \(S_1\) , D on \(S_2\) , can be proved easily in a manner analogous to (2.27). These do not, however, necessarily imply the general relation (2.28).

---

holds for \(\psi (x)\) of the form \(\psi (x) = (1 / 2\pi)^2\) exponent \(\left[\frac{x^2}{4\sqrt{x}}\right]\) the so called "minimum uncertainty packets" which give normal distributions for both position and momentum, and that furthermore the first variation of \((I_x + I_k)\) vanishes for such \(\psi (x)\) . (see App.56). Thus, although \(\ln (1 / \pi e)\) has not been proved an absolute maximum of \(I_x + I_k\) , it is at least a stationary value.  

The principle (2.30) is stronger than (2.29), since it implies (2.29) but is not implied by it. To see that it implies (2.29) we use the well known fact (easily established by a variation calculation, that, for fixed variance \(\nabla^2\) , the distribution of minimum information is a normal distribution, which has information \(I = \ln (1 / \nabla^2 \sqrt{2 \pi e})\) . This gives us the general inequality involving information and variance:  

(2.31) \(I \geq \ln (1 / \nabla^2 \sqrt{2 \pi e})\) (for all distributions)  

Substitution of (2.31) into (2.30) then yields:  

\[{\ln(1/\nabla_{x}^{2}\sqrt{2\pi e})+\ln(1/\nabla_{x}^{2}\sqrt{2\pi e})\leq I_{x}+I_{k}\leq\ln(1/\pi e)}\] \[\Rightarrow(1/\nabla_{x}\nabla_{k}^{2}\pi e)\leq(1/\pi e)\Rightarrow\nabla_{x}^{2}\nabla_{k}^{2}\geq\frac{1}{4}\]  

So that our principle implies the standard principle (2.29).  

To show that (2.29) does not imply (2.30) it suffices to give a counter- example. The distributions \(P(x) = \frac{1}{2} \delta (x) + \frac{1}{2} \delta (x - 10)\) and \(P(k) = \frac{1}{2} \delta (k) + \frac{1}{2} \delta (k - 10)\) , which consist simply of spikes at 0 and 10, clearly satisfy (2.29), while they both have infinite information and thus do not satisfy (2.30). Therefore it is possible to have arbitrarily high information about both \(x\) and \(k\) (or \(p\) ) and still

---

satisfy (2.13). We have, then, another illustration that information concepts are more powerful and more natural than the older measures based upon variance.

---

## 5. Measurement  

We now consider the question of measurement in quantum mechanics, which we desire to treat as a natural process within the theory of pure wave mechanics. From our point of view there is no fundamental distinction between "measuring apparatus" and other physical systems. For us, therefore, a measurement is simply a special case of interaction between physical systems - - an interaction which has the property of correlating a quantity in one subsystem with a quantity in another.  

Nearly every interaction between systems produces some correlation however. Suppose that at some instant a pair of systems are independent, so that the composite system state function is a product of subsystem states ( \(\gamma^{5} = \gamma^{1}\gamma^{5}\) ). Then this condition obviously holds only instantaneously if the systems are interacting - - the independence is immediately destroyed and the systems become correlated. We could, then, take the position that the two interacting systems are continually "measuring" one another, if we wished. At each instant t we could put the composite system into canonical representation, and choose a pair of operators \(\hat{A} (t)\) in \(S_{1}\) and \(\hat{B} (t)\) in \(S_{2}\) which define this representation. We might then reasonably assert that the quantity \(\hat{A}\) in \(S_{1}\) is measured by \(\hat{B}\) in \(S_{2}\) (or vice- versa), since there is a one- one correspondence between their values.  

Such a viewpoint, however, does not correspond closely with our intuitive idea of what constitutes "measurement", since the quantities \(\hat{A}\) and \(\hat{B}\) which turn out to be measured depend not only

---

1 If \(\mathbf{u}_t^S\) is the unitary operator generating the time dependence for the state function of the composite system \(\mathbf{S} = \mathbf{S}_1 + \mathbf{S}_2\) , so that \(\mathbf{y}_t^S = \mathbf{u}_t^S \mathbf{y}_0^S\) , then we shall say that \(\mathbf{S}_1\) and \(\mathbf{S}_2\) have not interacted during the time interval \([0, t]\) if and only if \(\mathbf{u}_t^S\) is the direct product of two subsystem unitary operators, i.e., if \(\mathbf{u}_t^S = \mathbf{u}_t^{S_1} \otimes \mathbf{u}_t^{S_2}\) .

---

on the time, but also upon the initial state of the composite system. A more reasonable position is to associate the term "measurement" with a fixed interaction H between systems \(\tilde{\mathcal{A}}\) , and to define the "measured quantities" not as those quantities \(\tilde{\mathcal{A}} (t)\) , \(\tilde{\mathcal{B}} (t)\) which are instantaneously canonically correlated, but as the limit of the instantaneous canonical operators as the time goes to infinity, \(\tilde{\mathcal{A}}_{\infty}\) , \(\tilde{\mathcal{B}}_{\infty}\) - - provided that this limit exists and is independent of the initial state. In such a case we are able to associate the "measured quantities", \(\tilde{\mathcal{A}}_{\infty}\) , \(\tilde{\mathcal{B}}_{\infty}\) , with the interaction H independently of the actual system states and the time. We can therefore say that H is an interaction which causes the quantity \(\tilde{\mathcal{A}}_{\infty}\) in \(S_{1}\) to be measured by \(\tilde{\mathcal{B}}_{\infty}\) in \(S_{2}\) . For finite times of interaction the measurement is only approximate, approaching exactness as the time of interaction increases indefinitely.  

There is still one more requirement that we must impose on an interaction before we shall call it a measurement. If H is to produce a measurement of A in \(S_{1}\) by B in \(S_{2}\) , then we require that H shall never decrease the information in the marginal distribution of A. If H is to produce a measurement of A by correlating it with B, we expect that a knowledge of B shall give us more information about A than we had before the measurement took place, since otherwise the measurement would be useless. How, H might produce a correlation between A and B by simply destroying the marginal information of A, without improving the expected conditional information of A given B, so that a knowledge of B

---

1 Here H means the total Hamiltonian of S, not just an interaction part.  

2 Actually, rather than referring to canonical operators \(\hat{\Lambda}\) , \(\hat{\mathcal{B}}\) , which are not unique, we should refer to the bases of the canonical representation, \(\{\hat{\mathbf{\Gamma}}_{i}\}\) in \(S_{1}\) and \(\{\hat{\mathcal{N}}_{j}\}\) in \(S_{2}\) , since any operators \(\hat{\mathcal{T}} = \sum_{i} \hat{\Lambda}_{i} \hat{\mathcal{N}}_{i}\) , with the completely arbitrary eigenvalues \(\hat{\Lambda}_{i}\) , \(\hat{\mathcal{N}}_{j}\) , are canonical. The limit then refers to the limit of the canonical bases, if it exists in some appropriate sense. However, we shall, for convenience, continue to represent the canonical bases by operators.

---

would give us no more information about A than we possessed originally. Therefore in order to be sure that we will gain information about A by knowing B, when B has become correlated with A, it is necessary that the marginal information about A has not decreased. The expected information gain in this case is assured to be not less than the correlation \(\{A, B\}\) .  

The restriction that H shall not decrease the marginal information of A has the interesting consequence that the eigenstates of A will not be disturbed, i.e. initial states of the form \(\psi_{0}^{s} = \phi N_{0}\) , where \(\phi\) is an eigenfunction of A, must be transformed after any time interval into states of the form \(\psi_{t}^{s} = \phi N_{t}\) , since otherwise the marginal information of A, which was initially perfect, would be decreased. This condition, in turn, is connected with the repeatability of measurements, as we shall subsequently see, and could alternately have been chosen as the condition for measurement.  

We shall therefore accept the following definition. An interaction H is a measurement of A in \(S_{1}\) by B in \(S_{2}\) if H does not destroy the marginal information of A (equivalently: if H does not disturb the eigenstates of A in the above sense) and if furthermore the correlation \(\{A, B\}\) increases toward its maximum with time.  

We now illustrate the production of correlation with an example of a simplified measurement due to Von Neumann \(^{2}\) . /Suppose that we have a system of only one coordinate, \(q\) , (such as position of a particle), and an apparatus of one coordinate \(r\) (for example

---

1 The maximum of {A,B} is - I_A if A has only a discrete spectrum, and ∞ if it has a continuous spectrum.  2 von Neumann [1], pg.442.

---

the position of a meter needle). Further suppose that they are initially independent, so that the combined wave function is \(\psi_{e}^{m A} = \phi (q) \mathcal{L}(r)\), where \(\phi (q)\) is the initial system wave function, and \(\mathcal{L}(r)\) is the initial apparatus function. Finally suppose that the masses are sufficiently large or the time of interaction sufficiently small that the kinetic portion of the energy may be neglected, so that during the time of measurement the Hamiltonian shall consist only of an interaction, which we shall take to be:  

\[\frac{(3,1)}{(3,1)} \qquad H_{1} = -i \hbar q \frac{\partial}{\partial r}\]  

Then it is easily verified that the state \(\psi_{\frac{1}{2}}^{S A}(q, r)\) :  

\[\psi_{\frac{1}{2}}^{S A}(q, r) = \phi (q) \mathcal{L}(r - q t)\]  

is a solution of the Schrödinger equation  

\[\mathrm{i}\hbar \frac{\partial \psi_{\frac{1}{2}}^{S A}}{\partial t} = \mathrm{H}_{1}\psi_{\frac{1}{2}}^{S A}\]  

for the specified initial conditions at time \(t = 0\) .  

Translating (3.2) into square amplitudes we get:  

\[\begin{array}{r l} & {\mathrm{P}_{\mathrm{t}}(q,r) = \mathrm{P}_{1}(q)\mathrm{P}_{2}(r - q t)}\\ & {\mathrm{where}\quad \mathrm{P}_{1}(q) = \phi_{\mathrm{e}}(q)\phi (q),\quad \mathrm{P}_{2}(r) = \mathcal{H}_{\mathrm{e}}(r)\mathcal{H}(r)}\\ & {\mathrm{and}\quad \mathrm{P}_{\mathrm{t}}(q,r) = \psi_{\mathrm{e}}^{S + A}(q,r)\psi_{\mathrm{e}}^{S + A}(q,r)} \end{array} \quad (3.4)\]  

and we note that for a fixed time, \(t\), the conditional square amplitude distribution for \(r\) has been translated by an amount depending upon the value of \(q\), while the marginal distribution for \(q\) has been unaltered. We see thus that a correlation has

---

been introduced between q and r by this interaction, which allows us to interpret it as a measurement. It is instructive to see quantitatively how fast this correlation takes place. We note that:  

\[\begin{array}{r l r}{{\mathrm{I}_{Q\mathrm{R}}(t)=\iint_{\mathrm{P}_{\mathrm{t}}(q,\mathrm{r})\mathrm{ln}\mathrm{P}_{\mathrm{t}}(q,\mathrm{r})\mathrm{d}\mathrm{q}\mathrm{d}\mathrm{r}}}\\ &{}&{=\iint_{\mathrm{P}_{\mathrm{l}}(q)\mathrm{P}_{\mathrm{2}}(\mathrm{r}\mathrm{-}\mathrm{q}\mathrm{t})\mathrm{ln}\mathrm{P}_{\mathrm{l}}(q)\mathrm{P}_{\mathrm{2}}(\mathrm{r}\mathrm{-\mathrm{q}\mathrm{t}})\mathrm{d}\mathrm{q}\mathrm{d}\mathrm{r}}}\\ &{}&{=\iints_{\mathrm{P}_{\mathrm{l}}(q)\mathrm{P}_{\mathrm{2}}(\omega)\mathrm{ln}\mathrm{P}_{\mathrm{l}}(q)\mathrm{P}_{\mathrm{2}}(\omega)\mathrm{d}\mathrm{q}\mathrm{d}\omega}}\\ &{}&{=\mathrm{I}_{Q\mathrm{R}}(0)}\end{array} \quad (3.5)\]  

so that the information of the joint distribution does not change. Furthermore, since the marginal distribution for q is unchanged:  

\[\mathrm{I}_{\mathrm{Q}}(t) = \mathrm{I}_{\mathrm{Q}}(0) \quad (3.6)\]  

and the only quantity which can change is the marginal information, \(\mathrm{I}_{\mathrm{R}}\) , of r, whose distribution is:  

\[\mathrm{P}_{\mathrm{t}}(r) = \int \mathrm{P}_{\mathrm{t}}(r,q)\mathrm{d}q = \int \mathrm{P}_{\mathrm{l}}(q)\mathrm{P}_{\mathrm{2}}(r - \mathrm{q}t)\mathrm{d}q \quad (3.7)\]  

Application of a special inequality (proved in §5, Appendix) to (3.7) yields the relation:  

\[\mathrm{I}_{\mathrm{R}}(t) \triangleq \mathrm{I}_{\mathrm{Q}}(0) - \ln t \quad (3.8)\]  

so that, except for the additive constant \(\mathrm{I}_{\mathrm{Q}}(0)\) , the marginal information \(\mathrm{I}_{\mathrm{R}}\) tends to decrease at least as fast as \(\ln t\) with time during the interaction. This implies the relation for the correlation:

---

\[{\{Q,R\}_{t}=\mathrm{I}_{Q R}(t)-\mathrm{I}_{Q}(t)-\mathrm{I}_{R}(t)\stackrel{\Delta}{=}\mathrm{I}_{R Q}(t)-\mathrm{I}_{Q}(t)=\mathrm{I}_{Q}(0)+\mathrm{I}_{R}(t)} \quad (3.9)\]  

But at \(t = 0\) the distributions for \(R\) and \(Q\) were independent, so that \(\mathrm{I}_{RQ}(0) = \mathrm{I}_R(0) + \mathrm{I}_Q(0)\) . Substitution of this relation, (3.5), and (3.6) into (3.9) then yields the final result:  

\[\{Q,R\}_{t}\cong \mathrm{I}_{R}(0) - \mathrm{I}_{Q}(0) + \ln t\]  

Therefore the correlation is built up at least as fast as \(\ln t\) , except for an additive constant representing the difference of the information of the initial distributions \(P_2(r)\) and \(P_1(q)\) . Since the correlation goes to infinity with increasing time, and the marginal system distribution is not changed, the interaction (3.1) satisfies our definition of a measurement of \(q\) by \(r\) .  

Even though the apparatus does not indicate any definite system value (since there are no independent system or apparatus states), one can nevertheless look upon the total wave function (3.2) as a superposition of pairs of subsystem states, each element of which has a definite \(q\) value and a correspondingly displaced apparatus state \(\frac{1}{2}\) . Thus we can write (3.2) as:  

\[\psi^{S + A} = \int \phi (q^{*})\delta (q - q^{*})\gamma (r - q^{*})dq^{*}\]  

which is a superposition of states \(\psi_{q, \infty} = \delta (q - q^{*})\gamma (r - q^{*})\) . Each of these elements, \(\psi_{q, \infty}\) of the superposition describes a state in which the system has the definite value \(q = q^{*}\) , and in which the apparatus has a state that is displaced from its original state by the amount \(q^{*}\) . These elements \(\psi_{q, \infty}\) are then superposed with coefficients \(\phi (q^{*})\) to form the total state (3.11).

---

1 See discussion of relative states, pg. (see 36)

---

Conversely, if we transform to the representation where the apparatus is definite, we write (3.2) as:  

\[\begin{array}{r l r}{{\mathcal{V}_{t}^{S\ast A}\equiv\int(1/\mathbb{H}_{r^{\prime}})\int^{\mathbb{r}^{\prime}}(q)\oint(r-r^{\prime})\mathrm{d}r^{\prime}}}\\ &{}&{\mathrm{where}\quad\int^{\mathbb{r}^{\prime}}(q)=\mathbb{H}_{r^{\prime}}\oint(q)\mathcal{H}(r^{\prime}-q t)}\\ &{}&{\mathrm{and}\quad(1/\mathbb{H}_{r^{\prime}})^{2}=\int^{\infty}(q)\oint(q)\mathcal{H}(r^{\prime}-q t)\mathcal{H}(r-q t)\mathrm{d}q}\end{array} \quad (3.12)\]  

Then the \(\int^{\mathbb{r}^{\prime}}(q)\) are the relative system state functions for the apparatus states \(\mathcal{S}(r - r^{\prime})\) of definite value \(r m r^{\prime}\) .  

We notice that these relative system states, \(\int^{\mathbb{r}^{\prime}}(q)\) , are nearly eigenstates for the values \(q m r^{\prime} / t\) , if the degree of correlation between \(q\) and \(r\) is sufficiently high. If \(t\) is very large, or \(\mathcal{H}(r)\) sufficiently sharp (near \(\mathcal{S}(r)\) ) then \(\int^{\mathbb{r}^{\prime}}(q)\) is nearly \(\mathcal{S}(q - r^{\prime} / t)\) .  

This property, that the relative system states become approximate eigenstates of the measurement, is in fact common to all measurements. If we adopt as a measure of the nearness of a state \(\mathcal{V}\) to being an eigenfunction of an operator \(A\) the information \(I_{A}(\mathcal{V})\) , which is reasonable because \(I_{A}(\mathcal{V})\) measures the sharpness of the distribution of \(A\) for \(\mathcal{V}\) , then it is a consequence of our definition of a measurement that the relative system states tend to become eigenstates as the interaction proceeds. Since \(\exp [I_{Q}^{\mathbb{r}}] = I_{Q} + [Q, R]\) , and \(I_{Q}\) remains constant while \([Q, R]\) tends toward its maximum (or infinity) during the interaction, we have that \(\exp [I_{Q}^{\mathbb{r}}]\) tends to a maximum (or infinity). But \(I_{Q}^{\mathbb{r}}\) is just the information in the relative system states, which we have adopted as a measure of the nearness to an eigenstate. Therefore,

---

at least in expectation, the relative system states approach eigenstates.  

We have seen that (3.12) is a superposition of states \(\psi_{r}\) , for each of which the apparatus has recorded a definite value \(r'\) , and the system is left in approximately the eigenstate of the measurement corresponding to \(q = r'/t\) . The discontinuous "jump" into an eigenstate is thus only a relative proposition, dependent upon our decomposition of the total wave function into the superposition, and relative to a particularly chosen apparatus \(C_{r'}\) . Value. So far as the complete theory is concerned all elements of the superposition exist simultaneously, and the entire process is quite continuous.  

We have here only a special case of the following general principle which will hold for any situation which is treated entirely wave mechanically:  

Principle: For any situation in which the existence of a property \(R_{1}\) for a subsystem \(S_{1}\) of a composite system \(S\) will imply the later property \(Q_{1}\) for \(S\) , then it is also true that an initial state for \(S_{1}\) of the form \(\psi_{1} = \sum_{i} \sum_{j} \psi_{1}^{i} \psi_{1}^{j}\) which is a superposition of states with the properties \(R_{1}\) , will result in a later state for \(S\) of the form \(\psi_{1} = \sum_{i} \sum_{j} a_{i} \psi_{1}^{i} \psi_{1}^{j}\) , which is also a superposition, of states with the property \(Q_{1}\) . That is, for any arrangement of an interaction between two systems \(S_{1}\) and \(S_{2}\) , which has the property that each initial state \(\psi_{1}^{i} \psi_{1}^{j}\) will result in a final situation with total state \(\psi_{1}^{i} \psi_{1}^{j}\) an initial

---

state of \(S_{1}\) of the form \(\sum_{i} a_{i} \phi_{i}^{S_{1}}\) will lead, after interaction, to the superposition \(\sum_{i} a_{i} \psi_{i}^{S_{1} + S_{2}}\) for the whole system.  

This follows immediately from the superposition principle for solutions of a linear wave equation. It therefore holds for any system of quantum mechanics for which the superposition principle holds, both particle and field theories, relativistic or not, and is applicable to all physical systems, regardless of size.  

This principle has the far reaching implication that for any possible measurement, for which the initial system state is not an eigenstate, the resulting state of the composite system leads to no definite system state nor any definite apparatus state. The system will not be put into one or another of its eigenstates with the apparatus indicating the corresponding value, and nothing resembling Process 1 can take place.  

To see that this is indeed the case, suppose that we have a measuring arrangement with the following properties. The initial apparatus state is \(\psi_{0}^{A}\) . If the system is initially in an eigenstate of the measurement, \(\phi_{1}^{S}\) , then after a specified time of interaction the total state \(\phi_{1}^{S} \psi_{0}^{A}\) will be transformed into a state \(\phi_{1}^{S} \psi_{1}^{A}\) , i.e. the system eigenstate shall not be disturbed, and the apparatus state is changed to \(\psi_{1}^{A}\) , which is different for each \(\phi_{1}^{S}\) . (\(\psi_{1}^{A}\) may for example be a state describing the apparatus as indicating, by the position of a meter needle, the eigenvalue of \(\phi_{1}^{S}\) .) However, if the initial system state is not an eigenstate but a

---

superposition \(\sum_{i} \alpha_{i} \phi_{i}^{S}\) , then the final composite system state is also a superposition, \(\sum_{i} \alpha_{i} \phi_{i}^{S} \psi_{i}^{A}\) . This follows from the superposition principle because, since all we need do is superpose our solutions for the eigenstates, \(\phi_{i}^{S} \psi_{i}^{A} \rightarrow \phi_{i}^{S} \psi_{i}^{A}\) , to arrive at the solution, \(\sum_{i} \alpha_{i} \phi_{i}^{S} \phi_{i}^{A} \rightarrow \sum_{i} \alpha_{i} \phi_{i}^{S} \psi_{j}^{A}\) , for the general case. Thus in general after a measurement has been performed there will be no definite system state nor any definite apparatus state, even though there is a correlation. It seems as though nothing can ever be settled by such a measurement. Furthermore this result is independent of the size of the apparatus, and remains true for apparatus of quite macroscopic dimensions.  

Suppose, for example, that we coupled a spin measuring device to a cannonball, so that if the spin is up the cannonball will be shifted one foot to the left, while is the spin is down it will be shifted an equal distance to the right. If we now perform a measurement with this arrangement upon a particle whose spin is a superposition of up and down, then the resulting total state will also be a superposition of two states, one in which the cannonball is to the left, and one in which it is to the right. There is no definite position for our macroscopic cannonball!  

This behavior seems to be quite at variance with our observations, since macroscopic objects always appear to us to have definite positions. Can we reconcile this prediction of the purely wave mechanical theory with experience, or must we abandon it as untenable? In order to answer this question we must consider the problem of observation itself within the framework of the theory.

---

We shall now give an abstract treatment of the problem of observation. In keeping with the spirit of our investigation of the consequences of pure wave mechanics we have no alternative but to introduce observers, considered as purely physical systems, into the theory.  

We saw in the last chapter that in general a measurement (coupling of system and apparatus) had the outcome that neither the system nor the apparatus had any definite state after the interaction - - a result seemingly at variance with our experience. However, we do not do justice to the theory of pure wave mechanics until we have investigated what the theory itself says about the appearance of phenomena to observers, rather than hastily concluding that the theory must be incorrect because the actual states of systems as given by the theory seem to contradict our observations.  

We shall see that the introduction of observers can be accomplished in a reasonable manner, and that the theory then predicts that the appearance of phenomena, as the subjective experience of these observers, is precisely in accordance with the predictions of the usual probabilistic interpretation of quantum mechanics.  

## 6.1. Formulation of the Problem  

We are faced with the task of making deductions about the appearance of phenomena on a subjective level, to observers which are considered as purely physical systems and are treated within the theory. In order to accomplish this it is necessary to identify

---

OBSERVATION 

Beginner 

اللاء دين
equation

---

some objective properties of such an observer (states) with subjective knowledge (i.e. perceptions). Thus, in order to say that an observer O has observed the event \(\alpha\) , it is necessary that the state of O has become changed from its former state to a new state which is dependent upon \(\alpha\) .  

It will suffice for our purposes to consider our observers to possess memories (i.e. parts of a relatively permanent nature whose states are in correspondence with the past experience of the observer). In order to make deductions about the subjective experience of an observer it is sufficient to examine the contents of the memory.  

As models for observers we can, if we wish, consider automatically functioning machines, possessing sensory apparatus and coupled to recording devices capable of registering past sensory data and machine configurations. We can further suppose that the machine is so constructed that its present actions shall be determined not only by its present sensory data, but by the contents of its memory as well. Such a machine will then be capable of performing a sequence of observations (measurements), and furthermore of deciding upon its future experiments on the basis of past results. We note that if we consider that current sensory data, as well as machine configuration, is immediately recorded in the memory, then the actions of the machine at a given instant can be regarded as a function of the memory contents only, and all relevant experience of the machine is contained in the memory.  

For such machines we are justified in using such phrases as "the machine has percieved A" or "the machine is aware of A" if

---

the occurrence of A is represented in the memory, since the future behavior of the machine will be based upon the occurrence of A. In fact, all of the customary language of subjective experience is quite applicable to such machines, and forms the most natural and useful mode of expression when dealing with their behavior, as is well known to individuals who work with complex automata. When dealing with observers quantum mechanically we shall ascribe state function, \(\psi^0\), to them. When the state \(\psi^0\) describes an observer whose memory contains representations of the events A, B, ..., C we shall denote this fact by appending the memory sequence in brackets as a subscript, writing:  

\[\psi^0 [A,B,\ldots ,C]\]  

The symbols A, B, ..., C, which we shall assume to be ordered time wise, shall therefore stand for memory configurations which are in correspondence with the past experience of the observer. These configurations can be thought of as punches in a paper tape, impressions on a magnetic reel, configurations of a relay switching circuit, or even configurations of brain cells. We only require that they be capable of the interpretation "The observer has experienced the succession of events A, B, ..., C." (We shall sometimes write dots in a memory sequence, [..., A, B, ..., C], to indicate the possible presence of previous memories which are irrelevant to the case being considered.)  

Our problem is, then, to treat the interaction of such observer with other physical systems (observations), within the

---

framework of wave mechanics, and to deduce the resulting memory configurations, which we can then interpret as the subjective experiences of the observers.  

We begin by defining what shall constitute a "good" observation. A good observation of a quantity \(A\) , with eigenfunctions \(\{\phi_i\}\) for a system \(S\) , by an observer whose initial state is \(\psi_0^0\) , shall consist of an interaction which, in a specified period of time, transforms each (total) state  

\[\psi^{S_0} = \phi_1^0 \psi_0^0\] \[\mathrm{into~a~state\]  

\[\psi^{-S_0} = \phi_1^0 \psi_0^0\] \[\qquad = \phi_1^0 \psi_0^0\]  

where \(\alpha_{1}\) characterizes the state \(\phi_{1}^{0}\) (It might stand for a recording of the eigenvalue, for example.) That is, our requirement is that the system if it is in an eigenstate, shall be unchanged, and that the observer state shall change so as to describe an observer who is "aware" of which eigenfunction it is, i.e. some property is recorded in the memory of the observer which characterizes \(\phi_{1}\) , such as the eigenvalue. The requirement that the eigenstates for the system be unchanged is necessary if the observation is to be significant (repeatable), and the requirement that the observer state change in a manner which is different for each eigenfunction is necessary if we are to be able to call the interaction an observation at all.

---

1 It should be understood that \(\psi_{[..\alpha ]}^{0}\) is a different state for each i. A more correct form would be to write \(\psi_{i[..\alpha ]}^{0}\) , but no confusion can arise if we simply let \(\psi_{i}^{0}\) be indexed only by the index of the memory configuration.  

2 Cf. the definition of measurement in the last chapter.

---

## 5. Deductions. 

From the requirements of section 1 we shall first deduce the result of an observation upon a system which is not in an eigenstate of the observation. We know, by our previous remark upon what constitutes a good observation that the interaction transforms states \(\phi_1 \psi_0^0 [\ldots ]\) into states \(\phi_1 \psi_0^0 [\ldots \alpha_1]\). Consequently we can simply superpose these solutions of the wave equation to arrive at the final state for the case of an arbitrary initial system state. Thus if the initial system state is not an eigenstate, but a general state \(\sum_i a_i \phi_1^0\), we get for the final total state: 

\[ (2.1) \quad \psi^{S+0} = \sum_i a_i \phi_1^0 \psi_0^0 [\ldots \alpha_1] \]

This remains true also in the presence of further systems which do not interact for the time of measurement. Thus, if systems \(S_1, S_2, \ldots, S_n\) are present as well as \(O\), with original states \(\psi^S_1, \psi^S_2, \ldots, \psi^S_n\), and the only interaction during the time of measurement is between \(S\) and \(O\), the result of the measurement will be the transformation of the initial total state: 

\[ \psi^{S_1+S_2+\ldots+S_n+0} = \psi^{S_1} \psi^{S_2} \ldots \psi^{S_n} \psi_0^0 [\ldots] \]

into the final state: 

\[ (2.2) \quad \psi^1 S_1 + S_2 + \ldots + S_n + 0 = \sum_i a_i \phi_1^1 \psi_1^S_2 \ldots \psi_n^S_n \psi_0^0 [\ldots \alpha_1] \]

此项 as \(\psi^1 \psi^2 \ldots \psi^n \psi_0^0 [\ldots \alpha_1]\) and \(\phi_1^0\) are eigenfunctions of the observation. Thus we arrive at the general rule for the transformation of

---

total state functions which describe systems within which observation processes occur:  

Rule 1: The observation of a quantity A, with eigenfunctions \(\phi_{1}^{S_{1}}\) , in a system \(S_{1}\) by the observer \(O\) , transforms the total state according to:  

\[\psi_{1}^{S_{1}}\psi_{2}^{S_{2}}\dots \psi_{n}^{S_{n}}\psi_{0}^{O}\xrightarrow{\sum_{i}a_{i}\phi_{i}^{S_{i}}\psi_{i}^{S_{i}}\dots\psi_{n}^{S_{n}}\psi_{0}^{O}}[\dots\alpha_{2}]\] \[\mathrm{where~}a_{1}=(\phi_{1}^{S_{1}}\psi_{1}^{S_{1}}).\]  

If we next consider a second observation to be made, where our total state is now a superposition, we can apply Rule 1 separately to each element of the superposition, since each element separately obeys the wave equation and behaves independently of the remaining elements, and then superpose the results to obtain the final solution. We formulate this as:  

Rule 2: Rule 1 may be applied separately to each element of a superposition of total system states, the results being superposed to obtain the final total state. Thus, a determination of \(B\) , with eigenfunctions \(\eta_{j}^{S_{j}}\) , on \(S_{2}\) by the observer \(O\) transforms the total state  

\[\sum_{i}a_{i}\phi_{i}^{S_{i}}\psi_{i}^{s_{2}}\dots \psi_{n}^{s_{n}}\psi_{0}^{O}\]  

into the state  

\[\sum_{i,j}a_{i}b_{j}\phi_{i}^{S_{i}}\eta_{j}^{S_{2}}\psi_{i}^{s_{2}}\dots \psi_{n}^{s_{n}}\eta_{j}^{O}\]  

where \(b_{j \in \mathcal{S}}(\eta_{j}^{S_{j}} \psi_{j}^{S_{j}})\) , which follows from the application of Rule 1 to each element \(\phi_{i}^{S_{i}}\psi_{i}^{S_{i}}\psi_{0}^{O}\) and then superposing the results with the coefficients \(a_{1}\) .

---

These two rules, which follow directly from the superposition principle, give us a convenient method for determining final total states for any number of observations in any combinations. We must now seek the interpretation of such final total states.  

We first consider the simple case of a single observation of a quantity A, with eigenfunctions \(\phi_{1}\) , in the system S with initial state \(\psi^{S}\) , by an observer O whose initial state is \(\psi_{[0..0]}^{0}\) . The final result is, as we have seen, the superposition (2.1):  

\[(2.3) \quad \psi^{S + 0} = \sum_{i} a_{i} \phi_{i} \psi_{[0..0]}^{0} \quad (2.3)\]  

We note that there is no longer any independent system state or observer state, although the two have become correlated in a one- one manner. However, each element of the superposition (2.3), \(\phi_{i} \psi_{[0..0]}^{0}\) ,

---

the system is described a particular eigenstate and describes a definite system state which is an eigenstate of A, the observant always observes the definite state that particular system state. It is this correlation which allows one to maintain the interpretation that a measurement has been performed.  

We now carry the discussion a step further and allow the observer to repeat the observation. Then according to Rule 2 we arrive at the total state after the second observation:  

\[(2.4) \quad \psi^{S + 0} = \sum_{i} a_{i} \psi_{i}^{0}\]  

Again, we see that each element of \(\left(\frac{\partial}{\partial x}\right)\) , \(\psi_{i}^{0} \psi_{i}^{0} \psi_{i}^{0} \psi_{i}^{0}\) , describes a system eigenstate, but this time also describes the observer who obtained the same result for each of the two observations. Thus, to each separate observer which is described by an element of the superposition (2.2) the observation was repeatable. This repeatability is, of course, a consequence of the fact that after an observation the relative system state for a particular observer state is the corresponding eigenstate.  

Let us suppose now that an observer \(0\) , with initial state \(\psi_{0}^{0}\) , measures the same quantity \(A\) in a number of separate systems which are in the same state, \(\psi_{1}^{0} = \psi_{2}^{0} = \dots = \psi_{n}^{0} = \sum_{i} a_{i} \psi_{i}^{0}\) (where the \(a_{i}\) are, as usual, eigenfunctions of \(A\) ). The initial total state function is then  

\[(2.3) \quad \psi_{0}^{S_{1} S_{2} \dots S_{n} + 0} = \psi_{0}^{S_{1}} \psi_{0}^{S_{2}} \dots \psi_{0}^{S_{n}} \psi_{0}^{0}\]

---

1 At this point we encounter a language difficulty. Whereas before the observation we had a single observer state afterwards there were a number of different states for the observer, all occurring in a superposition. Each of these separate states is a state for an observer, so that we can speak of the different observers described by the different states. On the other hand, the same physical system is involved, and from this viewpoint it is the same observer, which is in different states for different elements of the superposition (i.e., has had different experiences in the separate elements of the superposition). In this situation we shall use the singular when we wish to emphasize that a single physical system is involved, and the plural when we wish to emphasize the different experiences for the separate elements of the superposition. (e.g., "The observer performs an observation of the quantity A, after which each of the observers of the resulting superposition has perceived an eigenvalue.")

---

We shall assume that the measurements are performed on the systems in the order \(S_1, S_2, \ldots, S_n\). Then the total state after the first measurement will be, by Rule 1,  

\[(2.4) \quad \psi^{S_1 S_2 \ldots S_n} = \sum_i a_i \phi_i^{S_1} \psi^{S_2} \ldots \psi^{S_n} \psi_1^{0} \psi_2^{0} \ldots \psi_n^{0} \psi_1^{0} \psi_2^{0} \ldots \psi_1^{0} \psi_2^{0} \ldots \psi_2^{0} \psi_1^{0} \psi_2^{0} \ldots\]  

(where operators to the first system, \(S_1\) )  

After the second measurement it will be, by Rule 2,  

\[(2.5) \quad \psi_2^{S_1 S_2} = \sum_{i,j} a_i a_j \phi_i^{S_1} \phi_j^{S_2} \psi_1^{S_2} \psi_2^{S_1} \psi_1^{S_2} \psi_2^{S_1} = \psi_1^{S_2} \psi_2^{S_1} \ldots \psi_1^{S_2} \psi_2^{S_1} \dots \psi_1^{S_2} \psi_2^{S_1} \]and in general, after \(\psi\) measurements have taken place (Rule 2 gives the result:\]  

and in general, after \(\psi\) measurements have taken place (Rule 2 gives the result:)  

\[(2.6) \quad \psi_r = \sum_{i,j,k} a_i a_j \ldots a_k \phi_i^{S_1} \phi_j^{S_2} \ldots \phi_k^{S_r} \psi_1^{S_r} \psi_2^{S_r} \ldots \psi_k^{S_r} \psi_1^{S_r} \ldots \psi_k^{S_r} \psi_1^{S_1} \ldots \psi_k^{S_r} \psi_1^{S_1} = \psi_1^{S_1} \psi_2^{S_1} \ldots \psi_1^{S_1} \psi_2^{S_1} \psi_1^{S_1} \ldots \psi_1^{S_1} \psi_1^{S_1} \ldots \psi_2^{S_1} \psi_1^{S_1} \psi_1^{S_1} \psi_1^{1} \ldots \psi_1^{1} \psi_1^{1} \psi_1^{1} \psi_1^{2} \psi_1^{1} \psi_1^{1} \psi_1 \psi_1^{1} \psi_1^{1} \psi_1^{3} \psi_1^{1} \psi_1^{1} \psi_1^1 \psi_1^{1} \psi_1^{1} \psi_1^2 \psi_1^{1} \psi_1^{1} \psi_1^3 \psi_1^{1} \psi_1^{1} \psi_1^4 \psi_1^{1} \psi_1^1 \psi_1^1 \psi_1^1 \psi_1^1 \ldots \psi_1^1 \psi_1^1 \psi_1^1 \dots \psi_1^1 \psi_1^1 \psi_1^1 \cdots \psi_1^1 \psi_1^1 \psi_1^1 \cdot \psi_1^1 \psi_1^1 \psi_1^1 \quad \psi_1^1 \psi_1^1 \psi_1^1 \qquad \psi_1^1 \psi_1^1 \psi_1^1 \]  

We can give this state, \(\psi_r\) , the following interpretation. It consists of a superposition of states:

---

position should repeat any one of the preceding determinations, that observer would obtain the same result that was obtained for the earlier observation, since the relative system states are now eigenstates. That is, if at this stage a redetermination of an earlier system observation \((S_{1})\) takes place, every element of the resulting final superposition will describe the observer whose memory state is of the form \(\left[\alpha_{1}^{1}, \alpha_{2}^{1}, \ldots , \alpha_{n}^{1}\right]\) in which the earlier memory coincides with the later- i.e. the memory states are correlated. It will thus appear to the observer which is described by a typical element of the superposition that each initial observation on a system caused the system to "jump" into an eigenstate, in a random fashion and thereafter remain there. Therefore, qualitatively, at least, the probabilistic assertions of Process 1 appear to be valid to the observer described by a typical element of the final superposition. In order to establish quantitative results, we must put some sort of measure (weighting) on the elements of a final superposition. This is necessary to be able to make assertions which will hold for almost all of the observers described by elements of a superposition. In order to make quantitative statements about the relative frequencies of the different possible results of observation which are recorded in the memory of a typical observer we must have a method of selecting a typical observer.  

In order to establish quantitative results, we must put some sort of measure (weighting) on the element of a final superposition. This is necessary to be able to make assertions which will hold for almost al of the observers described by elements of a superposition. In order to make quantitative statements about the relative frequencie of the different possible results of observation which are recorded in the memory of a typical observer we must hae a method of selecting a typical observer.

---

weww.weeww.eww.eww.eww.eww.eww.eww.ewww.eww.eww.eww.eww.eww.eww.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.eww.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.wewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.wewa.eww.ewa.ewa.ewa.ewa.ewa.ewa.ewa.eww.ewa.wewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.eww.eww.ewa.ewa.ewa.ewa.ewa.ewa.eww.ewa.ewa.wewa.ewa.ewa.ewa.ewa.ewa.ewa.eww.ewa.eww.ewa.ewa.ewa.ewa.ewa.ewa.ewa.wewa.ewa.eww.ewa.ewa.ewa.ewa.ewa.ewa.eww.eww.eww.ewa.ewa.ewa.ewa.ewa.wewa.ewa.ewa.ewa.eww.ewa.ewa.ewa.ewa.eww.ewa.ewa.ewa.ewa.wewa.ewa.ewa.ewa.ewa.eww.ewa.ewa.ewa.eww.ewa.ewa.ewa.ewa.ewa.wewa.ewa.ewa.wewa.ewa.ewa.ewa.ewa.ewa.ewa.wewa.ewa.ewa.wewa.eww.ewa.ewa.ewa.ewa.eww.ewa.ewa.wewa.ewa.wewa.ewa.ewa.ewa.ewa.ewa.wewa.ewa.ewa.wewa.wewa.ewa.ewa.ewa.ewa.ewa.ewa.wewa.ewa.wewa.ewa.ewa.ewa.ewa.eww.ewa.eww.ewa.wewa.ewa.ewa.ewa.ewa.ewa.wewa.ewa.eww.eww.ewa.ewa.ewa.ewa.ewa.wewa.eww.ewa.ewa.wewa.ewa.ewa.ewa.ewa.eww.ewa.wewa.ewa.eww.ewa.ewa.ewa.ewa.ewa.wewa.eww.eww.ewa.ewa.ewa.ewa.ewa.ewa.wewa.ewa.ewa.eww.ewa.ewa.ewa.ewa.ewa.eww.ewa.ewa.ewa.wewa.ewa.ewa.ewa.ewa.ewa.eww.ewa.ewa.eww.ewa.ewa.ewa.ewa.ewa.ewa.wewa.ewa.wewa.eww.ewa.ewa.ewa.ewa.ewa.eww.ewa.wewa.ewa.wewa.ewa.ewa.ewa.ewa.ewa.wwa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.wwa.ewa.ewa.ewa.wewa.ewa.ewa.ewa.ewa.ewa.wwa.ewa.wwa.ewa.ewa.ewa.ewa.ewa.ewa.wwa.ewa.ewa.wa.ewa.ewa.ewa.ewa.ewa.wwa.ewa.ewa.ewa.wa.ewa.ewa.ewa.ewa.ewa.wwa.eww.ewa.ewa.ewa.ewa.ewa.ewa.wwa.ewa.ewa.eww.ewa.ewa.ewa.ewa.ewa.ewa.mwa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.wa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.mwa.ewa.ewa.wa.ewa.ewa.ewa.ewa.ewa.ewa.wa.ewa.ewa.wa.ewa.ewa.ewa.ewa.ewa.ewa.mwa.ewa.ewa.eww.ewa.ewa.ewa.ewa.ewa.ewm.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.awa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.owa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.owm.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.mw.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.mwm.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.awm.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.wm.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.awm.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.awm.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.aawm.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewa.ewm.ewa.ewa.ewa.mwm.ewa.ewa.ewa.ewa.ewa.ewm.ewa.ewa.ewa.awn.ewa.ewa.ewa.ewa.ewa.ewm.ewa.ewa.ewa.awm.ewa.ewa.ewa.ewa.ewa.ewm.ewa.ewa.ewa.wm.ewa.ewa.ewa.ewa.ewa.ewm.ewa.ewa.ewm.ewa.ewa.ewa.ewa.ewa.ewa.mwm.ewa.ewa.ewm.ewa.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewa.ewm.ewa.ewa.ewa.ewa.ewa.ewa.awm.ewa.ewa.ewm.ewa.ewa.ewa.ewa.ewa.ewm.ewa.ewa.awa.ewa.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewa.awa.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewa.ewa.awa.ewa.ewa.ewa.ewa.awn.ewa.ewa.ewa.ewa.awa.ewa.ewa.ewa.awn.ewa.ewa.ewa.ewa.ewa.awa.ewa.ewa.awn.ewa.ewa.ewa.ewa.ewa.ewa.awa.ewa.awn.ewa.ewa.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewm.ewa.ewa.ewa.ewa.ewa.ewa.ewa.awn.ewa.wa.ewa.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewa.wa.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewa.ewa.wa.ewa.ewa.ewa.awn.ewa.ewa.ewa.ewa.ewa.wa.ewa.awn.ewa.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewa.owa.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewa.ewa.owa.ewa.ewa.ewa.awn.ewa.ewa.ewa.ewa.ewa.owa.ewa.awn.ewa.ewa.ewa.ewa.ewa.ewa.awn.ewm.ewa.ewa.ewa.ewa.ewa.ewa.ewa.awn.awn.ewa.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewm.awn.ewa.ewa.ewa.ewa.ewa.ewa.awn.ewa.wa.wa.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewa.wa.wa.ewa.ewa.ewa.awn.ewa.ewa.ewa.ewa.wa.ewa.awn.ewa.ewa.wa.wa.ewa.ewa.ewa.aawm.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewa.ewa.ewm.ewa.ewa.ewa.ewa.ewa.awn.ewa.ewa.ewa.awn.ewa.ewa.ewa.awn.ewa.ewm.ewa.ewa.ewa.awn.ewa.ewa.awn.ewa.ewa.awn.ewa.ewa.awn.ewm.ewa.ewa.ewa.awn.ewa.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.aawm.ewa.ewa.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewm.ewa.ewa.awn.ewa.awn.ewa.awn.ewa.awn.wa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewm.awn.ewa.awn.ewa.awn.ewa.awn.ewa.awn.wa.aawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.aawn.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.aan.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.aun.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.aen.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.aewm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.ewa.awn.ewa.awn.ewa.awn.ewm.awn.ewa.ewa.awn.ewa.awn.ewa.awn.ewa.aawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.awn.ewa.awn.ewa.awn.ewa.awn.ewa.awn.awa.m.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.aowm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.awm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.auwm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.aon.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.aown.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.aoun.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.aouwm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.ewm.awn.ewa.awn.ewa.awn.ewa.awn.ewa.ewa.aun.ewa.awn.ewa.awn.ewa.awn.ewa.aun.ewa.aun.ewa.awn.ewa.awn.ewa.awn.ewa.aowm.ewa.ewa.awn.ewa.awn.ewa.awn.ewa.awn.awn.ewm.awn.ewa.awn.ewa.awn.ewa.awn.awn.ewa.aun.ewa.awn.ewa.awn.ewa.awn.ewm.awn.ewa.m.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.waa.m.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.aww.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.awo.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.awwm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewa.wawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewm.wawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.wawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.wawa.m.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewm.awm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ewwawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.waawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.awaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.awawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.owaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.owawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.oaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.owoawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.oweawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.oeawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ooawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.oooawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ooooawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.oonawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.onoawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.onawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.onaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.oneawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.oenawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.onenawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.enoawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.eneawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.enenawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.ennawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.enneawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.enawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.enaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.eenawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.eeawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.eeeawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.eeeeawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.weeawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.weeaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.wweaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.wweaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.wwwawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.uwwaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.wuwaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.uwaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aauwawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aawaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aawanawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aawnawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aanawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aannawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aanaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aeawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aeaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aaaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aaaaaaaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aanawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.anawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.anaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aaanawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aaaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aaaaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.aabawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.abaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.abaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.abaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.baaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.baaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.caaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.daaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.eaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.faaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.gaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.haaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.iiaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.jaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.kaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.laaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.maaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.naaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.oaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.paaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.rraawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.saaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.taaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.uaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.vaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.waaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.xaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.yaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.zaaawm.ewa.awn.ewa.awn.ewa.awn.ewa.awn.

<|ref|>

<|ref|>

<|ref|>

---

so that we can make use of it, while keeping in mind that all results should be translated back to measure theoretic language.  

Thus, in particular, if we consider the sequences to become longer and longer (more and more observations performed) each memory sequence of the final superposition will satisfy any given criterion for a randomly generated sequence, generated by the independent probabilities \(\mathcal{A}_i^a \mathcal{A}_i^a\) , except for a set of total measure which tends toward zero as the number of observations becomes unlimited. Hence all averages of functions over any memory sequence, including the special case of frequencies, can be computed from the probabilities \(\mathcal{A}_i^a \mathcal{A}_i^a\) , except for the set of memory sequences of measure zero. We have therefore shown that the statistical assertions of Process 1 will appear to be valid to almost all observers described by separate elements of the superposition (2.6), in the limit as the number of observations goes to infinity.  

While we have so far considered only sequences of observations of the same quantity upon identical systems, the result is equally true for arbitrary sequences of observations. For example, the sequence of observations of the quantities \(A^1, A^2, \ldots , A^n, \ldots\) with (generally different) eigenfunction sets \(\{\phi_1^1, \phi_2^1, \ldots, \phi_n^1\}\) , \(\{\phi_n^m\}\) , \(\ldots\) applied successively to the systems \(S_1, S_2, \ldots, S_n, \ldots\) , with (arbitrary) initial states \(\psi_1, \psi_2, \ldots, \psi_n, \ldots\) , transforms the total initial state:

---

Smart
or may be easily verified by writing
more general sequence of measurements) and
applying rules 6 and 7 in this same manner
or presented here.

---

by rules 1 and 2, into the final state

---

sequences, but of random sequences for which the individual terms are no longer independent. The memory states \(\mathcal{B}_{m}^{r}\) now depend upon the memory states \(\alpha_{L}^{r}\) which represent the result of the previous measurement upon the same system, \(S_{r}\) . The joint (normalized) measure for this pair of memory states, conditioned by fixed values for remaining memory states is:  

\[M^{\alpha_{L}^{1}\ldots\alpha_{L}^{r_{1}}\alpha_{L}^{r_{2}}\ldots\alpha_{L}^{r_{m}}}(\alpha_{L}^{r}\beta_{m}^{r}) = \frac{M(\alpha_{L}^{1}\ldots\alpha_{L}^{r_{1}}\ldots\alpha_{L}^{r_{m}}\beta_{m}^{r})}{\sum_{m = 1}^{r}M(\alpha_{L}^{1}\ldots\alpha_{L}^{r_{1}}\ldots\alpha_{r_{m}}\beta_{m}^{r})} \quad (2.15)\]  

The joint measure (2.15) is, first of all, independent of the memory states for the remaining systems (5. ... excluding \(S_{r}\) ). Second, the dependence of \(\beta_{m}^{r}\) on \(\alpha_{L}^{r}\) is equivalent, measure theoretically, to that given by the stochastic process which converts the states \(\phi_{L}^{r}\) into the states \(N_{m}^{r}\) with transition probabilities:  

\[T_{em} = \text{Prob.} (\phi_{r}^{r} \Rightarrow N_{m}^{r}) = |(\pi_{m}^{r} \phi_{L}^{r})|^{2} \quad (2.16)\]  

If we were to allow yet another quantity \(C\) be measured in \(S_{r}\) , the new memory states \(\beta_{r}^{r}\) corresponding to the eigenfunctions of \(C\) would have a similar dependence upon the previous states \(\beta_{m}^{r}\) , but no direct dependence on the still earlier states \(\alpha_{L}^{r}\) . This dependence upon only the previous result of observation is a consequence of the fact that the relative system states are completely determined by the last observation.

---

1 Cf. Chapter II, §6.

---

We can therefore summarize the situation for an arbitrary sequence of observations, upon the same or different systems in any order, and for which the number of observations of each quantity in each system is very large, with the following result:  

Except for a set of memory sequences of measure nearly zero, the averages of any functions over a memory sequence can be calculated approximately by the use of the independent probabilities given by Process 1 for each initial observation, on a system, and by the use of the transition probabilities (2.16) for succeeding observations upon the same system. In the limit, as the number of all types of observations goes to infinity the calculation is exact, and the exceptional set has measure zero.  

This prescription for the calculation of averages over memory sequences by probabilities assigned to individual elements is precisely that of the orthodox theory (Process 1). However, therefore since all predictions of the usual theory will appear to be valid to observer since these predictions hold for almost all memory sequences.  

In particular, the uncertainty principle is never violated, since, as above, the latest measurement upon a system supplies all possible information about the relative system state, so that there is no direct correlation between any earlier results of observation on the system, and the succeeding observation.

---

Any observation of a quantity B, between two successive observations of quantity A (all on the same system) will destroy the one- one correspondence between the earlier and later memory states for the result of A. Thus for alternating observations of different quantities there are fundamental limitations upon the correlations between memory states for the same observed quantity, these limitations expressing the content of the uncertainty principle.  

In conclusion, we have described in this section processes involving an idealized observer, processes which are entirely deterministic and continuous from the over- all viewpoint (the total state function is presumed to satisfy a wave equation at all times) but whose result is a superposition, each element of which describes the observer with a different memory state. We have seen that almost all of these observers it appears that the probabilistic aspects of the usual form of quantum theory are valid. We have thus seen how pure wave mechanics, without any initial probability assertions, can lead to these notions on a subjective level, as appearances to observers.

---

Stion here on contiuation from 72  

3. Remarks on the choice of square amplitude measure:  

While at first sight an artificial choice, and one which seems to give rise to the danger of begging the question, a little reflection shows that this choice of measure is not so arbitrary as it appears, but is the only reasonable choice for the purpose of making statistical deductions.  

Let us consider the search for a general scheme for assigning a measure to the elements of a superposition of orthogonal states \(\sum a_{i} \phi_{i}\) . We require then a positive function \(m\) of the complex coefficients of the elements of the superposition, so that \(m(a_{i})\) shall be the measure assigned to the element \(\phi_{i}\) . In order that this general scheme shall be unambiguous we must first require that the states themselves always be normalized, so that we can distinguish the coefficients from the states. However, we can still only determine the coefficients, in distinction to the states, up to an arbitrary phase factor, and hence the function \(m\) must be a function of the amplitudes of the coefficients alone, (i.e. \(m(a_{i}) = m(\sqrt{a_{i}^{*}a_{i}})\) ), in order to avoid ambiguities.  

If we now impose the additivity requirement that if we regard a subset of the superposition, say \(\sum a_{i} \phi_{i}\) , as a single element \(\alpha \phi^{\prime}\) :  

\[(3.1) \qquad \alpha \phi^{\prime} = \sum_{i = 1}^{n} \alpha_{i} \phi_{i}\]  

then the measure assigned to \(\phi^{\prime}\) shall be the sum of the measures assigned to the \(\phi_{i}\) ( \(i\) from 1 to \(n\) ):

---

\[(3.2) \quad M(\alpha) = \sum_{i} m(a_{i})\]  

then we have already restricted the choice of \(m\) to the square amplitude alone. \((m(a_{i}) = a_{i}^{*}a_{i}\) , apart from a multiplicative constant.)  

To see this we note that the normality of \(\phi^{\prime}\) requires that \(|\alpha | = \sqrt{\sum_{i = 1}^{m}a_{i}^{*}a_{i}}\) . From our remarks upon the dependence of \(m\) upon the amplitude alone, we replace the \(a_{i}\) by their amplitudes \(\mathcal{A}_{i} = |a_{i}|\) .  

(3.2) then requires that  

\[(3.3) m(\alpha) = m(\sqrt{\sum_{i}a_{i}^{*}a_{i}}) = m(\sqrt{\sum_{i}a_{i}^{2}}) = \sum m(u_{i}) = \sum m(\sqrt{a_{i}^{2}})\]  

Defining a new function \(g(x)\) :  

\[(3.4) q(x) = m(\sqrt{x})\]  

we see that (3.3) requires that  

\[(3.5) q(\sum u_{i}^{2}) = \sum q(u_{i}^{2})\]  

so that \(g\) is restricted to be linear and necessarily has the form:  

\((3.6)\) \(g(x) = c x\) (c constant)  

Therefore \(g(x) = c x^{2} = m\sqrt{x} = m(x)\) and we have deduced that \(m\) is restricted to the form:  

\[(3.7) m(a_{i}) = m(u_{i}) = c u_{i}^{2} = c a_{i}^{*}a_{i}\]  

and we have shown that the only choice of measure consistent with

---

our additivity requirement is the square amplitude measure, apart from an arbitrary multiplicative constant which may be fixed, if desired, by normalization requirements. (The requirement that the total measure be unity implies that this constant is 1.)  

The situation here is fully analagous to that of classical statistical mechanics, where one puts a measure on trajectories of systems in the phase space by placing a measure on the phase space itself, and then making assertions which hold for "almost all" trajectories (such as ergodicity, quasi- ergodicity, etc.) This notion of "almost all" depends here also upon the choice of measure, which is in this case taken to be the Lebesgue measure on the phase space. One could, of course, contradict the statements of classical statistical mechanics by choosing a measure for which only the exceptional trajectories had non- zero measure. Nevertheless the choice of Lebesgue measure on the phase space can be justified by the fact that it is the only choice for which the "conservation of probability" holds, (Liouville's theorem) and hence the only choice which makes possible any reasonable statistical deductions at all.  

In our case, we wish to make statements about "trajectories" of observers. However, for us a trajectory is constantly branching (transforming from state to superposition) with each successive measurement. To have a requirement analogous to the "conservation of probability" in the classical case, we demand that the measure assigned to a trajectory at one time shall equal the sum of the

---

1 See Khinchin [6].

---

measures of its separate branches at a later time. This is precisely the additivity requirement which we imposed and which leads uniquely to the choice of square- amplitude measure. Our procedure is therefore quite as justified as that of classical statistical mechanics.  

(continued on page 73)

---

## 4 Several Observers  

We shall now consider the consequences of our scheme when several observers are allowed to interact with the same systems, as well as with one another (communication). In the following discussion observers shall be denoted by \(0_{1}, 0_{2}, \ldots\) , other systems by \(S_{1}, S_{2}, \ldots\) , and observables by operators \(A, B, C,\) with eigenfunctions \(\{\phi_{j}\} , \{n_{j}\} , \{r_{j}\}\) respectively. The symbols \(\alpha_{j}, \beta_{j}, \gamma_{j}, \ldots\) occurring in memory sequences shall refer to characteristics of the states \(\phi_{j}, n_{j}, \{r_{j}\}\) respectively. \((\gamma_{j}^{O_{j}} \ldots)\) is interpreted as describing an observer, \(0_{j}\) , who has just observed the eigenvalue corresponding to \(\phi_{j}\) , i.e. who is "aware" that the system is in state \(\phi_{j}\) ).  

We shall also wish to allow communication among the observers, which we view as an interaction by means of which the memory sequences of different observers become correlated. (For example, the transfer of impulses from the magnetic tape memory of one mechanical observer to that of another constitutes such a transfer of information.) We shall regard these processes as observations made by one observer on another and shall use the notation that  

\[\frac{\gamma_{j} \circ_{j}}{[\ldots \alpha_{j} \circ_{k}]}\]  

represents a state function describing an observer \(0_{j}\) who has obtained the information \(\alpha_{j}\) from another observer, \(0_{k}\) . Thus the obtaining of information about \(A\) from \(0_{j}\) by \(0_{2}\) will transform the state  

\[\frac{\gamma_{j} \alpha_{j}}{[\ldots \alpha_{j}]} \frac{\gamma_{j} \alpha_{2}}{[\ldots]}\]

---

at said , that total is the amount of money at the time when she became the mother of the child. The amount of money at the time of the child's birth is the amount of money at the time of the child's death. The amount of money at the time of the child's death is the amount of money at the time of the child's death. The amount of money at any time is the amount of money at any time. The amount of money at any time is the amount of money at any time. The amount at any time is the amount of money at any time. The amount at any time is the sum of the amount at any time. The amount at any time is the sum of the amount at any time. 

1 We assume that such transfers merely duplicate, but do not destroy, the original information.

---

into the state  

\[(\mathrm{4.1})\quad \psi_{\mathrm{~\alpha~}}^{\mathrm{~\alpha~}}\psi_{\mathrm{~\alpha~}}^{\mathrm{~\alpha~}}\psi_{\mathrm{~\beta~}}^{\mathrm{~\alpha~}}\psi_{\mathrm{~\beta~}}^{\mathrm{~\beta~}}\psi_{\mathrm{~\beta~}}^{\mathrm{~\beta~}}\psi_{\mathrm{\beta~}}^{\mathrm{~\beta~}}\psi_{\mathrm{\beta~}}^{\mathrm{~\alpha~}}\psi_{\mathrm{\beta~}}^{\mathrm{~\alpha~}}\psi_{\mathrm{\alpha~}}^{\mathrm{~\alpha~}}\psi_{\mathrm{\alpha~}}^{\mathrm{~\alpha}}\psi_{\mathrm{\alpha~}}^{\mathrm{~\alpha~}}\psi_{\mathrm{\alpha}}\psi_{\mathrm{\alpha}}\psi_{\mathrm{\alpha}}\psi_{\mathrm{\alpha}}\]  

Rules 1 and 2 are, of course, equally applicable to these interactions. We shall now illustrate the possibilities for several observers, by considering several cases.  

Case 1: We allow two observers to separately observe the same quantity in a system, and then compare results.  

We suppose that first observer \(O_{1}\) observes the quantity A for the system S. Then by Rule 1 the original state  

\[\psi^{5,0,1,0,2} = \psi^{5}\psi^{0,2}\psi^{0,2}\]  

is transformed into the state  

\[(\mathrm{4.2})\qquad \psi^{\prime} = \sum_{i}\left(\phi_{i}^{5}\psi^{5}\right)\phi_{i}^{5}\frac{\psi^{0,2}}{\left[\dots\right]}\frac{\psi^{0,2}}{\left[\dots\right]}\]  

We now suppose that \(O_{2}\) observes A, and by Rule 2 the state becomes:  

\[(\mathrm{4.3})\qquad \psi^{\prime \prime} = \sum_{i}\left(\phi_{i}^{5}\psi^{5})\phi_{i}^{5}\frac{\psi^{0,2}}{\left[\dots\right]}{\frac{\psi^{0,2}}{\left[\dots\right]}} \quad (4.3)\]  

We now allow \(O_{2}\) to "consult" \(O_{1}\) , which leads in the same fashion from (4.1) and Rule 2 to the final state  

\[(\mathrm{4.9})\qquad \psi^{\prime \prime \prime} = \sum_{i}\left(\phi_{i}^{5}\psi^{\prime 5}\right)\phi_{i}^{5}\frac{\psi^{0,2}}{\left[..\right]}\frac{\psi^{0,2}}{\left[..\right]}\frac{\psi^{\prime 0,2}}{\left[..\right]}\]

---

Thus, for every element of the superposition the information obtained from \(O_{1}\) agrees with that obtained directly from the system. This means that observers who have separately observed the same quantity will always agree with each other.  

Furthermore, it is obvious at this point that the same result, (4.4), is obtained if \(O_{1}\) first consults \(O_{1}\) , then performs the direct observation, except that the memory sequence for \(O_{1}\) is reversed \(([\alpha_{1}^{3} \alpha_{1}]\) instead of \([\alpha_{1} \alpha_{1}^{3}]\) ). There is still perfect agreement in every element of the superposition. Therefore, information obtained from another observer is always reliable, since subsequent direct observation will always verify it. We thus see the central role played by correlations in wave functions for the preservation of consistency in situations where several observers are allowed to consult one another. It is the transitivity of correlation in these cases (that if \(S_{1}\) is correlated to \(S_{2}\) , and \(S_{2}\) to \(S_{3}\) , then so is \(S_{2}\) to \(S_{2}\) ) which is responsible for this consistency.  

Case 2: We allow two observers to measure separately two different, non- commuting quantities in the same system.  

Assume that first \(O_{1}\) observes A for the system, so that, as before, the initial state \(\psi^{s} \psi^{a} \psi^{a}\) is transformed to:

---

\[(\mathrm{4.6})\quad \Psi^{\prime \prime} = \sum_{i,j}\left(\phi_{i}\psi^{\prime}\right)\left(n_{j}\phi_{i}\right)\hat{m}_{i}\psi_{[a]}^{\prime}\psi_{[a]}^{\prime \prime} \quad (4.6)\]  

\(0_{2}\) is now perfectly correlated with the system, since a redetermination by him will lead to agreeing results. This is no longer the case for \(0_{1}\) , however, since a redetermination of \(A\) by him will result in (by rule 2)  

\[(\mathrm{4.7})\quad \Psi^{\prime \prime} = \sum_{i,j,n_{i}}\left(\phi_{i}\psi^{\prime}\right)\left(n_{j}\phi_{j}\right)\left(\phi_{k}\psi_{k}^{\prime}\right)\phi_{k}^{\prime \prime}\psi_{[a]}^{\prime \prime}\psi_{[a]}^{\prime \prime} \quad (4.7)\]  

Hence the second measurement of \(0_{2}\) does not in all cases agree with the first, and has been upset by the intervention of \(0_{2}\) .  

We can deduce the statistical relation between \(0_{2}\) 's first and second results \((\alpha_{1}\) and \(\alpha_{k}\) ) by our previous method of assigning a measure to the elements of the superposition (4.7). The measure assigned to the \((\phi_{j}, \phi_{k})\) element is then:  

\[(\mathrm{4.8})\qquad M_{j,k} = \left|(\phi_{j}\psi^{\prime})(n_{j}\phi_{i})(\phi_{k},n_{j})\right|^{2}\]  

This measure is equivalent, in this case, to the probabilities assigned by the orthodox theory (Process 1), where \(0_{2}\) 's observation is regarded as having converted each state \(\phi_{i}\) into a non- interfering mixture of states \(n_{j}\) , weighted with probabilities \(\left|(n_{j}, \phi_{i})\right|^{2}\) , upon which \(0_{2}\) makes his second observation.  

Note, however, that this equivalence with the statistical results obtained by considering that \(0_{2}\) 's observation changed the system state into a mixture, holds true only so long as \(0_{2}\) 's second observation is restricted to the system. If he were to

---

attempt to simultaneously determine a property of the system as well as of \(O_2\) , interference effects might become important. The description of the states relative to \(O_2\) , after \(O_2\) 's observation, is non- interfering mixtures is therefore incomplete.  

Case 3: We suppose that two systems \(S_1\) and \(S_2\) are correlated but no longer interacting, and that \(O_1\) measures property A in \(S_1\) , and \(O_2\) property B in \(S_2\) .  

We wish to see whether \(O_2\) 's intervention with \(S_2\) can in any way affect \(O_1\) 's results in \(S_1\) , so that perhaps signals might be sent by these means. We shall assume that the initial state for the system pair is  

\[(\pmb {4.5}) \qquad \psi^{s_1,s_2} = \sum_{i} a_i \phi_i^{s_1} \phi_i^{s_2}\]  

We now allow \(O_1\) to observe A in \(S_2\) , so that after this observation the total state becomes:  

\[(\pmb {4.10}) \qquad \psi^{s_1,s_2,90_2} = \sum_{i} a_i \phi_i^{s_1} s_i^{s_2} \psi_{-i}^{0_1} \psi_{-i}^{0_2} \psi_{-i}^{0_2} \psi_{-i}^{0_2} [\dots]\]  

\(O_1\) can of course continue to repeat the determination, obtaining the same result each time.  

We now suppose that \(O_2\) determines B in \(S_2\) , which results in  

\[(\pmb {4.11}) \qquad \psi^{m} = \sum_{i,j} a_i (m_j^2 \phi_i^{2}) \phi_i^{2} m_j^2 \psi_{-i}^{0_1} \psi_{-i}^{0_2} [\dots]\]  

 prácticas, we see that the intervention of \(O_2\) in the way affects \(O_1\) 's determination, since \(O_2\) is still perfectly correlated to the

---

states \(\phi_{i}\) of \(S_{i}\) , and any further observations by \(0_{4}\) will lead to the same results as the earlier observations. Thus each memory sequence for \(0_{4}\) continues without change due to \(0_{2}\) 's observation, and such a scheme could not be used to send any signals.  

Furthermore, we see that the result (4.11) is arrived at even in the case that \(0_{2}\) should make his determination before that of \(0_{4}\) . Therefore any expectations for the outcome of \(0_{4}\) 's first observation are in no way affected by whether or not \(0_{2}\) performs his observation before that of \(0_{4}\) . This is true because the expectation of the outcome for \(0_{4}\) can be computed from (4.10), which is the same whether or not \(0_{2}\) performs his measurement before or after \(0_{4}\) .  

It is therefore seen that one observer's observation upon one system of a correlated, but non- interacting pair of systems, has no effect on the remote system, in the sense that the outcome or expected outcome of any experiments by another observer on the remote system are not effected. Paradoxes like that of Einstein- Rosen- Podolsky \(^{1}\) which are concerned with such correlated, non- interacting, systems are thus easily understood in the present scheme.  

Many further combinations of several observers and systems can be easily studied in the present framework, and all questions answered by first writing down the final state for the situation with the aid of the rules 1 and 2, and then noticing the relations between the elements of the memory sequences.

---

1 Einstein [g].

---

## V. SUPPLEMENTARY TOPICS  

We have now completed the abstract treatment of measurement and observation, with the deduction that the statistical predictions of the usual form of quantum theory (Process 1) will appear to be valid to all observers. We have therefore succeeded in placing our theory in correspondence with experience, at least insofar as the ordinary theory correctly represents experience.  

We should like to emphasize that this deduction was carried out by using only the principle of superposition, and the postulate that an observation has the property that if the observed variable has a definite value in the object- system then it will remain definite and the observer will perceive this value. This treatment is therefore valid for any possible quantum interpretation of observation processes, i.e., any way in which one can interpret wave functions as describing observers, as well as for any form of quantum mechanics for which the superposition principle for states is maintained. Our abstract discussion of observation is therefore logically complete, in the sense that our results for the subjective experience of observers are correct, if there are any observers at all describable by wave mechanics.1  

In this chapter we shall consider a number of diverse topics from the point of view of our pure wave mechanics, in order to supplement the abstract discussion and give a feeling for the new viewpoint. Since we are now mainly interested in elucidating the reasonableness of the theory, we shall often restrict ourselves to plausibility arguments, rather than detailed proofs.  

## §1. Macroscopic Objects and Classical Mechanics  

In the light of our knowledge about the atomic constitution of matter, any "object" of macroscopic size is composed of an enormous number of constituent particles. The wave function for such an object is then in a space of fantastically high dimension

---

1They are, of course, vacuously correct otherwise.

---

(3N, if N is the number of particles). Our present problem is to understand the existence of macroscopic objects, and to relate their ordinary (classical) behavior in the three dimensional world to the underlying wave mechanics in the higher dimensional space.  

Let us begin by considering a relatively simple case. Suppose that we place in a box an electron and a proton, each in a definite momentum state, so that the position amplitude density of each is uniform over the whole box. After a time we would expect a hydrogen atom in the ground state to form, with ensuing radiation. We notice, however, that the position amplitude density of each particle is still uniform over the whole box. Nevertheless the amplitude distributions are now no longer independent, but correlated. In particular, the conditional amplitude density for the electron, conditioned by any definite proton (or centroid) position, is not uniform, but is given by the familiar ground state wave function for the hydrogen atom. What we mean by the statement, "a hydrogen atom has formed in the box," is just that this correlation has taken place—a correlation which insures that the relative configuration for the electron, for a definite proton position, conforms to the customary ground state configuration.  

The wave function for the hydrogen atom can be represented as a product of a centroid wave function and a wave function over relative coordinates, where the centroid wave function obeys the wave equation for a particle with mass equal to the total mass of the proton- electron system. Therefore, if we now open our box, the centroid wave function will spread with time in the usual manner of wave packets, to eventually occupy a vast region of space. The relative configuration (described by the relative coordinate state function) has, however, a permanent nature, since it represents a bound state, and it is this relative configuration which we usually think of as the object called the hydrogen atom. Therefore, no matter how indefinite the positions of the individual particles become in the total state function (due to the spreading

---

of the centroid), this state can be regarded as giving (through the centroid wave function) an amplitude distribution over a comparatively definite object, the tightly bound electron- proton system. The general state, then, does not describe any single such definite object, but a superposition of such cases with the object located at different positions.  

In a similar fashion larger and more complex objects can be built up through strong correlations which bind together the constituent particles. It is still true that the general state function for such a system may lead to marginal position densities for any single particle (or centroid) which extend over large regions of space. Nevertheless we can speak of the existence of a relatively definite object, since the specification of a single position for a particle, or the centroid, leads to the case where the relative position densities of the remaining particles are distributed closely about the specified one, in a manner forming the comparatively definite object spoken of.  

Suppose, for example, we begin with a cannonball located at the origin, described by a state function:  

\[\Psi_{[e]}(a,a,0,1)\]  

where the subscript indicates that the total state function \(\Psi\) describes a system of particles bound together so as to form an object of the size and shape of a cannonball, whose centroid is located (approximately) at the origin, say in the form of a real gaussian wave packet of small dimensions, with variance \(\Psi_{0}^{2}\) for each dimension  

If we now allow a long lapse of time, the centroid of the system will spread in the usual manner to occupy a large region of space. (The spread in each dimension after time \(t\) will be given by \(\Psi_{t}^{2} = \Psi_{0}^{2} + (\hbar^{2}t^{2} / 4\Psi_{0}^{2}m^{2})\) , where \(m\) is the mass.) Nevertheless, for any specified centroid position, the particles, since they remain in bound states, have distributions which again correspond to

---

the fairly well defined size and shape of the cönnonball. Thus the total state can be regarded as a (continuous) superposition of states  

\[\psi = \int d x_{1} y_{1} \int_{[c_{j}(x_{1}, y_{1}, \xi)]}^{[c_{j}(x_{1}, y_{1}, \xi)]} d x d y d \xi\]  

each of which ( \(\int_{[c_{j}(x_{1}, y_{1}, \xi)]}^{[\xi_{j}(x_{1}, y_{1}, \xi)]}\) ) describes a cannonball at the position \((x, y, \xi)\) . The coefficients \(a_{x y \xi}\) of the superposition then correspond to the centroid distribution.  

It is not true that each individual particle spreads independently of the rest, in which case we would have a final state which is a grand superposition of states in which the particles are located independently everywhere. The fact that they are in bound states restricts our final state to a superposition of "cannonball" states. The wave function for the centroid can therefore be taken as a representative wave function for the whole object.  

It is thus in this sense of correlations between constituent particles that definite macroscopic objects can exist within the framework of pure wave mechanics. The building up of correlations in a complex system supplies us with a mechanism which also allows us to understand how condensation phenomena (the formation of spatial boundaries which separate phases of different physical or chemical properties) can be controlled by the wave equation, answering a point raised by Schrödinger.  

Classical mechanics, also, enters our scheme in the form of correlation laws. Let us consider a system of objects (in the previous sense), such that the centroid of each object has initially a fairly well defined position and momentum (e.g. let the wave function for the centroids consist of a product of gaussian wave packets). As time progresses, the centers of the square amplitude distributions for the objects will move in a manner approximately obeying the laws of motion of classical mechanics, with the degree of approximation depending upon the masses and the length of time considered, as is well known. (Note that we do not mean to imply that the wave packets of the individual objects remain

---

nagwont) 3anivv en hohrngav an nao avas anh (hohrton anh to  -mo a tavn notanitvtaeb abuntlqna na (notron) yaw hohrton anh  -ava notron-monton le hwod vintnht anh, troton atintah vavtntan  hwa alqna va adroab ton aobh, nonh, sstta lantang anh.  ma  toqdo anh nih waoa noa to notronqvan a an, troton stnteb  -anobt noq tawqatn, ba hstaoi  ad nao atoqdo xalqno aon haa xaqna noqatn anhna a ni  -naw anotatlon to qvita nqwont anqont qa tlan  -1 schrödinger [18].  anh anh tlan a ni.  -aotatran notnita  to anqtanah notatav lantqtan oa basi yan nqta a noa not  anotqan aqna tavn hqta na (hohron to) atotran alqna va  -anor a to anqtan a anh to waoa nao. aw aatantran  -aog alqna a to notatnqtona anh anha, troton atntah vavt  anh awan aao anh oa abat, hohrton anh to atatran a to not  -ntatah a aatqtan, qntnqtan anh to aatatna notatq atatq  -no anqtanat qanma a ni, ano hqtona anh qanq vlaoao hqton  -to naoqa oaqde oqntan anh vavtran  -a hqtona lantqna a nih nqna a, alqna a to aonqna  -notatn anh ava a od anqna, nqnto anh 

-ah  "nohtonh oqta lqto anh tanh aatqotnq qqtona anh qanq  toqdo na qto aq oa qonqtoq hnoq aqotnq to qqtaqa a qadqta  hqtoq aq toqtona aqonq, lqtonqna a to aqna hna aqta anh to  qqtaqa lqto a to qqto anh qqta, nqtonq aq to  (qotantqtonqa)  -noqnaqah qna to  "qonqtan qih qanqnaqah lqna to qqtoq aqwa  -ava anh to hqtonq aqta, aqah to aqaq qnoi a qoia aq to aq  to qqtoq aqta a qqnoq oa qanq qqta aqta anh hqtona lqih qqto  qoqta aq qih qqta qqtona qqtoq aqta aqta aqta  qqtoq aqta aqta aqta aqta aqta aqta aqta a qqtoq aqta aqta aqta aqta aqta  aqta aqta aqta aqta aqta aqta aqa aqta aqta aqta aqta aqta aqta a  qqtoq aqta aqta aqta aqta aqtoq aqta aqta aqta aqta aqta a qqtoa aqta aqta aqta aqta aqta aqta a aqta aqta aqta aqta aqta aqta a 

To notqan aqta a qqnoq oa qanq qqta aqta aqta aqta aqta aqta aqtoq aqta  aqta aqta aqta aqta aqta  aqta  aqta aqta aqta aqta aqta

---

independent if they are interacting. They do not. The motion that we refer to is that of the centers of the marginal distributions for the centroids of the bodies.)  

The general state of a system of macroscopic objects does not, however, ascribe any nearly definite positions and momenta to the individual bodies. Nevertheless, any general state can at any instant be analyzed into a superposition of states each of which does represent the bodies with fairly well defined positions and momenta. Each of these states then propagates approximately according to classical laws, so that the general state can be viewed as a superposition of quasi- classical states propagating according to nearly classical trajectories. In other words, if the masses are large or the time short, there will be strong correlations between the initial (approximate) positions and momenta and those at a later time, with the dependence being given approximately by classical mechanics.  

Since large scale objects obeying classical laws have a place in our theory of pure wave mechanics, we have justified the introduction of models for observers consisting of classically describable, automatically functioning machinery, and the treatment of observation of Chapter IV is non- vacuous.  

Let us now consider the result of an observation (considered along the lines of Chapter IV) performed upon a system of macroscopic bodies in a general state. The observer will not become aware of the fact that the state does not correspond to definite positions and momenta (i.e. he will not see the objects as "smeared out" over large regions of space) but will himself simply become correlated with the system - - after the observation the composite system of objects - observer will be in a superposition of states, each element of which describes an observer who has perceived that the objects have nearly definite positions and momenta, and for whom the relative system state is a quasi- classical state in the

---

aum. iLendonno aat to aane ina eae banteb iLaw vnlaat aat
to nolionogga (eounidneo) a ea bonagat a en aea aat aat aat aat aat aat aat aat aat aat a 

nobtlaog aat a a Lendonno a aoblaog (  ) nolaw to naa
-aatno nol aoblaogga aat a a a a a a a a a a a a a a a a a a a a 

nobtlaobtaeb nolotnao aat a at nong
-nagobn aabonaa aobtaag laabnvan nnaa aat aat aon a at a
nobn aataa laan a aan nlaow a aaa nolaw a aaan aat a a a a a a a a a a a a a a a a a

---

previous sense, and furthermore to whom the system will appear to behave according to classical mechanics if his observation is continued. We see, therefore, how the classical appearance of the macroscopic world to us can be explained in the wave theory.  

## §2. Amplification Processes.  

In Chapter III and IV we discussed abstract measuring processes, which were considered to be simply a direct coupling between two systems, the object- system and the apparatus (or observer). There is, however, in actuality a whole chain of intervening systems linking a microscopic system to a macroscopic observer. Each link in the chain of intervening systems becomes correlated to its predecessor, so that the result is an amplification of effects from the microscopic object- system to a macroscopic apparatus, and then to the observer.  

The amplification process depends upon the ability of the state of one micro- system (particle, for example) to become correlated with the states of an enormous number of other microscopic systems, the totality of which we shall call a detection system. For example, the totality of gas atoms in a Geiger counter, or the water molecules in a cloud chamber, constitute such a detection system.  

The amplification is accomplished by arranging the condition of the detection system so that the states of the individual micro- systems of the detector are metastable, in a way that if one micro- system should fall from its metastable state it would influence the reduction of others. This type of arrangement leaves the entire detection system metastable against chain reactions which involve a large number of its constituent systems. In a Geiger counter, for example, the presence of a strong electric field leaves the gas atoms metastable against ionization. Furthermore, the products of the ionization of one gas atom in a Geiger counter can cause further ionizations, in a cascading process. The operation of cloud chambers

---

and photographic films is also due to metastability against such chain reactions.  

The chain reactions cause large numbers of the micro- systems of the detector to behave as a unit, all remaining in the metastable state, or all discharging. In this manner the states of a sufficiently large number of micro- systems are correlated, so that one can speak of the whole ensemble being in a state of discharge, or not.  

For example, there are essentially only two macroscopically distinguishable states for a Geiger counter; discharged or undischarged. The correlation of large numbers of gas atoms, due to the chain reaction effect, implies that either very few, or else very many of the gas atoms are ionized at a given time. Consider the complete state function \(\psi^{\mathrm{g}}\) of a Geiger counter, which is a function of all the coordinates of all of the constituent particles. Because of the correlation of the behavior of a large number of the constituent gas atoms, the total state \(\psi^{\mathrm{g}}\) can always be written as a superposition of two states  

\[{\psi^{\mathrm{g}} = a_{\mathrm{a}}\frac{\psi^{2}}{[\mathrm{u}]} +a_{\mathrm{a}}\frac{\psi^{2}}{[\mathrm{D}]}} \quad (2.1)\]  

where \(\psi_{\mathrm{uJ}}^{2}\) signifies a state where only a small number of gas atoms are ionized, and \(\psi_{\mathrm{DJ}}^{2}\) a state for which a large number are ionized.  

To see that the decomposition (2.1) is valid, expand \(\psi^{\mathrm{g}}\) in terms of individual gas atom stationary states:  

\[\psi^{\mathrm{g}} = \sum_{i = 1}^{n}a_{i j \dots k}\psi_{i}^{s_{2}}\psi_{j}^{s_{2}}\dots \psi_{k}^{s_{n}} \quad (2.2)\]  

where \(\psi_{2}^{s_{r}}\) is the \(Q^{\mathrm{th}}\) state of atom \(r\) . Each element of the superposition (2.2)  

\[\psi_{i}^{s_{2}}\psi_{j}^{s_{2}}\dots \psi_{\mathrm{k}}^{s_{m}} \quad (2.3)\]  

must contain either a very large number of atoms in ionized states,

---

or else a very small number, because of the chain reaction effect. By choosing some medium- sized number as a dividing line, each element of (2.2) can be placed in one of the two categories, high number of low number of ionized atoms. If we then carry out the sum (2.2) over only those elements of the first category, we get a state (and coefficient)  

\[a_{1}^{\psi_{1}^{1}} = \sum_{i,j,k}\alpha_{i,j,k}^{\psi_{1}^{1}}\psi_{j}^{s_{1}}\psi_{k}^{s_{2}}\dots \psi_{k}^{s_{m}} \quad (2.4)\]  

The state \(\frac{\psi_{1}^{1}}{[0]}\) is then a state where a large number of particles are ionized. The subscript \([D]\) indicates that it describes a Geiger counter which has discharged. If we carry out the sum over the remaining terms of (2.2) we get in a similar fashion:  

\[a_{2}\frac{\psi_{1}^{2}}{[U]} = \sum_{i,j,k}\alpha_{i,j,k}^{\psi_{1}^{2}}\psi_{j}^{s_{1}}\psi_{k}^{s_{2}}\dots \frac{\psi_{k}^{s_{m}}}{k} \quad (2.5)\]  

where \([U]\) indicates the undischarged condition. Combining (2.4) and (2.5) we arrive at the desired relation (2.1). So far, this method of decomposition can be applied to any system, whether or not it has the chain reaction property. However, in our case, more is implied, namely that the spread of the number of ionized atoms in both \(\frac{\psi_{1}^{2}}{[0]}\) and \(\frac{\psi_{1}^{2}}{[U]}\) will be small compared to the separation of their averages, due to the fact that the existence of the chain reactions means that either many or else few atoms will be ionized, with the middle ground virtually excluded.  

This type of decomposition is also applicable to all other detection devices which are based upon this chain reaction principle (such as cloud chambers, photo plates, etc.).  

We consider now the coupling of such a detection device to another micro- system (object- system) for the purpose of measurement. If it is true that the initial object- system state \(\phi_{1}\) will at some time \(t\) trigger the chain reaction, so that the state of the counter becomes \(\frac{\psi_{1}^{1}}{[D]}\) , while the object- system state \(\phi_{2}\) will

---

not, then it is still true that the initial object- system state \(\alpha_{1} \phi_{1} + \alpha_{2} \phi_{2}\) will result in the superposition  

\[a_{1} \phi_{1} \psi_{[0]}^{4} + a_{2} \phi_{2}^{4} \psi_{[U]}^{4} \quad (2.6)\]  

at time t.  

For example, let us suppose that a particle whose state is a wave packet \(\phi\) , of linear extension greater than that of our Geiger counter, approaches the counter. Just before it reaches the counter it can be decomposed into a superposition \(\phi = a_{1} \phi_{1} + a_{2} \phi_{2}\) ( \(\phi_{1}\) , \(\phi_{2}\) orthogonal) where \(\phi_{1}\) has non- zero amplitude only in the region before the counter and \(\phi_{2}\) has non- zero amplitude elsewhere (so that \(\phi_{1}\) is a packet which will entirely pass through the counter while \(\phi_{2}\) will entirely miss the counter). The initial total state for the system particle \(\phi\) counter is then:  

\[\phi \psi_{[U]} = (a_{1} \phi_{1} + a_{2} \phi_{2}) \psi_{[U]}\]  

where \(\psi_{[U]}\) is the initial (assumed to be discharged) state of the counter.  

But at a slightly later time \(\phi_{1}\) is changed to \(\phi_{1}^{\prime}\) , after traversing the counter and causing it to go into a discharged state \(\psi_{[0]}^{4}\) , while \(\phi_{2}\) passes by into a state \(\phi_{2}^{\prime \prime}\) leaving the counter in an undischarged state \(\psi_{[U]}^{2}\) . Superposing these results, the total state at the later time is  

\[a_{1} \phi_{1}^{\prime} \psi_{[0]}^{4} + a_{2} \phi_{2}^{\prime \prime} \psi_{[U]}^{2} \quad (2.7)\]  

in accordance with (2.6). Furthermore, the relative particle state for \(\psi_{[0]}^{4}\) , \(\phi_{2}^{\prime \prime}\) , is a wave packet emanating from the counter, while the relative state for \(\psi_{[U]}^{2}\) is a wave with a "shadow" cast by the counter. The counter therefore serves as an apparatus which performs an approximate position measurement on the particle.

---

No matter what the complexity or exact mechanism of a measuring process, the general superposition principle as stated in Chapter III, §3, remains valid, and our abstract discussion is unaffected. It is a vain hope that somewhere embedded in the intricacy of the amplification process is a mechanism which will somehow prevent the macroscopic apparatus state from reflecting the same indefiniteness as its object- system.  

## §3. Reversibility and Irreversibility  

Let us return, for the moment, to the probabilistic interpretation of quantum mechanics based on Process 1 as well as Process 2. Suppose that we have a large number of identical systems (ensemble), and that the \(j^{\text{th}}\) system is in the state \(\psi^{j}\) . Then for purposes of calculating expectation values for operators over the ensemble, the ensemble is represented by the mixture of states \(\psi^{j}\) weighted with \(1 / N\) , where \(N\) is the number systems, for which the density operator \(i\)  

\[\mathcal{P} = \frac{1}{N}\sum_{j}\left[\psi^{j}\right]\]  

where \(\left[\psi^{j}\right]\) denotes the projection operator on \(\psi^{j}\) . This density operator, in turn, is equivalent to a density operator which is a sum of projections on orthogonal states (the eigenstates of \(\rho\) ):  

\[\mathcal{P} = \sum_{i}\mathcal{P}_{i}\left[\mathcal{N}_{i}\right],\quad (\mathcal{N}_{i},\mathcal{N}_{j}) = \delta_{i,j},\quad \sum_{i}\mathcal{P}_{i} = \mathbb{1} \quad (3.2)\]  

so that any ensemble is always equivalent to a mixture of orthogonal states, which representation we shall henceforth assume.  

Suppose that a quantity \(A\) , with (non- degenerate) eigenstates \(\{\phi_{j}\}\) is measured in each system of the ensemble. This measurement has the effect of transforming each state \(\mathcal{N}_{i}\) into the state \(\phi_{j}\) , with probability \(|\langle \phi_{j}, \mathcal{N}_{i} \rangle |^{2}\) ; i.e., it will transform a large ensemble of systems in the state \(\mathcal{N}_{i}\) into an ensemble represented by the mixture whose density operator is \(\sum_{j} |\langle \phi_{j}, \mathcal{N}_{i} \rangle |^{2} [\phi_{j}]\) . Extending this result to the case where the original ensemble is a mixture of the \(\mathcal{N}_{i}\) weighted by \(\mathcal{P}_{i}\) ((3.2)), we find that the density operator \(\mathcal{P}\) is

---

στάσε μεσφε-τοσέδο λάβησι αύτ' σαπί στίς έλία αύ τίς σαπί τίσον
ποτέσαρχημε αύτ' ήί τίσον έλία 

(0.5) 

, σ' αύτί τά 

α. ει στάσε σασίν σάτισάσε σάτισάσε σασίν σάτισάσε σάτισάσε σάτισάσε σάτισάσε σασίν σάτι σάτισάσε σάτισάσε σάτισάσε σ ασίν σάτισάσε σάτισάσε σάτισάσει σάτισάσει σάτισάσει σάτισάσει σασίν σάτισάσει σάτισάσει σάτισάσει σ ασίν σάτισάσει σάτισάσει σάτισάσε σάτισάσει σάτισάσει σασίν σάτι σάτισάσει σάτισάσει σάτισάσει σ άσίν σάτισάσει σάτισάσει σάτισάσεις σάτισάσεις σάτισάσεις σάτισάσεις σ άσίν σάτισάσεις σάτισάσεις σάτισάσεις σ ασίν σάτισάσεις σάτισάσεις σάτισάσει σάτισάσεις σάτισάσεις σ άσίν σάτι σάτισάσεις σάτισάσεις σάτισάσεις σασίν σάτι σάτισάσεις σάτισάσεις σάτίσάσεις σάτισάσεις σάτισάσεις σάτισασεις σάτισάσεις σάτισάσεις σάτισάσεις 

σάτι σάτι σάτι σάτι σάτι σάτι σάτι σάτίσάτι σάτι σάτι σάτι σάτι σάτίσάτίσάτίσάτίσάτίσάτίσάτίσάτισάτίσάτίσάτίσάτίσάτίσάτίσατίσάτίσάτίσάτίσάτίσάτίσάτί σάτίσάτίσάτίσάτίσάτίσάτίσαίσάτίσάτίσάτίσάτίσάτίσάτίσ ατίσάτίσάτίσάτίσάτίσάτίσάτίατίσάτίσάτίσάτίσάτίσάτίσάτι σάτίσάτίσάτίσάτίσάτίσάτι σάτισάτίσάτίσάτίσάτίσάτίσάτι σατίσάτίσάτίσάτίσάτίσάτίσάτ ίσάτίσάτίσάτίσάτίσάτίσάτίσ άτίσάτίσάτίσάτίσάτίσάτίσάτί ατίσάτίσάτίσάτίσάτίσάτίσάτι ατίσάτίσάτίσάτίσάτίσάτίσάτ ισάτίσάτίσάτίσάτίσάτίσάτίσ ισάτίσάτίσάτίσάτίσάτίσάτί σατίσάτίσάτίσάτίσάτίσάτίσ ατί σάτίσάτίσάτίσάτίσάτίσάτί σάτισάτίσάτίσάτίσάτίσάτί σάτίσ άτίσάτίσάτίσάτίσάτίσάτι σάτί σάτίσάτίσάτίσάτίσάτί σάτί σάτίσάτίσάτίσάτίσάτί σατί σάτίσάτίσάτίσάτίσάτί σάτίσάτι σάτίσάτίσάτίσάτίσάτι σάτί σάτισάτίσάτίσάτίσάτί σάτί σάτίσ άτίσάτίσάτίσάτίσάτι σάτί σάτί σάτίσάτίσάτίσάτί σάτί σάτίσάτι σάτίσάτίσάτίσάτι σάτί σάτί σάτισάτίσάτίσάτίσάτί σατί σάτί σάτίσάτίσάτίσάτί σάτίσάτί σάτίσάτίσάτίσάτί σάτί σάτισάτίσάτίσάτίσάτι σάτί σάτί σατίσάτίσάτίσάτίσάτί σάτί σάτί σάτίσάτίσάτίσάτί σατί σάτί σάτισάτίσάτίσάτίσάτίσάτι σάτί σατί σάτίσάτίσάτίσάτίσάτι σάτί σαίσάτίσάτίσάτίσάτίσάτί σάτί σάτι σάτίσάτίσάτίσάτίσάτί σάτί σατί σάτίσάτίσάτίσάτίσατί σάτί σάτίσάτίσάτίσάτίσάτίσάτι σαίσάτίσάτίσάτίσάτίσάτί σατί σάτι σάτίσάτίσάτίσάτίσάτίσατί σάτί σάτισάτίσάτίσάτίσάτισάτί σάτί σάτίσάτίσάτίσάτίσατί σάτίσάτίσάτίσάτίσάτί σάτι σάτί σάτίσάτίσάτίσάτίσάτι σάτίσάτι σάτίσάτίσάτίσάτίσατί σάτί σατίσάτίσάτίσάτίσάτίσάτι σάτί ατίσάτίσάτίσάτίσάτίσάτί σάτί σαίσάτίσάτίσάτίσάτίσατί σάτί σαίσάτίσάτίσάτίσάτί σάτί σάτί σατίσάτίσάτίσάτίσατί σάτί σατί σάτίσάτίσάτίσάτί σάτί σάτί σάτισάτίσάτίσάτίσατί σάτί σατί σατίσάτίσάτίσάτίσάτί σάτί ατίσάτίσάτίσάτίσάτίσάτι σάτί άτίσάτίσάτίσάτίσάτίσάτί σάτί άτίσάτίσάτίσάτίσάτίσάτι σάτι άτίσάτίσάτίσάτίσάτίσάτί σάτι άτίσάτίσάτίσάτίσάτίσάτι σάντί σάτίσάτίσάτίσάτίσάτίσάτί σαντί σάτίσάτίσάτίσάτίσάτίσάτί ατί σάτίσάτίσάτίσάτίσάτίσάτι ατί σάτίσάτίσάτίσάτίσάτίσάίσάτίσάτίσάτίσάτίσάτίσάτί σ ατί σάτίσάτίσάτίσάτίσάτίσάτ ίσ άτίσάτίσάτίσάτίσάτίσάτίσ άτί σάτίσάτίσάτίσάτίσάτίσάτί αίσάτίσάτίσάτίσάτίσάτίσάτί αί σάτίσάτίσάτίσάτίσάτίσάτί σ αί σάτίσάτίσάτίσάτίσάτίσάτι σ αί σάτίσάτίσάτίσάτίσάτίσατί σ αί σάτίσάτίσάτίσάτίσάτί σάτί σ αί σάτίσάτίσάτίσάτίσάτι σάτί σ αί σάτίσάτίσάτίσάτίσατί σάτί σ αί σάτίσάτίσάτίσάτί σάτί σ αί σάτισάτίσάτίσάτίσάτίσάτί σ αί σ αί σάτίσάτίσάτίσάτίσάτί σ αί σ α ί σάτίσάτίσάτίσάτίσάτίσάτί σ άί σάτίσάτίσάτίσάτίσάτίσάτίσ άί σάτίσάτίσάτίσάτίσάτίσάτι αί σάτίσάτίσάτίσάτίσάτίσάίσ άί σάτίσάτίσάτίσάτίσάτίσ άί σάί σάτίσάτίσάτίσάτίσάτίσάτί α ί σάτίσάτίσάτίσάτίσάτίσάί σάτί σάτίσάτίσάτίσάτίσάτί σ αί σάί σάτίσάτίσάτίσάτίσάτί σάτί αί σάτίσάτίσάτίσάτίσάτί σάί σάτί σάτίσάτίσάτίσάτίσάί σάτί σάί σάτίσάτίσάτίσάτίσάτί σ αί αί σάτίσάτίσάτίσάτίσάτίσά ί σάτίσάτίσάτίσάτίσάτίσάτίσ αί σάτί σάτίσάτίσάτίσάτίσάτίσ άί σ άί σάτίσάτίσάτίσάτίσάτίσ ά ί σάτίσάτίσάτίσάτίσάτίσάτί α ι σάτίσάτίσάτίσάτίσάτίσάτί σ áτί σάτίσάτίσάτίσάτίσάτίσάτί άί σάτί σάτίσάτίσάτίσάτίσάτί αί σάτί σάτίσάτίσάτίσάτίσάίσ άί σάί σάτίσάτίσάτίσάτίσ άί σάτί σάτίσάτίσάτίσάτίσάί αί σάτί σάτίσάτίσάτίσάτίσάτι σ άί σάτίσάτίσάτίσάτίσάτίσ αί σάί σάτίσάτίσάτίσάτίσάί σάί σάτί σάτίσάτίσάτίσάτίσ άί σάτί σ άτίσάτίσάτίσάτίσάτίσάτί σάί σάί σάτίσάτίσάτίσάτίσάτί αί σάί σάτίσάτίσάτίσάτίσάτι σάί σάί σάτίσάτίσάτίσάτίσ άί αί σάτίσάτίσάτίσάτίσάτίσ άί αί σάτί σάτίσάτίσάτίσάτίσ άί αί σάί σάτίσάτίσάτίσάτίσά ί σάτί σάτίσάτίσάτίσάτίσάτί σ άί σάί σάτίσάτίσάτίσάτίσάί αί σάί σάτίσάτίσάτίσάτίσ άί άί σάτίσάτίσάτίσάτίσάτίσάί σ άί σάτίσάτίσάτίσάτίσάτί σάί αί σάτίσάτίσάτίσάτίσάτίσ αί αί σάτίσάτίσάτίσάτίσάτί σά ί σάτίσάτίσάτίσάτίσάτίσάί αί σάτίσάτίσάτίσάτίσάτί σ άί σ άί σάτίσάτίσάτίσάτίσάί σ άί σ άί σάτίσάτίσάτίσάτίσ άί αί σ άί σάτίσάτίσάτίσάτίσάί αί σ άί σάτίσάτίσάτίσάτίσ άί σ άί σ άί σάτίσάτίσάτίσάτί σ άί αί σ άί σάτίσάτίσάτίσάτί σ άί σ άί σ άί σάτίσάτίσάτίσάί σ άί αί σ άί σάτίσάτίσάτίσάί σ άί σ άί σ άί σάτίσάτίσάτίσ άί αί σ άί σ άί σ άί σάτίσάτίσάτί σ άί αί σ άί σ άί σ άί σ άί σ άί σ άί σ άί αί σ άί σ άί σ άί σ άί σ ά ί σ άί σ άί σ άί σ άί σ άί σ άί σάί σ άί σ άί σ άί σ άί σ άί σ άί

---

transformed by the measurement of \(A\) into the new density operator \(f^{\prime}\)  

\[f^{\prime} = \sum_{i}\mathfrak{f}_{i}\sum_{j}\mathbb{I}\{(\mathfrak{n}_{i},\phi_{j})\}^{2}[\phi_{j}] = \sum_{j}\big(\sum_{i}\mathfrak{f}_{i}\big(\phi_{j},(\mathfrak{n}_{i},\phi_{j})\mathfrak{n}_{i}\big)\big)[\phi_{j}]\] \[\qquad = \sum_{j}\big(\phi_{j}\big)\sum_{i}\mathfrak{f}_{i}\big[\mathfrak{n}_{i}\big]\phi_{j}\big)\big[\phi_{j}\big] = \sum_{j}\big(\phi_{j},\mathfrak{f}\phi_{j}\big)\big[\phi_{j}\big]\]  

This is the general law by which mixtures change through Process 1.  

However, even when no measurements are taking place, the states of an ensemble are changing according to Process 2, so that after a time interval t each state \(\psi\) will be transformed into a state \(\psi^{\prime} = \cup_{t}\psi\) , where \(\cup_{t}\) is a unitary operator. This natural motion has the consequence that each mixture \(f = \sum_{i}\mathfrak{f}_{i}[\mathfrak{n}_{i}]\) is carried into the mixture \(f^{\prime} = \sum_{i}\mathfrak{f}_{i}[\cup_{t}\mathfrak{n}_{i}]\) after a time \(t\) . But for every state \(\mathfrak{f}\) ,  

\[f^{\prime}\mathfrak{f} = \sum_{i}\mathfrak{f}_{i}[\cup_{t}\mathfrak{n_{i}}]^{\mathfrak{f}} = \sum_{i}\mathfrak{f}_{i}(\cup_{t}\mathfrak{n_{i}},\mathfrak{f})\cup_{t}\mathfrak{n_{i}}\] \[\qquad = \cup_{t}\sum_{i}\mathfrak{f}_{i}(\mathfrak{n_{i}},\cup_{t}^{-1}\mathfrak{f})\mathfrak{n_{i}} = \cup_{t}\sum_{i}\mathfrak{f}_{i}[\mathfrak{n_{i}}](\cup_{t}^{-1}\mathfrak{f})\] \[\qquad = (\cup_{t}\mathfrak{f}\cup_{t}^{-1})\mathfrak{f}\]  

Therefore  

\[f^{\prime} = \cup_{t}\mathfrak{f}\cup_{t}^{-1}\]  

which is the general law for the change of a mixture according to Process 2.  

We are now interested in whether or not we get from any mixture to another by means of these two processes, i.e., if for any pair \(f, f^{\prime}\) , there exist quantities \(A\) which can be measured and unitary (time dependence) operators \(U\) such that \(f\) can be transformed into \(f^{\prime}\) by suitable applications of Processes 1 and 2. We shall see that this is not always possible, and that Process 1 can cause irreversibility changes in mixtures.  

For each mixture \(f\) we define a quantity \(I_{f}\) :  

\[I_{f} = \mathrm{Trace}\left(f\ln f\right) \quad (3.6)\]  

This number, \(I_{f}\) , has the character of information. If \(f = \sum_{i}\mathfrak{f}_{i}[\mathfrak{n}_{i}]^{\prime}\) ,

---

a mixture of orthogonal states \(N_{x}\) weighted with \(\mathcal{P}_{x}\) , then \(\mathcal{I}_{\mathcal{P}}\) is simply the information of the distribution \(\mathcal{P}_{x}\) over the eigenstates of \(\mathcal{P}\) (relative to the uniform measure). (Trace \((\mathcal{P}\mathcal{M}\mathcal{P})\) is a unitary invariant and is proportional to the negative of the entropy of the mixture, as discussed in Chapter III, § 2.)  

Process 2 therefore has the property that it leaves \(\mathcal{I}_{\mathcal{P}}\) unchanged, because  

\[I_{\mathcal{P}}^{\prime} = \mathrm{Trace}\left(\mathcal{P}^{\prime}\mathcal{M}\mathcal{P}^{\prime}\right) = \mathrm{Trace}\left(\mathcal{U}_{\mathcal{P}}\mathcal{S}\mathcal{U}_{\mathcal{P}}^{-1}\mathcal{M}\mathcal{U}_{\mathcal{P}}\mathcal{S}\mathcal{U}_{\mathcal{P}}^{-1}\right)\] \[\qquad = \mathrm{Trace}\left(\mathcal{U}_{\mathcal{P}}\mathcal{S}\mathcal{U}_{P}\mathcal{U}_{\mathcal{P}}^{-1}\right) = \mathrm{Trace}\left(\mathcal{P}\mathcal{M}\mathcal{P}\right) = \mathcal{I}_{\mathcal{P}}^{\prime}\]  

Process 1, on the other hand, can decrease \(\mathcal{I}_{\mathcal{P}}\) but never increase it. According to (3.3)  

\[{\mathcal{P}}^{\prime}=\sum_{i,j}(\phi_{i,j}^{\prime}\mathcal{P}\phi_{i}^{\prime})[\phi_{i}^{\prime}]=\sum_{i,j}\mathcal{P}_{i}\left|(\mathcal{n}_{i,j}\phi_{i}^{\prime})\right|^{2}[\phi_{i}^{\prime}]\] \[=\sum_{i,j}\mathcal{P}_{i}^{\prime}[\phi_{i}^{\prime}]\]  

where \(\begin{array}{r}{\mathcal{P}_{i}^{\prime} = \sum_{i}\mathcal{P}_{i}\mathrm{T}_{i j}} \end{array}\) and \(\begin{array}{r}{\mathrm{T}_{i j} = |(\mathcal{n}_{i,j}\phi_{i}^{\prime})|^{2}} \end{array}\) is a doubly- stochastic matrix.3 But \(\begin{array}{r}{\mathcal{I}_{\mathcal{P}}^{\prime} = \sum_{i}\mathcal{P}_{i}^{\prime}\mathcal{M}_{i}\mathcal{P}_{i}^{\prime}} \end{array}\) and \(\begin{array}{r}{\mathcal{I}_{\mathcal{P}} = \sum_{i}\mathcal{P}_{i}\mathcal{M}_{i}\mathcal{P}_{i}} \end{array}\) , with the \(\mathcal{P}_{i,j}\mathcal{P}_{i}^{\prime}\) connected by \(\mathrm{T}_{i,j}\) , implies by the theorem of information decrease for stochastic processes (II- §6) that:  

\[\mathcal{I}_{\mathcal{P}}^{\prime} \triangleq \mathcal{I}_{\mathcal{P}}^{\prime}\]  

Moreover, it can easily be shown by a slight strengthening of the theorems of Chapter II, §6 that strict inequality must hold unless (for each \(i\) such that \(\mathcal{E}_{i} > 0\) ) \(\mathrm{T}_{i j} = 1\) for one \(j\) and 0 for the rest \((\mathrm{T}_{i j} = \delta_{i k j})\) . This means that \(|(\mathcal{M}_{i,j}\phi_{i}^{\prime})|^{2} = \delta_{i k j}\) , which implies that the original mixture was already a mixture of eigenstates of, the measurement.  

We have answered our question, and it is not possible to get from any mixture to another by means of Processes 1 and 2. There is an essential irreversibility to Process 1, since it corresponds

---

4. Togstvago vrisesb wan est esti A. Tis stnagorvaean est vd benoozesat 

\[
\begin{align*}
\sum_{i=1}^{n} \sum_{j=1}^{n} \sum_{k=1}^{n} \sum_{l=1}^{n} \sum_{m=1}^{n} \sum_{p=1}^{n} \sum_{q=1}^{n} \sum_{r=1}^{n} \sum_{s=1}^{n} \sum_{t=1}^{n} \sum_{u=1}^{n} \sum_{v=1}^{n} \sum_{w=1}^{n} \sum_{x=1}^{n} \sum_{y=1}^{n} \sum_{z=1}^{n} \sum_{a=1}^{n} \sum_{b=1}^{n} \sum_{c=1}^{n} \sum_{d=1}^{n} \sum_{e=1}^{n} \sum_{f=1}^{n} \sum_{g=1}^{n} \sum_{h=1}^{n} \sum_{i=1}^{n} \sum_{j=1}^{n} \sum_{l=1}^{n} \sum_{m=2}^{n} \sum_{n=1}^{n} \sum_{o=1}^{n} \sum_{p=1}^{n} \sum_{q=2}^{n} \sum_{r=1}^{n} \sum_{s=2}^{n} \sum_{t=1}^{n} \sum_{u=2}^{n} \sum_{v=1}^{n} \sum_{w=2}^{n} \sum_{x=1}^{n} \sum_{y=2}^{n} \sum_{z=1}^{n} \sum_{a=2}^{n} \sum_{b=1}^{n} \sum_{c=2}^{n} \sum_{d=1}^{n} \sum_{e=2}^{n} \sum_{f=1}^{n} \sum_{g=2}^{n} \sum_{h=1}^{n} \sum_{i=2}^{n} \sum_{j=1}^{n} \sum_{l=2}^{n} \sum_{m=2}^{n} \sum_{n=2}^{n} \sum_{o=1}^{n} \sum_{p=2}^{n} \sum_{q=2}^{n} \sum_{r=2}^{n} \sum_{s=2}^{n} \sum_{t=2}^{n} \sum_{u=2}^{n} \sum_{v=2}^{n} \sum_{x=2}^{n} \sum_{y=2}^{n} \sum_{z=2}^{n} \sum_{a=2}^{n} \sum_{b=2}^{n} \sum_{c=2}^{n} \sum_{d=2}^{n} \sum_{e=2}^{n} \sum_{f=2}^{n} \sum_{g=2}^{n} \sum_{h=2}^{n} \sum_{i=2}^{n} \sum_{j=2}^{n} \sum_{l=2}^{n} \sum_{m=2}^{2} \sum_{n=2}^{2} \sum_{o=1}^{2} \sum_{p=2}^{2} \sum_{q=2}^{2} \sum_{r=2}^{2} \sum_{s=2}^{2} \sum_{t=2}^{2} \sum_{u=2}^{2} \sum_{v=2}^{2} \sum_{x=2}^{2} \sum_{y=2}^{2} \sum_{z=2}^{2} \sum_{a=2}^{2} \sum_{b=2}^{2} \sum_{c=2}^{2} \sum_{d=2}^{2} \sum_{e=2}^{2} \sum_{f=2}^{2} \sum_{g=2}^{2} \sum_{h=2}^{2} \sum_{i=2}^{2} \sum_{j=2}^{2} \sum_{l=2}^{2} \sum_{m=2}^{2} \sum_{n=2}^{2} 
\]

1. Benoozl dnoozis eganis aovnusik nisiv vd vat ksenes gis es aint
gatsa gis, eoozis gisas es aovnusik on nisiv vovn
is gatsa gis on, 2. Benoozis ois gisusis gis gis aovnusik is
gatsa 3. ois benoozisat on isiv gatsa gis on
asd noozis ksenes aint. ooozis gatsa 4. aint gatsa
isiv gis on gis ksenes. 

\[
\sum_{i=1}^{n} \sum_{j=1}^{n} \sum_{\ell=1}^{n} \sum_{m=1}^{n} \sum_{p=2}^{n} \sum_{q=1}^{n} \sum_{r=1}^{m} \sum_{s=1}^{n} \sum_{t=1}^{n} = \sum_{i=1}^{n} \sum_{j=1}^{n} \left( \sum_{k=1}^{n} \sum_{l=1}^{n} \right) = \sum_{i=1}^{n} \sum_{j=1}^{n} 1 = \sum_{i=1}^{n} \sum_{j=1}^{n} n = \sum_{i=1}^{n} \sum_{j=1}^{n} i = \sum_{i=1}^{n} \sum_{j=1}^{n} j = \sum_{i=1}^{n} \sum_{j=1}^{n} k = \sum_{i=1}^{n} \sum_{j=1}^{n} l = \sum_{i=1}^{n} \sum_{j=1}^{n} m = \sum_{i=1}^{n} \sum_{j=1}^{n} p = \sum_{i=1}^{n} \sum_{j=1}^{n} q = \sum_{i=1}^{n} \sum_{j=1}^{n} r = \sum_{i=1}^{n} \sum_{j=1}^{n} s = \sum_{i=1}^{n} \sum_{j=1}^{n} t = \sum_{i=1}^{n} \sum_{j=1}^{n} u = \sum_{i=1}^{n} \sum_{j=1}^{n} v = \sum_{i=1}^{n} \sum_{j=1}^{n} x = \sum_{i=1}^{n} \sum_{j=1}^{n} y = \sum_{i=1}^{n} \sum_{j=1}^{n} z = \sum_{i=1}^{n} \sum_{j=1}^{n} a = \sum_{i=1}^{n} \sum_{j=1}^{n} b = \sum_{i=1}^{n} \sum_{j=1}^{n} c = \sum_{i=1}^{n} \sum_{j=1}^{n} d = \sum_{i=1}^{n} \sum_{j=1}^{n} e = \sum_{i=1}^{n} \sum_{j=1}^{n} f = \sum_{i=1}^{n} \sum_{j=1}^{n} g = \sum_{i=1}^{n} \sum_{j=1}^{n} h = \sum_{i=1}^{n} \sum_{j=1}^{n}

---

to a stochastic process, which cannot be compensated by Process 2, which is reversible, like classical mechanics. \(^{4}\)  

Our theory of pure wave mechanics, to which we now return, must give equivalent results on the subjective level, since it leads to Process 1 there. Therefore, measuring processes will appear to be irreversible to any observers (even though the composite system including the observer changes its state reversibly).  

There is another way of looking at this apparent irreversibility within our theory which recognizes only Process 2. When an observer performs an observation the result is a superposition, each element of which describes an observer who has perceived a particular value. From this time forward there is no interaction between the separate elements of the superposition (which describe the observer as having perceived different results), since each element separately continues to obey the wave equation. Each observer described by a particular element of the superposition behaves in the future completely independently of any events in the remaining elements, and he can no longer obtain any information whatsoever concerning these other elements (they are completely unobservable to him).  

The irreversibility of the measuring process is therefore, within our framework, simply a subjective manifestation reflecting the fact that in observation processes the state of the observer is transformed into a superposition of observer states, each element of which describes an observer who is irrevocably cut off from the remaining elements. While it is conceivable that some outside agency could reverse the total wave function, such a change cannot be brought about by any observer which is represented by a single element of a superposition, since he is entirely powerless to have any influence on any other elements.  

There are, therefore, fundamental restrictions to the knowledge that an observer can obtain about the state of the universe. It is impossible for any observer to discover the total state function of

---

4 For another, more complete, discussion of this topic in the probabilistic interpretation see von Neumann [17], Chapter V, §4. 

(1.5. III. reçâşîrî ni bâzavodâh as çavûkîh asî îc
-îm J. avodâh. bi fâni vîrçâçîrî asî asn avîrçâçîrî S asavonî
çavâvod, hâçâmâdî 

sazavonî tevun dui J. asavodâh hiso: hâzâni rîvîrî, asî, no, J. asavonî
(1.5.) as gîrîvoda. .ti 

J. J. J. J. J. J. J. J. J. J. J. (8.5.)
J. J. J. J. J. J. J. J. J. J.
J. J. J. J. J. J. J. J. J. J.

nîrçâvoda-vîdîdîh as as
J. J. J. J. J. J. J. J. J. (8,5)
J. J. J. J. J. J. J. J. J. J
J. J. J. J. J. J. J. J. J. 

asî îc gavrîndarîzârî bîrîhîs as vî mwîrî as dîlîmîz mîs. ti tevovonî
asolîm bîcî tevî vîlîsîpavî bîrîzârî fâni dî. II tevîmîdî îc ametodî
fâni asî nîcî? hîs jî asî nîcî J. = J. (1.5. fâni dîsas J. nîsas nîcî)
asîlîgî dîlîm. . J. J. J. J. J. J. J. J. J. J.
To asdârâzârîzî îc asûxîm-as hîsazîs asv asûxîm lârîzîvî asî fâni
. fîmârîzâsas asî
. toz as dîlîmîzî dîm asî bi hîs. mîdîzârîzî mîs hîsasvîs asvî
asînî. J. hîs J. asavodâh. J. asasî vî dîrîzîs asî asûxîm vîs mîcî
ehîmazîzîzî asî sîmîs J. J. asavodî asî vîlîdîzârîzî. Lâlîmâsas mîs asî

---

any physical system, since the process of observation itself leaves no independent state for the system or the observer, but only a composite system state in which the object- system states are inextricably bound up with the observer states. As soon as the observation is performed, the composite state is split into a superposition for which each element describes a different object- system state and an observer with (different) knowledge of it. Only the totality of these observer states, with their diverse knowledge, contains complete information about the original object- system state- - - but there is no possible communication between the observers described by these separate states. Any single observer can therefore possess knowledge only of the relative state function (relative to his state) of any systems, which is in any case all that is of any importance to him.  

We conclude this section by commenting on another question which might be raised concerning irreversible processes: Is it necessary for the existence of measuring apparatus, which can be correlated to other systems, to have frictional processes which involve systems of a large number of degrees of freedom? Are such thermodynamically irreversible processes possible in the framework of pure wave mechanics with a reversible wave equation, and if so, does this circumstance pose any difficulties for our treatment of measuring processes?  

In the first place, it is certainly not necessary for dissipative processes involving additional degrees of freedom to be present before an interaction which correlates an apparatus to an object- system can take place. The counter- example is supplied by the simplified measuring process of III - §3, which involves only a system of one coordinate and an apparatus of one coordinate and no further degrees of freedom.  

To the question of whether such processes are possible within reversible wave mechanics, we answer yes, in the same sense that

---

they are present in classical mechanics, where the microscopic equations of motion are also reversible. This type of irreversibility, which might be called macroscopic irreversibility, arises from a failure to separate "macroscopically indistinguishable" states into "true" microscopic states. \(^{5}\) It has a fundamentally different character than the irreversibility of Process 1, which applies to microstates as well and is peculiar to quantum mechanics. Macroscopically irreversible phenomena are common to both classical and quantum mechanics, since they arise from our incomplete information concerning a system, not from any intrinsic behavior of the system. \(^{6}\)  

Finally, even when such frictional processes are involved, they present no new difficulties for the treatment of measuring and observation processes given here. We imposed no restrictions on the complexity or number of degrees of freedom of measuring apparatus or observers, and if any of these processes are present (such as heat reservoirs, etc.) then these systems are to be simply included as part of the apparatus or observer.  

## §4. Approximate Measurement  

A phenomenon which is difficult to understand within the framework of the probabilistic interpretation of quantum mechanics is the result of an approximate measurement. In the abstract formulation of the usual theory there are two fundamental processes; the discontinuous, probabilistic Process 1 corresponding to precise measurement, and the continuous, deterministic Process 2 corresponding to absence of any measurement. What mixture of probability and causality are we to apply to the case where only an approximate measurement is effected (i.e., where the apparatus or observer interacts only weakly and for a finite time with the object- system)?  

In the case of approximate measurement, we need to be supplied with rules which will tell us, for any initial object- system state, first, with what probability can we expect the various possible

---

revaa. I. I. a e t a t a t a t a t a t a t a t a t a t a t t a t a t a t a t a t a t a t a t a t  a t a t a t a t a t a t a t a t a t a a t a t a t a t a t a t a t a t a t a  a t a t a t a t a t a t a t a t a t  t a t a t a t a t a t a t a t a t a t   a t a t a t a t a t a t a t a t a t a   a t a t a t a t a t a t a t a t a t  e t a t a t a t a t a t a t a t a t a  t a t a t a t a t a t a t a t a t a  e t a t a t a t a t a t a t a t a t  a  t a t a t a t a t a t a t a t a t  a a t a t a t a t a t a t a t a t  a t  a t a t a t a t a t a t a t a t  a t t a t a t a t a t a t a t a t  a t a  t a t a t a t a t a t a t a t  a t a a t a t a t a t a t a t a t  a t a t  a t a t a t a t a t a t a t  a t a t t a t a t a t a t a t a t  a t a t a  t a t a t a t a t a t a t  a t a t a a t a t a t a t a t a t  a t a t a t  a t a t a t a t a t a t  a t a t a t t a t a t a t a t a t  a t a t a t a  t a t a t a t a t a t  a t a t a t a a t a t a t a t a t  a t a t a t a t  a t a t a t a t a t  a t a t a t a t t a t a t a t a t  a t a t a t a t a  t a t a t a t a t  a t a t a t a t a a t a t a t a t a t  a  t a t a t a a t a t a t a t a t a t  a  t a t a a t a t a t a t a t a t  a t  a t a a t a t a t a t a t a t  a t a a t a a t a t a t a t a t  a t a a t a a t  a t a a t a a t a t a t a t  a t a a t a a t a t  a t a a t a a t a t a t  a t a a t a a t a t a t  a  t a a t a a t a t a t a t a t  a t a t a a t a a t a t a t  a t a a t a t a a t a t a t  a t a a t a a t a a t a t a t  a t a a t a  t a a t a a t a t a t a t  a t a a t  a t a a t a a t a t a t  a t a  t a a t a a t a t a t a t  a  t a a t a a t a t a a t a t  a t a a t a a t a t a a t  a t a a t a a t a t a a t  a t  a t a a t a a t a t a t a t  a  t a a a t a a t a t a t a t  a t a a t a  t a a t a t a t a t a t  a t a a t a t a a t a t  a t a a t a t a a t a t  a  t a a t a a t a t a t a a t  a t a a t a a t a t a t  t a a t a a t a t a t a t  a t a a a t a t a t a t  a t a a a t a t a a t a t  a t a a a t a t a t a t  a  t a a a t a t a t a t a t  a t a a a t a t a t  a t a a a t a t a t a t a t  a t a a a a t a t a t a t  a t a a a a t a t a a t a t  a t a a a a t a t a t a t  t a a a a a t a t a t a t  a t a a a a a t a t a t  a t a a a a a t a t a t a t  a t a a a t a a t a t a t  a t a a a a a t a t a a t  a t a a a a a t a t a t  a t a  a a a a a a a a a a a a a a a a a a a a  a a a a a a a a a a a a a a a a a  a  a a a a a a a a a a a a a a a a  a  t a a a a a a a a a a a a a a a a  a  s a a a a a a a a a a a a a a a a  a  e a a a a a a a a a a a a a a a a  a  r a a a a a a a a a a a a a a a a  a  o a a a a a a a a a a a a a a a a  a  n a a a a a a a a a a a a a a a a  a  m a a a a a a a a a a a a a a a a  a  l a a a a a a a a a a a a a a a a  a  k a a a a a a a a a a a a a a a a  a  c a a a a a a a a a a a a a a a a  a  d a a a a a a a a a a a a a a a a  a  f a a a a a a a a a a a a a a a a  a  g a a a a a a a a a a a a a a a a  a  h a a a a a a a a a a a a a a a a  a  j a a a a a a a a a a a a a a a a  a  b a a a a a a a a a a a a a a a  a  c b a a a a a a a a a a a a a a a  a  d c b a a a a a a a a a a a a a a a  a   a  d c b a a a a a a a a a a a a a a  a  d c  b a a a a a a a a a a a a a a a  a   d c  b a a a a a a a a a a a a a a a a  a   d  c  b a a a a a a a a a a a a a a a  d  c  b  a a a a a a a a a a a a a a a a  d  c b  a a a a a a a a a a a a a a a a  a   c  b  a a a a a a a a a a a a a a a  a   c b  a a a a a a a a a a a a a a a  a  c  b  a a a a a a a a a a a a a a  a  c  d  b  a a a a a a a a a a a a a a a a a  c  d  b  a a a a a a a a a a a  a  c  d  b a a a a a a a a a a a a a a a  a c  d  b  a a a a a a a a a a a a a  a c  d  c  b  a a a a a a a a a a a a  a c  d  c b  a a a a a a a a a a a a a  a c  c  b  a a a a a a a a a a a a a  a c   c  b  a a a a a a a a a a a a a a  c  c  b  a a a a a a a a a a a a a a c  c  c  b  a a a a a a a a a a a a  c  c  c  b  a a a a a a a a a a a  c  c  c  b

---

apparatus readings, and second, what new state to ascribe to the system after the value has been observed. We shall see that it is generally impossible to give these rules within a framework which considers the apparatus or observer as performing an (abstract) observation subject to Process 1, and that it is necessary, in order to give a full account of approximate measurements, to treat the entire system, including apparatus or observer, wave mechanically.  

The position that an approximate measurement results in the situation that the object- system state is changed into an eigenstate of the exact measurement, but for which particular one the observer has only imprecise information, is manifestly false. It is a fact that we can make successive approximate position measurements of particles (in cloud chambers, for example) and use the results for somewhat reliable predictions of future positions. However, if either of these measurements left the particle in an "eigenstate" of position (5 function), even though the particular one remained unknown, the momentum would have such a variance that no such prediction would be possible. (The possibility of such predictions lies in the correlations between position and momentum at one time with position and momentum at a later time for wave packets- correlations which are totally destroyed by precise measurements of either quantity.)  

Instead of continuing the discussion of the inadequacy of the probabilistic formulation, let us first investigate what actually happens in approximate measurements, from the viewpoint of pure wave mechanics. An approximate measurement consists of an interaction, for a finite time, which only imperfectly correlates the apparatus (or observer) with the object- system. We can deduce the desired rules in any particular case by the following method: For fixed interaction and initial apparatus state and for any initial object- system state we solve the wave equation for the time of interaction in question. The result will be a superposition of

---

- 8 8 8 8 8 8 8 8 8 8 9 8 8 8 8 8 8 8 8 8 0 8 8 8 8 8 8 8 8 8 1 8 8 8 8 8 8 8 8 8 2 8 8 8 8 8 8 8 8 8 3 8 8 8 8 8 8 8 8 8 4 8 8 8 8 8 8 8 8 8 5 8 8 8 8 8 8 8 8 8 6 8 8 8 8 8 8 8 8 8 7 8 8 8 8 8 8 8 8 8  8 8 8 8 8 8 8 8 8  - 8 8 8 8 8 8 8 8 8  ( 8 8 8 8 8 8 8 8 8  ) 8 8 8 8 8 8 8 8 8  : 8 8 8 8 8 8 8 8 8  ; 8 8 8 8 8 8 8 8 8  , 8 8 8 8 8 8 8 8 8 ., 8 8 8 8 8 8 8 8 8  . 8 8 8 8 8 8 8 8 8  = 8 8 8 8 8 8 8 8 8  > 8 8 8 8 8 8 8 8 8  < 8 8 8 8 8 8 8 8 8  ≥ 8 8 8 8 8 8 8 8 8  ≤ 8 8 8 8 8 8 8 8 8  ≈ 8 8 8 8 8 8 8 8 8  ∽ 8 8 8 8 8 8 8 8 8  ™ 8 8 8 8 8 8 8 8 8  ¶ 8 8 8 8 8 8 8 8 8  · 8 8 8 8 8 8 8 8 8  ' 8 8 8 8 8 8 8 8 8  " 8 8 8 8 8 8 8 8 8  ’ 8 8 8 8 8 8 8 8 8  ” 8 8 8 8 8 8 8 8 8  “ 8 8 8 8 8 8 8 8 8  ‘ 8 8 8 8 8 8 8 8 8  • 8 8 8 8 8 8 8 8 8  + 8 8 8 8 8 8 8 8 8  / 8 8 8 8 8 8 8 8 8  \ 8 8 8 8 8 8 8 8 8  } 8 8 8 8 8 8 8 8 8  ~ 8 8 8 8 8 8 8 8 8  ^ 8 8 8 8 8 8 8 8 8  & 8 8 8 8 8 8 8 8 8  | 8 8 8 8 8 8 8 8 8  { 8 8 8 8 8 8 8 8 8  ] 8 8 8 8 8 8 8 8 8  [ 8 8 8 8 8 8 8 8 8  o 8 8 8 8 8 8 8 8 8  p 8 8 8 8 8 8 8 8 8  s 8 8 8 8 8 8 8 8 8  t 8 8 8 8 8 8 8 8 8  u 8 8 8 8 8 8 8 8 8  v 8 8 8 8 8 8 8 8 8  w 8 8 8 8 8 8 8 8 8  x 8 8 8 8 8 8 8 8 8  y 8 8 8 8 8 8 8 8 8  z 8 8 8 8 8 8 8 8 8  a 8 8 8 8 8 8 8 8 8  b 8 8 8 8 8 8 8 8 8  c 8 8 8 8 8 8 8 8 8  d 8 8 8 8 8 8 8 8 8  e 8 8 8 8 8 8 8 8 8  f 8 8 8 8 8 8 8 8 8  g 8 8 8 8 8 8 8 8 8  h 8 8 8 8 8 8 8 8 8  i 8 8 8 8 8 8 8 8 8  j 8 8 8 8 8 8 8 8 8  k 8 8 8 8 8 8 8 8 8  l 8 8 8 8 8 8 8 8 8  m 8 8 8 8 8 8 8 8 8  n 8 8 8 8 8 8 8 8 8  ö 8 8 8 8 8 8 8 8 8  ß 8 8 8 8 8 8 8 8 8  à 8 8 8 8 8 8 8 8 8  á 8 8 8 8 8 8 8 8 8  â 8 8 8 8 8 8 8 8 8  æ 8 8 8 8 8 8 8 8 8  ç 8 8 8 8 8 8 8 8 8  è 8 8 8 8 8 8 8 8 8  é 8 8 8 8 8 8 8 8 8  ê 8 8 8 8 8 8 8 8 8  î 8 8 8 8 8 8 8 8 8  í 8 8 8 8 8 8 8 8 8  ú 8 8 8 8 8 8 8 8 8  ü 8 8 8 8 8 8 8 8 8  þ 8 8 8 8 8 8 8 8 8  ð 8 8 8 8 8 8 8 8 8  š 8 8 8 8 8 8 8 8 8  ſ 8 8 8 8 8 8 8 8 8  ġ 8 8 8 8 8 8 8 8 8  č 8 8 8 8 8 8 8 8 8  ž 8 8 8 8 8 8 8 8 8  ş 8 8 8 8 8 8 8 8 8  œ 8 8 8 8 8 8 8 8 8  ô 8 8 8 8 8 8 8 8 8  ø 8 8 8 8 8 8 8 8 8  ÷ 8 8 8 8 8 8 8 8 8  × 8 8 8 8 8 8 8 8 8  √ 8 8 8 8 8 8 8 8 8  ° 8 8 8 8 8 8 8 8 8  ± 8 8 8 8 8 8 8 8 8 ² 8 8 8 8 8 8 8 8 8 ³ 8 8 8 8 8 8 8 8 8 ⁴ 8 8 8 8 8 8 8 8 8 ¹ 8 8 8 8 8 8 8 8 8 ½ 8 8 8 8 8 8 8 8 8 ¾ 8 8 8 8 8 8 8 8 8 ⅛ 8 8 8 8 8 8 8 8 8 ¼ 8 8 8 8 8 8 8 8 8 ₀ 8 8 8 8 8 8 8 8 8 ₁ 8 8 8 8 8 8 8 8 8 ₂ 8 8 8 8 8 8 8 8 8 ๓ 8 8 8 8 8 8 8 8 8 ๔ 8 8 8 8 8 8 8 8 8 ๕ 8 8 8 8 8 8 8 8 8 ๖ 8 8 8 8 8 8 8 8 8 ๑ 8 8 8 8 8 8 8 8 8 ๒ 8 8 8 8 8 8 8 8 8 ๐ 8 8 8 8 8 8 8 8 8 ٨ 8 8 8 8 8 8 8 8 8 ۹ 8 8 8 8 8 8 8 8 8 ۰ 8 8 8 8 8 8 8 8 8 ۱ 8 8 8 8 8 8 8 8 8 ۲ 8 8 8 8 8 8 8 8 8 ۳ 8 8 8 8 8 8 8 8 8 ۴ 8 8 8 8 8 8 8 8 8 ۵ 8 8 8 8 8 8 8 8 8 ۶ 8 8 8 8 8 8 8 8 8 ۷ 8 8 8 8 8 8 8 8 8 ۸ 8 8 8 8 8 8 8 8 8 ৯ 8 8 8 8 8 8 8 8 8 ۱۰ 8 8 8 8 8 8 8 8 8 ۱۱ 8 8 8 8 8 8 8 8 8 ۱۲ 8 8 8 8 8 8 8 8 8 ۱۳ 8 8 8 8 8 8 8 8 8 ۱۴ 8 8 8 8 8 8 8 8 8 ۱۵ 8 8 8 8 8 8 8 8 8 ۱۶ 8 8 8 8 8 8 8 8 8 ۱۷ 8 8 8 8 8 8 8 8 8 ۱۸ 8 8 8 8 8 8 8 8 8 ۱۹ 8 8 8 8 8 8 8 8 8 ۲۰ 8 8 8 8 8 8 8 8 8 ٢١ 8 8 8 8 8 8 8 8 8 ٣١ 8 8 8 8 8 8 8 8 8

---

apparatus (observer) states and relative object- system states. 

Then (according to the method of Chapter IV for assigning a measure to a superposition) we assign a probability to each observed result equal to the square-amplitude of the coefficient of the element which contains the apparatus (observer) state representing the registering of that result. Finally, the object-system is assigned the new state which is its relative state in that element. 

For example, let us consider the measuring process described in Chapter III - §3, which is an excellent model for an approximate measurement. After the interaction, the total state was found to be (III - (3.12)): 

\[ \mathcal{H}_e^{S+A} = \int \frac{1}{N_r} \int_0^{r'} \mathcal{G}(q) \mathcal{S}(r-r') dq \]

Then, according to our prescription, we assign the probability density \(P(r')\) to the observation of the apparatus coordinate \(r'\) 

\[ P(r') = \left| \frac{1}{N_r} \right|^2 = \int d^4 q \mathcal{G}(q) \mathcal{M}^{abc}(r'-q^c) dq \]

which is the square amplitude of the coefficient \((\frac{1}{N_r})\) of the element \(\mathcal{G}^{r'}(q) \mathcal{S}(r-r')\) of the superposition (4.1) in which the apparatus coordinate has the value \(r' = r''\). Then, depending upon the observed apparatus coordinate \(r'\), we assign the object-system the new state 

\[ \mathcal{G}^{r'}(q) = N_r \mathcal{G}(q) \mathcal{M}(r'-q^c) \]

(where \(\mathcal{G}(q)\) is the old state, and \(\mathcal{M}(r)\) is the initial apparatus state) which is the relative object-system state in (4.1) for apparatus coordinate \(r'\). 

This example supplies the counter-example to another conceivable method of dealing with approximate measurement within the framework of Process 1. This is the position that when an approximate measurement of a quantity \(Q\) is performed, in actuality another quantity \(Q'\) is precisely measured, where the eigenstates of \(Q'\) correspond to fairly well-defined (i.e., sharply peaked distributions

---

for) \(Q\) values. \(^{2}\) However, any such scheme based on Process 1 always has the prescription that after the measurement, the (unnormalized) new state function results from the old by a projection (on an eigenstate or eigenspace), which depends upon the observed value. If this is true, then in the above example the new state \(\hat{\xi}^{\prime}(\hat{g})\) must result from the old, \(\phi (\hat{g})\) , by a projection \(E\) :  

\[\hat{\xi}^{\prime \prime}(\hat{g}) = N E\phi (\hat{g}) = N_{\gamma^{\prime}}\phi (\hat{g})N(r^{\prime} - g t)\]  

(where \(N_{\gamma^{\prime}}\) are normalization constants). But \(E\) is only a projection if \(E^{2} = E\) . Applying the operation (4.4) twice, we get:  

\[E(N E\phi (\hat{g})) = N E^{2}\phi (\hat{g}) = N^{\prime}\phi (\hat{g})n^{2}(r^{\prime} - g t)\] \[\Rightarrow E^{2}\phi (\hat{g}) = \frac{N^{\prime}}{N}\phi (\hat{g})n^{2}(r^{\prime} - g t)\]  

and we see that \(E\) cannot be a projection unless \(n(\hat{g}) = n^{2}(\hat{g})\) for all \(\hat{g}\) \((i\in \mathcal{I}(g) = 0\) or all \(\hat{g}\) ) and we have arrived at a contradiction to the assumption that in all cases the changes of states for approximate measurements are governed by projections. (In certain special cases, such as approximate position measurements with slits or Geiger counters, the new functions arise from the old by multiplication by sharp cutoff functions which are 1 over the slit or counter and 0 elsewhere, so that these measurements can be handled by projections.)  

One cannot, therefore, account for approximate measurements by any scheme based on Process 1, and it is necessary to investigate these processes entirely wave- mechanically. Our viewpoint constitutes a framework in which it is possible to make precise deductions about such measurements and observations, since we can follow in detail the interaction of an observer or apparatus with an object- system.

---

Sovtva navrva-voino vvtslslr jna svstva (navrvao) svtslvaa  avlavaa, a zanlavaa toi vi vtslvao to bonva an to vnslvao) navi  vlsva navrvao nnao to vtslvao to nvlavaa av (novlavao)vaa to  nvlavao an to novlavao nav  ov svtslvaa-avvaa an to lvaa  ov svtslvaoavvaa avva (navrvao) avrvaa an nslvao novlva  navlava a svrva-voino ov vtslava  vtslava an to nvlavaa-avvaa  avlavaa an to nvlavaa avrvaa ov vtslavaa  avlavaa an to nvlavaa avrvaa ov vtslavava  avlavaa an to nvlavaa avrvaa ov vtslavavav  avlavaa an to nvlavaa avrvaa ov vtslavavi  avlavaa an to nvlavaa avrvaa ov vtslavavo  avlavaa an to nvlavaa avrvaa ov vtslavo  avlavaa an to nvlavaa avrvaa ov vtslavu  avlavaa an to nvlavaa avrvaa ov vtslavi  avlavaa an to nvlavaa avrvaa ov vtslavn  avlavaa an to nvlavaa avrvaa ov vtslavm  avlavaa an to nvlavaa avrvaa ov vtslavk  avlavaa an to nvlavaa avrvaa ov vtslavj  avlavaa an to nvlavaa avrvaa ov vtslavh  avlavaa an to nvlavaa avrvaa ov vtslavf  avlavaa an to nvlavaa avrvaa ov vtslavc  avlavaa an to nvlavaa avrvaa ov vtslavb  avlavaa an to nvlavaa avrvaa ov vtslava  avlavaa an to nvlavaa avrvaa ov vtslaa  avlavaa an to nvlavaa avrvaa ov vtslab  avlavaa an to nvlavaa avrvaa ov vtslac  avlavaa an to nvlavaa avrvaa ov vtslae  avlavaa an to nvlavaa avrvaa ov vtslaf  avlavaa an to nvlavaa avrvaa ov vtslai  avlavaa an to nvlavaa avrvaa ov vtslaj  avlavaa an to nvlavaa avrvaa ov vtslal  avlavaa an to nvlavaa avrvaa ov vtslaz  avlavaa an to nvlavaa avrvaa ov vtslba  avlavaa an to nvlavaa avrvaa ov vtslbi  avlavaa an to nvlavaa avrvaa ov vtslbo  avlavaa an to nvlavaa avrvaa ov vtslbu  avlavaa an to nvlavaa avrvaa ov vtslbr  avlavaa an to nvlavaa avrvaa ov vtslbs  avlavaa an to nvlavaa avrvaa ov vtslbt  avlavaa an to nvlavaa avrvaa ov vtslcu  avlavaa an to nvlavaa avrvaa ov vtslcv  avlavaa an to nvlavaa avrvaa ov vtslcl  avlavaa an to nvlavaa avrvaa ov vtslcm  avlavaa an to nvlavaa avrvaa ov vtslcn  avlavaa an to nvlavaa avrvaa ov vtslco  avlavaa an to nvlavaa avrvaa ov vtslcp  avlavaa an to nvlavaa avrvaa ov vtslcr  avlavaa an to nvlavaa avrvaa ov vtslcs  avlavaa an to nvlavaa avrvaa ov vtslct  avlavaa an to nvlavaa avrvaa ov vtsldu  avlavaa an to nvlavaa avrvaa ov vtslcd  avlavaa an to nvlavaa avrvaa ov vtslce  avlavaa an to nvlavaa avrvaa ov vtslcf  avlavaa an to nvlavaa avrvaa ov vtslch  avlavaa an to nvlavaa avrvaa ov vtslci  avlavaa an to nvlavaa avrvaa ov vtslbc  avlavaa an to nvlavaa avrvaa ov vtslbd  avlavaa an to nvlavaa avrvaa ov vtslbe  avlavaa an to nvlavaa avrvaa ov vtslbf  avlavaa an to nvlavaa avrvaa ov vtslcg  avlavaa an to nvlavaa avrvaa ov vtsldh  avlavaa an to nvlavaa avrvaa ov vtslfi  avlavaa an to nvlavaa avrvaa ov vtslgi  avlavaa an to nvlavaa avrvaa ov vtslhi  avlavaa an to nvlavaa avrvaa ov vtslji  avlavaa an to nvlavaa avrvaa ov vtslki  avlavaa an to nvlavaa avrvaa ov vtslkl  avlavaa an to nvlavaa avrvaa ov vtslkm  avlavaa an to nvlavaa avrvaa ov vtslkn  avlavaa an to nvlavaa avrvaa ov vtslko  avlavaa an to nvlavaa avrvaa ov vtslho  avlavaa an to nvlavaa avrvaa ov vtslpo  avlavaa an to nvlavaa avrvaa ov vtslno  avlavaa an to nvlavaa avrvaa ov vtslro  avlavaa an to nvlavaa avrvaa ov vtslto  avlavaa an to nvlavaa avrvaa ov vtslfo  avlavaa an to nvlavaa avrvaa ov vtslgo  avlavaa an to nvlavaa avrvaa ov vtsldo  avlavaa an to nvlavaa avrvaa ov vtsljo  avlavaa an to nvlavaa avrvaa ov vtslzo  avlavaa an to nvlavaa avrvaa ov vtslxo  avlavaa an to nvlavaa avrvaa ov vtslwo  avlavaa an to nvlavaa avrvaa ov vtslvo  avlavaa an to nvlavaa avrvaa ov vtslvi  avlavaa an to nvlavaa avrvaa ov vtslwi  avlavaa an to nvlavaa avrvaa ov vtslzi  avlavaa an to nvlavaa avrvaa ov vtslzu  avlavaa an to nvlavaa avrvaa ov vtslvu  avlavaa an to nvlavaa avrvaa ov vtslwu  avlavaa an to nvlavaa avrvaa ov vtslhu  avlavaa an to nvlavaa avrvaa ov vtslju  avlavaa an to nvlavaa avrvaa ov vtslfu  avlavaa an to nvlavaa avrvaa ov vtslku  avlavaa an to nvlavaa avrvaa ov vtslmu  avlavaa an to nvlavaa avrvaa ov vtslnu  avlavaa an to nvlavaa avrvaa ov vtslpu  avlavaa an to nvlavaa avrvaa ov vtslqu  avlavaa an to nvlavaa avrvaa ov vtslru  avlavaa an to nvlavaa avrvaa ov vtslri  avlavaa an to nvlavaa avrvaa ov vtslsi  avlavaa an to nvlavaa avrvaa ov vtslui  avlavaa an to nvlavaa avrvaa ov vtslqi  avlavaa an to nvlavaa avrvaa ov vtslpi  avlavaa an to nvlavaa avrvaa ov vtslqo  avlavaa an to nvlavaa avrvaa ov vtslmo  avlavaa an to nvlavaa avrvaa ov vtslmi  avlavaa an to nvlavaa avrvaa ov vtslni  avlavaa an to nvlavaa avrvaa ov vtslng  avlavaa an to nvlavaa avrvaa ov vtslmg  avlavaa an to nvlavaa avrvaa ov vtslkh  avlavaa an to nvlavaa avrvaa ov vtslgh  avlavaa an to nvlavaa avrvaa ov vtslfg  avlavaa an to nvlavaa avrvaa ov vtslff  avlavaa an to nvlavaa avrvaa ov vtslgg  avlavaa an to nvlavaa avrvaa ov vtslhg  avlavaa an to nvlavaa avrvaa ov vtslhh  avlavaa an to nvlavaa avrvaa ov vtslhl  avlavaa an to nvlavaa avrvaa ov vtslhf  avlavaa an to nvlavaa avrvaa ov vtslif  avlavaa an to nvlavaa avrvaa ov vtsliff  avlavaa an to nvlavaa avrvaa ov vtslig  avlavaa an to nvlavaa avrvaa ov vtsligh  avlavaa an to nvlavaa avrvaa ov vtslih  avlavaa an to nvlavaa avrvaa ov vtslij  avlavaa an to nvlavaa avrvaa ov vtsljj  avlavaa an to nvlavaa avrvaa ov vtsljk  avlavaa an to nvlavaa avrvaa ov vtslkk  avlavaa an to nvlavaa avrvaa ov vtslkg  avlavaa an to nvlavaa avrvaa ov vtslkj  avlavaa an to nvlavaa avrvaa ov vtslhk  avlavaa an to nvlavaa avrvaa ov vtsljh  avlavaa an to nvlavaa avrvaa ov vtslhj  avlavaa an to nvlavaa avrvaa ov vtslfh  avlavaa an to nvlavaa avrvaa ov vtslfih  avlavaa an to nvlavaa avrvaa ov vtslfih  avlavaa an to nvlavaa avrvaa ov vtsllih  avlavaa an to nvlavaa avrvaa ov vtslli  avlavaa an to nvlavaa avrvaa ov vtsllj  avlavaa an to nvlavaa avrvaa ov vtsllk  avlavaa an to nvlavaa avrvaa ov vtsllh  avlavaa an to nvlavaa avrvaa ov vtsllg  avlavaa an to nvlavaa avrvaa ov vtsllf  avlavaa an to nvlavaa avrvaa ov vtsllb  avlavaa an to nvlavaa avrvaa ov vtsllc  avlavaa an to nvlavaa avrvaa ov vtslla  avlavaa an to nvlavaa avrvaa ov vtslls  avlavaa an to nvlavaa avrvaa ov vtsllt  avlavaa an to nvlavaa avrvaa ov vtsllu  avlavaa an to nvlavaa avrvaa ov vtsllv  avlavaa an to nvlavaa avrvaa ov vtsllw  avlavaa an to nvlavaa avrvaa ov vtsllx  avlavaa an to nvlavaa avrvaa ov vtsllz  avlavaa an to nvlavaa avrvaa ov vtsllq  avlavaa an to nvlavaa avrvaa ov vtsllr  avlavaa an to nvlavaa avrvaa ov vtslll  avlavaa an to nvlavaa avrvaa ov vtsllm  avlavaa an to nvlavaa avrvaa ov vtslln  avlavaa an to nvlavaa avrvaa ov vtsllp  avlavaa an to nvlavaa avrvaa ov vtsllo  avlavaa an to nvlavaa avrvaa ov vtslli  avlavaa an to nvlavaa avrvaa ov vtsll

---

§5. Discussion of a Spin Measurement Example. 

We shall conclude this chapter with a discussion of an in-
structive example of Bohm¹. Bohm considers the measurement of the
component of the angular momentum of an atom, whose total angular
momentum is \(\frac{\hbar}{2}\), which is brought about by a Stern-Gerlach experiment.
The measurement is accomplished by passing an atomic beam through
an inhomogenous magnetic field, which has the effect of giving the
particle a momentum which is directed up or down depending upon
whether the spin was up or down. 

The measurement is treated as impulsive, so that during the
time that the atom passes through the field the Hamiltonian is taken
to be simply the interaction: 

\[H = M \left( \vec{S} \cdot \vec{\sigma} \right), \quad M = -\frac{2\pi}{\hbar} \]

(5.1) 

where \(\vec{\sigma}\) is the magnetic field and \(\vec{S}\) the spin operator for the
atom. The particle is presumed to pass through a region of the
field where the field is in the \(\vec{\sigma}\) direction, so that during the
time of transit the field is approximately \(\vec{\sigma} = \vec{\sigma}_0 + \vec{\sigma}_0 \cos(\vec{\sigma}_0) \vec{\sigma}_0\) and
\(\vec{\sigma}_0 = \left( \frac{\partial \vec{\sigma}_0}{\partial \vec{\sigma}} \right) = 0\), and hence the interaction is approximately: 

\[H_T \cong M \left( \vec{\sigma}_0 + \vec{\sigma} \vec{\sigma}_0' \right) S_\vec{\sigma}\]

(5.2) 

where \(S_\vec{\sigma}\) denotes the operator for the \(\vec{\sigma}\) component of the spin. 

It is assumed that the state of the atom, just prior to entry
into the field, is a wave packet of the form: 

\[\psi = f_0(\vec{\sigma}) \left( c_+ v_+ + c_- v_- \right)\]

(5.3) 

where \(v_+\) and \(v_-\) are the spin functions for \(S_\vec{\sigma} = 1\) and \(-1\) respectively.
Solving the Schrödinger equation for the Hamiltonian (5.2) and
initial condition (5.3) yields the state for a later time \(t\): 

\[ \psi = f_0(\vec{\sigma}) \left( c_+ e^{-i\omega (\vec{\sigma}_0 + \vec{\sigma} \vec{\sigma}_0') t / \hbar} v_+ + c_- e^{+i\omega (\vec{\sigma}_0 + \vec{\sigma} \vec{\sigma}_1') t / \hbar} v_- \right) \]

---

I  s e a o o r i  n o  b e a e s  s m e n o s  i n s e  y m e ,  r e v a w o h  s a o u l a v  (  t o t  - m i )  s i n  r e m e n e m a s e n  a i t  t o r t a  s a i t  r e a t i t r e a t i t r e a t i t r e a t i t r a t i t r e a t i t r e a t i t r e a  t o r t a  s a i t  r e a t i t r a t i t r e a t i t r e  a t i t r e a t i t r e a t i t r e a i t r e a t i t r e a t i t r e a t i  t o r t a  s a i t  r e a t i t r i t r e a t i t r e a t i t r e a t i i t r e a t i t r e a t i t r e a t i r e a t i t r e a t i t r e a t i t r i t r e a t i t r e a t  i t r e a t i t r e a t i t r e a t i a t i t r e a t i t r e a t i t r e a r e a t i t r e a t i t r e a t i t r  e a t i t r e a t i t r e a t i t r e  a t i t r e  a t i t r e a t i t r e  a t i t r e t r e a t i t r e a t i t r e a t i t  r e a t i t r e a t i t r e a t  i t r e a t  i t r e a t i t r e a t  i t r e a t r e a t i t r e a t i t r e a t i t i t r e a t i t r e a t i t r e a t  i t i t r e a t i t r e a t i t r e a  i t r e a t i t r e a t i t r e a t  t r e a t i t r e a t i t r e a t i t t r e a t i t r e a t i t r e a t i t a t r e a t i t r e a t i t r e a t i  r e a t i t r e a t i t r e a t i t a r e a t i t r e a t i t r e a t i t a  r e a t i t r e a t i t r e a t i t  a r e a t i t r e a t i t r e a t i t  t r e a t i t r e a t i t r e a t  i r e a t i t r e a t i t r e a t i t  i r e a t i t r e a t i t r e a t  i r  e a t i t r e a t i t r e a t  i r  r e a t i t r e a t i t r e a t  i r a t i t r e a t i t r e a t  i r  r a t i t r e a t i t r e a t  i r  a t i t r e a t i t r e a t  i r  a r e a t i t r e a t  i r  a r e a t  i r  a r e a t  i r  a r  a r e a t  i r  a r  a r  a r  a r  a r  a r  a r a r  a r  a r  a r  a r  a r  a  r  a r  a r  a r  a r  a  r  a  r  a  r  a  r  a  r  a r  a  r  a  r  a  r  a  a  r  a  r  a  r  a  r  a  a  r

---

Therefore, if \(\Delta t\) is the time that it takes the atom to traverse the field \(^2\) , each component of the wave packet has been multiplied by a phase factor \(e^{i\omega (\theta_0 + \frac{\pi}{2}\theta_0)\Delta t / \hbar}\) , i.e., has had its mean momentum in the \(\gamma\) direction changed by an amount \(\pm \frac{\hbar}{2}\omega \Delta t\) , depending upon the spin direction. Thus the initial wave packet (with mean momentum zero) is split into a superposition of two packets, one with mean \(\gamma\) - momentum \(+\frac{\hbar}{2}\omega \Delta t\) and spin up, and the other with spin down and mean \(\gamma\) - momentum \(-\frac{\hbar}{2}\omega \Delta t\) .  

The interaction (5.2) has therefore served to correlate the spin with the momentum in the \(\gamma\) - direction. These two packets of the resulting superposition now move in opposite \(\gamma\) - directions, so that after a short time they become widely separated (provided that the momentum changes \(\pm \frac{\hbar}{2}\omega \Delta t\) are large compared to the momentum spread of the original packet), and the \(\gamma\) - coordinate is itself then correlated with the spin- - - representing the "apparatus" coordinate in this case. The Stern- Gerlach apparatus therefore splits an incoming wave packet into a superposition of two diverging packets, corresponding to the two spin values.  

We take this opportunity to caution against a certain viewpoint which can lead to difficulties. This is the idea that, after an apparatus has interacted with a system, in "actuality" one or another of the elements of the resultant superposition described by the composite state- function has been realized to the exclusion of the rest, the existing one simply being unknown to an external observer (i.e. that instead of the superposition there is a genuine mixture). This position must be erroneous since there is always the possibility for the external observer to make use of interference properties between the elements of the superposition.  

In the present example, for instance, it is in principle possible to deflect the two beams back toward one another with magnetic fields and recombine them in another inhomogeneous field, which duplicates the first, in such a manner that the orginal spin state (before entering the apparatus) is restored.3 This would not be

---

- It is to be observed as it is to be observed. But observation is not to be observed. It is to be observed. It is to be observed. It is to be observed. It is to observe. It is to observe. It is to observe. It is to observe. It is to be observed. It is to observe. It is to observe. It is not to be observed. It is to observe. It is to observe. It is to observe. 

But again it is to be observed. It is to be observed. It is to be observed. It is not to be observed. It is to be observed. It is to be observed. It's to be observed. It is to be observed. It is to be observed. It is to observed. It is to be observed. It is to be observed. It is to be observed, but it is to be observed. It is to be observed. It is to be observed. It's to observe. It is to be observed. It is to be observed. It is to be observed. 

But not to observe it is to be observed. It is to be observed. It is to be observed. It isn't to be observed. It isn't to be observed. It isn't to be observed. It is to be observed. It is to be observed. It is to to be observed. It is to be observed. It is to be observed. It is to not to be observed. It is to be observed. It is to be observed. It is not be observed. It is to be observed. It is to be observed. It is to be observe. It is to be observed. It is to be observed. It is to be observed, it is to be observed. It is to be observed. It is to be observed. It 

It is to be observed. It is to be observed. It is to be observed. It is observed. It is to be observed. It is to be observed. It is to be observed to be observed. It is to be observed. It is to be observed. It is to 

2This time is, strictly speaking, not well defined. The time is, strictly speaking, not well defined. The time is, strictly speaking, not well-defined. The time is, strictly speaking, not well-defined. The time is, strictly speaking, 

3As pointed out by Bohm [1], pg. 604.

---

possible if the original Stern- Gerlach apparatus performed the function of converting the original wave packet into a non- interfering mixture of packets for the two spin cases. Therefore the position that after the atom has passed through the inhomogeneous field it is "really" in one or the other beam with the corresponding spin, although we are ignorant of which one, is incorrect.  

After two systems have interacted and become correlated it is true that marginal expectations for subsystem operators can be calculated correctly when the composite system is represented by a certain non- interfering mixture of states. Thus if the composite system state is \(\mathcal{H}^{s_1 + s_2} = \sum_i \alpha_i \mathcal{A}_i^{s_1} \mathcal{M}_i^{s_2}\) , where the \(\{\mathcal{M}_i\}\) are orthogonal, then for purposes of calculating the expectations of operators on \(\mathcal{S}_1\) the state \(\mathcal{H}^{s_1 + s_2}\) is equivalent to the non- interfering mixture of states \(\mathcal{A}_i^{s_1} \mathcal{M}_i^{s_2}\) weighted by \(P_i = \alpha_i \mathcal{A}_i\) , and one can take the picture that one or another of the cases \(\mathcal{A}_i^{s_1} \mathcal{M}_i^{s_2} \mathcal{A}_i^{s_1}\) has been realized to the exclusion of the rest, with probabilities \(P_i\) .4  

However, this representation by a mixture must be regarded as only a mathematical artifice which, although useful in many cases, is an incomplete description because it ignores phase relations between the separate elements which actually exist, and which become important in any interactions which involve more than just a subsystem.  

In the present example, the "composite system" is made of the "subsystems" spin value (object- system) and \(g\) - coordinate (apparatus) and the superposition of the two diverging wave packets is the state after interaction. It is only correct to regard this state as a mixture so long as any contemplated future interactions or measurements will involve only the spin value or only the \(g\) - coordinate, but not both simultaneously. As we saw, phase relations between the two packets are present and become important when they are deflected back and recombined in another inhomogeneous field—a process involving the spin values and \(g\) - coordinate simultaneously.

---

e n t s e x e v e n t o f h o r s e n t e s i a t t e s t a n t e m i t a n t i s t i t e r o t o s e n t i t 4 See Chapter III, §1.  o n e o v e w s i t s o t r e n o q u o n o s e s , 5 h i e t i t  -  -  -  -  -  -  -  -  -  -  t o t o s e n t o s e n t i t  g u i b i n e s t o  t h i s  t r a n s o n e s e w o f a g a n s i o n e o t o r o t i s  o n i t e t e m u s  s e n e n t i t s ) s e m o s e o v a w l i s t i t e s o n i t e m u s . n o t o s e n t i t s s i g e o n i t n o q u  s e n o , u s e s o n e o w t o n o t i s e o r o t o g i s e o n t i t s t i t g e s e t i t ( o r e o s u s e n o m o n  s i t s e t i t s s e n i t s o n i t s s e n e s e w i s e s i t s s e n e s e w i s e s i t s s e s e w i s e s i t s s e n e s e w i t s s e n e s e w i t s s e n e s e s e w i t s s e n e s e w i t s s e s e w i t s s e n e s e w i t s s s e n e s e w i t s s e n e s e w i s e s e w i t s s e n e s e w i s e s e s e w i t s s e n e s e w i s e s s e n e s e w i s e s e s e w i s e s e s e w i s e s e s e s e w i s e s e s e s e w i s s e s e s e s e s e s e s e s e s e s e s s e s e s e s e s e s e s e s e s e e s e s e s e s e s e s e s e s e s e e e s e s e s e s e s e s e s e s e s s s e s e s e s e s e s e s e s e s e t s e s e s e s e s e s e s e s e s e s t s e s e s e s e s e s e s e s e s e t e s e s e s e s e s e s e s e s e s e t t s e s e s e s e s e s e s e s e s e e t s e s e s e s e s e s e s e s e s s e e s e s e s e s e s e s e s e s e e s s e s e s e s e s e s e s e s e s s e t s e s e s e s e s e s e s e s e e s e e s e s e s e s e s e s e s e s s e s s e s e s e s e s e s e s e s e e s e t s e s e s e s e s e s e s e s s e s e e s e s e s e s e s e s e s e e s e s s e s e s e s e s e s e s e s s e s e t s e s e s e s e s e s e s e e s e s e e s e s e s e s e s e s e s s e s e s s e s e s e s e s e s e s e e s e s e t s e s e s e s e s e s e s s e s e s e e s e s e s e s e s e s e e s e s e s s e s e s e s e s e s e s s e s e s e t s e s e s e s e s e s e e s e s e s e e s e s e s e s e s e s s e s e s e s s e s e s e s e s e s e e s e s e s e t s e s e s e s e s e s s e s e s e s e e s e s e s e s e s e e s e s e s e s s e s e s e s e s e s s e s e s e s e t s e s e s e s e s e e s e s e s e s e e s e s e s e s e s s e s e s e s e s s e s e s e s e s e e s e s e s e s e t s e s e s e s e s s e s e s e s e s e t s e s e s e s e e s e s e s e s e s e t s e s e s e s s e s e s e s e s e s e t s e s e s e e s e s e s e s e s e s e t s e s e s s e s e s e s e s e s e s e t s e s e e s e s e s e s e s e s e s e t s e s s e s e s e s e s e s e s e s e t s e e s e s e s e s e s e s e s e s e t s s e s e s e s e s e s e s e s e s e

---

It is therefore improper to attribute any less validity or "reality" to any element of a superposition than any other element, due to this ever present possibility of obtaining interference effects between the elements. All elements of a superposition must be regarded as simultaneously existing. 

At this time we should like to add a few remarks concerning the notion of transition probabilities in quantum mechanics. Often one considers a system, with Hamiltonian \(H\) and stationary states \(\{\phi_i\}\), to be perturbed for a time by a time-dependent addition to the Hamiltonian, \(H_t(t)\). Then under the action of the perturbed Hamiltonian \(H' = H + H_t(t)\) the states \(\{\phi_i'\}\) are generally no longer stationary but change after time \(t\) into new states \(\{\psi_t(t)\}\) : 

\[ (5.5) \quad \phi_j' \to \psi_t'(t) = \sum_i (\phi_j', \psi_t'(t)) \phi_j = \sum_i a_{ij}(t) \phi_j' \]

which can be represented as a superposition of the old stationary states with time-dependent coefficients \(a_{ij}(t)\). 

If at time \(Z\) a measurement with eigenstates \(\phi_j\) is performed, such as an energy measurement (whose operator is the original \(H\)), then according to the probabilistic interpretation the probability for finding the state \(\phi_j'\), given that the state was originally \(\phi_j\), is \(P_{ij}(t) = |a_{ij}(t)|^2\). The quantities \(|a_{ij}(t)|^2\) are often referred to as transition probabilities. In this case, however, the name is a misnomer, since it carries the connotation that the original state \(\phi_j'\) is transformed into a mixture (of the \(\phi_j'\) weighted by \(P_{ij}(t)\)), and gives the erroneous impression that the quantum formalism itself implies the existence of quantum-jumps (stochastic processes) independent of acts of observation. This is incorrect since there is still a pure state \(\sum_i a_{ij}(t) \phi_j'\) with phase relations between the \(\phi_j'\), and expectations of operators other than the energy must be calculated from the superposition and not the mixture.

---

There is another case, however, the one usually encountered in fact, where the transition probability concept is somewhat more justified. This is the case where the perturbation is due to interaction of the system \((s_{1})\) with another system \(s_{2}\) , and not simply a time dependence of \(s_{1}\) 's Hamiltonian as in the case just considered. In this situation the interaction produces a composite system state, for which there are in general no independent subsystem states. However, as we have seen, for purposes of calculating expectations of operators on \(s_{1}\) alone, we can regard \(s_{1}\) as being represented by a certain mixture. According to this picture the states of subsystem \(s_{1}\) are gradually converted into mixtures by the interaction with \(s_{2}\) and the concept of transition probability makes some sense. Of course, it must be remembered that this picture is only justified so long as further measurements on \(s_{1}\) alone are contemplated, and any attempt to make a simultaneous determination in \(s_{1}\) and \(s_{2}\) involves the composite state where interference properties may be important.  

An example is a hydrogen atom interacting with the electromagnetic field. After a time of interaction we can picture the atom as being in a mixture of its states, so long as we consider future measurements on the atom only. But in actuality the state of the atom is dependent upon (correlated with) the state of the field, and some process involving both atom and field could conceivably depend on interference effects between the states of the alleged mixture. With these restrictions, however, the concept of transition probability is quite useful and justified.

---

## CHAPTER VI. DISCUSSION  

We have shown that our theory based on pure wave mechanics, which takes as the basic description of physical systems the state function- - - supposed to be an objective description (i.e. in one- - one, rather than statistical, correspondence to the behavior of the system)- - - can be put in satisfactory correspondence with experience. We saw that the probabilistic assertions of the usual interpretation of quantum mechanics can be deduced from this theory, in a manner analogous to the methods of classical statistical mechanics, as subjective appearances to observers- - - observers which were regarded simply as physical systems subject to the same type of description and laws as any other systems, and having no preferred position. The theory is therefore capable of supplying us with a complete conceptual model of the universe, consistent with the assumption that it contains more than one observer.  

Because the theory gives us an objective description, it constitutes a framework in which a number of puzzling subjects (such as classical. level phenomena, the measuring process itself, the inter- relationship of several observers, questions of reversibility and irreversibility, etc.) can be investigated in detail in a logically consistent manner. It supplies a new way of viewing processes, which clarifies many apparent paradoxes of the usual interpretation- - - indeed, it constitutes an objective framework in which it is possible to understand the general consistency of the ordinary view.  

We shall now resume our discussion of alternative interpretations. There has been expressed lately a great deal of dissatisfaction with the present form of quantum theory by a number of authors, and a wide variety of new interpretations have sprung into existence. We shall now attempt to classify briefly a number of these interpretations, and comment upon them.

---

Восстановлено, уставом оно есть установка, само настройка за установку  одно устройство как встроенное устройство, устройство, устройство, устройство, устройство, устройство, устройство, устройств, устройство, устройство, устройство, устройство, устройство, устройство, устройства, устройство, устройство, устройство, устройство, устройство, устройство,  устройство, устройство, устройство, устройство, устройство, устройство, устройства, устройство, устройство, устройство, устройство, устройство, устройство, 

1Such as that of Einstein, Rosen, and Podolsky [8], as well as as the paradox of the introduction. 

- устройство, устройство, устройство, устройство, устройство, устройство, устройстве, устройство, устройство, устройство, устройство, устройство, устройство, 
- устройство, устройство, устройство, устройство, устройство, устройство, 
 устройство, устройство, устройство, устройство, устройство, устройство, 
 устройства, устройство, устройство, устройство, устройство, устройство, 
 устройство. 

- устройство, устройство, устройство, устройства, устройство, устройство, устройство,
 устройство, устройство, устройство, устройство, устройство, устройство, устрой
 устройство, устройство, устройство, устройство, устройство, устройство, устройс
 устройство, устройство, устройство, устройство, устройство, устройство, 
  устройство, устройство, устройство, устройство, устройство, устройство, 
   устройство, устройство, устройство, устройство, устройство, устройство, 
    устройство, устройство, устройство, устройство, устройство, устройство, 
     устройство, устройство, устройство, устройство, устройство, устройство, 
      устройство, устройство, устройство, устройство, устройство, устройство, 
       устройство, устройство, устройство, устройство, устройство, устройство, 
        устройство, устройство, устройство, устройство, устройство, устройство, 
         устройство, устройство, устройство, устройство, устройство, устройство, 
          устройство, устройство, устройство, устройство, устройство, устройство, 
           устройство, устройство, устройство, устройство, устройство, устройство, 
            устройство, устройство, устройство, устройство, устройство, устройство, 
             устройство, устройство, устройство, устройство, устройство, устройство, 
              устройство, устройство, устройство, устройство, устройство, устройство, 
               устройство, устройство, устройство, устройство, устройство, устройство, 
                устройство, устройство, устройство, устройство, устройство, устройство, 
                 устройство, устройство, устройство, устройство, устройство, устройство, 
                  устройство, устройство, устройство, устройство, устройство, устройство, 
                   устройство, устройство, устройство, устройство, устройство, устройство, 
                    устройство, устройство, устройство, устройство, устройство, устройство, 
                     устройство, устройство, устройство, устройство, устройство, устройство, 
                      устройство, устройство, устройство, устройство, устройство, устройство, 
                       устройство, устройство, устройство, устройство, устройство, устройство, 
                        устройство, устройство, устройство, устройство, устройство, устройство, 
                         устройство, устройство, устройство, устройство, устройство, устройство, 
                          устройство, устройство, устройство, устройство, устройство, устройство, 
                           устройство, устройство, устройство, устройство, устройство, устройство, 
                            устройство, устройство, устройство, устройство, устройство, устройство, 
                             устройство, устройство, устройство, устройство, устройство, устройство, 
                              устройство, устройство, устройство, устройство, устройство, устройство, 
                               устройство, устройство, устройство, устройство, устройство, устройство, 
                                устройство, устройство, устройство, устройство, устройство, устройство, 
                                 устройство, устройство, устройство, устройство, устройство, устройство, 
                                  устройство, устройство, устройство, устройство, устройство, устройство, 
                                   устройство, устройство, устройство, устройство, устройство, устройство, 
                                    устройство, устройство, устройство, устройство, устройство, устройство, 
                                     устройство, устройство, устройство, устройство, устройство, устройство, 
                                      устройство, устройство, устройство, устройство, устройство, устройство, 
                                       устройство, устройство, устройство, устройство, устройство, устройство, 
                                        устройство, устройство, устройство, устройство, устройство, устройство, 
                                         устройство, устройство, устройство, устройство, устройство, устройство, 
                                          устройство, устройство, устройство, устройство, устройство, устройство, 
                                           устройство, устройство, устройство, устройство, устройство, устройство, 
                                            устройство, устройство, устройство, устройство, устройство, устройство, 
                                             устройство, устройство, устройство, устройство, устройство, устройство, 
                                              устройство, устройство, устройство, устройство, устройство, устройство, 
                                               устройство, устройство, устройство, устройство, устройство, устройство, 
                                                устройство, устройство, устройство, устройство, устройство, устройство, 
                                                 устройство, устройство, устройство, устройство, устройство, устройство, 
                                                  устройство, устройство, устройство, устройство, устройство, устройство, 
                                                   устройство, устройство, устройство, устройство, устройство, устройство, 
                                                    устройство, устройство, устройство, устройство, устройство, устройство, 
                                                     устройство, устройство, устройство, устройство, устройство, устройство, 
                                                        устройство, устройство, устройство, устройство, устройство, устройство, 
                                                                 устройство, устройство, устройство, устройство, устройство, устройство,

---

a. The "popular" interpretation. This is the scheme alluded to in the introduction, where \(\psi\) is regarded as objectively characterizing the single system, obeying a deterministic wave equation when the system is isolated but changing probabilistically and discontinuously under observation.  

In its unrestricted form this view can lead to paradoxes like that mentioned in the introduction, and is therefore untenable. However, this view is consistent so long as it is assumed that there is only one observer in the universe (the solipsist position—Alterna- tive 1 of the introduction). This consistency is most easily understood from the viewpoint of our own theory, where we were able to show that all phenomena will seem to follow the predictions of this scheme to any observer. Our theory therefore justifies the personal adoption of this probabilistic interpretation, for purposes of making practical predictions, from a more satisfactory framework.  

b. The Copenhagen interpretation. This is the interpretation developed by Bohr. The \(\psi\) function is not regarded as an objective description of a physical system (i.e., it is in no sense a conceptual model), but is regarded as merely a mathematical artifice which enables one to make statistical predictions, albeit the best predictions which it is possible to make. This interpretation in fact denies the very possibility of a single conceptual model applicable to the quantum realm, and asserts that the totality of phenomena can only be understood by the use of different, mutually exclusive (i.e. "complementary") models in different situations. All statements about microscopic phenomena are regarded as meaningless unless accompanied by a complete description (classical) of an experimental arrangement.

---

While undoubtedly safe from contradiction, due to its extreme conservatism, it is perhaps overcautious. We do not believe that the primary purpose of theoretical physics is to construct "safe" theories at severe cost in the applicability of their concepts, which is a sterile occupation, but to make useful models which serve for a time and are replaced as they are outworn.2  

Another objectionable feature of this position is its strong reliance upon the classical level from the outset, which precludes any possibility of explaining this level on the basis of an underlying quantum theory. (The deduction of classical phenomena from quantum theory is impossible simply because no meaningful statements can be made without pre- existing classical apparatus to serve as a reference frame.) This interpretation suffers from the dualism of adhering to a "reality" concept (i.e., the possibility of objective description) on the classical level but renouncing the same in the quantum domain.  

c. The "hidden variables" interpretation. This is the position (Alternative 4 of the introduction) that \(\psi\) is not a complete description of a single system. It is assumed that the correct complete description, which would involve further (hidden) parameters, would lead to a deterministic theory, from which the probabilistic aspects arise as a result of our ignorance of these extra parameters in the same manner as in classical statistical mechanics.  

The \(\psi\) - function is therefore regarded as a description of an ensemble of systems rather than a single system. Proponents of this interpretation include Einstein,3 Bohm,4 Wiener and Siegal.5 Einstein hopes that a theory along the lines of his general relativity, where all of physics is reduced to the geometry of

---

smožno osti za elektro-izvještajne "zašljene" odgovarajući na sastavu i prostornoštrujeći na to podnijeti, smećeva zaštita koji razvijavajući vlasništvo od zaštite od neke neke neke neke neke neke neke neke neke neke neka neke neke neke neke neke neke neke neke neke neki neke neke neke neke neke neke neke neke neke neku neke neke neke neke neke neke neke neke neke nekes neke neke neke neke neke neke neke neke neke neks neke neke neke neke neke neke neke neke neke nekas neke neke neke neke neke neke neke neke neke neker neke neke neke neke neke neke neke neke neke nekar neke neke neke neke neke neke neke neke neke neket neke neke neke neke neke neke neke neke neke neken neke neke neke neke neke neke neke neke neke neked neke neke neke neke neke neke neke neke neke nekem neke neke neke neke neke neke neke neke neke nekee neke neke neke neke neke neke neke neke neke nekk neke neke neke neke neke neke neke neke neke nekne neke neke neke neke neke neke neke neke neke neeke neke neke neke neke neke neke neke neke neke neek neke neke neke neke neke neke neke neke neke nekei neke neke neke neke neke neke neke neke neke nekel neke neke neke neke neke neke neke neke neke nekle neke neke neke neke neke neke neke neke neke nekl neke neke neke neke neke neke neke neke neke nekm neke neke neke neke neke neke neke neke neke nekey neke neke neke neke neke neke neke neke neke neky neke neke neke neke neke neke neke neke neke nekie neke neke neke neke neke neke neke neke neke neike neke neke neke neke neke neke neke neke neke nekin neke neke neke neke neke neke neke neke neke nekan neke neke neke neke neke neke neke neke neke nekeh neke neke neke neke neke neke neke neke neke ne ke neke neke neke neke neke neke neke neke neke ne kene neke neke neke neke neke neke neke neke neke nee neke neke neke neke neke neke neke neke neke ne e neke neke neke neke neke neke neke neke neke ne ka neke neke neke neke neke neke neke neke neke ne kes neke neke neke neke neke neke neke neke neke ne kem neke neke neke neke neke neke neke neke neke ne ker neke neke neke neke neke neke neke neke neke ne ki neke neke neke neke neke neke neke neke neke ne l neke neke neke neke neke neke neke neke neke nele neke neke neke neke neke neke neke neke neke ne le neke neke neke neke neke neke neke neke neke nebe neke neke neke neke neke neke neke neke neke nekt neke neke neke neke neke neke neke neke neke nekte neke neke neke neke neke neke neke neke neke neko neke neke neke neke neke neke neke neke neke neve neke neke neke neke neke neke neke neke neke newe neke neke neke neke neke neke neke neke neke neje neke neke neke neke neke neke neke neke neke nehe neke neke neke neke neke neke neke neke neke ne he neke neke neke neke neke neke neke neke neke neye neke neke neke neke neke neke neke neke neke nepe neke neke neke neke neke neke neke neke neke nefe neke neke neke neke neke neke neke neke neke nege neke neke neke neke neke neke neke neke neke nekg neke neke neke neke neke neke neke neke neke nega neke neke neke neke neke neke neke neke neke neha neke neke neke neke neke neke neke neke neke nekh neke neke neke neke neke neke neke neke neke neja neke neke neke neke neke neke neke neke neke neji neke neke neke neke neke neke neke neke neke nekj neke neke neke neke neke neke neke neke neke nejk neke neke neke neke neke neke neke neke neke ne jneke neke neke neke neke neke neke neke neke neke nene neke neke neke neke neke neke neke neke neke neng neke neke neke neke neke neke neke neke neke ne je neke neke neke neke neke neke neke neke neke ne ja neke neke neke neke neke neke neke neke neke ne

---

space- time, could satisfactorily explain quantum effects. In such a theory a particle is no longer a simple object but possesses an enormous amount of structure (i.e., it is thought of as a region of space- time of high curvature). It is conceivable that the interactions of such "particles" would depend in a sensitive way upon the details of this structure, which would then play the role of the "hidden variables." However, these theories are non- linear and it is enormously difficult to obtain any conclusive results. Nevertheless, the possibility cannot be discounted.  

Bohm considers \(\mathcal{W}\) to be a real force field acting on a particle which always has a well- defined position and momentum (which are the hidden variables of this theory). The \(\mathcal{W}\) - field satisfying Schrödinger' equation is pictured as somewhat analogous to the electromagnetic field satisfying Maxwell's equations, although for systems of \(M\) particles the \(\mathcal{W}\) - field is in a \(3m\) - dimensional space. With this theory Bohm succeeds in showing that in all actual cases of measurement the best predictions that can be made are those of the usual theory, so that no experiments could ever rule out his interpretation in favor of the ordinary theory. Our main criticism of this view is on the grounds of simplicity- - if one desires to hold the view that \(\mathcal{W}\) is a real field then the associated particle is superfluous since, as we have endeavored to illustrate, the pure wave theory is itself satisfactory.  

Wiener and Siegal have developed a theory which is more closely tied to the formalism of quantum mechanics. From the set \(N\) of all non- degenerate linear Hermitian operators for a system having a complete set of eigenstates, a subset \(I\) is chosen such that no two members of \(I\) commute and every element outside \(I\) commutes with at least one element of \(I\) . The set \(I\) therefore contains precisely one operator for every orientation of the principal axes of the Hilbert space for the system. It is postulated that each of the operators of \(I\) corresponds to an independent observable which can take any of the real numerical values of the spectrum of the operator. This theory, in

---

анортик аст ас ош  ноясто-истного мост азал унвостромн астн  •  галъ аъастд тои оь аъ  •  ноясто-истного азалтгоу ас аст,  •  малъаъуасано  •  галъаъ  тоистного аст аъ аъастнн  •  ноясто-истног  то асогнуу  уннннн  аст  ноии  •  аъастного  галъаъ  то  унстдаастнн  аст  аъ  то  аъогоа  аъ  аъастног  а  •  тоу аъогоа ноии  аъогоа  аъастн  аъама  аст  аъ  тоу  •  ноясто-исто  аъа  аъ  аъогоа  аъастн  аъама  аъаст  аъама  аъама  аъама  аъама  аъаама  аъама  аъама  аъама  ааама  аъама  аъама  аъама  •  аъама  аъама  аъама  аъа  аъама  аъама  аъама  аъа ма  аъама  аъама  аъама  аъа аъама  аъама  аъама  аъама аъама  аъама  аъама  аъама 

## 6 For an example of this type of theory see Einstein and Rosen [9]. 

аст аъ аъаст  •  ноясто-исто ннст  аъ аъастнн  аъама  аъама  аъама  аъаъа  аъаъа  аъаъа  аъаъа  •  аъаъа  аъаъа  аъаъа  Аъаъа  аъаъа  аъаъа  аъъаъа  аъаъа  аъаъа  аъ аъаъа  аъаъа  аъаъа  ааъаъа  аъаъа  аъаъа  аъ  аъаъа  аъаъа  аъаъа  оъаъа  аъаъа  аъаъа  аъоъа  аъаъа  аъаъа  аъаъ  аъаъа  аъаъа  аъаъа аъаъа  аъаъа  аъаъа  аьаъа  аъаъа  аъаъа  аъааъа  аъаъа  аъаъа  аъаьа  аъаъа  аъаъа  аъаъа аьаъа  аъаъа  аъаъа  аьаьа  аъаъа  аъаъа  аъаьа аъаъа  аъаъа  аъаъа  оьаъа  аъаъа  аъаъа  аъоьа  аъаъа  аъаъа  аъаъ  оьаъа  аъаъа  аъаъа  оьаьа  аъаъа  аъаъа  аъоьа аъаъа  аъаъа  аъаъа аъоьа  аъаъа  аъаъа  аьоьа  аъаъа  аъаъа  аъаьоьа  аъаъа  аъаъа  аъоьоьа  аъаъа  аъаъа  аъьоьа  аъаъа  аъаъа  аъъоьа  аъаъа  аъаъа  аъьаъа  аъаъа  аъаъа  аъьоьоьа  аъаъа  аъаъа  аьъоьа  аъаъа  аъаъа  аъъаъоьа  аъаъа  аъаъа  аъоъоьа  аъаъа  аъаъа  аъэоьоьа  аъаъа  аъаъа  аэоьоьа  аъаъа  аъаъа  оъэоьоьа  аъаъа  аъаъа аъэоьоьа  аъаъа  аъаъоьа  аъэоьоьа  аъаъа  аъэоьоьа  аъэоьоьа  аъэоьоьа аъэоьоьа  аъэоьоьа  аэоьоьа  аъэоьоьа  аъээоьоьа  аъэоьоьа  аъэзоьоьа  аъэоьоьа  аъэээоьоьа  аъэээоьоьа  аээоьоьа  аъэээоьоьа  оъэоьоьа  аъэээоьоьа  оээоьоьа  аъэээоьоьа  эээоьоьа  аъэээоьоьа  еээоьоьа  аъэээоьоьа  ёээоьоьа  аъэээоьоьа  ьээоьоьа  аъэээоьоьа  йээоьоьа  аъэээоьоьа  кээоьоьа  аъэээоьоьа  лээоьоьа  аъэээоьоьа  мээоьоьа  аъэээоьоьа  нээоьоьа  аъэээоьоьа  пээоьоьа  аъэээоьоьа  рээоьоьа  аъэээоьоьа  зээоьоьа  аъэээоьоьа  цээоьоьа  аъэээоьоьа  чээоьоьа  аъэээоьоьа  щээоьоьа  аъэээоьоьа  шээоьоьа  аъэээоьоьа  сээоьоьа  аъэээоьоьа  тээоьоьа  аъэээоьоьа  фээоьоьа  аъэээоьоьа  хээоьоьа  аъэээоьоьа  дээоьоьа  аъэээоьоьа  жээоьоьа  аъэээоьоьа  яээоьоьа  аъэээоьоьа  иээоьоьа  аъэээоьоьа  юээоьоьа  аъэээоьоьа  уээоьоьа  аъэээоьоьа  вээоьоьа  аъэээоьоьа  гээоьоьа  аъэээоьоьа  дуээоьоьа  аъэээоьоьа  зуээоьоьа  аъэээоьоьа  нуээоьоьа  аъэээоьоьа  хуээоьоьа  аъэээоьоьа  суээоьоьа  аъэээоьоьа  туээоьоьа  аъэээоьоьа  таээоьоьа  аъэээоьоьа  саээоьоьа  аъэээоьоьа  чаээоьоьа  аъэээоьоьа  шаээоьоьа  аъэээоьоьа  хаээоьоьа  аъэээоьоьа  каээоьоьа  аъэээоьоьа  гаээоьоьа  аъэээоьоьа  жаээоьоьа  аъэээоьоьа  баээоьоьа  аъэээоьоьа  ваээоьоьа  аъэээоьоьа  раээоьоьа  аъэээоьоьа  заээоьоьа  аъэээоьоьа  наээоьоьа  аъэээоьоьа  маээоьоьа  аъэээоьоьа  паээоьоьа  аъэээоьоьа  лаээоьоьа  аъэээоьоьа  меээоьоьа  аъэээоьоьа  леээоьоьа  аъэээоьоьа  сеээоьоьа  аъэээоьоьа  тоээоьоьа  аъэээоьоьа  теээоьоьа  аъэээоьоьа  пеээоьоьа  аъэээоьоьа  цеээоьоьа  аъэээоьоьа  тиээоьоьа  аъэээоьоьа  шеээоьоьа  аъэээоьоьа  гиээоьоьа  аъэээоьоьа  шиээоьоьа  аъэээоьоьа  гуээоьоьа  аъэээоьоьа  фиээоьоьа  аъэээоьоьа  куээоьоьа  аъэээоьоьа  буээоьоьа  аъэээоьоьа  вуээоьоьа  аъэээоьоьа  бээоьоьа  аъэээоьоьа  биээоьоьа  аъэээоьоьа  виээоьоьа  аъэээоьоьа  муээоьоьа  аъэээоьоьа  выээоьоьа  аъэээоьоьа  веээоьоьа  аъэээоьоьа  воээоьоьа  аъэээоьоьа  неээоьоьа  аъэээоьоьа  ноээоьоьа  аъэээоьоьа  люээоьоьа  аъэээоьоьа  лиээоьоьа  аъэээоьоьа  миээоьоьа  аъэээоьоьа  диээоьоьа  аъэээоьоьа  сиээоьоьа  аъэээоьоьа  пиээоьоьа  аъэээоьоьа  риээоьоьа  аъэээоьоьа  киээоьоьа  аъэээоьоьа  роээоьоьа  аъэээоьоьа  соээоьоьа  аъэээоьоьа  коээоьоьа  аъэээоьоьа  поээоьоьа  аъэээоьоьа  доээоьоьа  аъэээоьоьа  проээоьоьа  аъэээоьоьа  комээоьоьа  аъэээоьоьа  приээоьоьа  аъэээоьоьа  прээоьоьа  аъэээоьоьа  преээоьоьа  аъэээоьоьа  праээоьоьа  аъэээоьоьа  предээоьоьа  аъэээоьоьа  презээоьоьа  аъэээоьоьа  просээоьоьа  аъэээоьоьа  продээоьоьа  аъэээоьоьа  предоээоьоьа  аъэээоьоьа  предложээоьоьа  аъэээоьоьа  предусээоьоьа  аъэээоьоьа  предлагаээоьоьа  аъэээоьоьа  предполагаээоьоьа  аъэээоьоьа  предприээоьоьа  аъэээоьоьа  предположиээоьоьа  аъэээоьоьа  прогнээоьоьа  аъэээоьоьа  пропнээоьоьа  аъэээоьоьа 

6 For an example of this type of theory see Einstein and Rosen [9].

---

its present form, is a theory of infinitely many "hidden variables," since a system is pictured as possessing (at each instant) a value for every one of these "observables" simultaneously, with the changes in these values obeying precise (deterministic) dynamical laws. However, the change of any one of these variables with time depends upon the entire set of observables, so that it is impossible ever to discover by measurement the complete set of values for a system (since only one "observable" at a time can be observed). Therefore, statistical ensembles are introduced, in which the values of all of the observables are related to points in a "differential space," which is a Hilbert space containing a measure for which each (differential space) coordinate has an independent normal distribution. It is then shown that the resulting statistical dynamics is in accord with the usual form of quantum theory.  

It cannot be disputed that these theories are often appealing, and might conceivably become important should future discoveries indicate serious inadequacies in the present scheme (i.e., they might be more easily modified to encompass new experience). But from our viewpoint they are usually more cumbersome than the conceptually simpler theory based on pure wave mechanics. Nevertheless, these theories are of great theoretical importance because they provide us with examples that "hidden variables" theories are indeed possible.  

d. The stochastic process interpretation. This is the point of view which holds that the fundamental processes of nature are stochastic (i.e., probabilistic) processes According to this picture physical systems are supposed to exist at all times in definite states, but the states are continually undergoing probabilistic changes. The discontinuous probabilistic "quantum-jumps" are not associated with acts of observation, but are fundamental to the systems themselves.

---

a  n o w  n i  ,  a t o o t i t e  n u n i n a p  n i s i t i t e  v i l t o r o t a t i t a t a  h i n o  ,  n u n i -  o o a q e  n e  a s s e a n o o o t  t u n  ,  t o o l i o  a l c i n i t e  a  t e n n o i  o n  a l  a l o i t t e a q  a  v i o o n i t  t o  n o i t o r  a  n a  t o  t i n i o o r t  a l  t i  ,  s . s . )  a n n u n t a t a  t o  t n o u n e  n o n n o n e  -  t a n t i  a r t  t a n t  a l d i n v i s e n o o  a l  t i  ,  ( a n u n t a v i o  n i n i t  t o  a n i t -  o o a q e  n u n  n o u  v a w  a v i t i t a n o e  a  n i  h a n a n o  h i n o w  n e a n t a r t a q  n o u  t o  a n o i t o s  a r t  t o  a l o r  a r t  v a l i  n o r t  h i n o w  n e a n t a r t  a l i n t  t o  a l i s t o h  t i  h a n  n a n o i t - n o n  a t a  a e l i n o o a t  t a a r t  ,  t a v o w o n i  ,  a e l i d a t a n  n a h i n  t i  -  a n t i t a v o w  ,  a t i t a n e v a l i n o o n  n u n  n i s t o t o  a t  t i n o i t i t h  v l a v i o n o n e  a l  -  h o n t n o o o t i h  a d  o n n o n  t i t i t o i t a a q  a n t  ,  a e a t  a l o t t a n a q  a n o  n u n i t o s  h i n o i t  h a n o  a t  o n  o t  ,  a n o h i n a n o  n i n o t  a l o t t a n o  n i n o t  a n i n o t  a l o t t a n o  n i n o  t i n o t  a n i n o t  a l o t t a n  n i n o t  a n i n o t  a l o t t  a n i n o t  a n i n o t  a l o t t a  n i n o t  a n i n o t  a l o t t t a n  n i n o t  a n i n o t  a n i n o t  a n i n o t

---

A stochastic theory which emphasizes the particle, rather than wave, aspects of quantum theory has been investigated by Bopp. The particles do not obey deterministic laws of motion, but rather probabilistic laws, and by developing a general "correlation statistics" Bopp shows that his quantum scheme is a special case which gives results in accord with the usual theory. (This accord is only approximate and in principle one could decide between the theories. The approximation is so close, however, that it is hardly conceivable that a decision would be practically feasible.)  

Bopp's theory seems to stem from a desire to have a theory founded upon particles rather than waves, since it is this particle aspect (highly localized phenomena) which is most frequently encountered in present day high- energy experiments (cloud chamber tracks, etc.). However, it seems to us to be much easier to understand particle aspects from a wave picture (concentrated wave packets) than it is to understand wave aspects (diffraction, interference, etc.) from a particle picture.  

Nevertheless, there can be no fundamental objection to the idea of a stochastic theory, except on grounds of a naked prejudice for determinism. The question of determinism or indeterminism in nature is obviously forever undecidable in physics, since for any current deterministic [probabilistic] theory one could always postulate that a refinement of the theory would disclose a probabilistic [deterministic] substructure, and that the current deterministic [probabilistic] theory is to be explained in terms of the refined theory on the basis of the law of large numbers [ignorance of hidden variables]. However, it is quite another matter to object to a mixture of the two where the probabilistic processes occur only with acts of observation.  

e. The wave interpretation. This is the position proposed in the present thesis, in which the wave function itself is held to be the fundamental entity, obeying at all times a deterministic wave equation.

---

This view also corresponds most closely with that held by Schrodinger. However, this picture only makes sense when observation processes themselves are treated within the theory. It is only in this manner that the apparent existence of definite macroscopic objects, as well as localized phenomena, such as tracks in cloud chambers, can be satisfactorily explained in a wave theory where the waves are continually diffusing. With the deduction in this theory that phenomena will appear to observers to be subject to Process 1, Heisenberg's criticism of Schrodinger's opinion- - - that continuous wave mechanics could not seem to explain the discontinuities which are everywhere observed- - - is effectively met. The "quantum- jumps" exist in our theory as relative phenomena (i.e., the states of an object- system relative to chosen observer states show this effect), while the absolute states change quite continuously.  

The wave theory is definitely tenable and forms, we believe, the simplest complete, self- consistent theory.  

We should like now to comment on some views expressed by Einstein. Einstein's criticism of quantum theory (which is actually directed more against what we have called the "popular" view than Bohr's interpretation) is mainly concerned with the drastic changes of state brought about by simple acts of observation (i.e., the infinitely rapid collapse of wave functions), particularly in connection with correlated systems which are widely separated so as to be mechanically uncoupled at the time of observation. At another time he put his feeling colorfully by stating that he could not believe that a mouse could bring about drastic changes in the universe simply by looking at it.  

However, from the standpoint of our theory, it is not so much the system which is affected by an observation as the observer, who becomes correlated to the system.  

In the case of observation of one system of a pair of spatially separated, correlated systems, nothing happens to the remote system

---

nast rastrsk, stolbrag and asaknagna nolik vrasn vtskionos A  oit  ,,gno, vn bostavstvni nad zad vrasn misnno to sasoga, ovav  ,,stor vrasti nit, nolik to vrad, staknivnastvni vdo to on stolbrag  ,,nastakn stolbragno, latsnag, staknivnag, vn nas, vrad, staknid  ,,av savn nolik sano laskoga a ki snodno nutnno, art vnat, vnok, gno 

9 Schrödinger [18]. 

10 Heisenberg [14]. 

11 Einstein [7]. 

12 For example, the paradox of Einstein, Rosen, and Podolsky  [8]. 

13 Address delivered at Palmer Physical Laboratory, Princeton,  Spring, 1954. 

nob ot ot nolikogo starinabnii on od nas vrasti, naslovnogo  ot obshchego boga so vnosov, so vogo vnosov, vlasnogo so  vrasn na nekimstveni so nekimstveni so nekimstveni  vnosov vas ot oslo, naslovni na vlasnogo vnosov vlasnogo a  nad oslavnogo avvala blino oni vnosov, oslovni vlasnogo  ,,nastabnii, oslovnogo, a oslovni, blino vnosov, oslovni, a  ,,desnii, oslovnogo, vlasnogo, oni vnosov, oslovni, a  na vrasn boshkov oni so vrasn na vlasnogo od so v vnosov, oslovni  ,,vlasnogo, vlasnogo, oslovni, a  ,,vlasnogo, oslovni, a  ,,vlasnogo, oslovnogo, oslovni, a  ,,vlasnogo, oslovnogi, oslovni, a  ,,vlasnogo, oslovnogi, a  ,,vlasnogo, oslovnogi, oslovni, oslovni, a  ,,vlasnogo, oslovnogi, vlasnogo, oslovni, oslovni, a  ,,vlasnogo, oslovo, oslovni, a  ,,vlasnogo, oslovo, oslovo, oslovni, a  ,,vlasnogo, oslovni, a, oslovni, a  ,,vlasnogo, oslovni, a oslovni, a  ,,vlasnogo, oslovni, a oslovo, a  ,,vlasnogo, oslovni, a oslovo, oslovo, oslovo, a  ,,vlasnogo, oslovni, a oslovni, oslovo, oslovo, oslovo, a  ,,vlasnog, oslovni, a oslovo, oslovo, oslovo, oslovo, oslovo, oslovo  ,,vlasnogo, oslovni, a oslovo, oslvo, oslovo, oslovo, oslovo, oslovo, oslvo, oslovo, oslovo, oslovo  ,,vlasnogo oslovni, a oslovo, oslovo, oslovo, oslvo, oslovo  ,,vlasnogo oslovni, a oslovo  ,,vlasnogo oslovo, oslovo, oslovo, oslovo, oslovo oslovo, oslovo, oslovo, oslovo, oslovo.

---

to make any of its states more "real" than the rest. It had no independent states to begin with, but a number of states occurring in a superposition with corresponding states for the other (near) system. Observation of the near system simply correlates the observe: to this system, a purely local process- - - but a process which also entails automatic correlation with the remote system. Each state of the remote system still exists with the same amplitude in a superposition; but now a superposition for which element contains, in addition to a remote system state and correlated near system state, an observer state which describes an observer who perceives the state of the near system.14 From the present viewpoint all elements of this superposition are equally "real." Only the observer state has changed, so as to become correlated with the state of the near system and hence naturally with that of the remote system also. The mouse does not affect the universe- - - only the mouse is affected.  

Our theory in a certain sense bridges the positions of Einstein and Bohr, since the complete theory is quite objective and deterministic ("God does not play dice with the universe"), and yet on the subjective level, of assertions, relative to observer states, it is probabilistic in the strong sense that there is no way for observers to make any predictions better than the limitations imposed by the uncertainty principle.15  

In conclusion, we have seen that if we wish to adhere to objective descriptions then the principle of the psycho- physical parallel- - - - - - - - - - - - - - - - - - - - - ism requires that we should be able to consider some mechanical devices as representing observers. The situation is then that such devices must either cause the probabilistic discontinuities of Process 1, or must be transformed into the superpositions we have discussed. We are forced to abandon the former possibility since it leads to the situation that some physical systems would obey different laws from the rest, with no clear means for distinguishing between these two types of systems. We are thus led to our present theory which results from the complete abandonment of Process 1 as

---

v d b i n t a n d i t i w v i s o o i o t r a n a s h n o g a v t r o o o a l a w e t v a n i t  - t a s o o n e n w o n e e . o a n a w i s o o v t a n t o v a n i t , t o v w o n  a t i v o n t a n t o v a n i t a n t i v h o t a n t o v a n i t a n t i v h o t a  - t r o o n a n t a n t i v h o t a n t o v a n i t a  - t r o o n a n t a n t i v h o  t a n t o v a n i t a n t i v h o t a a n t i v h o t a n t i v h o t a n t i v h o t a n t o v a n i t a a n t i v h o t a n t i v h o t a  - t r o o n a n i t a n t i v h o t a n t i v h o t a n i t a n t i v h o t a n t i v h o  t a n t i v h o t a n t i v h o t a n  t a n t i v h o t a n t i v h o t a  - a n t i v h o t a n t i v h o t a n t  - a n t i v h o t a n t i v h o t a  -  a n t i v h o t a n t i v h o t a  - n t i v h o t a n t i v h o t a  -  n t i v h o t a n t i v h o t a  -  t a n t i v h o t a n t i v h o t a 

t o v e l a n o w a n t o t o n e s t a n t o v e l a n t o v e l a n t o v e l a n t o v a n t o v e l a n t o v e l a n t o v o v e l a n t o v e l a n t o v e l a t o v e l a n t o v e l a n t o v e l o v e l a n t o v e l a n t o v e l a v e l a n t o v e l a n t o v e l a n o v e l a n t o v e l a n t o v e l a o v e l a n t o v e l a n t o v e l a a n t o v e l a n t o v e l a a n t o 

14See in this connection Chapter IV, particularly pgs. 87, 88.  e t o m 15cf. Chapter V, § 2.  m o r d 

n i w a n i n t a n t o v e l a n t o v e l a n t o n e s t a n t o v e l a n t o v e n a n t o v e l a n t o v e l a n t o v i s o o v e l a n t o v e l a n t o v e l a s t a n t o v e l a n t o v e l a n t i v h o t a n t i v h o t a n t a n t i v h o t a n t i v h o t a n a n t i v h o t a n t i v h o t a n t 

n o w o n o w o n o w o n o w o n o w o n o w o w o n o w o n o w o n o w o n o w o o w o n o w o n o w o n o w o n o w o  o w o n o w o n o w o n o w o n o w o

---

a basic process. Nevertheless, within the context of this theory, which is objectively deterministic, it develops that the probabilistic aspects of Process 1 reappear at the subjective level, as relative phenomena to observers.  

One is thus free to build a conceptual model of the universe, which postulates only the existence of a universal wave function which obeys a linear wave equation. One then investigates the internal correlations in this wave function with the aim of deducing laws of physics, which are statements that take the form: Under the conditions C the property A of a subsystem of the universe (subset of the total collection of coordinates for the wave function) is correlated with the property B of another subsystem (with the manner of correlation being specified). For example, the classical mechanics of a system of massive particles becomes a law which expresses the correlation between the positions and momenta (approximate) of the particle at one time with those at another time.16 All statements about subsystems then become relative statements, i.e., statements about the subsystem relative to a prescribed state for the remainder (since this is generally the only way a subsystem even possesses a unique state), and all laws are correlation laws.  

The theory based on pure wave mechanics is a conceptually simple, causal theory, which fully maintains the principle of the psychophysical parallelism. It therefore forms a framework in which it is possible to discuss (in addition to ordinary phenomena) observation processes themselves, including the inter- relationships of several observers, in a logical, unambiguous fashion. In addition, all of the correlation paradoxes, like that of Einstein, Rosen and Podolsky, find easy explanation.  

While our theory justifies the personal use of the probabilistic interpretation as an aid to making practical predictions, it forms a broader frame in which to understand the consistency of that interpretation. It transcends the probabilistic theory, however, in its ability to deal logically with questions of imperfect observation and

---

approximate measurement.  

Since this viewpoint will be applicable to all forms of quantum mechanics which maintain the superposition principle, it may prove a fruitful framework for the interpretation of new quantum formalisms. Field theories, particularly any which might be relativistic in the sense of general relativity, might benefit from this position, since one is free to construct formal (non- probabilistic) theories, and supply any possible statistical interpretations later. (This viewpoint avoids the necessity of considering anomalous probabilistic jumps scattered about space- time, and one can assert that field equations are satisfied everywhere and everywhere, then deduce any statistical assertions by the present method.)  

By focusing attention upon questions of correlations, one may be able to deduce useful relations (correlation laws analogous to those of classical mechanics) for theories which at present do not possess known classical counterparts. Quantized fields do not generally possess pointwise independent field values, the values at one point of space- time being correlated with those at neighboring points of space- time in a manner, it is to be expected, approximating the behavior of their classical counterparts. If correlations are important in systems with only a finite number of degrees of freedom, how much more important they must be for systems of infinitely many coordinates.  

Finally, aside from any possible practical advantages of the theory, it remains a matter of intellectual interest that the statistical assertions of the usual interpretation aren't independent hypotheses, but are deducible (in the present sense) from the pure wave mechanics, which results from that conclusion.

---

## APPENDIX I  

We shall now supply the proofs of a number of assertions which have been made in the text.  

## 51. Proof of Theorem 1.  

We now show that \(\{x, y, \ldots , z\} > 0\) unless \(x, y, \ldots , z\) are independent random variables. Abbreviate \(P(x_1, y_1, \ldots , s_k)\) by \(P_{ij \ldots k}\) and let  

\[Q_{ij \ldots k} = \left\{ \begin{array}{cc} \frac{P_{ij \ldots k}}{P_{i} P_{j} \cdots P_{k}} & \text{if } P_{i} P_{j} \cdots P_{k} > 0 \\ 1 & \text{if } P_{i} P_{j} \cdots P_{k} = 0 \end{array} \right. \quad (1.1)\]  

(Note that \(P_{i} P_{j} \cdots P_{k} = 0\) implies that also \(P_{ij \ldots k} = 0\) .) Then always  

\[P_{ij \ldots k} = Q_{ij \ldots k} P_{i} P_{j} \cdots P_{k} \quad (1.2)\]  

and we have  

\[\begin{array}{r l} & {\{x,y,\ldots ,z\} = \mathrm{Exp}\Big[\mathrm{ln}\frac{P_{i j\ldots k}}{P_{i} P_{j}\cdots P_{k}}\Big] = \mathrm{Exp}\Big[\mathrm{ln}Q_{i j\ldots k}\Big]}\\ & {\qquad = \sum_{i\ldots k}P_{i} P_{j}\cdots P_{k}Q_{i j\ldots k}\mathrm{ln}Q_{i j\ldots k}} \end{array} \quad (1.3)\]  

Applying the inequality for \(x \geq 0\) :  

(1.4) \(x \ln x > x - 1\) (except for \(x \geq 1\) )  

(which is easily established by calculation the minimum of \(x \ln x - (x - 1)\) to (1.3) we have:  

\[P_{i} P_{j} \cdots P_{k} Q_{i j \ldots k} \ln Q_{i j \ldots k} > P_{i} P_{j} \cdots P_{k} (Q_{i j \ldots k} - 1) \quad (1.5)\]  

Therefore we have for the sum:

---

\[{\sum_{i,j,k}\mathrm{P}_{i}\mathrm{P}_{j}\cdots\mathrm{P}_{k}\mathrm{Q}_{i j..k}\ln\mathrm{Q}_{i j..k}\geq\sum_{i,j,k}\mathrm{P}_{i}\mathrm{P}_{j}\cdots\mathrm{P}_{i}\mathrm{Q}_{i j..k}\mathrm{-}\sum_{i,j,k}\mathrm{P}_{i}\mathrm{P}_{j}\cdots\mathrm{P}_{\mathrm{k}}}\] \[{\mathrm{unless~all~Q}_{i j..k}=1.~E u t~\sum_{i,j,k}\mathrm{P}_{i}\mathrm{P}_{j}\cdots\mathrm{P_{k}}\mathrm{Q}_{i j..k}=\sum_{i,j,k}\mathrm{P}_{i j..k}=1,~a n d}\] \[{\sum_{i,j,k}\mathrm{P}_{i}\mathrm{P}_{j}\cdots\mathrm P_{k}=1,~s o~t h a t~t h e~r i g h t~s i d e~o f~(\mathrm{1.6})~v a n i s h e s.~T h e}\] \[{\mathrm{l e f t~s i d e~i s,~b y~(\mathrm{1.3})~t h e~c o r r e l a t i o n~\{X,Y,\ldots,Z\},~a n d~t h e~c o n d i t i o n}}\] \[{\mathrm{t h a t~a l l~o f~t h e~Q}_{i j..k}~e q u a l~o n e~i s~p r e c i s e l y~t h e~i n d e p e n d e n c e}}\] \[{\mathrm{c o n d i t i o n~t h a t~P}_{i j..k}=\mathrm{P}_{i}\mathrm{P}_{j}\cdots\mathrm{P}_{k}~f o r~a l l~i,j,\ldots,k.~W e~h a v e}}\] \[{\mathrm{t h e r e f o r e~p r o v e d~t h a t}}\]  

(1.7) \(\{X, Y, \ldots , Z\} > 0\) unless \(X, Y, \ldots , Z\) are mutually independent.  

## §2. Convex Function Inequalities.  

We shall now establish some basic inequalities which follow from the convexity of the function \(x \ln x\) .  

\[\mathrm{L e m m a~l i:} x_{1}\geq 0, P_{1}\geq 0, \sum_{1}^{n}P_{1} = 1\] \[\Rightarrow (\sum_{1}^{n}P_{1}x_{1})\ln (\sum_{1}^{n}P_{1}x_{1})\leq \sum_{1}^{n}P_{1}x_{1}\ln x_{1}\]  

This property is usually taken as the definition of a convex function, but follows from the fact that the second derivative of \(x \ln x\) is positive for all positive \(x\) , which is the elementary notion of convexity. There is also an immediate corrolary for the continuous case:  

\[\mathrm{Corollary~l i:} g(x)\geq 0, P(x)\geq 0, \int P(x) \mathrm{d}x = 1\] \[\Rightarrow \left[\int P(x)g(x) \mathrm{d}x\right] \ln \left[\int P(x)g(x) \mathrm{d}x\right] \leq \int P(x)g(x) \ln g(x) \mathrm{d}x\]  

We can now derive a more general and very useful inequality from Lemma 1:

---

1 See Hardy, Littlewood, and Pólya [13], pg.70.

---

\[\begin{array}{r l}{\mathrm{Lemma~2:}} & {\qquad \mathbf{x}_{1}\geq 0,\quad \mathbf{a}_{1}\geq 0\qquad \mathrm{(a l l~1)}}\\ & {\Rightarrow \left(\sum_{i}\mathbf{x}_{1}\right)\ln \left(\frac{\sum_{i}\mathbf{x}_{1}}{\sum_{i}\mathbf{a}_{1}}\right)\leq \sum_{i}\mathbf{x}_{1}\ln \left(\frac{\mathbf{x}_{1}}{\mathbf{a}_{1}}\right)} \end{array}\]  

Proof Let \(P_{1} = \mathbf{a}_{1} / \sum_{i}\mathbf{a}_{1}\) , so that \(P_{1} \geq 0\) and \(\sum_{i} P_{1} = 1\) . Then by Lemma 1:  

\[\left(\sum_{i} P_{1} \left(\frac{x_{1}}{a_{1}}\right)\right) \ln \left[\sum_{i} P_{1} \left(\frac{x_{1}}{a_{1}} \right)\right] \leq \sum_{i} P_{1} \left(\frac{x_{1}}{a_{1}^{2}}\right) \ln \left(\frac{x_{1}}{a_{1}^{2}}\right) \quad (2.1)\]  

Substitution for \(P_{1}\) yields:  

\[\left[\sum_{i} \left(\frac{a_{1}}{\sum_{i} a_{1}}\right) \left(\frac{x_{1}}{a_{1}}\right)\right] \ln \left[\sum_{i} \left(\frac{a_{1}}{\sum_{i} a_{\alpha}}\right) \left(\frac{x_{1}}{a_{\alpha}}\right)\right] \leq \sum_{i} \left(\frac{a_{1}}{\sum_{i} a_{\alpha}} \right) \left(\frac{x_{1}}{a_{1}}\right) \ln \left(\frac{x_{1}}{a_{1}}\right) \quad (2.2)\]  

which reduces to  

\[\left(\sum_{i} x_{1}\right) \ln \left(\frac{\sum_{i} x_{1}}{\sum_{i} a_{1}}\right) \leq \sum_{i} x_{1} \ln \left(\frac{x_{1}}{a_{1}}\right) \quad (23)\]  

and we have proved the lemma.  

We also mention the analogous result for the continuous case:  

\[\begin{array}{r l r} & {} & {\mathrm{Corollary~2:}\qquad f(x)\geq 0,\quad g(x)\geq 0\qquad \mathrm{(a l l~x)}}\\ & {} & {\Rightarrow \left[f(x)d x\right]\ln \left[\frac{f(x)d x}{g(x)d x}\right]\leq \int f(x)\ln \left[\frac{g(x)}{g(x)}\right]d x} \end{array} \quad (23)\]  

## 3. Refinement Theorems.  

We now supply the proof for theorems 2 and 4 of chapter II, which concern the behavior of correlation and information upon refinement of the distributions. We suppose that the original (unrefined) distribution is \(P_{i j \ldots k} = P(x_{1}, y_{1}, \ldots , x_{k})\) , and that the refined distribution is \(P_{i j \ldots k}^{i j \ldots n}\) , where the original value \(x_{1}\) for \(X\) has been resolved into a number of values \(x_{1}^{i j \ldots k}\) , and similarly for \(Y, \ldots , Z\) . Then:

---

\[P_{ij..k} = \sum_{k' = 1}^{n} P_{ij..k}^{k'}\cdot \dots \cdot P_{i} = \sum_{k' = 1}^{n} P_{i}^{k'}\cdot \dots \quad \text{etc.} \quad (3.1)\]  

Computing the new correlation \(\{x, y, \dots, z\}\) for the refined distribution \(P_{ij..k}^{k'}\) we find:  

\[[x, y, \dots, z] = \sum_{i,j,\dots,k} \sum_{k' = 1}^{n} P_{ij..k}^{k'}. \ln \left( \frac{P_{ij..k}^{k'}}{P_{i}^{k'}.P_{j}^{k'}.P_{k'}^{k'}} \right) \quad (3.2)\]  

However, by Lemma 2, §2:  

\[(\sum_{k' = 1}^{n} P_{i}^{k'}.P_{j}^{k'}) \ln \left( \frac{\sum_{k' = 1}^{n} P_{i}^{k'}.P_{k'}^{k'}}{\sum_{k' = 1}^{n} P_{i}^{k'}.P_{i}^{k'}.P_{k'}^{k'}} \right) \quad (3,3)\]  

Substitution of (3.3) into (3.2), noting that \(\sum_{k' = 1}^{n} P_{i}^{k'}.P_{y}^{k'}.P_{k'}^{k'}\) is equal to \((\sum_{k' = 1}^{n} P_{i}^{k'})(\sum_{j' = 1}^{n} P_{j}^{k'})\dots (\sum_{k' = 1}^{n} P_{k'}^{k'})\) , leads to:  

\[\begin{array}{r l} & {\left\{x,y,\dots,z\right\}^{\prime}\overset {\cong}{\underset{j,\dots,k}{\sum}}\left(\sum_{k^{\prime} = 1}^{n}P_{i j,\dots,k}^{k^{\prime}}\right)\ln \left(\frac{\sum_{k^{\prime} = 1}^{n}P_{i j,\dots,k}^{i^{\prime}}}{(\sum_{k^{\prime}}P_{i}^{k^{\prime}})(\sum_{j^{\prime}}P_{j}^{k^{\prime}})\dots(\sum_{k^{\prime}}P_{k^{\prime}}^{k^{\prime}})}\right)}\\ & {\qquad = \sum_{i,j,\dots,k}\ln \frac{P_{i j,\dots,k}^{k}}{P_{i}^{k}.P_{j}^{k}.P_{k}^{k}} = \left\{x,y,\dots,z\right\}} \end{array} \quad (3.4)\]  

and we have completed the proof of Theorem 2 (Chap.II), which asserts that refinement never decreases the correlation.  

We now consider the effect of refinement upon the relative information. We shall use the previous notation, and further assume that \(a_{i}^{k}, b_{j}^{k}, \dots , c_{k}^{k}\) are the information measures for which we wish to compute the relative information of \(P_{ij..k}^{k'}\) and of \(P_{ij..k}\) . The information measures for the unrefined distribution \(P_{ij..k}\) then satisfy the relations:

---

1 Cf. Shannon [7], appendix 7, where a quite similar theorem is proved.

---

\[a_{1} = \sum_{k} a_{1}^{k} \quad b_{j} = \sum_{k} b_{j}^{k} \quad \dots \quad (3.5)\]  

The relative information of the refined distribution is  

\[I_{X Y..Z} = \sum_{i \cdot j} \sum_{k} \sum_{k} \sum_{k} \ln \left[ \frac{p_{i j..k}^{k} \cdot N_{k}}{a_{i}^{k} b_{j}^{k} \cdot c_{k}^{k} N_{k}} \right] \quad (3.6)\]  

and by exactly the same procedure as we have just used for the correlation we arrive at the result:  

\[I_{X Y..Z} \stackrel {\Delta}{=} \sum_{i \cdot k} P_{i j..k} \ln \frac{P_{i j..k}}{a_{i}^{k} b_{j}^{k} \cdot c_{k}} = I_{X Y..Z} \quad (3.7)\]  

and we have proved that refinement never decreases the relative information (Theorem 4, Chap.II).  

It is interesting to note that the relation (3.4) for the behavior of correlation under refinement can be deduced from the behavior of relative information, (3.7). This deduction is an immediate consequence of the fact that the correlation is a relative information - - the information of the joint distribution relative to the product measure of the marginal distributions.  

§4. Monotone Decrease of Information for Stochastic Processes  

We consider a sequence of transition- probability matrices \(\mathbf{T}_{ij}^{n}\) ( \(\sum_{j} \mathbf{T}_{ij}^{n} = 1\) for all \(n, i\) , and \(0 \leq \mathbf{T}_{ij}^{n} \leq 1\) for all \(n, i, j\) ), and a sequence of measures \(a_{1}^{n}\) (\(a_{1}^{n} \geq 0\)) having the property that  

\[a_{j}^{n + 1} = \sum_{i} a_{i}^{n + 1} \quad (4.1)\]  

We further suppose that we have a sequence of probability dis-

---

- tributions, \(\mathbf{F}_{i}^{n}\) such that  

\[{\bf p}_{j}^{n + 1} = \sum_{i}{\bf p}_{i j}^{n n} \quad (4.2)\]  

For each of these probability distributions the relative information \(\mathbf{I}^{n}\) (relative to the \(\mathbf{a}_{i}^{n}\) measure) is defined:  

\[{\bf I}^{n} = \sum_{i}{\bf p}_{i}^{n}\ln \left(\frac{{\bf p}_{i}^{n}}{{\bf a}_{i}}\right) \quad (4.3)\]  

Under these circumstances we have the following theorem:  

\[I^{n + 1} \leq I^{n}\]  

Proof: Expanding \(\mathbf{I}^{n + 1}\) we get:  

\[{\bf I}^{n + 1} = \sum_{i}{\bf p}_{i}^{n + 1}\ln \left(\frac{{\bf p}_{i}^{n + 1}}{{\bf a}_{i}^{n + 1}}\right) = \sum_{j}\left(\frac{{\bf p}_{i}^{n}}{{\bf a}_{i}^{n + 1}}\right)\ln \left(\frac{{\bf p}_{i}^{n n}}{{\bf a}_{i}^{n + 1}}\right) \quad (4.4)\]  

However, by Lemma 2 ( §2, App.) we have the inequality  

\[\left(\sum_{i}{\bf p}_{i j}^{n n}\right)\ln \left(\frac{\sum_{i}{\bf p}_{i j}^{n n}}{\sum_{i}{\bf a}_{i j}^{n n}}\right)\leq \sum_{i}{\bf p}_{i j}^{n n}\ln \frac{{\bf p}_{i j}^{n n}}{{\bf a}_{i j}^{n n}} \quad (4.5)\]  

Substitution of (4.5) into (4.4) yields:  

\[\begin{array}{r l r}{{\bf I}^{n+1}}&{\leq\sum_{i}\left(\sum_{j}{\bf p}_{i j}^{n n}\right)\ln\frac{{\bf p}_{i}^{n}}{{\bf a}_{i}^{n}}}\\\ &{}&{=\sum_{i}{\bf p}_{i}^{n}\left(\sum_{j}{\bf a}_{i j}^{n n}\right)\ln\left(\frac{{\bf p}_{i}^{n}}{{\bf a}_{i}^{n}}\right)=\sum_{i}{\bf p}_{i}^{n}\ln\left(\frac{{\bf p}_{i}^{n}}{{\bf a}_{i}^{n n}}\right)=\sum_{i}{\bf p}_{i}^{n}}\end{array} \quad (4.6)\]  

and the proof is completed.

---

This proof can be successively specialized to the case where \(\mathbf{T}\) is stationary \((\mathbf{T}_{1j}^{n} = \mathbf{T}_{1j}\) for all \(\mathbf{n}\) ) and then to the case where \(\mathbf{T}\) is doubly- stochastic \((\sum_{1j}^{n} = 1\) for all \(\mathbf{j}\) ):  

Corollary 1: \(\mathbf{T}_{1j}^{n}\) is stationary \((\mathbf{T}_{1j}^{n} = \mathbf{T}_{1j})\) ; all \(\mathbf{n}\) ), and the measure \(\mathbf{a}_{1}\) is a stationary measure \((\mathbf{a}_{1} = \sum_{1j} \mathbf{a}_{1j})\) , imply that the information, \(\mathbf{I}^{n} = \sum_{1j} \mathbf{p}_{1}^{n} \ln (\mathbf{p}_{1}^{n} / \mathbf{a}_{1}^{n})\) , is monotone decreasing. (As before, \(\mathbf{p}_{1}^{n + 1} = \sum_{1j} \mathbf{p}_{1}^{n} \mathbf{p}_{1j}^{n}\) .)  

Proof: Immediate consequence of preceding theorem.  

Corollary 2: \(\mathbf{T}_{1j}\) is doubly- stochastic \((\sum_{1j}^{n} = 1\) , all \(\mathbf{j}\) ) implies that the information relative to the uniform measure \((\mathbf{a}_{1} = 1\) , all \(\mathbf{i}\) ), \(\mathbf{I}^{n} = \sum_{1j} \mathbf{p}_{1}^{j} \ln \mathbf{p}_{1}^{n}\) , is monotone decreasing.  

Proof: For \(\mathbf{a}_{1} = 1\) (all \(\mathbf{i}\) ) we have that \(\sum_{1j} \mathbf{a}_{1j} = \sum_{1j} \mathbf{a}_{1j} = 1 = \mathbf{a}_{1}\) . Therefore the uniform measure is stationary in this case and the result follows from Corollary 1.  

These results hold for the continuous case also, and may be easily verified by replacing the above summations by integrations, and by replacing Lemma 2 by its corollary.  

§5. Proof of Special Inequality for Chap. IV. (1.7).  

Lemma: Given probability densities \(\mathbf{P}(\mathbf{r}), \mathbf{P}_{1}(\mathbf{x}), \mathbf{P}_{2}(\mathbf{r})\) , with \(\mathbf{P}(\mathbf{r}) = \int \mathbf{P}_{1}(\mathbf{x}) \mathbf{P}_{2}(\mathbf{r} - \mathbf{x}) \mathrm{d}\mathbf{x}\) . Then \(\mathbf{I}_{R} \triangleq \mathbf{I}_{X} - \ln \mathbf{r}\) where \(\mathbf{I}_{X} = \int \mathbf{P}_{1}(\mathbf{x}) \ln \mathbf{P}_{1}(\mathbf{x}) \mathrm{d}\mathbf{x}\) and \(\mathbf{I}_{R} = \int \mathbf{P}(\mathbf{r}) \ln \mathbf{P}(\mathbf{r}) \mathrm{d}\mathbf{r}\)  

Proof: We first note that:

---

\[(5.1) \quad \int P_2(r - x \tau) dx = \int P_2(\omega) \frac{d\omega}{\tau} = \frac{1}{\tau} \quad (all r) \quad (5.1)\]  

and that furthermore  

\[(5.2) \quad \int P_2(r - x \tau) d\tau = \int P_2(\omega) d\omega = 1 \quad (all x) \quad (5.2)\]  

We now define the density \(\tilde{\mathbf{F}}^r (x)\) :  

\[(5.3) \quad \tilde{\mathbf{F}}^r (x) = \tau P_2(r - x \tau) \quad (5.3)\]  

which is normalized, by (5.1). Then, according to §2, Corrolary 1 (App.) we have the relation:  

\[(5.4) \quad \left(\int \tilde{\mathbf{F}}^r (x) P_1(x) dx\right) \ln \left(\int \tilde{\mathbf{F}}^r (x) P_1(x)dx\right) \leq \int \tilde{\mathbf{F}}^r (x) P_1(x) \ln P_1(x) dx \quad (5.4)\]  

Substitution from (5.3) gives  

\[(5.5) \quad \left(\tau \int P_2(r - x \tau) P_1(x) dx\right) \ln \left(\tau \int P_2(r - x \tau) P_1(x)dx\right) \quad \leq \tau \int P_2(r - x \tau) P_1(x) \ln P_1(x) dx\]  

The relation \(P(r) = \int P_1(x) P_2(r - x \tau) dx\) , together with (5.5) then implies  

\[(5.6) \quad P(r) \ln \tau P(r) \leq \int P_2(r - x \tau) P_1(x) \ln P_{1}(x) dx \quad (5.6)\]  

which is the same as:  

\[(5.7) \quad P(r) \ln P(r) \leq \int P_2(r - x \tau) P_1(r) \ln P_1(r) dx - P(r) \ln \tau \quad (5.7)\]  

Integrating with respect to \(r\) , and interchanging the order of integration on the right side gives:  

\[(5.8) \quad I_R = \int P(r) \ln P(r) dr \leq \int \int P_2(r - x \tau) dr P_1(x) \ln P_1(x) dx - \int \int P_2(r) dr \quad (5.8)\]  

But using (5.2) and the fact that \(\int P(r) dr = 1\) this means that  

\[(5.9) \quad I_R \leq \int P_1(x) \ln P_1(x) dx - \ln \tau = I_X - \ln \tau \quad (5.9)\]  

and the proof of the lemma is completed.

---

## 56. Stationary Point of \(I_k + I_x\)  

We shall show that the information sum:  

\[I_{k} + I_{x} = \int_{-\infty}^{\infty}\phi (k)\ln \phi (k)\mathrm{d}k + \int_{-\infty}^{\infty}\psi (x)\ln \psi (x)\mathrm{d}x\] \[\qquad \mathrm{where~}\phi (k) = (1 / \sqrt{2\pi})\int_{-\infty}^{\infty}\mathrm{e}^{-1k x}\psi (x)\mathrm{d}x\]  

is stationary for the functions:  

\[\psi_{0}(x) = (1 / 2\pi \sqrt{x})^{\frac{1}{2}}e^{-x^{2} / 4\sqrt{x}}, \quad \phi_{0}(k) = (2\sqrt{x})^{\frac{1}{2}}e^{-k\sqrt{x}^{2}x} \quad (1.2)\]  

with respect to variations of \(\psi\) , \(\hat{S}\psi\) , which preserve the normalization:  

\[\int_{-\infty}^{\infty}(\psi^{*}\psi)\mathrm{d}x = 0 \quad (1.3)\]  

The variation \(\hat{S}\psi\) gives rise to a variation \(\hat{S}\phi\) of \(\phi (k)\) :  

\[\hat{S}\phi = (1 / \sqrt{2\pi})\int_{-\infty}^{\infty}\mathrm{e}^{-i k x}\hat{S}\psi \mathrm{d}x \quad (1.4)\]  

To avoid duplication of effort we first calculate the variation  

\(\hat{S} I_{\hat{\gamma}}\) for an arbitrary wave function \(u(\hat{\gamma})\) . By definition,  

\[I_{\hat{\gamma}} = \int_{-\infty}^{\infty}u^{*}(\hat{\gamma})u(\hat{\gamma})\ln u^{*}(\hat{\gamma})u(\hat{\gamma})\mathrm{d}\hat{\gamma} \quad (1.5)\]  

so that  

\[\hat{S} I_{\hat{\gamma}} = \int_{-\infty}^{\infty}\left[\int u^{*}u\delta (\ln u^{*}u) + \delta (u^{*}u)\ln u^{*}u\right]\mathrm{d}\hat{\gamma}\] \[\qquad = \int_{-\infty}^{\infty}(1 + \ln u^{*}u)(u^{*}\delta u u\delta u^{*})\mathrm{d}\hat{\gamma}\]  

We now suppose that \(u\) has the real form:  

\[u(\hat{\gamma}) = a e^{-b\hat{\gamma}^{2}} = u^{*}(\hat{\gamma}) \quad (1.7)\]  

and from (1.6) we get  

\[\hat{S} I_{\hat{\gamma}} = \int_{-\infty}^{\infin}(1 + \ln a^{2} - 2b\hat{\gamma}^{2})a e^{-b\hat{\gamma}^{2}}(\hat{S} u)\mathrm{d}\hat{\gamma} + \mathrm{complex~conjugate} \quad (1.8)\]

---

\[S_{\mathrm{I}_{\mathrm{K}}}\Big|_{\mathrm{g}}^{0} = \int_{-\infty}^{\infty}(1 + \ln \mathrm{a}^{2} - 2\mathrm{b}^{2}\mathrm{k}^{2})\mathrm{a}^{2}\mathrm{e}^{-\mathrm{b}^{2}\mathrm{k}^{2}}\int_{\mathrm{2\pi}}^{\infty}\int_{-\infty}^{\infty}\mathrm{e}^{-\mathrm{i}\mathrm{k}\mathrm{x}}\mathrm{S}_{\mathrm{I}_{\mathrm{K}}}^{0}\mathrm{d}\mathrm{x}\mathrm{d}\mathrm{k} + \mathrm{e}.\mathrm{e}.\]  

Interchanging the order of integration and performing the definite integration over k we get:  

\[\mathcal{S}_{\mathrm{I}_{\mathrm{K}}}\Big|_{\mathrm{g}}^{0} = \int_{-\infty}^{0}\int_{0}^{\infty}(\ln \mathrm{a}^{2} + \frac{2}{2\mathrm{b}},) \mathrm{e}^{-\mathrm{i}\mathrm{k}^{2}}\mathrm{S}_{\mathrm{I}_{\mathrm{K}}}^{0}\mathrm{d}\mathrm{x} + \mathrm{e}.\mathrm{e}. \quad (1.10)\]  

while application of (1.8) to \(\psi_{0}\) gives  

\[\mathcal{S}_{\mathrm{I}_{\mathrm{K}}}\Big|_{\mathrm{g}}^{1} = \int_{\infty}^{0}(1 + \ln \mathrm{a}^{2} - 2\mathrm{b}^{2}\mathbf{x}^{2})\mathrm{a}^{2}\mathrm{e}^{-\mathrm{b}^{2}\mathbf{x}^{2}}\mathcal{S}_{\mathrm{I}_{\mathrm{K}}}^{0}\mathrm{d}\mathbf{x} + \mathrm{e}.\mathrm{e}.\] \[\mathrm{where} \mathrm{a}^{n} = (1 / 2\pi \mathrm{v}_{x}^{2})^{\frac{1}{2}}, \mathrm{b}^{n} = (1 / 4\pi_{x}^{2})\]  

Adding (1.10) and (1.11), and substituting for \(\mathbf{a}^{n}, \mathbf{b}^{n}, \mathbf{a}^{m}, \mathbf{b}^{m}\) , yields:  

\[\mathcal{S}(\mathrm{I}_{\mathrm{K}} + \mathrm{I}_{\mathrm{X}})\Big|_{\mathrm{v}_{0}} = (1 - \ln \pi)\int_{-\infty}^{\infty}(1 / 2\pi \mathrm{v}_{x}^{2})^{\frac{1}{2}}\mathrm{e}^{-(x^{2} / 4\mathrm{v}_{x}^{2})}\mathcal{S}_{\mathrm{I}_{\mathrm{K}}}^{0}\mathrm{d}\mathrm{x} + \mathbf{c}.\mathbf{c}. \quad (1.12)\]  

But the integrand of (1.12) is simply \(\psi_{0}(x) \mathcal{S}_{\mathrm{I}_{\mathrm{K}}}^{0}(x)\) , so that  

\[\mathcal{S}(\mathrm{I}_{\mathrm{K}} + \mathrm{I}_{\mathrm{x}})\Big|_{\mathrm{v}_{0}} = (1 - \ln \pi)\Bigg(\int_{-\infty}^{\infty}\mathrm{S}_{\mathrm{I}_{\mathrm{K}}}^{0}\mathrm{d}\mathrm{x} + c.c. \quad (1.13)\]  

Since \(\psi_{0}\) is real, \(\psi_{0} \mathcal{S}_{\mathrm{I}_{\mathrm{K}}}^{0} + c.c. = \psi_{0} \mathcal{S}_{\mathrm{I}_{\mathrm{K}}}^{0} + c.\mathrm{c}.\mathrm{c} = \psi_{0} \mathcal{S}_{\mathrm{I}_{\mathrm{K}}}^{0} \psi_{0} \mathcal{S}_{\mathrm{I}_{\mathrm{K}}}^{0} = \mathcal{S}(\psi_{0} \psi_{0})\) , so that  

\[\mathcal{S}(\mathrm{I}_{\mathrm{K}} + \mathrm{I}_{\mathrm{K}})\Big|_{\mathrm{v}_{0}} = (1 - \ln \pi)\left(\int_{-\infty}^{\infty}\mathcal{S}(\psi_{0} \psi_{0})\mathrm{d}\mathrm{k} = 0\right.\]  

due to the normality restriction (1.3), and the proof is completed.

---

## APPENDIX II  

## Remarks on the Role of Theoretical Physics  

There have been lately a number of new interpretations of quantum mechanics, most of which are equivalent in the sense that they predict the same results for all physical experiments. Since there is therefore no hope of deciding among them on the basis of physical experiments, we must turn elsewhere, and enquire into the fundamental question of the nature and purpose of physical theories in general. Only after we have investigated and come to some sort of agreement upon these general questions, i.e. of the role of theories themselves, will we be able to put these alternative interpretations in their proper perspective.  

Every theory can be divided into two separate parts, the formal part, and the interpretive part. The formal part consists of a purely logico- mathematical structure, i.e., a collection of symbols together with rules for their manipulation, while the interpretive part consists of a set of "associations," which are rules which put some of the elements of the formal part into correspondence with the perceived world. The essential point of a theory, then, is that it is a mathematical model, together with an isomorphism between the model and the world of experience (i.e., the sense perceptions of the individual, or the "real world" depending upon one's choice of epistemology).  

The model nature is quite apparent in the newest theories, as in nuclear physics, and particularly in those fields outside of physics proper, such as the Theory of Games, various economic models, etc., where the degree of applicability of the models is still a matter of considerable doubt. However, when a theory is highly successful and becomes firmly established, the model tends to become identified with "reality" itself, and the model nature of the theory

---

4By isomorphism we mean a mapping of some elements of the model into elements of the perceived world which has the property that the model is faithful, that is, if in the model a symbol A implies a symbol B, and A corresponds to the happening of an event in the perceived world, then the event corresponding to B must also obtain. The word homomorphism would be technically more correct, since there may not be a one- one correspondence between the model and the external world.

---

becomes obscured. The rise of classical physics offers an excellent example of this process. The constructs of classical physics are just as much fictions of our own minds as those of any other theory-- we simply have a great deal more confidence in them. It must be deemed a mistake, therefore, to attribute any more "reality" here than elsewhere.  

Once we have granted that any physical theory is essentially only a model for the world of experience, we must renounce all hope of finding anything like "the correct theory." There is nothing which prevents any number of quite distinct models from being in correspondence with experience (i.e., 'all "correct"), and furthermore no way of ever verifying that any model is completely correct, simply because the totality of all experience is never accessible to us.  

Two types of prediction can be distinguished; the prediction of phenomena already understood, in which the theory plays simply the role of a device for compactly summarizing known results (the aspect of most interest to the engineer), and the prediction of new phenomena and effects, unsuspected before the formulation of the theory. Our experience has shown that a theory often transcends the restricted field in which it was formulated. It is this phenomenon (which might be called the "inertia" of theories) which is of most interest to the theoretical physicist, and supplies a greater motive to theory construction than that of aiding the engineer.  

From the viewpoint of the first type of prediction we would say that the "best" theory is the one from which the most accurate predictions can be most easily deduced-- two not necessarily compatible ideals. Classical physics, for example, permits deductions with far greater ease than the more accurate theories of relativity; and quantum mechanics, and in such a case we must retain them all. It would be the worst sort of folly to advocate that the study of classical physics be completely dropped in favor of the newer theories.

---

It can even happen that several quite distinct models can exist which are completely equivalent in their predictions, such that different ones are most applicable in different cases, a situation which seems to be realized in quantum mechanics today. It would seem foolish to attempt to reject all but one in such a situation, where it might be profitable to retain them all.  

Nevertheless, we have a strong desire to construct a single all- embracing theory which would be applicable to the entire universe. From what stems this desire? The answer lies in the second type of prediction- - - the discovery of new phenomena- - - and involves the consideration of inductive inference and the factors which influence our confidence in a given theory (to be applicable outside of the field of its formulation). This is a difficult subject, and one which is only beginning to be studied seriously. Certain main points are clear, however, for example, that our confidence increases with the number of successes of a theory. If a new theory replaces several older theories which deal with separate phenomena, i.e., a comprehensive theory of the previously diverse fields, then our confidence in the new theory is very much greater than the confidence in either of the older theories, since the range of success of the new theory is much greater than any of the older ones. It is therefore this factor of confidence which seems to be at the root of the desire for comprehensive theories.  

A closely related criterion is simplicity- - - by which we refer to conceptual simplicity rather than ease in use, which is of paramount interest to the engineer. A good example of the distinction is the theory of general relativity which is conceptually quite simple, while enormously cumbersome in actual calculations. Conceptual simplicity, like comprehensiveness, has the property of increasing confidence in a theory. A theory containing many ad hoc constants and restrictions, or many independent hypotheses, in no way impresses us as much as one which is largely free of arbitrariness.

---

It is necessary to say a few words about a view which is sometimes expressed, the idea that a physical theory should contain no elements which do not correspond directly to observables. This position seems to be founded on the notion that the only purpose of a theory is to serve as a summary of known data, and overlooks the second major purpose, the discovery of totally new phenomena. The major motivation of this viewpoint appears to be the desire to construct perfectly "safe" theories which will never be open to contradiction. Strict adherence to such a philosophy would probably seriously stifle the progress of physics.  

The critical examination of just what quantities are observable in a theory does, however, play a useful role, since it gives an insight into ways of modification of a theory when it becomes necessary. A good example of this process is the development of Special Relativity. Such successes of the positivist viewpoint, when used merely as a tool for deciding which modifications of a theory are possible, in no way justify its universal adoption as a general principle which all theories must satisfy.  

In summary, a physical theory is a logical construct (model), consisting of symbols and rules for their manipulation, some of whose elements are associated with elements of the perceived world. The fundamental requirements of a theory are logical consistency and correctness. There is no reason why there cannot be any number of different theories satisfying these requirements, and further criteria such as usefulness, simplicity, comprehensiveness, pictorability, etc., must be resorted to in such cases to further restrict the number. Even so, it may be impossible to give a total ordering of the theories according to "goodness", since different ones may rate highest according to the different criteria, and it may be most advantageous to retain more than one.  

As a final note, we might comment upon the concept of causality. It should be clearly recognized that causality is a property of a

---

model, and not a property of the world of experience. The concept of causality only makes sense with reference to a theory, in which there are logical dependences among the elements. A theory contains relations of the form "A implies B", which can be read as "A causes B", while our experience, uninterpreted by any theory, gives nothing of the sort, but only a correlation between the event corresponding to B and that corresponding to A.

---

[1] D. Bohm; Quantum Theory. Prentice- Hall, New York: 1951
[2] D. Bohm; Phys. Rev. 84, 166, 1952 and 85, 180, 1952
[3] N. Bohr, in Albert Einstein, Philosopher- Scientist. The Library of Living Philosophers, Inc., Vol.7, p.199. Evanston: 1949
[4] N. Bohr; Atomic Theory and the Description of Nature.
[5] F. Bopp; Z. Naturforsch. 2a(4), 202, 1947; 7a 82, 1952; 8a, 6, 1953
[6] J. L. Doob; Stochastic Processes. Wiley, New York: 1953
[7] A. Einstein, in Albert Einstein, Philosopher- Scientist. The Library of Living Philosophers, Inc., Vo1.7, p.665 Evanston: 1949
[8] A. Einstein, B. Podolsky, N. Rosen; Phys. Rev. 47, 777, 1935
[9] A. Einstein, N. Rosen; Phys. Rev. , , 1935
[10] W. Feller; An Introduction to Probability Theory and its Applications. Wiley, New York: 1950
[11] D. ter Haar; Elements of Statistical Mechanics. Rinehart, New York: 1954
[12] P. R. Halmos; Measure Theory. Van Nostrand, New York: 1950
[13] G. H. Hardy, J. E. Littlewood, G. Pólya; Inequalities. Cambridge Univ. Press: 1952
[14] W. Heisenberg, in Niels Bohr and the Development of Physics. McGraw- Hill, p.12. New York: 1955
[15] J. Kelley; General Topology. Van Nostrand, New York: 1955
[16] A. I. Khinchin; Mathematical Foundations of Statistical Mechanics. (Translated by George Gamow) Dover, New York: 1945
[17] J. von Neumann; Mathematical Foundations of Quantum Mechanics (Translated by R. T. Beyer) Princeton Univ. Press: 1955
[18] E. Schrödinger; Brit. J. Phil. Sci. 2, 109, 233, 1952
[19] C. E. Shannon, W. Weaver; The Mathematical Theory of Communication. University of Illinois Press:
[20] N. Wiener, I. E. Siegal; Nuovo Cimento,
[21] P. M. Woodward; Probability and Information Theory. with Applications to Radar. McGraw- Hill, New York: 1953