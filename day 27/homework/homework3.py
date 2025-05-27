def password(password):
    if len(password) < 8:
        return "please long password"
    else:
        return "password is ok"
    
print(password("saba062saba"))