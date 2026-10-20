import os, fitz, re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

pdfs = sorted([f for f in os.listdir('.') if f.endswith('.pdf')])
doc0 = fitz.open(pdfs[0])
doc1 = fitz.open(pdfs[1])

print(f"Doc0: {len(doc0)} pages, Doc1: {len(doc1)} pages")

# Lecture to Topic ID mapping
LECTURE_TOPIC_MAP = {
    3: "gaoshu-01-indeterminate-0-0",
    4: "gaoshu-01-infinitesimal-order",
    5: "gaoshu-01-power-exponential-1-inf",
    6: "gaoshu-01-sequence-monotone-bounded",
    7: "gaoshu-01-discontinuity-points",
    8: "gaoshu-02-derivative-definition",
    9: "gaoshu-02-higher-order-leibniz",
    10: "gaoshu-02-mean-value-theorems",
    11: "gaoshu-01-difference-inf-inf",
    12: "gaoshu-02-taylor-formula-proof",
    13: "gaoshu-01-indeterminate-0-0",
    14: "gaoshu-02-inequality-and-roots",
    15: "gaoshu-02-inequality-and-roots",
    16: "gaoshu-03-variable-limit-integral",
    17: "gaoshu-03-definite-integral-symmetry",
    18: "gaoshu-03-variable-limit-integral",
    19: "gaoshu-03-definite-integral-symmetry",
    20: "gaoshu-03-improper-integral-convergence",
    21: "gaoshu-03-geometric-applications",
    22: "gaoshu-03-geometric-applications",
    23: "gaoshu-10-cross-taylor-proofs",
    24: "gaoshu-04-first-order-ode",
    25: "gaoshu-04-second-order-constant-coeff",
    26: "gaoshu-04-euler-equation",
    27: "gaoshu-04-first-order-ode",
    28: "gaoshu-09-vector-products-geometry",
    29: "gaoshu-05-differentiability-concept",
    30: "gaoshu-05-chain-rule-composite",
    31: "gaoshu-09-plane-and-line-equations",
    32: "gaoshu-05-lagrange-multipliers",
    33: "gaoshu-06-double-integral-polar",
    34: "gaoshu-06-triple-integral-coordinates",
    35: "gaoshu-07-curvilinear-path-independent",
    36: "gaoshu-07-gauss-divergence-theorem",
    37: "gaoshu-07-stokes-theorem-curl",
    38: "gaoshu-08-series-convergence-tests",
    39: "gaoshu-08-series-convergence-tests",
    40: "gaoshu-08-power-series-radius-interval",
    41: "gaoshu-08-power-series-summation",
    42: "gaoshu-08-fourier-series-dirichlet",
    43: "xiandai-01-determinant-calc-techniques",
    44: "xiandai-02-adjoint-matrix-properties",
    45: "xiandai-02-elementary-matrix-operations",
    46: "xiandai-03-linear-independence-proof",
    47: "xiandai-04-solution-structure-and-rank",
    48: "xiandai-04-matrix-equation-and-common-solutions",
    49: "xiandai-05-eigenvalue-eigenvector-properties",
    50: "xiandai-06-diagonalization-criterion",
    51: "xiandai-06-real-symmetric-orthogonal-diag",
    52: "xiandai-07-quadratic-form-canonical",
    53: "xiandai-08-ab-zero-deep-dive",
    54: "gailv-01-total-probability-bayes",
    55: "gailv-02-distribution-function-properties",
    56: "gailv-02-function-distribution-one-dim",
    57: "gailv-03-joint-marginal-conditional",
    58: "gailv-03-random-variable-functions-2d",
    59: "gailv-04-expectation-egx-formulas",
    60: "gailv-05-chebyshev-inequality",
    61: "gailv-06-three-sampling-distributions",
    62: "gailv-07-moment-and-mle-estimation",
    63: "gailv-07-unbiasedness-eval-criteria"
}

