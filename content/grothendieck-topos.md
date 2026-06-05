---
title: Grothendieckトポス
weight: 7
section: 6
toc: true
---

## Grothendieck位相

本章では位相空間上 $X$ 上の層の圏論的な抽象化について説明する。
その為にはまず、位相空間の開集合系 $\mathcal{O}\_X$ の性質の圏論的な抽象化を行う。

基本的な考え方は $X$ の開集合の関係 $V\subseteq U$ を、圏 $\mathcal{C}$ の射 $f: a\rightarrow b$ として抽象化するという事である。
ただし、それだけで $\mathcal{C}$ を位相構造のようなものとしては見なせないので、$\mathcal{C}$ と **被覆(covering)** というものの組を考える必要がある。

### 篩(ふるい)

最初に、位相空間 $U$ の開被覆の抽象化を行う。まず、 $U$ に含まれる適当な開集合の集合 $\\{U\_{\lambda}\subseteq U\\}\_{\lambda\in\Lambda}$ を抽象化した概念としてpresieveが定義される。

{{% definition title="presieve" %}}
圏 $\mathcal{C}$ と対象 $c\in\mathcal{C}$ に対して、 $c$ をコドメインとする射の族
を $c$ 上の **presieve** と呼ぶ。
{{% /definition %}}

presieveに対応する日本語直訳は"前篩(ぜんふるい)"であろうが、そのような用語を使っている文献を一つも見つけられなかったので、
ここでは英語表記のままにした。

続いて、$U$ に含まれる開集合の集合 $S=\\{U\_{\lambda}\subseteq U\\}$ のうち、より小さい開集合をとる操作について閉じているもの、すなわち
$$ V\in S, W\subseteq V \Rightarrow W\in S$$
を満たすものを抽象化した概念として、篩(ふるい,sieve)が定義される。

{{% definition title="篩(ふるい)" %}}
圏 $\mathcal{C}$ の対象 $c$ 上のpresieve $S$ が、前合成について閉じているとき、すなわち $f\circ g$ が定義される任意の $g$ に対して
$$ f\in S \Rightarrow f\circ g\in S$$
が成り立つ時、これを $c$ 上の **篩(ふるい,sieve)** という。
{{% /definition %}}

{{< refer def.sieve >}} でも述べたように、 $c$ 上の篩全体は $\mathcal{Y}(c)=\mathcal{C}(-, c)$ の部分対象全体と半順序集合として同型である。
状況によって、定義を使い分ける事がある。
$c$ 上の篩全体は最大値を持ち、それを $M\_c$ と書く。 既に述べたように $c$ 上の篩 $S$ が最大であることと、 $1\_c\in S$ であることは同値である。

{{% definition %}}
presieve $P$ に対して、 $P\subseteq S$ となる最小の篩 $S$ を **Pによって生成される篩** という。
{{% /definition %}}

$M\_c$ が存在するので、任意のpresieveに対してそれが生成する篩が存在する。

{{% proposition %}}
$c$ 上の篩 $S$ と、射 $f: d\rightarrow c$ に対して
$$ f^{\ast}(S) = \\{ g \mid \mathrm{cod}(g) = d, f\circ g \in S\\}$$
は $d$ 上の篩である。
{{% /proposition %}}
{{% details 証明 %}}
任意の $g\in f^{\ast}(S)$ と $g\circ h$ が定義される $h$ について
$f\circ (g\circ h) = (f\circ g)\circ h$
である。この時 $f^{\ast}(S)$の定義より $f\circ g\in S$ であるので $S$ が篩である事より
$f\circ (g\circ h)\in S$
である。よって $g\circ h\in f^{\ast}(S)$ であるので $f^{\ast}(S)$ も篩である。 $\square$
{{% /details %}}

これは、$U$ 上の篩を $V\subseteq U$ に制限することで $V$ 上の篩を作るという操作の抽象化である。
ここで $f^{\ast}$ という引き戻しと同じ表記を用いているのは、実際にこれが以下のような引き戻しであるからである。
もしくは $S$ の $(f\circ -): M\_d\rightarrow M\_c$ による逆像が $f^{\ast}(S)$ であると言っても良い。

