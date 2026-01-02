# Everett -- Recursive Games 1955.pdf

Annals of Mathematics StudiesNumber 39

---

Copyright © 1957, by Princeton University Press  London: Oxford University Press  All Rights Reserved  L. C. Card 57- 5460  

The 5 years ago stand- join with the w 5, 1957) of th  

Since GAMES, Volume 3 developed in the certain classes publish the ex- ture and con- tions of this s of us large a c- c- lution- like r THORI OF GAMES  

There in Volumes I and is planned to l- new book of R. Survey (Wiley theory and a b  

The Princeton Univ Project sponsor Composition. tom M. Frank, Thompson, A. b D. Scrokovitz, M. Petiakoff,  

The referencing was: "Gutowry, J. i

---

1. tion.  

## PREFACE  

The Theory of Games that John von Neumann created some thirty years ago stands as one of many lasting monuments to his great genius. We join with the whole scientific world in mourning the untimely loss (February 8, 1957) of this giant of modern mathematics.  

Since the publication in 1953 of CONTRIBUTIONS TO THE THEORY OF GAMES, Volume II (Annals of Mathematics Study 28), work in game theory has developed in two principal directions. One has been the investigation of certain classes of infinite two- person zero- sum games, not only to establish the existence of solutions but also to describe their detailed nature and construction. The present Study is devoted mainly to contributions of this sort. Other research has been directed toward the solution of as large a class of n- person games as possible, or the proposal of new solution- like notions. Such work is to appear in CONTRIBUTIONS TO THE THEORY OF GAMES, Volume IV (Annals of Mathematics Study 40).  

There is no general bibliography in this Study to supplement those in Volumes I and II (Annals of Mathematics Studies 24 and 28). Instead, it is planned to have such a bibliography in Volume IV (Study 40). Also, the new book of R. D. Luce and H. Raiffa, GAMES AND DECISION- An Introductory Survey (Wiley 1957), contains an excellent contemporary survey of game theory and a bibliography.  

The editing and preparing of this Study have been done partly at Princeton University in the Department of Mathematics through a Logistics Project sponsored by the Office of Naval Research, and partly at the RAND Corporation. Princeton Project members who participated in the task have been M. Frank, J. H. Griesmer, H. W. Kuhn, R. Z. Norman, M. Sion, G. L. Thompson, A. W. Tucker, and Philip Wolfe. RAND participants have been L. D. Berkovitz, A. W. Boldyreff, M. Dresher, O. Gross, O. Helmer, S. Johnson, M. Peisakoff, H. Scarf, and L. S. Shapley.  

The following additional persons have generously assisted in the refereeing work: D. Blackwell, H. Everett, W. H. Fleming, R. Isaacs, J. P. Mayberry, J. Nash, R. Restrepo, J. Robinson, and D. V. Widder. The typing

---

PREFACE 

of the master copy has been done by Mrs. Euthie Anthony with efficient care.
To all these, and to the Princeton University Press through its Director,
H. S. Bailey, Jr., the Editors express sincere thanks. 

M. Dresher 

A. W. Tucker 

P. Wolfe 

Preface 

Introduc 

Paper 1 

2 

3 

4 

5 

6 

7 

8 

9 

10 

11 

12 

13 

14 

15

---

ith efficient care,  th its Director,  

## CONTENTS  

Dresher W. Tucker Wolfe  

Preface v Introduction 1  

PART I: Moves as Plays of Other Games  

Paper 1. On Games of Survival 15  

By J. Milnor and L. S. Shapley  

2. Recursive Games 47 By H. Everett  

3. Finitary Games 79 By J. R. Isbell  

4. Approximation to Bayes Risk in Repeated Play 97 By James Hannan  

5. Information in Games With Finite Resources 141 By David Gale  

PART II: Games With Perfect Information  

6. Effective Computability of Winning Strategies 147 By Michael O. Rabin  

7. The Banach-Mazur Game and Banach Category Theorem 159 By John C. Oxtoby  

8. Topological Games With Perfect Information 165 By Claude Berge  

9. Stochastic Games With Zero Stop Probabilities 179 By Dean Gillette  

10. Cartesian Products of Termination Games 189 By John C. Holladay  

11. A Study of Simple Games Through Experiments On Computing Machines 201 By W. Walden  

PART III: Games With Partial Information  

12. Games With Partial Information 213 By H. E. Scarf and L. S. Shapley  

13. A Discrete Evasion Game 231 By L. E. Dubins  

14. An Infinite Move Game With a Lag 257 By Samuel Karlin  

15. The Effect of Psychological Attitudes on The Outcomes of Games 273 By John G. Kemeny and Gerald L. Thompson

---

CONTENTS 

PART IV: Games With a Continuum of Strategies 

Paper 16. On a Game Without a Value
By Maurice Sion and Philip Wolfe
299 

17. A Rational Game on The Square
By O. Gross
307 

18. Tactical Problems Involving Several Actions
By Rodrigo Restrepo
313 

19. Multistage Poker Models
By Samuel Karlin and Rodrigo Restrepo
337 

20. On Games Described by Bell Shaped Kernels
By Samuel Karlin
365 

PART V: Games With a Continuum of Moves 

21. On Differential Games With Survival Payoff
By H. E. Scarf
393 

22. A Note on Differential Games of Prescribed Duration
By W. H. Fleming
407 

23. On Differential Games With Integral Payoff
By L. D. Berkovitz and W. H. Fleming
413

---

## INTRODUCTION  

Most of the contributions in this Study deal with infinite twoperson zero- sum games, establishing the existence of solutions and investigating in detail the nature and construction of solutions. The papers fall in two broad categories, those in which the games are presented in "normalized form" and those which exploit the structure of the game given in "extensive form."  

Laying down the necessary definitions for an infinite game in extensive form is not a difficult matter, since it is obviously trivial to relax the usual condition that the number of choices at each move is finite. If plays of infinite length are also allowed, it is sufficient to redefine a play to be a sequence of choices, with the payoff function then defined on such sequences. Simple measurability conditions will ensure the existence of an expected payoff for any pair of the players' pure strategies, given probability distributions at each of the umpire's choices. The normalized form for such a game can then be obtained, once the sets of pure strategies for the two players have been described as appropriate measure spaces, by defining mixed strategies as probability measures over these spaces. Mixed strategies can be obtained from behavior strategies as product measures in the usual manner.  

Most of the previous research on infinite games has taken as its object games that are in normalized form with a continuum of pure strategies for each player. If this continuum is taken as a unit interval, as is usually the case, the set of all joint outcomes constitutes a unit square and the payoff function can be taken simply as a function on the unit square. Thus the phrase "game on the unit square" describes a two- person zero- sum game defined by a measurable function \(K(x, y), 0 \leq x, y \leq 1\) , in which the two players select \(x\) and \(y\) independently, each in ignorance of the other's choice, following which the player selecting \(y\) pays the other the amount \(K(x, y)\) . All games having continua of pure strategies can be regarded as games on the unit square, but the setting up of \(K\) will require special handling if the extensive structure of the game involves a more complicated information pattern than mere independent selection of \(x\) and \(y\) .

---

In any case, the basic question asked about these infinite games is: Do they have optimal strategies (or, at least, "e- optimal strategies" for arbitrarily small \(\epsilon\) )? The early example of Ville showed that a rather simple game on the square need not have a value. He gave also the first general theorem of a positive nature: A game on the unit square possesses optimal strategies if it has a continuous payoff function K. The positive results that have been obtained along these lines are not a great deal stronger. Glicksberg has shown that e- optimal strategies exist if the payoff function is upper- or lower- semicontinuous, results which can be refined somewhat by the use of a theorem of Kneser on mixed strategies. Karlin has obtained related extensions in terms of the behavior of the payoff function as the kernel of an integral transformation.  

Although these results establish the existence of a value and of optimal strategies for some games in extensive form treated in this Study, they are too weak to settle these questions for most of them. Many of these games, formulated to model game- like situations drawn from other fields, have payoffs which are too "pathological" to allow treatment by very general methods, and detailed use must be made of their particular extensive structures.  

Most of the games studied, moreover, belong to the broad class of "multi- move" games: infinite games which are built up out of a set of "components" which are games or game- like structures, themselves of finite length. If one component of such a set is prescribed as a "start", and the outcome of each of the components is an instruction to play another component of the set, possibly together with a numerical payoff, then the entire infinite game is recursively defined by the set of rules for the components. An extraordinary variety of types of infinite games- - each presenting a unique problem to the theorist- - results from the specification of various information patterns and payoffs for the infinite game.  

Part I is devoted to games built out of repeated play of simultaneous- move games. That is, it is supposed that each component is already a game in normalized form, each player being uninformed of the other's

---

present choice but completely informed of all choices made in components previously played- - and hence knowing in which component he is playing at the moment of choice. The games of Part II are again multinove games, but have perfect information for both players; not only is each player informed of all previous choices, but each component is a game of perfect information. The games of Part III, on the other hand, carry even a weaker information structure than do those of Part I; at the time of choice, a player is only partially informed of the component he is playing. They are games of "information lag". In another direction, the papers of Part IV deal with the oldest type of infinite game- - games given directly in normalized form on the unit square. Finally, Part V consists of contributions to the theory of the important but difficult class of games whose plays are described by a continuum of choices.  

## PART I--Moves as Plays of Other Games  

The games studied in the five papers of this Part have, in various publications, borne the descriptive titles "survival," "ruin," "attrition," "stochastic," "recursive," and "multistage." The study of these games was initiated by a group of mathematicians at the RAND Corporation in 1951. In several unpublished RAND memoranda cited in Paper 1, special cases of the game of survival described in the next paragraph were studied. One involved repeated play of a single two- by- two matrix game by players who begin playing with given initial resources and continue until one player is ruined. Another concerned a similar game having a matrix of arbitrary finite size with integral entries.  

PAPER 1 This line of development has been carried considerably further by Milnor and Shapley in the first paper of this Study. Precisely, two players with initial resources r and R - r agree to play the zero- sum matrix game \(\| a_{i,j}\|\) an unprescribed number of times. If a player is ruined, the game terminates, and the payoff is 1 to the survivor, 0 to the ruined player. Since the transition probabilities are controlled by the participants, and not by chance, it is possible for both players to survive indefinitely, in which case the payoffs are \(Q \geq 0\) and \(1 - Q \geq 0\) , where \(Q\) may be an arbitrary function of the entire course of play. Using a certain game- theoretic functional equation and the theory of semi- martingales, the authors analyze the extent to which the existence of solutions depends on \(Q\) .  

It is shown that, if the game has a value, it can be given as a function of the first player's initial resources and is a monotonic solution of the functional equation

---

\[\mathcal{B}(r) = \mathrm{val}\left\| \mathcal{B}(r + \mathbf{a}_{1j})\right\| \qquad 0< r< R,\]  

with boundary conditions \(\mathcal{B}(r) = 0\) if \(r \leq 0\) and \(\mathcal{B}(r) = 1\) if \(r \geq R\) . In particular, if \(Q = 1\) then the value exists as well as an optimal strategy for the first player. If there are no zeros in \(\| \mathbf{a}_{1j}\|\) , then the value exists and is independent of \(Q\) . In the latter case, optimal strategies exist for both players. If \(\| \mathbf{a}_{1j}\|\) contains zeros, then the existence of a game value depends on the "regularity" of the function \(Q\) .  

PAPER 2 In a "survival game", a payoff accumulates throughout an entire play of the game. In the recursive game developed in this Paper, a payoff occurs only when the game stops. A recursive game is a set of n "game elements", each of which is a two-person game (with no restriction on the cardinality of the players' sets of strategies) whose outcome is either a zero-sum payoff or an instruction that a specified game of the set be played again. Plays of infinite length may thus occur, and are assigned payoff zero. The game is studied by means of its "value mapping": given an n- vector \(\mathbf{v}\) , a zero- sum game is derived from each game element by replacing for each \(i = 1, \ldots , n\) , the outcome "play game element \(i\) next" by the number \(\mathbf{v}_i\) ; the \(n\) values (when they exist) of the games so derived constitute the image of \(\mathbf{v}\) under the value mapping. Everett shows, under the hypothesis that any game derived from a game element has optimal strategies, that the recursive game has a value in stationary strategies- - mixed strategies for the recursive game consisting simply in the employ of the same mixed strategy in each game element. However, optimal strategies may not exist- - only "e- optimal" strategies. If, on the other hand, the games derived from the game elements are assumed only to have values, then the recursive game will still have a value, but not necessarily in stationary strategies. These results are generalized to a type of recursive game in which moves are made continuously, the passage from one game element to its successor taking an infinitesimal time.  

Everett also considers stochastic games, where payoffs take place even though play does not stop. It is no longer true that values must exist. However, several large classes of stochastic games have values. In particular, Everett shows that a stochastic game always has a value when it consists of one element, which can at most repeat itself.  

This paper thus complements the historically important 1953 paper of Shapley, \(^{5}\) which shows the existence of optimal stationary strategies for stochastic games having probability one of terminating in a finite length of time. Everett's results include those of Shapley and also the special cases of survival games described above.

---

0 < r < R,  

if r > R. n optimal jll, then the optimal strategy is the existence of a game.  

out an entire in this Paper, is a set of n restriction on to come is either the set be are assigned ping": given element by re- ment 1 next" games so de- Everett shows, nt has optimal y strategies- the employ of mal strategies r hand, the e values, then ily in sta- of recursive one game ele  

offs take place alues must ex- e values. In a value when  

tant 1953 paper strategies for finite length o the special  

(USA) 39 (1953)  

PAPER 3 In "Finitary games," Isbell gives a variety of results related to the decomposition of a given game into finite game elements and the reconstruction of games from them. He finds first that, employing suitable behavior strategies, the customary condition that a play of a finite game cannot meet a given information set more than once can be removed without losing the existence of optimal strategies in the game. By means of the Kakutani fixed- point theorem, this result can be given in the form of the existence of an equilibrium point for such a finite many- person game. Another result is closely related to those of Papers 1 and 2: A finitary game is composed from a finite number of game elements as is the recursive game of Paper 2, with the provision that all non- terminating plays have the same value to a given player (not necessarily zero). Isbell shows that such a game possesses optimal strategies, although not necessarily stationary ones. Finally he proves a minimax theorem of considerable range for "programming games" having a two- player payoff function which is the quotient of two multilinear forms.  

PAPER 4 In this paper which views repeated play of a single finite game as a statistical decision process, Hannan studies strategy- sequences for player II of a zero- sum two- person game which take advantage of player I's misplay. These strategy- sequences are continuous approximations to the (fictitious play) strategy- sequence which consists in playing against I's cumulative past choice at each play. Hannan exhibits a strategy- sequence for II, using at the \((x + 1)\) st move a Bayes strategy against the sum of I's cumulative past choices and the vector \((3n^2 /2m)^{1 / 2}k^{1 / 2}z\) where \(z\) is chosen at random from the unit m- cube (the original matrix game being m by n). An upper bound is derived for the expected inutility incurred by this strategy for : moves.  

PAPER 5 Studying the role of information in the sequential play of matrix games, Gale analyzes a particular class of games, called games with finite resources, for which the information about the opponent's moves may be omitted without any loss in the game value. In such a game each player is required to play each pure strategy of a given finite game a fixed number of times in any order. The payoff is the sum of the payoffs from the individual plays. Gale shows that in such games it is of no advantage to a player to know which strategies are available to his opponent. Further, it turns out that the uniform mixed strategy is optimal.  

## PART II- Games with Perfect Information  

The five papers that comprise the second part of this Study treat games with perfect information, that is, games in which each player is always

---

informed of the complete previous history of the play. Historically, this was the first category of games in extensive form to be studied. It owes its importance to the result, stated (for the game of Chess) by E. Zermelo and first given a complete proof by J. von Neumann, which asserts that a finite two- person zero- sum game can always be solved by pure strategies without randomization. The basis of this result is clear: At each occasion for a choice, a player selects from among the subgames with perfect information that follow each of the alternatives open to him. If all of the plays are of finite length (i.e., composed of a finite number of choices an induction completes the proof, provided that the result holds for games with but one choice in each play. (A transfinite induction is needed if there is no uniform bound on the length of the plays.) Therefore the theorem is valid as stated in games that offer but a finite number of alternatives at each occasion for a choice, while pure strategies are \(\epsilon\) - optimal in all games with perfect information in which all plays are of finite length.  

PAPER 6 While the question of the existence of winning strategies for infinite games with all plays of finite length and perfect information is thus affirmatively settled, Rabin points out some fundamental problems pertaining to the computability of winning strategies in these games. First, he asks, how are the rules of a game to be given so as to ensure the possibility of actually playing it? The rules must be such that it is possible to ascertain effectively within a finite time (i) whether a move by a player is legal and (ii) whether the payoff from any play can be computed. These requirements are expressed mathematically by stipulating that certain functions are effectively computable (recursive). Rabin thus arrives at a mathematical definition of "actual games," i.e., games which can actually be played. The second problem posed is the analogue for actual games of the basic question for games: Does every actual game (which necessarily possesses optimal strategies) possess optimal strategies which are effectively computable? Using a standard result of recursive function theory, this question is answered in the negative: there exist actual games which have no computable winning strategies. A further theorem indicates that substituting a computer for the player having winning strategies is sometimes the worst possible arrangement. A short description of Turing machines and recursive functions is appended to the paper.  

PAPER 7 The "game of Banach and Mazur" has been part of the folklore of game theory for some time. It is "played" as follows: a subset A of the real line is given, and two players alternately choose nonempty closed bounded intervals of the line in such a way that each interval is a subinterval of the preceding choice. The player who chooses first wins

---

corically, this filed. It owes by E. Zermelo serts that a strategies At each mnes with perfect If all of number of choices holds for games is needed if before the theorem of alterna- re <optimal of finite  

strategies for in- perfect informa- ndamental prob- in these games. as to ensure the that it is whether a move play can be stypulating). Rabin thus , games which logue for tual game imal strategies f recursive there exist further theo- ving winning hort description e paper.  

e folklore of ows: a subset oose nonempty interval is es first wins  

if the intersection of this nest of intervals with A is nonempty; otherwise the other player wins. The theorem conjectured by Mazur and proved by Banach (but never published) asserts that (i) the game is determined in favor of the second player if and only if A is of first category, and (ii) the game is determined in favor of the first player if and only if the complement of A is of first category at some point. A proof of this theorem by Mycielski, Swierczkowski, and Zieba has been announced, and will appear in Fundamenta Mathematica. In the present paper, Oxtoby generalizes the game to an arbitrary topological space in which the players alternately choose sets from a family of sets with nonempty interiors such that every nonempty open set contains set of the family. Under these conditions (i) holds without change, while (ii) is valid if X is a complete metric space. As an intereecting by- product, the Banach category theorem is shown to be a corollary of (i) in an arbitrary topological space.  

PAPER 8 In "Topological games with perfect information" Berge treats a certain class of many- person games with perfect information of the type of "games of pursuit," for which the set X of all "positions" is topologized. Defining the rules and payoff of the game by certain functions on X, the game is called topological if these functions are continuous. It is not required that X be finite, or that a play, which is a sequence of elements of X, be bounded in length. The theorem of Zermelo, von Neumann, and Kuhn on the existence of an equilibrium point in pure strategies is obtained for this game. In addition, Berge gives some topological properties of the function on X whose value at any position in X is the payoff a given player can ensure himself if play starts from that position.  

PAPER 9 In this paper Gillette examines some questions related to a game of infinite length considering repeated play of a finite number of finite zero- sum two- player games of perfect information, the outcome of each of which is a finite payoff and instructions to play another game of the set. Similarly [footnote 5 above] has considered games of this sort for which one- member of the set is a game from which there is no passage to another, subject to the assumption that with probability one every play enters this game. Dropping Shepperl's restriction, Gillette uses as "average" payoff function for the infinite game the expression  

\[\lim_{n\to \infty}\frac{1}{n}\sum_{i = 1}^{n}p_{i} + \dots +p_{n}),\]  

where \(p_{i}\) is the payoff or the occasion of the ith play of a game of the set. Via the auxiliary "discounted" payoff

---

\[\mathrm{s}\Big[\mathrm{p}_0 + (1 - \mathrm{s})\mathrm{p}_1 + \dots +(1 - \mathrm{s})\mathrm{p}_\mathrm{n}\Big] \qquad (0< \mathrm{s}< 1),\]  

which converges to the average payoff as \(\mathrm{s} \longrightarrow 0\) , Gillette relates his game to the stochastic game with positive stop probabilities for which Shapley has shown the existence of a value using "stationary" strategies, i.e., mixed strategies for the infinite game arising from the same mixed strategy at each occurrence of a given member of the collection of finite games. He shows that if all the finite games are games of perfect information, then the infinite game has a solution in stationary pure strategies. In the general case, if for any two finite games there is, regardless of what strategies are used, a positive probability of eventually passing from one to the other, then the game has a solution in stationary mixed strategies. Examples are given which show that these results cannot be extended in certain directions.  

PAPER 10 In this paper Holladay studies certain finite two- person win- lose games of perfect information, called "termination games," typified by the classical game of Nim. They have the properties (1) that, symmetrically, a position can be characterized by a player as "unsafe" or "safe" according as the other player, confronted with it, can win the game or not, and (11) that the player confronted with a terminal position loses. Holladay defines the Cartesian product of n such games \(\{\mathrm{G}_1\}\) to be a game whose positions are n- tuples of positions of the component game, in which a move consists in a move in one of the component positions of a position. He shows that for any termination game \(\mathrm{G}\) there exists a natural- number valued function \(\mathrm{v}_{\mathrm{G}}\) on the positions of \(\mathrm{G}\) such that the position \((\mathrm{p}_1, \dots , \mathrm{p}_n)\) of the product game is safe if and only if the n- tuple \((\mathrm{v}_{\mathrm{G}}(\mathrm{p}_1), \dots , \mathrm{v}_{\mathrm{G}}(\mathrm{p}_n))\) is a safe position in n- pile Nim. This result is extended to other games related to Nim, including Nim played with ordinal numbers.  

PAPER 11 Walden reports here on an empirical study (by means of high- speed computing machinery) of some finite zero- sum two- person games of perfect information played by "players" who use various methods for choosing strategies in the game: the rational player, the player who chooses at random, the player who chooses rationally under the assumption that his opponent will choose at random, and an intermediate type. Outcomes obtained by certain pairs of these players playing 8- and 10- move games whose payoffs (zero- one valued) have been selected at random are plotted as functions of \(\mathrm{p}\) , the proportion of payoff- one positions in the games.  

be looked at perfect information length. Station pattern tailed comes might be how would also tion. The er discover they are ga games with and cannot  

PAPER 12 In this paper Holladay studies certain finite two- person win- lose games of perfect information,called "termination games," typified by the classical game of Nim. They have the properties (i) that, symmetrically, a position can be characterized by a player as "unsafe"or "safe" according as the other player, confronted with it, can win the game or not and (ii) that the player confronted with a terminal position loses. Holladay defines the Cartesian product of nsuch games \(\{\mathrm{G}_1\}\) to be a game whose positions are n- tuples ofpositions of the component game, in which a move consists in a move in one of the component positionsof a position. He shows that for any termination game \(\mathrm{G}\) there exists a natural-  

PAPERs 13 T and 14 P  

special form of a target simplicity, criteria of Here one has arise when t are abandoned unit of dist the moves of

---

(0 < s < 1),  

relates his for which " strategies, e same mixed ion of finite effect in- ry pure strategy is, regard- eventually pass- tationary mix- ults cannot be  

person win- lose games," typified that, symmetri- e" or "safe" he game or not, n loses. 1) to be a ent game, in tions of a po- ists a natural- t the position e n- tuple his result is  

