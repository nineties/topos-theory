---
title: 位相空間上の層
weight: 5
section: 4
toc: true
---

# 位相空間上の層

前層・層の概念は元々は位相空間上の数学的対象について調べる手段として誕生し、それを圏論的に一般化したものが前章の前層の定義である。本章では位相空間上の前層・層について説明していく。

最初に直感的なイメージの説明を行う。位相空間 $X$ 上の前層・層 $\mathcal{F}$ とは各開集合 $U\in\mathcal{O}(X)$ に集合 $\mathcal{F}(U)$ を紐づけるものであり、特定の条件を満たすものである。例えば $X$ を地球表面とした時 $\mathcal{F}$ は地球表面上の領域 $U$ に対して地図 $\mathcal{F}(U)$ を紐づけるものといったイメージである。

{{< figure src="../images/earth-and-map.png" width="30%" >}}

ここで **与えられた地図から範囲を狭めた新たな地図を作る整合的な操作** を備えたものを **前層(presheaf)** という。
すなわち、$U\supseteq V$ の時に、地図 $\mathcal{F}(U)$ の範囲を絞って $\mathcal{F}(V)$ を作る **制限写像(restriction map)** と呼ばれる写像 $\rho^U_V$ を備えており、これが範囲を絞る操作について整合的であるものである。

$$\xymatrix{
U \ar[r]^{\supseteq} \ar[d]^{\mathcal{F}} & V \ar[d]^{\mathcal{F}}\\\\
\mathcal{F}(U) \ar[r]^{\rho^U_V} & \mathcal{F}(V)
}$$

{{% definition title="位相空間上の前層" %}}
位相空間$X$ 上の層 $\mathcal{F}$ とは、各開集合 $U\in\mathcal{O}(X)$ に集合 $\mathcal{F}(U)$ を対応させるものであり、
任意の $U\supseteq V\ (U,V\in\mathcal{O}(X))$ に対して以下の条件を満たす **制限写像(restriction map)** 
$$ \rho^U_V: F(U)\rightarrow F(V) $$
を備えるものである。

1. $\rho^U_U$ は恒等写像である。
2. $U\supseteq V\supseteq W$ のとき、 $\rho^U_W = \rho^V_W\circ\rho^U_V$

{{% /definition %}}
