# Everett -- Continuous Time Recursive Games (draft).pdf

## H. Everett \*  

This paper presents a generalization of the theory of Recursive Games presented in the previous paper [1], to the case of a continuous, rather than discrete, time parameter. It will be shown that the theory of continuous time recursive games can be reduced in a simple manner to the earlier theory. We shall make use of the notation and results of [1] without further explanation.  

A continuous time Recursive Game \(\Gamma\) is a collection of game elements \(\{\Gamma^1 \}\) , with payoff functions of the form:  

\[\mathrm{H}^{1}(\mathbf{x}^{1},\mathbf{r}^{1};\vec{\Gamma}) = \mathrm{p}^{1}\mathrm{e}^{1} + \sum_{j}^{1}\mathrm{q}^{1}\mathrm{J}^{1}\mathrm{r}^{1}\qquad (\sum \mathrm{omits} \mathrm{j} = 1) \quad (1)\]  

where the interpretation is that if the players are playing strategies \(\mathbf{x}^{1}\) , \(\mathbf{r}^{1}\) in \(\Gamma^{1}\) , then in the (infinitesimal) time interval dt the play stops with payoff \(\mathrm{e}^{1}\) with probability \(\mathrm{p}^{1}\mathrm{dt}\) , while with probability \(\mathrm{q}^{1}\mathrm{dt}\) the players move on and play \(\Gamma^{1}\) .  

In such games the players are at each instant playing some strategy, but they are free to change at any time. However, we assume that with all admissible time dependent strategies the probabilities are integrable, i.e., \(\int \mathrm{p}^{1}\mathrm{dt}\) and the \(\int \mathrm{q}^{1}\mathrm{dt}\) always exist. (In any actual game it is simply impossible that the players could change strategies so fast that this condition would not be met.) We furthermore assume that the transition rates \(\mathrm{p}^{1}\) and \(\mathrm{q}^{1}\mathrm{J}\) , as well as the

---

payoffs \(e^{1}\) , are bounded for all strategies, in all elements.  

We shall show that we can, in a simple manner, associate with a discrete time recursive game \(\vec{\Gamma} (\Delta)\) , which, if it has a critical vector, supplies all the information necessary for optimal (or \(\mathbb{C}\) - best) play in \(\vec{\Gamma}\) — i.e., which has the same value, and whose \(\mathbb{C}\) - best strategies furnish \(\mathbb{C}\) - best strategies for \(\vec{\Gamma}\) . Thus the problem of continuous time recursive games is reduced to that of discrete time games which have been studied in [1].  

The reduction to a discrete time game is accomplished as follows: Let \(\Delta\) be a positive number such that \(\Delta (p^{1} + \sum_{j} e^{1j})\) is 1 for all strategies in all elements. (The existence of such a \(\Delta\) is guaranteed by the boundedness of the transition rates.) Then let \(\vec{\Gamma} (\Delta)\) be the discrete time recursive game whose payoff function for the i- th element is:  

\[\vec{\Pi}^{1}(\vec{x}^{1},\vec{r}^{1},\vec{\Gamma}^{1}(\Delta)) = \vec{p}^{1}e^{1} + \sum_{j}q^{1j}\vec{\Pi}^{1}(\vec{a}) \quad (2)\]  

where the numbers are defined from the payoff of \(\vec{\Gamma}\) for the same strategies, given by (1), as follows:  

\[p^{1} = \Delta p^{1},\quad q^{1j} = \Delta q^{1j}(1 + j) \quad (3)\]  

If the discrete recursive game \(\vec{\Gamma} (\Delta)\) so constructed possesses a critical vector, then for every \(\epsilon > 0\) there exists a strategy \(\mathcal{X}^{\epsilon} = \{\vec{x}_{t}^{\epsilon}\}\) for \(P_{1}\) (constructed according to

---

the method of (2.7), [1]). which satisfies the inequalities (2.8) of [1]. We wish to assert that this strategy \(X^{\xi}\) is also \(\xi\) - best in the continuous time game \(\Gamma^{\xi}\) , from which \(\Gamma^{\xi}(\Delta)\) was derived. However, we must first understand how to use \(X^{\xi}\) in \(\Gamma^{\xi}\) , in case it is not a stationary strategy. We shall therefore supply a rule for the unambiguous application of \(X^{\xi}\) to \(\Gamma^{\xi}\) .  

First, we define an event to be anytime the play stops or there is a transition to another element. We define the k- th round to be the time between the occurrence of the k- 1 st event and the k- th event. We then state the rule:  