with ordinal  

s of high- speed erson games of ods for choosing chooses at on that his outcomes obtain- games whose lotted as func- games.  

## PART III--Games with Partial Information  

The games discussed in the first three papers of this part may be looked on as falling somewhere between the simplicity of the games of perfect information of Part II and the completely general game of infinite length. Since the repetitive structure and corresponding simple information pattern of the multistage games of Part I permit the drawing of detailed conclusions regarding the nature of their optimal strategies, it might be hoped that a game in which the information was "nearly perfect" would also have some of the tractibility of the game of perfect information. The information patterns considered here are those in which a player discovers his opponent's moves after a certain built- in time delay; they are games of "information lag." Unlike games of perfect information, games with a lag of more than one move cannot be decomposed into subgames, and cannot in general be solved by a series of move- by- move optimizations.  

PAPER 12 In "Games with partial information", Scarf and Shapley introduce certain "generalized subgames" for handling games with information lag. The play of a generalized subgame, considered as a game by itself, begins with a chance move, the results being partially withheld in accordance with the original game's information pattern. The play then continues as in the original game, with the same payoff. The authors show that the values of the generalized subgames, if they exist, satisfy a certain recursive relation which can be used to obtain the value and optimal strategies of the original game. A sufficient condition for the existence of values for the generalized subgames, including the original game, is that there be a finite number of choices at each move, and that the payoff for games of infinite length be an upper- or lower- semicontinuous function of the move sequence.  

PAPERS 13 The game considered by Dubins in Paper 13 and later by Karlin in and 14 Paper 14 is a "pursuit" game played on the integral points of a line, with an information lag of precisely two moves. It is a special form of the classical military problem of predicting the position of a target which is maneuvering to confound prediction. Despite its simplicity, and the fact that the existence of a value is given by the criteria of Paper 12, this game has not been easy to solve explicitly. Here one has an excellent illustration of the technical difficulties which arise when the simple information patterns of the games of Parts I and II are abandoned. At each unit of time, the "evader" may move either one unit of distance to the left or one to the right. The "pursuer", knowing the moves of the evader, has one move: he predicts two units of time in

---

advance the position of the evader. If the pursuer predicts correctly, he receives a payoff of 1; otherwise the payoff is zero. Using different techniques, Dubins and Karlin show that this game has the value \((3 - \sqrt{5}) / 2\) and that the evader has a unique optimal strategy which depends on the previous move only. The evader's optimal strategy is to move in the same direction as his last move with probability \(1 - v\) and make a turn with probability \(v\) .  

For the infinite- move game it is shown that the pursuer possesses no optimal strategy. However, Karlin proves that in the truncated game of \(n\) moves there is a positive probability that the pursuer predicts correctly at each stage.  

PAPER 15 In "The effect of psychological attitudes on the outcomes of game Kemeny and Thompson study the effect on the strategic behavior of the player of a matrix game of his assessment of the game's outcome by means of various transformations on the entries of the matrix. Using a "utility function" \(f\) , a monotone increasing real- valued function of the game payoffs, he plays the game "as it looks to him", employing the optimal strategies for the matrix game obtained from the original game by replacing each entry \(a_{ij}\) with \(f(a_{ij})\) . A complete characterization is possible of those utility functions which are strategy- preserving in the sense that a player's optimal strategies are the same in the transformed game as in the original. Such functions must be either linear or exponential. The author go on to discuss in detail the effects of other types of utility functions, corresponding to attitudes toward gain as "optimistic", "reckless", etc., on a player's strategies and his willingness to enter the game.  

## PART IV-Games with a Continuum of Strategies  

The papers of this part are united more by their use of the tools of ordinary analysis than by a common subject- matter. The games they study are closer to the classical game on the unit square than to games in extensive form, but Papers 18 and 19 make use of the methods developed for both.  

PAPER 16 The theorem of Glicksberg on semicontinuous payoffs has been cited above as a positive general result concerning the existence of a value for a game on the square. That no extensive weakening of the hypothesis of semicontinuity can be made is shown by the example given in this paper by Sion and Wolfe of a game whose payoff is not far from being semicontinuous. The example takes the form of a modified "Colonel Blotto" game whose lack of optimal strategies is perhaps surprising. It is cast,

---

advance the position of the evader. If the pursuer predicts correctly, he receives a payoff of 1; otherwise the payoff is zero. Using different techniques, Dubins and Karlin show that this game has the value \((3 - \sqrt{5}) / 2\) and that the evader has a unique optimal strategy which depends on the previous move only. The evader's optimal strategy is to move in the same direction as his last move with probability \(1 - v\) and make a turn with probability \(v\) .  

For the infinite- move game it is shown that the pursuer possesses no optimal strategy. However, Karlin proves that in the truncated game of \(n\) moves there is a positive probability that the pursuer predicts correctly at each stage.  

PAPER 15 In "The effect of psychological attitudes on the outcomes of game Kemeny and Thompson study the effect on the strategic behavior of the player of a matrix game of his assessment of the game's outcome by means of various transformations on the entries of the matrix. Using a "utility function" \(f\) , a monotone increasing real- valued function of the game payoffs, he plays the game "as it looks to him", employing the optimal strategies for the matrix game obtained from the original game by replacing each entry \(a_{ij}\) with \(f(a_{ij})\) . A complete characterization is possible of those utility functions which are strategy- preserving in the sense that a player's optimal strategies are the same in the transformed game as in the original. Such functions must be either linear or exponential. The authors go on to discuss in detail the effects of other types of utility functions, corresponding to attitudes toward gain as "optimistic", "reckless", etc., on a player's strategies and his willingness to enter the game.  

## PART IV-Games with a Continuum of Strategies  

The papers of this part are united more by their use of the tools of ordinary analysis than by a common subject- matter. The games they study are closer to the classical game on the unit square than to games in extensive form, but Papers 18 and 19 make use of the methods developed for both.  

PAPER 16 The theorem of Glicksberg on semicontinuous payoffs has been cited above as a positive general result concerning the existence of a value for a game on the square. That no extensive weakening of the hypothesis of semicontinuity can be made is shown by the example given in this paper by Sion and Wolfe of a game whose payoff is not far from being semicontinuous. The example takes the form of a modified "Colonel Blotto" game whose lack of optimal strategies is perhaps surprising. It is cast,

---

redicts correctly, he o. Using different the value \((3 - \sqrt{5}) / 2\) ch depends on the . to move in the same nd make a turn with  

: the pursuer possesses the truncated game of suer predicts correct  

n the outcomes of game strategic behavior :he game's outcome by ne matrix. Using a ilued function of the ,employing the optimal zinal game by replacing ization is possible of in the sense that a sformed game as in the xponential. The authors of utility functions, c", "reckless", etc., r the game.  

## rategies  

their use of the tools . The games they study than to games in ex- . ethods developed for  

s payoffs has been concerning the existence. ive weakening of the the example given in is not far from being. ified "Colonel Blotto" prising. It is cast,  

via a general result relating infinite games in extensive form to games on the unit square, into the form of a simple pursuit game having no optimal strategies.  

PAPER 17 As another informative example of the behavior of games on the square, Gross here describes a game whose payoff is a rational function of the choices x and y of the two players. This follows up earlier work which showed that rational payoffs do not permit as simple optimal strategies as polynomial payoffs do. The present example has unique optimal strategies which are distribution functions whose spectra consist of the Cantor discontinuous.  

