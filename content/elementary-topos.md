---
title: 初等トポス
weight: 4
section: 3
toc: true
---

## 初等トポス

### ハイティング代数・ブール代数

ブール代数を一般化した概念としてハイティング代数が定義される。
ハイティング代数は直観主義論理の意味論として用いられる。
以後、ハイティング代数を圏論的に述べる為にいくつか確認する。

まず、対象 $a,b$ の間に射が高々一つしかな圏 $\mathcal{C}$ を **半順序集合(partially ordered set)** という。
射$a\rightarrow b$ を $a\leq b$ と書くと、半順序集合の公理

- 反射則: 任意の $a\in\mathcal{C}$ について $a\leq a$
- 推移則: $a\leq b$ かつ $b\leq c$ ならば $a\leq c$
- 反対称則: $a\leq b$ かつ $b\leq a$ ならば $a = a$

を満たす事が分かる。半順序集合であって、任意の有限積と有限余積を持つ圏を **束(lattice)** という。
$a,b$ の積・余積をそれぞれ $a\wedge b, a\vee b$ と書く。束であり、始対象と終対象を持つものを **有界束(bounded lattice)** という。始対象を $\bot$、終対象を $\top$ と書く。

束について、以下の性質が成り立つ。
{{% proposition %}}
圏 $\mathcal{C}$ が束であるならば、任意の $a,b,c\in\mathcal{C}$ について以下が成り立つ。
- **交換則(commutativity)** : $a\wedge b = b \wedge a$, $a\vee b = b\vee a$
- **結合則(associativity)** : $a\wedge(b\wedge c) = (a\wedge b)\wedge c$, $a\vee(b\vee c) = (a\vee b)\vee c$
- **吸収則(absorption law)** : $a\wedge(a\vee b) = a\vee(a\wedge b) = a$
{{% /proposition %}}
{{% details 証明 %}}
交換則・吸収則は有限積・余積を持つ圏について一般に成り立つ性質であるので、吸収則と冪等則について示す。

$a\leq a$ と $a\leq a\vee b$ より $a\leq a\wedge(a\vee b)$ である。これと $a\wedge(a\vee b)\leq a$ より $a\wedge(a\vee b)=a$。もう一方も同様。(証明終)
{{% /details %}}

{{% definition title="ハイティング代数" %}}
圏 $\mathcal{H}$ が有界束でありかつカルテシアン閉圏である時、これを **ハイティング代数(Heyting algebra)** という。

指数対象 $b^a$ を $a\Rightarrow b$ と書く。
また、$a\Rightarrow\bot$ を $a$ の **擬似補(pseudo complement)** といい $\neg a$ と書く。
{{% /definition %}}

ハイティング代数の指数対象とは、$b,c$ について自然な同型
$ \mathcal{H}(c\wedge a, b) \simeq \mathcal{H}(c, a\Rightarrow b) $
が存在するものであるが、両辺とも射は1つしかないので
$c\wedge a \leq b$ と $c\leq (a\Rightarrow b)$ が同値となるような対象の事である。

冒頭でも述べたように、ハイティング代数は直観論理の意味論として用いられる。その場合は
$\wedge, \vee$ を「かつ」「または」、$\Rightarrow$ を「ならば」、$\neg$ を「でない」
と解釈する。


{{% proposition %}}
ハイティング代数 $\mathcal{H}$ は分配束である。すなわち任意の$a,b,c\in\mathcal{H}$ について
$$a\wedge(b\vee c) = (a\wedge b)\vee(a\wedge c)$$
$$a\vee(b\wedge c) = (a\vee b)\wedge(a\vee c)$$
{{% /proposition %}}
{{% details 証明 %}}
$a\wedge b \leq a$ かつ $a\wedge b \leq b\vee c$ より $a\wedge b \leq a\wedge(b\vee c)$ である。
同様にして $a\wedge c \leq a\wedge(b\vee c)$ でもある。よって
$$(a\wedge b)\vee(a\wedge c)\leq a\wedge(b\vee c) $$
である。

