import json

with open('src/data/knowledgeBase.ts', 'r', encoding='utf-8') as f:
    text = f.read().replace('\r\n', '\n')

# 1. gaoshu-00-algebra-five-actions triggers
old_triggers = '''    "triggers": [
      "式中含二次三项式形如 x^2 + px + q（反常积分、二次型、有理积分）",
      "含根号差式形如 \\sqrt{A} - \\sqrt{B} 处于分子或分母",
      "数列或级数通项形如 \\frac{1}{n(n+k)} 或 \\frac{1}{n(n+1)(n+2)}",
      "极限与不等式证明中出现 e^x, \\ln(1+x), \\sin x, \\tan x 混合",
      "初等函数定义域、反函数与初等三角积化和差与和差化积"
    ],'''

new_triggers = '''    "triggers": [
      "式中含二次三项式形如 $x^2 + px + q$（反常积分、二次型、有理积分）",
      "含根号差式形如 $\\sqrt{A} - \\sqrt{B}$ 处于分子或分母",
      "数列或级数通项形如 $\\frac{1}{n(n+k)}$ 或 $\\frac{1}{n(n+1)(n+2)}$",
      "极限与不等式证明中出现 $e^x$, $\\ln(1+x)$, $\\sin x$, $\\tan x$ 混合",
      "初等函数定义域、反函数与初等三角积化和差与和差化积"
    ],'''

assert old_triggers in text, "old_triggers not found in knowledgeBase.ts"
text = text.replace(old_triggers, new_triggers)

# 2. gaoshu-q-2016-1-4
text = text.replace(
    '已知函数 $f(x) = \\begin{cases} x, & x \\le 0 \\\\ \\frac{1}{n}, & \\frac{1}{n+1} < x \\le \\frac{1}{n}, n=1, 2, \\dots \\end{cases}$，则 (\\quad)',
    '已知函数 $f(x) = \\begin{cases} x, & x \\le 0 \\\\ \\frac{1}{n}, & \\frac{1}{n+1} < x \\le \\frac{1}{n}, n=1, 2, \\dots \\end{cases}$，则（　　）'
)

# 3. gaoshu-q-2019-1-4
text = text.replace(
    '那么函数 $P(x,y)$ 可取为 (\\quad)',
    '那么函数 $P(x,y)$ 可取为（　　）'
)

# 4. gaoshu-q-2017-1-10
text = text.replace(
    '"id": "gaoshu-q-2017-1-10",\n          "year": "2017",\n          "category": "数一",\n          "questionNumber": "10",\n          "source": "2017年全国硕士研究生招生考试数学（一）第10题",\n          "difficulty": "3星",\n          "content": "已知曲线 $C: y = \\int_0^x \\sqrt{\\cos 2t} \\, dt$ ($0 \\le x \\le \\frac{\\pi}{4}$)，则曲线 $C$ 的弧长为 $\\\\underline{\\\\hspace{3em}}$。",\n          "answer": "\\pi / 2"',
    '"id": "gaoshu-q-2017-1-10",\n          "year": "2017",\n          "category": "数一",\n          "questionNumber": "10",\n          "source": "2017年全国硕士研究生招生考试数学（一）第10题",\n          "difficulty": "3星",\n          "content": "已知曲线 $C: y = \\int_0^x \\sqrt{\\cos 2t} \\, dt$ ($0 \\le x \\le \\frac{\\pi}{4}$)，则曲线 $C$ 的弧长为 $\\\\underline{\\\\hspace{3em}}$。",\n          "answer": "$\\\\frac{\\\\pi}{2}$"'
)

# 5. gaoshu-q-2020-1-17
text = text.replace(
    '"id": "gaoshu-q-2020-1-17",\n          "year": "2020",\n          "category": "数一",\n          "questionNumber": "17",\n          "source": "2020年全国硕士研究生招生考试数学（一）第17题",\n          "difficulty": "4星",\n          "content": "求函数 $f(x,y) = x^2 + 4y^2 - 4x - 8y + 5$ 在区域 $D = \\\\{(x,y) \\\\mid x^2 + y^2 \\\\le 1, x \\\\ge 0, y \\\\ge 0\\\\}$ 上的最大值和最小值。",\n          "answer": "9 - 5\\sqrt{3}"',
    '"id": "gaoshu-q-2020-1-17",\n          "year": "2020",\n          "category": "数一",\n          "questionNumber": "17",\n          "source": "2020年全国硕士研究生招生考试数学（一）第17题",\n          "difficulty": "4星",\n          "content": "求函数 $f(x,y) = x^2 + 4y^2 - 4x - 8y + 5$ 在区域 $D = \\\\{(x,y) \\\\mid x^2 + y^2 \\\\le 1, x \\\\ge 0, y \\\\ge 0\\\\}$ 上的最大值和最小值。",\n          "answer": "$9 - 5\\\\sqrt{3}$"'
)

