summary = 0

for i in range(2, 101, 2):
    summary += i

print(summary)

#--

summary2 = 0

for i in range(1, 101):
    if i % 2 == 0:
        summary2 +=i

print(summary2)