
def fn():
    x = [100]
    print(id(x))
    print(x[0] + 1)

fn()
print("-----")
fn()

fn()