from amplify import BinaryPoly, BinaryQuadraticModel, gen_symbols, Solver
from amplify.client import FixstarsClient

q = gen_symbols(BinaryPoly, 2)
f = 1 - q[0] * q[1]
model = BinaryQuadraticModel(f)

client = FixstarsClient()
client.token = "CxVcQ2gwOawevU/7itsRGkAph9wAXwck"
client.parameters.timeout = 1000    # タイムアウト1秒

solver = Solver(client)
result = solver.solve(model)
for solution in result:
    print(f"energy = {solution.energy}\nvalues = {solution.values}")