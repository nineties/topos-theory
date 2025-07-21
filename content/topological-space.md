---
title: 位相空間上の層
weight: 5
section: 4
toc: true
---

## 位相空間上の層

**前層(presheaf)** 及び **層(sheaf)** の概念は元々は位相空間上の数学的対象について調べる手段として誕生し、それを圏論的に一般化したものが前章の前層の定義である。本章では位相空間上の前層・層について説明していく。

位相空間 $X$ 上の前層・層 $F$ とは各開集合 $U\in\mathcal{O}(X)$ に集合 $F(U)$ を紐づけるものであり、特定の条件を満たすものである。例えば $X$ を地球表面とした時 $F$ は地球表面上の領域 $U$ に対して何らかの数学的対象 $F(U)$ を紐づけるものである。例えば地球表面上の温度分布に関心があるならば $F(U)$ は二次元の連続関数の集合といった感じである。
ここで注意したいのは $F$ は特定の状況を与えるものではなく、数学の舞台を設定するものである。温度分布の例で言うならば、$F(U)$ はあらゆる状況の集合であって元$s\in F(U)$ が特定の状況を表す。この元 $s$ のことを **切断(section)** と言う。

{{< figure src="../images/earth-and-map.png" width="30%" >}}

### 前層

位相空間 $X$ 上の前層とは **注目する範囲を狭める操作** を備えたものである。すなわち、$U\supseteq V$ の時に、$F(U)$ から $F(V)$ を作る **制限写像(restriction map)** と呼ばれる写像 $\rho^U_V$ を備えており、これが範囲を操作について整合的であるものである。

{{% definition title="位相空間上の前層" %}}
位相空間$X$ 上の層 $F$ とは、各開集合 $U\in\mathcal{O}(X)$ に集合 $F(U)$ を対応させるものであり、
任意の $U\supseteq V\ (U,V\in\mathcal{O}(X))$ に対して以下の条件を満たす **制限写像(restriction map)** 
$$ \rho^U_V: F(U)\rightarrow F(V) $$
を備えるものである。

1. $\rho^U_U$ は恒等写像である。
2. $U\supseteq V\supseteq W$ のとき、 $\rho^U_W = \rho^V_W\circ\rho^U_V$

$F(U)$ の元を **切断(section)** と呼ぶ。$s \in F(U)$ の時 $\rho^U_V(s)$ の代わりに $s|_V$ と書くこともある。
{{% /definition %}}

この定義は $X$ の開集合系 $\mathcal{O}(X)$ を包含関係 $\subseteq$ によって圏とみなした時 $F$ 及び $\rho$ が$\mathcal{O}(X)^{\mathrm{op}}$ から $\mathbf{Set}$ への関手であるといっている事に他ならず、圏論的な前層の定義と一致する。この時 $F(U\supseteq V) = \rho^U_V$ である。

### 層
前層のうち、局所的な数学対象を貼り合わせて大域的な数学対象を矛盾なく構成できるものを層という。

{{% definition title="位相空間上の層" %}}
位相空間 $X$ 上の前層 $F$ で以下の条件を満たすものを **層(sheaf)** という。

1. $X$ の任意の開集合 $U$ と、その開被覆 $U=\bigcup\_{\lambda\in\Lambda}U\_{\lambda}$、切断 $s,t\in F(U)$ について、全ての $\lambda\in \Lambda$ で $s|\_{U\_{\lambda}} = t|\_{U\_{\lambda}}$ であるならば $s = t$ である。

2. $X$ の任意の開集合 $U$ と、その開被覆 $U=\bigcup\_{\lambda\in\Lambda}U\_{\lambda}$、切断の族 $s\_{\lambda}\in F(U\_{\lambda})$ について、任意の $\alpha,\beta\in\Lambda$ で $s\_{\alpha}|\_{U\_{\alpha}\cap U\_{\beta}} = s\_{\beta}|\_{U\_{\alpha}\cap U\_{\beta}}$ であるならば、ある切断 $s\in F(U)$ が存在し全ての $\lambda\in\Lambda$ に対して $s|\_{U\_{\lambda}} = s\_{\lambda}$
{{% /definition %}}

1つめの条件は $F(U)$ の切断はその局所的な情報のみから一意に定まるということをいっている。2つめの条件は重なる部分で一致する切断は貼り合わせて一つの大きな切断にする事が出来るということをいっている。
