---
title: 位相空間上の層
weight: 5
section: 4
toc: true
---

## 位相空間上の層
図形などの数学的対象について調べるときに、全体の性質を一気に把握することが難しい場面で、 **局所的な情報をまず調べ、それらをつなぎ合わせて全体の性質を知る**
という操作を行う場面が多いと思う。 **層(sheaf)** はこのような操作ができる数学対象を抽象化した概念であり、元々は位相空間上の数学対象を扱う手段として誕生し、後に圏論的に一般化されたものである。 本章では、まず位相空間上の層について解説し、続く章で圏論的な一般化を行う。


位相空間 $X$ 上の前層・層 $F$ とは各開集合 $U\in\mathcal{O}\_X$ に集合 $F(U)$ を紐づけるものであり、特定の条件を満たすものである。例えば $X$ を地球表面とした時 $F$ は地球表面上の領域 $U$ に対して何らかの数学的対象 $F(U)$ を紐づけるものである。例えば地球表面上の温度分布に関心があるならば $F(U)$ は二次元の連続関数の集合について考えるといった事である。

$F$ は特定の状況を与えるものではなく、数学の舞台を設定するものである。温度分布の例で言うならば、$F(U)$ はあらゆる状況の集合であって元$s\in F(U)$ が特定の状況を表す。この元 $s$ のことを **切断(section)** と言う。

{{< figure src="../images/earth-and-map.png" width="50%" >}}

そして、上で述べたことを実現する為、前層 $F$ は、数学的対象 $F(U)$ の注目する範囲 $U$ を狭めていく操作を備えており、層 $F$ は更に $F(U)$ らを貼り合わせてより大きな範囲に対する数学対象を得る操作を備えている。

### 前層

位相空間 $X$ 上の前層 $F$ は **注目する範囲を狭める操作** を備えている。すなわち、$U\supseteq V$ の時に、$F(U)$ から $F(V)$ を作る **制限写像(restriction map)** と呼ばれる写像 $\rho^U_V$ を備えており、これが範囲を狭める操作について整合的であるものである。

{{% definition title="位相空間上の前層" %}}
位相空間$X$ 上の前層 $F$ とは、各開集合 $U\in\mathcal{O}_X$ に集合 $F(U)$ を対応させるものであり、
任意の $U\supseteq V\ (U,V\in\mathcal{O}_X)$ に対して以下の条件を満たす **制限写像(restriction map)** 
$$ \rho^U_V: F(U)\rightarrow F(V) $$
を備えるものである。

1. $\rho^U_U$ は恒等写像である。
2. $U\supseteq V\supseteq W$ のとき、 $\rho^U_W = \rho^V_W\circ\rho^U_V$

$F(U)$ の元を **切断(section)** と呼ぶ。$s \in F(U)$ の時 $\rho^U_V(s)$ の代わりに $s|_V$ と書くこともある。
{{% /definition %}}

この定義は $X$ の開集合系 $\mathcal{O}_X$ を包含関係 $\subseteq$ によって圏とみなした時 $F$ 及び $\rho$ が$\mathcal{O}_X^{\mathrm{op}}$ から $\mathbf{Set}$ への関手であるといっている事に他ならず、圏論的な前層の定義と一致する。この時 $F(U\supseteq V) = \rho^U_V$ である。

### 層
前層のうち、局所的な数学対象を貼り合わせて大域的な数学対象を矛盾なく構成できるものを層という。

{{% definition title="位相空間上の層(切断利用)" %}}
位相空間 $X$ 上の前層 $F$ で以下の条件を満たすものを **層(sheaf)** という。

1. $X$ の任意の開集合 $U$ と、その開被覆 $U=\bigcup\_{\lambda\in\Lambda}U\_{\lambda}$、切断 $s,t\in F(U)$ について、全ての $\lambda\in \Lambda$ で $s|\_{U\_{\lambda}} = t|\_{U\_{\lambda}}$ であるならば $s = t$ である。

2. $X$ の任意の開集合 $U$ と、その開被覆 $U=\bigcup\_{\lambda\in\Lambda}U\_{\lambda}$、切断の族 $s\_{\lambda}\in F(U\_{\lambda})$ について、任意の $\alpha,\beta\in\Lambda$ で $s\_{\alpha}|\_{U\_{\alpha}\cap U\_{\beta}} = s\_{\beta}|\_{U\_{\alpha}\cap U\_{\beta}}$ であるならば、ある切断 $s\in F(U)$ が存在し全ての $\lambda\in\Lambda$ に対して $s|\_{U\_{\lambda}} = s\_{\lambda}$
{{% /definition %}}