# 6. gaoshu-q-2022-1-9
text = text.replace(
    '"id": "gaoshu-q-2022-1-9",\n          "year": "2022",\n          "category": "数一",\n          "questionNumber": "9",\n          "source": "2022年全国硕士研究生招生考试数学（一）第9题",\n          "difficulty": "3星",\n          "content": "设 $I = \\int_0^1 dx \\int_x^1 \\frac{\\sin y}{y} \\, dy$，则 $I = \\\\underline{\\\\hspace{3em}}$。",\n          "answer": "1 - \\cos 1"',
    '"id": "gaoshu-q-2022-1-9",\n          "year": "2022",\n          "category": "数一",\n          "questionNumber": "9",\n          "source": "2022年全国硕士研究生招生考试数学（一）第9题",\n          "difficulty": "3星",\n          "content": "设 $I = \\int_0^1 dx \\int_x^1 \\frac{\\sin y}{y} \\, dy$，则 $I = \\\\underline{\\\\hspace{3em}}$。",\n          "answer": "$1 - \\\\cos 1$"'
)

# 7. gaoshu-q-2021-1-11
text = text.replace(
    '"id": "gaoshu-q-2021-1-11",\n          "year": "2021",\n          "category": "数一",\n          "questionNumber": "11",\n          "source": "2021年全国硕士研究生招生考试数学（一）第11题",\n          "difficulty": "3星",\n          "content": "计算三重积分 $\\iiint_{\\Omega} (x^2 + y^2) \\, dV$，其中 $\\Omega$ 是球面 $x^2 + y^2 + z^2 = R^2$ 所围成的闭区域。",\n          "answer": "8\\pi R^5 / 15"',
    '"id": "gaoshu-q-2021-1-11",\n          "year": "2021",\n          "category": "数一",\n          "questionNumber": "11",\n          "source": "2021年全国硕士研究生招生考试数学（一）第11题",\n          "difficulty": "3星",\n          "content": "计算三重积分 $\\iiint_{\\Omega} (x^2 + y^2) \\, dV$，其中 $\\Omega$ 是球面 $x^2 + y^2 + z^2 = R^2$ 所围成的闭区域。",\n          "answer": "$\\\\frac{8}{15}\\\\pi R^5$"'
)

# 8. gaoshu-q-2021-1-18
text = text.replace(
    '"id": "gaoshu-q-2021-1-18",\n          "year": "2021",\n          "category": "数一",\n          "questionNumber": "18",\n          "source": "2021年全国硕士研究生招生考试数学（一）第18题",\n          "difficulty": "4星",\n          "content": "计算曲面积分 $I = \\iint_S (x+z)\\,dy\\,dz + (y+z)\\,dz\\,dx + (z+x)\\,dx\\,dy$，其中 $S$ 为平面 $x+y+z=1$ 在第一卦限部分的上侧。",\n          "answer": "3\\pi / 2"',
    '"id": "gaoshu-q-2021-1-18",\n          "year": "2021",\n          "category": "数一",\n          "questionNumber": "18",\n          "source": "2021年全国硕士研究生招生考试数学（一）第18题",\n          "difficulty": "4星",\n          "content": "计算曲面积分 $I = \\iint_S (x+z)\\,dy\\,dz + (y+z)\\,dz\\,dx + (z+x)\\,dx\\,dy$，其中 $S$ 为平面 $x+y+z=1$ 在第一卦限部分的上侧。",\n          "answer": "$\\\\frac{3\\\\pi}{2}$"'
)

