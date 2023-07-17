---
title: 1. トポス理論の概要
section: 1
---

[元になったOlivia先生の講義スライド](https://www.oliviacaramello.com/Teaching/Lecture1.pdf)

# 統一概念としてのトポス

**トポス(Topos)** を発明した **アレクサンドル・グロタンディーク (A. Grothendieck)** はトポス理論のテーマを以下のように述べている。 <font color="blue"> (要確認: この文章の出自) </font>

> "It is the **topos** theme which is this “bed” or “deep river” where come to be married geometry and algebra, topology and arithmetic, mathematical logic and category theory, the world of the “continuous” and that of “discontinuous” or discrete structures. It is what I have conceived of most broad to perceive with finesse, by the same language rich of geometric resonances, an “essence” which is common to situations most distant from each other coming from one region or another of the vast universe of mathematical things".  **A. Grothendieck**

これを日本語に翻訳すると以下のようになるだろう。

> トポスのテーマとは、幾何学と代数学、位相空間と算術、数理論理学と圏論、そして「連続」の世界と「不連続」または離散的な構造の世界が結婚する「ベッド」や「深い川」といったものです。これは、幾何学的な共鳴に富んだ同じ言語によって、数学的なものの広大な宇宙のある領域、あるいは別の領域からやってきた、互いに最も離れた状況に共通する「本質」を精巧に知覚するために、私が最も広範に考察したものである。


トポス理論は、異なる数学理論間の関係を体系的に調査し、**多様な異なる視点** によってそれらを研究するための枠組みと大きく関連する **統一的な数学対象** とみなすことができる。

その方法は様々な分野に **横断的** であり、それぞれの専門的な技法を **補完** するものである。その一般性にもかかわらず、トポス理論的技法は、他の方法では到底到達できないような洞察を生み出し、 **異なる文脈間での知識の効果的な伝達** を可能にする深いつながりを確立する。このようなトポスの役割は、それが **多面的** な性質を持つことと結びついている。例えばトポスは

- 一般化された空間概念(Generalized space)
- 数学的宇宙(Mathematical universe)
- 理論(Theory)

などと見なすことが出来る。

# 簡単な歴史

- トポスはもともと、代数幾何学で必要とされる「エキゾチックな」コホモロジー理論に数学的裏付けを与えるために、1960年代初頭にアレクサンドル・グロタンディークによって発明された。すべての位相空間はトポスを生み出し、この意味でのトポスは **空間概念の一般化** と考える事ができる。

- 60年代後半に、ウィリアム・ローヴェア(William Lawvere)とマイルス・ティアニー(Myles Tierney)は、Grothendieck Toposという概念が、**数学宇宙** ももたらすことに気づいた。この宇宙では、馴染みのある集合論的な構成が行えるが、トポス固有の柔軟性のおかげで、特定の性質を持つ新しい数学世界を構築するのにも活用できる。

- 数年後、分類トポスの理論は、上述の視点にさらに基礎的な視点を加えた。トポスは一般化された空間概念や数学宇宙としてだけでなく、理論の同等性の一般的な概念まで考慮される **一階の理論** としても見なすことができる。

# 空間概念としてのトポス

Grothendieckは位相空間論や幾何学的な直観を、位相空間では無い対象を扱う分野に持ち込むことを目的としてトポスを発明した。Grothendieckは位相空間 $X$ の多くの重要な性質が、$\mathbf{Set}$ に値を持つ$X$上の **層(sheaf)** の圏 $\mathbf{Sh}(X)$ の不変性として自然に定式化出来ることに着目し、 位相空間 $X$ を小さな圏 $C$ と一般化された **被覆(covering)** $J$ のペア $(C,J)$ に置き換え、その上の層としてトポスを定義した。


$$
\xymatrix {
X \ar@{~>}[d] \ar@{.>}[r] & \mathbf{Sh}(X) \ar@{~>}[d] \\\\
(C,J) \ar@{.>}[r] & \mathbf{Sh}(C,J) \\\\
}
$$

{{% definition title="トポス理論的不変量" %}}
**トポス理論的不変量(Topos-theoretic invariant)** とは **圏同値(Categorical equivalence)** な圏の間で変わらないトポスの性質のことである。
{{% /definition %}}

トポスの間のGeometric morphism(<font color="blue">日本語訳不明)の概念は、トポス内のアーベル群やモジュールのカテゴリから一般的なコモロジー理論を構築するのに特に有用であることが示されている。これらのコホモロジー不変量は、現代の代数幾何学の発展に、そしてそれを超えて大きな影響を与えている。一方、基本群や高次ホモトピー群のようなホモトピー理論的な不変量は、トポスの不変量として定義することができる。これらはトポスの唯一の不変量ではなく、実際、代数的、論理的、幾何学的、またはそれ以外の性質のトポスの不変量は無数に存在する。

# 数学宇宙としてのトポス