1つめの条件は $F(U)$ の切断はその局所的な情報のみから一意に定まるということをいっている。2つめの条件は重なる部分で一致する切断は貼り合わせて一つの大きな切断にする事が出来るということをいっている。

層の具体例は様々あり

- 位相空間上の実数値連続関数
- 代数多様体上の正則関数
- 微分可能多様体上の微分可能関数

などである。

### 層の圏論的定義

簡単なケースとして 開被覆$U=U_1\cup U_2$ の場合を考えると、 $F$ が層であるならば重なる部分で一致する $s_1,s_2$ の組とそれを貼り合わせた $s\in F(U)$ が一対一に対応している。すなわち、

$$F(U) \simeq \\{(s_1, s_2) \in F(U_1)\times F(U_2) \mid \rho^{U_1}\_{U_1\cap U_2}(s_1) = \rho^{U_2}\_{U_1\cap U_2}(s_2)\\}$$

であり、 $s|\_{U_1}=s_1$ 及び $s|\_{U_2}=s_2$ を満たす射影 $\rho^U\_{U_1}: F(U)\rightarrow F(U_1)$ 及び $\rho^U\_{U_2}: F(U)\rightarrow F(U_2)$ が備わっているということなので、これは $\mathbf{Set}$ においてはイコライザを用いて

$$ F(U) \simeq \mathrm{eq}\left(\rho^{U_1}\_{U_1\cap U_2}, \rho^{U_2}\_{U_1\cap U_2}\right)$$

と書くことができる。より一般には任意の開被覆 $U=\bigcup\_{\lambda\in\Lambda}U\_{\lambda}$ に対して、全ての共通部分で一致する切断の族 $\\{s\_{\lambda}\\}$ とそれらを貼り合わせた $s\in F(U)$ が一対一に対応すると言う事である。この定義では切断 $s\in F(U)$ を明示的に使わないので、後に位相空間以外にも一般化する事が出来る。

{{% definition title="位相空間上の層(イコライザ利用)" %}}
位相空間 $X$ 上の前層 $F$ が以下の条件を満たすときこれを **層(sheaf)** という。

$X$ の任意の開集合 $U$ と、その開被覆 $U=\bigcup\_{\lambda\in\Lambda}U\_{\lambda}$について
$$ F(U) \simeq \mathrm{eq}\left(\prod\_{\lambda\in\Lambda}F(U\_{\lambda})\overset{p}{\underset{q}{\rightrightarrows}}\prod\_{\alpha,\beta\in\Lambda}F(U\_{\alpha}\cap U\_{\beta})\\right)$$
が成り立つ。但し $p$ は $\rho^{U\_{\alpha}}\_{U\_{\alpha}\cap U\_{\beta}}$ を束ねたもの、 $q$ は$\rho^{U\_{\beta}}\_{U\_{\alpha}\cap U\_{\beta}}$ を束ねたもの。
{{% /definition %}}

{{% details 同値性の証明 %}}
位相空間上の層の切断を用いた定義を①、イコライザを用いた定義を②とする。

(①$\Rightarrow$ ②)

位相空間 $X$ 上の前層 $F$ が定義①を満たすとする。開被覆 $U=\bigcup\_{\lambda\in\Lambda}U\_{\lambda}$ に対して
$$e(s) = \\{s|\_{U\_{\lambda}}\\}\_{\lambda\in\Lambda},\quad
p(\\{s\_{\lambda}\\}\_{\lambda\in\Lambda}) = \\{s\_{\alpha}|\_{U\_{\alpha}\cap U\_{\beta}}\\}\_{\alpha,\beta\in\Lambda},\quad
q(\\{s\_{\lambda}\\}\_{\lambda\in\Lambda}) = \\{s\_{\beta}|\_{U\_{\alpha}\cap U\_{\beta}}\\}\_{\alpha,\beta\in\Lambda}$$
とおくと、$F$ が前層であることより下の図式は可換である。

