#task 1

def stutter(lst):
    return f"{lst[0]}{lst[1]}... {lst[0]}{lst[1]}... {lst}?"


print(stutter("incredible")) #incredible ---> in... in... incridible
print(stutter("enthusiastic"))
print(stutter("outstanding"))


#task 2

def relation_to_luke(lst):
    if lst == "Darth Vader":
        return "Luke,i am your father."
    elif lst == "Leila":
        return "Luke, i am your sister."
    elif lst == "Han":
        return "Luke, i am your brother in law."
    else:
        return "anDroid."

print(relation_to_luke("Darth Vader")) # ➞ "Luke, I am your father."
print(relation_to_luke("Leila")) # ➞ "Luke, I am your sister."
print(relation_to_luke("Han"))
print(relation_to_luke("robot"))

#task 3

def mood_today(list):
    if list == 'happy':
        return "Today, I am feeling happy"
    elif list == "sad":
        return "Today, I am feeling sad"
    elif list == "zor":
        return "Today, I am zor"
    else:
        return "Today, I am feeling neutral"
print(mood_today('happy')) #➞ "Today, I am feeling happy"
print(mood_today("sad"))
print(mood_today("zor"))
print(mood_today(" "))

# task 4
def count_vowels(list1):
    vowels = "eoaiu"
    amount = 0
    for x in list1:
        if x in vowels:
            amount += 1
    return amount
print(count_vowels('celebration')) #nechta glasniy bor ligini sanab beradi
print(count_vowels('Palm'))
print(count_vowels('Prediction'))