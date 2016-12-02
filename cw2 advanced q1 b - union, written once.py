string1 = ['p', 'w', 'q', 'r', 'w', 'a', 'y', 'g', 'z', 'v']
string2 = ['e', 'w', 'u', 't', 'x', 'o', 'u', 'a', 'p', 'a']

def unionString(s1, s2):
    s3 = string1 + string2  # concatenates both lists into one
    s3 = set(s3)            # converts concatenaton to set so each element is written once
    return s3

print(unionString(string1, string2))