$$\xymatrix{
F(U) \ar[r]^-e & \displaystyle\prod\_{\lambda\in\Lambda}F(U\_{\lambda}) \ar@<+2pt>[r]^-{p} \ar@<-2pt>[r]\_-{q} &\displaystyle\prod\_{\alpha,\beta\in\Lambda}F(U\_{\alpha}\cap U\_{\beta})
}$$

ある集合 $A$ 及び関数 $f: x\mapsto \\{f\_{\lambda}(x)\\}\_{\lambda\in\Lambda}$ が以下を可換にするとする。

$$\xymatrix{
A \ar[r]^-f & \displaystyle\prod\_{\lambda\in\Lambda}F(U\_{\lambda}) \ar@<+2pt>[r]^-{p} \ar@<-2pt>[r]\_-{q} &\displaystyle\prod\_{\alpha,\beta\in\Lambda}F(U\_{\alpha}\cap U\_{\beta})
}$$

すると各 $x\in A$ に対して $f\_{\alpha}(x)|\_{U\_{\alpha}\cap U\_{\beta}}=f\_{\beta}(x)|\_{U\_{\alpha}\cap U\_{\beta}} \quad (\alpha,\beta\in\Lambda)$ であるので、定義①の条件2よりある $s\in F(U)$ が存在して $s|\_{U\_{\lambda}} = f\_{\lambda}(x)\quad (\lambda\in\Lambda)$ となる。また条件１よりこれを満たす $s$ は一意である。

従って任意の $A,f$ に対して、以下の図式が可換となるような $u: A\ni x \mapsto s\in F(U)$ が一意に存在するので、これはイコライザの定義を満たし $F(U)\simeq\mathrm{eq}(p, q)$ である。
$$\xymatrix{
A \ar@{.>}[d]^-{\exists! u} \ar[rd]^{f} & & \\\\
F(U) \ar[r]^-e & \displaystyle\prod\_{\lambda\in\Lambda}F(U\_{\lambda}) \ar@<+2pt>[r]^-{p} \ar@<-2pt>[r]\_-{q} &\displaystyle\prod\_{\alpha,\beta\in\Lambda}F(U\_{\alpha}\cap U\_{\beta})
}$$

(②$\Rightarrow$ ①)

位相空間 $X$ 上の前層 $F$ が定義②を満たすとする。開被覆 $U=\bigcup\_{\lambda\in\Lambda}U\_{\lambda}$、切断 $s,t\in F(U)$ について、全ての $\lambda\in\Lambda$ で $s|\_{U\_{\lambda}} = t|\_{U\_{\lambda}}$ であるとする。すると、以下の図式は $u=s$ としても $u=t$ としても可換となるが、 $u$ の一意性より $s=t$ である。従って定義①の条件１が示された。

$$\xymatrix{
1 \ar[d]^-u \ar[rd]^{\\{s|\_{U\_{\lambda}}\\}} & & \\\\
F(U) \ar[r]^-e & \displaystyle\prod\_{\lambda\in\Lambda}F(U\_{\lambda}) \ar@<+2pt>[r]^-{p} \ar@<-2pt>[r]\_-{q} &\displaystyle\prod\_{\alpha,\beta\in\Lambda}F(U\_{\alpha}\cap U\_{\beta})
}$$

そして、切断の族 $s\_{\lambda}\in F(U\_{\lambda})$ について、任意の $\alpha,\beta\in\Lambda$ で $s\_{\alpha}|\_{U\_{\alpha}\cap U\_{\beta}} = s\_{\beta}|\_{U\_{\alpha}\cap U\_{\beta}}$ であるならば、以下の図式が可換となる $s\in F(U)$ が存在し、この時 $s|\_{U\_{\lambda}} = s\_{\lambda}$ となる。従って定義①の条件２も示された。

$$\xymatrix{
1 \ar[d]^-s \ar[rd]^{\\{s\_{\lambda}\\}} & & \\\\
F(U) \ar[r]^-e & \displaystyle\prod\_{\lambda\in\Lambda}F(U\_{\lambda}) \ar@<+2pt>[r]^-{p} \ar@<-2pt>[r]\_-{q} &\displaystyle\prod\_{\alpha,\beta\in\Lambda}F(U\_{\alpha}\cap U\_{\beta})
}$$

$\square$

{{% /details %}}

この定義は切断を用いた定義の素直な翻訳であるが、より抽象度の高い定義として関手の連続性を用いた以下のような定義も可能である。

