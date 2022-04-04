#Try It Yourself Excercises 2-3 to 2-7

#2-3 PERSONAL MESSAGE
print("\n2-3")
name = "Thuy Tran"
message = f"Hello {name}, would you like to learn Python with me?"
print(message)

#2-4 NAME CASES
print("\n2-4")
name = "thuy tran"
print(name.title())
print(name.upper())
print(name.lower())

#2-5 FAMOUS QUOTE
print("\n2-5")
nye_quote = 'Bill Nye once said, "The more you find out about the world, the more opportunities there are to laugh at it."'
print(f"{nye_quote}")

#2-6 FAMOUS QUOTE 2
print("\n2-6")
famous_person = "bill nye"
famous_quote = '"The more you find out about the world, the more opportunities there are to laugh at it."'
message = f"{famous_person.title()} once said, {famous_quote}"
print(message)

#2-7 STRIPPING NAMES
print("\n2-7")
name = "     'Garett Bidus'         "
message = "is my friend!"
print(f"{name} {message}")
#using lstrip(),rstrip(),strip()
print(f"{name.lstrip()} {message} -left trim-\n{name.rstrip()} {message} -right trim-\n{name.strip()} {message} -trim both sides-\n\n\n\t\t\t\t{name.strip()} {message} -new lines & tab combination")