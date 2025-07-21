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

$\mathbf{Set}$ における対象 $a$ の部分対象全体と $a$の部分集合全体は一対一に対応する。すなわち、部分対象 $m$ に対応する部分集合とは関数 $m$ の像であり、部分対象の順序 $\leq$ は部分集合の包含関係 $\subseteq$ と対応する。また $\mathbf{Set}$ は冪化可能である。

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
$p$ を $b$ の $f$ に沿った引き戻し、 $\bar{g}$ を  $g$ の $f$ に沿った引き戻しと言い、それぞれ $f^\ast b$ や $f^\ast g$ と書く。
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

## 前層の圏

部分分類対象子を持つ条件は非常に厳しく、ほとんどの圏はトポスにならないが **前層(presheaf)** の圏はトポスでありかつ重要な例である。
これらは元々、位相空間の上に紐づけられた数学対象を研究する道具として生まれた概念である。位相空間上の層については次章で説明する。

{{% definition title="前層" %}}
小圏 $\mathcal{C}$ の上の **前層(presheaf)** とは反変関手 $\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ の事である。

また、前層を対象とする関手圏 $\hat{\mathcal{C}}$ を **前層の圏(category of preshaves)** といい $\mathrm{PSh}(\mathcal{C})$ と書く。
{{% /definition %}}

高階な圏であるので、 {{< refer def.functor-as-a-diagram >}} の考え方を用いて開いて考えよう。
まず前層 $F:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ は $\mathbf{Set}$ の中の $\mathcal{C}^{\mathrm{op}}$ の形の図式と同一視することが出来、前層の間の自然変換 $\phi: F\rightarrow G$ はこれら図式を(整合的に)繋ぐ射(関数)の集まりである。

$$\xymatrix{
F\_a \ar[d]^{\phi\_a} \ar[r] & F\_b \ar[r] \ar[d]^{\phi\_b} & F\_c \ar[d]^{\phi\_c}\\\\
G\_a                  \ar[r] & G\_b \ar[r]                  & G\_c
\ar@{.}(-5,7);(47,7)
\ar@{.}(47,7);(47,-5)
\ar@{.}(47,-5);(-5,-5)
\ar@{.}(-5,-5);(-5,7)
\ar@{.}(-5,-13);(47,-13)
\ar@{.}(47,-13);(47,-25)
\ar@{.}(47,-25);(-5,-25)
\ar@{.}(-5,-25);(-5,-13)
}$$

特に $\mathcal{C}=\mathbf{1}$ の場合はこれは $\mathbf{Set}$ そのものであり、 $\mathrm{PSh}(\mathcal{C})$ は $\mathbf{Set}$ を自然に一般化した概念である。
これが $\mathbf{Set}$ と同様の性質を持つことは容易に想像できるであろう。今後の定理とその証明にあたってもこのイメージを持っていると読みやすくなるだろう。

では、前層の圏が初等トポスである事を示すために、有限完備であること、カルテシアン閉であること、部分対象分類子を持つことを順に示す。

### 完備性

{{% proposition %}}
前層の圏は双完備である。
{{% /proposition %}}

従って、当然、有限完備である。これは以下の定理と $\mathbf{Set}$ が双完備であることから示される。

{{% theorem title="関手圏の極限の点別計算定理" label="th.limits-of-functor-categories" %}}
図式 $F:\mathcal{J}\rightarrow\mathcal{D}^{\mathcal{C}}$ について
$a\in \mathcal{C}$ に固定した関手 $F\_{(-)}(a):\mathcal{J}\rightarrow\mathcal{D} $ の極限 $\displaystyle\varprojlim\_{i\in\mathcal{J}} F\_i(a)$ が全ての $a\in\mathcal{C}$ について存在するならば、$F$ の極限も存在し

$$ \left(\varprojlim\_{i\in\mathcal{J}} F\_i\right)(a) \simeq \varprojlim\_{i\in\mathcal{J}} F\_i(a) $$

である。余極限についても同様。
{{% /theorem %}}

一見して分かりにくいが、これも同様に開いて考えれば難しくない。下図赤線で囲った部分のように、各対象ごとに個別に極限を求めたものが、関手圏の極限と一致するという定理である。