PAPER 18 In this paper, Restrepo solves the "m by n bullet silent duel." This problem, special cases of which have been studied in several places cited in the paper, is that of finding optimal strategies for the following continuous zero- sum two- person game: Two duelists have guns with m and n bullets, respectively; if the first (the second) fires a bullet at time t, where \(0 \leq t \leq 1\) , he will kill his opponent with probability \(\mathrm{P}(t) \mid \mathrm{Q}(t)\) , where \(\mathrm{P}(0) = \mathrm{Q}(0) = 0\) , \(\mathrm{P}(1) = \mathrm{Q}(1) = 1\) ; the payoff is \(1 + 1\) to the survivor, if unique, and otherwise zero. Restrepo shows that there are unique "independent" optimal strategies for each player. The strategy for player I is characterized in terms of numbers \(0 < a_1 < \dots < a_{m+1} < 1\) by m independent distribution functions \(\mathrm{F}_1\) . Player I chooses the time of firing his lit bullet in accordance with \(\mathrm{F}_1\) , which assigns probability one to the closed interval from \(a_1\) to \(a_{1+1}\) and varies continuously in its interior. Formulas are given for calculating the distributions as functions of P and Q.  

PAPER 19 Karlin and Restrepo here develop a method for attacking the problem of finding optimal strategies for games most aptly described as continuous versions of poker. In these, mixed strategies may often be represented in the form of a vector function \((\theta_1(x), \dots , \theta_m(x))\) of the "hand" x, and the payoff as a quasi- bilinear integral function of these strategies. Their technique, which is applied to a variety of continuous poker games, consists in part of a sort of theoretical iteration: properties proved (or conjectured) for one player's mixed strategy are used to delimit the other's, and vice versa.  

PAPER 20 In this paper, Karlin studies games on the unit square whose payoff functions K satisfy the strong requirement of being "bell shaped": \(\mathrm{K}(x, y) = \delta (x - y)\) , where \(\delta\) is a "proper Polya frequency"

---

function" satisfying the condition that the determinant whose entry i, j is \(\mathfrak{s}(x_{1} - y_{1})\) be positive for any real numbers \(x_{1}< \dots < x_{m}\) , \(y_{1}< \dots < y_{m}\) . The optimal strategies for such a game are unique, consisting of a step- function distribution for the minimizing player having k steps (say), and one for the maximizing player having either k or k - 1 steps. Other results include a relation between k and the value v (necessarily positive) of the game: \(kv \geq \theta (0)\) . Results for similar games, whose kernels are Green's functions of differential equations, relate the optimal strategies of these games to the coefficients of the equations.  

## PART V- - Games with a Continuum of Moves  

Most of the games in extensive form treated in the preceding parts of this Study have been explicitly extended in time, with the time- interval between one stage of the game and a succeeding stage being unspecified but definite. As we have seen, if the information pattern of the game is sufficiently simple, its study can be reduced to that of the behavior of a finite set of finite games under variations of their payoff functions. The retention of this discrete- time feature of a von Neumann- Morgenstern game in the extension of their theory to infinite games naturally permits the analysis of infinite games to follow in many respects the familiar lines of the development of finite game theory.  

However, such game models are often intended only as approximations to models of competitive situations which take place in a time continuum. It has thus seemed appropriate to the authors of the papers in this Part to depart from the "classical" discrete formulation of a game to study their problems directly in a continuous framework, with the "positions" of the contending parties described at any moment by continuous variables, and their strategic decisions given as functions of continuous variables. Owing to the fact that, in the bulk of the particular games of this sort which have been studied, strategic choice is exercised on the "positional variables" through their races of change, they have come to be called "differential games" by various authors.  

The systematic study of particular examples of such games was initiated by Rufus Isaacs in a number of unpublished RAND Corporation memoranda of 1954 and 1955, but almost no work in this field has yet appeared in print. What constitutes a "differential game" is not a matter of general agreement among those working in the field, but a general formulation which seems to capture the principal features of the existing examples has been given by Isaacs. This runs as follows: A bounded connected open subset A of Euclidean n- space, a bounded real- valued (payoff) function on the boundary of A, the "starting point" \(x^{0}\) , and the set of

---

lose entry 1, j < Xm', unique, consistent having k er k or k - 1 he value v or similar games, ons, relate the he equations.  

ne preceding parts the time- interval unspecified but ne game is suf- ehavior of a functions. The orenstern game ly permits the "amiliar lines  

r as approxima- in a time con- ne papers in on of a game to th the "po- by continuous of continuous icular games of cised on the have come to be  

ch games was corporation d has yet appear- a matter of eneral formula- xisting examples connected open off) function set of  

differential equations  

\[\frac{\mathrm{d}x_{j}}{\mathrm{d}t} = f_{j}(x_{1},\ldots ,x_{n};t;\mathcal{G};\mathbb{Y}) \qquad (j = 1,\ldots ,n)\]  

are all given. The \(x_{j}\) are called the "positional variables". \(\mathcal{G}\) and \(\mathbb{Y}\) called "navigational variables," are selected by the two players from suitably prescribed sets of functions of \(t\) and the positional variables. With such pure strategies assumed to satisfy conditions guaranteeing solutions to the differential equations, a play of the game consists in the trajectory of the positional variables from the starting point to the termination of the play (if any) at the boundary of A. The resulting payoff is then determined by the value of the payoff function at termination.  

Unfortunately, no precise and at the same time satisfying formulation of the notion of a strategy in a differential game has been devised. There are still many unresolved conceptual problems. The authors of the papers in this Part have undertaken the study of restricted problems in the field with the aim of developing methods and insights suited to this new and important type of game.  

PAPER 21 One way to utilize discrete game theory in the study of differential games is to replace the differential equation describing the game by a difference equation employing a discrete time- step 8. The resulting structure can be looked upon as a generalization of the recursive game studied by Everett in Paper 2, a "game element" being given for each point \(x\) in the space of positional variables. In this Paper, Scarf brings methods from the study of stochastic processes to bear on differential games by utilizing the fact that, given mixed strategies for both players of the game, the discrete game constitutes an \(n\) - dimensional random walk the limiting behavior of which as \(8 \rightarrow 0\) has received considerable study. Scarf calls a differential game "unbiased" if the projection of its vector payoff (the vector whose components are the functions \(f_{j}(x_{1}, \ldots , x_{n}; t; \mathcal{G}; \mathbb{Y})\) ) along any line yields a "fair game"—i.e., if the game with payoff function \(E_{j} a_{j} f_{j}\) has value zero for arbitrary constants \(a_{j}\) . For such a game, the recurrence relations which the values of its discrete versions (dependent on \(8\) ) satisfy pass over into a second- order linear partial differential equation as \(8 \rightarrow 0\) . If now this equation, with boundary values prescribed by the given value function on the boundary of A, has a sufficiently differentiable solution \(V(x)\) , then the maxmin and minmax values of the discrete approximating games converge to this function for every starting point \(x\) . These results thus give both a means of establishing the existence of a value in certain differential

---

games and clues for obtaining approximations to their optimal strategies.  

PAPER 22 Results analogous to those of Paper 21 are obtained here by Fleming for a class of differential games which differ from the above principally in terminating at the end of a prescribed time- period, rather than upon entry of the play into some set of positions. Fleming employs conditions on the differential equations and payoff of the game that are sufficiently strong to ensure the existence of values for its discrete approximating games. Passing to the limit with the recurrence relations defining their values, he obtains a first order partial differential equation. If a continuously differentiable solution exists for this equation, it represents a value for the differential game as does the V of Paper 21, but in the stronger sense that the corresponding value- functions for the discrete games converge uniformly to this value on compacta.  

PAPER 23 In the final Paper of this Study, Berkovitz and Fleming attack the existence of optimal strategies for a type of differential game sufficiently restricted to have saddlepoints in "pure" continuous strategies. Only one positional variable is used (this restriction is not essential), but the payoff is given as an integral over the entire trajectory of a play in such a way as to be convex for the minimizing player and concave for the maximizing player. (As Isbell and Marlow point out, a payoff integral can be incorporated into the description of a differential game given above by adding one positional variable.) The authors do not, as in the two preceding papers, approach the game through a discrete analogue, but take it up directly as a saddlepoint problem with inequality and differential side conditions, employing techniques from the calculus of variations. Analogues of the Euler equations for ordinary extremal problems are obtained as necessary conditions descriptive of the saddlepoint; their solutions are characteristics of a partial differential equation involving the value of the game. Sufficient conditions are also given that a family of characteristics determine a solution of the game. The authors finally employ their variational techniques in the solution of an illustrative example.

---

## RECURSIVE GAMES  

H. Everett  

## INTRODUCTION  

A recursive game is a finite set of "game elements", which are games for which the outcome of a single play (payoff) is either a real number, or another game of the set, but not both. By assigning real numbers to game payoffs, each element of the recursive game becomes an ordinary game, whose value and optimal strategies (if they exist) of course depend upon the particular assignment. It is shown that if every game element possesses a solution for arbitrary assignments, then the recursive game possesses a solution. In particular, if the game elements possess minimal solutions for all assignments of real numbers to game payoffs, then the recursive game possesses a supinf solution in stationary strategies, while if the game elements possess only supinf solutions, then the recursive game possesses a supinf solution which may, however, require non- stationary strategies. No restrictions are placed upon the type of game elements, other than the condition that they possess solutions for arbitrary assignments of real numbers to game payoffs. Some extensions to more general games are given.  

## §1. DEFINITIONS  

A recursive game, \(\vec{\tau}\) , is a finite set of \(n\) "game elements", denoted by \(n^{1}, n^{2}, \ldots , n^{n}\) , each of which possesses a pair of strategy spaces, denoted by \(s_{1}^{k}\) and \(s_{2}^{k}\) , corresponding to \(r^{k}\) for Players 1 and 2 respectively. To every pair of strategies \(x^{k} \in s_{1}^{k}, y^{k} \in s_{2}^{k}\) , there is associated an expression (generalized payoff):  

\[(1.0) \qquad \mathrm{H}^{k}(x^{k}, y^{k}; \vec{\tau}) = p^{k} e^{k} + \sum_{j = 1}^{n} q^{k} j_{r}^{j} \quad (1.0)\]

---

where  

\[p^{k}, q^{kj} \geq 0 \quad \text{and} \quad p^{k} + \sum_{i} c_{i}^{kj} = 1.\]  

The interpretation of this generalized payoff is that if Player 1 and Player 2 play \(r^{k}\) with strategies \(x^{k}\) and \(x^{k}\) respectively, the possible outcomes of the single round are either to terminate play with Player 1 receiving an amount \(e^{k}\) from Player 2, or to have no payoff and proceed to play another game of the set, where \(r^{k}\) and the \(q^{kj}\) are the probabilities of these events.  

A strategy \(x \in S_{1}^{k}\) for \(P_{1}\) is an infinite sequence of vectors, \(x = (x_{t}^{1}) = \overline{x}_{1}^{1}, \overline{x}_{2}^{1}, \dots , \overline{x}_{t}^{1}, \dots\) where \(\overline{x}_{t}^{1} = (x_{t}^{1}, x_{t}^{2}, \dots , x_{t}^{n})\) and \(x_{t}^{1} \in S_{1}^{k}\) for all \(t\) and all \(i\) , with the interpretation that if \(P_{1}\) finds himself in \(r^{k}\) for the \(t\) - th round of play, he will use strategy \(x_{t}^{k}\) . A strategy \(x\) is stationary in component 1 if \(x_{t}^{1} = x_{1}^{1}\) for all \(t\) . A strategy \(x\) is stationary if it is stationary in all components. Similar definitions hold for a strategy \(\overline{x} \in S_{2}^{k}\) for \(P_{2}\) .  

A pair of strategies \(x, \overline{x}\) and a starting position \(r^{j}\) , define a random walk with absorbing barriers among the game elements. Since absorption in \(r^{k}\) in the \(t\) - th round carries the payoff \(e_{t}^{k}\) an expectation, \(\mathbb{E}x^{j}[x, \overline{x}]\) is defined. Thus to each strategy pair there corresponds an expectation vector, whose components correspond to the starting positions. If we define the \(n \times n\) matrices \(P_{t}\) and \(Q_{t}\) and the column vector \(\overline{E}_{t}\) for the strategy pair \((x, \overline{x})\) by:  

\[[P_{t}^{1}]^{1j} = \delta^{1j}p^{1} \qquad [Q_{t}^{1}]^{1j} = q^{1j}\]  

(1.2)  

\[[Q_{0}^{1}]^{1j} = \delta^{1j} \qquad E_{t}^{1} = e^{1}\]  

where \(p^{1}, q^{1j}\) , and \(e^{1}\) are given by \(H^{1}(x_{t}^{1}, y_{t}^{1}; \overline{r})\) through (1.0), then straightforward calculation gives the expectation vector for \(n\) rounds of play as:  

\[\mathbb{E}x_{n}^{1}(x, \overline{x}) = \sum_{k = 1}^{n} \left(\prod_{t = 0}^{k - 1} Q_{t}\right) P_{k} \overline{E}_{k}^{1}, \quad (1.3)\]  

where  

\[\prod_{t = 0}^{k - 1} Q_{t} = Q_{0} Q_{1} Q_{2} Q_{3} \dots Q_{k - 1}\]  

and hence that the ultimate expectation is

---

\[\overrightarrow{\mathrm{Ex}} (\mathbf{x}, \Psi) = \lim_{n \to \infty} \overrightarrow{\mathrm{Ex}}_n (\mathbf{x}, \Psi) = \sum_{k = 1}^{\infty} \left(\prod_{t = 0}^{k - 1} \mathbf{Q}_t\right) \mathrm{P}_k \overrightarrow{\mathrm{E}}_k \quad (1.4)\]  

which for bounded payoffs always converges, and which assigns zero expectation to a non- terminating play.  

A recursive game will be said to possess a solution if there exists a vector \(\overrightarrow{\mathbf{V}}\) , and if for all \(\epsilon > 0\) there exist strategies \(x^{\epsilon} \in S_1, \Psi^{\epsilon} \in S_2\) , such that:  

\[\overrightarrow{\mathrm{Ex}} (x^{\epsilon}, \Psi) \geq \overrightarrow{\mathrm{V}} - \epsilon \overrightarrow{\mathrm{T}} \quad \text{for all} \quad \Psi \in S_2\] \[\text{and}\] \[\overrightarrow{\mathrm{Ex}} (x, \Psi^{\epsilon}) \leq \overrightarrow{\mathrm{V}} + \epsilon \overrightarrow{\mathrm{T}} \quad \text{for all} \quad x \in S_1\]  

