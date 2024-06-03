# Syntax is the grammar of programming language.
# Every programming language has the concept of identifier
# All the user defined names in a program (variable name, function name, class name)
# etc. are the identitfiers

# Rules for making an identifier
# 1. Identifier name must start with alphabet (not number)
A = 1  # Valid
Xy = 2 # Valid
# 1X = 3 # Invalid
X1 = 3 # Valid

# 2. Identifiers name are case sensitive
Abc = 2
abc = 1

# 3. We cannot use special symbols in identifier name
# a@ = 2 # Invalid
# !2 = 12 # Invalid
# a-b = 12 # Invalid


# 4. But we can use underscore in variable name
a_2 = 2
_a = 1
_ = 2
a___ = 12


# 5. Keywords can;t be used as identifier
# All those words which have special meaning in a programming language
# are called keywords
# Python has 36 such keywords
# and = 1
# for = 12
x = help("keywords")
print(x)


# Python syntax follows the concept if indentation to indicate a code block 
# rather than curly braces

a = 1
# if(a == 1){
#     print("It is True")
# }

if a == 1:
    print("This is True")