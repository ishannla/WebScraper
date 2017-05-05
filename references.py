# REMEMBER THAT FIND_ALL RETURNS A RESULT-SET OBJECT

# item.contents       RETURNS A LIST OF ALL THE CLASSES WITH THE SAME NAME

# print(link) vs. print(link.text)  PRINTS THE ENTIRE LINE VS JUST THE TEXT/DATA INSIDE

# print("<a href='%s'>%s</a>" %(link.get("href"), link.text)) PRINTING TEXT IN HREF FORMAT

# print("string one = %s string two = %s" %("1", "2"))  CONCATENATION

# print(link.get("href"))           EXTRACTING URLS WITHIN <A> HYPERLINK TAG

# print(soup.find_all("a"))      FINDING ALL TAGS OF CERTAIN TYPE

# print(soup.prettify())            MAKING HTML DATA A BIT PRETTIER

# ____________________________________________________________________________________________-