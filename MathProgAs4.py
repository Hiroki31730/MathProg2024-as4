# 課題d~fまでのコード
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# モデルの定義
model = pyo.ConcreteModel()

# 変数の定義
model.a = pyo.Var(domain=pyo.NonNegativeIntegers)
model.b = pyo.Var(domain=pyo.NonNegativeIntegers)
model.c = pyo.Var(domain=pyo.NonNegativeIntegers)
model.d = pyo.Var(domain=pyo.NonNegativeIntegers)

# maximizeの式の設定
def ObjRule(model):
    return 200*model.a + 150*model.b + 100*model.c + 100*model.d

# 条件をmaximizeとして式を設定する
model.obj = pyo.Objective(rule = ObjRule, sense = pyo.maximize)


# 制約1
def Construle1(model, sub1):
    return (10*model.a) + (5*model.b) + (0*model.c) + (0*model.d) <= sub1

# 制約2
def Construle2(model, sub2):
    return (0*model.a) + (3*model.b) + (8*model.c) + (2*model.d) <= sub2

# 制約3
def Construle3(model, sub3):
    return (0*model.a) + (2*model.b) + (2*model.c) + (8*model.d) <= sub3

#　保存するファイルネーム
output_filename = 'results_f.txt'

# ファイルに書き込む処理
with open(output_filename, 'w') as f:
    for x in range(21):
        # sub1~3とforの回数を変更することで、(d)~(f)を実現できる。
        sub1 = 1000
        sub2 = 2000-50*x
        sub3 = 3000
        
        # 制約の適用
        model.eq1 = pyo.Constraint(rule = Construle1(model, sub1))
        model.eq2 = pyo.Constraint(rule = Construle2(model, sub2))
        model.eq3 = pyo.Constraint(rule = Construle3(model, sub3))
        
        # glpkを用いて解く
        opt = pyo.SolverFactory('glpk')

        # solveを使って最適解を求める
        res = opt.solve(model)

        print('\n')
        print('optimum value = ', model.obj())
        print("a = ", model.a())
        print("b = ", model.b())
        print("c = ", model.c())
        print("d = ", model.d())
        # 書き込み
        f.write(f'{sub2},{pyo.value(model.obj)},{pyo.value(model.a)},{pyo.value(model.b)},{pyo.value(model.c)},{pyo.value(model.d)}\n')
