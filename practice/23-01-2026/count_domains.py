def get_domain_counts(emails):
    """
    Question 1: The Domain Counter
    Input: A list of email strings.
    Output: A dictionary where the keys are domains (like 'gmail.com') 
            and values are how many times they appeared.
    
    Example: ["a@b.com", "c@b.com", "d@e.com"] -> {"b.com": 2, "e.com": 1}
    """
    counts = {}
    for mail in emails:
        b = 0
        # print(mail)
        for i in mail:  
                b += 1
                if i == "@":
                        break
        # print(mail[(b-1)::])
        domains = mail[(b-1)::]
        
        if domains not in counts:
                counts[domains] = 1
        else:
                counts[domains]  += 1
    return counts

emails = ["dev@python.org", "student@gmail.com", "admin@python.org", "user@yahoo.com"]
print(f"Result: {get_domain_counts(emails)}") 


'''
this above code can be written in more professional way
'''