$$\xymatrix{
\varprojlim\_{i\in\mathcal{J}}F\_i(a) \ar[d] \ar[r] & \varprojlim\_{i\in\mathcal{J}} F\_i(b) \ar[r] \ar[d] & \varprojlim\_{i\in\mathcal{J}} F\_i(c) \ar[d] & =\quad \varprojlim\_{i\in\mathcal{J}}F\_i \\\\
F\_i(a) \ar[d] \ar[r] & F\_i(b) \ar[r] \ar[d] & F\_i(c) \ar[d] & \\\\
F\_j(a)        \ar[r] & F\_j(b) \ar[r]        & F\_j(c)        &
\ar@{.}(-15,7);(95,7)
\ar@{.}(95,7);(95,-7)
\ar@{.}(95,-7);(-15,-7)
\ar@{.}(-15,-7);(-15,7)
\ar@{.}(-15,-15);(95,-15)
\ar@{.}(95,-15);(95,-28)
\ar@{.}(95,-28);(-15,-28)
\ar@{.}(-15,-28);(-15,-15)
\ar@{.}(-15,-37);(95,-37)
\ar@{.}(95,-37);(95,-50)
\ar@{.}(95,-50);(-15,-50)
\ar@{.}(-15,-50);(-15,-37)
\ar@\[red\]@{.}(-17,9);(15,9)
\ar@\[red\]@{.}(15,9);(15,-52)
\ar@\[red\]@{.}(15,-52);(-17,-52)
\ar@\[red\]@{.}(-17,-52);(-17,9)
}$$

{{% details 証明 %}}

全ての $a\in\mathcal{C}$ について $\varprojlim\_{i\in\mathcal{J}} F\_i(a)$ が存在するとする。
$\mathcal{J}$ の射 $f: i\rightarrow j$ に対応する自然変換 $F\_f:F\_i\rightarrow F\_j$ を $\mathcal{C}$ の射 $u: a\rightarrow b$ についてcomponent-wiseに描くと以下のようになり、これが全ての $f:i\rightarrow j$ と $u:a\rightarrow b$ について可換となる。

$$ \xymatrix{
F\_i(a) \ar[d]\_{F\_f(a)} \ar[r]^{F\_i(u)}  & F\_i(b) \ar[d]^{F\_f(b)} \\\\
F\_j(a)                  \ar[r]\_{F\_j(u)} & F\_j(b)
}$$

ここで $\varprojlim\_{i\in\mathcal{J}} F\_i(a)$ が存在するので、下図のような極限錐がそれぞれ存在する。

$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F\_i(a) \ar[rd] \ar@/_1pc/[rdd] &&& \varprojlim\_{i\in\mathcal{J}}F\_i(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F\_i(a) \ar[d]\_{F\_f(a)} \ar[r]^{F\_i(u)} & F\_i(b) \ar[d]^{F\_f(b)}& \\\\
& F\_j(a)                  \ar[r]\_{F\_j(u)} & F\_j(b)                &
}$$

ここで $\varprojlim\_{i\in\mathcal{J}}F\_i(a)$ の錐の側面に各 $F\_i(u)$ (図の水平の射) を合成したものは $F(-)(b):\mathcal{J}\rightarrow\mathcal{D}$ への錐となるので、下図が可換となる射 $\bar{u}: \varprojlim\_{i\in\mathcal{J}}F\_i(a)\rightarrow\varprojlim\_{i\in\mathcal{J}}F\_i(b)$ が唯一つ存在。

$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F\_i(a) \ar[rd] \ar@/_1pc/[rdd] \ar@{.>}[rrr]^{\bar{u}} &&& \varprojlim\_{i\in\mathcal{J}}F\_i(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F\_i(a) \ar[d]\_{F\_f(a)} \ar[r]^{F\_i(u)} & F\_i(b) \ar[d]^{F\_f(b)}& \\\\
& F\_j(a)                  \ar[r]\_{F\_j(u)} & F\_j(b)                &
}$$

そこで、$\mathcal{C}$ の各対象 $a$ に $\varprojlim\_{i\in\mathcal{J}}F\_i(a)$ を、射 $u:a\rightarrow b$ に $\bar{u}$ を対応させる関係を考えるとこれは関手 $G: \mathcal{C}\rightarrow\mathcal{D}$ となる。これが $\varprojlim\_{i\in\mathcal{J}}F\_i$ である事を示す。

