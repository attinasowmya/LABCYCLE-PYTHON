def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
            
# driver code
string = "geeks for geeks"
sub_str ="geek"
check(string, sub_str)
