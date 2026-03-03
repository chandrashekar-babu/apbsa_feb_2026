from subprocess import Popen

p = Popen("ls")
print("Launched ls command: p =", p)

exit_code = p.wait()
print("exit_code = ", exit_code)

with Popen("/bin/date") as p:
    print("Launched date command: p =", p)

print("date command complete")