{{% definition title="位相空間上の層(連続性利用)" %}}
位相空間 $X$ 上の前層 $F$ が **層(sheaf)** であるとは、 $\mathcal{O}_X^{\mathrm{op}}$ の **余完備充満部分圏(cocomplete full subcategory)** $J$ に対して以下が成立することである。
$$ F\left(\varprojlim\_{U\_{\lambda}\in J}U\_{\lambda}\right) \simeq \varprojlim\_{U\_{\lambda}\in J}F(U\_{\lambda})$$
{{% /definition %}}

この定義の状況を図示すると以下の様になる。 $J$ が余完備であるというのは任意の $U\_{\alpha},U\_{\beta}\in J$ に対して $U\_{\alpha}\cap U\_{\beta} \in J$ ということで、充満であるというのは開集合の間の包含関係を漏らさず $J$ に持ってきているということである。そして
$$\varprojlim\_{U\_{\lambda}\in J}U\_{\lambda} = \bigcup\_{U\_{\lambda}\in J}U\_{\lambda}$$
であるので、上記の定義は位相空間 $X$ 上での領域の貼り合わせと、対応する数学的対象 $\\{F(U\_{\lambda})\\}$ の貼り合わせが整合的であるという事を言っており、直感的にも理解しやすい定義となっている。

{{< figure src="../images/sheaf-using-continuous-functor.png" width="60%" >}}


{{% details 同値性の証明 %}}
位相空間上の層の切断を用いた定義を①、連続性を用いた定義を③とする。

(①$\Rightarrow$ ③)

位相空間 $X$ 上の前層 $F$ が定義①を満たすとする。$\mathcal{O}^{\mathrm{op}}\_X$ の余完備充満部分圏 $J$ に対して

$$U = \varprojlim\_{U\_{\lambda}\in J}U\_{\lambda} = \bigcup\_{U\_{\lambda}\in J}U\_{\lambda}$$

とおくと$\\{U\_{\lambda}\\}$ は $U\in\mathcal{O}^{\mathrm{op}}\_X$ の開被覆になっている。まず、任意の$J$ の対象 $U\_{\alpha}\supseteq U\_{\beta}$ に対して $F$ が前層であることより以下は可換。


$$\xymatrix{
F(U) \ar[d]_{\rho^U\_{U\_{\alpha}}} \ar[rd]^{\rho^U\_{U\_{\beta}}} & \\\\
F(U\_{\alpha}) \ar[r]\_{\rho^{U\_{\alpha}}\_{U\_{\beta}}} & F(U\_{\beta})
}$$

ここで、任意の$J$ の対象 $U\_{\alpha}\supseteq U\_{\beta}$ に対して以下が可換となるような $A$ と $\\{f\_{U\_{\lambda}}\\}$ が存在したと仮定する。

$$\xymatrix{
A \ar[d]_{f\_{U\_{\alpha}}} \ar[rd]^{f\_{U\_{\beta}}} & \\\\
F(U\_{\alpha}) \ar[r]\_{\rho^{U\_{\alpha}}\_{U\_{\beta}}} & F(U\_{\beta})
}$$

任意の $x\in A$ に対して $s\_{\lambda} = f\_{U\_{\lambda}}(x)$ とおくと、任意の $J$ の対象 $U\_{\alpha},U\_{\beta}$ に対して、 $J$ が余完備であることから $U\_{\alpha}\cap U\_{\beta}$ が存在し、以下の図式が共に可換となるから
$$ s\_{\alpha}|\_{U\_{\alpha}\cap U\_{\beta}} = s\_{\beta}|\_{U\_{\alpha}\cap U\_{\beta}} = f\_{U\_{\alpha}\cap U\_{\beta}}(x)$$

$$\xymatrix{
A \ar[d]\_{f\_{U\_{\alpha}}} \ar[rd]^{f\_{U\_{\alpha}\cap U\_{\beta}}} & & A \ar[d]\_{f\_{U\_{\beta}}} \ar[rd]^{f\_{U\_{\alpha}\cap U\_{\beta}}} & \\\\
F(U\_{\alpha}) \ar[r] & F(U\_{\alpha}\cap U\_{\beta}) & F(U\_{\beta}) \ar[r] & F(U\_{\alpha}\cap U\_{\beta})
}$$

