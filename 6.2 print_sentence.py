# 在位于屏幕中央且宽度合适的方框内打印输入的句子

sentence = input("Input a sentence: ")

screen_width = 80
max_text_width = screen_width - 4
text_width = len(sentence)
if text_width > max_text_width:
    box_width = screen_width
    left_margin = 0
    if text_width % max_text_width > 0:
        sentence_lines = text_width//max_text_width + 1
    else:
        sentence_lines = text_width//max_text_width
else:    
    box_width = text_width + 4
    left_margin = (screen_width - box_width) // 2
    sentence_lines = 1


print()
print(' ' * left_margin + '+' + '-' * (box_width-2) +  '+')

if sentence_lines == 1:
    print(' ' * left_margin + '| ' + ''.center(text_width)   + ' |')
    print(' ' * left_margin + '| ' + sentence + ' |')
    print(' ' * left_margin + '| ' + ' ' * text_width   + ' |')
else :
    print(' ' * left_margin + '| ' + ''.center(max_text_width)   + ' |')
    for line in range(0, sentence_lines):
        if line < sentence_lines - 1 :
            print(' ' * left_margin + '| ' + sentence[line*max_text_width:(line+1)*max_text_width] + ' |')
        elif line == sentence_lines - 1 :
            if text_width % max_text_width > 0:
                last_line_lenth = text_width % max_text_width
                last_line_remain = max_text_width - (text_width % max_text_width)
            else:
                last_line_lenth = max_text_width
                last_line_remain = 0
            print(' ' * left_margin + '| ' + sentence[-last_line_lenth:] + ' '*last_line_remain +' |')
    print(' ' * left_margin + '| ' + ' ' * max_text_width   + ' |')
print(' ' * left_margin + '+' + '-' * (box_width-2) +  '+')
print()
