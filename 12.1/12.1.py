import codecs
import re
def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
      text = re.sub(r'<[^>]+>', '', html)
      cleaned_text = re.sub(r'\s+', ' ', text).strip()
      with codecs.open(result_file, 'w', 'utf-8') as result:
          result.write(cleaned_text)
          print(cleaned_text)
delete_html_tags('C:/Users/aswat/Downloads/draft.html', 'C:/Users/aswat/Downloads/cleaned.txt')