そこで任意の $H:\mathcal{C}\rightarrow\mathcal{D}$ から $F$ への錐を考える。
$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F\_i(a) \ar[rd] \ar@/_1pc/[rdd] \ar@{.>}[rrr]^{\bar{u}} &&& \varprojlim\_{i\in\mathcal{J}}F\_i(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F\_i(a) \ar[d]\_{F\_f(a)} \ar[r]^{F\_i(u)} & F\_i(b) \ar[d]^{F\_f(b)}& \\\\
& F\_j(a)                  \ar[r]\_{F\_j(u)} & F\_j(b)                & \\\\
H(a) \ar[ru] \ar@/^1pc/[ruu] \ar[rrr]^{H(u)} &&& H(b) \ar[lu] \ar@/_1pc/[luu]
}$$

この左側だけに注目すると $\varprojlim_{i\in\mathcal{J}}$ についての普遍性より以下を可換にする射 $H(a)\rightarrow\varprojlim_{i\in\mathcal{J}}F\_i(a)$ が一意に存在。右側も同様。

$$ \xymatrix{
\varprojlim\_{i\in\mathcal{J}}F\_i(a) \ar[rd] \ar@/_1pc/[rdd] \ar@{.>}[rrr]^{\bar{u}} &&& \varprojlim\_{i\in\mathcal{J}}F\_i(b) \ar[ld] \ar@/^1pc/[ldd] \\\\
& F\_i(a) \ar[d]\_{F\_f(a)} \ar[r]^{F\_i(u)} & F\_i(b) \ar[d]^{F\_f(b)}& \\\\
& F\_j(a)                  \ar[r]\_{F\_j(u)} & F\_j(b)                & \\\\
H(a) \ar[ru] \ar@/^1pc/[ruu] \ar@{.>}[uuu] \ar[rrr]^{H(u)} &&& H(b) \ar[lu] \ar@/_1pc/[luu] \ar@{.>}[uuu]
}$$

この射の族 $\left\\{H(a)\rightarrow\varprojlim_{i\in\mathcal{J}}F\_i(a)\right\\}$ は自然変換 $H\rightarrow G$ となり、これが一意であるので $G\simeq \varprojlim\_{i\in\mathcal{J}}F\_i$ である。$\square$
{{% /details %}}

この定理を、評価関手というものを用いて言い直すこともできる。

{{% definition title="点での評価関手" %}}
対象 $a\in\mathcal{D}$ を固定した時に、 $F: \mathcal{C}\rightarrow\mathcal{D}$ に $a$ を "代入" する操作$\mathrm{ev}\_a$ は関手 $\mathcal{D}^{\mathcal{C}}\rightarrow\mathcal{D}$ となる。
$$\mathrm{ev}\_a: \mathcal{D}^{\mathcal{C}}\ni (F\xrightarrow{\phi}G) \longmapsto (F(a)\xrightarrow{\phi_a}G(a))\in\mathcal{D}$$
これを **点 $a$ での評価関手(evaluation functor at point $a$)** という。
{{% /definition %}}

関手圏の極限の点別計算定理より以下が成り立つ。

{{% proposition %}}
点での評価関手は極限を保つ。
$$ \mathrm{ev}\_a\left(\varprojlim F\right)\simeq \varprojlim \mathrm{ev}\_a\circ F $$
{{% /proposition %}}

### 指数対象

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
$x: \mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ について自然な同型
$\hat{\mathcal{C}}(x\times p, q) \simeq\hat{\mathcal{C}}(x, q^p)$
の成立を示せば良い。{{< refer th.density-theorem >}}より適当な図式 $d:\mathcal{J}\rightarrow\mathcal{C}$ が存在して
$ x = \varinjlim\_{i\in\mathcal{J}}\mathcal{Y}(d_i)$
と書けるので、これと {{< refer prop.yoneda-preserves-limits >}}の双対版、米田の補題を用いて
$$\begin{aligned}
\hat{\mathcal{C}}(x, q^p) &\simeq \hat{\mathcal{C}}\left(\varinjlim\_{i\in\mathcal{J}}\mathcal{Y}(d_i), q^p\right)\simeq\varprojlim\_{i\in\mathcal{J}} \hat{\mathcal{C}}(\mathcal{Y}(d_i), q^p)
\simeq \varprojlim\_{i\in\mathcal{J}} q^p(d_i) = \varprojlim\_{i\in\mathcal{J}}\hat{\mathcal{C}}(\mathcal{Y}(d_i)\times p, q) \\\\
&\simeq \hat{\mathcal{C}}\left(\varinjlim\_{i\in\mathcal{J}}\mathcal{Y}(d_i)\times p, q\right) = \hat{\mathcal{C}}(x\times p, q)
\end{aligned}$$
$\square$
{{% /details %}}

