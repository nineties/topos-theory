---
title: 初等トポス
weight: 4
section: 3
toc: true
---

## 初等トポス

集合論において、集合 $U$ の部分集合 $X$ は特性関数 $\chi$ によって表現する事ができる。
$$ X = \\{x\in U\mid\chi(x)\\}$$
初等トポスとはカルテシアン閉圏のうち、このような特性関数が常に存在する圏の事であり、集合論的な操作を行うことができる圏である。
$\chi(x)$ が真であるとはつまり "$x\in X$"であるという事であるので、初等トポスとは集合への元の帰属関係 $\in$ を表現する事が出来る圏だと言っても良い。

### 部分対象

まず集合の包含関係 $X\subseteq U$ を圏論的に一般化する。
$\mathbf{Set}$ においてはこれは包含写像 $X\hookrightarrow{} U$ によって表現できる。包含写像は単射であるが、 $\mathbf{Set}$ における単射はモノ射であるので、一般化する場合にもモノ射を用いる。ただし、モノ射の中には包含写像以外の物も含まれるのでこれを分類するという操作が必要となる。

{{% definition title="モノ射の順序関係" %}}
$a\in\mathcal{C}$ をコドメインとするモノ射 $m:x \hookrightarrow a, n:y \hookrightarrow a$ について、以下が可換となるような射 $f:x\rightarrow y$ が存在するときに $m\leq n$ であるとすると、 $a$をコドメインとするモノ射全体は関係 $\leq$ によって 前順序(preorder) をなす。(前順序"集合"とは限らないので注意)
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
コドメインが $a\in\mathcal{C}$ であるモノ射 $m, n: x\hookrightarrow a$ の同値関係 $m\sim n$ を
$$ m\leq n\text{かつ} n\leq m$$
によって定める。このとき、コドメインが $a$ であるモノ射全体を同値関係 $\sim$ で割った同値類を $a$ の **部分対象(subobject)** という。以下, 代表元が $m$ の同値類を $[m]$ と書く。

対象 $a$ の部分対象全体は $\leq$ によって 半順序(partially ordered) となる。任意の対象 $a\in\mathcal{C}$ の部分対象全体の類が集合となる圏は **冪化可能(well-powered)** であるという。
{{% /definition %}}

{{% proposition %}}
$a$ の部分対象 $m: x\hookrightarrow a, n:\hookrightarrow a$ が同値である事と、以下を可換にする同型射 $f:x\rightarrow y$ が存在することは同値。


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

$\mathbf{Set}$ における対象 $a$ の部分対象全体と $a$の部分集合全体は一対一に対応する。すなわち、部分対象 $[m]$ に対応する部分集合とは関数 $m$ の像であり、部分対象の順序 $\leq$ は部分集合の包含関係 $\subseteq$ と対応する。

### 部分対象分類子
$$ X = \\{x\in U\mid\chi(x)\\}$$

を圏論的に定式化する為には **引き戻し(pullback)** を用いる事ができる。引き戻しとは $\mathcal{J}$ が $\bullet\rightarrow\bullet\leftarrow\bullet$ の形の時の図式 $F:\mathcal{J}\rightarrow\mathcal{C}$ に対する極限を言うのだった。これを、図式を具体的に書き下して書き直すと以下の定義となる。

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

そこで、一方を定数関数 $\mathrm{true}: 1\rightarrow \\{\mathrm{true}, \mathrm{false}\\}$ 、もう一方を特性関数とすれば求める構成ができる。すなわち、以下において $Y$ が引き戻しならば($X\times 1\simeq X$ であるから)

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

