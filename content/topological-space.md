---
title: 位相空間上の層
weight: 5
section: 4
toc: true
---

## 位相空間上の層

**前層(presheaf)** 及び **層(sheaf)** の概念は元々は位相空間上の数学的対象について調べる手段として誕生し、それを圏論的に一般化したものが前章の前層の定義である。本章では位相空間上の前層・層について説明していく。

位相空間 $X$ 上の前層・層 $F$ とは各開集合 $U\in\mathcal{O}_X$ に集合 $F(U)$ を紐づけるものであり、特定の条件を満たすものである。例えば $X$ を地球表面とした時 $F$ は地球表面上の領域 $U$ に対して何らかの数学的対象 $F(U)$ を紐づけるものである。例えば地球表面上の温度分布に関心があるならば $F(U)$ は二次元の連続関数の集合といった感じである。
ここで注意したいのは $F$ は特定の状況を与えるものではなく、数学の舞台を設定するものである。温度分布の例で言うならば、$F(U)$ はあらゆる状況の集合であって元$s\in F(U)$ が特定の状況を表す。この元 $s$ のことを **切断(section)** と言う。

{{< figure src="../images/earth-and-map.png" width="50%" >}}

### 前層

位相空間 $X$ 上の前層とは **注目する範囲を狭める操作** を備えたものである。すなわち、$U\supseteq V$ の時に、$F(U)$ から $F(V)$ を作る **制限写像(restriction map)** と呼ばれる写像 $\rho^U_V$ を備えており、これが範囲を操作について整合的であるものである。

{{% definition title="位相空間上の前層" %}}
位相空間$X$ 上の層 $F$ とは、各開集合 $U\in\mathcal{O}_X$ に集合 $F(U)$ を対応させるものであり、
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
- 複素多様体上のホロモーフィック関数

などである。

### 層の圏論的定義

簡単なケースとして $U=U_1\cup U_2$ の場合を考えると、 $F$ が層であることは共通部分で一致する $s_1,s_2$ の組とそれを貼り合わせた $s\in F(U)$ が一対一に対応しており、

$$F(U) \simeq \\{(s_1, s_2) \in F(U_1)\times F(U_2) \mid \rho^{U_1}\_{U_1\cap U_2}(s_1) = \rho^{U_2}\_{U_1\cap U_2}(s_2)\\}$$

$s|\_{U_1}=s_1$ 及び $s|\_{U_2}=s_2$ を満たす射影 $\rho^U\_{U_1}: F(U)\rightarrow F(U_1)$ 及び $\rho^U\_{U_2}: F(U)\rightarrow F(U_2)$ が備わっているということなので、これは $\mathbf{Set}$ においてはイコライザを用いて

$$ F(U) \simeq \mathrm{eq}\left(\rho^{U_1}\_{U_1\cap U_2}, \rho^{U_2}\_{U_1\cap U_2}\right)$$

と書くことができる。より一般には任意の開被覆 $U=\bigcup\_{\lambda\in\Lambda}U\_{\lambda}$ に対して、全ての共通部分で一致する切断の族 $\\{s\_{\lambda}\\}$ とそれらを貼り合わせた $s\in F(U)$ が一対一に対応すると言う事である。この定義では切断 $s\in F(U)$ を明示的に使わないので、後に位相空間以外にも一般化する事が出来る。

{{% definition title="位相空間上の層(イコライザ利用)" %}}
位相空間 $X$ 上の層 $F$ が以下の条件を満たすときこれを **層(sheaf)** という。

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

この定義の状況を図示すると以下の様になる。 $J$ が余完備であるというのは任意の $U\_{\alpha},U\_{\beta}\in J$ に対して $U\_{\alpha}\cap U\_{\beta} \in J$ ということで、充満であるというのは開集合の間の包含関係を漏らさず $J$ に持ってきているということである。そして
$$\varprojlim\_{U\_{\lambda}\in J}U\_{\lambda} = \bigcup\_{U\_{\lambda}\in J}U\_{\lambda}$$
であるので、上記の定義は位相空間 $X$ 上での領域の貼り合わせと、対応する数学的対象 $\\{F(U\_{\lambda})\\}$ の貼り合わせが整合的であるという事を言っており、直感的にも理解しやすい定義となっている。

{{< figure src="../images/sheaf-using-continuous-functor.png" width="60%" >}}
