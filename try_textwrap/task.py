number = 0
while number <= 35:
    number = int(input('Enter your number of characters per line and this number must be greater than 35: '))

with open('text.txt', 'r', encoding='utf8') as t:
    with open('rewrited_text.txt', 'w', encoding='utf8') as rewrited_t:
        next_symbol = True
        while next_symbol:
            chunk = t.read(number)
            next_symbol = t.read(1)
            t.seek(t.tell() - 1)
            if chunk == '':
                break

            if len(chunk) < number:
                rewrited_t.write(chunk)
            elif '\n' in chunk[1:number-2]:
                ind = chunk.index('\n')
                chunk = chunk[:ind]
                rewrited_t.write(chunk + '\n')
                # Return the cursor back:
                lost_symbols = number - len(chunk)
                t.seek(t.tell() - lost_symbols + 1)
            elif next_symbol in (' ', '\n'):
                rewrited_t.write(chunk+'\n')
                t.seek(t.tell() + 1)
            elif chunk[number-1] in (' ', '\n'):
                if chunk[number-1] == ' ':
                    chunk = chunk[:number-1]  # --> 'text  text'
                    chunk = chunk.replace(' ', '  ', 1)  # --> 'text  text '
                    rewrited_t.write(chunk + '\n')
                elif chunk[number-1] == '\n':
                    chunk = chunk.replace(' ', '  ', 1)  # --> 'text  text '
                    rewrited_t.write(chunk)
            elif chunk[0] in (' ', '\n'):
                chunk = chunk[1:]
                chunk = chunk.replace(' ', '  ', 1)
                rewrited_t.write(chunk + '\n')
            else:
                ind = chunk.rfind(' ')
                chunk = chunk[:ind]
                lost_symbols = number - len(chunk)
                t.seek(t.tell() - lost_symbols + 1)  # +1 <--> not to start from a whitespace
                new_chunk = list(chunk)
                while lost_symbols != 0:
                    counter = 0
                    iter_chunk = tuple(new_chunk)
                    for i in range(len(iter_chunk)):
                        if lost_symbols == 0:
                            break
                        if iter_chunk[i] == ' ':
                            new_chunk.insert(counter, ' ')
                            counter += 1
                            lost_symbols -= 1
                        counter += 1
                new_chunk_str = ''
                for i in new_chunk:
                    new_chunk_str += i
                rewrited_t.write(new_chunk_str + '\n')
                del new_chunk, iter_chunk
print('We did it!')