\(\overrightarrow{\mathrm{Ex}} \geq \overrightarrow{\mathrm{W}} \longrightarrow \overrightarrow{\mathrm{U}} \geq \overrightarrow{\mathrm{W}}^1\) for all i, and \(\overrightarrow{\mathrm{T}} = (1, 1, \ldots , 1)\) . Then \(\overrightarrow{\mathrm{V}}\) and \(\Psi^{\epsilon}\) are called \(\epsilon\) - best strategies, and \(\overrightarrow{\mathrm{V}}\) is the value of the recursive game. (Our definition thus corresponds to a solution of all of games which can arise from the different possible starting positions.  

## §2. THE VALUE MAPPING, M  

For an arbitrary vector \(\overrightarrow{\mathrm{W}} = (W^1, W^2, \ldots , W^n)\) we can reduce a game element \(r^k\) to an ordinary (non- recursive) game \(r^k(\overrightarrow{\mathrm{W}})\) by defining "numerical valued) payoff function for \(r^k(\overrightarrow{\mathrm{W}})\) to be:  

\[\overrightarrow{\mathrm{H}}^k (x^k, y^k; \overrightarrow{\mathrm{W}}) = \mathrm{p}^k \mathrm{e}^k + \sum_j \mathrm{q}^k \mathrm{j} \mathrm{w}^j, (x^k, y^k) \in S_1^k \times S_2^k\]  

With results from \(\mathrm{H}(x^k, y^k; \overrightarrow{\mathrm{T}})\) by replacing the symbols \(\overrightarrow{\mathrm{r}}^j\) by the real numbers \(\overrightarrow{\mathrm{W}}^j\) in (1.0). In effect we are arbitrarily assigning a "value", \(\overrightarrow{\mathrm{w}}^j\) , to the command to play \(\overrightarrow{\mathrm{r}}^j\) .  

DEFINITION 1. A game element \(\overrightarrow{\mathrm{r}}^1\) satisfies the supinf condition if the ordinary game \(\overrightarrow{\mathrm{r}}^1 (\overrightarrow{\mathrm{W}})\) possesses a supinf solution in the usual sense for all \(\overrightarrow{\mathrm{W}}\) .  

DEFINITION 2. A game element \(\overrightarrow{\mathrm{r}}^1\) satisfies the minimax condition if \(\overrightarrow{\mathrm{r}}^1 (\overrightarrow{\mathrm{W}})\) possesses a minimax solution for all \(\overrightarrow{\mathrm{W}}\) .

---

Of course, if a game element satisfies the minimax condition, it also satisfies the supinf condition. We shall henceforth deal only with recursive games, all of whose elements satisfy at least the supinf condition.  

If each of the n game elements of a recursive game \(\bar{\Gamma}\) satisfies the supinf condition, then for any n- vector \(\bar{\mathbf{U}}\) , we define the n- vector are \(\bar{\mathbf{U}}' = \mathbf{M}(\bar{\mathbf{U}})\) through:  

\[U^{1} = \mathrm{Val} \bar{\mathbf{r}}^{1}(\bar{\mathbf{U}}) \quad (2.4)\]  

The mapping, M, of n- vectors into n- vectors is then called the value mapping for the game \(\bar{\Gamma}\) .  

We now define the relations \(\geq\) and \(\leq\) for vectors (or numbers) to mean:  

\[\bar{\mathbf{U}} \geq \bar{\mathbf{v}} \Rightarrow \left\{ \begin{array}{ll} \mathbf{U}^{1} > \mathbf{V}^{1} & \mathrm{if} \mathbf{V}^{1} > 0 \\ \mathbf{U}^{1} \geq \mathbf{V}^{1} & \mathrm{if} \mathbf{V}^{1} \leq 0 \end{array} \right\} \mathrm{for~all} \quad (2.5)\]  

(2.5)  

\[\bar{\mathbf{U}} \leq \bar{\mathbf{v}} \Rightarrow \left\{ \begin{array}{ll} \mathbf{u}^{1} < \mathbf{v}^{1} & \mathrm{if} \mathbf{v}^{1} < 0 \\ \mathbf{u}^{1} \leq \mathbf{v}^{1} & \mathrm{if} \mathbf{v}^{1} \geq 0 \end{array} \right\} \mathrm{for~all} \quad (1)\]  

and we further define, for \(\bar{\mathbf{T}}\) , the classes \(C_{1}(\bar{\mathbf{T}})\) , \(C_{2}(\bar{\mathbf{T}})\) of n- vectors by:  

\[\bar{\mathbf{W}} \in C_{1}(\bar{\mathbf{T}}) \Rightarrow \mathbf{M}(\bar{\mathbf{W}}) \geq \bar{\mathbf{W}}\]  

(2.6)  

\[\bar{\mathbf{W}} \in C_{2}(\bar{\mathbf{T}}) \Rightarrow \mathbf{M}(\bar{\mathbf{W}}) \leq \bar{\mathbf{W}}\]  

and we note that \(C_{1}(\bar{\mathbf{T}})\) and \(C_{2}(\bar{\mathbf{T}})\) are always disjoint except possibly for the zero vector.  

THEOREM 1. (a) \(\bar{\mathbf{W}} \in C_{1}(\bar{\mathbf{T}}) \Rightarrow\) for every \(\epsilon > C\) there exists a strategy \(\mathbf{x}^{\epsilon} \in S_{1}\) such that  

\[\bar{\mathbf{E}} \mathbf{x}(\mathbf{x}^{\epsilon}, \bar{\mathbf{y}}) \geq \bar{\mathbf{W}} - \epsilon \bar{\mathbf{T}} \quad (\text{all} \quad \bar{\mathbf{y}} \in S_{2})\]  

(b) \(\bar{\mathbf{W}} \in C_{2}(\bar{\mathbf{T}}) \Rightarrow\) for every \(\epsilon >\) there exists a strategy \(\bar{\mathbf{y}}^{\epsilon} \in S_{2}\) such that \(\bar{\mathbf{E}} \mathbf{x}(\mathbf{x}, \bar{\mathbf{y}}) \leq \bar{\mathbf{W}} + \bar{\epsilon} \bar{\mathbf{T}}\) (all \(\mathbf{x} \in S_{2}\) ).

---

PROOF. We shall prove (a) by supposing that we are given a \(\epsilon \subset_{1}(\vec{\tau})\) and an \(\epsilon >0\) , and then using \(\vec{W}\) to construct a strategy on. \(\epsilon \mathcal{S}_{1}\) , which we subsequently prove gives the desired result. files Let \(\vec{W}^{1} = \mathbb{M}(\vec{W})\) . Because \(\vec{W}\in C_{1}(\vec{\tau})\) all components \(\vec{W}^{1}\) which are positive increase under the value mapping, and since there are only a finite number, there exists a \(\gamma >0\) such that \(\vec{W}^{1} > 0\Longrightarrow \vec{W}^{1} - \vec{W}^{1}\geq \gamma\) for all 1. Choose 8 such that \(0< 8< \min (\gamma ,\epsilon)\) , and then let strate- \(\vec{\mathbf{x}}^{\epsilon}\in \mathcal{S}_{1}\) for \(\mathbb{P}_{1}\) have components \(\bar{X}_{t}^{1}\) as follows:  

1) If \(\vec{r}^{1}(\vec{W})\) possesses an optimal strategy, \(\vec{X}^{1}\in \vec{S}_{1}^{1}\) , for \(\mathbb{P}_{1}\) , then let \(\vec{X}_{t}^{1} = \vec{X}^{1}\) for all t. (stationary in comp. 1)  

2) If \(\vec{r}^{1}(\vec{W})\) fails to possess an optimal strategy for \(\mathbb{P}_{1}\) , but \(\vec{W}^{1} > 0\) , then let \(\vec{X}_{t}^{1} = \vec{X}^{1}\) forall t, where \(\vec{X}^{1}\in \vec{S}_{1}^{1}\) is 8-best in \(\vec{r}^{1}(\vec{W})\) . (stationary in comp. 1)  

3) If \(\vec{r}^{1}(\vec{W})\) fails to possess an optimal strategy for \(\mathbf{P}_{1}\) , and \(\vec{W}^{1}\leq 0\) , then let \(\vec{X}_{t}^{1}\in \vec{S}_{1}^{1}\) be a strategy which is \(\delta_{t}\) -best in \(\vec{r}^{1}(\vec{W})\) , where \(\delta_{t} = (\frac{1}{2})^{t}\delta\) . (non-stationary in comp. 1).  

\(\vec{\mathbf{x}}_{t} = \vec{\mathbf{x}}_{t}\) (2.1), (2.4), and (2.6), for \(\vec{\mathbf{x}}_{t}\) so defined and for all \(\vec{\mathbf{Y}}_{t}\) :  

\[\mathrm{H}^{1}\Big(\vec{x}_{t}^{1},\vec{x}_{t}^{1};\vec{W}\Big) = \mathrm{p}_{t}^{1}\mathrm{e}_{t}^{1} + \sum_{j}\mathrm{q}_{t}^{1}\vec{\mathrm{d}}_{t}^{1}\vec{\mathrm{w}}^{j}\] \[\mathrm{~\vec{\Sigma}~}\vec{\mathrm{e}}_{t}^{1}\Bigg(\vec{\mathrm{w}}^{1} + \gamma -\delta \mathrm{~in~}1\Big)\mathrm{~and~}2\Big)\big(\vec{\mathrm{w}}^{1} > 0\Big)\Bigg)\] \[\mathrm{~\vec{\Sigma}~}\Bigg(\vec{\mathrm{w}}^{1} - \delta_{t}\mathrm{~in~}3\Big)\big(\vec{\mathrm{w}}^{1}\leq 0\Big)\]  

so that if we define the non- negative vectors \(\vec{\mathrm{w}}\) and \(\vec{\delta}_{t}\) by:  

\[\mathrm{~\vec{\Sigma}~}\mathrm{~\vec{\Sigma}~}\mathrm{~\vec{\Sigma}~}\mathrm{\quad This is a friendly reminder - the current text generation call will exceed the model's predefined maximum length (8192). Depending on the model, you may observe exceptions, performance degradation, or nothing at all.

---

Using the facts that the addition of a constant vector to each side, and the multiplication of each side by a matrix with non- negative elements will preserve the inequality, we calculate the expectation in the recursive game for n rounds under \(\mathbf{x}^{\epsilon}\) and for an arbitrary \(\mathbf{y}\) :  

\[\overrightarrow{\mathbf{x}}_{\mathbf{n}} = \sum_{\mathbf{k} = 1}^{\mathbf{n}}\left(\prod_{\mathbf{t} = 0}^{\mathbf{k} - 1}\mathbf{q}_{\mathbf{t}}\right)\mathbf{P}_{\mathbf{k}}\overrightarrow{\mathbf{x}}_{\mathbf{k}}\]  

\[\geq \sum_{\mathbf{k} = 1}^{\mathbf{n}}\left(\prod_{\mathbf{t = 0}}^{\mathbf{k} - 1}\mathbf{q}_{\mathbf{t}}\right)\left[\left(\mathbf{I} - \mathbf{q}_{\mathbf{k}}\right)\overrightarrow{\mathbf{w}} +\overrightarrow{\mathbf{u}} -\overrightarrow{\mathbf{s}}_{\mathbf{k}}\right]\]  

by (1.3) and (2.10), where I is the identity matrix. This may be rewritten, by collapsing the terms involving \(\overrightarrow{\mathbf{w}}\) , as  

\[\overrightarrow{\mathbf{x}}_{\mathbf{n}}\geq \overrightarrow{\mathbf{w}} -\left(\prod_{\mathbf{t} = 0}^{\mathbf{n}}\mathbf{q}_{\mathbf{t}}\right)\overrightarrow{\mathbf{w}}\] \[\qquad +\sum_{\mathbf{k} = 1}^{\mathbf{n}}\left(\prod_{\mathbf{t} - \mathbf{c}}^{\mathbf{k} - 1}\mathbf{q}_{\mathbf{t}}\right)\overrightarrow{\mathbf{u}} -\sum_{\mathbf{k} = 1}^{\mathbf{n}}\left(\prod_{\mathbf{t} + \mathbf{c}}^{\mathbf{k} - 1}\mathbf{q}_{\mathbf{t}}\right)\overleftarrow{\mathbf{s}}_{\mathbf{k}}.\]  

Now let  

\[\tau = \max_{i}W^{i} / (\gamma -8)\]  

if this is positive, and zero otherwise. (In case all \(W^{i} < 0\) .) Then, clearly, by definition of \(\overrightarrow{\mathbf{u}}\) we have \(\tau \overrightarrow{\mathbf{u}} \geq \overrightarrow{\mathbf{w}}\) , and hence  

\[\sum_{\mathbf{k} = 1}^{\mathbf{n}}\left(\prod_{\mathbf{t} > 0}^{\mathbf{k} - 1}\mathbf{q}_{\mathbf{t}}\right)\overrightarrow{\mathbf{u}}\longrightarrow \left(\prod_{\mathbf{t} = 0}^{\mathbf{n}}\mathbf{q}_{\mathbf{t}}^{\prime}\right)\overrightarrow{\mathbf{w}}\]  

(2.13)  

\[\geq \sum_{\mathbf{k} = 1}^{\mathbf{n}}\left({\prod_{\mathbf{t} = 0}^{\mathbf{k} - 1}\mathbf{q}_{\mathrm{t}}}\right)\overrightarrow{\mathbf{u}} -\tau \left({\prod_{\mathbf{t} = 0}^{\mathbf{n}}\mathbf{q}_{\mathrm{t}}}\right)\overrightarrow{\mathbf{u}} = \sum_{\mathbf{k} = 1}^{\mathbf{n}}\overrightarrow{\mathbf{u}}_{\mathbf{k} - 1} - \tau \overrightarrow{\mathbf{u}}_{\mathbf{n}}\]  

where we have defined  

\[\overrightarrow{\mathbf{u}}_{\mathbf{k}} = \left(\prod_{\mathbf{t} = 0}^{\mathbf{k}}\mathbf{q}_{\mathbf{t}}\right)\overrightarrow{\mathbf{u}}.\]  

Now, because \(\overrightarrow{0} \leq \overrightarrow{\mathbf{u}}_{\mathbf{k}} \leq (\gamma - 8)^{\frac{1}{2}}\) and \(\tau \geq 0\) , it is clear that there

---

, and exists at = such that for all n > m  

ents  

\[\sum_{k = 1}^{n}\vec{\mu}_{k - 1}\geq \vec{\tau}\vec{\mu}_{n}\]  

since, is a component of the sum diverges, the boundedness of \(\vec{\tau}\vec{\mu}_{n}\) in- sses the result, and if a component converges, it means the corresponding \(\vec{\tau}\vec{\mu}_{n}\vec{\tau}\vec{\mu}_{n}\vec{\tau}\vec{\mu}_{n} = 0\) , which also insures the result. This result, \(\vec{\tau}\vec{\mu}_{n}\vec{\tau}\vec{\mu}_{k}\vec{\tau}\vec{\mu}_{k}\vec{\tau}\vec{\mu}_{n}\vec{\tau}\vec{\mu}_{k}\) implies that there exists an m such that for \(\vec{\tau}\vec{\mu}_{n}\vec{\tau}\vec{\mu}_{m}\vec{\tau}\vec{\mu}_{n}\vec{\tau}\vec{\mu}_{m}\)  

re-  

\[\overline{\mathbf{E}\mathbf{x}}_{n}\geq \overline{\mathbf{W}} -\sum_{k = 1}^{n}\left(\prod_{t = 0}^{k - 1}Q_{t}\right)\vec{\delta}_{k}\]  

and hence that  

\[\overline{\mathbf{E}\mathbf{x}}(\mathbf{x}^{\epsilon},\mathbf{\Psi}) = \lim_{n\to \infty}\overline{\mathbf{E}\mathbf{x}}_{n}\geq \overline{\mathbf{W}}\]  

2.5  

\[-\lim_{n\to \infty}\sum_{k = 1}^{n}\left(\prod_{t = 0}^{k-1}Q_{t}\right)\vec{\delta}_{k}\quad (\mathrm{all}\quad \Psi)\]  

en,  

exists all components of the matrix are non- negative and \(\leq 1\) . This implies that  

\[\lim_{n\to \infty}\sum_{k = 1}^{n}\left(\prod_{\substack{t=0\\t=0}}^{k-1}Q_{t}\right)\vec{\delta}_{k}\leq \left(\sum_{k=1}^{\infty}\delta_{k}\right)^{\frac{1}{1}}\]  

'2.16)  

\[= \left(\sum_{k = 1}^{\infty}\left(\frac{1}{2}\right)^{k}\delta\right)^{\frac{1}{1}} = \delta^{\frac{1}{1}}.\]  

definition of \(\delta_{k} = (\frac{1}{2})^{k}\delta\) . Moreover, since \(\delta\) was chosen \(< \epsilon\) , we are finally, from (2.16) and (2.15) that  

\[\overline{\mathbf{E}\mathbf{x}}(\mathbf{x}^{\epsilon},\Psi)\geq \overline{\mathbf{W}} -\epsilon \overline{\mathbf{\tau}}\quad \mathrm{for~all}\quad \Psi \in \mathcal{G}_{2}\]

---

and the proof of (a) of Theorem 1 is completed. Identical treatment reversing the roles of the players proves (b).  

Since the games are zero- sum, an immediate consequence of Theorem 1 is:  

\[\overline{W}_{1}\in C_{1}(\overrightarrow{\Gamma}),\overline{W}_{2}\in C_{2}(\overrightarrow{\Gamma})\Longrightarrow \overline{W}_{1}\leq \overline{W}_{2}. \quad (2.18)\]  

## §3. THE CRITICAL VECTOR  

DEFINITION 3. \(\overline{V} = \overline{V} (\overrightarrow{\Gamma})\) is a critical vector for \(\overrightarrow{\Gamma} \xrightarrow{\quad \overrightarrow{\Gamma} \quad}\) for every \(\epsilon > 0\) there exists a pair of vectors, \(\overline{W}_{1}\) and \(\overline{W}_{2}\) , lying componentwise within an \(\epsilon\) - neighborhood of \(\overline{V}\) , \((\epsilon \in \mathbb{N}_{\epsilon}(\overline{V}))\) , such that \(\overline{W}_{1} \in C_{1}(\overrightarrow{\Gamma})\) and \(\overline{W}_{2} \in C_{2}(\overrightarrow{\Gamma})\) . \((\overline{V}\) is in the intersection of the closures of \(C_{1}(\overrightarrow{\Gamma})\) and \(C_{2}(\overrightarrow{\Gamma})\) .)  

THEOREM 2. \(\overline{V}\) is a critical vector in \(\overrightarrow{\Gamma} \xrightarrow{\quad \overrightarrow{\Gamma} \quad}\) possesses a solution, with value \(\overline{V}\) . (Hence \(\overline{V}\) is unique.)  

PROOF. Follows immediately from definition of critical vector Theorem 1, and the definition of a solution.  

COROLLARY. If \(\overrightarrow{\Gamma}\) possesses a critical vector, \(\overline{V}\) , then there exist for all \(\epsilon > 0\) , \(\epsilon\) - best strategies \(x^{\epsilon}\) , \(\Psi^{\epsilon}\) , for the players which are stationary in all components \(i\) for which either \(\Gamma^{1}\) satisfies the minimax condition, or \(\overline{V}^{1}\) is favorable. \((\overline{V}^{1} > 0\) is favorable for \(P_{1}\) , \(\overline{V}^{1} < 0\) is favorable for \(P_{2}\) .)  

PROOF. Follows from construction of \(\epsilon\) - best strategies (2.7) proof of Theorem 1.  

REMARK 1. The value of an ordinary (non- recursive) game is obviously a critical 1- vector in that game.  

## §4. REDUCTIONS OF RECURSIVE GAMES  

For any recursive game \(\overrightarrow{\Gamma} = (\overrightarrow{\Gamma}^{1}, \overrightarrow{\Gamma}^{2}, \dots , \overrightarrow{\Gamma}^{n})\) , we can form

---

it re- re- re- re- re- re- re- re- re- re- re - re- re- re- re- re- re- re- re- re- re re- re- re- re- re- re- re- re- re- re. re- re- re- re- re- re- re- re- re- re-. re- re- re- re- re- re- re- re- re- re . re- re- re- re- re- re- re- re- re- re  

\[\dots \xrightarrow{\mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot} \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot\] \[\mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot\mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\] \[\mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\mathrm{j}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{j}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot\] \[\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i} \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}.\mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot}\] \[\mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i} \cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{j} \cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot\] \[\mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \mathrm{j}\cdot\] \[\mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i}\cdot \cdot \cdot \mathrm{i}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \mathrm{i}\cdot \cdot \cdot \cdot \cdot \mathrm{i}\cdot \cdot \cdot \mathrm{i}\cdot \cdot \cdot\] \[\mathrm{i}\cdot \mathrm{i}\cdot \mathrm{i} \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \mathrm{i}\cdot \mathrm{i}\cdot \cdot \cdot \cdot \cdot\] \[\mathrm{i}\cdot \mathrm{i}\mathrm{i}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \mathrm{i}\mathrm{i}\cdot \cdot \cdot \cdot \cdot \cdot\] \[\mathrm{i}\cdot \mathrm{j}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \mathrm{j}\cdot \cdot \cdot \cdot \cdot \cdot\] \[\mathrm{i}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \textnormal {i}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \textnormal {j}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \] \[\mathrm{i}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot\] \[\mathrm{i} \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot\] \[\mathrm{j}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \mathrm{j}\mathrm{j}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \textnormal{j}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot\] \[\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot\dots \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \text {j}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \text {j}\] \[\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \text{1}\cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \dots \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot\]  