従って定義①の条件2より $s\in F(U)$ が存在して $s|\_{U\_{\lambda}} = s\_{\lambda}$ となる。この対応 $x\mapsto s$ を $u$ とすると以下の図式が可換となり、条件１よりこのような $u$ は唯一つに定まる。従って $F(U) \simeq \varprojlim\_{U\_{\lambda}\in J}F(U\_{\lambda})$ である。

$$\xymatrix{
A \ar[d] \ar[rd] \ar@{.>}[r]^{\exists! u} & F(U) \ar[ld] \ar[d]\\\\
F(U\_{\alpha}) \ar[r] & F(U\_{\beta})
}$$

(③$\Rightarrow$ ①)

位相空間 $X$ 上の前層 $F$ が定義③を満たすとする。任意の開集合 $U\in\mathcal{O}^{\mathrm{op}}\_X$ と開被覆 $U=\bigcup\_{\lambda\in\Lambda}U\_{\lambda}$ に対して、いずれかの $U\_{\lambda}$ に含まれる開集合全てを対象とする $\mathcal{O}^{\mathrm{op}}\_X$ の充満部分圏を $J$ とする。混同を避ける為 $J$ の対象を $V\_{\lambda}$ と表記する。$J$ が余完備である事は簡単にわかり

$$ F\left(\varprojlim\_{V\_{\lambda}\in J}V\_{\lambda}\right) \simeq \varprojlim\_{V\_{\lambda}\in J}F(V\_{\lambda})$$

である。ここで、切断 $s,t\in F(U)$ について、全ての $\lambda\in\Lambda$ で $s|\_{U\_{\lambda}} = t|\_{U\_{\lambda}}$ であるとすると、 $F$ が前層であることにより任意の $V\in J$ に対して $s|\_V = t|\_V$ である。任意の $J$ の対象 $V\_{\alpha}\supseteq V\_{\beta}$ に対して、 以下は可換であるからこれは $1$ を頂点とする錐。

$$\xymatrix{
1 \ar[d]\_{s|\_{V\_{\alpha}}} \ar[rd]^-{s|\_{V\_{\beta}}} & \\\\
F(V\_{\alpha}) \ar[r] & F(V\_{\beta})
}$$

従って、任意の $V\in J$ について以下が可換となるような $u$ が一意に存在するが、これは $u=s$ としても $u=t$ としても可換。従って $s=t$ であるので定義①の条件１が示された。
$$\xymatrix{
1 \ar[d]\_{s|\_V} \ar@{.>}[r]^-{\exists u} & F(U) \ar[ld]^{\rho^U\_V} \\\\
F(V) &
}$$

続いて、切断の族 $\\{s\_{\lambda}\\}\_{\lambda\in\Lambda}$ について、任意の $\alpha,\beta\in\Lambda$ で $s\_{\alpha}|\_{U\_{\alpha}\cap U\_{\beta}} = s\_{\beta}|\_{U\_{\alpha}\cap U\_{\beta}}$ であるとする。ここで各 $V\in J$ について $V\subseteq U\_{\lambda}$ となる $U\_{\lambda}$ を用いて $ t\_V = s\_{\lambda}|\_V$ となる族 $\\{t\_V\\}\_{V\in J}$ を定める。 ここで $V\subseteq U\_{\alpha}$ かつ $V\subseteq U\_{\beta}$ の時には $V\subseteq U\_{\alpha}\cap U\_{\beta}$ であるので
$$ s\_{\alpha}|\_V = s\_{\beta}|\_V $$
であるから $t\_V$ は $\lambda$ の選び方によらず well-defined である。この時、任意の $V\_{\alpha}\supseteq V\_{\beta}$ に対して以下が可換となるので、

$$\xymatrix{
1 \ar[d]\_{t\_{V\_{\alpha}}} \ar[rd]^-{t\_{V\_{\beta}}} & \\\\
F(V\_{\alpha}) \ar[r] & F(V\_{\beta})
}$$

任意の $V\in J$ に対して、以下が可換となる $s \in F(U)$ がただ一つ存在する。そして、全ての $\lambda\in\Lambda$ に対して
$$ s|\_{U\_{\lambda}} = \rho^U\_{U\_{\lambda}}(s) = t\_{U\_{\lambda}} = s\_{\lambda}|\_{U\_{\lambda}} = s\_{\lambda}$$
であるから定義①の条件２も示された。