# Fine-grained topic assignment based on keyword matching
def refine_topic_id(lec_num, default_tid, text, title):
    combined = (title + " " + text).lower()
    if lec_num == 3:
        if "单调有界" in combined or "数列" in combined or "子列" in combined:
            return "gaoshu-01-sequence-monotone-bounded"
        return "gaoshu-01-indeterminate-0-0"
    elif lec_num == 4:
        if "无穷小" in combined or "阶" in combined or "等价" in combined:
            return "gaoshu-01-infinitesimal-order"
        return "gaoshu-01-indeterminate-0-0"
    elif lec_num == 5:
        if "1^∞" in combined or "幂指" in combined:
            return "gaoshu-01-power-exponential-1-inf"
        return "gaoshu-01-indeterminate-0-0"
    elif lec_num == 7:
        if "间断" in combined or "连续" in combined:
            return "gaoshu-01-discontinuity-points"
        return "gaoshu-02-mean-value-theorems"
    elif lec_num == 10:
        return "gaoshu-02-mean-value-theorems"
    elif lec_num == 11:
        if "∞ - ∞" in combined or "差" in combined:
            return "gaoshu-01-difference-inf-inf"
        return "gaoshu-01-indeterminate-0-0"
    elif lec_num == 14 or lec_num == 15:
        return "gaoshu-02-inequality-and-roots"
    elif lec_num == 18:
        if "变限" in combined or "积分上限" in combined:
            return "gaoshu-03-variable-limit-integral"
        return "gaoshu-03-definite-integral-symmetry"
    elif lec_num == 25:
        if "可降阶" in combined or "降阶" in combined:
            return "gaoshu-04-reducible-ode"
        return "gaoshu-04-second-order-constant-coeff"
    elif lec_num == 28:
        if "平面" in combined or "直线" in combined:
            return "gaoshu-09-plane-and-line-equations"
        elif "曲面" in combined or "投影" in combined:
            return "gaoshu-09-surfaces-and-projections"
        return "gaoshu-09-vector-products-geometry"
    elif lec_num == 30:
        if "隐函数" in combined:
            return "gaoshu-05-implicit-function-differentiation"
        return "gaoshu-05-chain-rule-composite"
    elif lec_num == 33:
        if "交换" in combined or "次序" in combined or "对称性" in combined:
            return "gaoshu-06-order-exchange-symmetry"
        return "gaoshu-06-double-integral-polar"
    elif lec_num == 35:
        if "格林" in combined or "路径无关" in combined or "第二类" in combined:
            return "gaoshu-07-curvilinear-path-independent"
        return "gaoshu-07-green-formula-hole-technique"
    elif lec_num == 43:
        if "余子式" in combined or "展开" in combined:
            return "xiandai-01-cofactor-sum-expansion"
        return "xiandai-01-determinant-calc-techniques"
    elif lec_num == 44:
        if "高次幂" in combined or "a^n" in combined:
            return "xiandai-02-matrix-power-calculation"
        return "xiandai-02-adjoint-matrix-properties"
    elif lec_num == 46:
        if "极大线性无关" in combined or "等价" in combined or "秩" in combined:
            return "xiandai-03-maximal-linearly-independent-set"
        return "xiandai-03-linear-independence-proof"
    elif lec_num == 48:
        return "xiandai-04-matrix-equation-and-common-solutions"
    elif lec_num == 49:
        if "秩一" in combined or "αβ^t" in combined:
            return "xiandai-05-rank-one-eigenvalues"
        return "xiandai-05-eigenvalue-eigenvector-properties"
    elif lec_num == 51:
        return "xiandai-06-real-symmetric-orthogonal-diag"
    elif lec_num == 52:
        if "正定" in combined:
            return "xiandai-07-positive-definite-criteria"
        return "xiandai-07-quadratic-form-canonical"
    elif lec_num == 53:
        if "ab=o" in combined or "ab=0" in combined:
            return "xiandai-08-ab-zero-deep-dive"
        return "xiandai-08-cross-rank-eigen-systems"
    elif lec_num == 54:
        if "独立" in combined or "伯努利" in combined:
            return "gailv-01-event-independence-bernoulli"
        return "gailv-01-total-probability-bayes"
    elif lec_num == 55:
        if "正态" in combined or "指数" in combined or "均匀" in combined or "分布" in combined:
            return "gailv-02-common-distributions-standard"
        return "gailv-02-distribution-function-properties"
    elif lec_num == 58:
        return "gailv-03-random-variable-functions-2d"
    elif lec_num == 59:
        if "协方差" in combined or "相关系数" in combined or "方差" in combined:
            return "gailv-04-variance-covariance-correlation"
        return "gailv-04-expectation-egx-formulas"
    elif lec_num == 60:
        if "中心极限" in combined:
            return "gailv-05-central-limit-theorems"
        return "gailv-05-chebyshev-inequality"
    elif lec_num == 61:
        if "正态总体" in combined or "抽样定理" in combined:
            return "gailv-06-normal-population-sample-theorems"
        return "gailv-06-three-sampling-distributions"
    elif lec_num == 62:
        if "无偏" in combined or "有效" in combined:
            return "gailv-07-unbiasedness-eval-criteria"
        return "gailv-07-moment-and-mle-estimation"
    elif lec_num == 63:
        return "gailv-07-unbiasedness-eval-criteria"

    return default_tid

print("Refine topic rules defined successfully.")