特別な場合として $\mathcal{C}=\mathbf{1}$ の場合を考えてみると、$\mathcal{C}(p, q)$ と一致する事が分かる。

### 篩(ふるい)

$\mathrm{PSh}(\mathcal{C})$ が部分分類対象子 $\Omega:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ を持つとすると、米田の補題より任意の $a\in\mathcal{C}$ に対して
$$ \Omega(a)\simeq \hat{\mathcal{C}}(\mathcal{Y}(a), \Omega) $$
となる。そして、 $\Omega$ は $\mathrm{Sub}$ を表現する対象なのであるから、任意の $x:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ に対して
$$ \hat{\mathcal{C}}(x, \Omega)\simeq\mathrm{Sub}(x)$$
でなければならない。従って、これらを組み合わせて$ \Omega(a)\simeq \mathrm{Sub}(\mathcal{Y}(a))$ すなわち
$$ \Omega \simeq \mathrm{Sub}(\mathcal{Y}(-)) $$
でなければならない。

ここで登場した表現可能関手の部分対象の集合 $\mathrm{Sub}(\mathcal{Y}(a)) = \mathrm{Sub}(\mathcal{C}(-, a))$ は
 **コドメインが$a$である射**  からなる何らかの集合と同一視できそうである。これを **ふるい(sieve)** という。漢字では篩と書く。

{{% definition title="篩(ふるい)" %}}
小圏 $\mathcal{C}$ の対象 $a$ をコドメインとする射の集合 $S$ が、任意の $f\in S$ と $f\circ g$ が定義される $g$ について $f\circ g\in S$ である時 (前合成、precomposition について閉じている時)、これを $a$ 上の **篩(ふるい, sieve)** という。
{{% /definition %}}

篩の具体例をいくつか見てみる。例えば以下のような圏において
$$\xymatrix{ a \ar[r]^f & b } $$
$a$ 上の篩は $\emptyset, \\{1_a\\}$ の2つ。 $b$ 上の篩は $\emptyset, \\{f\\}, \\{1_b, f\\}$ の3つである。


位相空間 $X$ の開集合を対象とし、開集合の包含関係 $V\subseteq U$ を射 $V\rightarrow U$ とすると圏となる。
この圏における開集合 $U$ 上の篩 $S$ とはどのようなものか考えると、$(V\rightarrow U)\in S$ であるならば、
任意の $W\subseteq V$ である $W$ に対して $(W\rightarrow U)\in S$ となるような集合が $S$ である。
この例で言うと、$U$ に含まれる開集合を $V$ に含まれるという条件でふるいにかけている、ようなイメージである。
{{% tikz %}}
  \usetikzlibrary{arrows,patterns}
  \begin{tikzpicture}
  \tikzset{filledcircle/.style={draw, circle, fill=gray, minimum size=1.5cm, inner sep=0pt}}

  % Draw outer set X
  \draw[thick] (0,0) ellipse (4cm and 3cm);
  \node at (3.5,2.5) {$X$};

  % Draw inner set U
  \draw[thick] (-1,0) ellipse (2.5cm and 2cm);
  \node at (1,1.8) {$U$};

  % Draw sets V and W inside U
  \node[filledcircle,label=center:$V$] (V) at (-1,0) {};

  \end{tikzpicture}
{{% /tikz %}}


定義より明らかに以下が成立する。
{{% proposition label="prop.maximal-sieve" %}}
小圏 $\mathcal{C}$ の対象 $a$ について $a$上の篩全ての集合は半順序集合となり、これは最大値を持つ。最大の篩は $1_a$ を含むものである。
{{% /proposition %}}


