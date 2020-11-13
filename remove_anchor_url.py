# Complete the function/method so that it returns the url with anything after the anchor (#) removed.

# Examples
# # returns 'www.codewars.com'
# remove_url_anchor('www.codewars.com#about')

# # returns 'www.codewars.com?page=1' 
# remove_url_anchor('www.codewars.com?page=1') 

def remove_url_anchor(url):
    url_strip = url.split("#", 1) #strips string at the first occurence of '#' into a list
    substring = url_strip[0] # take index 0 as a list to get the string before #

    return substring

url = "www.codewars.com#about"

print(remove_url_anchor(url))


    # CodeWars solution:
    #     def remove_url_anchor(url):
    #       return url.split('#')[0]