\(\therefore\) shall say that a game element \(\mathrm{r}^{1}\) has bounded payoff if there exist \(\mathrm{r}\mathrm{i}\mathrm{i}\mathrm{i}\mathrm{i}\mathrm{i}\mathrm{i}\mathrm{i}\cdot \mathrm{i}\mathrm{i}\mathrm{i}\mathrm{i}\mathrm{i}\mathrm{i}\mathrm{j}\mathrm{i}\mathrm{i}\mathrm{i}\mathrm{i}\mathrm{i}\mathrm{i}\dots\) \(\beta\) such that \(\beta \leq \mathrm{e}^{1}\leq \alpha\) for all \((\mathrm{x}^{1},\mathrm{y}^{1})\in \mathrm{S}_{1}^{1}\times \mathrm{S}_{2}^{1}\)  

\(\therefore\) shall now investigate the behavior of the value, if it exists, it is reduced game \(\mathrm{r}^{1}\mathrm{s}(\mathrm{v}^{\mathrm{1}}\mathrm{s})\) formed by assigning the single real number : \(\therefore\) is set \(\mathrm{s}\) . We will abbreviate the k- th component of  

\[\mathrm{\overline{{V a l}}}^{s}\left\{\mathrm{\overline{{r}}}^{s}\left(\mathrm{v}^{\mathrm{1}}\overline{{\mathrm{s}}}\right)\right\}\]  

\(\therefore\) : \(\therefore\) is the game element \(\mathrm{r}^{k}(\mathrm{v}^{\mathrm{1}}\mathrm{s})\) by \(\mathrm{r}^{k}(\mathrm{v})\) . We then have:  

\(\therefore\) : (a) \(\alpha >0\) , \(\beta < 0\) are any payoff bounds for all \(\mathrm{r}^{k}\) , k e s. (b) \(\mathrm{v}^{k}(\mathrm{v})\) exists for all v.  

\(\therefore\) : (c) \(\beta \leq \mathrm{v}^{k}(\mathrm{v})\leq \alpha\) for \(\beta \leq \mathrm{v}\leq \alpha\) (d) for every \(\delta >0\) , and for all v, \(\mathrm{v}^{k}(\mathrm{v}) - \delta \leq \mathrm{v}^{k}(\mathrm{v} - \delta)\leq \mathrm{v}^{k}(\mathrm{v})\leq\) \(\mathrm{v}^{k}(\mathrm{v} + \delta)\leq \mathrm{v}^{k}(\mathrm{v}) + \delta\) where \(\mathrm{\Delta}^{\mathrm{*}}\leq \mathrm{\Delta}^{\mathrm{*}}\) means " \(\leq\) " unless \(\mathrm{v}^{k}(\mathrm{v}) = \mathrm{v}\) .  

\(\therefore\) is, that if the reduced game possesses a solution for all v, its value components change monotonically with v at a rate less than or equal to the rate of change of v, with strict inequality holding whenever \(\mathrm{v}^{k}(\mathrm{v})\neq \mathrm{v}\) .  

:7) in  

PROOF. We shall consider a single game element \(\mathrm{r}^{k}(\mathrm{v})\) , with \(\therefore \mathrm{r}\mathrm{e}\mathrm{e}\mathrm{\quad \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \quad \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot}\) and shall, for convenience, drop the superscript. For any \(\therefore \mathrm{r}\mathrm{e}\mathrm{e}\mathrm{\quad \cdot \cdot}\) pair x, y, in the reduced game, the expectation for the starting \(\therefore \mathrm{r}\mathrm{e}\mathrm{e}\mathrm{\quad \cdot \cdot}\mathrm{r}\mathrm{e}\mathrm{e}\mathrm{\quad \cdot \cdot}\mathrm{r}\) can always be written in the form:  

\[\therefore \mathrm{r}\mathrm{e}\mathrm{e}\mathrm{\quad \cdot \cdot}\cdot \mathrm{r}\mathrm{e}\mathrm{e}\mathrm{\quad \cdot \cdot}\mathrm{\quad \cdot \cdot}\mathrm{\quad \cdot \cdot}\mathrm{\cdot \cdot}\mathrm{\cdot \cdot}\mathrm{\cdot \cdot}\mathrm{\cdot}\mathrm{\cdot \cdot}\mathrm{\cdot \cdot}\mathrm{\cdot \cdot}\]  

\(\therefore \mathrm{r}\mathrm{e}\mathrm{e}\mathrm{\quad \cdot \cdot}\quad \mathrm{\quad \cdot \cdot}\mathrm{\quad \cdot \cdot}\mathrm{\quad}\mathrm{\quad \cdot \cdot}\mathrm{\quad \cdot \cdot}\mathrm{\mathrm{\quad \cdot \cdot}\mathrm{\quad \cdot \cdot}\mathrm{\quad}}\mathrm{\quad \cdot \cdot}\mathrm{\quad \cdot \cdot}\mathrm{\quad}\) is the probability of ultimately receiving a game payoff to one form a: \(\therefore \mathrm{r}\mathrm{e}\mathrm{e}\mathrm{\quad \cdot \cdot} \mathrm{\quad \cdot \cdot}\mathrm{\quad \cdot \cdot}\mathrm{\mathrm{}}\) is the rest of the expecta \(\therefore \mathrm{r}\mathrm{e}\mathrm{e}\mathrm{\quad \cdot \cdot}{\mathrm{\quad \cdot \cdot}\mathrm{\quad \cdot \cdot}\mathrm{\quad}}\) satisfies the relation \(\beta \leq \mathrm{E}\leq \alpha\) for all x, y, and

---

\(\alpha , \beta\) are payoff bounds for the game elements of \(s\) . Then (c) is proved immediately, since (4.2) implies that:  

\[(1 - S)\beta + S\beta \leq (1 - S)\mathrm{E} + S\nu \leq (1 - S)\alpha + S\alpha \quad \mathrm{all} \quad \chi , \forall\]  

\[(4.3) \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \mathrm{all} \quad \chi , \forall\] \[\qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad\] \[\qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad\] \[\quad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \mathrm{all} \quad \chi , \forall\]  

Now (b) implies that for every \(\epsilon > 0\) there exist strategies \(\chi^{\epsilon}, \Psi^{\epsilon}\) , which are \(\epsilon\) - best in \(\Gamma (\nu)\) , so that  

\[(4.4) \qquad (1 - S)\mathrm{E} + S\nu \geq V(\nu) - \epsilon \quad \mathrm{under} \quad \chi^{\epsilon} \quad \mathrm{for} \quad \mathrm{all} \quad \forall\] \[(4.5) \qquad (1 - S)\mathrm{E} + S\nu \leq V(\nu) + \epsilon \quad \mathrm{under} \quad \Psi^{\epsilon} \quad \mathrm{for} \quad \mathrm{all} \quad x.\]  

We shall now prove (d) by considering the effects of these strategies in \(\Gamma (\nu \pm \delta)\) . Consider first \(\Gamma (\nu - \delta)\) . In this case the expectation for \(x\) and \(\Psi\) may be written as  

\[(4.6) \qquad (1 - S)\mathrm{E} + S(\nu - \delta)\]  

where \(S\) and \(E\) are the same as in \(\Gamma (\nu)\) , for \(x\) and \(\Psi\) . Now, because of (4.5), \(P_{2}\) possesses a strategy \(\Psi^{\epsilon}\) , for all \(\epsilon > 0\) , which yields, when applied to \(\Gamma (\nu - \delta)\) an expectation such that (from (4.6)):  

\[(4.7) \qquad \mathrm{Ex} = (1 - S)\mathrm{E} + S(\nu - \delta) \leq V(\nu) + \epsilon - S\delta \leq V(\nu) + \epsilon\]  

and since such a strategy exists for all \(\epsilon > 0\) we can conclude that  

\[(4.9) \qquad V(\nu - \delta) \leq V(\nu)\]  

We now prove that \(V(\nu - \delta) \geq V(\nu) - \delta\) . From (4.4) there exists, for every \(\epsilon > 0\) , an \(\chi^{\epsilon}\) , such that, when applied to \(\Gamma (\nu - \delta)\) , by (4.6):  

\[(4.10) \qquad \mathrm{Ex} = (1 - S)\mathrm{E} + S (\nu - \delta) \geq V(\nu) - \epsilon - S\delta \quad \mathrm{for} \quad \mathrm{all} \quad \forall\]  

and, since \(P_{1}\) possesses such a strategy for all \(\epsilon > 0\) , and because \(S \leq 1\) , we can conclude that  

\[(4.11) \qquad V(\nu - \delta) \geq V(\nu) - \delta.\]

---

We shall use such that the equality can hold only if \(V(v) = v\) .  

- - : Assume \(V(v - 8) = V(v) - 8\) .  

