# 创建一个疯狂填词（Mad Libs）程序。
# 它将读入文本文件，并让用户在该文本文件中出现ADJECTIVE、NOUN、ADVERB或VERB等单词的地方，加上他们自己的文本。
# 例如，一个文本文件可能看起来像这样：
# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN wasunaffected by these events.
# 程序将找到这些出现的单词，并提示用户取代它们。
# 程序将找到这些出现的单词，并提示用户取代它们。
# Enter an adjective:
# silly
# Enter a noun:
# chandelier
# Enter a verb:
# screamed
# Enter a noun:
# pickup truck
# 以下的文本文件将被创建：
# The silly panda walked to the chandelier and then screamed. A nearby pickuptruck was unaffected by these events.
# 结果应该打印到屏幕上，并保存为一个新的文本文件。

preFile = open('eighthPractice_2.txt')
content = str(preFile.read())
words = content.split(' ')
newWords = []
for word in words:
    if 'noun' in word.lower():
        print('Enter a noun:')
        newWord = word.replace('NOUN', input())
        newWords.append(newWord)
    elif 'adjective' in word.lower():
        print('Enter an adjective:')
        newWord = word.replace('ADJECTIVE', input())
        newWords.append(newWord)
    elif 'verb' in word.lower():
        print('Enter a verb:')
        newWord = word.replace("VERB", input())
        newWords.append(newWord)
    else:
        newWords.append(word)
        continue
    

newStr = ' '.join(newWords)
print(newStr)
preFile.close()
newFile = open('eighthPractice_2_new.txt', 'w')
newFile.write(newStr)
newFile.close()