RULE 1: If \(X^{\xi} = \left\{ \begin{array}{ll} \overline{X}^{\xi} & \text{is an} \xi \text{-best strategy for} \Gamma^{\xi}(\Delta), \\ \text{constructed according to (2.7) of} [1], & \text{then in} \Gamma^{\xi} \\ \text{play at the instant} \Gamma \text{the strategy} \overline{X}^{\xi} & \text{where} \tau = k + 1 + [\overline{X} /\Delta ], \\ \text{with} k \text{the number of the current round, and} [\overline{T} /\Delta ] \text{the} \\ \text{greatest integer} \leq \overline{T} /\Delta \text{ (T measured from commencement of play.)} \end{array} \right.\)  

Thus according to RULE 1 one is always playing an element of the sequence \(\left\{ \begin{array}{ll} \overline{X}^{\xi} & \text{, and changing to the next succeeding element each time that an event occurs and each time that an interval of time of duration \(\Delta\) elapses. Similar considerations hold for \(P_{2}\) , of course. With this understanding of how to play in \(\Gamma^{\xi}\) the strategies \(X\) and \(Y\) which are constructed for \(\Gamma^{\xi}(\Delta)\) we can state:

---

THOREA 1: \(\vec{\Gamma}(\Delta)\) possesses a critical vector \(\vec{\nabla}\) , and \(\epsilon\) - best strategies \(\chi^{\epsilon}, \vec{\nabla}^{\epsilon}\) (constructed according to (2.7) of [1]) \(\Rightarrow \chi^{\epsilon}\) and \(\vec{\nabla}^{\epsilon}\) are also \(\epsilon\) - best in \(\vec{\Gamma}\) , which has a solution with value \(\vec{\nabla}\) .  

PROOF: Let us assume that it is the k- th round and that \(P_{1}\) is playing \(\chi^{\epsilon}\) , and let \(t\) measure the time elapsed since the beginning of the round (k- 1st event). \(P_{1}\) is therefore playing \(\frac{\vec{\nabla}}{\chi_{k+1} + [\vec{\nabla} / \Delta]}\) , which changes only at times \([\vec{\nabla} / \Delta]\) , and for which, according to (2.8) and (2.9) of [1]:  

\[p^{a_{1}e_{1} + \sum_{i}q^{a_{1}j}w^{j}}\geq w^{i} + \mu^{i} - \delta_{k + 1 + [\vec{\nabla} / \Delta]}^{1} \quad (4)\]  

for all \(\vec{r}^{1} \in S_{2}^{1}\) , and for all \(i\) . This implies, according to (3), that  

\[p^{1}e^{1} + \sum_{j}q^{1j}w^{j}\geq (p^{1} + \sum_{j}q^{1j})w^{1} + \frac{1}{\Delta}\mu^{1} - \frac{1}{\Delta}\delta_{k + 1 + [\vec{\nabla} / \Delta]}^{1}\quad (5)\]  

for all \(\vec{r}^{1}\) and all \(i\) . Since (5) holds for all \(\vec{r}^{1}\) and all \(i\) , it holds at each instant of play of \(\vec{\nabla}\) .  

We are now interested in the ultimate outcome of the k- th round, regardless of the time involved, and wish to compute the probabilities \(\vec{\nabla}_{k}^{1}\) , \(\vec{\nabla}_{k}^{1j}\) ( \(i \neq j\) ) for the various possible ultimate outcomes of the k- th round. We can then view the course of play as a discrete stochastic process which takes place only with each event, in which time is eliminated.

---

Whatever strategy \(\gamma = \gamma (t) - P_2\) is playing, the transition rates \(p^1, q^{1j}\) , as well as the payoffs \(e^1\) are functions of the time subject to (5), Let us restrict our attention to the i- th element, and let \(n(t)dt\) be the probability of an event in the time interval dt, so that the transition rate \(n(t)\) is:  

\[n(t) = p^1 (t) + \sum_j q^{1j} (t) \quad (6)\]  

Furthermore, let \(R(t)\) be the probability that the k- th event has not yet occurred at time \(t\) (Note: \(t\) measured from beginning of k- th round). Then clearly \(R(t)\) is monotone decreasing, bounded between 0 and 1, and satisfies the relation:  

\[\int_{0}^{t} R(\tau) n(\tau) d\tau = 1 - R(t) \quad (7)\]  

The probability that by time \(t\) the k- th round will have resulted in a stop, \(\bar{p}^1 (t)\) , is  

\[\bar{p}^1 (t) = \int_0^t R(\tau) p^1 (\tau) d\tau \quad (8)\]  

while the probability that it will have resulted in a transition to \(\bar{n}^j\) , \(\bar{q}^{1j}(t)\) , is  

\[\bar{q}^{1j}(t) = \int_0^t R(\tau) q^{1j}(\tau) d\tau \quad (9)\]  

Finally, if \(\bar{\bar{\sigma}}^1 (t) = (\int_0^t R(\tau) p^1 (\tau) e^1 (\tau) d\tau) / (\int_0^t R(\tau) p^1 (\tau) d\tau)\) denotes the mean payoff (which is, of course, bounded by any bounds for \(e^1\) ), then we can write the total expected payoff as:  

\[\bar{p}^1 (t) \bar{\sigma}^1 (t) = \int_0^t R(\tau) p^1(\tau) e^1(\tau) d\tau \quad (10)\]

---

However, making use of (5), we have that for the k- th round, in the i- th element, under \(\mathcal{X}^{\epsilon}\) and for all \(\vec{\mathcal{Y}} (t)\) ;  

\[\begin{array}{r l r}{{\mathbb{P}^{1}(t)\vec{\mathbb{E}}^{1}(t)+\sum_{j}\vec{\mathbb{Q}}^{1}\vec{\mathbb{J}}(t)\vec{\mathbb{W}}\vec{\mathbb{J}}=\int_{\mathbb{R}(\mathbb{Z})}^{\mathbb{T}}\mathbb{P}^{1}(\mathbb{Z})\mathbb{e}^{1}(\mathbb{Z})d\mathbb{Z}+\sum_{j}\vec{\mathbb{W}}\int_{\mathbb{R}(\mathbb{Z})}^{\mathbb{T}}\mathbb{Q}^{1}\vec{\mathbb{J}}(\mathbb{Z})d\mathbb{Z}}}\\ &{}&{=\int_{\mathbb{R}(\mathbb{Z})}^{\mathbb{T}}\left[\mathbb{P}^{1}(\mathbb{Z})\mathbb{e}^{1}(\mathbb{Z})+\sum_{j}\vec{\mathbb{Q}}^{1}\vec{\mathbb{J}}(\mathbb{Z})\vec{\mathbb{W}}\right]d\mathbb{Z}}\\ &{}&{\cong\int_{\mathbb{R}(\mathbb{Z})}^{\mathbb{T}}\left[\mathbb{n}(\mathbb{Z})\vec{\mathbb{W}}^{1}+\frac{1}{\mathbb{Z}}\vec{\mathbb{A}}^{1}-\frac{1}{\mathbb{Z}}\mathbb{S}_{k+1+}^{1}\left[\vec{\mathbb{Z}}/\mathbb{A}\right]\right]d\mathbb{Z}}\end{array} \quad (12)\]  

so that, using (7):  

\[\begin{array}{r l r}{{\mathbb{P}^{1}(t)\mathbb{E}^{1}(t)+\sum_{j}\vec{\mathbb{Q}}^{1}\vec{\mathbb{J}}^{1}(t)\vec{\mathbb{W}}\vec{\mathbb{J}}\geq\left[\mathbb{I}-\mathbb{R}(t)\right]\vec{\mathbb{W}}^{1}+\frac{1}{\mathbb{Z}}\vec{\mathbb{A}}^{i}\left(\int_{\mathbb{R}(\mathbb{Z})}^{\mathbb{T}}\vec{\mathbb{R}}(\mathbb{Z})d\mathbb{Z}\right)}}\\ &{}&{-\frac{1}{\mathbb{Z}}\int_{\mathbb{R}(\mathbb{Z})}^{\mathbb{T}}\mathbb{S}_{k+1+}^{1}\left[\vec{\mathbb{Z}}/\vec{\mathbb{A}}\right]d\mathbb{Z}}\end{array} \quad (12)\]  

Now by the construction (2.7) of [1] \(\begin{array}{r l r}{5_{k + 1 + }^{1}\left[\vec{\mathbb{Z}} /\vec{\mathbb{A}}\right]\cong \left(\vec{\mathbb{H}}\right)^{k + 1 + }\left[\vec{\mathbb{Z}} /\vec{\mathbb{A}}\right]5} \end{array}\) so that, since \(\mathbb{R}(\mathbb{Z})\) is bounded by \(\mathbb{1}_{\mathbb{A}}\) and certainly \(\mathbb{Z}\notin \mathbb{T}\) we have that \(\begin{array}{r}{\int_{\mathbb{R}(\mathbb{Z})}^{\infty}\mathbb{S}_{k + 1 + }^{1}\left[\mathbb{Z} / \mathbb{A}\right]d\mathbb{Z}\cong \mathbb{S}_{(\frac{1}{\mathbb{Z}} )}^{(\frac{1}{\mathbb{Z}} )}k + 1 + \left[\mathbb{Z} / \mathbb{A}\right]d\mathbb{Z}} \end{array}\) \(\begin{array}{r}{\dot{\mathbb{S}} (\frac{1}{\mathbb{Z}})^{k + 1}\triangle \sum_{n = 0}^{\infty}(\frac{1}{\mathbb{Z}})^{n} = \Delta (\frac{1}{\mathbb{Z}})^{k}\mathbb{S}} \end{array}\) , and therefore the ultimate transition probabilities \(\vec{\mathbb{P}}_{k}^{1}\) and \(\vec{\mathbb{Q}}_{k}^{1j}\) for the k- th round, which are given by the limit of (12) as \(t \to \infty\) , satisfy:  

\[\vec{\mathbb{Y}}_{k}^{1}\vec{\mathbb{e}}_{k}^{1} + \sum_{j}\vec{\mathbb{Q}}_{k}^{1j}\vec{\mathbb{W}}\vec{\mathbb{J}}\cong \left[1 - \mathbb{R}(\infty)\right]\vec{\mathbb{W}}^{1} + \frac{1}{\mathbb{Z}}\vec{\mathbb{A}}^{1}\left(\int_{\mathbb{R}(\mathbb{Z})}^{\infty}\mathbb{R}(\mathbb{Z})d\mathbb{Z}\right) - \left(\frac{1}{\mathbb{Z}}\right)^{k}\mathbb{S} \quad (13)\]  

We now observe that if \(\vec{\mathbb{W}}^{1} > 0\) (which implies \(\vec{\mathbb{U}}^{1} > 0\) ) that \(\mathbb{R}(\mathbb{Z})\) must be zero, since otherwise \(\int_{\mathbb{R}(\mathbb{Z})}^{\infty}\mathbb{R}(\mathbb{Z})d\mathbb{X}\) would be infinite ( \(\mathbb{R} \in \mathbb{V}\) ) and the left side of (13) would be infinite, an impossibility for bounded \(\vec{\mathbb{e}}^{1}\) and finite \(\vec{\mathbb{W}}^{1}\) . Therefore if \(\vec{\mathbb{W}}^{1}\) is positive \(\left[1 - \mathbb{R}(\infty)\right]\vec{\mathbb{W}}^{1} = \vec{\mathbb{W}}^{1}\) , while if \(\vec{\mathbb{W}}^{1} \cong 0\) then \(\left[1 - \mathbb{R}(\infty)\right]\vec{\mathbb{W}}^{1}\cong \vec{\mathbb{W}}^{1}\) . Hence (13) implies that

---

\[\nabla_{\mathbf{p},\mathbf{k}}^{\mathrm{i}\epsilon \mathbf{i}} + \sum_{j}\mathbf{\bar{q}}_{\mathbf{k},\mathbf{j}}^{\mathrm{i}\mathbf{j}}\mathbf{w}^{\mathrm{j}}\geq \mathbf{w}^{\mathrm{i}} + \frac{1}{\Delta}\mathbf{u}^{\mathrm{i}}(\int_{0}^{\infty}\mathbf{R}(\mathbf{z})\mathrm{d}\mathbf{z}) - (\frac{1}{\mathbf{\Lambda}})^{\mathbf{k}}5 \quad (14)\]  

Finally, since \(\Delta\) was chosen so that \(\Delta (p^{\mathrm{i}} + \sum_{j}q^{\mathrm{i}}j) \leq 1\) , for all strategies in all elements, we have that \(\Delta n(\mathbf{z}) \leq 1\) for all \(\mathbf{z}\) , so that \(\int_{0}^{\mathbf{t}}\mathbf{R}(\mathbf{z})n(\mathbf{z})\mathrm{d}\mathbf{z} = 1 - \mathbf{R}(\mathbf{t}) \leq \int_{0}^{\mathbf{t}}\mathbf{R}(\mathbf{z})\frac{1}{\Delta}\mathrm{d}\mathbf{z} = \frac{1}{\Delta}\int_{0}^{\mathbf{t}}\mathbf{R}(\mathbf{z})\mathrm{d}\mathbf{z}\) . Therefore \(\frac{1}{\Delta}\int_{0}^{\infty}\mathbf{R}(\mathbf{z})\mathrm{d}\mathbf{z} \geq 1 - \mathbf{R}(\infty)\) . But since \(\mathbf{u}^{\mathrm{i}} = 0\) unless \(\mathbf{w}^{\mathrm{i}} > 0\) , and because \(\mathbf{w}^{\mathrm{i}} > 0\) implies \(\mathbf{R}(\infty) = 0\) , we can conclude that \(\frac{1}{\Delta}\mathbf{u}^{\mathrm{i}}(\int_{0}^{\infty}\mathbf{\bar{R}}(\mathbf{z})\mathrm{d}\mathbf{z}) \geq \mathbf{u}^{\mathrm{i}}\) . It then follows from (14) that under \(\mathcal{L}^{\epsilon}\) and for any \(\gamma\) :  

\[\nabla_{\mathbf{p},\mathbf{k}}^{\mathrm{i}\epsilon \mathbf{i}}\mathbf{\Sigma} + \sum_{j}\mathbf{\bar{q}}_{\mathbf{k},\mathbf{j}}^{\mathrm{i}}\mathbf{w}^{\mathrm{j}}\geq \mathbf{w}^{\mathrm{i}} + \mathbf{\Sigma}\mathbf{u}^{\mathrm{i}} - (\frac{1}{\mathbf{\Lambda}})^{\mathbf{k}}5 \quad (15)\]  

Similar analysis holds for each element, so that (15) holds for all i.  

This expression (15) involving the ultimate transition probabilities and expected payoffs for the k- th round is formally equivalent to the expressions (2.8), (2.9) of [1]. But if we form matrices \(P_{\mathbf{k}}\) , \(Q_{\mathbf{k}}\) , and vectors \(\vec{E}_{\mathbf{k}}\) from \(\vec{\mathbf{p}}_{\mathbf{k}}^{\mathrm{i}}\) , \(\vec{q}_{\mathbf{k}}^{\mathrm{i}\mathbf{j}}\) and \(\vec{\mathbf{e}}_{\mathbf{k}}^{\mathrm{i}}\) by the formulas (1.2) of [1] then the formulas (1.3), (1.4) of [1] for the expectation are applicable to our case. Therefore the proof of Theorem 1, [1], is also applicable, and we can conclude that the ultimate expectation for \(\mathcal{X}^{\epsilon}\) satisfies  

\[\Xi \mathbf{x}(\mathbf{x}^{\epsilon},\mathbf{y})\geq \mathbf{w}^{\epsilon} - \epsilon \mathbf{1} \quad (16)\]  

Since \(\mathbf{w}^{\mathrm{i}}\) is \(\in \mathbb{R}_{\epsilon}(\mathbf{v})\) , the strategy \(\mathcal{X}^{\epsilon}\) is 2E- best for \(P_{1}\) . Reversal of the roles of the players shows the same for \(P_{2}\) , and the theorem is proved.

---

Theorem 1 is easily generalized to the case of continuous time stochastic games, which are games \(\vec{\Gamma}\) whose elements \(\vec{\Gamma}^1\) have payoffs of the form  

\[\mathrm{H}^{1}(\mathbf{x}^{1},\mathbf{y}^{1};\vec{\Gamma}) = \mathrm{e}^{1} + \mathrm{p}^{1}\mathrm{S} + \sum_{j}\mathrm{q}^{1}\mathrm{j}\vec{\Gamma}\mathrm{j}\]  

where the interpretation is that if the players are playing \(\mathbf{x}^{1},\mathbf{y}^{1}\) in \(\vec{\Gamma}^{1}\) , then in time dt a payoff \(\mathrm{e}^{1}\mathrm{dt}\) takes place, and with probability \(\mathrm{p}^{1}\mathrm{dt}\) play stops while with probability \(\mathrm{q}^{1}\mathrm{dt}\) there is a transition to \(\vec{\Gamma}^{1}\) . \(\mathrm{e}^{1}\) is in this case a rate of payoff which is going on at all times (accumulating throughout the course of play) until play stops. Theorem 1 then goes through directly with substitution of \(\mathrm{e}^{1}\) for \(\mathrm{p}^{1}\) in all formulas (E for \(\vec{\mathrm{P}}\vec{\mathrm{E}}\) ), and we have  

THEOREM 2: Theorem 1 holds for continuous time stochastic games.  

Finally, we remark that there is no difficulty in handling recursive (or stochastic) games in which some elements are discrete time games and the others continuous. One simply reduces the continuous time game elements to discrete time elements in the manner presented here, leaving the discrete time elements unaltered.  

A supply of examples may be obtained easily from the examples of [1] by suitable reinterpretation of probabilities as transition rates.  

## References  

[1] Everett, H., "Recursive Games", this study,