- - : \(\frac{1}{2}\) has for every \(\epsilon > 0\) a strategy \(\Psi^{\epsilon}\) which is \(\epsilon\) -best. \(\frac{1}{2}\) : - - : \(\frac{1}{2}\) : \(\frac{1}{2}\) : \(\frac{1}{2}\) : \(\frac{\epsilon}{2}\) : \(\frac{\epsilon}{2}\) : \(\frac{\epsilon}{2}\) \(\frac{\epsilon}{2}\) : \(\frac{\epsilon}{2}\) : \(\frac{\frac{1}{2}}{2}\) : \(\frac{\frac{1}{2}}{2}\) : \(\frac{\frac{\epsilon}{2}}{2}\) : \(\frac{\frac{\epsilon}{2}}{2}\) : \(\epsilon\) : \(\frac{\frac{1}{2}}{2}\) : \(\frac{\frac{1}{\epsilon}}{2}\) : \(\frac{\frac{1}{\epsilon}}{2}\) : \(\frac{\epsilon}{2}\) : \(\frac{\frac{1}{\epsilon}}{2}\) : \(\frac{\frac{\epsilon}{2}}{2}\) : \(\frac{\epsilon}{2}\) : \(\frac{\frac{1}{\frac{1}{\epsilon}}}{2}\) : \(\frac{\frac{1}{\frac{1}{\epsilon}}}{2}\) : \(S\) : \(\frac{\frac{1}{\frac{1}{\epsilon}}}{2}\) : \(\frac{1}{\frac{1}{\epsilon}}\) : \(\frac{1}{\frac{1}{\epsilon}}\) : \(\frac{1}{\frac{\frac{1}{\epsilon}}{2}}\) : \(\frac{1}{\frac{1}{\epsilon}}\) : \(\frac{1}{\epsilon}\) : \(\frac{1}{\frac{1}{\epsilon}}\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\frac{\frac{1}{\epsilon}}{2}\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\epsilon\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\frac{S}{2}\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(S\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\epsilon = \frac{1}{\epsilon}\) : \(\frac{1}{\epsilon} = \frac{\frac{1}{\epsilon}}{\epsilon}\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(V\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\alpha\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\beta\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\gamma\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\delta\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\eta\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\zeta\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\xi\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\lambda\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\mu\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\nu\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\rho\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\sigma\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\tau\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\pi\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\chi\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\psi\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\phi\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\theta\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\omega\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\varphi\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\kappa\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\iota\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\Lambda\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\Sigma\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\Omega\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\Pi\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\Xi\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\Gamma\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\Delta\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\Psi\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\Phi\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\Theta\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\Upsilon\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\I\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\J\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\K\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\L\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\M\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\N\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\O\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\P\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\Q\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\R\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(\S\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(T\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(U\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(V_{1}\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\) : \(W_{1}\) : \(\frac{1}{\epsilon} = \frac{1}{\epsilon}\)

---

\[V(v - 8) \geq V(v) - 8 \left(\frac{\alpha - V(v)}{\alpha - v}\right) \quad (4.21)\]  

However, one or the other multipliers of 8 in (4.20) and (4.21) is less than 1 whenever \(V(v) \neq v\) , which would contradict assumption (4.12), so that we can conclude that  

\[V(v - 8) = V(v) - 8 \Longrightarrow V(v) = v \quad (4.22)\]  

which, together with (4.11) establishes the truth of  

\[V(v - 8) \stackrel{\ast}{\geq} V(v) - 8, \quad (\text{all} \quad v, \quad 8) \quad (4.23)\]  

Finally, reversal of the roles of the players suffices to establish the analogues of (4.9) and (4.23) for the game \(r(v + 8)\) and the proof is completed.  

We shall now state an analogous result for the ordinary game \(r^{\frac{1}{4}}(\overrightarrow{W})\) for arbitrary \(\overrightarrow{W}\) :  

LEMMA 2. (a) \(\alpha > 0\) , \(\beta < 0\) are payoff bounds for \(r^{\frac{1}{4}}\)  

(b) \(\frac{5}{8} = (8^1, 8^2, \dots, 8^4)\) , \(8^1 \geq 0\) all 1  

(c) \(\gamma = \max \delta^1\)  

(d) \(\beta \frac{1}{5} \leq \frac{1}{W} \leq \alpha \frac{1}{1}\)  

imply that:  

(e) \(\beta \leq \operatorname {Val} r^{\frac{1}{4}}(\overrightarrow{W}) \leq \alpha\)  

(f) \(\operatorname {Val} r^{\frac{1}{4}}(\overrightarrow{W}) - \gamma \leq \operatorname {Val} r^{\frac{1}{4}}(\overrightarrow{W} - \frac{5}{8})\)  

\[\leq \operatorname {Val} r^{\frac{1}{4}}(\overrightarrow{W}) \leq V a l r^{\frac{1}{4}}(\overrightarrow{W} + \frac{5}{8}) \leq V a l r^{\frac{1}{4}}(\overrightarrow{W}) + \gamma .\]  

This is simply a statement of the well- known fact that the value of an ordinary game is a continuous, monotonic function of its payoffs, obeying the Lipschitz condition of order 1. This may, however, be proved easily, if desired, by suitable modification of the proof of Lemma 1.  

REMARK 2. Since critical vectors are values, Lemmas 1 and 2 apply to critical vectors.  

Since Lemma 2 establishes the continuity of the value mapping M we are in a position to draw some useful conclusions about critical vectors

---

THEOREM 3. If \(\vec{\nabla}\) is the critical vector for \(\vec{\nabla}\) , then \(\vec{\nabla}\) is a fixed point of the value mapping, and, furthermore, \(\vec{W}_1 \in C_1(\vec{\nabla}) \Rightarrow \vec{W}_1 \leq \vec{\nabla}\) and \(\vec{W}_2 \in C_2(\vec{\nabla}) \Rightarrow \vec{W}_2 \geq \vec{\nabla}\) .  

\(\vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla} = \vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla}\) . Follows from the definition of a critical vector, the value mapping, and (2.18).  

\(\vec{\nabla} \vec{\nabla} \vec{\nabla} \cdot \vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla}\vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla} ,\) If \(\vec{\nabla}\) possesses a critical vector, \(\vec{\nabla}\) , then any subset \(s\) of the game elements of \(\vec{\nabla}\) is reduced game, \(\vec{\nabla} \vec{\nabla} \vec{\nabla} (\vec{\nabla} \vec{\nabla} \vec{\nabla})\) (which is formed by assigning \(\vec{\nabla}\) to payoff \(\vec{\nabla}\) for \(i \in \vec{s}\) ), \(\vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla} s\) is a critical vector, \(\vec{\nabla} (\vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla} (\vec{\nabla} s))\) , whose elements are the same as the components of \(\vec{\nabla}\) restricted to the subset \(s\) . Symbolically: \(\vec{\nabla} \vec{\nabla} (\vec{\nabla} \vec{\nabla} s) = \vec{\nabla} s\) .  

\(\vec{\nabla} \vec{\nabla} \vec{\nabla} \nabla\) critical in \(\vec{\nabla}\) implies that for every \(\epsilon > 0\) there exists \(\vec{\nabla} \in \vec{\nabla} (\vec{\nabla})\) such that  

\(\vec{\nabla} \vec{\nabla} (\vec{\nabla} \vec{\nabla} ) \geq \vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla})\) i.e., \((\vec{\nabla} \vec{\nabla} \in C_1(\vec{\nabla}))\)  

\(\vec{\nabla} \vec{\nabla} \vec{\nabla} \in \vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla}) \geq \vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{(\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{(\vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla} )}\) which implies that  

\(\vec{\nabla} \vec{\nabla} \vec{\nabla} \bar{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla} \bar{\nabla} s\)  

\(\vec{\nabla} \vec{\nabla} \vec{\nabla} \dot{\vec{\nabla}} \vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla}(\vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla} (s))\) Lemma 2, (4.24) and the definition of the value map:  

\[\forall \mathrm{al} \vec{\nabla} (\vec{\nabla} \vec{\nabla} \vec{\vec{\nabla}} \vec{\nabla} \vec{\nabla} \vec{\nabla}) \geq \forall \mathrm{al} \vec{\nabla} (\vec{\nabla} \vec{\vec{\nabla}} \vec{\nabla} \vec{\vec{\nabla}} \vec{\nabla} \vec{s})\] \[\qquad = \forall \mathrm{al} \vec{\nabla} (\vec{\nabla} \vec{s}) \geq \vec{\nabla} \vec{\nabla} \vec{\nabla} \dot{\vec{\vec{\nabla}}} \vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla}\] \[\qquad = \forall \mathrm{al} \vec{\nabla} (\vec{\nabla}\vec{\nabla} \vec{\nabla} \vec{\nabla} \dot{\vec{\bar{\nabla}}} \vec{\nabla} \vec{\nabla} \vec{\nabla} \dot{\vec{s}})\]  

\(\vec{\nabla} \vec{\nabla} \vec{\nabla} \hat{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla} \hat{\nabla} s\) a statement that for the value map \(\vec{\nabla}\) for the reduced  

\(\vec{\nabla} \vec{\nabla} (\vec{\nabla} \dot{\vec{\nabla}} \vec{\nabla} \vec{\vec{\nabla}} \vec{s}) \geq \vec{\nabla} \vec{\nabla} \vec{\vec{\nabla}} \vec{\vec{\nabla}} \vec{\nabla} \vec{\nabla} \vec{s})\) (so that \(\vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla}\in C_1(\vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla}))\) .)  

\(\vec{\nabla} \vec{\nabla} \vec{\nabla} \tilde{\nabla} \vec{\nabla} \vec{\nabla} \vec{\nabla} \tilde{\nabla} s\) and we conclude that \(\vec{\nabla} \vec{\nabla} \vec{\nabla} \vec{\vec{\nabla}} \vec{s}\) is critical and the proof is completed.

---

## \(\S 5\) . EXISTENCE OF THE CRITICAL VECTOR - MAIN THEOREM  

THEOREM 5. Every recursive game whose game elements have bounded payoffs and satisfy the supinf condition possesses a critical vector.  

PROOF. Induction on the number of game elements using:  

HYPOTHESIS (k): Every recursive game consisting of k or fewer game elements, all of which have bounded payoffs, and satisfy the supinf condition, possesses a critical vector.  

Now consider any recursive game \(\bar{\Gamma}\) which consists of \(k +\) game elements with the above properties. Remove one element, say \(\Gamma^{\mathbb{Q}}\) and consider the remaining set, \(\bar{\Gamma}^{\mathbb{Q}}\) , as a reduced game \(\bar{\Gamma}^{\mathbb{Q}}(\nu)\) with is a function of the "value" \(\nu\) assigned to \(\Gamma^{\mathbb{Q}}\) . This is then a recursive game with \(k\) elements and hence by hypothesis possesses a cr call vector \(\bar{\nabla}^{\mathbb{Q}}(\nu)\) for all \(\nu\) . Moreover, since Lemma 1 applies to c call vectors, as we have seen, we conclude that \(\bar{\nabla}^{\mathbb{Q}}(\nu)\) is a continuous monotonic function of \(\nu\) in all components.  

Now consider the ordinary game \(\Gamma^{\mathbb{Q}}(\bar{\nabla}^{\mathbb{Q}}(\nu), \nu)\) , which poses a value for all \(\nu\) by virtue of its satisfying the supinf condition. Define:  

\[\bar{\nabla} (\nu) = \mathrm{Val} \Gamma^{\mathbb{Q}}(\bar{\nabla}^{\mathbb{Q}}(\nu), \nu) \quad (5.1)\]  

then applying Lemmas 1 and 2 we obtain the conditions on \(\bar{\nabla} (\nu)\) :  

\[\bar{\nabla} (\nu) - \delta \lesssim \bar{\nabla} (\nu - \delta) \lesssim \bar{\nabla} (\nu) \lesssim \bar{\nabla} (\nu + \delta)\]  

\[\lesssim \bar{\nabla} (\nu) + \delta , \text{all} \delta \geq 0.\]  

\[\beta \lesssim \bar{\nabla} (\nu) \lesssim \alpha \text{for all} \nu \text{such that} \beta \lesssim \nu \lesssim \alpha \quad (5.3)\]  

where \(\alpha , \beta\) are the upper and lower payoff bounds for all of the game elements of \(\bar{\Gamma}\) . Therefore, \(\bar{\nabla} (\nu)\) is a continuous mapping of the \(c\) line segment \([\beta , \alpha ]\) into itself, so that there exists a closed, nonempty set of fixed points, and hence in particular there exists a finite point of minimum absolute value which we shall designate as \(\nu^{*}\) . The there always exists a \(\nu^{*}\) such that:

---

