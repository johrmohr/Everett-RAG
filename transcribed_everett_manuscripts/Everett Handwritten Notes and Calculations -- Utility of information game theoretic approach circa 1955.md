# Everett Handwritten Notes and Calculations -- Utility of information game theoretic approach circa 1955.pdf

Ully of Information, Some Unorthodox approach. 

Model: \(P_1\) has Subjective distribution on random variable \(P_1(x)\) \(P_2\) has "1" "1" "1" \(P_2(x)\) 

They each make a guess of theoretical value
Possible Payoff: (a) Nearest player wins overall
(b) Payoff according to actual distance
of game to current result 

the Model for "Realistic" A large ensemble
total at in every run, panel \(P_2\)'s distribution
for each work out (single object thought) 

Example \(P_1\) has uniform over entire interval
\(P_2\) has uniform over half interval. 

Combine by following manner: number
selected at random from uniform interval,
then \(P_2\) (only) is informed of which half
the number lies in. 

In more generally We can simply consider
a joint distribution on \(N\)-variables. The
players betting on a single variable
while they may possess differing information on the
other variables. This gives a model in which
Subjective probability each with are different, while
both are correct in the long run

---

by studying such a model, and in particular
killing behavior of the players, one can study
the effects, i.e. the utility, of information. 

Ultimate objective to define game in a
natural way so that the df. of information
from information Theory (EPHP) is a direct
measure of the relative advantages of the
players. (Condition i) of the above, briefly the
advantages of players who know another variable
in joint choice over players whose not.) 

Comparably all the above in terms of
uniform distribution, often transformed to this
by Social Transformation. (then clearly minimize 

Strategy for players is to play uniformly over his
(uniform) subjective distribution.)
(somewhere) 

Example \(P_1\) uniform over \([0, 1]\) 

\(P_2\) uniform over \([0, \frac{1}{2}]\) 

(actually, successive games would give \(P_2\) over \([0, \frac{1}{2}]\))
both time and \([\frac{1}{2}, 1]\) at half, but it suffices
to coincide the above case, in which "initially"
the number will be chosen only from \([0, \frac{1}{2}]\)

---

Give example of cardinals, players buy tickets, etc. 

Then \(P_1\) plays (i.e. games) a number uniformly from \([0, 1]\) while \(P_2\) games uniformly from \([0, \frac{1}{2}]\) and the number itself is distributed uniformly from \([0, \frac{1}{2}]\). 

So we shall now compute the actions of various payoffs. 

First Payoff \(\in \mathbb{R}\) meaning wins 1 unit from state \(s\). 

Assume \(K\) is the actual number chosen,
\(y\) is the guess by \(P_1\) and \(P_2\). 

Joint
deaths
of guessers

---

Note area content from \(x=0\) to \(x=\frac{1}{4}\) and equal to \(\frac{1}{2}\) of total area or \(\frac{1}{8}\) actually changes then through and increase to \(\frac{1}{2}\) of total. 

area right \(\triangle\) height \(h\) \(\Rightarrow\) base 24 

that area = \(\frac{1}{2}(h)(2h) = \frac{h^2}{2}\) 

so that area of shaded region is \(x^2 + \left(\frac{1}{2} - x\right)^2\) for \(x > \frac{1}{4}\) < \(\frac{1}{2}\) = \(x^2 + \frac{1}{4} - x + x^2\)

---

