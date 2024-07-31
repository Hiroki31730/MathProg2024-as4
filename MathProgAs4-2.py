# (g)と(h)を解くコード
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
def ObjRule1(model):
    return 200*model.a + 150*model.b + 100*model.c + 100*model.d

# maximizeの式の設定2
def ObjRule2(model):
    return 250*model.a + 150*model.b + 100*model.c + 70*model.d


# 制約1
def Construle1(model):
    return (10*model.a) + (5*model.b) + (0*model.c) + (0*model.d) <= 1000

# 制約2
def Construle2(model):
    return (0*model.a) + (3*model.b) + (8*model.c) + (2*model.d) <= 2000

# 制約3
def Construle3(model):
    return (0*model.a) + (2*model.b) + (2*model.c) + (8*model.d) <= 3000

# ファイルネームの設定
output_filename = 'results_h.txt'

# 書き込み
with open(output_filename, 'w') as f:
        # maximizeと制約の設定
        model.obj = pyo.Objective(rule = ObjRule1, sense = pyo.maximize)
        model.eq1 = pyo.Constraint(rule = Construle1)
        model.eq2 = pyo.Constraint(rule = Construle2)
        model.eq3 = pyo.Constraint(rule = Construle3)
        
        # glpkを使う
        opt = pyo.SolverFactory('glpk')

        # solveで解く
        res = opt.solve(model)
        print('\n')
        print('optimum value = ', model.obj())
        print("a = ", model.a())
        print("b = ", model.b())
        print("c = ", model.c())
        print("d = ", model.d())
        f.write(f'{200},{100},{pyo.value(model.obj)},{pyo.value(model.a)},{pyo.value(model.b)},{pyo.value(model.c)},{pyo.value(model.d)}\n')
        
        # maximizeの設定だけを変える
        model.obj = pyo.Objective(rule = ObjRule2, sense = pyo.maximize)
        model.eq1 = pyo.Constraint(rule = Construle1)
        model.eq2 = pyo.Constraint(rule = Construle2)
        model.eq3 = pyo.Constraint(rule = Construle3)

        opt = pyo.SolverFactory('glpk')


        res = opt.solve(model)
        print('\n')
        print('optimum value = ', model.obj())
        print("a = ", model.a())
        print("b = ", model.b())
        print("c = ", model.c())
        print("d = ", model.d())
        f.write(f'{250},{70}, {pyo.value(model.obj)},{pyo.value(model.a)},{pyo.value(model.b)},{pyo.value(model.c)},{pyo.value(model.d)}\n')