$$\xymatrix{
1 \ar[d]\_{t\_V} \ar@{.>}[r]^-{\exists s} & F(U) \ar[ld]^{\rho^U\_V} \\\\
F(V) &
}$$

$\square$
{{% /details %}}

## エタールバンドル

### バンドルの断面の層

{{% definition title="バンドルの断面" %}}
位相空間 $E, X$ に対して連続写像 $\pi: E\rightarrow X$ を$X$ 上の **束,バンドル(bundle)** という。
この時 $E$ を **全空間(total space)**、 $X$ を **底空間(base space)** という。

底空間 $X$ の任意の開集合 $U$ と、バンドル $\pi: E\rightarrow X$ に対して、 $\pi\circ s: U\rightarrow X$ が包含写像となるような 連続写像 $s: U\rightarrow E$ を $U$ 上の **断面(cross section)** という。
{{% /definition %}}

例えば全空間を$xy$平面($\mathbb{R}^2$), 底空間を$x$軸($\mathbb{R}$)として、バンドル $\pi(x, y) = x$ について考える。(位相はユークリッド空間としての通常の位相とする。)

$\pi$ に対する開集合 $U\subseteq\mathbb{R}$上の 断面 $s$ とはどのようなものであるかというと、
$ s(x) = (f(x), g(x)) $
なる連続関数であって、
$ \pi(s(x)) = x $
を満たすものであるから $f(x)=x$ であれば良くて、 $s(x) = (x, g(x))$ と表される。
すなわち、この場合の $U$ 上の断面とは $U$ 上で定義された連続関数 $y=g(x)$ のことである。

同様に全空間を $xy$ 平面から原点を除いた空間とし、同じく $\pi$ をバンドルとすると
$U$ 上の断面は $U$ 上で定義された連続関数 $y=g(x)$ で $g(0)\neq 0$ を満たすもの事である。
$g(0)\neq 0$ を満たす為、これらの断面をつなぎ合わせてより大きな断面を作る操作が矛盾なくできることがわかる。

バンドルの断面の集合は自動的に層となる。上の二つの例でも $\mathbb{R}$ 上で定義された連続関数の集合や、 原点で $0$ にならない連続関数の集合がいずれも層の条件を満たす事が分かると思う。

{{% definition title="バンドルの断面の層" %}}
バンドル $\pi: E\rightarrow X$ が与えられた時、開集合 $U\subseteq \mathcal{O}\_X$ に $U$ 上の断面の集合 $\Gamma\_{\pi}(U)$ を対応させ、
$V\subseteq U$ に制限写像 $\rho^U\_V: \Gamma\_{\pi}(U)\rightarrow\Gamma\_{\pi}(V)$ を対応させる対応関係は関手

$$ \Gamma\_{\pi}: \mathcal{O}^{\mathrm{op}}\_X \rightarrow \mathbf{Set} $$

になり、これは$X$ 上の層である。
{{% /definition %}}

{{% details 証明 %}}
制限写像の性質から関手であることは明らかなので、層である事を示す。

$X$ の任意の開集合 $U$ とその開被覆 $U=\bigcup\_{\lambda\in\Lambda}U\_{\lambda}$、切断(断面) $s,t\in\Gamma\_{\pi}(U)$ について、
全ての $\lambda\in \Lambda$ で $s|\_{U\_{\lambda}} = t|\_{U\_{\lambda}}$ であるとする。

断面の定義より $s,t$ は連続写像 $U\rightarrow E$である。ここで任意の $x\in U$ について、 $x\in U\_{\lambda}$ となる $\lambda$ が存在し、この時
$$ s(x) = s|\_{U\_{\lambda}}(x) = t|\_{U\_{\lambda}}(x) = t(x)$$
となる。よって全ての $x\in U$ で値が等しいので $s=t$ である。


続いて、$X$ の任意の開集合 $U$ と、その開被覆 $U=\bigcup\_{\lambda\in\Lambda}U\_{\lambda}$、切断(断面)の族 $s\_{\lambda}\in \Gamma\_{\pi}(U\_{\lambda})$ について、任意の $\alpha,\beta\in\Lambda$ で $s\_{\alpha}|\_{U\_{\alpha}\cap U\_{\beta}} = s\_{\beta}|\_{U\_{\alpha}\cap U\_{\beta}}$ であるとする。