{{% proposition label="prop.subobject-classifying-arrow" %}}
部分対象と分類射は一対一に対応する。
{{% /proposition %}}
{{% details 証明 %}}
$\mathcal{C}$ を部分対象分類子 $\mathrm{true}:1\rightarrow\Omega$ を持つ圏であるとする。
モノ射 $i: x\xhookrightarrow{}u$ と $j: y\xhookrightarrow {}$ が同値であるとする。すなわち同型射 $\alpha:x\rightarrow y$ が存在して $i = j\circ\alpha$ であるとする。
$$\xymatrix{
x \ar@{^{(}->}[rd]^-{i} \ar[rr]^{\alpha} && y \ar@{^{(}->}[ld]^-{j} \\\\
 & u &
}$$
また、 $i,j$ に対応する分類射をそれぞれ $\chi_i,\chi_j$ とする。

まず、 $u\xhookleftarrow{j}y\rightarrow 1$ が $u\xrightarrow{\chi_j}\Omega\xleftarrow{\mathrm{true}}1$ に対する引き戻しであるので、任意の $f: z\rightarrow u$ に対して、以下が可換となるような $v:z\rightarrow y$ が一意に存在する。
$$\xymatrix{
z \ar[rd]^v \ar@{.>}@/^1pc/[rrd] \ar@/^-1pc/[rdd]\_{f}& & \\\\
& y \ar@{^{(}->}[d]^{j} \ar@{.>}[r] & 1 \ar@{^{(}->}[d]^{\mathrm{true}} \\\\
& u \ar[r]^{\chi_j} & \Omega
}$$
$i=j\circ\alpha$ を用いて書き直すと以下の図式が可換であるが、$i$ がモノ射である事より、この図式が可換となるような$z$から$x$への射は $\alpha^{-1}\circ v$ 唯一つである。従って、この図式の四角形の部分は引き戻しの図式であるので、 $\chi_j$ は $i$ に対応する分類射である。従って分類射が一意に定まることから $\chi_i = \chi_j$ $\square$

$$\xymatrix{
z \ar[rd]^{\alpha^{-1}\circ v} \ar@{.>}@/^1pc/[rrd] \ar@/^-1pc/[rdd]\_{f}& & \\\\
& x \ar@{^{(}->}[d]^{i} \ar@{.>}[r] & 1 \ar@{^{(}->}[d]^{\mathrm{true}} \\\\
& u \ar[r]^{\chi_j} & \Omega
}$$
{{% /details %}}

### 部分対象関手

$x\in\mathcal{C}$ の部分対象の集まりを$\mathrm{Sub}(x)$ と表すと、{{< ref prop.subobject-classifying-arrow >}} より同型

$$ \mathcal{C}(x, \Omega) \simeq \mathrm{Sub}(x) $$

が存在する。これより、$\mathrm{Sub}$ が表現可能関手であって、 $\Omega$ がそれを表現する対象である事が示唆される。本節ではこれを証明する。その為に、まず引き戻しの性質を確認する。

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
$f: x\rightarrow y$ に対して $1_x^\*f = f$
$$\xymatrix{
y \ar[d]\_f \ar[r] & y \ar[d]^f \\\\
x \ar[r]^{1_x} & y
}$$
{{% /proposition %}}
これの証明は簡単なので省略。以上命題から、部分対象から部分対象への写像を考える事ができ、かつそれの合成や合成に関する単位元の存在が分かり、以下の部分対象関手が定義される。

{{% definition title="部分対象関手" %}}
冪化可能な圏 $\mathcal{C}$ において、 $\mathrm{Sub}(x)$ を $x\in\mathcal{C}$ の部分対象の集合とし、任意の $f: x\rightarrow y$ に対して $\mathrm{Sub}(f): \mathrm{Sub}(y)\rightarrow\mathrm{Sub}(x)$ を$\mathrm{Sub}(y)$ の部分対象(の代表元)の $f$ に沿った引き戻し(を代表元とする部分対象)に写す写像とすれば、$\mathrm{Sub}$ は反変関手 $\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ となる。これを **部分対象関手(subobject classifier)** という。

$$\xymatrix{
\bullet \ar@{^{(}->}[d]^{}=\"p\" \ar[r] & \bullet \ar@{^{(}->}[d]\_{}=\"q\" \\\\
x \ar[r]\_f & y 
\ar@{|->}\_{\mathrm{Sub}(f)} \"q\"; \"p\"
}$$
{{% /definition %}}
{{% details 証明 %}}
$\mathrm{Sub}$ が関手であることを示す。既に示した命題より、あとは $\mathrm{Sub}(f)$ の定義が、部分対象の代表元の選び方によらないことだけを示せば十分である。

以下の図式において、左の四角が引き戻しであるとする。また $m\simeq n$ であるとする。この時 $k$ は同型射であり、右の四角も引き戻しである。したがって、外側の四角も引き戻しであるので、$f^\*m$ は $n$ の $f$ に沿った引き戻しでもある。したがって $\mathrm{Sub}(f)$ は部分対象の代表元の選び方によらない。$\square$

$$\xymatrix{
\bullet \ar@{^{(}->}[d]\_{f^\*m} \ar[r]^g & \bullet \ar@{^{(}->}[d]^{m} \ar[r]^k & \bullet \ar@{^{(}->}[d]^n \\\\
x \ar[r]\_f & y \ar[r]^{1_y} & y
}$$

{{% /details %}}

そして、この部分対象関手を表現する対象及び普遍要素が部分対象分類子である。

{{% theorem label="prop.representability-of-sub" %}}
圏 $\mathcal{C}$ が有限完備かつ局所小である時、部分対象関手 $\mathrm{Sub}:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ が表現可能であることと、部分対象分類子 $\mathrm{true}:1\rightarrow\Omega$ が存在することは同値。

また、$\mathrm{Sub}$ を表現する対象が $\Omega$ であり、普遍要素が $[\mathrm{true}:1 \rightarrow\Omega]\in\mathrm{Sub}(\Omega)$ である。
{{% /theorem %}}

{{% details 証明 %}}
($\mathrm{Sub}$が表現可能 $\Rightarrow$ 部分対象分類子を持つ)

$\mathrm{Sub}$ がある $\Omega\in\mathcal{C}$ によって表現されるとする。すなわち、$a\in\mathcal{C}$ について自然な同型
$$ \phi_a: \mathrm{Sub}(a) \xrightarrow{\simeq} \mathrm{C}(a, \Omega) $$
が存在するとする。ここで同型 $ \phi\_{\Omega}: \mathrm{Sub}(\Omega) \xrightarrow{\simeq} \mathrm{C}(\Omega, \Omega) $ において右の $1\_\Omega$ に対応する部分対象の代表元を $\mathrm{true}: t\xhookrightarrow{}\Omega$ とする。(この時点では $\mathrm{true}$ のドメイン $t$ が終対象であるかは分からないので注意。)

あとは、任意のモノ射 $m: x\xhookrightarrow{} u$ に対して以下の図式が引き戻しとなるような $\chi: u\rightarrow\Omega$ が唯一つであることと、 $t$ が終対象であることを示せば良い。

$$\xymatrix{
x \ar[d]\_{m} \ar[r] & t \ar[d]^{\mathrm{true}} \\\\
u \ar[r]^{\chi} & \Omega \\\\
}$$

$m$ が $\mathrm{true}$ の $\chi$ に沿った引き戻しであるとすると
$$ [m] = \mathrm{Sub}(\chi)([\mathrm{true}]) $$
である。また、以下が可換であるから

$$\xymatrix{
\mathrm{Sub}(\Omega) \ar[d]\_{\mathrm{Sub}(\chi)} \ar[r]^{\phi\_\Omega} & \mathcal{C}(\Omega, \Omega) \ar[d]^{-\circ\chi} \\\\
\mathrm{Sub}(u) \ar[r]^{\phi\_u} & \mathrm{C}(u, \Omega)
}$$

$$\phi_u(\mathrm{Sub}(\chi)([\mathrm{true}])) = \phi\_{\Omega}([\mathrm{true}])\circ \chi$$

である。これらと、 $\phi\_{\Omega}([\mathrm{true}])=1\_\Omega$ より
$$\chi = \phi_u([m]) $$
である。したがって $m$ が $\mathrm{true}$ の $\chi$ に沿っての引き戻しとなるような $\chi$ は確かに存在し一意的に定まる。

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

である。
{{% /details %}}

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
| 部分対象分類子 | $\Omega=\\{\mathrm{true}, \mathrm{false}\\}$                                 | $[\mathrm{true}: 1\rightarrow\Omega]$ |

そして、(驚くべき事ではあるが)初等トポスには任意の有限余極限も存在する。
この定理の証明は非常に困難な道のりを辿るので、本章末尾に記載することにするが、ここではその雰囲気のみ紹介する。もし、初等トポス $\mathcal{C}$ が任意の有限余極限を持つならば、 {{< ref prop.ccc-is-distributive >}} より分配圏となるので、例えば

$$ \Omega^{a+b}\simeq \Omega^a \times \Omega^b$$

といった同型が存在する。この右辺はカルテシアン閉圏では任意の$a,b$ に対して必ず存在するので、逆に

$$ \Omega^x \simeq \Omega^a \times \Omega ^b $$

を満たす $x$ として $x$ を定めることで $a+b$ を定義できそうに思われる。
より一般化すると関手 $\Omega^{(-)}: \mathcal{C}^{\mathrm{op}}\rightarrow\mathcal{C}$ の性質を用いる事が出来そうであるが、実際の証明は大変複雑である。本章最終節にてこの証明を記載する。

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

## 層

**前層(presheaf)** 及び **層(sheaf)** は元々、位相空間の上に紐づけられた数学対象を研究する道具として生まれた概念であるが、その圏論的一般化は非常に重要である。

### 前層の圏

{{% definition title="前層" %}}
小圏 $\mathcal{C}$ の上の **前層(presheaf)** とは反変関手 $\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ の事である。

また、前層を対象とする関手圏 $\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}$ を **前層の圏(category of preshaves)** といい $\mathrm{PSh}(\mathcal{C})$ と書く。
{{% /definition %}}

前層の圏はとても良い性質を持つ。

{{% proposition %}}
前層の圏は双完備である。
{{% /proposition %}}

これは以下の定理と $\mathbf{Set}$ が双完備であることから示される。

{{% theorem title="関手圏の極限は点別に計算可能" label="th.limits-of-functor-categories" %}}
図式 $F:\mathcal{J}\rightarrow\mathcal{D}^{\mathcal{C}}$ について
$a\in \mathcal{C}$ に固定した関手 $F(-)(a):\mathcal{J}\rightarrow\mathcal{D} $ の極限 $\varprojlim_{i\in\mathcal{J}} F(i)(a)$ が全ての $a\in\mathcal{C}$ について存在するならば、$F$ の極限も存在し

$$ \left(\varprojlim\_{i\in\mathcal{J}} F(i)\right)(a) \simeq \varprojlim_{i\in\mathcal{J}} F(i)(a) $$

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

{{% proposition %}}
前層の圏はカルテシアン閉圏である。

前層 $p,q:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ に対する指数対象は
$$ q^p = \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(-)\times p, q) $$
である。
{{% /proposition %}}
{{% details 証明 %}}
任意の $p,q,r\in\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}$ について、 $q,r$ に関して自然な同型
$$ \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(r,q^p)\simeq\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(r\times p, q)$$
が存在することを示せば良い。

すなわち、自然変換 $\alpha: r\rightarrow q^p$ 、すなわち関数の族
$\\{ \alpha_c: r(c) \rightarrow \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(c)\times p, q)\\}\_{c\in\mathcal{C}}$
と、自然変換 $\beta: r\times p\rightarrow q$ 、すなわち関数の族 $\\{\beta_c: r(c)\times p(c)\rightarrow q(c)\\}\_{c\in\mathcal{C}}$ の対応を考える。

ここで、$x\in r(c), y\in p(c)$ に対して
$$\phi(\alpha)\_c: (x, y) \longmapsto \alpha_c(x)\_c(1_c, y) $$
$x\in r(c), d\in\mathcal{C}, f\in \mathcal{Y}(c)(d)\simeq\mathbf{Set}(d, c), z\in p(d)$ に対して
$$\psi(\beta)\_c: x\longmapsto \\{(f, z) \longmapsto \beta_d(r(f)(x), z)\\}\_{d\in\mathcal{D}}$$

とおくと

$$ \psi\circ\phi(\alpha)\_c: x\longmapsto \\{(f, z) \longmapsto \alpha_d(r(f)(x))\_d(1_d, z)\\}\_{d\in\mathcal{D}}$$

である。$\alpha$ は自然変換であるから以下が可換となるので

$$\xymatrix{
r(c) \ar[d]\_{r(f)} \ar[r]^-{\alpha_c} & \mathbf{Set}^{\mathbf{C}^{\mathrm{op}}}(\mathcal{Y}(c)\times p, q) \ar[d]^{-\circ(\mathcal{Y}(f)\times 1_p)} \\\\
r(d)                \ar[r]^-{\alpha_d} & \mathbf{Set}^{\mathbf{C}^{\mathrm{op}}}(\mathcal{Y}(d)\times p, q)
}$$

$$ \alpha_d(r(f)(x))\_d(1_d, z) = \alpha_c(x)\_d\circ(\mathcal{Y}(f)\times 1_p)(1_d, z) = \alpha_c(x)\_d(f,z)$$
となるから、 $\psi\circ\phi(\alpha) = \alpha$ である。
同様にして

$$ \phi\circ\psi(\beta)\_c: (x,y) \longmapsto \beta_c(r(1_c)(x), y) = \beta_c(x,y) $$

であるから $\phi\circ\psi(\beta) = \beta$ である。従って、以下は同型。
$$ \phi: \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(r,q^p)\xrightarrow{\simeq}\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(r\times p, q)$$

続いて、この同型の自然性を示す。 任意の $\sigma: r'\rightarrow r, \rho: q\rightarrow q'$ に対して、以下の可換性を示せば良い。
$$\xymatrix{
\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(r,q^p) \ar[r]^{\phi} \ar[d]\_{\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\sigma, \rho^p)} & \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(r\times p, q) \ar[d]^{\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\sigma\times p, \rho)} \\\\
\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(r',{q'}^p) \ar[r]^{\phi} & \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(r'\times p, q')
}$$

任意の $\alpha: r\rightarrow q^p$ に対して、図式の右上を辿ったものの $c$-componentは

$$(\rho\circ \phi(\alpha)\circ(\sigma\times 1_p))\_c: (x,y)\longmapsto \rho_c(\phi(\alpha)\_c(\sigma_c(x), y)) = \rho_c(\alpha_c(\sigma_c(x))(1_c,y))$$

である。左下を辿ったものは

$$\phi(\rho^p\circ\alpha\circ\sigma)\_c: (x,y)\longmapsto (\rho^p\circ\alpha\circ\sigma)\_c(x)(1_c, y)=((\rho^p)\_c(\alpha_c(\sigma_c(x))))(1_c, y)$$

であり、
$$\rho^p(f) = \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(-)\times p, \rho)(f)=\rho \circ f\circ(\mathcal{Y}(-)\times 1_p) $$
であるから

$$((\rho^p)\_c(\alpha_c(\sigma_c(x))))(1_c, y) = \rho\_c(\alpha_c(\sigma_c(x))(\mathcal{Y}(1_c),y)) = \rho_c(\alpha_c(\sigma_c(x))(1_c, y))$$

となる。以上より上記の図式は可換となる。$\square$
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
まず、$\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}$ の終対象 $1:\mathcal{C}^{\mathrm{op}}\rightarrow\mathbf{Set}$ は点別に計算できるので、任意の $c\in\mathcal{C}$ について $1(c)$ は $\mathbf{Set}$ の終対象である。そこで
$$ 1(c) = \\{\ast\\}$$
とおく。

部分対象分類子 $\Omega$ が存在するならば、米田の補題より
$$ \Omega(c) \simeq \mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(c),\Omega) $$
であり、 $\mathbf{Set}^{\mathcal{C}^{\mathrm{op}}}(\mathcal{Y}(c),\Omega) \simeq \mathrm{Sub}(\mathcal{Y}(c))$ であるから、$\Omega=\mathrm{Sub}(\mathcal{Y}(-))$ でなければならない事が分かる。

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
