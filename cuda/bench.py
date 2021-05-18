import os
import subprocess 

sizes = [102, 1020, 10200, 102000, 1020000, 10200000]

sizes = [10200]

sizes = list(range(102000, 102000*13, 102000))
# AA broken here
vars = ["AA", "NEWCACHE", "OPTIMIZE", "CACHELICM", "PHISTRUCT", "INLINE", "FORWARD"]

def run(CACHELICM, OPTIMIZE, FORWARD, INLINE, NEWCACHE, AA, PHISTRUCT, runs):
    if INLINE=="no": return
    print(f'CACHELICM={CACHELICM} OPTIMIZE={OPTIMIZE} FORWARD={FORWARD} INLINE={INLINE} NEWCACHE={NEWCACHE} AA={AA} PHISTRUCT={PHISTRUCT} make -B -j', flush=True)
    comp = subprocess.run(f'CACHELICM={CACHELICM} OPTIMIZE={OPTIMIZE} FORWARD={FORWARD} INLINE={INLINE} NEWCACHE={NEWCACHE} AA={AA} PHISTRUCT={PHISTRUCT} make -B -j', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    assert (comp.returncode == 0)
    for size in sizes:
        res = []
        for i in range(runs):
            res.append(os.popen("./rsbench -m event -l " + str(size) + "| grep \"Runtime\" | grep -e \"[0-9\.]*\" -o").read().strip())
            # print(res, flush=True)
        print(f'CACHELICM={CACHELICM} OPTIMIZE={OPTIMIZE} FORWARD={FORWARD} INLINE={INLINE} NEWCACHE={NEWCACHE} AA={AA} PHISTRUCT={PHISTRUCT} size={size}', "\t", "\t".join(res), flush=True)


def do(remain, set):
    if len(remain) == 0:
        # print(set)
        run(**set)
    else:
        strue = set.copy()
        strue[remain[0]] = "yes"
        do(remain[1:], strue)
        sfalse = set.copy()
        sfalse[remain[0]] = "no"
        do(remain[1:], sfalse)

do(vars[2:], {"runs":5, "AA":"no", "NEWCACHE": "no"})

#vars = ["AA", "NEWCACHE", "OPTIMIZE", "CACHELICM", "PHISTRUCT", "INLINE"]
#do(vars[2:], {"runs":5, "AA":"no", "NEWCACHE": "yes"})