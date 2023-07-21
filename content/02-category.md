---
title: 2. 圏論的準備
section: 2
toc: true
---

{{% toc %}}

[元になったOlivia先生の講義スライド](https://www.oliviacaramello.com/Teaching/Lectures2_3_4.pdf)

## 圏論の概要
**圏論(category theory)** は、1942-45年にSamuel EilenbergとSaunders Mac Laneによって代数的位相幾何学の文脈で発明された数学の一分野であり、数学的概念を表現し議論するための抽象的な言語を提供する。
実際、圏論の諸概念は、それらの例を数学のあらゆる分野で見つけることができる統一的な概念である。
圏論に通底する哲学は、集合論を構成する、集合とその所属関係という原始的な概念を、集合と関数の概念を抽象化した、対象と射という概念で置き換えることである。

発明されて以来、このアプローチは数学者が自分の主題を捉える方法に深いパラダイムシフトをもたらし、以前ではほとんど不可能だった重要な発見への道を開いた。
圏論の大きな成果の一つがトポス理論であり、これは全面的に圏論の言語で書かれた理論である。

## 圏論の諸概念
### 圏

{{% definition title="圏" %}}
(小さな) **圏(category)** $\mathcal{C}$ は

- **対象(object)** の 集合 $\mathrm{Ob}(\mathcal{C})$
- 各 $a, b\in\mathrm{Ob}(\mathcal{C})$ に対して **射(arrow)** の集合 $\mathcal{C}(a,b)$
- 各 $a,b,c\in\mathrm{Ob}(\mathcal{C})$ に対して射の **合成(composition)**
$$ \mathcal{C}(a,b)\times\mathcal{C}(b,c)\ni(f,g)\mapsto g\circ f\in\mathcal{C}(a,c)$$

からなり、以下の2条件を満たすものである。

1. 任意の $f\in\mathcal{C}(a,b), g\in\mathcal{C}(b,c),h\in\mathcal{C}(c,d)$ に対して
    $$ h\circ(g\circ f) = (h\circ g)\circ f $$
    (よって 括弧を外して $h\circ g\circ f$ と書いても問題ない)
2. 任意の $a\in\mathrm{Ob}(\mathcal{C})$ について **恒等射(identity arrow)** $1_a\in\mathcal{C}(a,a)$ が存在し、任意の $f\in\mathcal{C}(a,b)$ について
    $$ f\circ 1_a = 1_b\circ f = f$$

$f \in\mathcal{C}(a,b)$ の代わりに、$f \in\mathrm{Hom}\_{\mathcal{C}}(a,b)$ や $f:a\rightarrow b$ とも書く。$a$ を $f$ の **ドメイン(domain)** と呼び $\mathrm{dom}(f)=a$ と書く。同様に、 $b$ を **コドメイン(codomain)** と呼び $\mathrm{cod}(f)=b$ と書く。

{{% /definition %}}

対象や射の集まりとして集合より大きな **類,クラス(class)** を用いる事でより大きな圏を考える事もできる。また、圏の定義は一階述語理論的な公理化も可能である。

{{% definition title="圏の一階述語論理的公理化" %}}

圏とは以下の6つの述語・関数及び等号をもち

- 一引数の述語 $\mathrm{Obj},\mathrm{Arr}$
- 一引数の関数 $\mathrm{Dom},\mathrm{Cod}$
- 一引数の関数 $\mathrm{Id}$
- 二引数の関数 $\circ$

以下の公理を満たすものである。

$$
\begin{align*}
& \forall f,\ \mathrm{Arr}(f) \Rightarrow \mathrm{Obj}(\mathrm{Dom}(f))\wedge\mathrm{Obj}(\mathrm{Cod}(f)) \\\\
& \forall f,g,\ (\mathrm{Arr}(f)\wedge\mathrm{Arr}(g)\wedge\mathrm{Cod}(f)=\mathrm{Dom}(g)) \\\\
& \Rightarrow\mathrm{Arr}(g\circ f)\wedge\mathrm{Dom}(g\circ f)=\mathrm{Dom}(f)\wedge\mathrm{Cod}(g\circ f)=\mathrm{Cod}(g) \\\\
& \forall a,\ \mathrm{Obj}(a)\Rightarrow\mathrm{Arr}(\mathrm{Id}(a))\wedge\mathrm{Dom}(\mathrm{Id}(a))=\mathrm{Cod}(\mathrm{Id}(a))=a \\\\
& \forall f,g,h,\ (\mathrm{Arr}(f)\wedge\mathrm{Arr}(g)\wedge\mathrm{Arr}(h)\wedge\mathrm{Cod}(f)=\mathrm{Dom}(g)\wedge\mathrm{Cod}(g)=\mathrm{Dom}(h) \\\\
& \Rightarrow h\circ(g\circ f)=(h\circ g)\circ f \\\\
& \forall f,a\ \mathrm{Arr}(f)\wedge\mathrm{Obj}(a) \\\\
& \Rightarrow(\mathrm{Dom}(f)=a\Rightarrow f\circ\mathrm{Id}(a)=f)\wedge(\mathrm{Cod}(f)=a\Rightarrow \mathrm{Id}(a)\circ f=f)
\end{align*}
$$
<font color="blue">(Olivia先生のスライドでは二引数関数 $\circ$ の代わりに合成に関する三引数の *述語* を用いると書いてある。$f,g$ を合成して $h=g\circ f$ となることを $\mathrm{Comp}(f, g, h)$ といった述語で表す公理系を指しているのだろう。) </font>

{{% /definition %}}

圏 $\mathcal{C}$ は

- $\mathrm{Obj}(a)$ を $a\in\mathrm{Ob}(\mathcal{C})$
- $\mathrm{Arr}(f)$ を $f\in\coprod_{a,b\in\mathrm{Ob}(\mathcal{C})}\mathcal{C}(a,b)$
- $\mathrm{Dom}(f)$ を $\mathrm{dom}(f)$、$\mathrm{Cod}(f)$ を $\mathrm{cod}(f)$
- $\mathrm{Id}(a)$ を $1_a$
- $\circ$ を $\circ$

と解釈することでこの公理系を満たす。
