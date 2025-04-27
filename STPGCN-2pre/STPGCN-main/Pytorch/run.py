import os
#
os.system("python HKIn_noweighted.py --max_epoch=100 --rid=1 --seed=1 --L=3 --a=4 --b=2 --d=8 --data=Haikou --batch=32 --C=64 --workname=STPGCN-Haikou")
os.system("python HKIn_weighted.py --max_epoch=100 --rid=1 --seed=1 --L=3 --a=4 --b=2 --d=8 --data=Haikou --batch=32 --C=64 --workname=STPGCN-Haikou")
os.system("python HKOut_noweighted.py --max_epoch=100 --rid=1 --seed=1 --L=3 --a=4 --b=2 --d=8 --data=Haikou --batch=32 --C=64 --workname=STPGCN-Haikou")
os.system("python HKOut_weighted.py --max_epoch=100 --rid=1 --seed=1 --L=3 --a=4 --b=2 --d=8 --data=Haikou --batch=32 --C=64 --workname=STPGCN-Haikou")

# os.system("python SZIn_noweighted.py --max_epoch=100 --rid=1 --seed=1 --L=3 --a=4 --b=2 --d=8 --data=Shenzhen --batch=32 --C=64 --workname=STPGCN-Shenzhen")
# os.system("python SZIn_weighted.py --max_epoch=100 --rid=1 --seed=1 --L=3 --a=4 --b=2 --d=8 --data=Shenzhen --batch=32 --C=64 --workname=STPGCN-Shenzhen")
# os.system("python SZOut_noweighted.py --max_epoch=100 --rid=1 --seed=1 --L=3 --a=4 --b=2 --d=8 --data=Shenzhen --batch=32 --C=64 --workname=STPGCN-Shenzhen")
# os.system("python SZOut_weighted.py --max_epoch=100 --rid=1 --seed=1 --L=3 --a=4 --b=2 --d=8 --data=Shenzhen --batch=32 --C=64 --workname=STPGCN-Shenzhen")