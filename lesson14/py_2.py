favorite_languages = { 
  'user_0': 'python', 
  'user_1': 'js', 
  'user_2': 'php', 
  'user_3': 'python', 
  }
language = favorite_languages['user_1'].title() 
print(f"User_1 favorite language is {language}.")
language_1 = favorite_languages['user_2'].title()
print(f"User_2 favorite language is {language_1}.")
print("=================================")
favorite_languages1 = { 
  "user_0": "python", 
  'user_1': "js", 
  'user_2': "php", 
  'user_3': 'python', 
  }
for name, language in favorite_languages1.items(): 
  print(f"{name.title()}'s favorite language is {language.title()}.")
