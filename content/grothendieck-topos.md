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
$c$ 上の篩全体は最大値を持ち、それを $M\_c$ と書く。 既に述べたように $c$ 上の篩 $S$ が最大であることと、 $1\_c\in M\_c$ であることは同値である。

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

{{% proposition %}}
$R,S$ が $c$ 上の篩であり、$R\subseteq S$ であるとき
$$ R\in J(c) \Rightarrow S\in J(c)$$
{{% /proposition %}}

{{% details 証明 %}}
$R,S$ が $c$ 上の篩であり、$R\subseteq S$、$R\in J(c)$ であるとする。

任意の $(f:d\rightarrow c)\in R$ をとると $f\in S$ であるから
$f^{\ast}(S) = M\_d$
である。従って最大性公理より $f^{\ast}(S)=M\_d \in J(d)$ である。よって推移性公理より $S\in J(c)$ である。 $\square$
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
