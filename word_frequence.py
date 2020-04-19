import html2text
import requests
import re
def word_frequencies(url):
    # Create html2text for parse raw html
    html2text_handler = html2text.HTML2Text()
    # Set flag
    html2text_handler.ignore_links = True
    html2text_handler.ignore_emphasis = True
    html2text_handler.no_wrap_links = True
    # Get html content from url
    html_lines = requests.get(url).text
    # Remove html tags from content
    texts = html2text_handler.handle(html_lines)
    # Split words by space and remove special character
    words_list = texts.split()
    words_list_temp = []
    for word in words_list:
        string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:-]')
        if (string_check.search(word) == None):
            words_list_temp.append(word)
    words_list = words_list_temp
    # Count frequent of each words
    dict_frequency = {item : words_list.count(item) for item in words_list}
    # Sort words by frequency
    sorted_frequency = sorted(dict_frequency.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
    return sorted_frequency
print(word_frequencies("https://www.google.com/"))