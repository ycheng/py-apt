
import apt.cache as ac

c = ac.Cache()

print(c)
p = c["apt"]
print(p)
print(p.architecture())
print(p.candidate)
print("Versions:")
for v in p.versions:
    print("\t", v)
    print("\t", v.policy_priority)
    print("\t", v.raw_description)
    print("\t", v.uri)