# 9. gaoshu-q-2016-1-11
text = text.replace(
    '"id": "gaoshu-q-2016-1-11",\n          "year": "2016",\n          "category": "数一",\n          "questionNumber": "11",\n          "source": "2016年全国硕士研究生招生考试数学（一）第11题",\n          "difficulty": "3星",\n          "content": "计算曲线积分 $I = \\oint_L (y-z)\\,dx + (z-x)\\,dy + (x-y)\\,dz$，其中 $L$ 为圆周 $x^2+y^2+z^2=a^2, x+y+z=0$ 从 $z$ 轴正向看去为逆时针方向。",\n          "answer": "-6\\pi"',
    '"id": "gaoshu-q-2016-1-11",\n          "year": "2016",\n          "category": "数一",\n          "questionNumber": "11",\n          "source": "2016年全国硕士研究生招生考试数学（一）第11题",\n          "difficulty": "3星",\n          "content": "计算曲线积分 $I = \\oint_L (y-z)\\,dx + (z-x)\\,dy + (x-y)\\,dz$，其中 $L$ 为圆周 $x^2+y^2+z^2=a^2, x+y+z=0$ 从 $z$ 轴正向看去为逆时针方向。",\n          "answer": "$-6\\\\pi$"'
)

# 10. gaoshu-q-2023-1-19
text = text.replace(
    '"answer": "S(x) = \\\\frac{1}{2}\\\\ln\\\\frac{1+x}{1-x}, \\\\quad \\\\text{和为 } \\\\frac{\\\\sqrt{3}}{2}\\\\ln(2+\\\\sqrt{3})"',
    '"answer": "$S(x) = \\\\frac{1}{2}\\\\ln\\\\frac{1+x}{1-x}$，和为 $\\\\frac{\\\\sqrt{3}}{2}\\\\ln(2+\\\\sqrt{3})$"'
)

# 11. gaoshu-q-2016-1-13
text = text.replace(
    '"id": "gaoshu-q-2016-1-13",\n          "year": "2016",\n          "category": "数一",\n          "questionNumber": "13",\n          "source": "2016年全国硕士研究生招生考试数学（一）第13题",\n          "difficulty": "3星",\n          "content": "设向量 $\\\\boldsymbol{a} = (1, 1, 1)$, $\\\\boldsymbol{b} = (1, 0, -1)$，则以 $\\\\boldsymbol{a}, \\\\boldsymbol{b}$ 为邻边的平行四边形的面积为 $\\\\underline{\\\\hspace{3em}}$。",\n          "answer": "\\\\sqrt{3}"',
    '"id": "gaoshu-q-2016-1-13",\n          "year": "2016",\n          "category": "数一",\n          "questionNumber": "13",\n          "source": "2016年全国硕士研究生招生考试数学（一）第13题",\n          "difficulty": "3星",\n          "content": "设向量 $\\\\boldsymbol{a} = (1, 1, 1)$, $\\\\boldsymbol{b} = (1, 0, -1)$，则以 $\\\\boldsymbol{a}, \\\\boldsymbol{b}$ 为邻边的平行四边形的面积为 $\\\\underline{\\\\hspace{3em}}$。",\n          "answer": "$\\\\sqrt{3}$"'
)

# 12. gaoshu-q-2019-1-15
text = text.replace(
    '"id": "gaoshu-q-2019-1-15",\n          "year": "2019",\n          "category": "数一",\n          "questionNumber": "15",\n          "source": "2019年全国硕士研究生招生考试数学（一）第15题",\n          "difficulty": "4星",\n          "content": "设函数 $y(x)$ 满足微分方程 $y\'\' - 2y = 0$，且 $y(0) = 0, y\'(0) = 1$，求 $y(x)$。",\n          "answer": "\\\\frac{1}{2\\\\sqrt{2}}(e^{\\\\sqrt{2}x} - e^{-\\\\sqrt{2}x})"',
    '"id": "gaoshu-q-2019-1-15",\n          "year": "2019",\n          "category": "数一",\n          "questionNumber": "15",\n          "source": "2019年全国硕士研究生招生考试数学（一）第15题",\n          "difficulty": "4星",\n          "content": "设函数 $y(x)$ 满足微分方程 $y\'\' - 2y = 0$，且 $y(0) = 0, y\'(0) = 1$，求 $y(x)$。",\n          "answer": "$\\\\frac{1}{2\\\\sqrt{2}}(e^{\\\\sqrt{2}x} - e^{-\\\\sqrt{2}x})$"'
)

# 13. gaoshu-q-2021-1-10
text = text.replace(
    '"answer": "(f_1\' + f_2\' + y f_3\')dx + (f_1\' - f_2\' + x f_3\')dy"',
    '"answer": "$(f_1\' + f_2\' + y f_3\')\\\\,dx + (f_1\' - f_2\' + x f_3\')\\\\,dy$"'
)

with open('src/data/knowledgeBase.ts', 'w', encoding='utf-8', newline='\n') as f:
    f.write(text)

print("knowledgeBase.ts successfully fixed!")