$$\xymatrix{
f^{\ast}(S) \ar[r] \ar@{^{(}->}[d] & S \ar@{^{(}->}[d] \\\\
M\_d \ar[r]^{f\circ -} & M\_c
}$$

篩を部分関手とみなす場合には、以下のような引き戻しの図式となる。

$$\xymatrix{
f^{\ast}(S) \ar[r] \ar@{^{(}->}[d] & S \ar@{^{(}->}[d] \\\\
\mathcal{Y}(d) \ar[r]^{\mathcal{Y}(f)} & \mathcal{Y}(c)
}$$

{{% proposition %}}
$c$ 上の篩 $R,S$ と射 $f: d\rightarrow c$ に対して
$$ f^{\ast}(R\cap S) = f^{\ast}(R)\cap f^{\ast}(S)$$
{{% /proposition %}}
これは逆像の性質より明らか。

### Grothendieck位相の定義

{{% definition title="Grothendieck位相" %}}
圏$\mathcal{C}$ 上の **Grothendieck位相(Grothendieck topology)** とは、$\mathcal{C}$ の各対象 $c$ に、篩の族 $J(c)$ を対応させる写像 $J$ であって、
以下の公理を満たすものである。

- **最大性公理(maximality axiom)**:  $M\_c \in J(c)$
- **安定性公理(stability axiom)**: $S\in J(c)$ であるならば、任意の $f:d\rightarrow c$ に対して $f^{\ast}(S)\in J(d)$。
- **推移性公理(transitivity axiom)**: $S\in J(c)$ であり、$c$ 上の篩 $R$ が任意の $(f:d\rightarrow c)\in S$ に対して $f^{\ast}(R)\in J(d)$ を満たすならば、$R\in J(c)$ である。

$J(c)$ の元を $c$ の **$J$被覆($J$-covering)** もしくは単に **被覆(covering)** と呼ぶ。
{{% /definition %}}

これらは、位相空間の場合の以下の性質をそれぞれ抽象化したものである。

-  $U$ 自身は $U$ の開被覆である。
- (被覆の範囲を狭めても被覆): 任意の開被覆 $U=\bigcup U\_{\lambda}$ が与えられた時、これをより小さい開集合 $V\subseteq U$ に制限した $\\{V\cap U\_{\lambda}\\}$ は $V$ の開被覆である。
- (被覆の各ピースを覆っているならば、全体も覆っている): 任意の開被覆 $U=\bigcup U\_{\lambda}$ と、$U$ の部分集合の族 $R=\\{V\_{\alpha}\subseteq U\\}$ が与えられた時、任意の $U\_{\lambda}\subseteq U$ について
$\\{U\_{\lambda}\cap V\_{\alpha}\\}$ が $U\_{\lambda}$ の開被覆になっているのであれば、 $R$ は $U$ の開被覆である。

{{% definition title="景" %}}
小圏 $\mathcal{C}$ と $\mathcal{C}$ 上のGrothendieck位相 $J$ の組 $(\mathcal{C},J)$ を **景(site)** という。
{{% /definition %}}

{{% proposition %}}
$J$ をGrothendieck位相とすると
$$R,S\in J(c)\Rightarrow R\cap S\in J(c)$$
{{% /proposition %}}
{{% details 証明 %}}
$R,S$ が篩の時 $R\cap S$ も篩であるのは明らか。
$S\in J(c)$ であるので、任意の $(f:d\rightarrow c)\in S$ に対して、 $f^{\ast}(R\cap S)\in J(d)$ である事を示せば推移性公理より $R\cap S\in J(c)$ となる。

$(f:d\rightarrow c)\in S$ とする。すると $R\in J(c)$ であるので安定性公理より
$f^{\ast}(R)\in J(d)$ である。
ここで $f\in S$ であることから $f^{\ast}(S)=M\_d$ である事が簡単に分かるので、

$$f^{\ast}(R\cap S) = f^{\ast}(R)\cap f^{\ast}(S) = f^{\ast}(R)\cap M\_d = f^{\ast}(R) \in J(d)$$

である。 $\square$
{{% /details %}}

上記のGrothendieck位相の定義は $J$ が満たす抽象的な公理によって記述されていたが、
被覆の細分・合成といった操作を直感的に扱いやすくする目的で、 **合成篩(composite sieve)** を用いた定義も用いられる。

{{% definition title="合成篩を用いたGrothendieck位相の定義" %}}
圏$\mathcal{C}$ 上の **Grothendieck位相(Grothendieck topology)** とは、$\mathcal{C}$ の各対象 $c$ に、篩の族 $J(c)$ を対応させる写像 $J$ であって、
以下の公理を満たすものである。

1. $M\_c\in J(c)$
2. $c$ 上の篩 $S,T$ について $T\in J(c)$ かつ $T\subseteq S$ ならば $S\in J(c)$
3. $R\in J(c)$ ならば、任意の $f:d\rightarrow c$ について、ある $S\in J(d)$ が存在して、全ての $g\in S$ について $f\circ g\in R$
4. presieve $\\{f\_i:c\_i\rightarrow c\\}\_{i \in I}$ から生成された $S\in J(c)$ と、
   presieve $\\{g\_{ij}: d\_{ij}\rightarrow c\_i\\}\_{j\in I\_i}$ から生成された $T\_i\in J(c\_i)$ について、
   presieve $\\{f\_i\circ g\_{ij}: d\_{ij}\rightarrow c\\}\_{i\in I, j\in I\_i}$ から生成された **合成篩(composite sieve)** $R$ は $J(c)$ の元である。
   また、この合成篩を $S*\\{T\_i\\}\_{i\in I}$ と書く。
{{% /definition %}}　

{{% details 定義の同値性の証明 %}}
**($\Rightarrow$)**

$J$ が3つの公理を満たすとする。

1. 最大性公理そのものである。

2. $c$ 上の篩 $S,T$ について $T\in J(c)$ かつ $T\subseteq S$ であるとする。
任意の $(f:d\rightarrow c) \in T$ について、 $T\subseteq S$ より $f=f\circ 1\_d\in S$ であるから
$1\_d \in f^{\ast}(S)$。すなわち、最大性公理より $f^{\ast}(S)=M\_d \in J(d)$ であるので、推移性公理より $S\in J(c)$ である。

3. $R\in J(c)$ であるとする。任意の $f:d\rightarrow c$ について、安定性公理より $f^{\ast}(R)\in J(d)$ であり、$f^{\ast}(R)$ の定義より、任意の $g\in f^{\ast}(R)$ について $f\circ g\in R$ である。

4. $S\in J(c)$ をpresieve $\\{f\_i:c\_i\rightarrow c\\}\_{i \in I}$ から生成された篩、
   $T\_i\in J(c\_i)$ をpresieve $\\{g\_{ij}: d\_{ij}\rightarrow c\_i\\}\_{j\in I\_i}$ から生成された篩、
   $R$ を presieve $\\{f\_i\circ g\_{ij}: d\_{ij}\rightarrow c\\}\_{i\in I, j\in I\_i}$ から生成された篩とする。
   任意の $(f:d\rightarrow c)\in S$ に対して $f^{\ast}(R)\in J(d)$ である事を示せば、推移性公理より $R\in J(c)$ となる。

   ここで、 適当な $i\in I$ に対して $f=f\_i\circ h$ と書くことができて、引き戻しの性質より
   $$f^{\ast}(R) = (f\_i\circ h)^{\ast}(R) = h^{\ast}(f\_i^{\ast}(R))$$
   である。ここで任意の $k\in T\_i$ について、ある $j$ が存在して $k = g\_{ij}\circ u$ と書けるから、 $f\_i\circ k = (f\_i\circ g\_{ij})\circ u \in R$ である。
   従って $k\in f\_i^{\ast}(R)$ であるから $T\_i\subseteq f\_i^{\ast}(R)$ である。

   よって、 $T\_i\in J(c\_i)$ かつ $T\_i\subseteq f\_i^{\ast}(R)$ より $f\_i^{\ast}(R)\in J(c\_i)$ である。
   従って、安定性公理より $h^{\ast}(f\_i^{\ast}(R)) = f^{\ast}(R) \in J(d)$ である。

**($\Leftarrow$)**

$J$ が1.2.3.4.の条件を満たすとする。

- (最大性公理): 条件1.そのものである。
- (安定性公理): $S\in J(c)$ であるとすると、任意の$f:d\rightarrow c$ に対して条件3.よりある $R\in J(d)$ が存在して、すべての$g\in R$ に対して $f\circ g\in S$ である。すなわち $g\in f^{\ast}(S)$ であるから $R\subseteq f^{\ast}(S)$ である。よって条件2.より $f^{\ast}(S)\in J(d)$。
- (推移性公理): $c$ 上の篩 $S=\\{f\_i: c\_i\rightarrow c\\}\_{i\in I}$ について、 $S\in J(c)$ であり、 $c$ 上の篩 $R$ が任意の $f\_i \in S$ に対して $f\_{i}^{\ast}(R)\in J(c\_i)$ を満たすとする。ここで、 $T\_i = f\_{i}^{\ast}(R)$ とおき、その元を $T\_i = \\{g\_{ij}: d\_{ij}\rightarrow c\_i\\}\_{j \in I\_i}$ と書くと条件4.より合成篩 $S*\\{T\_i\\}\_{i\in I} = \\{f\_i\circ g\_{ij}: d\_{ij}\rightarrow c\\}\_{i\in I, j\in I\_i}$ は $J(c)$ の元である。ここで $g\_{ij}\in f\_{i}^{\ast}(R)$ より $f\_{i}\circ g\_{ij}\in R$ であるので、 $S*\\{T\_i\\}\_{i\in I}\subseteq R$ である。従って条件2.より $R\in J(c)$ である。

$\square$
{{% /details %}}

合成篩を用いた定義の条件2は **単調性公理** とも呼ばれる。

### Grothendieck前位相

Grothendieck位相の定義は以上で十分であるが、具体的な計算を行う際に便利な幾つかの概念を定める。

{{% definition title="Grothendieck前位相" %}}
任意の引き戻しをもつ圏 $\mathcal{C}$ 上の **Grothendieck前位相(Grothendieck pretopology)** もしくは **Grothendieck位相の基底(Basis for Grothendieck topology)** とは、$\mathcal{C}$ の各対象 $c$ に、presieveの族 $K(c)$ を対応させる写像 $K$ であって、以下の公理を満たすものである。

1. $\\{1\_c\\} \in K(c)$
2. $\\{f\_i: c\_i \rightarrow c\\}\_{i \in I}\in K(c)$ であるならば任意の $g:d\rightarrow c$ に対して、
   $\\{g^{\ast}(f\_i): c\_i\times\_c d\rightarrow d\\}\_{i \in I} \in K(d)$
3. $\\{f\_i: c\_i \rightarrow c\\}\_{i \in I}\in K(c)$ かつ、各 $i\in I$ について $\\{g\_{ij}:d\_{ij}\rightarrow c\_i\\}\_{j\in I\_i}\in K(c\_i)$ であるならば、
   $\\{f\_i\circ g\_{ij}: d\_{ij}\rightarrow c\\}\_{i \in I, j\in I\_i} \in K(c)$

引き戻しを持つとは限らない圏においては条件2を以下のように緩めて良い。

2. $\\{f\_i: c\_i \rightarrow c\\}\_{i \in I}\in K(c)$ であるならば任意の $g:d\rightarrow c$ に対して、
   presieve $\\{h\_j: d\_j\rightarrow d\\}\_{j\in J} \in K(d)$ が存在して、任意の $j\in J$ について $g\circ h\_j=f\_i\circ k$ と分解できる。

{{% /definition %}}

前段の条件2.を満たすとき、後段の条件2.を満たすのは引き戻しの図式から明らかである。

$$\xymatrix{
c\_i\times\_c d \ar[d]\_{g^{\ast}(f\_i)} \ar[r] & c\_i \ar[d]^{f\_i} \\\\
d \ar[r]^{g}                                   & c
}$$

{{% proposition title="Grothendieck前位相の生成する位相" %}}
任意のGrothendieck前位相 $K$ に対して、$J$ を
$$ R\in J(c) \Leftarrow \exists S\in K(c), S\subseteq R$$
と定めると $J$ はGrothendieck位相である。
{{% /proposition %}}
{{% details 証明 %}}
引き戻しを持つとは限らない圏 $\mathcal{C}$ について示す。 $K$ が $\mathcal{C}$ 上のGrothendieck前位相であるとし、
$J$ を $ R\in J(c) \Leftarrow \exists S\in K(c), S\subseteq R$ で定める。

**(最大性公理)**

$1\_c \in K(c)$ より成立。

**(安定性公理)**

$S\in J(c)$ であるとする。すると $T\subseteq S$ なる $T\in K(c)$ が存在する。
ここで$T=\\{f\_i:c\_i\rightarrow c\\}$ とすると、 任意の $g:d\rightarrow c$ に対して
$U=\\{h\_j: d\_j\rightarrow d\\} \in K(d)$ が存在して、任意の $j\in J$ について $g\circ h\_j = f\_i\circ k$ と分解できる。
よって $f\_i\in T\subseteq S$ より $fg\circ h\_j = f\_i\circ k \in S$ であるから $h\_j\in g^{\ast}(S)$ である。
従って $U\subseteq g^{\ast}(S)$ であり、これと $U\in K(d)$ より $g^{\ast}(S)\in J(d)$ である。

**(推移性公理)**

$S\in J(c)$ であり、 $c$ 上の篩 $R$ が任意の $(f:d\rightarrow c)\in S$ に対して $f^{\ast}(R)\in J(d)$ を満たすとする。
すなわち、 $S=\\{f\_i:c\_i\rightarrow c\\}$ とすると、
presieve $T\in K(c)\ {\rm s.t.}\ T\subseteq S$ が存在し任意の $i\in I$ に対して、presieve $U\_i\in K(c\_i)$ が存在して $U\_i\subseteq f\_i^{\ast}(R)$ であるとする。
ここで $U\_i=\\{g\_{ij}:d\_{ij}\rightarrow c\_i\\}$ とすると $V=\\{f\_i\circ g\_{ij}: d\_{ij}\rightarrow c\\} \in K(c)$ である。
ここで $g\_{ij}\in U\_i \subseteq f\_i^{\ast}(R)$ より $f\_i\circ g\_{ij} \in R$ であるから $V\subseteq R$ である。
すなわち、 $V\in K(c), V\subseteq R$ より $R\in J(c)$ である。

$\square$
{{% /details %}}

### カバレッジ

Grothendieck位相の3つの公理のうち、最も重要なものは安定性公理である。
安定性公理は開被覆を細かくしてく操作を抽象化したものであって後の章で述べる **局所性(locality)** という性質と密接に関わっている。
また、以下に述べるように安定性公理さえ成り立てば、最大性公理と推移性公理は後から追加する事が可能である。

{{% definition title="カバレッジ" %}}
圏 $\mathcal{C}$ 上の **カバレッジ(coverage)** とは各対象 $c$ に篩の集合を対応させる写像 $D$ であって、任意の射 $f:d\rightarrow c$ に対して
$$ S\in D(c) \Rightarrow f^{\ast}(S)\in D(d)$$
を満たすものである。
{{% /definition %}}

{{% theorem title="カバレッジの生成するGrothendieck位相" %}}
小圏 $\mathcal{C}$ 上のカバレッジ $D$ に対して、以下のように定められた $G\_D$ はGrothendieck位相である。

$c$ 上の篩 $S$ が $G\_D(c)$ の要素である条件を、以下が成立することと定める。

任意の $f:d\rightarrow c$ と $D$ に関して閉じている $d$ 上の篩 $T$ について、 $f^{\ast}(S)\subseteq T\Rightarrow T=M\_d$ である。

ここで $T$ が $D$ に関して閉じているとは、任意の $g:e\rightarrow d$ と $Z\in D(e)$ に対して、
$ Z \subseteq g^{\ast}(T) \Rightarrow g \in T $
が成り立つことである。
{{% /theorem %}}

複雑であるので、証明の前に概要を説明する。

まず「$T$ が $D$ に関して閉じている」条件を書き直すと
$ (g\circ -)(Z)\subseteq T \Rightarrow g \in T$
となるが、前合成 $(g\circ -)$ は $g$ をより狭い範囲に制限する操作を表すのだった。

すなわち、この条件は $g$ をカバレッジ $Z$ に含まれる射で狭い範囲に制限したものが全て $T$ に含まれるならば、
$g$ 自身も $T$ に含まれるという条件であり、細かい被覆を貼り合わせて大きな被覆が作れるということである。

すなわち、 $S$ の条件は $f^{\ast}(S)\subseteq T$ の元を貼り合わせていったら $T=M\_d$ になると言う事を言っており、
$S$ がそのような網羅性を持つ篩であるという事を要請するものである。

{{% details Grothendieck位相であることの証明 %}}
$D$ を小圏 $\mathcal{C}$ 上のカバレッジとする。

**(最大性公理)**

$f:d\rightarrow c$ と $D$ に関して閉じている $d$ 上の篩 $T$ について、
$f^{\ast}(M\_c)\subseteq T$ であるとすると、$f\circ 1\_d \in M\_c$ より $1\_d \in f^{\ast}(M\_c)\subseteq T$ である。
従って、 $T=M\_d$ となり条件を満たすので $M\_c \in G\_D(c)$ である。

**(安定性公理)**

$S\in G\_D(c), f:d\rightarrow c$ とする。

$g:e\rightarrow d$ と $D$ に関して閉じている $e$ 上の篩 $T$ について、
$g^{\ast}(f^{\ast}(S))\subseteq T$ であるとする。 すると $g^{\ast}(f^{\ast}(S)) = (f\circ g)^{\ast}(S)\subseteq T$ であるので
$S$ の満たす条件より $T=M\_e$ である。従って $f^{\ast}(S)$ も $G\_D$ の条件を満たすので $f^{\ast}(S)\in G\_D(d)$である。

**(推移性公理)**

$S\in G\_D(c)$ であり、$c$上の篩 $R$ が任意の $(f:d\rightarrow c)\in S$ に対して $f^{\ast}(R) \in G\_D(d)$を満たすとする。

ここで $g:e\rightarrow c$ と $D$ について閉じている $e$ 上の篩 $T$ について、$g^{\ast}(R)\subseteq T$ とする。$T=M\_e$ を示すことが目標である。
その為に $T$ を細分化した篩を考え、それらを貼り合わせるという方針で証明を行う。

射 $(h:x\rightarrow e) \in g^{\ast}(S)$ で $T$ を制限した $x$ 上の篩 $h^{\ast}(T)$ を考える。
任意の $(k:y\rightarrow x)$ と $Z\in D(y)$ に対して $Z\subseteq k^{\ast}(h^{\ast}(T)) = (h\circ k)^{\ast}(T)$ とすると
$T$ が $D$ について閉じていることより $h\circ k\in T$ すなわち $k\in h^{\ast}(T)$ である。従って $h^{\ast}(T)$ も $D$ について閉じている。

そして $g^{\ast}(R)\subseteq T$ であるので $h^{\ast}(g^{\ast}(R)) = (g\circ h)^{\ast}(R) \subseteq h^{\ast}(T)$ である。
ここで $h\in g^{\ast}(S)$ より $g\circ h\in S$ であるから、仮定より $(g\circ h)^{\ast}(R)\in G\_D(x)$ である。
そして、仮定より $g^{\ast}(R)\subseteq T$ であるので、両辺を $h$ で引き戻して $h^{\ast}(g^{\ast}(R))\subseteq h^{\ast}(T)$ すなわち、
$ 1\_x^{\ast}((g\circ h)^{\ast}(R)) \subseteq h^{\ast}(T) $である。以上より、 $h^{\ast}(T)$ が $D$ について閉じており、
$(g\circ h)^{\ast}(R)\in G\_D(x)$ かつ$ 1\_x^{\ast}((g\circ h)^{\ast}(R)) \subseteq h^{\ast}(T) $であるから $h^{\ast}(T) = M\_x$ である。

ここで $h^{\ast}(T)=M\_x \Leftrightarrow 1\_x \in h^{\ast}(T) \Leftrightarrow h \in T$ である。すなわち、任意の $h\in g^{\ast}(S)$ に対して $h\in T$
であるから $g^{\ast}(S)\subseteq T$ である。従って、$T$ が $D$ について閉じており、 $S\in G\_D(c)$ かつ $g^{\ast}(S)\subseteq T$ であることから $T=M\_e$ である。

$\square$
{{% /details %}}

実は $G\_D$ がGrothendieck位相である事の証明には $D$ がカバレッジである事実は不要である。
$D$ がカバレッジであるという条件は、 $G\_D$ が $D$ を含むという事実の為に必要となる。

{{% proposition %}}
$$S\in D(c) \Rightarrow S\in G\_D(c)$$
{{% /proposition %}}
{{% details 証明 %}}
$S\in D(c)$ であるとする。 $f:d\rightarrow c$ と $D$ について閉じている $d$ 上の篩 $T$ について $f^{\ast}(S)\subseteq T$ であるとする。
$D$ がカバレッジであることより $f^{\ast}(S)\in D(d)$ である。ここで $T$ は $D$ について閉じているので
$f^{\ast}(S)\in D(d)$ と $1\_d^{\ast}(f^{\ast}(S))\subseteq 1\_d^{\ast}(T)$ より $1\_d\in T$ である。従って $T=M\_d$ であるから $S\in G\_D(c)$ である。 $\square$
{{% /details %}}

{{% proposition %}}
$G\_D$ は $D$ を含むGrothendieck位相のうち最小のものである。
{{% /proposition %}}
{{% details 証明 %}}
$J$ を $D$ を含むGrothendieck位相とする。$S\in G\_D(c)$ とする。示すべきことは $S\in J(c)$ である。

ここで
$$ T=\\{f:d\rightarrow c \mid f^{\ast}(S)\in J(d)\\}$$
と置く。$1\_c\in T$ である事を示せば $1\_c^{\ast}(S)=S\in J(d)$ が示されるので、$T=M\_c$ である事を示せば良い。

**($T$ が篩である事)**

$(f:d\rightarrow c)\in T$ と任意の $g:e\rightarrow d$ について安定性公理より
$(f\circ g)^{\ast}(S) = g^{\ast}(f^{\ast}(S)) \in J(e)$ であるから $f\circ g \in T$。従って $T$ は $c$ 上の篩である。

**($T$ が $D$ について閉じている事)**

$g:e\rightarrow d$ と $Z\subseteq D(e)$ に対して $Z\subseteq g^{\ast}(T)$ であるとする。
任意の $(h:x\rightarrow e)\in Z$ に対して $h\in g^{\ast}(T)\Leftrightarrow g\circ h\in T\Leftrightarrow (g\circ h)^{\ast}(S)=h^{\ast}(g^{\ast}(S))\in J(d)$ 
である。従って推移性公理より $g^{\ast}(S) \in J(e)$ である。従って $T$ の定義より $g\in T$ である。
よって $T$ は $D$ について閉じている。

**($1\_c^{\ast}(S)\subseteq T$である事)**

$(f:d\rightarrow c)\in S$ とすると、 $S$ が篩であることより $f^{\ast}(S)=M\_d$ である。よって最大性公理より $f^{\ast}(S)\in J(d)$ であるから $f\in T$。
すなわち $S\subseteq T$ である。

以上より、$G\_D$ の性質から $T=M\_c$ である。 $\square$
{{% /details %}}

### Grothendieck位相の例

{{% definition title="自明な位相" %}}
小圏 $\mathcal{C}$ の各対象 $c$ 対して $J(c) = \\{M\_c\\}$ と定めると、 $J$ はGrothendieck位相となる。これを **自明な位相(trivial topology)** という。
{{% /definition %}}

{{% definition title="稠密位相" %}}
小圏 $\mathcal{C}$ の各対象 $c$ に対して、以下を満たす $D$ を **稠密位相(dense topology)** という。

$$ S\in D(c) \Leftrightarrow \forall f:d\rightarrow c, f^{\ast}(S)\neq\emptyset $$
{{% /definition %}}

任意の $f:d\rightarrow c$ と $g:e\rightarrow c$ について以下のような可換図式を満たす射が必ず存在するならば、その圏は **右Ore条件(right Ore condition)** を満たすという。

$$\xymatrix{
\bullet \ar[d] \ar[r] & d \ar[d]^{f} \\\\
e \ar[r]^{g} & c
}$$

{{% definition title="原子位相" %}}
右Ore条件を満たす小圏 $\mathcal{C}$ の各対象 $c$ に対して、以下を満たす $J$ を **原子位相(atomic topology)** という。
$$ S\in J(c) \Leftrightarrow S\neq\emptyset $$
{{% /definition %}}

{{% proposition %}}
右Ore条件を満たす小圏 $C$ 上の位相 $J$ が稠密位相であることと原子位相であることは同値。
{{% /proposition %}}
{{% details 証明 %}}
小圏 $\mathcal{C}$ が右Ore条件を満たすとする。$S$ を $c$ 上の篩とする。

$\forall f:d\rightarrow c, f^{\ast}(S)\neq\emptyset$ すなわち、
$\forall f:d\rightarrow c, \exists g:e\rightarrow d,\ \mathrm{s.t.}\  f\circ g\in S$
であるとする。すると $1\_c\circ g\in S$ を満たす $S$ の元が存在するから $S\neq\emptyset$ である。
逆に $S\neq\emptyset$ であるとする。すると、任意の $f:d\rightarrow c$ に対して、射 $g:e\rightarrow c\in S$
を任意に取ると、右Ore条件より $f\circ a = g\circ b$ を満たす$a,b$ が存在する。ここで $S$ は篩で $g\in S$ であるから
$g\circ b\in S$。よって $f\circ a\in S$ であるから
$\forall f:d\rightarrow c, \exists g:e\rightarrow d,\ \mathrm{s.t.}\  f\circ g\in S$
が成り立つ。 $\square$
{{% /details %}}

{{% proposition title="位相空間の開被覆から導出されるGrothendieck位相" %}}
位相空間 $X$ について、
$$ \\{U\_{\lambda}\xhookrightarrow{}U\\} \in J(U) \Leftrightarrow U=\bigcup U\_{\lambda}$$
となるように定めた $J$ は、半順序集合としての圏 $\mathcal{O}\_X$ 上のGrothendieck位相である。
{{% /proposition %}}

位相空間の開集合系は右Ore条件を満たす($U\_1\xhookrightarrow{} U, U\_2\xhookrightarrow{} U$ に対して常に $U\_1\cap U\_2$ が存在)が、原子位相ではない。
例えば $U$ の真部分集合 $V\subset U$ 一つのpresieve $\\{V\xhookrightarrow{} U\\}$ から生成される篩は $U$ 全体を覆っていないが、原子位相においては被覆として扱われる。

位相空間の開集合系から導出されるGrothendieck位相は次のように一般化できる。

{{% definition title="標準位相" %}}
**フレーム(frame)** すなわち、完備ハイティング代数 $\mathcal{H}$ に対して、
$$ \\{a\_{\lambda}\xhookrightarrow{}a\\} \in J(a) \Leftrightarrow a = \bigvee a\_{\lambda}$$
となるように定めた $J$ は $\mathcal{H}$ 上のGrothendieck位相である。これを **標準位相(canonical topology)** という。
{{% /definition %}}

### 最小の被覆篩を持つ位相

通常のGrothendieck位相 $J$ には、 各対象の被覆が無数に含まれうるが、出来るだけ少ない被覆のみから構成される位相は取り扱いが優しい。

{{% definition title="最小の被覆篩を持つGrothendieck位相" %}}
圏 $\mathcal{C}$ の射からなる集合 $\mathcal{A}$ を以下の2つの条件を満たすものとする。

- 左合成について閉じている。
- **補完的(interpolative)** である: 任意の$\mathcal{A}$ の射は、他の $\mathcal{A}$ の2つの射の合成に分解できる。

この時、以下で定義される $J\_{\mathcal{A}}$ はGrothendieck位相である。
$$ S \in J\_{\mathcal{A}}(c) \Leftrightarrow (\forall f\in\mathcal{A},\mathrm{cod}(f)=c \Rightarrow f \in S) $$

{{% /definition %}}
{{% details 証明 %}}
**(最大性公理)**

$M\_c \in J\_{\mathcal{A}}(c)$ は明らか。

**(安定性公理)**

$S \in J\_{\mathcal{A}}(c)$ と $f:d\rightarrow c$ について $f^{\ast}(S) \in J\_{\mathcal{A}}(d)$ を示す。

任意の $g\in\mathcal{A},\mathrm{cod}(g)=d$ に対して $\mathcal{A}$ は左合成について閉じているので $f\circ g \in \mathcal{A}$。
従って、 $f\circ g\in\mathcal{A}, \mathrm{cod}(f\circ g)=c$ より $f\circ g\in S$。従って $g\in f^{\ast}(S)$ であるから $f^{\ast}(S)\in J\_{\mathcal{A}}(d)$ である。

**(推移性公理)**

$S \in J\_{\mathcal{A}}(c)$であり $c$ 上の篩 $R$ が任意の $(f:d\rightarrow c)\in S$ に対して $f^{\ast}(R)\in J\_{\mathcal{A}}(d)$ であるとする。
この時 $R\in J\_{\mathcal{A}}(c)$ すなわち、 任意の $g\in\mathcal{A},\mathrm{cod}(g)=c$ に対して $g\in R$ である事を示せば良い。

ここで $\mathrm{A}$ が補完的であることより $g = h\circ k\ (h,k\in\mathcal{A}, h:d\rightarrow c, k: e\rightarrow d)$ と分解できる。
すると $h\in\mathcal{A},\mathrm{cod}(h)=c$ より $h\in S$ となる。従って仮定より $h^{\ast}(R)\in J\_{\mathrm{A}}(d)$ である。
よって $k\in\mathcal{A},\mathrm{cod}(k)=d$ より $k \in h^{\ast}(R)$ すなわち $g=h\circ k\in R$ となる。

$\square$
{{% /details %}}

このような $\mathrm{A}$ の例として、 圏 $\mathcal{C}$ の充満部分圏 $\mathcal{D}$ に対して、
$$ \mathcal{A} = \\{f \mid \mathrm{dom}(f)\in\mathcal{D} \\}$$
というものがある。 これが左合成によってドメインは変わらないので、これが左合成によって閉じているのは明らか。
また、任意の $(f:a\rightarrow b)\in\mathcal{A}$ に対して, $f=f\circ 1\_a,\ f, 1\_a \in \mathcal{A}$ と分解できる。

さて、 $J\_{\mathcal{A}}$ が最小の被覆篩を持つというのは以下の意味である。

{{% proposition %}}
$\mathcal{C}$ 上のGrothendieck位相 $J$ が任意の対象 $c$ について最小の被覆篩を持つ、すなわち $J(c)$ が包含関係について最小元を持つ、
ということと、ある $\mathcal{A}$ について $J=J\_{\mathcal{A}}$ であることは同値。
{{% /proposition %}}
{{% details 証明 %}}
**($\Rightarrow$)**

$\mathcal{C}$ 上のGrothendieck位相 $J$ が任意の対象 $c$ について最小の被覆篩を持つとする。ここで
$$\mathcal{A} = \bigcup\_{c\in\mathcal{C}} \min J(c)$$
と置くと $J\_{\mathcal{A}}=J$ である事を示す。

まず $\mathcal{A}$ が左合成について閉じていることを示す。
$(f:a\rightarrow b)\in\mathcal{A}$ 、 $g:b\rightarrow c$ とする。安定性定理より
$g^{\ast}(\min J(c)) \in J(b)$ であるので $\min J(b)\subset g^{\ast}(\min J(c))$ 。
ここで $f\in\min J(b)$ であるから $f\in g^{\ast}(\min J(c))$ すなわち $g\circ f\in \min J(c)\subset\mathcal{A}$。
従って $\mathcal{A}$ は左合成について閉じている。

続いて $\mathcal{A}$ が補完的である事を示す。すなわち任意の$(f:d\rightarrow c)\in\mathcal{A}$ が $f=f\_1\circ f\_2$ と分解できることを示す。
ここで
$$ R=\\{h \mid \exists g\in\min J(c), k\in\min J(\mathrm{dom}(g)), h=g\circ k\\} $$
とおく。これは、 $\mathcal{A}$ の射で分解できる $\mathrm{cod}(h)=c$ である $h$ の集合である。
$\min J(\mathrm{dom}(g))$ が前合成について閉じていることより、 $R$ も前合成について閉じているから $R$ は $c$ 上の篩である。

ここで $g\in\min J(c)$ で $R$ を引き戻すと、 $R$ の定義より
$$ \min J(\mathrm{dom}(g)) \subset g^{\ast}(R)$$
であるので、 単調性公理より $g^{\ast}(R)\in J(\mathrm{dom}(g))$ である。
従って、推移性公理より $R \in J(c)$ である。従って $f \in \min J(c)\subseteq R$ であるから $R$ の定義より $f$ は $\mathrm{A}$ の射で分解可能である。

最後に $J=J\_{\mathcal{A}}$ である事を示す。任意の対象 $c$ に対して
$$\begin{align*}
S\in J\_{\mathcal{A}}(c) &\Leftrightarrow (\forall f\in\mathcal{A},\mathrm{cod}(f)=c \Rightarrow f\in S) \\\\
                         &\Leftrightarrow (\forall f \in \min J(c) \Rightarrow f\ in S) \\\\
                         &\Leftrightarrow \min J(c) \subseteq S \\\\
                         &\Leftrightarrow S\in J(c) \quad (\because\text{単調性公理})
\end{align*}$$
であるから $J=J\_{\mathrm{A}}$ である。

**($\Leftrightarrow$)**

$\mathcal{C}$ 上のGrothendieck位相 $J\_{\mathcal{A}}$ が任意の対象 $c$ について最小の被覆篩を持つことを示す。
すなわち、 ある $S \in J\_{\mathcal{A}}(c)$ が存在して任意の $T\in J\_{\mathcal{A}}(c)$ に対して $S\subseteq T$ である事を示す。

$\mathcal{A}$ の元のうち、コドメインが $c$ である射の集合を $\mathcal{A}\_c$ とする。ここで
$$ S = \\{ f\circ g \mid f \in \mathcal{A}\_c, \mathrm{dom}(f)=\mathrm{cod}(g) \\}$$
と定めた時、これが最小の被覆篩である事を示す。

まず、 $S$ が篩であることは明らか。そして、任意の $f\in\mathcal{A}\_c$ について $f = f\circ 1\_{\mathrm{dom}(f)} \in S$ であるので
$S \in J\_{\mathcal{A}}(c)$ である。

続いて、$S$ が最小であることを示す。$T\in J\_{\mathcal{A}}(c)$ とすると、定義より $\mathcal{A}\_c \subseteq T$ 。
ここで $f\circ g\in S$ であるとすると $f\in \mathcal{A}\_c\subseteq T$ であり、 $T$ が篩であることより $f\circ g\in T$ であるから $S\subseteq T$ である。

$\square$
{{% /details %}}