[5. . . . . . . . . . . . . . . . . . . . . and for all v, V(v) = v = |v| ≥ |v*; .  

As a result now show that the (k+1)- vector \(\vec{V}\) defined by \(\vec{\mathbf{\tau}} = \vec{\mathbf{\tau}} (\vec{\mathbf{\tau}}), \vec{\mathbf{\tau}} = \vec{\mathbf{\tau}}\) , and which always exists, is critical in \(\vec{\mathbf{\tau}}\) . To do this we proceed to show that for any \(\epsilon > 0\) there is a \(\vec{\mathbf{\tau}}_1 \in \mathbb{N}_\epsilon (\vec{\mathbf{\tau}})\) such that \(\vec{\mathbf{\tau}}_1 \in \mathbb{T}\) :  

\(\vec{\mathbf{\tau}}_1 \in \mathbb{T}\) . \(\gamma^* > 0\) .  

We first remark that  

\[\vec{\mathbf{v}} (\mathbf{v}) > \mathbf{v} \text{for} 0 \leq \mathbf{v} < \mathbf{v}^*\]  

[5.5] If we let \(\mathbf{v} = \mathbf{v}^* - 8\) , \(8 > 0\) , then  

\(\vec{\mathbf{\tau}}_1 = \vec{\mathbf{\tau}} (\vec{\mathbf{\tau}}_1 - 1) \geq \vec{\mathbf{\tau}} (\mathbf{v}^*) - 8 = \mathbf{v}^* - 8 = \mathbf{v}\) ; but the equality cannot hold, it is valid to conclude the minimum absolute value property of the fixed point \(\mathbf{v}^*\) . Now, (5.5) implies that for every \(\epsilon > 0\) there is a \(\vec{\mathbf{\tau}}_1 \notin \mathbb{T}\) to find \(\vec{\mathbf{v}} (\mathbf{v}^*) > \mathbf{v}^*\) , and hence there exists a \(\delta\) , \(\epsilon < \delta\) , \(\vec{\mathbf{\tau}}_1 \in \mathbb{T}\) .  

\[\vec{\mathbf{v}} (\mathbf{v}^*) > \mathbf{v}^* + 8.\]  

We want to the reduced game \(\vec{\mathbf{\tau}}^r (\mathbf{v}^\epsilon)\) , for which the induces a game \(\vec{\mathbf{\tau}}^r\) generates the existence of a vector \(\vec{\mathbf{\tau}}^r (\mathbf{v}^\epsilon)\) which is critical at \(\vec{\mathbf{\tau}}^r\) , so that there is a vector \(\vec{\mathbf{\tau}}_1^r \in \mathbb{N}_\epsilon (\vec{\mathbf{\tau}}^r (\mathbf{v}^\epsilon))\) with the property:  

5.1 \(\vec{\mathbf{\tau}}_1^r (\vec{\mathbf{\tau}}_1^r, \mathbf{v}^\epsilon) \geq \vec{\mathbf{\tau}}_1^r \mathbf{v}^\epsilon\) for all \(\mathbf{k} \in \mathbb{r}\) .  

We first note that in \(\mathbb{r}^q\) , \(\text{Val} \mathbb{r}^q (\vec{\mathbf{\tau}}^r (\mathbf{v}^\epsilon), \mathbf{v}^\epsilon) > \mathbf{v}^\epsilon + 8\) , and \(\vec{\mathbf{\tau}}_1^r \in \mathbb{T}\) , \(\vec{\mathbf{\tau}}_1^r (\mathbf{v}^\epsilon, \mathbf{v}^\epsilon)\) , applying Lemma 2 we get  

\[\text{Val} \mathbb{r}^q (\vec{\mathbf{\tau}}_1^r, \mathbf{v}^\epsilon) > \mathbf{v}^\epsilon.\]  

\(\vec{\mathbf{\tau}}_1^r \in \mathbb{T}\) are simply the statement that the \(\mathbf{k} + 1\) vector \(\vec{\mathbf{\tau}}_1^r, \mathbf{v}^\epsilon\) has the property that \(\mathbb{M}(\vec{\mathbf{\tau}}_1) \geq \vec{\mathbf{\tau}}_1^r\) , so that  

\[\vec{\mathbf{\tau}}_1^r \in \mathbb{C}_1 (\vec{\mathbf{\tau}}^r).\]  

ed  

\(\vec{\mathbf{\tau}}_1^r \in \mathbb{T} \in \mathbb{T}\)  

\[\mathbf{v}^\epsilon \in \mathbb{N}_\epsilon (\mathbf{v}^*)\]  

\(\vec{\mathbf{\tau}}_1^r \in \mathbb{T}_1^r\) , using Lemma 1 for critical vectors, that \(\vec{\mathbf{\tau}}^r (\mathbf{v}^\epsilon) \in \mathbb{N}_\epsilon (\vec{\mathbf{\tau}}^r (\mathbf{\tau}^*))\) ,

---

which, because \(\overrightarrow{W_{1}}^{r} \in \mathbb{N}_{6}(\overrightarrow{V}^{r}(v^{\epsilon}))\) , and \(8 < \epsilon\) , implies that  

\[\overrightarrow{W_{1}}^{r} \in \mathbb{N}_{2\epsilon}(\overrightarrow{V}^{r}(v^{*})) \quad (5.11)\]  

and combining (5.10) and (5.11) we see that  

\[\overrightarrow{W_{1}} = [\overrightarrow{W_{1}}^{r}, v^{\epsilon}] \in \mathbb{N}_{2\epsilon} [(\overrightarrow{V}^{r}(v^{*}), v^{*})] \quad (5.12)\]  

and hence that \(\overrightarrow{W_{1}} \in \mathbb{N}_{2\epsilon}(\overrightarrow{V})\) , and Case 1 is completed.  

CASE 2: \(v^{*} \leq 0\) .

---

empty game, which has zero payoff for all strategies, and hence value the hypothesis is obviously satisfied, since zero itself is critical in this game, and the proof of Theorem 5 is completed. (An independent proof of the hypothesis for recursive games with one element is contained in Theorem 8. ) We can now summarize our results, using Theorems 2, 5, and Corollary 1:  

THEOREM 6. MAIN THEOREM. Every recursive game whose elements have bounded payoffs and satisfy the supinf condition possesses a solution, \(\overline{\mathbf{V}}\) , and \(\epsilon\) - best strategies \(x^{\epsilon}\) and \(\overline{\mathbf{y}}^{\epsilon}\) for the players which are stationary in all components i for which either \(\overline{\mathbf{r}}^{\frac{1}{2}}\) satisfies the minimax condition or \(\overline{\mathbf{v}}^{\frac{1}{2}}\) is favorable.  

An important consequence of Theorem 6 is that any recursive whose game elements are matrix games (matrices with generalized payoff elements of the form \(\mathbf{a}_{ij} = \mathbf{p}_{ij}\mathbf{e}_{ij} + \mathbf{e}_{ij}\mathbf{k}_{ij}\mathbf{r}^{k}\) ) possesses a solution at \(\epsilon\) - best stationary strategies for the players, since all such matrix elements satisfy the minimax condition.  

## §6. GENERALIZATIONS  

For our purposes we shall define a stochastic game, \(\vec{\mathbf{r}}\) a collection of game elements \((\vec{\mathbf{r}}^{\frac{1}{2}})\) , each with strategy spaces \(S_{1}^{\frac{1}{2}}\) \(S_{2}^{\frac{1}{2}}\) , and generalized payoff function of the form:  

\[\mathrm{H}^{1}(x^{1},\mathrm{y}^{1};\vec{\mathrm{r}}) = \mathrm{e}^{1} + \mathrm{p}^{1}\mathrm{S} + \mathrm{e}_{1}\mathrm{q}^{1}\mathrm{j}\mathrm{r}\mathrm{j};\quad (x^{1},\mathrm{y}^{1})\in S_{1}^{1}\times S_{2}^{1}\]  

(6.1)  

\[\mathrm{p}^{1},\mathrm{q}^{1}\mathrm{j}\mathrm{j}\geq 0;\mathrm{p}^{1} + \mathrm{e}_{1}\mathrm{q}^{1}\mathrm{j} = 1\]  

where now \(\mathrm{e}^{\frac{1}{2}}\) is a payoff which takes place whether or not the play \(\mathrm{p}^{\frac{1}{2}}\) is the stop probability, and the \(\mathrm{q}^{\frac{1}{2}}\mathrm{j}\) are the transition probab to other game elements, as before. With such games the payoffs are ed to accumulate throughout the course of the play, in distinction t cursive games, where payoff can take place only when the play stops.  

If we now extend all of our definitions and formulae in t viou s manner (which amounts to replacing \(\overline{\mathbf{P}}\overline{\mathbf{E}}\) by \(\overline{\mathbf{E}}\) in the expect formulae) to stochastic games, we notice that Theorems 1, 2, 3, and main true for stochastic games. Lemma 1, however, fails ((c) is no true, and the crucial \(\frac{1}{2}\) of (d) must be replaced by the milder \(\frac{1}{2}\) ) (e) of Lemma 2 is no longer true, so that the extension of the main rem to arbitrary stochastic games is prevented, and we must be cont

---

empty game, which has zero payoff for all strategies, and hence value the hypothesis is obviously satisfied, since zero itself is critical in this game, and the proof of Theorem 5 is completed. (An independent proof of the hypothesis for recursive games with one element is contained in Theorem 8. ) We can now summarize our results, using Theorems 2, 5, and Corollary 1:  

THEOREM 6. MAIN THEOREM. Every recursive game whose elements have bounded payoffs and satisfy the supinf condition possesses a solution, \(\bar{\mathbf{v}}\) and \(\epsilon\) - best strategies \(x^{\epsilon}\) and \(\mathbf{v}^{\epsilon}\) for the players which are stationary in all components i for which either \(\Gamma^{\perp}\) satisfies the minimax condition or \(\mathbf{v}^{\perp}\) is favorable.  

An important consequence of Theorem 6 is that any recursive whose game elements are matrix games (matrices with generalized payoff elements of the form \(\mathbf{a}_{ij} = \mathbf{p}_{ij}\mathbf{e}_{ij} + \mathbf{e}_{ij}\mathbf{q}_{ij}^{\mathrm{T}}\mathbf{r}^{k})\) possesses a solution a \(\epsilon\) - best stationary strategies for the players, since all such matrix g elements satisfy the minimax condition.  

## \(\S 6\) GENERALIZATIONS  

For our purposes we shall define a stochastic game, \(\bar{\mathbf{r}}\) a collection of game elements \((\Gamma^{\perp})\) , each with strategy spaces \(S_{1}^{\perp}\) \(S_{2}^{\perp}\) , and generalized payoff function of the form:  

\[\mathrm{H}^{1}(x^{1},\mathrm{y}^{1};\bar{\mathrm{r}}) = \mathrm{e}^{1} + \mathrm{p}^{1}\mathrm{S} + \mathrm{e}_{1}\mathrm{q}^{1}\mathrm{j}^{1}\mathrm{r};\mathrm{~}(x^{1},\mathrm{y}^{1})\in \mathrm{S}_{1}^{1}\times \mathrm{S}_{2}^{1}\]  

(6.1)  

\[\mathrm{p}^{1},\mathrm{q}^{1}\mathrm{j}\geq 0;\mathrm{p}^{1} + \mathrm{e}_{1}\mathrm{q}^{1}\mathrm{j} = 1\]  

where now \(\mathrm{e}^{\mathrm{i}}\) is a payoff which takes place whether or not the play \(\mathrm{p}^{\mathrm{i}}\) is the stop probability, and the \(\mathrm{q}^{\mathrm{i}}\mathrm{j}\) are the transition probab to other game elements, as before. With such games the payoffs are ed to accumulate throughout the course of the play, in distinction t cursive games, where payoff can take place only when the play stops.  

If we now extend all of our definitions and formulae in tvious manner (which amounts to replacing \(\mathrm{P}\bar{\mathrm{E}}\) by \(\bar{\mathrm{E}}\) in the expect formulae) to stochastic games, we notice that Theorems 1, 2, 3, and main true for stochastic games. Lemma 1, however, fails ((c) is no true, and the crucial \(\frac{\epsilon}{5}\) of (d) must be replaced by the milder \(\frac{\epsilon}{5}\) ) (e) of Lemma 2 is no longer true, so that the extension of the main rem to arbitrary stochastic games is prevented, and we must be cont

---

zeromapie a few special cases.  

n  

roof  

### a. PSEUDO-RECURSIVE GAMES  

d  

A pseudo- recursive game is a stochastic game for which \(e^{1} / p^{1}\) is bounded for all \(x^{1}\) , \(y^{1} \in S_{1}^{1} \times S_{2}^{1}\) in all game elements. Such a stochastic game is always be reduced to an equivalent recursive game, by simply rewriting the payoff function in the form:  

\[6.2 \qquad \stackrel {\dots}{\underset{\dots}{\dots}} \stackrel {\dots}{\underset{\dots}{\dots}} \stackrel {\dots}{\underset{}{\dots}} \stackrel {\dots}{\underset{\dots}{\dots}} \stackrel {\dots}{=} \stackrel {\dots}{\underset{\dots}{\dots}} \stackrel {\dots}{\underset {\dots}{\dots}} \stackrel {\dots}{\underset{\dots}{\dots}} \stackrel {\cdots}{\underset{\dots}{\dots}} \stackrel {\cdots}{\underset{\dots}{\dots}}\]  

This is formally the same as (1.0), so that:  

game  

game  

d  

me  

a. Simple stochastic game is a stochastic game which consists of all the elements, which can at most repeat itself, with payoff function for them:  

o be.  

and  

and  

and  

and  

for every \(x^{5} \in S_{1} \times S_{2}\)  

for every \(x^{5} \in S_{1} \times S^{2}\)  

tops  

tops  

tile  

low- n  

re- f  

re- f  

mple answer to the existence of a solution for simple stochastic games,  

ob-  

on  

re-  

re-  

nger  

1  

eo-  

to  

to  

s  

s  

s

---

PROOF. We simply remark that every point of the extended rea line is in either \(C_{1}(r)\) or \(C_{2}(r)\) , and that neither is empty since is always in \(C_{1}\) and \(+\infty\) is always in \(C_{2}\) , so that the intersection of their closures is non- empty. But a point in the closure of both is critical for \(r\) , and the theorem is proved.  

### c. UNIVALENT STOCHASTIC GAMES  

A univalent stochastic game is one for which the payoffs are always non- negative (or non- positive) for all strategies, and in all games. Such games are useful for describing certain pursuit games, which Player 1, the player being pursued, receives some positive payoff from the pursuer \((P_{2})\) for every move that takes place for which he successfully avoids capture, the play ending with no payoff when capture takes place.  

It is useful now to introduce the notion of a "trap" in a stochastic game, which is an element or set of elements such that once play reaches an element of the trap one of the players can force the pl to remain in trap indefinitely in such a way as to accumulate payoffs f the other player, and hence achieve an arbitrarily high expectation. T are, then, sets of elements which have infinite values in the sense of (6.4). A game contains no traps when each player can prevent infinite verse expectations in all elements. We shall see, however, that even trap- free stochastic games do not always possess solutions, at least in the sense of our previous definition of a solution.  

THEOREM 9. Every univalent stochastic game, whose game elements satisfy the supinf condition, and which contains no traps, possesses a solution.  

PROOF. Consider the sequence \(\{\overrightarrow{W_{k}}\}\) :  

\[\overrightarrow{W_{0}} = \overrightarrow{0\] \[\overrightarrow{W_{k + 1}} = M(\overrightarrow{W_{k}})\]  

which is generated by iterating the value mapping. Since all payoffs a non- negative we know that \(\overrightarrow{W_{1}} \geq 0 = \overrightarrow{W_{0}}\) . Now, assume that \(\overrightarrow{W_{k + 1}} \geq \overrightarrow{W_{k}}\) . Then, by Lemma 2(f) \(\text{val} \overrightarrow{r^{1}} (\overrightarrow{W_{k + 1}}) \geq \text{val} \overrightarrow{r^{1}} (\overrightarrow{W_{k}})\) for all \(i\) , which implies that \(M(\overrightarrow{W_{k + 1}}) \geq M(\overrightarrow{W_{k}})\) which means that \(\overrightarrow{W_{k + 2}} \geq \overrightarrow{W_{k + 1}}\) so that by induction we have proved:  

(6.5) \(\{\overrightarrow{W_{n}}\}\) is monotone increasing in all components.

---

tended real
tty since - 
intersection 

of both is 

yoffs are 

In all game
it games, ir 

ive payoff
hich he 

hen capture 

"in a
that once th 

rce the play
payoffs frc 

tation. Tra
sense of 

infinite ad
nat even 

at least in 

t least in 

t least in 

t least in 

t least in 

t least in 

t least in 

t least in 

t least in 

t least in 

t least in 

t least in 

t least in 

t least in 

<|det|>[[0, 0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0]

---

where the interpretation is that if the players are playing strategies \(X^{1}\) in \(r^{1}\) , then in the (infinitesimal) time interval dt the play stops with payoff \(e^{1}\) with probability \(p^{1}dt\) , while with probability \(q^{1}dt\) the players move on and play \(r^{1}\) . The \(p^{1}\) and \(q^{1}\) are referred to as transition rates. They are non- negative, but do not necessarily sum to unity.  

In such games the players are at each instant playing some strategy, but they are free to change at any time. However, we assume that with all admissible time dependent strategies the transition rates are integrable, i.e., \(f p^{1}dt\) and the \(f q^{1}dt\) always exist. (In any actual game it is simply impossible that the players could change strategies so fast that this condition would not be met.) We furthermore assume that the transition rates \(p^{1}\) and \(q^{1}\) , as well as the payoffs \(e^{1}\) , are bounded for all strategies, in all elements.  

We shall show that we can, in a simple manner, associate with \(\bar{\Gamma}\) a discrete time recursive game \(\bar{\Gamma} (\Delta)\) , which, if it has a critical vector, supplies all the information necessary for optimal (or \(\epsilon\) - best) play in \(\bar{\Gamma} - - 1\epsilon\) , which has the same value, and whose \(\epsilon\) - best strategic furnish \(\epsilon\) - best strategies for \(\bar{\Gamma}\) . Thus the problem of continuous time recursive games will be reduced to that of discrete time games which we have already discussed.  

The reduction to a discrete time game is accomplished as follow Let \(\Delta\) be a positive number such that \(\Delta (p^{1} + \epsilon_{j}q^{1}j)\) is \(\leq 1\) for all strategies in all elements. (The existence of such a \(\Delta\) is guaranteed the boundedness of the transition rates.) Then let \(\bar{\Gamma} (\Delta)\) be the discrete time recursive game whose payoff function for the i- th element is:  

\[\mathrm{H}^{1}(x^{1},y^{1};\bar{\Gamma} (\Delta)) = p^{*1}e^{*1} + \epsilon_{j}q^{*1}j^{1}j^{1}(\Delta) \quad (7.2)\]  

where the numbers are defined from the payoff of \(\bar{\Gamma}\) for the same strategies, given by (7.1) as follows:  

\[\begin{array}{c}{p^{*1} = \Delta p^{1},\quad q^{*1}j = \Delta q^{1}j\qquad (1\neq j)}\\ {q^{*1}1 = 1 - \Delta (p^{1} + \epsilon_{j}q^{1}j),\quad e^{*1} = e^{1}.} \end{array} \quad (7.3)\]  

If the discrete recursive game \(\bar{\Gamma} (\Delta)\) so constructed possess a critical vector, then for every \(\epsilon > 0\) there exists a strategy \(x^{\epsilon} = (\bar{X}_{t})\) for \(P_{1}\) (constructed according to the method of (2.7)), satisfies the inequalities (2.8). We wish to assert that this strategy \(x^{\epsilon}\) is also \(\epsilon\) - best in the continuous time game \(\bar{\Gamma}\) , from which \(\bar{\Gamma} (\Delta)\) derived, but we must first supply a rule for the unambiguous applicatic

---

ies \(\mathbf{x}_{1}^{1}\) 1 \(\mathbf{\bar{\tau}} = \mathbf{\bar{\tau}}\) is not a stationary strategy.  

y stops First. we define an event to be any time the play stops or there 1dt \(\mathbf{\Sigma} = \mathbf{\Sigma}\) a \(\mathbf{\Sigma} = \mathbf{\Sigma}\) event element. We define the k- th round to be the to as time between the chance of the k- 1- st event and the k- th event. We m to be state the rule:  

e strat at with nte- 1 game fast the ounded  

with 1cal 1st) 1egies time 1we  

follows: all 1eed by  

lis- is:  

rate-  

rate-  

1.4  

1.5  

1.6  

1.7  

1.8  

1.9  

1.10  

1.11  

1.12  

1.13  

1.14  

1.15  

1.16

---

process which takes place only with each event, in which time is eliminat  

Whatever strategy \(\mathbb{Y} = \bar{\mathbb{Y}} (t) \mathbb{P}_{2}\) is playing, the transition rate \(\mathbb{P}^{1}, \mathbb{q}^{1 \mathrm{j}},\) as well as the payoffs \(\mathbb{e}^{1}\) are functions of the time subject to (7.5). Let us restrict our attention to the 1- th element, and let \(\mathrm{n}(t) \mathrm{d}\) be the probability of an event in the time interval \(\mathrm{d} t\) , so that the relation rate \(\mathrm{n}(t)\) is:  

\[\mathrm{n}(t) = \mathrm{p}^{1}(t) + \mathrm{e}_{1}^{1} \mathrm{q}^{1 \mathrm{j}}(t) \quad (7.6)\]  

Furthermore, let \(\mathbb{R}(t)\) be the probability that the k- th event has not yet occurred at time \(t\) (Note: \(t\) measured from beginning of \(k\) - th round). Then clearly \(\mathbb{R}(t)\) is monotone decreasing, bounded between 0 and 1, and satisfies the relation:  

\[\int_{0}^{t} \mathbb{R}(\tau) \mathrm{n}(\tau) \mathrm{d} \tau = 1 - \mathbb{R}(t) \quad (7.7)\]  

The probability that by time \(t\) the \(k\) - th round will have resulted in a stop, \(\bar{\mathbb{p}}^{1}(t)\) , is  

\[\bar{\mathbb{p}}^{1}(t) = \int_{0}^{t} \mathbb{R}(\tau) \mathbb{p}^{1}(\tau) \mathrm{d} \tau \quad (7.8)\]  

while the probability that it will have resulted in a transition to \(\mathbb{r}^{1}, \bar{\mathbb{q}}^{1 \mathrm{j}}(t)\) , is  

\[\bar{\mathbb{q}}^{1 \mathrm{j}}(t) = \int_{0}^{t} \mathbb{R}(\tau) \mathbb{q}^{1 \mathrm{j}}(\tau) \mathrm{d} \tau \quad (7.9)\]  

Finally, if  

\[\bar{\mathbb{e}}^{1}(t) = \left(\int_{0}^{t} \mathbb{R}(\tau) \mathbb{p}^{1}(\tau)\mathbb{e}^{1}(\tau) \mathrm{d} \tau\right) / \left(\int_{0}^{t} \mathbb{R}(\tau) \mathbb{p}^{2}(\tau) \mathrm{d} \tau\right)\]  

denotes the mean payoff (which is, of course, bounded by any bounds for \(\mathbb{e}^{1}\) ), then we can write the total expected payoff as:  

\[\bar{\mathbb{p}}^{1}(t) \bar{\mathbb{e}}^{1}(t) = \int_{0}^{t} \mathbb{R}(\tau) p^{1}(\tau) e^{1}(\tau) \mathrm{d} \tau \quad (7.10)\]  

However, making use of (7.5), we have that for the \(k\) - th round

---

iminate the 1-th element, under \(x^e\) and for all \(\bar{Y} (t)\) :  

ion rat ject tc n(t)dt he trar:  

\[\sum_{j=0}^{t}\mathbb{R}(\tau)p^{\frac{1}{2}}(\tau)e^{\frac{1}{2}}(\tau)d\tau+\sum_{j}^{t}W^{j}\int_{0}^{t}\mathbb{R}(\tau)q^{\frac{1}{2}}d\tau\] \[= \int_{0}^{t}\mathbb{R}(\tau)\left[p^{\frac{1}{2}}(\tau)e^{\frac{1}{2}}(\tau)+\sum_{j}^{t}q^{\frac{1}{2}}d\tau\right]d\tau\] \[\geq \int_{0}^{t}\mathbb{R}(\tau)\left[n(\tau)W^{\frac{1}{2}}+\frac{1}{\Delta}u^{\frac{1}{2}}-\frac{1}{\Delta}\delta_{k+1+[\tau/\Delta]}^{\frac{1}{2}}\right]d\tau\]  

re- 2  

\[\sum_{j=0}^{t}\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\] \[\geq \mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)W^{\frac{1}{2}}+\frac{1}{\Delta}u^{\frac{3}{2}}\left(\int_{0}^{t}\mathbb{R}(\tau)d\tau\right)\] \[\geq \mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\delta_{k+1+[\tau/\Delta]}^{\frac{1}{2}}.\]  

Now we use the representation of (2.7)  

\[\sum_{j=0}^{t}\mathbb{R}(\tau)\mathbb{R}\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau))\]  

