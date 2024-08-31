---
title: 初等トポス
weight: 4
section: 3
toc: true
---

## 初等トポス

集合論において、集合 $U$ の部分集合 $X$ は特性関数 $\chi$ によって表現する事ができる。
$$ X = \\{x\in U\mid\chi(x)\\}$$
初等トポスとはカルテシアン閉圏のうち、このような構成が可能である圏の事であり、集合論的な操作を行うことができる圏である。
$\chi(x)$ が真であるとはつまり "$x\in X$"であるという事であるので、初等トポスとは集合への元の帰属関係 $\in$ を表現する事が出来る圏だと言っても良い。

### 部分対象

まず集合の包含関係 $X\subseteq U$ を圏論的に一般化する。
$\mathbf{Set}$ においてはこれは包含写像 $X\hookrightarrow{} U$ によって表現できる。包含写像は単射であるが、 $\mathbf{Set}$ における単射はモノ射であるので、一般化する場合にもモノ射を用いる。ただし、モノ射の中には包含写像以外の物も含まれるのでこれを分類するという操作が必要となる。

{{% definition title="モノ射の順序関係" %}}
$a\in\mathcal{C}$ をコドメインとするモノ射 $m:x \hookrightarrow a, n:y \hookrightarrow a$ について、以下が可換となるような射 $f:x\rightarrow y$ が存在するときに $m\leq n$ であると定める。
$a$をコドメインとするモノ射全体は関係 $\leq$ によって 前順序(preorder) をなす。(前順序"集合"とは限らないので注意)
$$\xymatrix{
    & a &       \\\\
x \ar@{^{(}->}[ru]^m \ar[rr]^f & & y \ar@{^{(}->}[lu]\_n
}$$
{{% /definition %}}

$n$ がモノである事よりこの図式が成立するような $f:x\rightarrow y$ は存在するならば唯一つである。前順序とは反射律と推移率すなわち

- $a\leq a$
- $a\leq b, b\leq c \Rightarrow a\leq c$

が成り立つ二項関係の事であるが、上で定義した $\leq$ がこれを満たすことは簡単に分かるので証明は省略する。

{{% definition title="部分対象" %}}
コドメインが $a\in\mathcal{C}$ であるモノ射 $m: x\hookrightarrow a, n: y\hookrightarrow a$ の同値関係 $m\sim n$ を
$$ m\leq n\text{かつ} n\leq m$$
によって定める。このとき、コドメインが $a$ であるモノ射全体を同値関係 $\sim$ で割った同値類を $a$ の **部分対象(subobject)** という。以下, 代表元が $m$ の同値類を $[m]$ と書く。

対象 $a$ の部分対象全体は $\leq$ によって 半順序(partially ordered) となる。任意の対象 $a\in\mathcal{C}$ の部分対象全体の類が集合となる圏は **冪化可能(well-powered)** であるという。
{{% /definition %}}
誤解の恐れがない場合は、モノ射 $m:x\hookrightarrow a$ や $x$ を $a$ の部分対象ということもある。

{{% proposition %}}
$a$ の部分対象 $m: x\hookrightarrow a, n:y\hookrightarrow a$ が同値である事と、以下を可換にする同型射 $f:x\rightarrow y$ が存在することは同値。


$$\xymatrix{
    & a &       \\\\
x \ar@{^{(}->}[ru]^m \ar[rr]^f & & y \ar@{^{(}->}[lu]\_n
}$$
{{% /proposition %}}
{{% details 証明 %}}
$m,n$ が同値であるとすると、$m=n\circ f$ を満たす $f:x\rightarrow y$ と $n=m\circ g$ を満たす $g:y\rightarrow x$ が存在する。よって
$$ m\circ 1_x = m\circ g\circ f$$
が成立するので $m$ がモノ射である事より $g\circ f=1_x$。同様に $f\circ g=1_y$ であるので $f,g$ は同型射。

逆に、$m=n\circ f$を満たす $f$ が同型射であるとすると両辺に $f^{-1}$ を右から合成して $m\circ f^{-1}=n$ が成立する。 よって $m\leq n$ かつ $n\leq m$ であるので $m\sim n$ である。 $\square$
{{% /details %}}

$\mathbf{Set}$ における対象 $a$ の部分対象全体と $a$の部分集合全体は一対一に対応する。すなわち、部分対象 $m$ に対応する部分集合とは関数 $m$ の像であり、部分対象の順序 $\leq$ は部分集合の包含関係 $\subseteq$ と対応する。

### 引き戻し
$$ X = \\{x\in U\mid\chi(x)\\}$$

を圏論的に定式化する為には **引き戻し(pullback)** を用いる事ができる。引き戻しとは $\mathcal{J}$ が $\bullet\rightarrow\bullet\leftarrow\bullet$ の形の時の図式 $F:\mathcal{J}\rightarrow\mathcal{C}$ に対する極限を言うのだった。これを、具体的に書き下すと以下の定義となる。

{{% definition title="引き戻し" %}}
図式 $a\xrightarrow{f} c\xleftarrow{g} b$ に対する **引き戻し(pullback)** とは、以下の図式が可換となるような任意の 対象 $x$ と射 $\alpha: x\rightarrow a, \beta: x\rightarrow b$ に対して
$$\xymatrix{
x \ar@/^1pc/[rrd]^{\beta} \ar@/^-1pc/[rdd]\_{\alpha} & & \\\\
& & b \ar[d]^{g} \\\\
& a \ar[r]^{f} & c
}$$
以下の図式が可換となるような $u$ が唯一つ存在するような対象 $p$ と射 $\bar{f},\bar{g}$ の事である。
$$\xymatrix{
x \ar[rd]^{u} \ar@/^1pc/[rrd]^{\beta} \ar@/^-1pc/[rdd]\_{\alpha} & & \\\\
& p \ar[r]^{\bar{f}} \ar[d]\_{\bar{g}} & b \ar[d]^{g} \\\\
& a \ar[r]^{f} & c
}$$
$\bar{f}$ を $g$ に沿った $f$ の引き戻しとも言い、$g^\*f$ とも書く。 $\bar{g}$ についても同様。
{{% /definition %}}

$\mathbf{Set}$ における図式 $A\xrightarrow{f} C\xleftarrow{g} B$ に対する引き戻し $A\times_C B$ は
$$ A\times_C B = \\{(a, b)\in A\times B\mid f(a)=g(b)\\\}$$
で与えられる。

$$\xymatrix{
A\times_C B \ar[r] \ar[d] & A \ar[d]^{f} \\\\
B \ar[r]^{g}              & C
}$$

引き戻しの性質をいくつか確認しておく。

{{% proposition label="prop.pullback-preserves-monomorphism" %}}
引き戻しはモノ射を保存する。
すなわち、以下が引き戻しの図式の時 $g$ がモノ射ならば $\bar{g}$ もモノ射。
$$\xymatrix{
p \ar[r]^{\bar{f}} \ar[d]\_{\bar{g}} & b \ar[d]^{g} \\\\
a \ar[r]^{f} & c
}$$
{{% /proposition %}}
{{% details 証明 %}}
$g$ がモノ射であるとする。並行射 $\alpha,\beta: x\rightarrow p$ について $\bar{g}\circ \alpha = \bar{g}\circ\beta$
であるとすると $f\circ\bar{g}\circ\alpha=f\circ\bar{g}\circ\beta$ であるから図式の可換性より
$g\circ\bar{f}\circ\alpha=g\circ\bar{f}\circ\beta$。よって $g$ はモノ射であるから $\bar{f}\circ\alpha=\bar{f}\circ\beta$である。従って、以下の可換図式を得るので引き戻しの普遍性より $\alpha=\beta$である。よって $\bar{g}$ はモノ射。$\square$

$$\xymatrix{
x \ar@<2pt>[rd]^{\alpha} \ar@<-2pt>[rd]\_{\beta} \ar@/^1pc/[rrd]^{\bar{f}\circ\alpha = \bar{f}\circ\beta} \ar@/^-1pc/[rdd]\_{\bar{g}\circ\alpha=\bar{g}\circ\beta} & & \\\\
& p \ar[r]^{\bar{f}} \ar[d]\_{\bar{g}} & b \ar[d]^{g} \\\\
& a \ar[r]^{f} & c
}$$
{{% /details %}}

{{% proposition label="prop.pasting-law-of-pullbacks" %}}
以下の可換図式において、右の四角が引き戻しであるならば、左の四角が引き戻しであることと、外側の四角が引き戻しであることは同値。
$$\xymatrix{
\cdot \ar[r] \ar[d] & \cdot \ar[r] \ar[d] & \cdot \ar[d] \\\\
\cdot \ar[r]        & \cdot \ar[r]        & \cdot
}$$
{{% /proposition %}}
{{% details 証明 %}}
右の四角が引き戻しであるとし、以下の可換図式を考える。

$$\xymatrix{
x \ar@/^-1pc/[rdd]\_-{f} \ar@/^2pc/[rrrd]^-{g} \ar@/^1pc/[rrd]^-{v} \ar[rd]^-{u} &&& \\\\
&\cdot \ar[r] \ar[d] & \cdot \ar[r] \ar[d] & \cdot \ar[d] \\\\
&\cdot \ar[r]        & \cdot \ar[r]        & \cdot
}$$
まず、左の四角が引き戻しであるとして、外側の四角について考える。
図式の外側が可換となるような、$f,g$に対して右の四角に注目することと $v$の存在が一意であることがわかる。
すると $f,v$ について左に四角に注目することで、 $u$ の一意性もわかる。従って 外側の四角も引き戻しの図式である。

外側の四角が引き戻しであるとする。$f,v$ に対して $v$ の方に右の四角の上辺を合成すれば $g$ となり、これに外側の四角が引き戻しであることを使用すれば $u$ が一意であることがわかる。従って左側の四角も引き戻しの図式である。
$\square$
{{% /details %}}

{{% proposition %}}
$f: x\rightarrow y$ に対して $1_y^\*f = f$
$$\xymatrix{
x \ar[d]\_f \ar[r] & x \ar[d]^f \\\\
y \ar[r]^{1_y} & y
}$$
{{% /proposition %}}
これの証明は簡単なので省略する。

### 部分対象分類子

引き戻しの図式の一方を定数関数 $\mathrm{true}: 1\rightarrow \\{\mathrm{true}, \mathrm{false}\\}$ 、もう一方を特性関数とすれば冒頭で説明した部分集合の構成が出来る。すなわち、以下において $Y$ が引き戻しならば($X\times 1\simeq X$ であるから)

$$\xymatrix{
Y \ar[r] \ar[d] & 1 \ar[d]^{\mathrm{true}} \\\\
X \ar[r]^-{\chi}              & \\{\mathrm{true}, \mathrm{false}\\}
}$$

$$ Y = \\{x\in X\mid \chi(x)=\mathrm{true} \\} $$

となる。これを一般の場合に拡張すると以下の定義を得る。

{{% definition title="部分対象分類子" %}}
有限完備な圏 $\mathcal{C}$ の **部分対象分類子(subobject classifier)** とは、射 $\mathrm{true}:1 \xhookrightarrow{}\Omega$ であって、任意のモノ射 $x\xhookrightarrow{} u$ に対して、以下の図式が引き戻しの図式となるような射 $\chi_x:u\rightarrow\Omega$ がただ一つ存在するようなものである。

$$\xymatrix{
x \ar@{.>}[r] \ar@{^{(}->}[d] & 1 \ar@{^{(}->}[d]^{\mathrm{true}} \\\\
u \ar[r]^{\chi_x} & \Omega
} $$

$\chi_x$ を $x\xhookrightarrow{} u$ の **分類射(classifying arrow)** という。
{{% /definition %}}

構成 $X=\\{x\in U\mid \chi(x)=\mathrm{true} \\}$ において集合 $X$ と特性関数 $\chi$ は一対一に対応する。これを一般化した定理が部分対象分類子を持つ圏についても成立する。

{{% proposition label="prop.subobject-classifying-arrow" %}}
$u$ の部分対象と分類射 $u\rightarrow\Omega$ は一対一に対応する。
{{% /proposition %}}
{{% details 証明 %}}
$\mathcal{C}$ を部分対象分類子 $\mathrm{true}:1\rightarrow\Omega$ を持つ圏であるとする。
$u$ の部分対象 $m:x\xhookrightarrow{}u$ に分類射 $\chi_x$ を対応させる対応 $\phi$ が全単射である事を示す。
まず、この対応が$m$の選び方に依らずwell-definedである事を示す。

モノ射 $m: x\xhookrightarrow{}u$ と $n: y\xhookrightarrow {}u$ が同値であるとする。すなわち同型射 $\alpha:x\rightarrow y$ が存在して $m = n\circ\alpha$ であるとする。
$$\xymatrix{
x \ar@{^{(}->}[rd]^-{m} \ar[rr]^{\alpha} && y \ar@{^{(}->}[ld]^-{n} \\\\
 & u &
}$$

部分対象分類子の定義より、 $m,n$ それぞれに対応する分類射 $\chi_m,\chi_n$ が存在するのでこれらが同一である事を示せば良い。
まず、 $u\xhookleftarrow{n}y\rightarrow 1$ が $u\xrightarrow{\chi_n}\Omega\xleftarrow{\mathrm{true}}1$ に対する引き戻しであるので、任意の $f: z\rightarrow u$ に対して、以下が可換となるような $v:z\rightarrow y$ が一意に存在する。
$$\xymatrix{
z \ar[rd]^v \ar@{.>}@/^1pc/[rrd] \ar@/^-1pc/[rdd]\_{f}& & \\\\
& y \ar@{^{(}->}[d]^{n} \ar@{.>}[r] & 1 \ar@{^{(}->}[d]^{\mathrm{true}} \\\\
& u \ar[r]^{\chi_n} & \Omega
}$$
これを $m=n\circ\alpha$ を用いて書き直すと以下の可換図式を得る。

$$\xymatrix{
z \ar[rd]^{\alpha^{-1}\circ v} \ar@{.>}@/^1pc/[rrd] \ar@/^-1pc/[rdd]\_{f}& & \\\\
& x \ar@{^{(}->}[d]^{m} \ar@{.>}[r] & 1 \ar@{^{(}->}[d]^{\mathrm{true}} \\\\
& u \ar[r]^{\chi_n} & \Omega
}$$
すると $m$ がモノであることにより、この図式が可換となる $z$ から $x$ への射は $\alpha^{-1}\circ v$ ただ一つとなるので、 $u\xhookleftarrow{m}x\rightarrow 1$ は $u\xrightarrow{\chi_n}\Omega\xleftarrow{\mathrm{true}}1$の引き戻しとなっている。すなわち $\chi_n$ は $m$ の分類射になっていて、分類射の一意性から $\chi_m = \chi_n$。

続いて $\phi:[m:x\xhookrightarrow{}u]\mapsto\chi_x$ が全単射である事を示す。まず、$\mathcal{C}$ は有限完備であるから任意の射 $\chi:u\rightarrow \Omega$ に対して引き戻し $\chi^\*\mathrm{true}$ が存在する。
$\mathrm{true}:1\rightarrow\Omega$ はモノであるので、 $\chi^\*\mathrm{true}$ もモノであるから、これを代表元とする部分対象が存在する。よって $\phi$ は全射。
また、 $\phi([m:x\xhookrightarrow{}u])=\phi([n:y\xhookrightarrow{}u]) = \chi$ であるとすると、引き戻しは同型を除いて一意であることから、同型射 $\alpha:x\rightarrow y$ が存在して $m=n\circ \alpha$ となること。すなわち $m\sim n$ であることが示される。よって $[m:x\xhookrightarrow{}u]=[n:y\xhookrightarrow{}u]$ であるから $\phi$ は単射。 $\square$
{{% /details %}}

### 部分対象関手

$x\in\mathcal{C}$ の部分対象の集まりを$\mathrm{Sub}(x)$ と表すと、{{< refer prop.subobject-classifying-arrow >}} より同型

$$ \mathcal{C}(x, \Omega) \simeq \mathrm{Sub}(x) $$

が存在する。これより、$\mathrm{Sub}$ が表現可能関手であって、 $\Omega$ がそれを表現する対象である事が示唆される。
そして、普遍要素 $u\in\mathrm{Sub}(\Omega)$ の存在も示唆されるが、実はこれが $\mathrm{true}:1\rightarrow\Omega$ であって、分類射 $\chi$ の構成は普遍的構成となっている。
本説ではこのことを示していく。

{{% definition title="部分対象関手" %}}
冪化可能な圏 $\mathcal{C}$ において、 $\mathrm{Sub}(x)$ を $x\in\mathcal{C}$ の部分対象の集合とし、任意の $f: x\rightarrow y$ に対して $\mathrm{Sub}(f): \mathrm{Sub}(y)\rightarrow\mathrm{Sub}(x)$ を$\mathrm{Sub}(y)$ の部分対象の $f$ に沿った引き戻しに写す写像とすれば、$\mathrm{Sub}$ は反変関手 $\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ となる。これを **部分対象関手(subobject functor)** という。

$$\xymatrix{
\bullet \ar@{^{(}->}[d]^{}=\"p\" \ar[r] & \bullet \ar@{^{(}->}[d]\_{}=\"q\" \\\\
x \ar[r]\_f & y 
\ar@{|->}\_{\mathrm{Sub}(f)} \"q\"; \"p\"
}$$
{{% /definition %}}
これが関手となることは、既に示した引き戻しの性質から容易に分かる。そして、この部分対象関手を表現する対象及び普遍要素が部分対象分類子である。

{{% theorem label="prop.representability-of-sub" %}}
圏 $\mathcal{C}$ が有限完備かつ局所小である時、部分対象関手 $\mathrm{Sub}:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ が表現可能であることと、部分対象分類子 $\mathrm{true}:1\rightarrow\Omega$ が存在することは同値。

また、$\mathrm{Sub}$ を表現する対象が $\Omega$ であり、普遍要素が $[\mathrm{true}:1 \rightarrow\Omega]\in\mathrm{Sub}(\Omega)$ である。
{{% /theorem %}}

{{% details 証明 %}}
$\mathrm{Sub}$ が表現可能関手である事と、 $\mathrm{Sub}$に関して普遍的構成が存在することは同値であるから、部分対象分類子が存在する条件と普遍的構成が存在する条件が一致する事を示せば良い。

$\mathrm{Sub}$ の普遍的構成とは {{< refer prop.universal-construction >}} より、ある対象 $\Omega\in\mathcal{C}$ とある要素 $[\mathrm{true}:t\hookrightarrow\Omega]\in\mathrm{Sub}(\Omega)$ が存在して、
任意の対象 $u\in\mathcal{C}$ と任意の要素 $[m:x\hookrightarrow u] \in \mathrm{Sub}(u)$ について
$$ [m] = \mathrm{Sub}(\chi)([\mathrm{true}]) $$
となるような $\chi:u\rightarrow\Omega$ が唯一つ存在するという事である。

すなわち、$\mathrm{Sub}(\chi)$ とは $\chi$ に沿った引き戻しの事であったから、任意のモノ射 $m:x\xhookrightarrow{}u$ に対して、以下の図式が引き戻しとなるような $\chi$ が唯一つ存在する事が
普遍的構成が存在する事、そして $\mathrm{Sub}$ が表現可能関手である事と同値である。

$$\xymatrix{
x \ar@{^{(}->}[d]\_{m} \ar[r] & t \ar[d]^{\mathrm{true}} \\\\
u \ar[r]^{\chi} & \Omega \\\\
}$$

あとは $t$ が終対象である事を示せば、部分対象分類子が存在する条件と一致するので証明が完了する。
ここで、任意の $x$ に対して$1_x$ がモノである事に注意すると、以下が引き戻しとなるような $\chi$ が一意に存在する。
$$\xymatrix{
x \ar[d]\_{1_x} \ar[r] & t \ar[d]^{\mathrm{true}} \\\\
x \ar[r]^{\chi} & \Omega \\\\
}$$
従って、この $\chi$ を $\mathrm{true}$ に沿って引き戻した射 $x\rightarrow t$ が存在する。よって、$\mathcal{C}(x, t)\neq \emptyset $ である。
そして、任意の $f:x\rightarrow t$ に対して、以下の可換図式を考えるとこれは引き戻しの図式となっている。
$$\xymatrix{
x \ar[d]\_{1_x} \ar[r]^f & t \ar[d]^{\mathrm{true}} \\\\
x \ar[r]^{\mathrm{true}\circ f} & \Omega \\\\
}$$
なぜならば、以下が可換となるような任意の $y$ と $\alpha:y\rightarrow x, \beta: y\rightarrow t$ について

$$\xymatrix{
y \ar@/^1pc/[rrd]^{\beta} \ar@/^-1pc/[rdd]\_{\alpha}& & \\\\
        &                          & t \ar[d]^{\mathrm{true}} \\\\
        & x \ar[r]^{\mathrm{true}\circ f} & \Omega \\\\
}$$
$\mathrm{true}\circ f\circ\alpha = \mathrm{true}\circ\beta$ であり $\mathrm{true}$ がモノであるから $f\circ\alpha = \beta$ となるので
以下も可換となる。またこの時 $y\rightarrow x$ は $\alpha $ に一意に定まるからである。

$$\xymatrix{
y \ar[rd]^{\alpha} \ar@/^1pc/[rrd]^{\beta} \ar@/^-1pc/[rdd]\_{\alpha}& & \\\\
        & x\ar[d]\_{1_x} \ar[r]^f & t \ar[d]^{\mathrm{true}} \\\\
        & x \ar[r]^{\mathrm{true}\circ f} & \Omega \\\\
}$$
従って、最初の図式の $\mathrm{true}\circ f$ は $1_x$ に対して一意に定まるものであり $f$ によらない。よって、もし2つの射 $f,g:x\rightarrow t$
が存在したとすると $\mathrm{true}\circ f=\mathrm{true}\circ g$ であって、 $\mathrm{true}$ はモノであるから $f=g$。
以上より任意の $x$ に対して射 $x\rightarrow t$ は唯一つしか存在しないので $t$ は終対象である。 $\square$

{{% /details %}}

{{% proposition %}}
部分対象分類子は同型を除いて一意である。
{{% /proposition %}}
これは表現可能関手を表現する対象であるから明らか。

### 初等トポス

以上より初等トポスを定義する事ができる。

{{% definition title="初等トポス" %}}
有限完備かつカルテシアン閉であり、部分対象分類子が存在する圏を **初等トポス(elementary topos)** 、もしくは単に **トポス(topos)** という。(toposの複数形はtopoiと書く。)
{{% /definition %}}

すなわち、初等トポスとは任意の有限極限、指数対象、部分対象分類子が存在する圏である。そして任意の有限極限は有限積とイコライザから構成されるので、有限積・イコライザ・指数対象・部分対象分類子が存在する圏とも言える。例えば $\mathbf{Set}$ は初等トポスであり、まとめると以下のようになる。

|                | 表現対象                                          | 普遍要素                      |
|:--------------:|:---------------------------------------------------:|:-----------------------------:|
| 有限積         | $\prod\_{i\in\mathcal{J}}A_i$                       | $\pi_i:\prod\_{i\in\mathcal{J}}A_i\rightarrow A_i$ |
| イコライザ     | $\mathrm{eq}(f,g) = \\{x \in X \mid f(x)=g(x)\\}$   | $i: \mathrm{eq}(f,g)\hookrightarrow X$ |
| 指数対象       | $Y^X = \\{f: X\rightarrow Y\\}$                     | $\epsilon: X\times Y^X\rightarrow Y$ |
| 部分対象分類子 | $\Omega=\\{\mathrm{true}, \mathrm{false}\\}$        | $[\mathrm{true}: 1\rightarrow\Omega]$ |

そして、(驚くべき事ではあるが)初等トポスは有限余完備でもある。
この定理の証明は非常に困難な道のりを辿るので、本章末尾に記載することにするが、ここではその雰囲気のみ紹介する。もし、初等トポス $\mathcal{C}$ が有限余完備であるならば、 {{< refer prop.ccc-is-distributive >}} より分配圏となるので、例えば

$$ \Omega^{a+b}\simeq \Omega^a \times \Omega^b$$

といった同型が存在する。この右辺はカルテシアン閉圏では任意の$a,b$ に対して必ず存在するので、逆に

$$ \Omega^x \simeq \Omega^a \times \Omega ^b $$

を満たす $x$ として $x$ を定めることで $a+b$ を定義できそうに思われる。
より一般化すると関手 $\Omega^{(-)}: \mathcal{C}^{\mathrm{op}}\rightarrow\mathcal{C}$ の性質を用いる事が出来そうであるが、実際の証明は大変複雑である。本章最終節にてこの証明を記載する。

## 層

**前層(presheaf)** 及び **層(sheaf)** は元々、位相空間の上に紐づけられた数学対象を研究する道具として生まれた概念であるが、その圏論的一般化は非常に重要である。

### 前層

{{% definition title="前層" %}}
小圏 $\mathcal{C}$ の上の **前層(presheaf)** とは反変関手 $\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ の事である。

また、前層を対象とする関手圏 $\hat{\mathcal{C}}$ を **前層の圏(category of preshaves)** といい $\mathrm{PSh}(\mathcal{C})$ と書く。
{{% /definition %}}

前層の圏はとても良い性質を持つ。

{{% proposition %}}
前層の圏は双完備である。
{{% /proposition %}}

これは以下の定理と $\mathbf{Set}$ が双完備であることから示される。

{{% theorem title="関手圏の極限は点別計算可能定理" label="th.limits-of-functor-categories" %}}
図式 $F:\mathcal{J}\rightarrow\mathcal{D}^{\mathcal{C}}$ について
$a\in \mathcal{C}$ に固定した関手 $F(-)(a):\mathcal{J}\rightarrow\mathcal{D} $ の極限 $\varprojlim\_{i\in\mathcal{J}} F(i)(a)$ が全ての $a\in\mathcal{C}$ について存在するならば、$F$ の極限も存在し

$$ \left(\varprojlim\_{i\in\mathcal{J}} F(i)\right)(a) \simeq \varprojlim\_{i\in\mathcal{J}} F(i)(a) $$

である。余極限についても同様。
{{% /theorem %}}

{{% details 証明 %}}

全ての $a\in\mathcal{C}$ について $\varprojlim\_{i\in\mathcal{J}} F(i)(a)$ が存在するとする。
$\mathcal{J}$ の射 $f: i\rightarrow j$ に対応する自然変換 $F(f):F(i)\rightarrow F(j)$ を $\mathcal{C}$ の射 $u: a\rightarrow b$ についてcomponent-wiseに描くと以下のようになり、これが全ての $f:i\rightarrow j$ と $u:a\rightarrow b$ について可換となる。

$$ \xymatrix{
F(i)(a) \ar[d]\_{F(f)_a} \ar[r]^{F(i)(u)}  & F(i)(b) \ar[d]^{F(f)_b} \\\\
F(j)(a)                  \ar[r]\_{F(j)(u)} & F(j)(b)
}$$

ここで $\varprojlim\_{i\in\mathcal{J}} F(i)(a)$ が存在するので、下図のような極限錐がそれぞれ存在する。

$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F(i)(a) \ar[rd] \ar@/_1pc/[rdd] &&& \varprojlim\_{i\in\mathcal{J}}F(i)(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F(i)(a) \ar[d]\_{F(f)_a} \ar[r]^{F(i)(u)} & F(i)(b) \ar[d]^{F(f)_b}& \\\\
& F(j)(a)                  \ar[r]\_{F(j)(u)} & F(j)(b)                &
}$$

ここで $\varprojlim\_{i\in\mathcal{J}}F(i)(a)$ の錐の側面に各 $F(i)(u)$ (図の水平の射) を合成したものは $F(-)(b):\mathcal{J}\rightarrow\mathcal{D}$ への錐となるので、下図が可換となる射 $\bar{u}: \varprojlim\_{i\in\mathcal{J}}F(i)(a)\rightarrow\varprojlim\_{i\in\mathcal{J}}F(i)(b)$ が唯一つ存在。

$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F(i)(a) \ar[rd] \ar@/_1pc/[rdd] \ar@{.>}[rrr]^{\bar{u}} &&& \varprojlim\_{i\in\mathcal{J}}F(i)(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F(i)(a) \ar[d]\_{F(f)_a} \ar[r]^{F(i)(u)} & F(i)(b) \ar[d]^{F(f)_b}& \\\\
& F(j)(a)                  \ar[r]\_{F(j)(u)} & F(j)(b)                &
}$$

そこで、$\mathcal{C}$ の各対象 $a$ に $\varprojlim\_{i\in\mathcal{J}}F(i)(a)$ を、射 $u:a\rightarrow b$ に $\bar{u}$ を対応させる関係を考えるとこれは関手 $G: \mathcal{C}\rightarrow\mathcal{D}$ となる。これが $\varprojlim\_{i\in\mathcal{J}}F(i)$ である事を示す。

そこで任意の $H:\mathcal{C}\rightarrow\mathcal{D}$ から $F$ への錐を考える。
$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F(i)(a) \ar[rd] \ar@/_1pc/[rdd] \ar@{.>}[rrr]^{\bar{u}} &&& \varprojlim\_{i\in\mathcal{J}}F(i)(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F(i)(a) \ar[d]\_{F(f)_a} \ar[r]^{F(i)(u)} & F(i)(b) \ar[d]^{F(f)_b}& \\\\
& F(j)(a)                  \ar[r]\_{F(j)(u)} & F(j)(b)                & \\\\
H(a) \ar[ru] \ar@/^1pc/[ruu] \ar[rrr]^{H(u)} &&& H(b) \ar[lu] \ar@/_1pc/[luu]
}$$

この左側だけに注目すると $\varprojlim_{i\in\mathcal{J}}$ についての普遍性より以下を可換にする射 $H(a)\rightarrow\varprojlim_{i\in\mathcal{J}}F(i)(a)$ が一意に存在。右側も同様。

$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F(i)(a) \ar[rd] \ar@/_1pc/[rdd] \ar@{.>}[rrr]^{\bar{u}} &&& \varprojlim\_{i\in\mathcal{J}}F(i)(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F(i)(a) \ar[d]\_{F(f)_a} \ar[r]^{F(i)(u)} & F(i)(b) \ar[d]^{F(f)_b}& \\\\
& F(j)(a)                  \ar[r]\_{F(j)(u)} & F(j)(b)                & \\\\
H(a) \ar[ru] \ar@/^1pc/[ruu] \ar@{.>}[uuu] \ar[rrr]^{H(u)} &&& H(b) \ar[lu] \ar@/_1pc/[luu] \ar@{.>}[uuu]
}$$

この射の族 $\\{H(a)\rightarrow\varprojlim_{i\in\mathcal{J}}F(i)(a)\\}$ は自然変換 $H\rightarrow G$ となり、これが一意であるので $G\simeq \varprojlim\_{i\in\mathcal{J}}F(i)$ である。$\square$
{{% /details %}}

この定理を、評価関手というものを用いて言い直すこともできる。

{{% definition title="点での評価関手" %}}
対象 $a\in\mathcal{D}$ を固定した時に、 $F: \mathcal{C}\rightarrow\mathcal{D}$ に $a$ を "代入" する操作$\mathrm{ev}\_a$ は関手 $\mathcal{D}^{\mathcal{C}}\rightarrow\mathcal{D}$ となる。
$$\mathrm{ev}\_a: \mathcal{D}^{\mathcal{C}}\ni (F\xrightarrow{\phi}G) \longmapsto (F(a)\xrightarrow{\phi_a}G(a))\in\mathcal{D}$$
これを **点 $a$ での評価関手(evaluation functor at point $a$)** という。
{{% /definition %}}

関手圏の極限の点別計算可能定理より以下が成り立つ。

{{% proposition %}}
点での評価関手は極限を保つ。
$$ \mathrm{ev}\_a\left(\varprojlim F\right)\simeq \varprojlim \mathrm{ev}\_a\circ F $$
{{% /proposition %}}

{{% proposition %}}
前層 $p,q:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ に対する指数対象は
$$ q^p = \hat{\mathcal{C}}(\mathcal{Y}(-)\times p, q) $$
であり常に存在する。従って $\mathrm{PSh}(\mathcal{C})$ はカルテシアン閉圏である。
{{% /proposition %}}
もし $q^p$ が存在するならば、米田の補題と指数対象の性質より、任意の $a\in\mathcal{C}$ に対して自然な同型
$$ q^p(a) \simeq \hat{\mathcal{C}}(\mathcal{Y}(a), q^p)\simeq\hat{\mathcal{C}}(\mathcal{Y}(a)\times p, q)$$
が存在する。従って
$$ q^p = \hat{\mathcal{C}}(\mathcal{Y}(-)\times p, q)$$
である事が必要である事が分かる。
{{% details 証明 %}}
$$ q^p = \hat{\mathcal{C}}(\mathcal{Y}(-)\times p, q)$$
とおく。また
$$ \mathrm{ev}\_a: \hat{\mathcal{C}}(\mathcal{Y}(a)\times p, q)\times p(a) \ni (\phi, x)\longmapsto \phi_a(1_a, x) \in q(a) $$
とおく。ここで $\\{\mathrm{ev}\_a\\}$ は自然変換 $\mathrm{ev}:q^p\times p\rightarrow q$ となっている。何故ならば任意の $f:b\rightarrow a$ に対して

$$ \xymatrix{
\hat{\mathcal{C}}(\mathcal{Y}(a)\times p, q)\times p(a) \ar[d]\_{(-\circ (\mathcal{Y}(f)\times 1_p))\times p(f)} \ar[r]^-{\mathrm{ev}\_a} & q(a) \ar[d]^{q(f)} \\\\
\hat{\mathcal{C}}(\mathcal{Y}(b)\times p, q)\times p(b)        \ar[r]^-{\mathrm{ev}\_b} & q(b) \\\\
} $$

の右側を辿ると
$$ (\phi, x) \longmapsto \phi_a(1_a, x) \longmapsto q(f)(\phi_a(1_a, x)) $$
左側を辿ると
$$ (\phi, x) \longmapsto (\phi\circ(\mathcal{Y}(f)\times 1_p), p(f)(x)) \longmapsto \phi_b\circ ((f\circ -)\times 1\_{p(b)})(1_b, p(f)(x)) = \phi_b(f, p(f)(x)) $$
となる。ここで $\phi:\mathcal{Y}(a)\times p\rightarrow q$ は自然変換であるから、以下が可換となる。
$$ \xymatrix{
\mathcal{C}(a, a)\times p(a) \ar[d]\_{(-\circ f)\times p(f)} \ar[r]^-{\phi_a} & q(a) \ar[d]^{q(f)} \\\\
\mathcal{C}(b, a)\times p(b)                                 \ar[r]^-{\phi_b} & q(b)
}$$ 
よって$\phi_b(f, p(f)(x)) = q(f)(\phi_a(1_a, x))$ である。従って $\mathrm{ev}$ についての図式は可換であるから、 $\mathrm{ev}: q^p\times p\rightarrow q$ は自然変換である。

最後に以上で定義された $q^p$ と $\mathrm{ev}: q^p\times p\rightarrow q$ が指数対象の普遍性、すなわち任意の $r: \mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ と $v: r\times p\rightarrow q$ に対して
以下が可換となるような $u: r\rightarrow q^p$ がただ一つ存在することを示す。
$$\xymatrix{
r\times p \ar[d]\_{u\times 1_p} \ar[rd]^{v} & \\\\
q^p\times p \ar[r]^{\mathrm{ev}} & q
}$$
(TBD)
{{% /details %}}

### 層
前層の圏はトポスであるのだが、その前準備として **層(sieve)** を導入する。

{{% definition title="層" %}}
小圏 $\mathcal{C}$ の対象 $c$ をコドメインとする射の集合 $S$ が、任意の $f\in S$ と $f\circ g$ が定義される $g$ について $f\circ g\in S$ である時 (すなわち、右への合成について閉じている時)、これを $c$ 上の **層(sieve)** という。
{{% /definition %}}

(TBD)

{{% proposition %}}
部分対象の集合 $\mathrm{Sub}(a)$ は順序 $\leq$ に対して最大値をもち、その最大値は $[1_a]$ である。
{{% /proposition %}}
{{% details 証明 %}}
まず $1_a: a\rightarrow a$ は(左簡約可能であるから)モノ射なので $[1_a] \in\mathrm{Sub}(a)$ である。そして、任意のモノ射 $m: x\hookrightarrow a$ に対して、以下が可換であるから $[m]\leq[1_a]$ である。 $\square$
$$\xymatrix{
              & a &          \\\\
x \ar[ru]^m \ar[rr]^m & & a \ar[lu]\_{1_a}
}$$
{{% /details %}}

{{% proposition %}}
前層の圏はトポスである。

部分対象分類子 $\Omega$ は
$$\Omega = \mathrm{Sub}(\mathcal{Y}(-))$$
であり、射(自然変換) $\mathrm{true}:1 \rightarrow \Omega$ は
$$ \mathrm{true}\_c(\ast) = \max\_{\leq}\Omega(c) = [1\_{\mathcal{Y}(c)}]$$
である。
{{% /proposition %}}
{{% details 証明 %}}
まず、$\hat{\mathcal{C}}$ の終対象 $1:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ は点別に計算できるので、任意の $c\in\mathcal{C}$ について $1(c)$ は $\mathbf{Set}$ の終対象である。そこで
$$ 1(c) = \\{\ast\\}$$
とおく。

部分対象分類子 $\Omega$ が存在するならば、米田の補題より
$$ \Omega(c) \simeq \hat{\mathcal{C}}(\mathcal{Y}(c),\Omega) $$
であり、 $\hat{\mathcal{C}}(\mathcal{Y}(c),\Omega) \simeq \mathrm{Sub}(\mathcal{Y}(c))$ であるから、$\Omega=\mathrm{Sub}(\mathcal{Y}(-))$ でなければならない事が分かる。

実際に $\Omega$ が部分対象分類子である事を示す為には、任意のモノ射 $m:A\hookrightarrow U$ に対して以下が引き戻しとなるような射 $\chi: U\rightarrow \Omega$ が唯一つ存在する事を示せば良い。
$$\xymatrix{
A \ar[r] \ar@{^{(}->}[d]\_{m} & 1 \ar[d]^{\mathrm{true}} \\\\
U \ar[r]^{\chi} & \Omega
}$$
すなわち、引き戻しは点別に計算できるので、各 $c\in\mathcal{C}$ について
$$\xymatrix{
A(c) \ar[r] \ar@{^{(}->}[d]\_{m_c} & \\{\ast\\} \ar[d]^{\mathrm{true}\_c} & \\\\
U(c) \ar[r]^-{\chi_c} & \mathrm{Sub}(\mathcal{Y}(c))    & \text{in $\mathbf{Set}$}
}$$
が引き戻しとなるような $\chi_c$ が一意である事を示せば良い。

$$ \chi_c\circ m_c = [1\_{\mathcal{Y}(c)}] $$

{{% /details %}}

## ハイティング代数

トポスは **直観主義論理(Intuitionistic Logic)** のモデルとしての構造をもつ。
具体的には、ブール代数を一般化した概念である **ハイティング代数(Heyting algebra)** の構造をもつ。トポスとの具体的な関わりについては後の章で説明するが、ここではハイティング代数の基本を紹介する。

### ハイティング代数

すでに述べたが、対象 $a,b$ の間に射が高々一つしかない圏 $\mathcal{C}$ を **半順序集合(partially ordered set, poset)** という。射$a\rightarrow b$ を $a\leq b$ と書くと、半順序集合の公理

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
- **冪等則(idempotent law)** : $a\wedge a = a\vee a = a$
{{% /proposition %}}
{{% details 証明 %}}
交換則・吸収則は有限積・余積について一般に成り立つ性質であるので、吸収則と冪等則について示す。

$a\leq a$ と $a\leq a\vee b$ より $a\leq a\wedge(a\vee b)$ である。これと $a\wedge(a\vee b)\leq a$ より $a\wedge(a\vee b)=a$。もう一方も同様。

また、吸収則において $b=a\wedge a$とおけば
$ a\wedge(a\vee(a\wedge a)) = a$ が成り立つので、この括弧内に吸収則を用いて $a\wedge a = a$。もう一方も同様。$\square$
{{% /details %}}

{{% definition title="ハイティング代数" %}}
圏 $\mathcal{H}$ が有界束でありかつカルテシアン閉圏である時、これを **ハイティング代数(Heyting algebra)** という。

指数対象 $b^a$ を $a\Rightarrow b$ と書く。
また、$a\Rightarrow\bot$ を $a$ の **擬似補(pseudo complement)** といい $\neg a$ と書く。
{{% /definition %}}

指数対象とは、$b,c$ について自然な同型
$ \mathcal{H}(c\wedge a, b) \simeq \mathcal{H}(c, a\Rightarrow b) $
が存在するものであったが、$\mathcal{H}$ においては両辺とも射は1つしかないので
$c\wedge a \leq b$ と $c\leq (a\Rightarrow b)$ が同値となるような対象のことである。

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
$\square$
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
である。$\square$
{{% /details %}}

{{% example %}}
位相空間 $X$ の開集合系 $\mathcal{O}(X)$ を包含関係によって半順序集合と見なしたものはハイティング代数となる。
{{% /example %}}

開集合系の公理から有界束である事がすぐ分かる。そして開集合 $U,V$ に対して
$U\cap W\subseteq V$ を満たす全ての開集合 $W$ の合併が指数対象 $V^U$ となる。そのような合併の存在は開集合の公理から保証される。

また、開集合 $U$ の擬似補は $U\cap W\subseteq\emptyset$ すなわち $U$ と交わらない全ての開集合 $W$ の和集合となる。

### ブール代数

ハイティング代数のうち、 排中律を満たすものをブール代数という。
古典論理の意味論に用いられものがブール代数である。

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
&\neg\neg a= \neg\neg a\wedge(\neg a\vee a)=(\neg\neg a\wedge \neg a)\vee (\neg\neg a\wedge a) =\bot\vee(\neg\neg a\wedge a) \\\\
&= (\neg a\wedge a)\vee(\neg\neg a\wedge a) = (\neg a\vee \neg\neg a)\wedge a= \top\wedge a = a
\end{align\*}
$\square$
{{% /details %}}

{{% proposition %}}
ブール代数において、ド・モルガンの法則が成り立つ。
$$\neg a\wedge \neg b = \neg(a \vee b)$$
$$\neg a\vee \neg b = \neg(a \wedge b)$$
{{% /proposition %}}
{{% details 証明 %}}
1つ目はハイティング代数である事から成立。2つ目は二重否定除去則を使って
$$ \neg a\vee\neg b = \neg\neg(\neg a\vee\neg b) = \neg(\neg\neg a\wedge\neg\neg b) = \neg(a\wedge b)$$
$\square$
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
である。$\square$
{{% /details %}}

