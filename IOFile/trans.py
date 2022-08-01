from translate import Translator
translator= Translator(to_lang="vi")
# translation = translator.translate("This is a pen.")
# print(translation)

file = open('./sample.txt', 'r')
content = ''
for each in file:
    content += translator.translate(each)
    content += '\n'
file.close()
fileOut = open('translatedFile.txt', 'w')
fileOut.write(content)
fileOut.close()
# print(content)
    
    