for \(\sum_{j=0}^{t}\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{E}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{E}(\tau)\mathbb{R}(\tau)\) , and certainly \(\tau \leq T\) , we have  

\[\int_{0}^{t}\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\dots \mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\mathbb{E}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau))\] \[\geq \int_{0}^{t}\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{R}(\mathbb{E}(\tau)\mathbb{E}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{E}(\tau)\mathbb{E}(\tau)\mathbb{R}(\tau)\mathbb{R}(\tau)\] \[\geq \int_{0}^{t}\mathbb{R}(\tau)\mathbb{R}(\tau)\dots \mathbb{R}(\tau)\mathbb{R}\mathbb{R}(\tau)\mathbb{R}(\tau)\mathbb{E}(\tau)\mathbb{R}(\mathbb{E}(\tau)\mathbb{R}(\tau)\mathbb{R}(\mathbb{E}(\tau)\mathbb{R}(\mathbb{E}(\tau)\mathbb{R}(\mathbb{E}(\tau)\dots \mathbb{R}(\tau)\mathbb{R}(\mathbb{E}(\tau)\mathbb{R}(\mathbb{E}(\mathbb{E}(\tau)\mathbb{R}(\mathbb{E}(\mathbb{E}(\tau)\mathbb{R}\mathbb{R}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\tau)\mathbb{R}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{R}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{\mathbb{\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}(\mathbb{E}\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{E}(\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathrm{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathcal{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbf{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\mathbb{\epsilon}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}\]

---

and therefore the ultimate transition probabilities \(\tilde{\mathbf{p}}_{\mathbf{k}}^{\mathrm{i}}\) and \(\tilde{\mathbf{q}}_{\mathbf{k}}^{\mathrm{i}\mathrm{j}}\) for the k- th round, which are given by the limit of (7.12) as \(t \longrightarrow \infty\) , satisfy:  

\[\tilde{\mathbf{p}}_{\mathbf{k}}^{\mathrm{i}\mathrm{i}\mathrm{i}} + \sum_{\mathrm{j}}^{\mathrm{i}}\tilde{\mathbf{q}}_{\mathbf{k}}^{\mathrm{i}\mathrm{j}}\mathbf{w}^{\mathrm{j}}\geqslant [1 - \mathrm{R}(\infty)]\mathbf{w}^{\mathrm{i}} + \frac{1}{\Delta}\mathbf{u}^{\mathrm{i}}\left(\int_{0}^{\infty}\mathrm{R}(\tau)\mathrm{d}\tau\right) - (\frac{1}{2})^{\mathrm{k}_{8}} \quad (7.13)\]  

We now observe that if \(\mathbf{w}^{\mathrm{i}} > 0\) (which implies \(\mu^{\mathrm{i}} > 0\) ) that \(\mathbb{R}(\infty)\) must be zero, since otherwise  

\[\int_{0}^{\infty}\mathbb{R}(\tau)\mathrm{d}\tau\]  

would be infinite ( \(\mathbb{R} \in \mathbb{I}\) ) and the left side of (7.13) would be infinite an impossibility for bounded \(\epsilon^{\mathrm{i}}\) and finite \(\mathbf{w}^{\mathrm{j}}\) . Therefore if \(\mathbf{w}^{\mathrm{i}}\) is positive \([1 - \mathbb{R}(\infty)]\mathbf{w}^{\mathrm{i}} = \mathbf{w}^{\mathrm{i}}\) , while if \(\mathbf{w}^{\mathrm{i}} \leq 0\) then \([1 - \mathbb{R}(\infty)]\mathbf{w}^{\mathrm{i}} \geq \mathbf{w}^{\mathrm{i}}\) . Hence (7.13) implies that  

\[\tilde{\mathbf{p}}_{\mathbf{k}}^{\mathrm{i}\mathrm{i}\mathrm{j}} + \sum_{\mathrm{j}}^{\mathrm{i}}\tilde{\mathbf{q}}_{\mathbf{k}}^{\mathbf{i}\mathrm{j}}\mathbf{w}^{\mathrm{j}} \geqslant \mathbf{w}^{\mathrm{i}} + \frac{1}{\Delta}\mathbf{u}^{\mathrm{i}} \left(\int_{0}^{\infty}\mathbb{R}(\tau)\mathrm{d}\tau\right) - (\frac{1}{2})^{\mathbf{k}_{8}} \quad (7.14)\]  

Finally, since \(\Delta\) was chosen so that \(\Delta (\mathbf{p}^{\mathrm{i}} + \epsilon_{\mathrm{j}}^{\mathrm{i}\mathrm{j}}\mathbf{q}^{\mathrm{i}\mathrm{j}}) \leq 1\) , fc all strategies in all elements, we have that \(\Delta \mathbf{n}(\tau) \leq 1\) for all \(\tau\) , that  

\[\int_{0}^{t}\mathbb{R}(\tau)\mathbf{n}(\tau)\mathrm{d}\tau = 1 - \mathbb{R}(t) \lesssim \int_{0}^{t}\mathbb{R}(\tau)\frac{1}{\Delta}\mathrm{d}\tau\] \[= \frac{1}{\Delta}\int_{0}^{t}\mathbb{R}(\tau)\mathrm{d}\tau .\]  

Therefore  

\[\frac{1}{\Delta} \int_{0}^{\infty} \mathbb{R}(\tau) \mathrm{d}\tau \geq 1 - \mathbb{R}(\infty) .\]  

But since \(\mu^{\mathrm{i}} = 0\) unless \(\mathbf{w}^{\mathrm{i}} > 0\) , and because \(\mathbf{w}^{\mathrm{i}} > 0\) implies \(\mathbb{R}(\mathbf{x}\) we can conclude that  

\[\frac{1}{\Delta} \mu^{\mathrm{i}} \left(\int_{0}^{\infty} \mathbb{R}(\tau) \mathrm{d}\tau\right) \geq \mu^{\mathrm{i}} .\]

---

for  

0,  

8.  

that  

finite,  

is  

> W  

for  

, so  

for  

, so  

(∞) = 0,  

for  

for  

for  

for

---

## §8. SUMMARY AND COMMENTS  

Our main tools have been the concepts of the value mapping and the critical vector. Theorems 1 and 2 establish that the critical vector is a solution of discrete time recursive (and stochastic) games, while Theorems 10 and 11 extend this result to the continuous time case. We can therefore state with full generality:  

If a recursive or stochastic game, either discrete or continuous (or mixed) time, possesses a critical vector then that critical vector is unique and is the solution of the game.  

Theorem 5 establishes the existence of a critical vector for a discrete time recursive games whose elements have bounded payoffs and satisfy the sup- inf condition. This result, together with the above result, implies that:  

Every discrete time recursive game whose elements have bounded payoffs and satisfy the sup- inf condition, as well as every continuous time game for which a derived discrete time game is such a recursive game, possesses a solution.  

This latter result cannot be extended to stochastic games, si the existence of a critical vector is no longer guaranteed, as shown by Examples 3 and 4 of §9.  

We should like now to emphasize several points. We have added ourselves solely to the combinatorial problem of what can be expected when a number of games are "hooked together" with various feedback path (by allowing some outcomes to feed into other games instead of numerical payoffs), under the assumption that the individual games (elements) are "inherently soluble" (i.e., that when the loops are opened, by replicating game payoffs by numerical payoffs, the resulting ordinary games have solutions).  

The situation is fully analogous to servomechanism analysis, where the complex behavior of a closed loop servomechanism is analyzed terms of the (open loop) behavior of its parts. The theory of servomechanisms is concerned solely with the problem of predicting this loop behavior from know behavior of the components. An appropriate alternate name for recursive games would be "games with feedback".  

Since it was not necessary to place any restrictions on the

---

game elements to achieve our results, they are valid whether the elements be matrix games, games on the square, infinite games in extensive and some type as yet undiscovered, or for that matter other recursive vectors. It is therefore improper to regard recursive games as a partiu- . lile for class of games. Rather, the concept is one which can be applied to We game (every game is trivially a one element recursive game), but which is useful only if the game is such that there are a number of different situations which are confront the players (the game elements) and the behavior of these elementary situations is completely understood.  

## 15. EXPRESS, COUNTER-EXAMPLES, APPLICATIONS  

In order to illustrate the results, and to motivate some of the restrictions imposed on the theorems, we list some simple examples of dis- . and re- . and re- . re- . re- . re- . re- . re- . re- . re-. re- . re- . re- . re- . re- . re- . re. re- . re- . re- . re- . re- . re- . re . re- . re- . re- . re- . re- . re- .  

3, since by  

addres- .  

paths  

eral ( are  

placing  

s,  

zed in  

closed  

alter  

the typ  

the typ

---

\[\sum_{t = 1}^{\infty}\alpha_{t}< \epsilon .\]  

EXAMPLE 3.  

\[r^2:(1 + r^2);r^3:(-2 + r^3).\]  

EXAMPLE of a stochastic game with traps, for which no solution exists.  

EXAMPLE 4.  

\[r^1:\left( \begin{array}{cc}1 + r^2 5\] \[-5 0 \end{array} \right)r^2:\left( \begin{array}{cc} - 1 + r^1 5\] \[-5 0 \end{array} \right).\]  

This is an example of a stochastic game which contains no tr but which still does not possess a solution according to our definitio due to the fact that under the "best" strategies the expectation oscil This game does not possess a critical vector.  

EXAMPLE 5.  

\[r^1:\left( \begin{array}{cc}r^1 r^1\] \[r^2 20\] \[20 r^2 \end{array} \right)r^2:(-10).\]  

This is a recursive game satisfying the minimax condition, 1 which the value of \(r^1\) is 5, with optimal strategies [0, 1/2, 1/2 for \(P_1\) and [1/2, 1/2] for \(P_2\) in \(r^1\) . However, for any truncation (compulsory stop after n- rounds) the value of \(r^1\) is 10 instead of This shows that the solution of a recursive (or stochastic) game can general be obtained as a limit of solutions of truncated games. Note that for this example the iterated value mapping starting with 0 do not converge to the value of the game.  

EXAMPLE 6. "Colonel Blotto commands a desert outpost staff three military units, and is charged with the task of capturing the e campment of two units of enemy tribesmen, which is located ten miles

---

Lets score + 1 if he successfully answers the easy base without losing the easy base, and - 1 if he loses his easy base and any mismatches. If the game are impossible, end the game and a draw. A draw is a game where the defending team is either stronger, or an attacking team is weaker than the defending strength or either stronger, then it is necessary to use base winners. 

In this game a strategy for a player to a single digit's greatest possible step is a partition of wins into attacking and defending steps. Letting A stand for attack, D for defend, the matrix for this game is: 

\[ \text{allution} \]

\[ \text{traps,} \]

\[ \text{scillate} \]

, for 

/1) 

tion 

of 5. 

annot in 

te also 

does 

ffed by 

en- 

s away. 

.

---

BIBLIOGRAPHY 

[1] SHAPLEY, L. S., "Stochastic games," Proceedings of the National Academy of Sciences, U.S.A., 39 (1953), pp. 1095-1100. 

H. Everett 

Princeton University