So area \(\frac{\pi}{4}\) (with \(x\) as 

\[A(\frac{\pi}{4}) = \begin{cases} \frac{1}{8} & x \leq \frac{1}{4} \\ 2x^2 - x + \frac{1}{4} & \frac{1}{4} \leq x \leq \frac{1}{2} \end{cases}\]

(Find, for \(x = \frac{1}{4}\) we get \(2(\frac{1}{4})^2 - \frac{1}{4} + \frac{1}{4} = \frac{2}{16} = \frac{1}{8}\) 

\[for x = \frac{1}{2} \quad 2(\frac{1}{2})^2 - \frac{1}{2} + \frac{1}{4} \\
= \frac{2}{4} - \frac{1}{2} + \frac{1}{4} = \frac{1}{4}\]

Now, to normalize, we must multiply by 2 

\[ \text{Proof } (2y \leq \Delta y) = \begin{cases} \frac{1}{4} & x \leq \frac{1}{4} \\ 2x^2 - 2x + \frac{1}{2} & \frac{1}{4} \leq x \leq \frac{1}{4} \end{cases} \]

Now, if the function didn't fit to the
proof (2y ≤ Δy) = ∫(2(1/4)) dx
= ∫(2(1/4) dx + ∫(2(4x^2 - 2x + 1/2)) dx
= 2/4(1/4) + 8x^(3/2) - 4x^(2/2) + 1/2

---

\[
\begin{aligned}
&= \frac{3}{16} + \frac{8}{3} \left[ \frac{1}{2} - \left( \frac{1}{4} \right)^3 \right] - 2 \left[ \left( \frac{1}{2} \right)^2 - \left( \frac{1}{4} \right)^2 \right] + \left[ \frac{1}{2} - \frac{1}{4} \right] \\
&= \frac{1}{8} + \frac{8}{3} \left( \frac{1}{8} - \frac{1}{64} \right) - 2 \left( \frac{1}{4} - \frac{1}{16} \right) + \frac{1}{4} \\
&= \frac{1}{8} + \frac{1}{3} - \frac{1}{24} - \frac{1}{2} + \frac{1}{8} + \frac{1}{4} \\
&= \frac{3}{24} + \frac{8}{24} - \frac{1}{24} - \frac{15}{24} + \frac{3}{24} + \frac{6}{24}
\end{aligned}
\]

\[
\begin{array}{c|c}
\frac{8}{3} & \frac{1}{12} \\
\frac{3}{20} & \frac{13}{13} \\
\end{array}
\quad \begin{array}{c|c}
\frac{20}{-13} & \frac{7}{1} \\
\end{array}
\quad = \quad \frac{17}{29}
\]

\[
\text{so that } \text{Post } P \text{ will win } \text{ in } \frac{17}{29}
\]

\[
\begin{align*}
\Rightarrow \text{Exp. for } P_1 \text{ is } \frac{17}{24}(+1) + \frac{1}{24}(-1) \\
&= \frac{10}{24} = \sqrt{\frac{5}{12}} \quad \text{value for } P_1 \\
\text{(under payoff +1 for winner)} \\
&\quad -1 \text{ for loser.}
\end{align*}
\]

---

More generally, \(P_1\) from \(O\) to \(a\) (4)
\(P_2\) from \(O\) to \(b\) (5) \(b > a\)

---

Area Z
cac1
A(z) = \(\frac{a^2}{2}\) (x^2)
A(z) = x^2 + (a-x)^2 (x > \(\frac{a}{2}\))
to that in this case
total area = ab 

Proof (guaranteeing, given x) 

\[
A(z) = \frac{\left(\frac{a^2}{2}\right)}{ab} \quad \text{for } x < \frac{a}{2} \\
x^2 + (a-x)^2 \quad \text{for } x > \frac{a}{2}
\]

\[
\frac{x^2 + a^2 - 2ax + x^2}{ab} = \frac{2x^2 - 2ax + a^2}{ab}
\]

\[
= \begin{cases} \frac{a}{2b} & x < \frac{a}{2} \\ \frac{2x^2 - 2ax + a^2}{ab} & x > \frac{a}{2} \end{cases}
\]

Now, probability on \(A\) is \(\frac{P(x)}{a} = \frac{1}{a}\) over \([0, a]\) 

\[
\text{So (second proof given by)} = \int_{0}^{a} P(z) P(z) dz \\
= \frac{1}{a} \left[ \int_{0}^{\frac{a}{2}} \frac{a}{2b} dx + \int_{\frac{a}{2}}^{a} \frac{2x^2 - 2ax + a^2}{ab} dx \right] \\
= \frac{1}{a} \left[ \frac{a}{2b} \left( \frac{a}{2} \right) + \frac{2}{ab} \frac{x^3}{3} \right]_{a/2}^{a} - \frac{2a}{ab} \frac{x^2}{2} \right]_{a/2}^{a} + \frac{a}{ab} x \right]_{a/2}^{a}
\]

---

\[
\begin{align*}
&= \frac{1}{a} \left[ \frac{a^2}{4b} + \frac{2}{3ab} \left[ \frac{3}{a} - \left( \frac{a}{2} \right)^3 \right] \right] \frac{1}{a^3 - \frac{a^2}{8}} \left[ \frac{1}{b} \left[ a^2 - \left( \frac{a}{2} \right)^2 \right] + \frac{a}{b} \left[ a - \frac{a}{2} \right] \right] \frac{1}{a^3 - \frac{a^3}{8}} \left[ \frac{1}{b} \left[ a^2 \right] \right] \frac{1}{a^3 - \frac{a^4}{8}} \left[ \frac{1}{b} \left[ a^2 + \frac{a^2}{8} \right] \right] \frac{1}{a^3 - \frac{a^{4}}{8}} \left[ \frac{1}{b} \left[ a^2 \frac{1}{8} \right] \right] \frac{1}{a^3 - \left( \frac{a}{2} \right)^3} \frac{1}{a^3 - \frac{a^2}{8}} \left( \frac{1}{b} \left[ a^2 \right] \right) \frac{1}{a^3 - \frac{a^2}{8}} \left(\frac{1}{b} \left[ a^2 \right] \right) \left( \frac{1}{b} \left[ a^2 \right] - \frac{a^2}{8} \right) \frac{1}{a^3 - \frac{a^2}{8}}
\end{align*}
\]

\[
\begin{align*}
&= \frac{1}{4} \left( \frac{a}{b} \right) + \frac{2}{3} \left( \frac{7}{8} \right) \left( \frac{a}{b} \right) - \frac{3}{4} \left( \frac{a}{b} \right) + \frac{1}{2} \left( \frac{a}{b} \right) \\
&= \left( \frac{1}{4} + \frac{7}{12} - \frac{3}{4} + \frac{1}{2} \right) \left( \frac{a}{b} \right) \\
&= \left( \frac{\frac{3}{12} + \frac{9}{12} - \frac{9}{12} + \frac{6}{12}}{12} \right) \\
&= \frac{16 - 9}{12} = \left( \frac{7}{12} \right) \left( \frac{a}{b} \right)
\end{align*}
\]

So Final result is that Proof that Player
2 will come closer than \(P_1\) is \(\frac{7}{12} \left( \frac{a}{b} \right)\) when
\(a < b\)
(attached for sufficiently greater than a!).
(namely \(b \geq 2a\) victory, or another value
comprising play!).
In this case Value \(v \in \Delta T\)

---

Payoff #2, Let Payoff be \(\Delta_3 - \Delta_4\) in \(F_1\) (maybe better \(\frac{1}{2} - \frac{1}{2}\) 

Joint Point
\(E_3, g = P(3, y) = \frac{1}{ab} \int_0^a \int_0^b dy dx\) 

If Payoff is \(H(3, 2y)\) \(\Delta_3 = |3 - 2|\) \(\Delta_4 = |y - x|\) 

thus, \(\text{cond. Exp}_x = \text{Exp}_x = \int H(3, 2y) P(3, y) dy dx\) 

i.e. \(\text{Exp}_x = \frac{1}{ab} \int_{\text{cond. Exp}_x}^a \int_{\text{cond. Exp}_x}^b dy dx\) 

and \(\text{Exp} = \frac{1}{a} \int_a^a \text{Exp}_x dx\)

---

as that 

\[E_{HP} = \frac{1}{a} \int_{0}^{a} \left[ \frac{1}{ab} \int_{\text{area}} H(z, y-x) \, dy \, dx \right] \, dx\]

\[= \frac{1}{a^2b} \int_{0}^{a} \int_{0}^{a} \int_{0}^{b} H(z-x, y-x) \, dx \, dy \, dz\]

So Parallele H's
\(H_4 = |z-x| - |y-x|\) (to \(P_1\) (y))
won't give by function 

Note, if His Separable, i.e. \(H = H'(z_3) + H''(z_3)\) 

\[Then \mathbb{E}_{HP} = \frac{1}{a^2b} \int_{0}^{a} \int_{\text{area}} H'(z_3) \, dy \, dz + H''(z_3) \, dx \, dy \int_{0}^{a} \int_{\text{area}} H'(z_3)\, dx \, dy + \frac{1}{a^2b} \int_{0}^{a} \int_0^b H'(z_3) \, dx \, dy \, dz\]

\[= \frac{1}{a^2b} \int_{0}^{\infty} \int_{0}^{\infty} H'(z_3) \, dx \, dy + \frac{1}{a^2b} \int_{0}^{\infty} \int_0^b H'(z_3) \, dx \, dy + \frac{1}{a^2} \int_{0}^{a} \int_0^b H'(z_3)\, dx \, dy\]

---

Which is something we want 

So consider \(\frac{1}{ab} \int_{0}^{a} \int_{0}^{b} H(x, y) dx dy\) 

case 1 

\[
\begin{align*}
H' &= |x-3| \\
\text{then} \int_{0}^{a} \int_{0}^{b} |x-3| dx dy \\
&= \int_{0}^{a} \left[ \int_{0}^{x} (x-3) dy + \int_{x}^{b} (3-x) dy \right] dx \\
&= \frac{x \int_{0}^{x} (x-3) dy - \int_{0}^{x} (3-x) dy}{11} \\
&= \frac{x^2 - \frac{3}{2} x^2}{11} \bigg|_{0}^{11} \\
&= \frac{x^2 - \frac{3}{2} x^3}{11} - x \left[ b-x \right] \\
&= \frac{x^2}{2} - \frac{bx^2}{2} - \frac{bx^2}{2} + x^2 \\
&= \int_{0}^{a} (x^2 - bx + \frac{b^2}{2}) dx \\
&= \frac{a^3}{3} - \frac{ba^2}{2} + \frac{b^2 a}{2} \left[ \frac{1}{11} - \frac{1}{11} \right] \\
&= \frac{a^3}{3} - \frac{ba^2}{2}
\end{align*}
\]

Assume \(ab\) always

---

\[ \text{for } H(y, z) = \frac{1}{|3-x|} \quad \text{ie} = \begin{cases} \frac{1}{3-x} & z > x \\ \frac{1}{x-3} & x > z \end{cases} \]

\[ \text{Exp}(H') = \frac{1}{ab} \int_{0}^{a} \int_{0}^{b} \frac{1}{|3-x|} \, dx \, dy = \frac{1}{ab} \int_{0}^{a} \left[ \int_{0}^{b} \frac{1}{|3-x|} \, dy \right] dx \]

\[ = \frac{1}{ab} \int_{0}^{a} \left[ \frac{x}{x-3} \, dx + \frac{b}{x} \, dx \right] \]

\[ \frac{d}{dy} \ln(x-3) = \left( \frac{1}{x-3} \right) (-1) \]

\[ \frac{d}{dy} (\ln(3-x)) = \left( \frac{1}{3-x} \right) \]

\[ \begin{aligned} \int_{0}^{x} \frac{1}{x-3} \, dy &= -\ln(x-3) \Big|_{0}^{x} \\ &= -\ln(x-x) + \ln(x) \\ &= \frac{1}{x} \end{aligned} \]

\[ \int_{x}^{b} \frac{1}{3-x} \, dy = \ln(3-x) \Big|_{x}^{b} = \ln(b-x) - \ln(0) \]

\[ \text{Exp}(H') = \frac{1}{ab} b \int_{0}^{a} \ln(x) + \ln(b-x) - 2\ln(0) \, dx \]

---

\[H'(x, y) = \frac{1}{(3-x)^2}\]

\[\Rightarrow \exp(H') = \frac{1}{ab} \int_{0}^{a} \int_{0}^{b} \frac{1}{(3-x)^2} dx dy\]

\[\text{now} \quad \int_{0}^{b} \frac{1}{(3-x)^2} d\zeta = \frac{1}{ab} \quad \frac{d}{d\zeta} \frac{1}{(3-x)} = -\frac{1}{(3-x)^2}\]

\[= -\frac{1}{2-x} \bigg|_{0}^{b} \quad \frac{d}{d\zeta} (2-x)^{-2} = -1(2-x)^{-2}\]

\[= -\frac{1}{b-x} + \frac{1}{0-x} \quad \frac{d}{d\zeta} -(2-a)^{-1} = +1(2-a)^{-2}\]

\[= -\frac{1}{b-x} - \frac{1}{x}\]

\[\text{value} \quad \int_{a}^{b} \frac{1}{3^2} d\zeta = \frac{d}{d\zeta} \left( \frac{1}{3} \right) = \frac{1}{3^2} \quad \frac{d}{d\zeta} \left( \frac{1}{3} \frac{1}{3} \right) = \frac{1}{3^2}\]

\[a=-1 \quad b=+1 \quad \frac{1}{-1} - \frac{1}{1} = (-2) \quad \Rightarrow \frac{1}{a} \times \frac{1}{b} \quad \text{then again}\]

---

\[ \int_a^0 \frac{1}{z^2} = -\frac{1}{3} \bigg|_a^0 \rightarrow \text{Out zero} \]

→ Out zero
No wonder I couldn't
put in cutoffs
later, when contrasting
difference moves in. 

\[ (\frac{1}{3})^2 \text{ in region } |z-1|<1 \]

i.e. \(H'(x,3) = \frac{1}{(3-x)^2}\) 

region \(3 \geq x+5\)
\(3 < x-5\)
\(= \frac{1}{(3)^2}\) in between 

\[ \text{then} \int_0^b H'(x,3) dx = \int_0^{x-5} \frac{1}{(3-x)^2} dx + \int_{x+5}^b \frac{1}{(3-x)^2} dx \]

\[ \text{so that} \quad = -\frac{1}{3-x} \bigg|_{0}^{x-5} - \frac{1}{3-x} \bigg|_{x+5}^{b} + \frac{25}{(3-1)^2} \]

\[ = -\frac{1}{x-5-x} + \frac{1}{x} - \frac{1}{b-x} + \frac{1}{x+5-x} + \frac{25}{(3-2)^2} \]

---

**Theorem**

\[
\begin{align*}
\int_{0}^{b} H'(x, y) dy &= \frac{2}{5} - \frac{1}{x} - \frac{1}{b x} + \frac{25}{(x^2)^2} \quad \text{for } 0 \leq x \leq b \\
&= \frac{5}{2} \\
\text{in case } x < 0 + \frac{5}{2}
\end{align*}
\]

we have no control from first term 

\[
\begin{align*}
\text{not that only } \int_{0}^{x+\frac{5}{2}} \frac{1}{(x^2)^2} dx + \int_{\frac{5}{2}}^{b} \frac{1}{x(x^2)^2} \\
&= \frac{x+\frac{5}{2}}{x^2} + \frac{1}{\frac{5}{2}} - \frac{1}{b-x} \quad \text{for } 0 \leq x \leq \frac{5}{2} \\
&\quad \text{and finally above in case } x > b - \frac{5}{2} \quad \text{no control from last term}
\end{align*}
\]

\[
\begin{align*}
\text{and finally above in case } x > b - \frac{5}{2} \qquad \text{no control from last term}
\end{align*}
\]

\[
\begin{align*}
\text{and finally } \int_{0}^{b} H'(x, y) dy &= \frac{2}{5}- \frac{1}{x} - \frac{1}{b x} + \frac {25}{(x^2)^2} \quad \text{for } 0 \leq \frac{5}{2} \\
&= \frac{5}{2} \\
\text{in case } x < 0+ \frac{5}{2}
\end{align*}
\]

\[
\begin{align*}
\text{and finally in case } x > b - \frac{5}{2} \qquad \text{and no control from last term}
\end{align*}
\]

---

\[ \int_{0}^{b} H(x, y) \, dy \]

\[ = \begin{cases} \frac{4}{5} - \frac{1}{x} - \frac{1}{b-x} & 0 \leq x \leq b \\ \frac{x+5}{5^2} + \frac{1}{5} - \frac{1}{b-x} & 0 \leq x \leq \frac{5}{5} \end{cases} \]

---

lower 

\[H(x, y) = \begin{cases} \frac{1}{(2-x)^2} & \text{and } 3 \leq x + \frac{y}{2} \\ \frac{1}{5^2} & \text{for } x - 5 \leq 3 \leq x + 5 \end{cases}\]

\[\tan \int_{0}^{b} 4(g, 3) \, dg \quad (\text{canc}) \quad 0 + 5 \leq x \leq b - 5\]

\[= \int_{0}^{x-5} \frac{1}{(3-x)^2} \, dy + \int_{x+5}^{b} \frac{1}{(3-x)^2} \, dy + \int_{x-5}^{x+5} \frac{1}{5^2} \, dy\]

\[= \left[ \frac{1}{3-x} \right]_{0}^{x-5} + \left[ \frac{1}{3-x} \right]_{x+5}^{b} + \frac{2}{5^2}\]

\[= \left[ \frac{1}{x-5} \right]_{x-5}^{x+1} + \left[ \frac{1}{x-5} \right]_{x+5}^{x} + \frac{2}{5^2}\]

\[= \left[ \frac{1}{5} \right]_{x-5}^{x} + \left[ \frac{1}{5} \right]_{x+5}^{x} + \frac{2}{5}\]

---

Now, since \(0 > x - \xi \Rightarrow x < \xi\)
first integral diverges, hence 

\[ \int_{0}^{x+\xi} \frac{1}{\xi^2} d\xi + \int_{\xi+\xi}^{b} \frac{1}{(3-x)^2} d\xi \]

\[ \frac{x+\xi}{\xi^2} + \frac{1}{\xi} - \frac{1}{b-x} \quad \text{for } 0 < x < \xi \]

and since \(x + \xi > b \Rightarrow x > b - \xi\)
second term out and hence 

\[ \int_{0}^{x-\xi} \frac{1}{\xi^2} d\xi + \int_{\xi-\xi}^{b} \frac{1}{\xi^2} d\xi \]

\[ = \frac{1}{\xi} - \frac{1}{x} + \frac{b-x+\xi}{\xi^2}. \quad \text{for } x > b \neq \xi \]

---

No finite summarize 

\[F(x) = \int_{0}^{b} H(x, y) dy = \begin{cases} \int_{0}^{1} \frac{x + \frac{1}{5}}{5^2} + \frac{1}{5} - \frac{1}{b - x} \text{ on } 0 \leq x \leq \frac{1}{5} \\ \int_{0}^{2} \frac{\frac{4}{5} - \frac{1}{x}}{x} - \frac{1}{b - x} \text{ on } \frac{1}{5} < x \leq b - \frac{1}{5} \\ \int_{0}^{3} \frac{\frac{1}{5} - \frac{1}{x}}{x} + \frac{b - x + \frac{1}{5}}{5^2} \text{ on } b - \frac{1}{5} < x \leq \frac{1}{2a} \end{cases}\]

each \(x \in S\) then (i) \(x = \frac{2S}{5^2} + \frac{1}{5} - \frac{1}{b-5} = \frac{3}{5} - \frac{1}{b-5}\) 

while (2) \(x = \frac{4}{5} - \frac{1}{5} - \frac{1}{b-5} = \left(\frac{3}{5} - \frac{1}{b-5}\right) \frac{1}{2}\) 

if \(x = b - S\) 

\[2 \text{ in } \frac{4}{5} - \frac{1}{b-5} - \frac{1}{b-5} = \frac{3}{5}-\frac{1}{b-5}\]

\[and 3 \text{ in } \frac{1}{5} - \frac{1}{b-5} + \frac{b-5}{5^2} = \frac{b-5}{5^2} + \frac{b-5}{5^2}\]

\[= \frac{1}{5} - \frac{1}{b-5} + \left(\frac{2}{5}\right) = \frac{3}{5} - \frac{1}{b-5} \quad \text{or} \quad \frac{1}{5}\]

**OK.**

\[we know \int_{0}^{a} \int_{b}^{b} f(x, y) dy dx = \int_{0}^{a} f(x) dx\]

---

\[
i c \int_{0}^{\xi} F^{4} dx + \int_{\xi}^{b-\xi} F^{2} dx + \int_{b-\xi}^{b} F^{3} dx
\]

(we assume \(a > \xi\) limits on second term)
and \(a\) if \(a < b - \xi\) 

\[
\begin{align*}
\infty \int_0^\xi F'(x) dx &= \int_0^\xi \frac{x^2}{5^2} dx + \int_0^\xi \frac{1}{5} dx + \int_0^\xi \frac{1}{5} dx - \int_0^\xi \frac{1}{b-x} dx \\
&= \frac{1}{5^2} \frac{\xi^2}{2} + \frac{\xi}{5} + \frac{\xi}{5} \left( \frac{d}{dx} - \ln(b-x) \right) \\
&= -\frac{1}{b-x} - 1 \\
\text{ic} \int_{\xi}^{b} \frac{1}{b-x} dx &= -\ln(b-x) \bigg|_{\xi}^{b} \\
&= -\ln(b-\xi) \bigg|_{\xi}^{b} \\
&= -\ln(b-d) + \ln(b-c) = \ln\left(\frac{b-c}{b-d}\right)
\end{align*}
\]

\[
\lim_{b \to \infty} \int_0^\xi F'(x) dx = \frac{1}{2} + 2 + \ln\left(\frac{b-\xi}{b}\right).
\]

---

\[
\begin{array}{c}
\Rightarrow a^k \\
\underset{\xi}{\underbrace{\int_{a}^{a} F dx}} = \underset{\xi}{\underbrace{\int_{a}^{a} \frac{4}{5} dx}} - \underset{\xi}{\underbrace{\int_{a}^{a} \frac{1}{x} dx}} - \underset{\xi}{\underbrace{\int_{a}^{a} -\frac{1}{6-x} dx}}} \\
= \underset{\xi}{\underbrace{\frac{4}{5} (a-\xi)}} - \underset{\xi}{\underbrace{\ln\left(\frac{a}{\xi}\right)}} - \underset{\xi}{\underbrace{\ln\left(\frac{b-\xi}{b-a}\right)}} \\
= \underset{\xi}{\underbrace{\frac{4}{5} (a - \xi)}} - \underset{\xi}{\underbrace{\ln\left(\frac{a(b-\xi)}{\xi(b-a)}\right)}}
\end{array}
\]

for the case \(a < b - \xi\) 

\[
\exp H^a = \frac{5}{2} + \ln\left(\frac{b-\xi}{b}\right) + \frac{4}{5}(a-\xi) - \ln\left[\frac{a(b-\xi)}{\xi(b-a)}\right]
\]

while for the other case
\[
\exp H^a = \int_0^a \int_0^{a-1} \frac{dx}{y^a} = \int_0^a \frac{dx}{y^a} \quad (\text{except when } y \text{ is } \text{even})
\]
we simply let \(b = a\) in above expression
(chosen just
we do
otherwise)

---

\[
\begin{array}{l} \text{for } a > b - \xi \\ \text{need } \int_{\xi}^{b-\xi} F_2 dx + \int_{\xi}^{a} \frac{1}{\xi - \xi} - \frac{1}{x} + \frac{b-x+\xi}{\xi^2} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \int_{\xi}^{a} dx \end{array}
\]

\[
\text{but } \int_{\xi}^{b-\xi} F_2 dx \text{ goes from } \int_{\xi}^{a} \text{ by replacing } a \text{ by } b-\xi
\]

\[
\begin{align*}
\Rightarrow \int_{\xi}^{b-\xi} F_2 dx &= \frac{4}{\xi} \left( b - \xi - \xi \right) - \ln \left[ \frac{(b-\xi)(b-\xi)}{\xi(b-b+\xi)} \right] \\
&= \frac{4}{\xi} (b-2\xi) - \ln \left[ \frac{(b-\xi)^2}{\xi^2} \right]
\end{align*}
\]

\[
\text{while } \int_{b-\xi}^{a} F_2 = \int_{b-\xi}^{a} \frac{1}{\xi} dx - \int_{b-\xi}^{a} \frac{1}{x} + \int_{b-\xi}^{b-x+\xi} \frac{b-x+\xi}{\xi^2} \\
= \frac{1}{\xi} \left[ a-b+\xi \right] - \ln \left( \frac{a}{b-\xi} \right) + \frac{b}{\xi^2} \left[ a-b+\xi \right] + \frac{1}{\xi} \left[ a-b+\xi \right] \\
= \frac{1}{\xi^2} \left[ a^2 - (b-\xi)^2 \right]
\]

\[
\begin{align*}
& \text{for } a > b - \xi \\
& \text{need } \int_{\xi}^{b-\xi} F_2 dx + \\
& \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \int_{\xi}^{a} dx \\
& \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \text{with } a > b - \xi \\
& \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \int_{\frac{a}{b-\xi}}^{b-\xi} F_2 dx \\
& \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad a > b - \xi \\
& \qquad \qquad \qquad \qquad \qquad \quad \text{but } \int_{\xi}^{b-\xi} F_2 dx \text{ is a function of } a \\
& \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text{by replacing } a \text{ by } b-\xi \\
& \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad a \text{ by } b-\xi \\
& \qquad \qquad \qquad \qquad a \text{ by } b-\xi \\
& a \text{ by } b-\xi \\
& a \text{ by } b-\text{xi} \\
& a \text{ by } b-\text{xi} \\
& a \text { by } b-\text{xi} \\
& a \text{ by } b-\text{x} \\
& a \text{ by } b-\text{x} \\
& a \text { by } b-\text{x} \\
& a \text { by } b-\text{x}
\end{align*}
\]

---

\[
\begin{align*}
\text{so ExpH'} &= \frac{5}{2} + \ln\left(\frac{b-5}{b}\right) + \left(\frac{2}{5} + \frac{b}{5^2}\right)\left(\frac{a-b+5}{a}\right) \\
&\qquad - \frac{1}{25^2}\left[a^2(b-5)^2\right] - \ln\left(\frac{a}{b-5}\right)
\end{align*}
\]

for \(b > a > b - 5\) 

in perturbation \(a = b\) 

\[
\begin{align*}
\text{weight} \\
\text{EXP H''} &= \frac{5}{2} + \ln\left(\frac{a-5}{a}\right) + \left(\frac{2}{5} + \frac{5a}{5^2}\right)\left(\frac{5}{5}\right) \\
&\qquad - \frac{1}{25^2}\left[a^3 - (a-5)^2\right] - \ln\left(\frac{a}{a-5}\right) \\
&\equiv \frac{5}{2} + \ln\left[\frac{(a-5)(a-5)}{a}\right] + 2 + \frac{a}{1} + \frac{1}{2} - \frac{a}{5} \\
&\equiv a^2 - [a^2 - 2a + 5] \\
&\equiv (2a - 5^2) \left(\frac{1}{25^2}\right) = \frac{2a6}{25^2} + \frac{8^2}{25^2} = \frac{1}{2} - \frac{a}{5} \\
&\equiv 5 + \ln\left[\frac{(a-5)(a-5)}{a^2}\right]
\end{align*}
\]

---

\[
\begin{align*}
\exp H' &= \frac{\xi}{2} + \frac{4}{\xi}(a-\xi) + \ln\left(\frac{b-\xi}{b}\right) \frac{\xi(b-a)}{a(b-\xi)} \\
&= \frac{5}{2} + \frac{4a}{\xi} - 4 + \ln\left[\frac{\xi(b-a)}{ab}\right] \\
&= \frac{4a}{\xi} - \frac{3}{2} + \ln\left(\frac{\xi(b-a)}{ab}\right)
\end{align*}
\]

\[
\exp H'' = 5 + \ln(

---

tuyan, in core \(a = b\) 

need simply \(H'(\text{ext})\) replaced by
\(a = a - \frac{5}{3}\) brute
by a 

\[ \text{end add } \int_{a-5}^{a} F^3 dx \]

\[ \int_{a-5}^{a} \frac{1}{5} - \frac{1}{x} + \frac{a-x+5}{5^2} dx \]

\[ = \frac{1}{5} [5] - \ln\left(\frac{a}{a-5}\right) + \frac{a}{5^2} [5] + \frac{1}{5} [5] - \frac{1}{25} \int_{11}^{12} a^2 - (a-5)^2 \]

\[ = (1 + \ln\left(\frac{a}{a-5}\right) + \frac{a}{5} + 1 + \frac{a}{5} + \frac{1}{2}) = \frac{a^2 - 2a + 5}{25^2} \]

\[ \frac{11}{5} - \ln\left(\frac{a}{a-5}\right) = \frac{-\frac{a}{5} + \frac{1}{2}}{25^2} \]

to solve we add \(H'\) with \(a \to a-5\) \(b \to a\). 

\[ \Rightarrow \frac{5}{2} + \ln\left(\frac{a-5}{a}\right) + \frac{4}{5} \left(a-5-5\right) - \ln\left(\frac{a-5}{5}\right) \left(a-5-5\right) \]

---

of course always the difference 

\[H'' = \frac{10}{2} - \ln\left(\frac{a}{\xi}\right) + \ln\left(\frac{a-\xi}{a}\right) + \frac{4}{\xi}\left(a-2\xi\right) - \ln\left(\frac{(a-\xi)^2}{\xi^2}\right)\]

\[= \frac{10}{2} + \frac{4a}{\xi} = 8 + \ln\left[\frac{(a-\xi)(a-\xi)}{a(a-\xi)^2}\right] \xi^2\]

\[and \quad \text{Exp}(H' + H'') = \left(\frac{5}{2}\right) + \ln\left(\frac{b-\xi}{b}\right) + \frac{4}{\xi}\left(a-\xi\right) - \ln\left(\frac{a(b-\xi)}{\xi(b-a)}\right) + \left(\frac{6}{2}\right) - \frac{4a}{\xi} - \ln\left(\frac{\xi^2}{a^2}\right)\]

\[= \frac{11}{2} - 4 + \ln\left(\frac{b-\xi}{b}\right) \frac{a^2}{\xi^2} \frac{\xi(b-a)}{a(b-\xi)}\]

---

\[= \frac{3}{2} + \ln\left(\frac{a}{b} \cdot \frac{b-a}{\frac{5}{3}}\right)\]

probably mistake somewhere. (misleading)

chuck losted 

Promising 

would be easier to get by simply omitting
terrigen in hidden cutoffs. 

(hoping this no large part of exp income from
this region.) 

Another possibility is 

forbiddent doubt they both agree,
winnow is one single other wrong.
(other independent ways metrics.) 

in contrast this would be requirements of
being within certain distance of correct answer. 

or yet another Single Player
possibility is payoff to propose internal specified
and On one option within and in that internal.

---

suppose \(P(x)\) indicates 

\(P(x) = 0\) 

Play to show a set then gets Poyol count measure of set in case of configurations, O otherwile
if Poyol measure is \(P(x)\)
natural is \(M(x)\) 

\[EXP = \frac{P(x)}{M(x)}\]

a sample choice 

\(X\) to maintain this state 

looks like Poyol's Poyol 

supply choice 

arbitrary small number of mode for cont distr. 

- many small number of modes 

- many mode of modes in a system 

- a number of modes in a system 

- many modes in a system 

- many small number of modes 

- many modes in a system 

- many small number of modes 

- many modes in a system