{{% proposition label="prop.subfunctor-of-yoneda" %}}
小圏 $\mathcal{C}$ の対象 $a$ について $\mathrm{Sub}(\mathcal{Y}(a))$ は $a$ 上の篩全ての集合と半順序集合として同型
{{% /proposition %}}
{{% details 証明 %}}
$[m: F\hookrightarrow \mathcal{Y}(a)] \in \mathrm{Sub}(\mathcal{Y}(a))$ に対して、
$$ S_m = \bigcup\_{x\in\mathcal{C}}\mathrm{Im}(m_x) $$
と定める。まず、これが同値類の代表元 $m$ の選び方によらない事を示す。
$m: F\hookrightarrow\mathcal{Y}(a)$ と $n: G\hookrightarrow\mathcal{Y}(a)$ が同値だとすると、自然同型 $\phi: F\rightarrow G$ が存在して
以下が可換。

$$\xymatrix{
    & \mathcal{Y}(a) &       \\\\
F \ar@{^{(}->}[ru]^m \ar[rr]^{\phi} & & G \ar@{^{(}->}[lu]\_n
}$$

従って、以下が可換で $\phi_x$ は全単射。

$$\xymatrix{
    & \mathcal{C}(x, a) &       \\\\
F(x) \ar@{^{(}->}[ru]^{m_x} \ar[rr]^{\phi_x} & & G(x) \ar@{^{(}->}[lu]\_{n_x}
}$$

よって $\mathrm{Im}(m_x) = \mathrm{Im}(n_x)$ であるから $S_m$ は $m$ の選び方によらない。

続いて、 $S_m$ がふるいである事を示す。任意の $(f:x\rightarrow a)\in S_m$ と $g:y\rightarrow x$ をとる。
$m$ は自然変換であるから以下が可換である。
$$\xymatrix{
F(x) \ar[r]^-{m_x} \ar[d]\_{F(g)} & \mathcal{C}(x, a) \ar[d]^{-\circ g} \\\\
F(y) \ar[r]^-{m_y}               & \mathcal{C}(y, a)
}$$
$f$ は $\mathrm{Im}(m_x)$ の元であるから、適当な $z\in F(x)$ が存在して $f = m_x(z)$。よって図式を辿ると
$$ f\circ g = m_y(F(g)(z)) $$
であるから、 $f\circ g\in \mathrm{Im}(m_y)$。従って $f\circ g\in S_m$ であるから $S_m$ は篩である。$\square$

{{% /details %}}

### 部分対象分類子

{{% proposition %}}
前層の圏はトポスである。部分対象分類子は $\Omega = \mathrm{Sub}(\mathcal{Y}(-))$
であり、射(自然変換) $\mathrm{true}:1 \rightarrow \Omega$ は $ \mathrm{true}\_c(\ast) = \max\Omega(c)$
である。また、モノ射 $m: A\hookrightarrow U$ に対応する分類射 $\chi: U\rightarrow\Omega$ は
$$\chi_c(x) = \\{f: a \rightarrow c \mid U(f)(x) \in \mathrm{Im}(m_a) \\}$$
で与えられる。

$$\xymatrix{
A \ar[r] \ar@{^{(}->}[d]\_{m} & 1 \ar[d]^{\mathrm{true}} \\\\
U \ar[r]^{\chi} & \Omega
}$$

{{% /proposition %}}

{{% details 証明 %}}
まず、$\hat{\mathcal{C}}$ の終対象 $1:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ は点別に計算できるので、任意の $c\in\mathcal{C}$ について $1(c)$ は $\mathbf{Set}$ の終対象である。そこで $ 1(c) = \\{\ast\\}$ とおく。

$\Omega$ が部分対象分類子である事を示す為には、任意のモノ射 $m:A\hookrightarrow U$ に対して以下が引き戻しとなるような射 $\chi: U\rightarrow \Omega$ が唯一つ存在する事を示せば良い。
$$\xymatrix{
A \ar[r] \ar@{^{(}->}[d]\_{m} & 1 \ar[d]^{\mathrm{true}} \\\\
U \ar[r]^{\chi} & \Omega
}$$
すなわち、{{< refer th.limits-of-functor-categories >}}より、各 $c\in\mathcal{C}$ について
$$\xymatrix{
A(c) \ar[r] \ar@{^{(}->}[d]\_{m_c} & \\{\ast\\} \ar[d]^{\mathrm{true}\_c} \\\\
U(c) \ar[r]^-{\chi_c} & \mathrm{Sub}(\mathcal{Y}(c))
}$$
が引き戻しとなるような $\chi_c$ が唯一つ存在する事を示せば良い。 $\mathbf{Set}$ であるので $\chi_c$ が満たす条件は
{{< refer prop.maximal-sieve >}} 及び {{< refer prop.subfunctor-of-yoneda >}} より
$$\begin{aligned}
A(c) &\simeq \\{x\in U(c) \mid \chi_c(x) = \max_{\leq}(\mathrm{Sub}(\mathcal{Y}(c))\\} \\\\
     & = \\{x \in U(c) \mid 1_c \in \chi_c(x)\\}
\end{aligned}$$
すなわち $A(c)\simeq \mathrm{Im}(m_c)$ であるので
$$ 1_c\in\chi_c(x) \Leftrightarrow x \in \mathrm{Im}(m_c)$$
である。ここで $\chi: U\rightarrow\Omega$ は自然変換であるから、任意の $f:a\rightarrow c$ に対して以下が可換となるから、左上に $x$ を取って$ \Omega(f)(\chi_c(x)) = \chi_a(U(f)(x)) $ が成り立つ。
$$\xymatrix{
U(c) \ar[r]^{U(f)} \ar[d]\_{\chi_c} & U(a) \ar[d]^{\chi_a} \\\\
\Omega(c) \ar[r]^{\Omega(f)} & \Omega(a)
}$$

ここで $\Omega(f)(\chi_c(x)) = \mathrm{Sub}(\mathcal{Y}(f))(\chi_c(x))$ は $\mathcal{Y}(c)$ の部分対象 $\chi_c(x)$ の $\mathcal{Y}(f)=f\circ -$ に沿った引き戻しであるから $ \Omega(f)(\chi_c(x)) = \\{g:b\rightarrow a \mid f\circ g\in\chi_c(x)\\}$ である。

$$\xymatrix{
\Omega(f)(\chi_c(x)) \ar[r] \ar[d] & \chi_c(x) \ar@{^{(}->}[d]^{\subseteq} \\\\
\mathcal{Y}(a) \ar[r]^{f\circ -} & \mathcal{Y}(c)
}$$

これから $f \in \chi_c(x) \Leftrightarrow 1_c \in \Omega(f)(\chi_c(x))$ である。

以上より

$$ f\in \chi_c(x) \Leftrightarrow 1_c\in \Omega(f)(\chi_c(x)) = \chi_a(U(f)(x)) \Leftrightarrow U(f)(x) \in \mathrm{Im}(m_a)$$

となるから

$$ \chi_c(x) = \\{ f: a\rightarrow c \mid U(f)(x) \in \mathrm{Im}(m_a) \\} $$

と分類射が一意に定まる。$\square$
{{% /details %}}

## ハイティング代数
以上、集合論的な操作が出来る圏としてのトポスを導入したが、今後はその上でどのような数学が展開できるのかを見ていく。

まず、トポスは **直観主義論理(Intuitionistic Logic)** のモデルとしての構造をもつ。
具体的には、ブール代数を一般化した概念である **ハイティング代数(Heyting algebra)** の構造をもつ。トポスとの具体的な関わりについては後の章で説明するが、ここでは準備としてハイティング代数の基本を紹介する。

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
$$ (U\Rightarrow V) = \bigcup\\{ W\in\mathcal{O}(X) \mid U\cap W\subseteq V \\}$$
となる。また $\bot = \emptyset$ であるので
$$ \neg U = \bigcup\\{ W\in\mathcal{O}(x) \mid U\cap W = \emptyset \\}$$
となる。例えば $\mathbb{R}$ 上の開集合として $U=(-\infty,0), V=(0,\infty)$ とすると
$ \neg U = (0, \infty), \neg V= (-\infty, 0)$なので
$$ \neg U \cap \neg V = \emptyset $$
$$ \neg (U\cup V) = \neg\left((-\infty, 0)\cup(0,\infty)\right)=\emptyset$$
より $\neg U\cap \neg V = \neg (U\cup V)$ だが
$$ \neg U \cup \neg V = (-\infty, 0)\cup(0, \infty) $$
$$ \neg (U\cap V) = \neg \emptyset = \mathbb{R}$$
より $\neg U\cup\neg V \neq \neg (U\cap V)$ である。

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

