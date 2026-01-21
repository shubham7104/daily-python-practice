def check_access(user):
    if user.get("is_active"):
        if user.get("role") == "admin":
            if user.get("verified"):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
user_data = {"is_active": True, "role": "admin", "verified": True}
print(f"Access: {check_access(user_data)}")