この時、写像 $s:U\rightarrow E$ を$x\in U$ に対して $x\in U\_{\lambda}$ となる $\lambda$ を用いて $s(x) = s\_{\lambda}(x)$ と定める。
重なる部分で $s\_{\lambda}$ の値は等しいので、これはwell-definedである。
また、各点 $x\in U$ の十分小さな近傍では $s$ はいずれかの $s\_{\lambda}$ と一致し、 $s\_{\lambda}$ は連続写像であるから、 $s$ も連続写像である。
そして、各点 $x\in U$ である $\lambda$ について
$$ \pi(s(x)) = \pi(s\_{\lambda}(x)) = x \quad (x \in U\_{\lambda})$$
となるので $\pi\circ s$ は包含写像 $U\rightarrow X$となる。したがって $s\in\Gamma\_{\pi}(U)$ である。

$\square$
{{% /details %}}

### 前層の芽のバンドル

バンドル$\pi:E\rightarrow X$ の断面の層は、各切断 $s\in\Gamma\_{\pi}(U)$ が具体的な連続写像 $s:U\rightarrow E$ であり、非常に扱いやすい。
一方で、一般的な位相空間 $X$ 上の前層 $F$ はもっと抽象的なものであり直接は扱いにくいが、 $F$ の情報を元にして **エタールバンドル(étale bundle)** というバンドルを構成する事ができ、同様の議論が可能になる。

前層 $F$ の切断をある点 $x$ における局所的な振る舞いで分類するという事を考える。この同値類を $F$ の $x$ における **芽(germ)** といい、
芽の集合を **茎(stalk)** という。すなわち、前層 $F$ の $x$ 上の茎とは、 $F$ の $x$ における局所的な情報を集めた集合である。

{{% definition title="前層の芽と茎" %}}
位相空間 $X$ 上の前層 $F:\mathcal{O}\_X^{\mathrm{op}}\rightarrow\mathbf{Set}$ の点 $x\in X$ 上の二つの切断、すなわち、
$$s\in F(U), t\in F(V)\quad (x\in U,x\in V,U\in\mathcal{O}\_X,V\in\mathcal{O}\_X)$$
が $x$ の近傍で一致する時、すなわち、ある開集合 $W\subseteq U\cap V$ が存在して $s|\_W=t|\_W$ となるとき、
$s$ と $t$ は **$x$で同じ芽を持つ** といい $s\sim\_x t$ と書く。

$s\sim\_x t$ は同値関係であり、この関係による同値類を **$F$の$x$上の芽(germ)** という。
切断 $s$ を代表元とする芽を $\mathrm{germ}\_x(s)$ や $s\_x$ と書く。

また、$x$上の $F$ の芽すべての集合

$$ F\_x = \\{ s\_x \mid U\in\mathcal{O}\_X, s\in F(U), x\in U\\} $$

を **$F$の$x$上の茎(stalk)** という。
{{% /definition %}}

茎 $F\_x$ には $F$ の $x$ における局所的な情報が詰まっているので、これを $x\in X$ に渡って集める事で $F$ 全体の情報をもつ位相空間を構成する事ができる。

{{% definition title="前層の芽のバンドル" %}}
位相空間 $X$ 上の前層 $F$ の茎 $F\_x\ (x\in X)$ の直和
$$ \Lambda\_F = \coprod\_{x\in X}F\_x = \\{(x, r) \mid x\in X, r\in F\_x \\} $$
に、開集合 $U\in\mathcal{O}\_X$ と切断 $s\in F(U)$ から定まる集合 $ s(U) = \\{ (x, s\_x) \mid x\in U \\}$ の族
$$ \\{ s(U) \mid U\in\mathcal{O}\_X, s\in F(U) \\} $$
を開基とする位相を入れた位相空間について、
$\Lambda\_F$ から $X$ への射影

$$ \pi: \Lambda\_F\ni(x, r)\mapsto x\in X $$

は連続写像となる。これを 前層$F$ の**芽のバンドル(bundle of germs)** という。
{{% /definition %}}

{{% details 連続性の証明 %}}
任意の開集合 $U\in\mathcal{O}\_X$ に対して $\pi^{-1}(U)$ が $\Lambda\_F$ の開集合である事を示せば良い。