また$a\wedge b\leq (a\wedge b)\vee(a\wedge c)$ より $b\leq (a\Rightarrow (a\wedge b)\vee(a\wedge c))$ である。
同様に $c\leq (a\Rightarrow (a\wedge b)\vee(a\wedge c))$ であるので
$$ b\vee c\leq (a\Rightarrow(a\wedge b)\vee(a\wedge c))$$
である。従って
$$ a\wedge(b\vee c)\leq (a\wedge b)\vee(a\wedge c)$$
である。以上より
$$a\wedge(b\vee c) = (a\wedge b)\vee(a\wedge c)$$
である。また、これを用いてもう一方も示される。

$$ \begin{align\*}
  (a\vee b)\wedge(a\vee c) &= ((a\vee b)\wedge a)\vee((a\vee b)\wedge c) \\\\
                           &= a\vee((a\vee b)\wedge c) \\\\
                           &= a\vee((a\wedge c)\vee(b\wedge c)) \\\\
                           &= (a\vee(a\wedge c))\vee(b\wedge c) \\\\
                           &= a\vee(b\wedge c)
\end{align\*}$$

(証明終)
{{% /details %}}

{{% proposition title="ド・モルガンの法則" %}}
ハイティング代数では以下の **ド・モルガンの法則(De Morgan's law)** が成り立つ。
$$\neg a\wedge \neg b = \neg(a \vee b)$$

ただし、以下は **成り立つとは限らない** 。
$$\neg a\vee \neg b = \neg(a \wedge b)$$
{{% /proposition %}}
{{% details 証明 %}}
まず、任意の $a\in\mathcal{H}$ について $a\wedge\neg a=\bot$ である事を示す。
$(a\Rightarrow\bot)\leq(a\Rightarrow \bot)$ より$a\wedge(a\Rightarrow \bot)\leq \bot$ すなわち $a\wedge\neg a\leq\bot$ である。一方 $\bot$ は始対象であるから $\bot\leq a\wedge \neg a$ である。従って $a\wedge \neg a=\bot$ である。

これを用いて
$$(a\vee b)\wedge (\neg a\wedge \neg b) = (a\wedge \neg a \wedge \neg b)\vee (b\wedge \neg a \wedge \neg b)=(\bot\wedge b)\vee(\bot\wedge b) = \bot\vee\bot = \bot$$
より$ \neg a\wedge \neg b \leq (a\vee b\Rightarrow\bot)$ すなわち $\neg a\wedge\neg b\leq\neg(a\vee b)$ である。

また、 $a\leq a\vee b$ より
$$ a\wedge\neg(a\vee b) \leq (a\vee b)\wedge\neg(a\vee b) = \bot$$
であるので $\neg(a\vee b)\leq (a\Rightarrow\bot)$ すなわち $\neg(a\vee b)\leq \neg a$ である。同様にして $\neg (a\vee b)\leq \neg b$ であるので $\neg(a\vee b)\leq \neg a\wedge\neg b$ である。

従って
$$\neg a\wedge \neg b = \neg(a \vee b)$$
である。(証明終)
{{% /details %}}

{{% example %}}
位相空間 $X$ の開集合系 $\mathcal{O}(X)$ を包含関係によって半順序集合と見なしたものはハイティング代数となる。
{{% /example %}}

開集合系の公理から有界束である事がすぐ分かる。そして開集合 $U,V$ に対して
$U\cap W\subseteq V$ を満たす全ての開集合 $W$ の合併が指数対象 $V^U$ となる。そのような合併の存在は開集合の公理から保証される。

また、開集合 $U$ の擬似補は $U\cap W\subseteq\emptyset$ すなわち $U$ と交わらない全ての開集合 $W$ の和集合となる。

ハイティング代数のうち、 排中律を満たすものをブール代数という。

{{% definition title="ブール代数" %}}
ハイティング代数であり、任意の対象 $a$ について
$$a \vee \neg a = \top $$
が成り立つものを **ブール代数(Boolean algebra)** という。
{{% /definition %}}

{{% proposition %}}
ブール代数において **二重否定除去則(law of double negation elimination)** が成り立つ。
$$ \neg\neg a=a $$
{{% /proposition %}}
{{% details 証明 %}}
\begin{align\*}
&\neg\neg a= \neg\neg a\wedge(\neg a\vee a)=(\neg\neg a\wedge \neg a)\vee (\neg\neg a\wedge a) \\\\
&=\neg\neg a\wedge a= (\neg\neg a\wedge a)\vee(\neg a\wedge a) = (\neg\neg a\vee \neg a)\wedge a= a
\end{align\*}
(証明終)
{{% /details %}}

{{% proposition %}}
ブール代数において、ド・モルガンの法則が成り立つ。
$$\neg a\wedge \neg b = \neg(a \vee b)$$
$$\neg a\vee \neg b = \neg(a \wedge b)$$
{{% /proposition %}}
{{% details 証明 %}}
1つ目はハイティング代数である事から成立。2つ目は二重否定除去則を使って
$$ \neg a\vee\neg b = \neg\neg(\neg a\vee\neg b) = \neg(\neg\neg a\wedge\neg\neg b) = \neg(a\wedge b)$$
(証明終)
{{% /details %}}

{{% proposition %}}
$\mathcal{B}$ がブール代数であるならば、任意の $a,b\in\mathcal{B}$ について
$$ (a\Rightarrow b) = \neg a\vee b $$
{{% /proposition %}}
{{% details 証明 %}}
$a\wedge c\leq b$ であるならば、
$$ c\leq \neg a\vee c = (\neg a\vee a)\wedge (\neg a\vee c) = \neg a\vee(a\wedge c) \leq \neg a\vee b$$
であり、 $c\leq\neg a\vee b$ であるならば
$$ a\wedge c \leq a\wedge (\neg a\vee b) = (a\wedge \neg a)\vee(a\wedge b) = a\wedge b \leq b$$
であるので、 $\neg a\vee b$ は指数対象 $b^a$ である。指数対象は同型を除いて一意であるので
$$ (a\Rightarrow b) \simeq \neg a\vee b$$
であるが、半順序集合において同型な対象は一致するので
$$ (a\Rightarrow b) = \neg a\vee b$$
である。(証明終)
{{% /details %}}

### 部分対象分類子

集合論において、集合 $U$ の部分集合 $X$ は特性関数 $\chi$ によって表現する事ができる。
$$ X = \\{x\in U\mid\chi(x)\\}$$
初等トポスとはカルテシアン閉圏のうち、このような特性関数が常に存在する圏の事である。
$\chi(x)$ とは $x\in X$ の事であるので、初等トポスとは集合への元の帰属関係 $\in$ を表現する事が出来る圏だと行っても良い。

**引き戻し(pullback)** を用いるとこれを圏論的に記述する事ができる。引き戻しとは $\mathcal{J}$ が $\bullet\rightarrow\bullet\leftarrow\bullet$ の形の時の図式 $F:\mathcal{J}\rightarrow\mathcal{C}$ に対する極限を言うのだった。
$\mathbf{Set}$ においてこの事を見ていく。まず、 $\mathbf{Set}$ における図式 $A\xrightarrow{f} C\xleftarrow{g} B$ に対する引き戻し $A\times_C B$ は
$$ A\times_C B = \\{(a, b)\mid f(a)=g(b)\\\}$$
で与えられる。

$$\xymatrix{
A\times_C B \ar[r] \ar[d] & A \ar[d]^{f} \\\\
B \ar[r]^{g}              & C
}$$

そこで、一方を定数関数 $\mathrm{true}: 1\rightarrow \\{\mathrm{true}, \mathrm{false}\\}$ とすれば、もう一方を特性関数とした場合の集合を構成する事ができる。すなわち、以下において $Y$ が引き戻しならば

$$\xymatrix{
Y \ar[r] \ar[d] & 1 \ar[d]^{\mathrm{true}} \\\\
X \ar[r]^-{p}              & \\{\mathrm{true}, \mathrm{false}\\}
}$$

$$ Y = \\{x\in X\mid p(x)=\mathrm{true} \\} $$

となる。これを一般の場合に拡張すると以下の定義を得る。

{{% definition title="部分対象分類子" %}}
有限完備な圏 $\mathcal{C}$ の **部分対象分類子(subobject classifier)** とは、射 $\mathrm{true}:1 \xhookrightarrow{}\Omega$ であって、任意のモノ射 $x\xhookrightarrow{} u$ に対して、以下の図式が引き戻しの図式となるような射 $\chi_x:u\rightarrow\Omega$ がただ一つ存在するようなものである。

$$\xymatrix{
x \ar@{.>}[r] \ar@{^{(}->}[d] & 1 \ar@{^{(}->}[d]^{\mathrm{true}} \\\\
u \ar[r]^{\chi_x} & \Omega
} $$

$\chi_x$ を $x\xhookrightarrow{} u$ の **分類射(classifying arrow)** という。
{{% /definition %}}

モノ射 $x\xhookrightarrow{}u$ を $\mathcal{C}/u$ における同値関係で割ったものを $u$ の部分対象というのだった。({{< ref def.subobject >}})
以下の命題より、 **部分対象と分類射は一対一に対応する** ということが分かる。

{{% proposition %}}
$\mathcal{C}/u$ において同型なモノ射に対応する分類射は一致する。
{{% /proposition %}}
{{% details 証明 %}}
$\mathcal{C}$ を部分対象分類子 $\mathrm{true}:1\rightarrow\Omega$ を持つ圏であるとする。
モノ射 $i: x\xhookrightarrow{}u$ と $j: y\xhookrightarrow {}$ が同型であるとする。すなわち同型射 $\alpha:x\rightarrow y$ が存在して $i = j\circ\alpha$ であるとする。
$$\xymatrix{
x \ar@{^{(}->}[rd]^-{i} \ar[rr]^{\alpha} && y \ar@{^{(}->}[ld]^-{j} \\\\
 & u &
}$$
また、 $i,j$ に対応する分類射をそれぞれ $\chi_i,\chi_j$ とする。

まず、 $u\xhookleftarrow{j}y\rightarrow 1$ が $u\xrightarrow{\chi_j}\Omega\xleftarrow{\mathrm{true}}1$ に対する引き戻しであるので、任意の $f: z\rightarrow u$ に対して、以下が可換となるような $u:z\rightarrow y$ が一意に存在する。
$$\xymatrix{
z \ar[rd]^u \ar@{.>}@/^1pc/[rrd] \ar@/^-1pc/[rdd]\_{f}& & \\\\
& y \ar@{^{(}->}[d]^{j} \ar@{.>}[r] & 1 \ar@{^{(}->}[d]^{\mathrm{true}} \\\\
& u \ar[r]^{\chi_j} & \Omega
}$$
$i=j\circ\alpha$ を用いて書き直すと以下の図式が可換であるが、 $u$ が一意である事と $\alpha$ が同型射であることより、この図式が可換となるような $\alpha^{-1}\circ u$ も一意に定まる。従って、この図式の四角形の部分は引き戻しの図式であるので、 $\chi_j$ は $i$ に対応する分類射である。従って分類射が一意に定まることから $\chi_i = \chi_j$

$$\xymatrix{
z \ar[rd]^{\alpha^{-1}\circ u} \ar@{.>}@/^1pc/[rrd] \ar@/^-1pc/[rdd]\_{f}& & \\\\
& x \ar@{^{(}->}[d]^{i} \ar@{.>}[r] & 1 \ar@{^{(}->}[d]^{\mathrm{true}} \\\\
& u \ar[r]^{\chi_j} & \Omega
}$$
(証明終)
{{% /details %}}

さらに、この一対一対応は自然である。また、$\mathcal{C}$ の各対象をその部分対象に移す関手 $\mathrm{Sub}$ を考えると、この関手を表現する対象が部分対象分類子となることも分かる。

{{% proposition label="prop.representability-of-sub" %}}
圏 $\mathcal{C}$ が有限完備かつ局所小である時、 $\mathcal{C}$ が部分対象分類子を持つことと、前層

$$\mathrm{Sub}:\mathcal{C}^{\mathrm{op}}\ni a \longmapsto \\{u\xhookrightarrow{} a\\}/{\simeq} \in\mathbf{Set}$$

が表現可能である事は同値。また、部分対象分類子 $\mathrm{true}:1\rightarrow \Omega$ について、 $\Omega$ はこの関手を表現する対象である。 すなわち、$a\in\mathcal{C}$ について自然な同型
$$ \mathrm{Sub}(a)\simeq\mathcal{C}(a,\Omega) $$
が存在する。また$\mathrm{true}$ は普遍要素の代表元である。

{{% /proposition %}}

{{% details 証明 %}}
($\mathrm{Sub}$が関手であることの証明)

任意の $f:b\rightarrow a$ と部分対象 $x\xhookrightarrow{i}a \in \mathrm{Sub}(a)$ について、$\mathrm{C}$ は有限完備だから$f$ に沿った $i$ の引き戻し $\bar{i}$ が存在する。この時 {{< ref prop.pullback-preserves-monomorphism >}} より $\bar{i}$ もモノ射である。

$$\xymatrix{
y \ar[d]\_{\bar{i}} \ar[r]^{\bar{f}} & x \ar[d]^{i} \\\\
b \ar[r]^{f} & a
}$$

この対応を用いて
$$\mathrm{Sub}(f): \mathrm{Sub}(a)\ni\\{x\xhookrightarrow{i} a\\}/{\simeq}\longmapsto\\{y\xhookrightarrow{\bar{i}} b\\}/{\simeq}\in\mathrm{Sub}(b)$$
とすると $\mathrm{Sub}$ は関手 $\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ となる。$\mathrm{Sub}$ が射の合成を保存することについて {{< ref prop.pasting-law-of-pullbacks >}} からわかるので、あとは同値類の代表元の選び方によらずwell-definedである事を示せば良いが、スライス圏 $\mathcal{C}/a$ における同型 $(x\xrightarrow{i}a)\simeq(x'\xrightarrow{i'}a)$ が存在する時、 $x\simeq x'$ でもあるので、対応する引き戻しも同型となることは明らか。

(部分対象分類子を持つ $\Rightarrow$ $\mathrm{Sub}$が表現可能)

$\mathcal{C}$ が有限完備かつ局所小であるとする。$\mathcal{C}$ が部分対象分類子 $\mathrm{true}1\rightarrow\Omega$ を持つとし、任意の $a\in\mathcal{C}$ について自然な同型
$$ \phi: \mathrm{Sub}(a) \xrightarrow{\simeq} \mathcal{C}(a, \Omega) $$
が存在する事を示す。$\phi$ が全単射であることは既に示したので、自然性のみを示せば良い。すなわち任意の $f:b\rightarrow a$ に対して以下が可換であることを示せば良いが、

$$\xymatrix{
\mathrm{Sub}(a) \ar[d]\_{\mathrm{Sub}(f)} \ar[r]^{\phi_a} & \mathcal{C}(a, \Omega) \ar[d]^{\mathcal{C}(f, \Omega)} \\\\
\mathrm{Sub}(b)                           \ar[r]^{\phi_b} & \mathcal{C}(b, \Omega)
}$$

以下の図式を考えると、

$$\xymatrix{
y \ar@{^{(}->}[d]\_{m'\in\mathrm{Sub}(f)([m])} \ar[r] & x \ar@{^{(}->}[d]^{m\in\mathrm{Sub}(a)} \ar[rr] && 1 \ar@{^{(}->}[d]^{\mathrm{true}} \\\\
b \ar[r]^{f} \ar@/^-1pc/[rrr]\_{\phi_b([m'])} & a \ar[rr]^{\phi_a([m])}            && \Omega \\\\
}$$

下側の$b$から$\Omega$ までの2つの経路はいずれも $m'$ に対する分類射であるから、分類射の一意性より任意のモノ射 $m:x\xhookrightarrow{} a$ に対して

$$ \phi_b\circ \mathrm{Sub}(f)([m]) = \phi_a([m])\circ f = ((-\circ f)\circ\phi_a)([m])=(\mathcal{C}(f,\Omega)\circ\phi_a)([m])$$

である。ただし $[m]$ は$m$ を含む同値類。

($\mathrm{Sub}$が表現可能 $\Rightarrow$ 部分対象分類子を持つ)

$\mathrm{Sub}$ がある $\Omega\in\mathcal{C}$ によって表現されるとする。すなわち、$a\in\mathcal{C}$ について自然な同型
$$ \phi_a: \mathrm{Sub}(a) \xrightarrow{\simeq} \mathrm{C}(a, \Omega) $$
が存在するとする。ここで同型 $ \phi\_{\Omega}: \mathrm{Sub}(\Omega) \xrightarrow{\simeq} \mathrm{C}(\Omega, \Omega) $ において右の $1\_\Omega$ に対応する部分対象の代表元を $\mathrm{true}: t\xhookrightarrow{}\Omega$ とする。
この時点では $\mathrm{true}$ のドメイン $t$ が終対象であるかは分からないので注意。

あとは、任意のモノ射 $m: x\xhookrightarrow{} u$ に対して以下の図式が引き戻しとなるような $\chi: u\rightarrow\Omega$ が唯一つであることと、 $t$ が終対象であることを示せば良い。

$$\xymatrix{
x \ar[d]\_{m} \ar[r] & t \ar[d]^{\mathrm{true}} \\\\
u \ar[r]^{\chi} & \Omega \\\\
}$$

まず、$m$ が $\mathrm{true}$ の $\chi$ に沿った引き戻しであることより
$$ [m] = \mathrm{Sub}(\chi)([\mathrm{true}]) $$
である。また、以下が可換であるから

$$\xymatrix{
\mathrm{Sub}(\Omega) \ar[d]\_{\mathrm{Sub}(\chi)} \ar[r]^{\phi\_\Omega} & \mathcal{C}(\Omega, \Omega) \ar[d]^{-\circ\chi} \\\\
\mathrm{Sub}(u) \ar[r]^{\phi\_x} & \mathrm{C}(u, \Omega)
}$$

$$\phi_u(\mathrm{Sub}(\chi)([\mathrm{true}])) = \phi\_{\Omega}([\mathrm{true}])\circ \chi$$

である。これらと、 $\phi\_{\Omega}([\mathrm{true}])=1\_\Omega$ より
$$\chi = \phi_u([m]) $$
である。従って、 $\chi$ は $m$ に対して一意に定まる。

また、任意の $f:x\rightarrow t$ に対して以下の図式は引き戻しの図式となるので
$$\xymatrix{
x \ar[d]\_{1_x} \ar[r]^{f} & t \ar[d]^{\mathrm{true}} \\\\
x \ar[r]^{\mathrm{true}\circ f} & \Omega \\\\
}$$

$\mathrm{true}\circ f = \phi_x([1_x])$ である。この右辺が $f$ に依らないことと、$\mathrm{true}$ がモノであることから$f:x\rightarrow t$ の他には射 $x\rightarrow t$ が存在しない事が分かる。よって射 $x\rightarrow t$ は存在するならば唯一つである。あとは任意の $x\in\mathcal{C}$ について、$x$ から $t$ への射が存在する事を示せば良い。

任意の $x\in\mathcal{C}$ について $1_x:x\rightarrow x$ はモノだから $[1_x]\in \mathrm{Sub}(x)$ なので、$\phi_x([1_x]):x \rightarrow \Omega$ という射が存在。よって、$\mathrm{C}$ は有限完備であるので、$x\xrightarrow{\phi_x([1_x])}\Omega\xleftarrow{\mathrm{true}} t$ に対する引き戻しが存在するが、上で示したことから下図のように左側面が $1_x$ となる図式で引き戻しとなるものが存在。よって、この上辺の射 $x\rightarrow t$ は必ず存在。以上より、任意の $x\in\mathcal{C}$ に対して射 $x\rightarrow t$ が唯一つ存在するので $t$ は終対象。

$$\xymatrix{
x \ar[d]\_{1_x} \ar[r] & t \ar[d]^{\mathrm{true}} \\\\
x \ar[r]^{\phi_x([1_x])} & \Omega
}$$


(部分対象分類子が普遍要素であること)

任意の $x\in\mathcal{C}$ と $[m]\in\mathrm{Sub}(x)$ に対して、ある $f: x\rightarrow\Omega$ が存在して
$$[m] = \mathrm{Sub}(f)([\mathrm{true}])$$
となる事を示せば良いが、$f$ として$m$ の分類射を取ればこれが成立する事が分かる。

(証明終)
{{% /details %}}

### 層

前層の圏 $\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}$ の部分対象分類子 $\Omega: \mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ について考える。米田の補題より、任意の $c\in\mathcal{C}$ について

$$ \Omega(c) \simeq \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(c),\Omega) $$

であり、{{< ref prop.representability-of-sub >}} より

$$ \Omega(c) \simeq \mathrm{Sub}(\mathcal{Y}(c)) $$

である。この $\Omega(c)$ を $c$ の上の層という。

{{% definition title="層" %}}
{{% /definition %}}


### 初等トポス

以上で、初等トポスが定義出来る。

{{% definition title="初等トポス" %}}
カルテシアン閉圏であり、任意の部分対象分類子が存在する圏を **初等トポス(elementary topos)** という。
{{% /definition %}}

初等トポスは一階述語論理による公理を与えることが出来る。