任意の $(x, r)\in\pi^{-1}(U)$ に対して、 $r$ は $x$ 上の芽であるからある $x$ の近傍 $V$ と切断 $s\in F(V)$ が存在して
$r=s\_x$ であるが、芽の定義よりこの $V$ は $V\subseteq U$ となるように選ぶ事ができる。この時 $(x, r)\in s(V)$ であるから
$$ \pi^{-1}(U)\subseteq \bigcup\_{V\subseteq U, s\in F(V)} s(V) $$
となる。

逆に $ (x,r)\in \bigcup\_{V\subseteq U, s\in F(V)} s(V) $ であるとすると、ある開集合 $V\subseteq U$ と切断 $s\in F(V)$ が存在して
$(x, r)\in s(V)$ であるが、この時 $x\in V\subseteq U$ であるので $x\in U$、すなわち $\pi(x, r)=x\in U$ であるから $(x, r)\in\pi^{-1}(U)$ である。
すなわち
$$ \pi^{-1}(U)\supseteq \bigcup\_{V\subseteq U, s\in F(V)} s(V) $$

したがって
$$ \pi^{-1}(U) = \bigcup\_{V\subseteq U, s\in F(V)} s(V) $$
であり、これは $\Lambda\_F$ の開基の元の合併であるから開集合である。 $\square$
{{% /details %}}

### エタールバンドル

さて、 芽のバンドル $\Lambda\_F$ が $F$ 全体の情報をもつ位相空間である、という事を述べたが具体的にどのような性質を持つのか調べていく。

{{% definition title="エタールバンドル" %}}
バンドル $\pi: E\rightarrow X$ が **エタール(étale)** もしくは **エタールバンドル(étale bundle)** であるとは、
これが **局所同相写像(local homeomorphism)** すなわち、
任意の点 $x\in E$ に対してある近傍 $V$ が存在して
$$ \pi|\_{V}: V\rightarrow \pi(V) $$
が同相写像となることである。
{{% /definition %}}

局所同相だが同相ではないエタールバンドルの例は
$$ \pi: \mathbb{R}\ni \theta \mapsto (\cos\theta,\sin\theta) \in S^1 $$
などである。写像全体としては、例えば $\theta=0,2\pi$ が同じ点に潰れるので同相ではないが、局所的に見れば線分と円弧であって同相である。

ここで、次の事が言える。すなわち、 $\Lambda\_F$ は単に位相空間であるだけでなく、$X$ と局所同相なのである。
これにより抽象的な前層 $F$ から具体的な幾何学的考察を行いやすい空間を構成することができた。

{{% proposition %}}
前層 $F$ の芽のバンドル $\pi:\Lambda\_F\rightarrow X$ はエタールである。
{{% /proposition %}}
{{% details 証明 %}}
$\Lambda\_F$ の任意の開基の元 $s(U)$ について $\pi|\_{s(U)}: s(U)\rightarrow U$ が同相写像であることを示せば十分である。
ここで $\pi(s(U))=U$ である事は容易に分かる。

($\pi|\_{s(U)}$ の全単射性)
任意の $x\in U$ に対して、 $(x, s\_x) \in s(U)$ であって $\pi|\_{s(U)}(x, s\_x) = x$ であるから、 $\pi|\_{s(U)}$ は全射。
そして $\pi|\_{s(U)}(x, s\_x) = \pi|\_{s(U)}(y, s\_y)$ であるとすると、$\pi$ の定義から $x=y$ であるので $\pi|\_{s(U)}$ は単射。

($\pi|\_{s(U)}$ の連続性)
$\pi$ が連続写像であるので、その制限である $\pi|\_{s(U)}$ も連続。

($\left(\pi|\_{s(U)}\right)^{-1}$ の連続性)
任意の開集合 $W\subseteq s(U)$ について
$\left(\left(\pi|\_{s(U)}\right)^{-1}\right)^{-1}(W) = \pi|\_{s(U)}(W)$
が開集合である事を示せば良い。ここで $s(U)$ の定義からある $X$ の開集合 $V\subseteq U$ が存在して $W=s(V)$ と表される事が分かるので
$$\pi|\_{s(U)}(W) = \pi|\_{s(U)}(s(V)) = \pi(s(V)) = V$$
である。よって$\left(\left(\pi|\_{s(U)}\right)^{-1}\right)^{-1}(W)$ は $X$ の開集合なので $\left(\pi|\_{s(U)}\right)^{-1}$ は連続。

$\square$
{{% /details %}}
